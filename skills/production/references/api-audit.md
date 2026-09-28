# API audit

Are the product's interfaces (its own API routes, public API, inbound and outbound webhooks, and third-party integrations) well-formed, robust, and on production footing? Authentication and authorization of routes are in identity-audit, and input-validation security in security-audit. This part covers contracts, webhooks and integrations.

- **Check prefix:** `API`
- **Applies to:** web app backends, public API, webhooks (inbound and outbound), integrations, SDK/CLI backends, mobile/desktop/extension backends
- **Not applicable when:** the product has no server-side interface and no integrations

## Evidence

- **Automated:** a route inventory generated from the code or framework (method, path, auth guard, validation); OpenAPI/GraphQL schema if present; contract tests.
- **Manual:** call representative endpoints with valid, invalid and edge requests on a non-production environment; send test webhook events through the provider's tooling; check each provider dashboard for failed deliveries where access exists.

## Checks

### Contract
| ID | Check | Verify | Severity |
|---|---|---|---|
| API-01 | One consistent error shape across routes, with machine-readable codes and human messages | Sample errors | Medium |
| API-02 | Correct status codes (400/401/403/404/409/422/429/5xx); never 200 with an error body | Sample calls | Medium |
| API-03 | Every list endpoint paginates, with bounded page sizes | Route inventory | High |
| API-04 | Versioning and a breaking-change policy exist for anything external clients or older app builds call (see CMP-10) | Docs; routes | High for public APIs and native apps |
| API-05 | Responses exclude internal fields (hashes, internal flags, other users' data in nested objects); IDs are not enumerable where guessing matters | Inspect payloads | High |
| API-06 | Retried unsafe operations are idempotent (idempotency keys or natural idempotency), especially creation and payment-adjacent requests | Send the same request twice | High |
| API-07 | Request schemas are validated and body sizes limited per route (larger limits only on upload routes) | Oversized/invalid requests | Medium |
| API-08 | Timestamps are ISO 8601 with time zone; money uses minor units with currency | Inspect payloads | Low |
| API-09 | A route inventory exists or has been generated, listing auth and authorization per route (feeds IDN-19) | Inventory in evidence | Medium |

### Inbound webhooks
| ID | Check | Verify | Severity |
|---|---|---|---|
| API-10 | Every provider's **live/production** webhook endpoint is registered to the production URL, with that endpoint's own signing secret in production config | Provider dashboard (or not verified) | Critical for payments/auth |
| API-11 | Signatures are verified on the raw body, with timestamp tolerance for replay protection | Send a bad signature → 4xx, nothing processed | Critical |
| API-12 | Processing is idempotent: event IDs are recorded and duplicates are no-ops | Deliver the same event twice | High |
| API-13 | Out-of-order delivery is handled (state checks, or fetching the current object from the provider) | Send an update before a create | High |
| API-14 | Handlers acknowledge quickly and do heavy work asynchronously | Code; timing | Medium |
| API-15 | Unknown event types are logged and acknowledged, not errored | Send an unhandled type | Low |
| API-16 | Processing failures alert a human, and the provider shows no backlog of failed deliveries | Alert rules; dashboard | High |

### Outbound webhooks (if the product sends them)
| ID | Check | Verify | Severity |
|---|---|---|---|
| API-17 | Payloads are signed with per-endpoint secrets and the scheme is documented | Inspect | High |
| API-18 | Delivery retries with backoff, then disables the endpoint and notifies the customer after repeated failure | Point at a failing endpoint | Medium |
| API-19 | Customers can see delivery logs and replay events | UI | Low |
| API-20 | Customer-supplied URLs are protected against SSRF (SEC-04) and called with timeouts | Code | High |

### Third-party integrations
| ID | Check | Verify | Severity |
|---|---|---|---|
| API-21 | Each integration uses production credentials, and its quotas and rate limits suit expected launch traffic | Config; provider limits | High |
| API-22 | Each integration's failure behaviour is defined (REL-04), and user-visible messages are honest | Simulate failure | Medium |

### Public API and developer experience
| ID | Check | Verify | Severity |
|---|---|---|---|
| API-23 | Rate limits and quotas are documented and communicated through response headers | Headers; docs | Medium |
| API-24 | Documentation is complete and current: quickstart, authentication, reference (OpenAPI or equivalent), errors, limits, changelog | Follow the quickstart | High for API products |
| API-25 | A sandbox or test mode mirrors production behaviour | Use it | Medium |
| API-26 | Deprecations are announced with timelines and deprecation/sunset signalling | Policy; headers | Medium |
| API-27 | SDKs are generated from, or tested against, the published spec | CI | Medium |
| API-28 | GraphQL (if used) limits query depth and complexity, and the introspection setting in production is a deliberate choice | Test deep queries | High where present |

## Severity notes

A payment or auth webhook that is unverified, unregistered in live mode, or failing silently is Critical: money or access goes out of sync with no one noticing.
