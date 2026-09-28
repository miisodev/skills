# UX audit

Can people understand the product and get what they came for without friction, confusion or dead ends? This part covers information architecture, navigation, flows, forms, feedback and errors as experienced. design-audit covers whether each screen and component is *finished*. accessibility-audit covers use by everyone. content-audit covers the words.

- **Check prefix:** `UX`
- **Applies to:** marketing site, web app, admin console, mobile app, desktop app, extension; the developer experience of public APIs, CLIs and SDKs (read "user" as "developer")
- **Not applicable when:** the product has no human-facing surface

## Evidence

- **Automated:** analytics funnels and drop-off (if accessible), session-replay tools already installed, rage-click/error-click reports.
- **Manual:** heuristic walkthrough of every critical journey as a first-time user at 375 px, tablet and desktop widths, or on real devices for apps. Attempt each journey with mistakes, and try to recover.

## Checks

### Navigation and structure
| ID | Check | Verify | Severity |
|---|---|---|---|
| UX-01 | Core actions are reachable within about three steps from anywhere relevant | Walk from each main area | High |
| UX-02 | Navigation labels are clear to a first-time user and the current location is always visible | Heuristic review | Medium |
| UX-03 | Navigation works and behaves consistently at every supported size and input method | Test at small, medium and large sizes, and with touch | High |
| UX-04 | Every deep flow has a visible way back or out | Enter each flow, try to leave | Medium |
| UX-05 | Search is available where content volume needs it and handles no-results helpfully | Queries with and without results | Medium |

### Flows
| ID | Check | Verify | Severity |
|---|---|---|---|
| UX-06 | Signup and login are short, with no unnecessary fields, and social or passwordless options work where offered | Walk it; count fields and steps | High |
| UX-07 | Onboarding delivers first value quickly and explains what the product needs from the user | Time to first value on a fresh account | High |
| UX-08 | Multi-step flows show progress, preserve input across steps and allow going back | Walk, go back, refresh | Medium |
| UX-09 | Users recover from mistakes without starting over (undo, edit, back) | Make mistakes deliberately | High |
| UX-10 | No dead ends: every state offers a next action | Look for pages with no forward path | High |
| UX-11 | Checkout or upgrade asks for nothing unnecessary and is clear about price and what the user gets | Walk the purchase flow | Critical if purchase is a core flow |

### Forms and input
| ID | Check | Verify | Severity |
|---|---|---|---|
| UX-12 | Every field has a persistent visible label. Placeholders show examples, never serve as labels | Inspect forms | Medium |
| UX-13 | Validation is inline (on blur) with specific, actionable messages, plus a summary on submit | Submit invalid data | Medium |
| UX-14 | Input is preserved on error, timeout and back navigation | Fail a submit, go back | High |
| UX-15 | Correct input types, autocomplete attributes and password-manager support | Inspect markup; try autofill on mobile | Medium |
| UX-16 | Requirements (format, length, why it is needed) are shown before the user fails them | Inspect complex fields | Low |

### Feedback and errors
| ID | Check | Verify | Severity |
|---|---|---|---|
| UX-17 | Every action gives immediate feedback, and long operations show progress | Trigger each main action | High |
| UX-18 | Error messages say what happened and what to do, in plain language, with no codes or stack traces | Force errors (invalid input, offline, server error) | High |
| UX-19 | 404, 500 and offline pages are helpful, branded and link somewhere useful | Visit a bad URL; simulate outage | Medium |
| UX-20 | Transient failures offer retry; a partial failure never looks like success | Throttle or kill network mid-action | High |
| UX-21 | Component failures are contained (error boundaries), not whole-page crashes | Force a component error | Medium |

### Mobile and touch
| ID | Check | Verify | Severity |
|---|---|---|---|
| UX-22 | Touch targets are at least 44×44 pt / 48×48 dp with adequate spacing | Inspect on device | Medium |
| UX-23 | The on-screen keyboard never covers the active input; safe areas are respected | Real device, notched phone | Medium |
| UX-24 | No horizontal overflow at 320–375 px; modals scroll-lock the background | Narrow viewport | Medium |

### Trust signals
| ID | Check | Verify | Severity |
|---|---|---|---|
| UX-25 | Contact/support route, policy links and company identity are visible where users decide to trust (signup, checkout) | Inspect those pages | Medium |
| UX-26 | Payment and data-entry pages show why they are safe (recognised payment UI, HTTPS, clear data use) | Inspect | Medium |

## Severity notes

Friction in the core journey (signup, first value, purchase) is at least High and `core_flow: true`. Where analytics show a large drop-off at a step, cite the numbers as evidence. For API/CLI/SDK surfaces, apply UX-06 to UX-10 and UX-17 to UX-20 as developer experience: time to first successful call, error messages that name the fix, and a quickstart that works when copied as written.
