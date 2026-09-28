# Brand audit

Does every surface look and sound like the same product, a finished one that belongs to the owner and not to a template? Where the project states its brand (a blueprint's brand document, a brand brief or guidelines, wherever they live), that is the standard for name, voice and visual direction. Otherwise, use the product's own strongest surface as the reference.

- **Check prefix:** `BRD`
- **Applies to:** marketing site, web app, admin console (lightly), mobile app, desktop app, extension, emails, docs, store listings, social profiles
- **Not applicable when:** internal tools with no brand intent (mark N/A with the reason)

## Evidence

- **Automated:** search for framework or template defaults (default favicons, `Create Next App`, `Vite + React`, template names, placeholder logos); manifest and icon files; OG images.
- **Manual:** put samples side by side (homepage, onboarding, dashboard, pricing, checkout, a transactional email, a 404, the store listing, docs) and compare name, logo, colour, type, imagery and voice.

## Checks

### Identity
| ID | Check | Verify | Severity |
|---|---|---|---|
| BRD-01 | The name, logo and marks are used consistently (spelling, casing, lockups) across every surface | Side-by-side review | Medium |
| BRD-02 | No template, framework or starter-kit leftovers: default favicons, page titles, meta descriptions, sample logos or copy | Search; inspect tabs and shares | High |
| BRD-03 | The favicon set, app icons, touch icons and PWA manifest (name, short name, theme colour) are complete and render at every size | Inspect files; install PWA | Medium |
| BRD-04 | Default and per-page social preview images are branded (SEO-09) | Share links | Medium |
| BRD-05 | Domains and social handles used in the product and footer are owned and consistent | Inspect links | Low |
| BRD-06 | The name has had at least a basic trademark conflict check in the markets served (legal status: LGL-11) | Search results in evidence | Medium |

### Voice
| ID | Check | Verify | Severity |
|---|---|---|---|
| BRD-07 | Voice is consistent across marketing, product UI, errors, emails and support replies (per the voice guide if one exists) | Sample comparison | Low |
| BRD-08 | Calls to action use consistent wording for the same action | Compare CTAs | Low |

### Visual
| ID | Check | Verify | Severity |
|---|---|---|---|
| BRD-09 | The product's visual design matches the marketing site's promise (users do not land in a different-looking product after signup) | Compare | Medium |
| BRD-10 | Emails, PDFs and invoices use the brand (logo, colours, sender name) | Samples | Low |
| BRD-11 | Imagery and illustration style is consistent, licensed and on-brand | Review | Low |
| BRD-12 | Visual direction and fixed choices in the brand brief (if any) are honoured | Compare with the project's stated brand direction | Medium |

## Severity notes

Template leftovers visible to users (BRD-02) are High, because they signal an unfinished product at first glance. Other brand findings are usually Medium or Low unless they cause confusion about who the user is dealing with.
