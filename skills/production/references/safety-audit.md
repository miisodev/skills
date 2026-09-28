# Safety audit

Can the product be used to harm its users or others (through abuse, fraud, spam, harassment or harmful content), and does it behave safely when it matters? This is the trust-and-safety part, and it includes the *safety* characteristic of ISO/IEC 25010:2023: fail-safe behaviour, operating limits and warnings. It matters most for products with user-generated content, messaging, marketplaces, payments between users, free tiers, or real-world consequences (health, finance, physical devices).

- **Check prefix:** `SAF`
- **Applies to:** any surface where users create, share or send content; interact with each other; get free resources; or where the product's output drives real-world decisions
- **Not applicable when:** single-user tools with no sharing, no free resources worth abusing, and no consequential output. State the reasoning when marking the part N/A

## Evidence

- **Automated:** existing moderation, spam and fraud tooling configuration; rate limits; signup protections.
- **Manual:** as a test user, try to post abusive or spam content, harass another test account, upload prohibited material types (use benign stand-ins), create accounts in bulk, and abuse free resources. Review what happens next: reports, blocks, review queues, enforcement.

## Checks

### User-generated content
| ID | Check | Verify | Severity |
|---|---|---|---|
| SAF-01 | Content rules (acceptable use policy) are published and linked where users create content | Inspect | High for UGC products |
| SAF-02 | Users can report content and accounts, and reports reach a review queue someone monitors | File a report | High for UGC products |
| SAF-03 | Users can block or mute others, and blocking actually prevents contact | Two test accounts | High for social/messaging |
| SAF-04 | Moderation exists proportional to the risk: automated filters for obvious abuse, human review for escalations, and enforcement actions (remove, suspend, ban) that work | Inspect tooling; test enforcement | High |
| SAF-05 | Child-safety obligations are handled where images or messaging are shared (known-CSAM hash matching where appropriate, mandatory reporting routes) | Config; process | Critical where applicable |
| SAF-06 | A legal takedown process exists (DMCA or local equivalent), with a designated contact | Document | Medium |
| SAF-07 | Public profiles and content do not expose private data (location, email) by default | Inspect | High |

### Abuse and fraud
| ID | Check | Verify | Severity |
|---|---|---|---|
| SAF-08 | Messaging and invitation features cannot be used to spam non-users (rate limits, verification, content limits) | Attempt bulk sends in a non-production environment | High |
| SAF-09 | Sign-up abuse is limited where free resources have value (disposable email policy, verification, bot challenges, per-device or payment limits) | Attempt bulk signups in a non-production environment | Medium |
| SAF-10 | Payment fraud controls are on (provider risk tools, card-testing detection, velocity limits) (see BIL-15) | Config | High for paid products |
| SAF-11 | Marketplace and user-to-user payments have dispute, escrow or refund protections and identity checks appropriate to the value | Review | High where present |
| SAF-12 | Referral, coupon and credit systems cannot be farmed | Attempt self-referral | Medium |
| SAF-13 | Scraping and data harvesting of user data is limited (rate limits, authentication, no bulk enumeration) | Test enumeration | Medium |

### Safe behaviour and consequences
| ID | Check | Verify | Severity |
|---|---|---|---|
| SAF-14 | Where output influences health, money, legal status or physical systems, the product shows limits, warnings and human confirmation for consequential actions | Review flows | High; Critical in regulated domains |
| SAF-15 | Automated actions on users' behalf (sends, purchases, deletions, device commands) have confirmation, limits and an audit trail | Review | High |
| SAF-16 | Crisis and harm situations have a defined response where users may disclose them (self-harm, threats, emergencies), with signposting to help | Review; test keywords where appropriate | High for social, health and AI companion products |
| SAF-17 | Safety settings and defaults are protective for vulnerable users (minors, new accounts) | Inspect defaults | Medium |

## Severity notes

For products with user-to-user interaction, missing reporting and blocking (SAF-02, SAF-03) is High and often a store-review blocker (MOB-10). Child-safety gaps on image- or message-sharing products are Critical.
