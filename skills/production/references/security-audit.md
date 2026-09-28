# Security audit

Can the product be used to leak data, run attacker code, abuse its resources or compromise its users, and would an attack be detected? This part covers application security aligned with OWASP Top 10:2025 and ASVS 5.0: injection and output handling, configuration and secrets, browser protections, files, supply chain, abuse and detection. Authentication and authorization are in identity-audit, AI-specific attacks in ai-audit, and native-app hardening in mobile-audit and desktop-audit.

- **Check prefix:** `SEC`
- **Applies to:** every surface
- **Not applicable when:** never

## Evidence

- **Automated:** secret scanning of the working tree **and** git history (gitleaks, trufflehog); dependency vulnerability audit for each ecosystem (`npm audit`, `pip-audit`, `cargo audit`, OSV-Scanner); static analysis if configured (Semgrep, CodeQL); security headers and cookie flags from `curl -I`; TLS scan.
- **Manual:** review input handling on every route that takes user input; inspect file upload and URL-fetch features; inspect client bundles for leaked configuration.
- **Needs owner approval:** dynamic scanners, fuzzers and active exploitation attempts against any shared or production environment.

## Checks

### Injection and output handling
| ID | Check | Verify | Severity |
|---|---|---|---|
| SEC-01 | All input is validated server-side at every boundary (body, query, params, headers, webhooks); client validation is UX only | Route review | High |
| SEC-02 | Database access uses parameterised queries or a safe ORM, with no string-built SQL/NoSQL queries | Code search | Critical if user input reaches a query unparameterised |
| SEC-03 | No command, template or code injection: user input never reaches shells, `eval`, template compilers or deserialisers unsafely | Code search | Critical |
| SEC-04 | Server-side request forgery is prevented: user-supplied URLs (webhooks, imports, previews, avatars) cannot reach internal or metadata addresses | Code review; test with an internal IP | High |
| SEC-05 | Open redirects are prevented: `next`/`returnTo` parameters are allowlisted | Test | Medium |
| SEC-06 | User and third-party content renders safely: output is encoded, rich text/markdown is sanitised, and there is no unsafe raw HTML injection | Code search; seed a script payload on a test account | High (Critical for stored XSS on shared views) |

### Files
| ID | Check | Verify | Severity |
|---|---|---|---|
| SEC-07 | Uploads are validated by content type and size, filenames are regenerated, and risky types (SVG, HTML) are handled safely | Upload tests | High |
| SEC-08 | Uploaded files are served from a separate origin or with safe headers, and private files require authorization (see IDN-14) | Inspect URLs and headers | High |
| SEC-09 | Uploads are scanned or sandboxed where users share files with each other | Config | Medium |

### Secrets and configuration
| ID | Check | Verify | Severity |
|---|---|---|---|
| SEC-10 | No secrets in the repository or its history; any found secret is treated as compromised and rotated | gitleaks/trufflehog | Critical |
| SEC-11 | No privileged keys in client code, bundles or binaries (check client-exposed prefixes like `NEXT_PUBLIC_`, `VITE_`, `EXPO_PUBLIC_`) | Inspect built bundles | Critical |
| SEC-12 | Production has debug modes off, verbose errors off, and no stack traces, SQL or internal paths in responses | Force errors | High |
| SEC-13 | Public source maps are a deliberate decision | Check deployed `.map` files | Low |
| SEC-14 | Credentials are per environment, rotated on staff departure or suspected leak, with a rotation runbook | Process evidence | Medium |

### Browser and transport protections
| ID | Check | Verify | Severity |
|---|---|---|---|
| SEC-15 | HTTPS everywhere with HSTS; no mixed content | `curl -I`; browser | High |
| SEC-16 | A Content-Security-Policy suited to the app is set (at least `frame-ancestors`, script sources) | Headers | Medium |
| SEC-17 | `X-Content-Type-Options: nosniff`, `Referrer-Policy` and `Permissions-Policy` are set | Headers | Low |
| SEC-18 | CSRF protection exists for cookie-authenticated state changes (tokens or strict SameSite plus origin checks) | Inspect | High |
| SEC-19 | CORS allows only explicit origins, never `*` with credentials, and preview origins are not trusted in production | Headers and config | High |
| SEC-20 | Third-party scripts are minimised, loaded from trusted origins, and pinned with Subresource Integrity where static | Inspect | Medium |

### Supply chain
| ID | Check | Verify | Severity |
|---|---|---|---|
| SEC-21 | No known critical/high vulnerabilities in reachable dependencies, or each is triaged with a recorded decision | Audit tools | High for critical reachable CVEs |
| SEC-22 | Dependency updates are automated and monitored; new dependencies are reviewed (install scripts, maintainers, typosquats) | Config; process | Medium |
| SEC-23 | CI/CD is hardened: least-privilege tokens, pinned third-party actions, protected secrets, no untrusted code running with deploy credentials | CI config | High |

### Abuse, detection and response
| ID | Check | Verify | Severity |
|---|---|---|---|
| SEC-24 | Security events are logged and monitored: authentication events, permission changes, admin actions, exports, spikes in 401/403/429 | Logging config | Medium |
| SEC-25 | Rate limits protect expensive and sensitive endpoints and return 429 with `Retry-After` (auth-specific limits: IDN-06) | Test bursts on a non-production environment | High |
| SEC-26 | Bot and automation protection exists where abuse is likely (signup, contact forms, free tiers, checkout card-testing) | Inspect | Medium |
| SEC-27 | A vulnerability disclosure route exists (`security.txt` or a published contact) | `/.well-known/security.txt` | Low |
| SEC-28 | A breach response plan exists: who acts, key rotation, user and regulator notification (deadlines in privacy-audit) | Document | Medium |
| SEC-29 | Realtime channels (WebSockets, WebRTC, server-sent events) authenticate and authorise every subscription and message | Code review | High where present |

## OWASP Top 10:2025 mapping

| OWASP category | Checks |
|---|---|
| A01 Broken Access Control (includes SSRF) | identity-audit IDN-10 to IDN-16, SEC-04 |
| A02 Security Misconfiguration | SEC-12 to SEC-19, INF-04 |
| A03 Software Supply Chain Failures | SEC-21 to SEC-23 |
| A04 Cryptographic Failures | SEC-15, DAT-17, IDN-01 |
| A05 Injection | SEC-01 to SEC-03, SEC-06 |
| A06 Insecure Design | SEC-25, SEC-26, safety-audit |
| A07 Authentication Failures | identity-audit IDN-01 to IDN-09 |
| A08 Software or Data Integrity Failures | SEC-23, API-11 (webhook signatures) |
| A09 Logging & Alerting Failures | SEC-24, OBS-04, OBS-14 |
| A10 Mishandling of Exceptional Conditions | SEC-12, REL-07 |

## Severity notes

Any path to arbitrary code execution, bulk data access, or leaked production credentials is Critical. A found secret is Critical until rotated. Deleting it from the repository does not fix it.
