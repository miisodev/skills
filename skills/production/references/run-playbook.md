# Run playbook — making full audits finish

A full audit is 753 checks across 39 parts. Run in one agent, it can exhaust the context window or drift into shallow passes. This playbook keeps runs finishable and comparable.

## Part bundles for parallel sub-agents

Parts are independent; each sub-agent takes a bundle and returns check results for the payload. Recommended bundles:

| Bundle | Parts |
|---|---|
| **Experience** | functional, ux, design, accessibility, content, localization, compatibility |
| **Trust** | security, identity, data, privacy, safety, ai |
| **Business** | api, billing, messaging, support, analytics, seo, brand, legal |
| **Operations** | performance, reliability, observability, infrastructure, cost, engineering |
| **Platform** | mobile, desktop, extension, package |
| **Specialized** | mcp, agent, deployment, sync, realtime, device, supply-chain, launch |

Merge rules:

1. The orchestrator owns the payload. Sub-agents return check results and findings; the orchestrator merges, deduplicates and scores.
2. Every result carries its surface, severity, `core_flow` and evidence. A sub-agent that cannot assess a check returns `not_verified` with the exact human step — it never omits the check.
3. Never omit: a check that does not apply is recorded `not_applicable` with the reason. An omitted check is unassessed and holds the decision.
4. Overlapping results are resolved by the orchestrator: the observed evidence wins over the inferred; the more severe status wins on ties.

## Token discipline

- After routing, load only the `*-audit.md` files for applicable parts — never the whole references tree.
- Carry check IDs, not prose: a sub-agent's return is a results list, not a narrative.
- The report is rendered from the payload by the scorer; agents do not reformat it.

## Checkpoint and resume

- Write the partial payload after each part (`production-readiness-partial.json`), and record `run.checkpoint` with the parts completed.
- A resumed run loads the partial payload, reads `results.missing_checks` from the scored partial, and assesses only what is missing.
- Record `run.run_id` (unique), the artifact or revision audited, and the checklist version — so two runs are comparable.

## Delta against a prior run

Compare a re-run's `result.json` with the prior one: **new** fails, **resolved** (previously failing, now passing), **still open**, and **no longer verified** (previously verified checks whose artifact, environment or dependencies changed). Reuse prior evidence only where the artifact, environment and relevant dependencies are unchanged. A release-diff run reports the delta, not the whole audit.
