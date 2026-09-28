# Identity audit

Can the right people get in, the wrong people stay out, and each person reach only what they are allowed to? This part covers authentication, sessions and tokens, OAuth/SSO, the account lifecycle, and authorization (the most common source of Critical findings in modern applications: one user reading or changing another's data).

- **Check prefix:** `IDN`
- **Applies to:** every surface with accounts or protected data: web app, admin console, API, mobile, desktop, extension, CLI/SDK (API keys and tokens)
- **Not applicable when:** the product has no accounts and no protected data

## Evidence

- **Automated:** route and endpoint inventory with the authentication/authorization guard on each; authorization tests if present; auth-provider configuration (redirect URIs, token lifetimes).
- **Manual:** with **two test accounts you create** (and a second tenant where multi-tenant), replay requests for A's resources using B's session, across read, update, delete, list filters, exports, file URLs and admin routes. Walk signup, login, reset, logout, email change and deletion.
- **Needs owner approval:** any testing that involves real users' accounts or data.

## Checks

### Authentication
| ID | Check | Verify | Severity |
|---|---|---|---|
| IDN-01 | Passwords (if used) are hashed with a modern slow hash (Argon2id, scrypt, bcrypt), or authentication is delegated to a reputable provider | Code or provider config | Critical if weak or reversible |
| IDN-02 | Password policy follows current guidance: length over complexity rules, breached-password check, paste allowed | Signup test | Medium |
| IDN-03 | No account enumeration via login, signup or reset responses or timing | Compare responses for real and fake emails | Medium |
| IDN-04 | Reset and magic-link tokens are single-use, short-lived and invalidated on use and on password change | Reuse a link; wait out expiry | High |
| IDN-05 | Email verification is required before actions that depend on owning the address | Test | Medium |
| IDN-06 | Brute-force protection on login, reset, OTP and verification (per account and per IP) | Burst attempts on a non-production environment | High |
| IDN-07 | MFA is available (passkeys or TOTP preferred over SMS), and required for admin and high-value accounts | Settings; admin accounts | High for admin |
| IDN-08 | OAuth/OIDC flows validate `state`/PKCE, use exact production redirect URIs, and link accounts safely (no takeover via an unverified provider email) | Provider config; flow test | High |
| IDN-09 | Enterprise SSO/SCIM (if offered) provisions and deprovisions correctly | Test tenant | High where sold |

### Sessions and tokens
| ID | Check | Verify | Severity |
|---|---|---|---|
| IDN-10 | Session cookies are `Secure`, `HttpOnly` and `SameSite`; tokens are stored where client-side scripts cannot trivially steal them | Inspect | High |
| IDN-11 | Sessions expire sensibly, refresh tokens rotate, and logout, password change and account deletion invalidate sessions everywhere | Two devices; change password | High |
| IDN-12 | JWTs (if used) are verified for signature, algorithm, issuer, audience and expiry, and never trusted for authorization data the client could alter | Code review | Critical if unverified |
| IDN-13 | API keys issued to users are shown once, hashed at rest, scoped, revocable and rotatable | Create, revoke, reuse | High |

### Authorization
| ID | Check | Verify | Severity |
|---|---|---|---|
| IDN-14 | Every object access is checked server-side against the requester: user B cannot read, change or delete user A's objects by changing an ID (IDOR/BOLA), including files and exports | Two-account replay | Critical |
| IDN-15 | Tenant isolation holds on every path: queries, search, list filters, exports, background jobs, caches, analytics views (database policies: DAT-10) | Two-tenant replay | Critical |
| IDN-16 | Function-level access is enforced server-side: admin and privileged routes reject normal users even when called directly | Call admin routes as a normal user | Critical |
| IDN-17 | Mass assignment is prevented: clients cannot set `role`, `plan`, `owner_id`, `tenant_id`, `is_admin` or prices | Send extra fields | Critical |
| IDN-18 | Roles and permissions match the documented model; least privilege is the default for new members | Role matrix vs. behaviour | High |
| IDN-19 | Every route not requiring auth is on an explicit, reviewed public allowlist | Route inventory | High |
| IDN-20 | Internal, cron and admin endpoints are protected by real authentication, not by obscure paths | Probe | High |

### Account lifecycle
| ID | Check | Verify | Severity |
|---|---|---|---|
| IDN-21 | Users can change email and password safely (reauthentication, notification to the old address) | Test | Medium |
| IDN-22 | Account recovery cannot be socially engineered past support (documented verification for support-assisted recovery) | Support process | Medium |
| IDN-23 | Account deletion works end to end in-app (data effects in DAT-19; app-store requirement in MOB-09) | Delete a test account | High |
| IDN-24 | Removing a member from a team or tenant revokes their access immediately, including API keys and active sessions | Test | High |
| IDN-25 | Admin impersonation or support access (if any) is authorised, logged and visible to the customer where appropriate | Inspect | Medium |

## Severity notes

Any confirmed cross-user or cross-tenant access (IDN-14 to IDN-17) is Critical and `core_flow: true`. If the two-account test could not be run, those checks are `not_verified` with Critical severity, which holds the decision until someone verifies them. That is intended: this is the single most important thing to prove before launch.
