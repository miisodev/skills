# Reliability audit

Will the product stay up, degrade gracefully when a dependency fails, survive load, and recover from disaster without losing data? This part draws on the production readiness review practice from site reliability engineering: defined service levels, known failure modes, tested capacity and rehearsed recovery. observability-audit covers *seeing* failures; this part covers *surviving* them.

- **Check prefix:** `REL`
- **Applies to:** web app, public API, webhooks, background jobs, data pipelines, the backends of mobile and desktop apps and extensions
- **Not applicable when:** the product is fully static or fully client-side with no server state (still apply REL-13 to REL-16 for any stored data)

## Evidence

- **Automated:** uptime history; incident history; platform status history; load-test reports; backup job logs; infrastructure-as-code.
- **Manual:** map every dependency and ask "what does the user see if this is down?"; read the runbooks; check the date of the last restore test.
- **Needs owner approval:** load tests, failover drills and restore tests against shared or production environments. Without approval, record them as not verified, and state what would verify them.

## Checks

### Service levels
| ID | Check | Verify | Severity |
|---|---|---|---|
| REL-01 | Availability and latency objectives (SLOs) are defined for core user journeys, even informally | Document | Medium |
| REL-02 | RTO and RPO are written and accepted by the owner | Document | High |
| REL-03 | Planned maintenance and deploys cause no user-visible downtime (health-checked, zero-downtime deploys) | Deploy config; observe a deploy | Medium |

### Failure modes
| ID | Check | Verify | Severity |
|---|---|---|---|
| REL-04 | Every external dependency (database, auth, payments, email, AI provider, storage, third-party APIs) has a defined failure behaviour: retry, queue, degrade or clear error | Dependency map | High |
| REL-05 | Outbound calls have timeouts and bounded retries with backoff; a slow dependency cannot exhaust the service | Code review | High |
| REL-06 | Single points of failure are known and deliberately accepted or mitigated | Architecture review | Medium |
| REL-07 | Errors fail safe: the system stops in a safe state instead of corrupting data, double-charging or exposing data | Inject failures on money and data paths | Critical on money/data paths |
| REL-08 | Kill switches or feature flags exist to disable risky new features without a deploy | Flag inventory | Medium |
| REL-09 | Idempotency protects retried operations (payments, sends, creates) from duplicates (see API-06) | Retry the same request | High |

### Capacity
| ID | Check | Verify | Severity |
|---|---|---|---|
| REL-10 | Expected peak traffic is estimated, and a load test at 2–3× that peak passed on a production-like environment (error rate < 1%, latency within PRF targets) | Load-test report | High before a marketed launch |
| REL-11 | Platform ceilings are known (function timeouts, concurrency, connection limits, rate limits of providers), as is the behaviour at each | Provider docs plus config | Medium |
| REL-12 | Autoscaling or headroom exists for launch spikes (press, campaigns), and spike protection is in place (queues, rate limits) | Config | Medium |

### Backup and recovery
| ID | Check | Verify | Severity |
|---|---|---|---|
| REL-13 | Automated backups of every data store (database **and** file storage), with retention appropriate to the data | Backup config | Critical if missing |
| REL-14 | A restore has actually been performed recently, and its time is recorded | Restore log | High (Critical for products holding money or irreplaceable user data) |
| REL-15 | Backups are stored separately from primary infrastructure, encrypted and access-restricted | Config | High |
| REL-16 | A disaster-recovery runbook exists: restore steps, DNS/config changes, contacts | Document | Medium |
| REL-17 | Infrastructure is reproducible (infrastructure-as-code, or a documented record of every manual setting) | Repository or document | Medium |

### Jobs and pipelines
| ID | Check | Verify | Severity |
|---|---|---|---|
| REL-18 | Scheduled jobs are registered in production, idempotent, and locked against concurrent double runs | Scheduler config; code | High |
| REL-19 | Failed jobs retry with backoff, then alert; dead-letter or failure records are kept | Config | High |
| REL-20 | Long jobs checkpoint and resume; job duration is monitored against its interval | Code/metrics | Medium |

### Incident readiness
| ID | Check | Verify | Severity |
|---|---|---|---|
| REL-21 | Rollback to the previous version is possible within minutes and has been rehearsed | Rollback log or rehearsal | High |
| REL-22 | An incident process exists: who responds, severity ladder, communication (status page, customers) | Document | Medium |
| REL-23 | Out-of-hours response is a deliberate, stated choice (even if it is "none") | Document | Low |

## Severity notes

No backups, or no way to restore, is Critical for any product that stores user data. Untested restores are High (Critical for money or irreplaceable data), and in autonomous runs usually `not_verified` unless evidence of a restore exists.
