# Functional audit

Does the product do what it claims, correctly, for the people it is for? Every other part assumes the product works. This part checks it: critical journeys complete end to end, business rules produce the right results, and the product meets its stated requirements. Where a `blueprint/product.md` or other requirements document exists, it is the standard. Otherwise, derive the requirements from the marketing claims, onboarding, docs and pricing page, because those are the promises users hold the product to.

- **Check prefix:** `FUN`
- **Applies to:** every user-facing surface (web app, mobile app, desktop app, admin console, public API, CLI/SDK, extension)
- **Not applicable when:** never. Every product has a core journey

## Evidence

- **Automated:** the project's end-to-end, integration and unit test suites (run them); test coverage of critical paths; seed or fixture data that exercises business rules.
- **Manual:** walk each critical journey on a non-production environment (or production with test accounts, where the profile allows), including the unhappy paths. Compare the product against every claim on the marketing site, pricing page and docs.
- **Needs owner approval:** journeys that send real messages, charge real money or change production data.

## Checks

### Requirements and claims
| ID | Check | Verify | Severity |
|---|---|---|---|
| FUN-01 | A list of critical user journeys exists or has been derived (signup → core value action → return; purchase; the admin/operator journeys) | Requirements doc, blueprint, or derived list recorded in the report | High |
| FUN-02 | Every "must" requirement (blueprint or equivalent) is met | Trace each to a working behaviour | Critical for core, High otherwise |
| FUN-03 | Every product claim on marketing, pricing and store pages is true today | Compare claims with behaviour, feature by feature | High |
| FUN-04 | Plan and tier limits advertised match what the product enforces | Test at, below and above each limit | High |

### Critical journeys
| ID | Check | Verify | Severity |
|---|---|---|---|
| FUN-05 | The core value action completes end to end for a new user | Fresh account, clean browser/device | Critical |
| FUN-06 | Onboarding and first run complete without dead ends, and a user can skip or resume | Walk it, abandon midway, return | High |
| FUN-07 | Every critical journey completes on each supported platform/surface | Repeat per surface | High |
| FUN-08 | Returning users find their data and state intact (session, drafts, settings) | Log out, in, and on another device | High |
| FUN-09 | Multi-user flows work where offered (invites, roles, sharing, handoffs) | Two or more test accounts | High |

### Correctness
| ID | Check | Verify | Severity |
|---|---|---|---|
| FUN-10 | Business rules compute correctly: prices, totals, taxes, proration, quotas, scoring, eligibility | Unit tests, or manual cases with known answers including boundaries | Critical where money or eligibility is involved |
| FUN-11 | Date, time and time-zone behaviour is correct (deadlines, recurrence, DST, user vs. server zone) | Cases across zones and a DST boundary | High |
| FUN-12 | Numbers, currency and rounding are handled exactly (no floating-point money) | Code review plus boundary cases | Critical for money |
| FUN-13 | Search, filtering and sorting return correct and complete results | Known data set; edge queries | Medium |
| FUN-14 | Imports and exports round-trip without loss or corruption | Export, re-import, compare | High |
| FUN-15 | Concurrent edits and double submissions produce a correct state (no duplicates, no lost updates) | Two sessions editing; double-click submit | High |

### Edge cases and failure behaviour
| ID | Check | Verify | Severity |
|---|---|---|---|
| FUN-16 | Empty, minimal, large and malformed inputs are handled without crashes or corrupted data | Boundary and fuzz-style manual inputs | High |
| FUN-17 | Interrupted operations (network loss, closed tab, app killed) leave a recoverable state | Interrupt mid-operation | High |
| FUN-18 | Destructive actions do exactly what they say, with confirmation or undo proportional to the damage | Delete, bulk actions, resets | High |
| FUN-19 | Feature flags in production expose no half-finished features, and flagged-off paths are unreachable | Flag inventory vs. behaviour | Medium |
| FUN-20 | Critical journeys have automated tests that run in CI and currently pass | CI config and latest run | High |

## Severity notes

A broken core value action, wrong money arithmetic, or data loss in a critical journey is Critical and makes the check `core_flow: true`. A false marketing claim is at least High because it creates legal and trust exposure (see legal-audit). Where no requirements exist anywhere, record FUN-01 as a finding and audit against the derived list.
