# Observability audit

When something goes wrong in production, will the team find out before users do, and be able to see why? This part covers logs, metrics, traces, error tracking, uptime monitoring and alerting. Product analytics (what users do) is analytics-audit.

- **Check prefix:** `OBS`
- **Applies to:** every surface with runtime code: web app, API, webhooks, jobs, mobile, desktop and extension clients (crash reporting)
- **Not applicable when:** never

## Evidence

- **Automated:** logging and monitoring configuration in code and infrastructure; error-tracking SDK initialisation per surface; alert rules; uptime-check configuration.
- **Manual:** trigger a handled and an unhandled error on a non-production environment and follow it into the tools; read a production log line; open the dashboards.

## Checks

### Errors and crashes
| ID | Check | Verify | Severity |
|---|---|---|---|
| OBS-01 | Error tracking is wired on every runtime surface: frontend, backend, jobs, and native crash reporting | SDK init per surface | High |
| OBS-02 | Stack traces are readable: source maps or debug symbols are uploaded and releases are tagged | Inspect a captured error | Medium |
| OBS-03 | Errors carry context (release, environment, route, anonymised user/session ID) without PII | Inspect an event | Medium |
| OBS-04 | New error types and error-rate spikes alert a human | Alert rules | High |

### Logs
| ID | Check | Verify | Severity |
|---|---|---|---|
| OBS-05 | Production logs are structured, levelled (debug off) and centralised with a retention period | Config; sample log | Medium |
| OBS-06 | Requests can be correlated across services and jobs (request/trace IDs) | Follow one request | Medium |
| OBS-07 | No secrets, tokens, passwords or unnecessary PII in logs (see PRV-10) | Search logs and logging calls | High |
| OBS-08 | Security-relevant events are logged: logins, failures, permission changes, admin actions, data exports (see SEC-24) | Inspect | Medium |

### Metrics and dashboards
| ID | Check | Verify | Severity |
|---|---|---|---|
| OBS-09 | Golden signals per service are visible: traffic, errors, latency (p50/p95/p99), saturation | Dashboards | Medium |
| OBS-10 | One "is production healthy?" view exists that someone other than its author can read | Dashboard | Low |
| OBS-11 | Business pulse metrics are visible (signups, core actions, payments succeeding, webhook success) | Dashboard | Medium |
| OBS-12 | Tracing exists for multi-service or AI/agent flows where latency hides in dependencies | Trace sample | Low |

### Uptime and alerting
| ID | Check | Verify | Severity |
|---|---|---|---|
| OBS-13 | External uptime checks cover the app, the API health endpoint and critical third-party paths, from outside the product's own infrastructure | Monitor config | High |
| OBS-14 | Alerts exist for downtime, 5xx rate, latency regression, queue backlog, failed jobs, failed webhooks and failed payments | Alert rules | High |
| OBS-15 | Every alert routes to a person who will see it, and has a runbook line; alert noise is low | Routing config; alert history | Medium |
| OBS-16 | Alerting has been tested end to end (a test alert reached a human) | Evidence of a test | Medium |
| OBS-17 | A status page exists (or a deliberate alternative), and the team can update it quickly | Status page | Low |

### Health endpoints
| ID | Check | Verify | Severity |
|---|---|---|---|
| OBS-18 | Health/readiness endpoints exist, check real dependencies, and are used by the platform to gate traffic | Call the endpoint; deploy config | Medium |

## Severity notes

No error tracking and no uptime monitoring on a launched product is High together, and the evidence that the team would learn of outages only from users. Secrets in logs (OBS-07) are High and can be Critical if logs are widely accessible.
