# Intent discovery — the shared contract between the skills

Both skills read the same stated intent wherever the project keeps it. This reference is the canonical discovery order and the mapping from blueprint sections to audit parts. It exists once, here, and both skill files point at it.

## Discovery order

1. **`.agents/blueprints/` (or wherever the project keeps its blueprint index)** — the blueprint README index and its approved documents. An approved document is the requirements standard.
2. **A one-page brief** (see the blueprint skill's brief mode) — for internal tools, libraries, migrations and spikes: problem, users, constraints, non-goals, acceptance criteria, owner, rollout/reversal. An approved brief is the requirements standard for its scope.
3. **Existing PRDs, specs, agent instruction files (`AGENTS.md`, `CLAUDE.md` and the like), READMEs, docs, pricing pages, store listings** — the strongest statement of requirements found. PRDs and specs are evidence, not approval.
4. **The product's public claims** — where nothing else exists, the standard is what the product says about itself.

Record in `run.assumptions` what you found, where, and what standard it set. If nothing durable exists, record the finding: there is **no durable requirements standard**, the functional checks derive from the public claims alone, and running the blueprint skill (or writing a brief) is the recommendation in the report.

## Blueprint section → audit parts

| Blueprint section | Sets the standard for | Audit parts |
|---|---|---|
| `product.md` — quality bar, requirements | What "finished" means, must-have journeys | FUN, UX, A11, PRF, REL, PRV, CMP |
| `business.md` — pricing, economics | What is billed and what it costs | BIL, LGL |
| `stack.md` — secrets policy, infrastructure, constraints | How the product runs and what it must never leak | SEC, INF, DEP, SCH |
| `brand.md` — personality, voice, visual direction | What the surfaces should say and look like | CON, MSG, BRD, SEO |
| `plan.md` — phases, exit criteria, risks, kill criteria | What launch means here | LCH, OBS |
| `market.md` — positioning, channels | Who the audience is and where they arrive | ANL, SEO, SUP |
| The brief — acceptance criteria, non-goals | Scope-limited checks for internal tools and spikes | The parts the brief's acceptance criteria name |

## Boundaries

- The blueprint sets requirements; the audit checks the shipped product against them. The audit does not redesign the blueprint.
- Where the shipped product **deviates from an approved blueprint section**, the audit records a finding citing the blueprint section and the observed behavior, and recommends either fixing the product or reopening the blueprint document (the blueprint skill's reopen flow) — pull requests are not part of this repository's workflow.
- Where the blueprint is silent, the check's own standard applies, and the report says the blueprint did not cover it.
