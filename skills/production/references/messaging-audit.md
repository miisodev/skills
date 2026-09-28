# Messaging audit

Do the product's emails, push notifications, SMS and in-app notifications arrive, say the right thing, and respect the rules and the recipient? A password reset that lands in spam is a broken login. A marketing email without a working unsubscribe is a legal problem.

- **Check prefix:** `MSG`
- **Applies to:** transactional email, marketing email, push notifications, SMS/WhatsApp, in-app notifications and digests
- **Not applicable when:** the product sends no messages of any kind

## Evidence

- **Automated:** DNS lookups for SPF, DKIM and DMARC on each sending domain; the email provider's domain status; the template inventory in code; notification triggers.
- **Manual:** trigger every transactional message on a non-production environment to a test inbox; check rendering in major clients (web and mobile, light and dark); check headers for authentication results; send a message through a spam checker if available.

## Checks

### Deliverability
| ID | Check | Verify | Severity |
|---|---|---|---|
| MSG-01 | SPF, DKIM and DMARC are configured and aligned for every sending domain (DMARC at least `p=none` with reporting, heading to enforcement) | `dig TXT`; message headers | High |
| MSG-02 | The sending domain is verified with the provider, the provider is out of sandbox/trial mode, and the from-address is on the product's own domain | Provider status | Critical if auth emails cannot be delivered |
| MSG-03 | Transactional and marketing mail are separated (streams, subdomains or providers) so marketing reputation cannot sink password resets | Config | Medium |
| MSG-04 | Bounces and complaints are processed into suppression lists, and bounce/complaint rates are monitored | Provider config | Medium |
| MSG-05 | High-volume senders meet mailbox-provider bulk-sender rules (authentication, one-click unsubscribe per RFC 8058, low complaint rate) | Headers; volumes | High for bulk senders |

### Transactional coverage and quality
| ID | Check | Verify | Severity |
|---|---|---|---|
| MSG-06 | Every required message exists and triggers: verification, password reset/magic link, welcome, receipts, payment failure, cancellation, security alerts (new sign-in, password or email change), account-deletion confirmation | Trigger each | High for auth and billing messages |
| MSG-07 | Messages render in the major clients and dark mode, include a plain-text part, and work with images off | Rendering test | Medium |
| MSG-08 | Links point to production, deep-link correctly into apps, and expire safely where they grant access | Click through | High for auth links |

### Consent and law
| ID | Check | Verify | Severity |
|---|---|---|---|
| MSG-09 | Marketing messages have the required consent for the market (opt-in under GDPR/PECR/CASL; CAN-SPAM rules in the US), working unsubscribe, sender identification and a postal address | Signup consent; sample message | High |
| MSG-10 | Replies go to a monitored address; "no-reply" is not used where users need to respond | Reply to a message | Low |
| MSG-11 | Users can set notification preferences per channel and category, and preferences are honoured | Change and trigger | Medium |

### Push, SMS and in-app
| ID | Check | Verify | Severity |
|---|---|---|---|
| MSG-12 | Push permission is requested in context (not at first launch), tokens are refreshed and pruned, and notifications deep-link correctly | Device test | Medium |
| MSG-13 | SMS senders are registered where required (e.g., US 10DLC, alphanumeric sender IDs), handle STOP/HELP, have consent, and cost is capped (CST-07) | Provider config | High where SMS is used |
| MSG-14 | Notification volume is sensible: no duplicates, digesting where appropriate, quiet hours honoured where promised | Trigger bursts | Low |
| MSG-15 | User-triggered sends (invites, shares, reminders) are rate-limited and cannot be used to spam non-users (SAF-08) | Test | High |
| MSG-16 | Messages are localized and on-brand, matching the product's language and voice (LOC-07) | Sample | Low |

## Severity notes

If verification or password-reset emails do not reliably arrive, users cannot sign up or recover accounts. That is Critical and `core_flow: true`.
