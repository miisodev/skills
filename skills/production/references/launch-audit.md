# Launch audit

Is **this deployment, now,** ready to meet users, and is the team ready for what happens next? Every other part proves the product is good. This one proves the switch to production has been made correctly, the live product works end to end, and launch day has a plan. Run it last.

- **Check prefix:** `LCH`
- **Applies to:** every surface being launched or released
- **Not applicable when:** never (for a Spot Audit, include it only if the concern is launch-related)

## Evidence

- **Automated:** production configuration and feature flags; `robots.txt` and headers on production; provider modes from configuration.
- **Manual:** the production smoke test (LCH-05), where the profile and the owner allow it; review the launch plan and rollback procedure.
- **Needs owner approval:** smoke tests that create real accounts, send real messages or take real payments on production. In autonomous runs, run only read-only production probes and record the rest as not verified.

## Checks

### Pre-flight
| ID | Check | Verify | Severity |
|---|---|---|---|
| LCH-01 | All Critical findings from the other parts are resolved or explicitly risk-accepted in writing by the owner | This report | Critical |
| LCH-02 | The release candidate is the build being launched: tagged, with CI green, deployed to production and matching what was tested | CI and deploy records | High |
| LCH-03 | The production switch is complete for every service: payments (live keys, prices, webhooks), auth (production instance, redirect URIs, OAuth consent screen published), email (verified domain, out of sandbox), SMS, analytics and error tracking (production projects), storage, AI providers (production keys, limits), webhooks pointing at production, scheduled jobs registered, debug off | Row-by-row evidence in the report | Critical for payments/auth/email |
| LCH-04 | Search visibility is correct for launch: staging `noindex` removed from production, and the sitemap is on the production domain (SEO-01) | `curl` production | Critical for public launch |

### Live verification
| ID | Check | Verify | Severity |
|---|---|---|---|
| LCH-05 | Production smoke test passes across the full lifecycle: land → sign up (email arrives) → onboard → core value action → upgrade/pay (entitlement immediate, receipt arrives) → log out and in → reset password → trigger a handled error → cancel → delete account → events appear in analytics and no unexpected errors appear in tracking | Run on production with the owner's approval | Critical |
| LCH-06 | The core path works on a real phone on a cellular network | Device test | High |
| LCH-07 | Production backups are running, and the first one exists (REL-13) | Backup status | Critical |
| LCH-08 | Monitoring and alerting watch the production URLs, and a test alert reached a human (OBS-16) | Evidence | High |

### Launch day and after
| ID | Check | Verify | Severity |
|---|---|---|---|
| LCH-09 | A written launch plan exists: sequence, owners, a merge freeze, a staged announcement (soft launch before broad), and who watches what | Document | Medium |
| LCH-10 | A rollback procedure for launch day is one page long, has a named person to run it, and has pre-agreed rollback triggers (for example sustained 5xx above 2%, or broken payments) | Document | High |
| LCH-11 | Support is staffed and monitored for launch (SUP-01, SUP-09) | Evidence | High |
| LCH-12 | A post-launch watch is scheduled: first 2 hours active, daily checks for 48 hours (errors, latency, funnel, payment success, webhook failures, cost, support themes), and a review after one week | Plan | Medium |
| LCH-13 | Store or marketplace approvals needed for launch are granted, or their timing is built into the plan (MOB-03, EXT-07) | Console | High where applicable |
| LCH-14 | External dependencies for launch are confirmed: domain renewals, quota increases requested from providers, press and partner timing | Checklist | Medium |

## Severity notes

A failed production smoke test is an automatic NO-GO. An unverified smoke test holds the decision (HOLD) until someone runs it. That is the expected outcome of an autonomous run, which should not run LCH-05 on production without approval.
