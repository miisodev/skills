# Content audit

Are the words, media and help content finished, accurate and trustworthy? Placeholder text, typos on the pricing page, broken links and stale help articles cost more trust per minute of effort to fix than almost anything else. This part covers product copy, marketing copy, help content and media. brand-audit covers voice consistency; legal-audit covers policy content.

- **Check prefix:** `CON`
- **Applies to:** marketing site, web app, admin console, mobile app, desktop app, extension, docs/help center, email and notifications, store listings
- **Not applicable when:** never for a product with users

## Evidence

- **Automated:** search source and rendered pages for placeholders (`lorem ipsum`, `TODO`, `TBD`, `placeholder`, `coming soon`, `example.com`, `test`, `asdf`); a link crawler over the public site and docs; a spell-checker over primary pages.
- **Manual:** read the pricing, checkout, signup, onboarding, email and error copy in full. Check that every help article matches the current product.

## Checks

### Finish
| ID | Check | Verify | Severity |
|---|---|---|---|
| CON-01 | No placeholder text, lorem ipsum, TODO markers or developer strings are visible to users | Search source and rendered pages | High |
| CON-02 | No placeholder, watermarked or unlicensed images; all media final | Visual review; asset licences | High |
| CON-03 | No test or sample data visible anywhere public (fake users, "test project", seeded reviews) | Browse public pages and demo accounts | High |
| CON-04 | Spelling and grammar are clean on primary pages, money pages and emails | Spell-check plus read-through | Medium; High on pricing/checkout |
| CON-05 | Footer and boilerplate are current (year, company name, working links, real contact) | Inspect | Low |

### Accuracy
| ID | Check | Verify | Severity |
|---|---|---|---|
| CON-06 | Prices, plan names, limits and feature lists are identical everywhere they appear (site, app, checkout, emails, docs, store listings) | Compare each | High |
| CON-07 | Claims (security, compliance, uptime, integrations, "AI-powered", testimonials, customer logos) are true and substantiated | Ask for evidence; check integrations exist | High |
| CON-08 | Screenshots and demo videos show the current product | Compare | Low |
| CON-09 | Dates, version numbers and "new" labels are current | Inspect | Low |

### Links and media
| ID | Check | Verify | Severity |
|---|---|---|---|
| CON-10 | Zero broken internal links; external links resolve and open appropriately | Link crawler | Medium |
| CON-11 | Downloads (PDFs, installers, assets) resolve and are the current versions | Download each | Medium |
| CON-12 | Media is optimised and has captions/alt text (see A11-10, A11-12) | Inspect | Low |

### Help and documentation
| ID | Check | Verify | Severity |
|---|---|---|---|
| CON-13 | Minimum help content exists: getting started, account and billing (including cancellation), data export and deletion, contact | Browse help | High |
| CON-14 | Help content matches the current UI and behaviour | Follow three articles step by step | Medium |
| CON-15 | Developer docs (if any) have a working quickstart, reference and changelog (see API-24) | Follow the quickstart | High for API products |
| CON-16 | In-product microcopy (empty states, tooltips, confirmations, errors) is specific and helpful, not generic developer text | Review against design-audit states | Medium |

### User-generated and dynamic content
| ID | Check | Verify | Severity |
|---|---|---|---|
| CON-17 | Content from users or third parties renders safely and does not break layouts (see SEC-06 and safety-audit) | Seed long, RTL, emoji and HTML-like content | Medium |
| CON-18 | AI-generated content shown to users is labelled where required and reviewed where it makes claims (see AIF-10) | Inspect | Medium |

## Severity notes

A wrong price, a false claim or placeholder text on a money or trust page is High. A false claim about security, compliance or results can be Critical because of the legal exposure (legal-audit).
