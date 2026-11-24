# Changelog

All notable changes to these skills are documented here. Versions follow [Semantic Versioning](https://semver.org/): a major version changes a skill's structure or outputs in ways that break existing use, a minor version adds capability, and a patch fixes content.

## [2.0.5] - 2026-11-24

### Both skills

- Recreate the README with nothing hidden and a clear hierarchy: every install path is open — the Claude Code plugin marketplace, the ChatGPT and Codex routes and the manual copy each get their own section instead of a collapsed dropdown. No skill content changes; both versions move to 2.0.5 together.

## [2.0.4] - 2026-11-24

### Both skills

- Add the MCPRush badge before the skills.sh badge, and make the header's version line dynamic (it points at the Release badge and changelog instead of a hard-coded version that goes stale on every release — the line had drifted to v2.0.2 while the release was v2.0.3). No skill content changes; both versions move to 2.0.4 together.

## [2.0.3] - 2026-11-24

### Both skills

- Restructure the README to mirror the homepage flow: what it is, what it's for, quick setup, disclaimer, then access and support — with MCPRush ordered before skills.sh, the ChatGPT and Codex install routes documented, and the versioning detail folded into the header. No skill content changes; both versions move to 2.0.3 together.

## [2.0.2] - 2026-11-24

### Both skills

- Remove the shebang from `readiness.py` per Anthropic's plugin-directory validation (the script is invoked as `python readiness.py`; behavior unchanged). No skill content changes; both versions move to 2.0.2 together. Note: the directory accepts scripts only from Verified organizations — this release removes the refused `#!` marker; the org-verification or appeal decision stays with the owner.

## [2.0.1] - 2026-11-24

### Both skills

- Normalize the `.gitattributes` rule to `eol=lf` per Anthropic's plugin-directory validation, so installed files cannot differ from the validated source. No skill content changes; both versions move to 2.0.1 together.

## [2.0.0] - 2026-11-24

### production

- **Fail-closed completeness:** the scorer derives the expected checks from the reference tables and the payload's surfaces; a check with no result is unassessed and holds the decision, `not_applicable` requires a reason, and a run with no assessed checks is NOT ASSESSED — never GO. **This changes decisions: an incomplete audit no longer reports GO.**
- **Scope-qualified decisions:** `run.surfaces_in_scope` narrows a run to specific surfaces; a scoped result is marked as such in the decision, record and report title, and is never a whole-product readiness claim.
- **`--fail-on NO_GO,HOLD,GO_WITH_CONDITIONS`** exit policy for CI (default exit 0 preserved for human runs).
- **Registry parser** aligned to the full check-ID grammar (2–3 digit forms); 3-digit IDs no longer silently drop.
- **Schema 1.1:** evidence required for pass/partial/fail; structured `risk_acceptance` (`by`, `reference`, `date`) replacing the free-text `risk_accepted_by`; findings reference checks as `ID` or `ID@surface`. Schema 1.0 payloads still score under the 1.0 rules.
- **Remediate profile:** re-run a prior audit's failed, partial and unverified checks and produce a delta against the earlier result.
- **Execution-safety preflight** for the auditor itself; evidence redaction ban; `run-playbook.md` (sub-agent part bundles, checkpoint/resume, delta comparison) and `intent-discovery.md` (the shared blueprint↔production contract).
- Outcome-based rewrites: LCH-05 is the declared core journey in the target environment (SaaS example retained; CLI and pipeline variants named); DAT-07/PRF-13 judge sequential scans by workload and latency budget.
- Two new examples: `mini-go-example-payload.json` (smallest complete passing audit) and `self-hosted-example-payload.json` (N/A patterns, non-core not_verified); the web-app example is now complete (every check recorded).

### blueprint

- **Brief mode:** a one-page intent artifact (problem, users, constraints, non-goals, acceptance criteria, owner, rollout/reversal) for internal tools, libraries, migrations and spikes — `references/brief.md`. No invented economics; the audit accepts an approved brief as the requirements standard.
- **Compliance and threat modeling as requirements** — `references/compliance.md`: data, access and threat vectors established in `product.md` and `stack.md`, not an eighth document.
- **Naming checklist** — `references/naming.md`: the owner-run registry checks with dated, class-scoped results.
- Requirements carry stable REQ ids so each must traces to its behavior and evidence; the index template no longer links not-started documents.
- The description is trimmed to 838 of the 1024-character budget; behavior and triggers unchanged.

### Both skills

- Both versions move to 2.0.0 together (schema and decision-semantics changes are breaking); plugin manifests for Anthropic's and OpenAI's directories bump with them.

## [1.1.2] - 2026-11-24

### Distribution

- Package the repository as one plugin for Anthropic's plugin directory (`.claude-plugin/plugin.json`) and OpenAI's plugin directory for ChatGPT and Codex (`plugin.json`, Agent Plugins format, with light and dark icons derived from the mark). Both validate locally; submission through the developer portals is the owner's act.
- Restructure the README to mirror the [miiso.dev/skills](https://miiso.dev/skills) homepage — brand, tagline, latest version, access and sponsorship links, what the skills are, what they're for, quick setup, support — carrying the tagline "Agent/LLM skills for engineering by miisodev" across surfaces.
- Welcome issues for suggestions, bugs and feedback, with pull requests still closed automatically; `CONTRIBUTING.md` updated to match.

### Both skills

- `blueprint` and `production` move to 1.1.2 together; no skill content changes in this release.

## [1.1.1] - 2026-11-18

### blueprint

- Make official trademark-registry checks an owner-run verification step with exact queries, goods/services, candidate classes and search instructions. Treat public aggregators as preliminary evidence and blocked or unloaded searches as unverified; require returned official results before closing availability checks.
- Link primary USPTO and WIPO guidance, including related goods/services across classes and national/register coverage limits. Both skill and marketplace versions move together; production behavior is unchanged.

## [1.1.0] - 2026-10-20

### production

- Broaden audit routing across MCP servers/clients/hosts, agents, self-hosted and disconnected deployments, offline synchronization, real-time/event systems, games/spatial interfaces and embedded/device software.
- Add seven independently applicable parts: MCP, agent execution, deployment and operability, offline/synchronization, real-time/event systems, device/embedded software and software supply chain. Add data-pipeline, model-lifecycle, SDK/CLI, non-web accessibility and platform-compatibility checks: 39 parts and 753 checks, computed from the shipped registry.
- Keep existing check IDs, schema version 1.0, scoring weights and decision rules; extend schema part/surface identifiers. Existing scoped payloads retain their results; full audits must assess the newly applicable parts or explain their exclusion.
- Add dated primary-source references, version-aware protocol guidance and an illustrative MCP-part payload. Distinguish engineering coverage from specialist certification and identify the retained 2025 LLM baseline rather than implying a complete newer-edition mapping.

### Distribution

- Link the MCPRush publisher home and individual listings for BrainLLM and both skills; identify the repository commands as the complete-package install path. Both skill package versions move together; blueprint behavior is unchanged.

## [1.0.1] - 2026-09-28

### blueprint

- The skill no longer dictates where the blueprint lives. It finds an existing blueprint by its index or documents wherever the project keeps them, and asks the owner for a location when there is none, recommending the project's own convention.
- What it enforces instead is completeness: the index lists all seven documents with a status, every listed file exists, and nothing else in the folder claims to be intent.

### production

- Scope no longer assumes a `blueprint/` folder or any file name. It reconnoitres the project for stated intent (blueprints, PRDs, specs, agent instruction files, READMEs, docs, pricing pages, store listings) and records what it used in `run.assumptions`.
- The brand, cost, functional and analytics references follow suit.

## [1.0.0] - 2026-09-28

First public release.

### blueprint

- Establishes a project's foundation together with its owner in seven documents: `vision.md`, `market.md`, `business.md`, `product.md`, `brand.md`, `stack.md` and `plan.md`.
- Each document goes through a per-document cycle: Discuss → Research and compute → Draft → Review → Approve, with owner sign-off.
- `blueprint/README.md` indexes the documents, `workbook.md` records progress, and `research/` holds dated evidence and a runnable economic model, so the work can resume in any session.
- The blueprint sets intent and leaves design, architecture, schemas, APIs and copy to the builder.

### production

- An autonomous production readiness audit: 32 parts and 604 checks, organised by surface (web, API, webhooks, jobs, mobile, desktop, extension, CLI/SDK, messaging, docs).
- A structured JSON payload (`assets/payload.schema.json`) and a Markdown report that rank parts and surfaces by risk and give a GO, GO WITH CONDITIONS, HOLD or NO-GO decision per surface and overall.
- `scripts/readiness.py` does the validation, scoring, ranking and gating (Python 3.8+, standard library only).
- Covers OWASP Top 10:2025, the OWASP LLM Top 10, WCAG 2.2 AA, and the major privacy, accessibility, consumer and tax regimes.

[1.1.1]: https://github.com/miisodev/skills/releases/tag/v1.1.1
[1.1.0]: https://github.com/miisodev/skills/releases/tag/v1.1.0
[1.0.1]: https://github.com/miisodev/skills/releases/tag/v1.0.1
[1.0.0]: https://github.com/miisodev/skills/releases/tag/v1.0.0
