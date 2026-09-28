# Support audit

When a customer is stuck, charged wrongly, locked out or harmed, can they reach someone, and can that person fix it without touching the database by hand? Support readiness decides whether launch-week problems become loyal customers or public complaints.

- **Check prefix:** `SUP`
- **Applies to:** every product with users; admin/support tooling as an internal surface
- **Not applicable when:** never for a product with external users

## Evidence

- **Automated:** support widget or contact configuration; admin/back-office routes and permissions.
- **Manual:** send a test support request through each advertised channel; walk the admin tools for the common cases below; read the support runbooks.

## Checks

### Channels
| ID | Check | Verify | Severity |
|---|---|---|---|
| SUP-01 | At least one support channel is visible in the product and on the site, and a test message reached a person | Send a test request | High |
| SUP-02 | Response-time expectations are set (internally, and publicly if promised), including out-of-hours reality | Document | Medium |
| SUP-03 | In-product feedback or bug reporting exists | Inspect | Low |
| SUP-04 | Security, legal, privacy and abuse reports are routed to the right person, not a general queue | Routing config | Medium |

### Tooling
| ID | Check | Verify | Severity |
|---|---|---|---|
| SUP-05 | Support can look up a customer, see their plan, billing state and recent activity without database access | Admin UI | High |
| SUP-06 | Support can fix the predictable problems: resync entitlements, resend verification, reset MFA safely, extend a trial, issue a refund or credit | Admin UI; runbooks | High |
| SUP-07 | Admin tools are protected (IDN-07, IDN-16), and support actions are logged and attributable | Inspect | High |
| SUP-08 | Support can act on privacy requests (export, delete) through a defined path (PRV-17) | Runbook | Medium |

### Preparation
| ID | Check | Verify | Severity |
|---|---|---|---|
| SUP-09 | Answers are prepared for the predictable first-week questions: can't log in, paid but no access, how to cancel, refund request, delete my data, bug report | Canned responses or runbook | Medium |
| SUP-10 | Refund and credit authority is defined (who decides, limits) | Document | Low |
| SUP-11 | A path exists from support to engineering for bugs, with severity and customer follow-up | Process | Medium |
| SUP-12 | Incident communication templates exist (status page post, customer reply, email) | Templates | Low |
| SUP-13 | Enterprise commitments (SLAs, named contacts, uptime credits), if sold, can actually be met | Contracts vs. capacity | High where sold |
| SUP-14 | Support data (tickets, attachments, call recordings) is covered by the privacy policy and retention rules | Tool settings | Low |

## Severity notes

No reachable support channel on a paid product is High. Having no way to fix "paid but no access" except by editing the database is High, because it will happen in the first week.
