# Engineering audit

Can someone other than the author keep this product working: change it safely, test it, understand it and operate it? This part covers code quality, testing of what would hurt, dependency hygiene and documentation. Security flaws in code are security-audit; delivery pipelines are infrastructure-audit.

- **Check prefix:** `ENG`
- **Applies to:** every codebase behind any surface
- **Not applicable when:** never for a product with code

## Evidence

- **Automated:** run the project's lint, type-check, test and build commands and record the results; dead-code and unused-dependency tools for the ecosystem; search for `TODO|FIXME|HACK`, debug output and disabled tests.
- **Manual:** read the README and try the setup on a clean checkout; read the core modules for structure and error handling.

## Checks

### Build and static quality
| ID | Check | Verify | Severity |
|---|---|---|---|
| ENG-01 | The project builds cleanly from a fresh checkout with documented commands | Run the build | High |
| ENG-02 | Lint and type checks pass and are enforced in CI (zero-warning policy or explicit suppressions) | Run; CI config | Medium |
| ENG-03 | Strict typing (or the ecosystem's equivalent) is on for application code; escapes (`any`, ignores) are rare and justified | Config; search | Low |
| ENG-04 | No debug output, commented-out code blocks or dead routes ship to production | Search; dead-code tool | Low |
| ENG-05 | TODO/FIXME items are triaged: launch-blocking ones resolved, the rest tracked | Search and review | Medium if any are launch-blocking |

### Testing what would hurt
| ID | Check | Verify | Severity |
|---|---|---|---|
| ENG-06 | Authentication and session lifecycle are covered by automated tests | Test inventory | High |
| ENG-07 | Money paths are covered: checkout, provider event → entitlement, cancellation, refunds | Test inventory | High for paid products |
| ENG-08 | Authorization is covered: cross-user and cross-tenant access attempts fail in tests | Test inventory | High |
| ENG-09 | The core value action has an end-to-end test that runs in CI | Test inventory; CI | High |
| ENG-10 | Pure business logic (pricing, permissions, parsing, dates) has unit tests with boundary cases | Test inventory | Medium |
| ENG-11 | The test suite passes now, is deterministic (no retry-until-green), and failures block merges | Run; CI history | High |
| ENG-12 | Integration tests use a real test database or service fakes that behave like production, rather than mocking everything | Inspect | Low |

### Dependencies
| ID | Check | Verify | Severity |
|---|---|---|---|
| ENG-13 | A lockfile is committed and CI installs from it exactly | Repository; CI | Medium |
| ENG-14 | Dependencies are reasonably current, with an automated update process that is actually merged | Outdated report; update-bot history | Low |
| ENG-15 | No unused, duplicated or abandoned dependencies on critical paths | Tooling; registry dates | Low |
| ENG-16 | Patched or forked dependencies are documented with reasons | Search for patches/overrides | Low |

### Structure and resilience in code
| ID | Check | Verify | Severity |
|---|---|---|---|
| ENG-17 | Error handling is consistent: one pattern for API errors, one for UI boundaries; no swallowed exceptions on critical paths | Code review | Medium |
| ENG-18 | Configuration and environment values are not hard-coded in source | Search | Medium |
| ENG-19 | Code structure is discoverable and consistent; shared code has one home | Review | Low |

### Documentation and handover
| ID | Check | Verify | Severity |
|---|---|---|---|
| ENG-20 | README covers what it is, prerequisites, setup, environment variables, tests and deployment, and setup actually works | Follow it | Medium |
| ENG-21 | Runbooks exist for deploy, rollback, restore, key rotation and common incidents | Docs | Medium |
| ENG-22 | Architecture is described (a page or a diagram): components, data flow, third-party seams | Docs | Low |
| ENG-23 | Significant decisions are recorded where future maintainers will find them | Decision records or equivalent | Low |
| ENG-24 | A competent developer could set up, change, test and deploy within one day without verbal handover | Judgment from the above | Medium; High where handover or sale is planned |

## Severity notes

A failing test suite or build on the release branch is High. Missing tests on money and authorization paths are High, because those regressions are silent and expensive. Style and structure findings are Low unless they are causing defects.
