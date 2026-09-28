---
name: production
description: "Autonomous production readiness audit for software products. In one long run, it inventories every surface (web, API, webhooks, jobs, mobile, desktop, extension, CLI/SDK, messaging, docs) and assesses 32 parts with about 600 evidence-backed checks: functional, UX, design, accessibility, content, localization, compatibility, performance, reliability, observability, infrastructure, cost, engineering, security, identity, data, privacy, safety, AI, API, billing, messaging, support, analytics, SEO, brand, legal, mobile, desktop, extension, package and launch. It returns a structured payload and report that rank parts and surfaces by risk and give a go/no-go recommendation per surface and overall. Use it when asked whether a product, app, site, release or feature is production-ready, launch-ready or safe to ship; for readiness, launch, security, accessibility, privacy or compliance audits; for pre-launch checklists, go/no-go decisions and post-launch health checks; or for a prioritized list of gaps and blockers."
license: MIT
metadata:
  author: miisodev
  version: "1.0.1"
---

# Production readiness

An autonomous audit that answers one question with evidence: **can this product face real users now, and if not, what stands in the way?** It runs start to finish without stopping to ask, covers every surface and every applicable part of the product, and returns a structured payload plus a report. The report ranks each part and each surface by risk and gives a go/no-go decision for each surface and for the whole product.

The skill is independent of stack, vendor, region and agent harness. Tools and vendors named in the references are examples. Use what the project actually runs on.

## How the run works

This is designed to be one long, thorough run. Work through the phases below until every applicable check has a recorded result, then produce the deliverables. Do not stop partway to ask questions. When something is ambiguous, make the most reasonable assumption, record it in `run.assumptions`, and continue. A wrong assumption stated plainly is easy for the owner to correct. A run that stops halfway gives them nothing.

1. **Scope.** Choose the profile from the request (table below); default to **Pre-Launch Gate** for an unlaunched product and **Full Audit** for a live one. Establish what the product is, who uses it and where (`product.markets` drives privacy, tax, accessibility and consumer law), and what environments you can reach. Then reconnoitre the project for its stated intent, wherever it lives and whatever it is called: a blueprint, PRD, spec, business plan, brand brief, agent instruction files (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md` and the like, which often point at the rest), READMEs, docs, the pricing page and store listings. Assume no folder or file name. Record in `run.assumptions` what you found and used, and where. The strongest statement of requirements found is the standard for the functional part; statements of pricing, brand and stack inform billing, cost, brand and infrastructure. Where there is none, derive the standard from the product's public claims.
2. **Inventory surfaces.** Find every surface the product exposes (catalogue below) from the repository, deploy configuration, DNS, app manifests, package manifests and docs. Record each in `surfaces` with a stable id, and mark which are core.
3. **Decide applicability.** For each of the 32 parts, decide whether it applies. Record every part that does not apply in `parts` with the reason. Anything not declared inapplicable must be assessed.
4. **Gather evidence.** Automated evidence first: run the project's own build, tests, linters and scanners, then the checks each reference lists. Then manual evidence: read code, walk journeys, probe endpoints and inspect pages, within the safety limits below. Each part's reference file lists its evidence sources.
5. **Assess every check.** For each applicable part, read its reference file and record a result for **every** check on every surface it applies to: `pass`, `partial`, `fail`, `not_verified` or `not_applicable` (with the reason in `evidence`). Omitting a check hides a gap. Apply the part's severity notes to set severity, and set `core_flow: true` where the check protects authentication, payment, the primary value action or data integrity. Add custom checks (`SEC-C01`) for risks the references do not cover.
6. **Write findings.** Every failing or partial check of Critical or High severity belongs to a finding, and lower-severity ones can be grouped into findings too. Findings carry evidence, user and business impact, a specific recommendation, effort (S/M/L), an owner ("unassigned" unless one is known; never invent names) and how the fix will be validated. Write the executive `summary` last.
7. **Score and render.** Save the payload as `production-readiness.json` in the output folder (below) and run `python <this skill's directory>/scripts/readiness.py <output folder>/production-readiness.json`. The script validates the payload and warns about checks you skipped. It computes scores, coverage, risk rankings and decisions, and writes `production-readiness.md` and `production-readiness.result.json`. Fix any errors and act on the warnings, then run it again.
8. **Return.** Reply with the decision, the top blockers, the items that must be verified by a person, the surface and part rankings (the top of each table is enough), and the paths to the report and payload.

For a run this size, use parallel sub-agents if the harness offers them. Parts are independent, and each sub-agent can take a group of parts and return check results for the payload. Merge the results into one payload before scoring.

### Where outputs go

Write to `production-readiness/<YYYY-MM-DD>/` at the repository root unless the user names a location. The audit is read-only by default: change no code, configuration or data unless the user asked for remediation. When they did, fix after the audit is recorded, then re-run the affected checks.

### Safety limits

Audits touch live systems, and in an autonomous run nobody is there to approve risky steps. Unless the user has explicitly authorised it for a specific environment:

- no load tests, fuzzers, vulnerability scanners or exploitation attempts against production or shared environments
- no cross-account testing with real users' accounts or data: create test accounts, or use a non-production environment
- no real payments, real messages to real people, or production data changes
- no changes to DNS, secrets, provider settings or billing

Read-only probes of production are fine: fetching public pages, headers, `robots.txt`, DNS and TLS. What these limits prevent you from verifying becomes `not_verified`, with the evidence field saying what would verify it. The decision logic treats unverified Critical items as a HOLD, which is correct: the owner then knows exactly what a person must check.

## Evidence standard

- A `pass` cites evidence: a command and its output, a test result, `file:line`, a measurement, a response header, or a named manual step. "Looks fine" is not evidence.
- Mark what you **observed** (ran, saw, measured) separately from what you **inferred** from code, and what is only **documented** (a policy says so). Use `evidence_type`.
- Anything you could not check is `not_verified`. It is never silently passed and never marked `not_applicable` to make the numbers look better.
- Prefer the project's own tooling and data (its tests, CI, analytics, monitoring) over generic tools.
- Legal, tax and regulatory checks are engineering assessments, not legal advice. Route ambiguity to counsel in the recommendation.

## Severity

| Severity | Meaning | Examples |
|---|---|---|
| **Critical** | Blocks core use, exposes user data, loses money, creates serious legal exposure, or cannot be recovered from | Cross-tenant data access; secrets in a client or binary; payments not granting access; no backups; trackers firing without required consent; auth emails not delivered |
| **High** | Major friction, degradation or material risk | No brute-force protection; no error tracking; core page far too slow; no dunning |
| **Medium** | Noticeable, not blocking | Missing empty states off core flows; minor accessibility gaps; warm queries unindexed |
| **Low** | Polish | Copy refinements, metadata, minor inconsistency |

Each check lists a default severity. The part's severity notes say when to raise or lower it. Severity follows impact on this product, not how hard the fix is.

## Decision logic

The script applies these rules. They are listed here so the results can be explained, and applied by hand if Python is unavailable.

| Condition (per surface, per part, and overall) | Status | Decision |
|---|---|---|
| An open Critical, or an open High with `core_flow`, not risk-accepted | ❌ Blocked | **NO-GO** |
| Otherwise, a Critical (or core-flow High) that is `not_verified`, or an applicable part with no results | ⬜ Hold | **HOLD**: verify the listed items, then re-run |
| Otherwise, an open High outside core flows, or any accepted risk | ⚠️ Conditional | **GO WITH CONDITIONS** |
| Otherwise | ✅ Ready | **GO** |

Scores (0–100) weight checks by severity (Critical 10, High 5, Medium 2, Low 1; partial earns half) over verified checks. Coverage is the verified share of applicable weight. Rankings put the most at-risk first: status, then score, then coverage. Scores are for comparison and prioritisation. The decision comes from the rules above, never from a score threshold.

Risk acceptance belongs to the owner. Record `risk_accepted_by` only when the owner has accepted a specific risk in writing (usually on a re-run). Never accept a risk on their behalf.

## Scope profiles

| Profile | When | Parts (`run.parts_in_scope`) |
|---|---|---|
| `pre-launch-gate` | First production launch | All applicable |
| `full-audit` | Periodic deep review of a live product | All applicable |
| `release-gate` | A major release on a live product | functional, security, identity, data, privacy, api, billing (if touched), reliability, observability, launch, plus the experience parts for changed surfaces |
| `design-review` | "Is this UI finished?" | functional, ux, design, accessibility, content, localization, compatibility |
| `spot-audit` | One concern | The relevant part(s) only |
| `post-launch-health-check` | 1–4 weeks after launch | performance, reliability, observability, cost, analytics, billing, support, messaging |

## Surfaces

Record every one that exists. A finding can span several surfaces, and product-wide checks (policies, organisation-level settings) use `"surface": "all"`.

| Kind | Examples |
|---|---|
| `marketing-site` | Landing pages, pricing, blog |
| `web-app` | The signed-in product in a browser, PWAs |
| `admin-console` | Internal admin, back office, support tooling |
| `public-api` | REST/GraphQL APIs used by customers or apps |
| `webhooks` | Inbound provider webhooks, outbound customer webhooks |
| `background-jobs` / `data-pipeline` | Queues, cron, ETL, sync |
| `mobile-app` | iOS, Android, cross-platform apps |
| `desktop-app` | Windows, macOS, Linux apps |
| `extension` | Browser extensions, platform plugins and marketplace apps |
| `cli` / `sdk-library` | Anything installed from a registry |
| `messaging` | Transactional and marketing email, push, SMS |
| `docs` / `store-listing` / `integration` | Help centre and developer docs; app-store and marketplace listings; third-party integrations |

## Parts

Each reference file follows the same structure: purpose, check prefix, the surfaces it applies to, evidence sources, a check table (ID, check, verify, default severity) and severity notes. Read the file for every applicable part. There are 604 checks across the 32 parts.

| Group | Part | Prefix | Reference |
|---|---|---|---|
| Experience | Functional | `FUN` | `references/functional-audit.md` |
| | UX | `UX` | `references/ux-audit.md` |
| | Design | `DES` | `references/design-audit.md` |
| | Accessibility | `A11` | `references/accessibility-audit.md` |
| | Content | `CON` | `references/content-audit.md` |
| | Localization | `LOC` | `references/localization-audit.md` |
| | Compatibility | `CMP` | `references/compatibility-audit.md` |
| Quality & operations | Performance | `PRF` | `references/performance-audit.md` |
| | Reliability | `REL` | `references/reliability-audit.md` |
| | Observability | `OBS` | `references/observability-audit.md` |
| | Infrastructure | `INF` | `references/infrastructure-audit.md` |
| | Cost | `CST` | `references/cost-audit.md` |
| | Engineering | `ENG` | `references/engineering-audit.md` |
| Trust | Security | `SEC` | `references/security-audit.md` |
| | Identity | `IDN` | `references/identity-audit.md` |
| | Data | `DAT` | `references/data-audit.md` |
| | Privacy | `PRV` | `references/privacy-audit.md` |
| | Safety | `SAF` | `references/safety-audit.md` |
| | AI | `AIF` | `references/ai-audit.md` |
| Business | API | `API` | `references/api-audit.md` |
| | Billing | `BIL` | `references/billing-audit.md` |
| | Messaging | `MSG` | `references/messaging-audit.md` |
| | Support | `SUP` | `references/support-audit.md` |
| | Analytics | `ANL` | `references/analytics-audit.md` |
| | SEO | `SEO` | `references/seo-audit.md` |
| | Brand | `BRD` | `references/brand-audit.md` |
| | Legal | `LGL` | `references/legal-audit.md` |
| Platform surfaces | Mobile | `MOB` | `references/mobile-audit.md` |
| | Desktop | `DSK` | `references/desktop-audit.md` |
| | Extension | `EXT` | `references/extension-audit.md` |
| | Package | `PKG` | `references/package-audit.md` |
| Final gate | Launch | `LCH` | `references/launch-audit.md` |

## The payload

`assets/payload.schema.json` defines the payload, and `assets/example-payload.json` is a small illustrative example of its shape. The example is deliberately truncated: a real payload has a result for every applicable check. In brief:

- `product`: name, description, types, markets
- `run`: date, profile, `parts_in_scope`, environments examined, assumptions, limitations
- `summary`: the executive summary, written last
- `surfaces`: id, name, kind, location, core
- `parts`: the parts that do not apply, with reasons
- `checks`: one result per check per surface, with status, severity, `core_flow`, evidence and `evidence_type`
- `findings`: grouped issues with impact, recommendation, effort, owner and validation

The script adds `results`: the decision, overall score and coverage, ranked parts and surfaces with status, score, coverage, open counts and checks assessed, plus the lists of blockers, items to verify, conditions and accepted risks. This combined JSON is the structured return for other tools. The Markdown report is for people.
