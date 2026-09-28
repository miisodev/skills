# Infrastructure audit

Is the platform under the product correctly configured, deployable and reproducible? This part covers environments and configuration, domains, DNS and TLS, the delivery pipeline, and runtime settings. reliability-audit covers surviving failure, observability-audit covers seeing it, and cost-audit covers paying for it.

- **Check prefix:** `INF`
- **Applies to:** every surface that is hosted or delivered: marketing site, web app, API, webhooks, jobs, docs, app and extension backends, update feeds
- **Not applicable when:** never for a hosted product

## Evidence

- **Automated:** CI/CD configuration; infrastructure-as-code; `.env.example` against the documented production variables; DNS lookups (`dig`/`nslookup`) for the domains; TLS checks (SSL Labs or `openssl s_client`); HTTP redirect checks with `curl -I`.
- **Manual:** read the deploy and rollback procedure; inspect platform settings where access exists.

## Checks

### Environments and configuration
| ID | Check | Verify | Severity |
|---|---|---|---|
| INF-01 | Development, staging/preview and production are separate, with separate credentials, databases and third-party projects | Config inventory | High |
| INF-02 | Every required production variable is present, and configuration is validated at boot (fail fast on missing or invalid) | Env schema vs. production list | High |
| INF-03 | Staging mirrors production (same platform, variable names, migrations, data shape) closely enough to trust tests there | Compare | Medium |
| INF-04 | No environment-conditional logic keyed on hostnames scattered through the code; no debug or seed endpoints reachable in production | Code search; probe routes | High |
| INF-05 | Every third-party service is on its production/live mode and credentials (full list under LCH-03) | Config inventory | Critical for payments/auth |

### Domains, DNS and TLS
| ID | Check | Verify | Severity |
|---|---|---|---|
| INF-06 | DNS records are correct, one canonical host is enforced (apex or www), and HTTP redirects to HTTPS | `dig`, `curl -I` | High |
| INF-07 | TLS certificates are valid for every serving host, auto-renew, and use modern protocols only | SSL Labs / openssl | High |
| INF-08 | Domains have auto-renew and registrar lock on, with a monitored contact email | Registrar (or record as not verified) | High |
| INF-09 | No dangling DNS records pointing to deprovisioned services (subdomain takeover risk) | Enumerate subdomains | High |
| INF-10 | Email-sending DNS (SPF, DKIM, DMARC) is configured for every sending domain (details in MSG-01) | `dig TXT` | High |

### Delivery pipeline
| ID | Check | Verify | Severity |
|---|---|---|---|
| INF-11 | The main branch is protected; tests, lint and type checks gate merges | Repository settings or CI config | Medium |
| INF-12 | Builds are reproducible from a commit; artifacts are not built on personal machines | CI config | Medium |
| INF-13 | Migrations and deploys are ordered safely (new code tolerates old schema, or migrations run first, atomically) | Deploy scripts (see DAT-05) | High |
| INF-14 | Secrets are injected at deploy/runtime from a secret store, never baked into images, bundles or binaries | Build config; artifact inspection | Critical if found in artifacts |
| INF-15 | Preview environments cannot reach production data or send real messages or charges | Config | High |
| INF-16 | Deploy history is visible (who, what, when) and deploys notify the team | Platform/CI | Low |

### Runtime
| ID | Check | Verify | Severity |
|---|---|---|---|
| INF-17 | Runtime and platform versions are supported (not end-of-life) | Runtime config vs. vendor EOL dates | Medium |
| INF-18 | Resource limits (memory, timeouts, concurrency, body size) are set deliberately for each service | Config | Medium |
| INF-19 | Data residency and hosting regions match the product's commitments and privacy obligations (see PRV-13) | Region config | High where committed |
| INF-20 | Access to production infrastructure is limited to named people with MFA, and offboarding removes it | Access list (or not verified) | High |

## Severity notes

Test-mode payment or auth configuration in production is Critical, because nothing can be bought or signed into. Secrets in built artifacts are Critical. Expired or soon-to-expire certificates or domains are Critical within 14 days of expiry, and High otherwise.
