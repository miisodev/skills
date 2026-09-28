# Changelog

All notable changes to these skills are documented here. Versions follow [Semantic Versioning](https://semver.org/): a major version changes a skill's structure or outputs in ways that break existing use, a minor version adds capability, and a patch fixes content.

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

[1.0.1]: https://github.com/miisodev/skills/releases/tag/v1.0.1
[1.0.0]: https://github.com/miisodev/skills/releases/tag/v1.0.0
