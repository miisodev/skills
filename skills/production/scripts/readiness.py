"""Score, rank and gate a production readiness payload, then render the report.
The auditing agent records judgments (each check's status, severity and
evidence, plus findings) in a JSON payload. This script does the arithmetic:
validation, per-part and per-surface scores, rankings, the go/no-go decision,
and a Markdown report. Standard library only; Python 3.8+.

Usage:
    python readiness.py PAYLOAD.json [--md REPORT.md] [--json RESULT.json]

Without --md/--json, writes <payload>.md and <payload>.result.json next to the
payload. Exit code 0 on success, 1 on validation errors, 2 on usage errors.
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

SCHEMA_VERSION = "1.1"
SUPPORTED_SCHEMA_VERSIONS = ("1.0", "1.1")
STATUSES = ("pass", "partial", "fail", "not_verified", "not_applicable")
SEVERITIES = ("critical", "high", "medium", "low")
WEIGHT = {"critical": 10, "high": 5, "medium": 2, "low": 1}
CREDIT = {"pass": 1.0, "partial": 0.5, "fail": 0.0}
EFFORT_ORDER = {"S": 0, "M": 1, "L": 2}
PRODUCT_WIDE = "all"

PARTS = {  # prefix -> (part id, display name)
    "FUN": ("functional", "Functional"), "UX": ("ux", "UX"), "DES": ("design", "Design"),
    "A11": ("accessibility", "Accessibility"), "CON": ("content", "Content"),
    "LOC": ("localization", "Localization"), "CMP": ("compatibility", "Compatibility"),
    "PRF": ("performance", "Performance"), "REL": ("reliability", "Reliability"),
    "OBS": ("observability", "Observability"), "INF": ("infrastructure", "Infrastructure"),
    "CST": ("cost", "Cost"), "ENG": ("engineering", "Engineering"),
    "SEC": ("security", "Security"), "IDN": ("identity", "Identity"), "DAT": ("data", "Data"),
    "PRV": ("privacy", "Privacy"), "SAF": ("safety", "Safety"), "AIF": ("ai", "AI"),
    "API": ("api", "API"), "BIL": ("billing", "Billing"), "MSG": ("messaging", "Messaging"),
    "SUP": ("support", "Support"), "ANL": ("analytics", "Analytics"), "SEO": ("seo", "SEO"),
    "BRD": ("brand", "Brand"), "LGL": ("legal", "Legal"), "MOB": ("mobile", "Mobile"),
    "DSK": ("desktop", "Desktop"), "EXT": ("extension", "Extension"),
    "PKG": ("package", "Package"), "LCH": ("launch", "Launch"),
    "MCP": ("mcp", "MCP"), "AGT": ("agent", "Agent execution"),
    "DEP": ("deployment", "Deployment and operability"),
    "SYN": ("sync", "Offline and synchronization"),
    "RTM": ("realtime", "Real-time and event systems"),
    "DEV": ("device", "Device and embedded software"),
    "SCH": ("supply-chain", "Software supply chain"),
}
PART_BY_ID = {pid: (prefix, name) for prefix, (pid, name) in PARTS.items()}
ID_RE = re.compile(r"^([A-Z][A-Z0-9]{1,3})-(C?\d{2,3})$")

STATUS_ORDER = {"blocked": 0, "hold": 1, "unassessed": 2, "conditional": 3, "ready": 4, "not_applicable": 5}
STATUS_LABEL = {
    "blocked": "❌ Blocked", "hold": "⬜ Hold", "unassessed": "⬜ Unassessed",
    "conditional": "⚠️ Conditional", "ready": "✅ Ready", "not_applicable": "— N/A",
}
DECISION_LABEL = {
    "NO_GO": "NO-GO", "HOLD": "HOLD (verification required)",
    "GO_WITH_CONDITIONS": "GO WITH CONDITIONS", "GO": "GO",
}


def load_registry(ref_dir):
    """Map check ID -> part id from the reference files, if they are present.

    Matches the same ID grammar as ID_RE (2-3 digit numeric forms); custom
    `C`-prefixed IDs are payload-local and are never expected checks.
    """
    registry = {}
    if not ref_dir.is_dir():
        return registry
    for f in ref_dir.glob("*-audit.md"):
        for m in re.finditer(r"^\| ([A-Z][A-Z0-9]{1,3}-(\d{2,3})) \|", f.read_text(encoding="utf-8"), re.M):
            prefix = m.group(1).split("-")[0]
            if prefix in PARTS:
                registry[m.group(1)] = PARTS[prefix][0]
    return registry


def validate(p, registry):
    errors, warnings = [], []
    version = p.get("schema_version")
    if version not in SUPPORTED_SCHEMA_VERSIONS:
        errors.append(f"schema_version is {version!r}; supported: {', '.join(SUPPORTED_SCHEMA_VERSIONS)}")
    strict = version == "1.1"
    for key in ("product", "run", "surfaces", "checks"):
        if key not in p:
            errors.append(f"missing top-level field: {key}")
    if errors:
        return errors, warnings
    scope = p["run"].get("parts_in_scope", "all")
    if scope != "all" and (not isinstance(scope, list) or any(x not in PART_BY_ID for x in scope)):
        errors.append(f"run.parts_in_scope must be \"all\" or a list of part ids from: {sorted(PART_BY_ID)}")
    sscope = p["run"].get("surfaces_in_scope", "all")
    declared = {s.get("id") for s in p["surfaces"]}
    if sscope != "all" and (not isinstance(sscope, list) or not sscope
                            or any(x not in declared for x in sscope)):
        errors.append(f"run.surfaces_in_scope must be \"all\" or a non-empty list of declared surface ids")
    for x in p.get("parts", []):
        if x.get("id") not in PART_BY_ID:
            errors.append(f"parts: unknown part id {x.get('id')!r}")
        elif x.get("applicable") is False and not (x.get("reason") or "").strip():
            errors.append(f"parts: {x.get('id')} is marked not applicable without a reason")
    surface_ids = {s.get("id") for s in p["surfaces"]}
    if PRODUCT_WIDE in surface_ids:
        errors.append(f"surface id {PRODUCT_WIDE!r} is reserved for product-wide checks")
    for s in p["surfaces"]:
        if not s.get("id") or not s.get("name"):
            errors.append(f"surface needs id and name: {s}")
    seen = set()
    for i, c in enumerate(p["checks"]):
        where = f"checks[{i}] ({c.get('id', '?')})"
        m = ID_RE.match(str(c.get("id", "")))
        if not m or m.group(1) not in PARTS:
            errors.append(f"{where}: id must look like SEC-04 (or SEC-C01 for a custom check) with a known prefix")
            continue
        if c.get("status") not in STATUSES:
            errors.append(f"{where}: status must be one of {STATUSES}")
        if c.get("status") != "not_applicable" and c.get("severity") not in SEVERITIES:
            errors.append(f"{where}: severity must be one of {SEVERITIES}")
        if c.get("status") == "not_applicable" and not (c.get("evidence") or "").strip():
            errors.append(f"{where}: not_applicable requires a reason in evidence")
        if strict and c.get("status") in ("pass", "partial", "fail") and not (c.get("evidence") or "").strip():
            errors.append(f"{where}: {c['status']} without evidence (schema 1.1)")
        surface = c.get("surface", PRODUCT_WIDE)
        if surface != PRODUCT_WIDE and surface not in surface_ids:
            errors.append(f"{where}: unknown surface {surface!r}")
        key = (c["id"], surface)
        if key in seen:
            errors.append(f"{where}: duplicate result for this check and surface")
        seen.add(key)
        if registry and not m.group(2).startswith("C") and c["id"] not in registry:
            warnings.append(f"{where}: id not found in the reference files (typo, or use a custom id like {m.group(1)}-C01)")
        if c.get("status") in ("pass", "partial", "fail") and not c.get("evidence") and not strict:
            warnings.append(f"{where}: {c['status']} without evidence")
        if c.get("status") in ("fail", "partial") and c.get("risk_accepted_by") and strict:
            errors.append(f"{where}: schema 1.1 records risk acceptance as risk_acceptance "
                          f"{{by, reference, date}}, not risk_accepted_by")
        if c.get("status") in ("fail", "partial") and c.get("risk_acceptance"):
            ra = c["risk_acceptance"]
            if not (isinstance(ra, dict) and (ra.get("by") or "").strip()
                    and (ra.get("reference") or "").strip() and (ra.get("date") or "").strip()):
                errors.append(f"{where}: risk_acceptance needs by, reference and date")
    if registry:
        recorded = {c.get("id") for c in p["checks"]}
        na = {x.get("id") for x in p.get("parts", []) if x.get("applicable") is False}
        for part in sorted(set(registry.values()) - na):
            if scope != "all" and part not in scope:
                continue
            ids = {cid for cid, pt in registry.items() if pt == part}
            missing = ids - recorded
            if missing and len(missing) < len(ids):
                warnings.append(f"part {part}: {len(missing)} of {len(ids)} checks have no result "
                                f"(the decision holds until they are assessed or recorded not_applicable with a reason): "
                                f"{', '.join(sorted(missing))}")
    result_keys = {(c.get("id"), c.get("surface", PRODUCT_WIDE)) for c in p["checks"]}
    by_id = defaultdict(list)
    for c in p["checks"]:
        by_id[c.get("id")].append(c.get("surface", PRODUCT_WIDE))
    covered = set()
    for f in p.get("findings", []):
        if f.get("severity") not in SEVERITIES:
            errors.append(f"finding {f.get('id')}: severity must be one of {SEVERITIES}")
        for ref in f.get("checks", []):
            if isinstance(ref, dict):
                cid, sid = ref.get("id"), ref.get("surface", PRODUCT_WIDE)
                if (cid, sid) not in result_keys:
                    errors.append(f"finding {f.get('id')}: references check {cid}@{sid} with no recorded result")
                covered.add((cid, sid))
                continue
            ref = str(ref)
            if "@" in ref:
                cid, _, sid = ref.partition("@")
                sid = PRODUCT_WIDE if sid == "all" else sid
                if (cid, sid) in result_keys:
                    covered.add((cid, sid))
                else:
                    errors.append(f"finding {f.get('id')}: references check {cid}@{sid} with no recorded result")
                continue
            sid = f.get("surfaces", [PRODUCT_WIDE])[0] if f.get("surfaces") else PRODUCT_WIDE
            if (ref, sid) in result_keys:
                covered.add((ref, sid))
            elif len(by_id.get(ref, [])) == 1:
                covered.add((ref, by_id[ref][0]))
            elif not by_id.get(ref):
                errors.append(f"finding {f.get('id')}: references check {ref} with no recorded result")
            else:
                warnings.append(f"finding {f.get('id')}: references check {ref} ambiguous across surfaces "
                                f"{', '.join(by_id[ref])}; use {ref}@<surface>")
    for c in p["checks"]:
        if c.get("status") in ("fail", "partial") and c.get("severity") in ("critical", "high") \
                and (c["id"], c.get("surface", PRODUCT_WIDE)) not in covered:
            warnings.append(f"{c['id']}@{c.get('surface', PRODUCT_WIDE)}: open {c['severity']} check has no finding")
    return errors, warnings


def is_open(c):
    return c["status"] in ("fail", "partial") and not (c.get("risk_acceptance") or c.get("risk_accepted_by"))


def is_blocking(c):
    return is_open(c) and (c["severity"] == "critical" or (c["severity"] == "high" and c.get("core_flow")))


def needs_verification(c):
    return c["status"] == "not_verified" and (
        c["severity"] == "critical" or (c["severity"] == "high" and c.get("core_flow")))


def summarize(checks):
    """Score and status for one group of check results (a part or a surface)."""
    applicable = [c for c in checks if c["status"] != "not_applicable"]
    if not applicable:
        return {"status": "not_applicable", "score": None, "coverage": None, "open": {}, "checks": 0}
    verified = [c for c in applicable if c["status"] in CREDIT]
    earned = sum(WEIGHT[c["severity"]] * CREDIT[c["status"]] for c in verified)
    possible = sum(WEIGHT[c["severity"]] for c in verified)
    total = sum(WEIGHT[c["severity"]] for c in applicable)
    open_counts = {s: sum(1 for c in applicable if is_open(c) and c["severity"] == s) for s in SEVERITIES}
    accepted = [c for c in applicable if c["status"] in ("fail", "partial") and (c.get("risk_acceptance") or c.get("risk_accepted_by"))]
    if any(is_blocking(c) for c in applicable):
        status = "blocked"
    elif any(needs_verification(c) for c in applicable):
        status = "hold"
    elif open_counts["high"] or accepted:
        status = "conditional"
    else:
        status = "ready"
    return {
        "status": status,
        "score": round(100 * earned / possible) if possible else None,
        "coverage": round(100 * possible / total) if total else None,
        "open": open_counts,
        "unverified_critical": sum(1 for c in applicable if needs_verification(c)),
        "accepted_risks": len(accepted),
        "checks": len(applicable),
    }


def rank(rows):
    def key(r):
        s = r["summary"]
        return (STATUS_ORDER[s["status"]], -1 if s["score"] is None else s["score"], s["coverage"] or 0)
    ordered = sorted(rows, key=key)
    for i, r in enumerate(ordered, 1):
        r["risk_rank"] = i
    return ordered


def decide(groups):
    statuses = {g["summary"]["status"] for g in groups}
    if "blocked" in statuses:
        return "NO_GO"
    if statuses & {"hold", "unassessed"}:
        return "HOLD"
    if "conditional" in statuses:
        return "GO_WITH_CONDITIONS"
    return "GO"


def compute(p, registry):
    for c in p["checks"]:
        c.setdefault("surface", PRODUCT_WIDE)
        c["part"] = PARTS[c["id"].split("-")[0]][0]
    na_parts = {x["id"]: x.get("reason", "") for x in p.get("parts", []) if x.get("applicable") is False}
    in_scope = p["run"].get("parts_in_scope", "all")
    out_of_scope = set() if in_scope == "all" else set(PART_BY_ID) - set(in_scope)
    sscope = p["run"].get("surfaces_in_scope", "all")
    scoped = sscope != "all"
    in_scope_surfaces = set(sscope) if scoped else None

    by_part = defaultdict(list)
    for c in p["checks"]:
        by_part[c["part"]].append(c)
    defined = defaultdict(set)
    for cid, part in registry.items():
        defined[part].add(cid)

    parts = []
    missing_checks = []
    for part_id, (prefix, name) in sorted(PART_BY_ID.items(), key=lambda kv: kv[1][1]):
        if part_id in out_of_scope and part_id not in by_part:
            continue
        if part_id in na_parts:
            parts.append({"id": part_id, "name": name, "prefix": prefix, "reason": na_parts[part_id],
                          "summary": {"status": "not_applicable", "score": None, "coverage": None, "open": {}, "checks": 0}})
            continue
        results = by_part.get(part_id, [])
        summary = summarize(results) if results else {
            "status": "unassessed", "score": None, "coverage": None, "open": {}, "checks": 0}
        assessed = {c["id"] for c in results if not c["id"].split("-")[1].startswith("C")}
        expected = defined[part_id]
        # Fail-closed completeness: every expected check in an in-scope applicable
        # part needs a result. A missing check is unassessed and gates the decision.
        missing = sorted(expected - assessed) if expected else []
        if missing:
            if summary["status"] in ("ready", "conditional", "not_applicable"):
                summary["status"] = "unassessed"
            summary["missing"] = len(missing)
            summary["assessed"] = f"{len(assessed & expected)}/{len(expected)}" if expected else None
            missing_checks.extend({"id": mid, "part": part_id} for mid in missing)
            parts.append({"id": part_id, "name": name, "prefix": prefix, "summary": summary})
            continue
        summary["assessed"] = f"{len(assessed & expected)}/{len(expected)}" if expected else None
        parts.append({"id": part_id, "name": name, "prefix": prefix, "summary": summary})

    surfaces = []
    for s in p["surfaces"]:
        if scoped and s["id"] not in in_scope_surfaces:
            continue
        results = [c for c in p["checks"] if c["surface"] == s["id"]]
        surfaces.append({"id": s["id"], "name": s["name"], "kind": s.get("kind", ""),
                         "core": s.get("core", False),
                         "summary": summarize(results) if results else {
                             "status": "unassessed", "score": None, "coverage": None, "open": {}, "checks": 0}})
    wide = [c for c in p["checks"] if c["surface"] == PRODUCT_WIDE]
    if wide:
        surfaces.append({"id": PRODUCT_WIDE, "name": "Product-wide", "kind": "product-wide", "core": True,
                         "summary": summarize(wide)})
    out_of_scope_surfaces = [s["id"] for s in p["surfaces"] if scoped and s["id"] not in in_scope_surfaces]
    for s in surfaces:
        s["decision"] = decide([s]) if s["summary"]["status"] != "not_applicable" else None

    applicable_parts = [x for x in parts if x["summary"]["status"] != "not_applicable"]
    overall = summarize(p["checks"])
    decision = decide(applicable_parts + surfaces)
    if scoped:
        decision = f"{decision} (scoped)"
    blockers = [c for c in p["checks"] if is_blocking(c)]
    to_verify = [c for c in p["checks"] if needs_verification(c)]
    conditions = [c for c in p["checks"] if is_open(c) and c["severity"] == "high" and not is_blocking(c)]
    accepted = [c for c in p["checks"] if c["status"] in ("fail", "partial")
                and (c.get("risk_acceptance") or c.get("risk_accepted_by"))]
    return {
        "decision": decision,
        "decision_scope": "scoped" if scoped else "product",
        "overall": overall,
        "parts": rank(applicable_parts) + [x for x in parts if x not in applicable_parts],
        "surfaces": rank(surfaces),
        "blockers": [c["id"] + "@" + c["surface"] for c in blockers],
        "verification_required": [c["id"] + "@" + c["surface"] for c in to_verify],
        "conditions": [c["id"] + "@" + c["surface"] for c in conditions],
        "accepted_risks": [{"check": c["id"] + "@" + c["surface"],
                            "by": (c.get("risk_acceptance") or {}).get("by") or c.get("risk_accepted_by", ""),
                            "reference": (c.get("risk_acceptance") or {}).get("reference", ""),
                            "date": (c.get("risk_acceptance") or {}).get("date", "")} for c in accepted],
        "missing_checks": missing_checks,
        "unassessed_parts": [x["id"] for x in parts if x["summary"]["status"] == "unassessed"],
        "out_of_scope_parts": sorted(out_of_scope - set(by_part)),
        "out_of_scope_surfaces": out_of_scope_surfaces,
    }


def fmt(v, suffix=""):
    return "—" if v is None else f"{v}{suffix}"


def open_str(o):
    return " / ".join(str(o.get(s, 0)) for s in SEVERITIES) if o else "—"


def render(p, r):
    prod, run = p["product"], p["run"]
    checks = {(c["id"], c["surface"]): c for c in p["checks"]}
    surf_names = {s["id"]: s["name"] for s in p["surfaces"]}
    surf_names[PRODUCT_WIDE] = "Product-wide"
    finding_by_check = defaultdict(list)
    for f in p.get("findings", []):
        for ref in f.get("checks", []):
            if isinstance(ref, dict):
                finding_by_check[(ref.get("id"), ref.get("surface", PRODUCT_WIDE))].append(f.get("id", ""))
            else:
                ref = str(ref)
                if "@" in ref:
                    cid, _, sid = ref.partition("@")
                    finding_by_check[(cid, PRODUCT_WIDE if sid == "all" else sid)].append(f.get("id", ""))
                else:
                    for c in p["checks"]:
                        if c["id"] == ref:
                            finding_by_check[(c["id"], c["surface"])].append(f.get("id", ""))
    L = []
    add = L.append
    scoped = r.get("decision_scope") == "scoped"
    title_scope = "scoped audit" if scoped else "production readiness"
    add(f"# {prod.get('name', 'Product')}: {title_scope}")
    add("")
    decision_text = DECISION_LABEL[r["decision"].split(" (")[0]] + (" (scoped)" if scoped else "")
    add(f"**Decision: {decision_text}** · Profile: {run.get('profile', '—')} · "
        f"Date: {run.get('date', '—')} · Overall score {fmt(r['overall']['score'])}/100 · "
        f"Verified coverage {fmt(r['overall']['coverage'], '%')}")
    add("")
    if scoped:
        add("This is a **scoped result**: it covers only the parts and surfaces in scope. "
            "It is not a whole-product readiness decision.")
        add("")
    if p.get("summary"):
        add("## Summary")
        add("")
        add(p["summary"].strip())
        add("")
    add("## Decision record")
    add("")
    add("```")
    add(f"Decision:        {decision_text}")
    add(f"Date:            {run.get('date', '')}")
    add(f"Scope profile:   {run.get('profile', '')}")
    add(f"Scope:           parts {run.get('parts_in_scope', 'all')}; surfaces {run.get('surfaces_in_scope', 'all')}")
    if scoped:
        add("Readiness:       NOT ASSESSED for the whole product (scoped run)")
    add(f"Blockers:        {len(r['blockers'])}")
    add(f"To verify:       {len(r['verification_required'])} critical/core items not yet verified")
    add(f"Missing:         {len(r['missing_checks'])} expected checks with no result (unassessed)")
    add(f"Conditions:      {len(r['conditions'])} open high-severity items outside core flows")
    add(f"Risk accepted:   {len(r['accepted_risks'])}")
    if r["unassessed_parts"]:
        add(f"Unassessed:      {', '.join(r['unassessed_parts'])}")
    if r.get("out_of_scope_surfaces"):
        add(f"Out of scope:    surfaces {', '.join(r['out_of_scope_surfaces'])}")
    add(f"Re-review:       {run.get('re_review', 'required before launch' if not r['decision'].startswith('GO') else 'at next release')}")
    add("```")
    add("")
    add("Decision rules: every expected check in an in-scope applicable part needs a result — a missing check is "
        "unassessed and holds the decision. Any open Critical, or open High in a core flow, is NO-GO. Critical or "
        "core-flow items not yet verified HOLD until verified. Other open High items make it GO WITH CONDITIONS.")
    add("")

    add("## Surfaces, ranked by risk")
    add("")
    add("| Rank | Surface | Kind | Status | Decision | Score | Coverage | Open C / H / M / L | To verify |")
    add("|---|---|---|---|---|---|---|---|---|")
    for s in r["surfaces"]:
        sm = s["summary"]
        add(f"| {s['risk_rank']} | {s['name']}{' (core)' if s.get('core') and s['id'] != PRODUCT_WIDE else ''} | "
            f"{s['kind']} | {STATUS_LABEL[sm['status']]} | {DECISION_LABEL.get(s['decision'], '—') if s['decision'] else '—'} | "
            f"{fmt(sm['score'])} | {fmt(sm['coverage'], '%')} | {open_str(sm['open'])} | {sm.get('unverified_critical', 0)} |")
    add("")

    add("## Parts, ranked by risk")
    add("")
    add("| Rank | Part | Status | Score | Coverage | Checks assessed | Open C / H / M / L | To verify |")
    add("|---|---|---|---|---|---|---|---|")
    for x in r["parts"]:
        sm = x["summary"]
        if sm["status"] == "not_applicable":
            continue
        add(f"| {x['risk_rank']} | {x['name']} (`{x['prefix']}`) | {STATUS_LABEL[sm['status']]} | {fmt(sm['score'])} | "
            f"{fmt(sm['coverage'], '%')} | {fmt(sm.get('assessed'))} | {open_str(sm['open'])} | {sm.get('unverified_critical', 0)} |")
    if r.get("out_of_scope_parts"):
        add("")
        add("Out of scope for this profile: " + ", ".join(PART_BY_ID[x][1] for x in r["out_of_scope_parts"]))
    na = [x for x in r["parts"] if x["summary"]["status"] == "not_applicable"]
    if na:
        add("")
        add("Not applicable: " + "; ".join(f"{x['name']} ({x.get('reason') or 'no reason given'})" for x in na))
    add("")

    def check_line(key):
        cid, sid = key.split("@")
        c = checks[(cid, sid)]
        refs = finding_by_check.get((cid, sid))
        ref_note = f" · finding {'/'.join(refs)}" if refs else ""
        return (f"- **{cid}** · {surf_names.get(sid, sid)} · {c['severity']}{' · core flow' if c.get('core_flow') else ''}"
                f"{ref_note}: {c.get('evidence', '')}")

    if r["blockers"]:
        add("## Blockers")
        add("")
        L.extend(check_line(k) for k in r["blockers"])
        add("")
    if r["verification_required"]:
        add("## Must be verified before launch")
        add("")
        add("These could not be verified in this run. Each is Critical-risk or in a core flow, so the decision holds until a person verifies it.")
        add("")
        L.extend(check_line(k) for k in r["verification_required"])
        add("")
    if r["missing_checks"]:
        add("## Missing results (unassessed)")
        add("")
        add("These expected checks have no recorded result in this run. The decision holds until each is assessed "
            "or recorded as not applicable with a reason.")
        add("")
        by_part = defaultdict(list)
        for m in r["missing_checks"]:
            by_part[m["part"]].append(m["id"])
        for part, ids in sorted(by_part.items()):
            add(f"- **{part}**: {', '.join(ids)}")
        add("")

    findings = p.get("findings", [])
    findings = sorted(findings, key=lambda f: (
        SEVERITIES.index(f["severity"]),
        0 if any(checks.get((cid, s), {}).get("core_flow") for cid in f.get("checks", []) for s in f.get("surfaces", [PRODUCT_WIDE])) else 1,
        EFFORT_ORDER.get(f.get("effort"), 1)))
    if findings:
        add("## Findings")
        add("")
        for sev in SEVERITIES:
            group = [f for f in findings if f["severity"] == sev]
            if not group:
                continue
            add(f"### {sev.capitalize()} ({len(group)})")
            add("")
            for f in group:
                add(f"#### {f.get('id', '')} {f.get('title', '')}")
                add("")
                rows = [
                    ("Checks", ", ".join(str(x) if isinstance(x, dict) else x for x in f.get("checks", []))),
                    ("Surfaces", ", ".join(surf_names.get(s, s) for s in f.get("surfaces", [])) or "Product-wide"),
                    ("Evidence", f.get("evidence", "")),
                    ("User impact", f.get("user_impact", "")),
                    ("Business impact", f.get("business_impact", "")),
                    ("Recommendation", f.get("recommendation", "")),
                    ("Effort", f.get("effort", "")),
                    ("Owner", f.get("owner", "unassigned")),
                    ("Validation", f.get("validation", "")),
                ]
                for label, value in rows:
                    if value:
                        add(f"- **{label}:** {value}")
                add("")

        add("## Remediation plan")
        add("")
        add("| # | Finding | Severity | Effort | Owner |")
        add("|---|---|---|---|---|")
        table_sevs = ("critical", "high", "medium") if run.get("profile") == "full-audit" else ("critical", "high")
        for i, f in enumerate([f for f in findings if f["severity"] in table_sevs], 1):
            add(f"| {i} | {f.get('id', '')} {f.get('title', '')} | {f['severity']} | {f.get('effort', '—')} | {f.get('owner', 'unassigned')} |")
        add("")

    nv = [c for c in p["checks"] if c["status"] == "not_verified" and not needs_verification(c)]
    if nv:
        add("## Other items not verified")
        add("")
        for c in nv:
            add(f"- **{c['id']}** · {surf_names.get(c['surface'], c['surface'])} · {c['severity']}: {c.get('evidence', '')}")
        add("")
    if r["accepted_risks"]:
        add("## Accepted risks")
        add("")
        for a in r["accepted_risks"]:
            add(f"- {a['check']} accepted by {a['by']}")
        add("")
    add("## Scope, assumptions and limitations")
    add("")
    for label, key in (("Product", None), ("Assumptions", "assumptions"), ("Limitations", "limitations")):
        if key is None:
            bits = [prod.get("description", ""), "Types: " + ", ".join(prod.get("types", [])) if prod.get("types") else "",
                    "Markets: " + ", ".join(prod.get("markets", [])) if prod.get("markets") else "",
                    "Environments examined: " + ", ".join(run.get("environments_examined", [])) if run.get("environments_examined") else ""]
            add(f"- **{label}:** " + " · ".join(b for b in bits if b))
        elif run.get(key):
            add(f"- **{label}:**")
            for item in run[key]:
                add(f"  - {item}")
    add("")
    add("Scores weight each check by severity (critical 10, high 5, medium 2, low 1; partial earns half) over the checks "
        "that were verified. Coverage is the share of applicable weight that was verified. Ranks list the most at-risk first.")
    add("")
    add(f"---")
    add("")
    add(f"Payload schema {p.get('schema_version', '—')} · scored by the production skill's readiness.py "
        f"(Agent Skills spec) · this is an engineering assessment, not regulatory, functional-safety or platform "
        f"certification · the cited standards' editions and review dates are in the skill's "
        f"references/standards-sources.md.")
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("payload")
    ap.add_argument("--md", help="Markdown report path")
    ap.add_argument("--json", help="Result JSON path (payload plus computed results)")
    ap.add_argument("--references", help="References directory (default: ../references next to this script)")
    ap.add_argument("--fail-on", help="Comma-separated decisions that exit non-zero for CI, e.g. NO_GO,HOLD (default: no gating)")
    a = ap.parse_args(argv)
    src = Path(a.payload)
    try:
        p = json.loads(src.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"error: cannot read payload: {e}", file=sys.stderr)
        return 2
    ref_dir = Path(a.references) if a.references else Path(__file__).resolve().parent.parent / "references"
    registry = load_registry(ref_dir)
    errors, warnings = validate(p, registry)
    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        return 1
    results = compute(p, registry)
    md_path = Path(a.md) if a.md else src.with_suffix(".md")
    json_path = Path(a.json) if a.json else src.with_name(src.stem + ".result.json")
    md_path.write_text(render(p, results), encoding="utf-8")
    json_path.write_text(json.dumps({**p, "results": results}, indent=2, ensure_ascii=False), encoding="utf-8")
    decision = results["decision"]
    o = results["overall"]
    print(f"Decision: {decision} | score {fmt(o['score'])} | coverage {fmt(o['coverage'], '%')} | "
          f"blockers {len(results['blockers'])} | to verify {len(results['verification_required'])} | "
          f"conditions {len(results['conditions'])} | missing {len(results['missing_checks'])} | "
          f"unassessed parts {len(results['unassessed_parts'])}")
    print(f"Report: {md_path}\nResult: {json_path}")
    if a.fail_on:
        wanted = {x.strip().upper() for x in a.fail_on.split(",")}
        base = decision.split(" (")[0]
        if base in wanted:
            print(f"gate: decision {base} matches --fail-on {a.fail_on}", file=sys.stderr)
            return 4
    return 0


if __name__ == "__main__":
    sys.exit(main())
