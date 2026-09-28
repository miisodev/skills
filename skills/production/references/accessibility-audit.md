# Accessibility audit

Can everyone use the product, including people using screen readers, keyboards, switch devices, magnification, voice control or captions, and people with cognitive, motor or vision differences? The default bar is **WCAG 2.2 AA** (or the platform equivalent for native apps), which also satisfies the common legal regimes below.

- **Check prefix:** `A11`
- **Applies to:** marketing site, web app, admin console, mobile app, desktop app, extension, docs/help center, email templates (A11-15 to A11-17)
- **Not applicable when:** no human-facing interface

## Evidence

- **Automated:** axe-core or equivalent over every core page/screen; Lighthouse accessibility; platform scanners (Accessibility Inspector, Android Accessibility Scanner, Accessibility Insights). Automated tools find roughly a third of issues. A clean automated result is necessary but not sufficient.
- **Manual:** keyboard-only pass of every critical journey; a screen-reader pass with at least one reader per platform shipped (NVDA or JAWS on Windows, VoiceOver on macOS/iOS, TalkBack on Android); zoom to 200% and 400% reflow; OS text scaling; reduced motion; high-contrast mode.

## Checks

### Operable
| ID | Check | Verify | Severity |
|---|---|---|---|
| A11-01 | Every interactive element is reachable and operable by keyboard (or switch access), in a logical order, with no traps | Keyboard-only pass | High; Critical if a core flow is blocked |
| A11-02 | A visible focus indicator is present everywhere and never hidden by sticky UI | Tab through | High |
| A11-03 | Dialogs, menus and custom widgets follow expected keyboard patterns and manage focus | Open and close each | High |
| A11-04 | A skip link or landmarks allow bypassing repeated navigation | Inspect | Medium |
| A11-05 | Targets are at least 24×24 CSS px (WCAG 2.2), or 44/48 on touch platforms | Inspect | Medium |
| A11-06 | Drag and complex gestures have single-pointer alternatives | Try without dragging | Medium |
| A11-07 | Time limits can be extended; session expiry warns before it ends | Idle out | Medium |

### Perceivable
| ID | Check | Verify | Severity |
|---|---|---|---|
| A11-08 | Text contrast is at least 4.5:1 (3:1 large text); UI components and focus indicators at least 3:1, in every theme | Contrast checker on each theme | Medium; High on core flows |
| A11-09 | Information is never conveyed by colour alone (errors, required fields, charts, status) | Greyscale review | Medium |
| A11-10 | Meaningful images have text alternatives; decorative ones are hidden from assistive technology | Inspect | Medium |
| A11-11 | Content reflows at 320 CSS px / 400% zoom and respects OS text scaling without loss | Zoom and scale | Medium |
| A11-12 | Video has captions, audio has transcripts, and auto-playing media can be paused | Inspect media | Medium |
| A11-13 | Motion respects reduced-motion settings, and nothing flashes more than three times per second | Enable reduced motion | Medium |

### Understandable and robust
| ID | Check | Verify | Severity |
|---|---|---|---|
| A11-14 | Semantic structure: one H1, logical headings, landmarks, lists and tables with headers | Screen reader heading/landmark navigation | Medium |
| A11-15 | Every control has an accessible name, role and state (icon buttons included) | Screen reader pass | High |
| A11-16 | Form fields have programmatic labels. Errors are announced and associated with their field | Submit invalid with a screen reader | High |
| A11-17 | Dynamic updates (toasts, validation, live data) are announced appropriately | Screen reader | Medium |
| A11-18 | Page language is set, and consistent navigation and identification are used across pages | Inspect | Low |
| A11-19 | Authentication does not rely on a cognitive test alone (paste is allowed, alternatives to puzzles exist) | Try password managers and paste | Medium |
| A11-20 | Help and contact are in a consistent place (WCAG 2.2 3.2.6), and users are not asked twice for the same information in a process (3.3.7) | Inspect flows | Low |

### Native and document surfaces
| ID | Check | Verify | Severity |
|---|---|---|---|
| A11-21 | Native apps expose every control through the platform accessibility API with labels, traits and hints | Platform inspector | High |
| A11-22 | Emails, PDFs and exported documents are readable by assistive technology (real text, structure, alt text) | Inspect samples | Low |
| A11-23 | An accessibility statement exists with a contact route, where required or sold to public-sector or enterprise buyers | Look for it | Medium where legally required |

## Legal context

| Regime | Scope | Standard |
|---|---|---|
| European Accessibility Act | Many consumer-facing digital products and services in the EU (e-commerce, banking, e-books, transport, communications), in force since 28 June 2025. Micro-enterprises providing services are exempt | EN 301 549 (≈ WCAG 2.1 AA) |
| ADA (US) | Title III: courts routinely apply it to websites and apps. Title II: state/local government, WCAG 2.1 AA with phased deadlines | WCAG 2.1/2.2 AA in practice |
| Section 508 (US) | Federal agencies and their vendors | WCAG 2.0 AA |
| UK Equality Act; Public Sector Bodies Accessibility Regulations | Service providers; public sector | WCAG 2.2 AA (public sector) |
| Other national laws (e.g., AODA in Ontario) | Varies | WCAG 2.0/2.1 AA |

Legal applicability is reported through legal-audit. This table sets severity: where a regime applies, failures that block a core flow are Critical.

## Severity notes

Anything that makes a core journey impossible for a keyboard or screen-reader user is Critical and `core_flow: true`. Isolated contrast or labelling gaps outside core flows are Medium.
