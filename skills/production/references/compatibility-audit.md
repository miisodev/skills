# Compatibility audit

Does the product work across the browsers, devices, operating systems, screen sizes, network conditions and versions its users actually have, and does it coexist with the systems it integrates with? A product that only works on its developers' machines is not ready.

- **Check prefix:** `CMP`
- **Applies to:** marketing site, web app, admin console, mobile app, desktop app, extension, public API/SDK/CLI (version compatibility)
- **Not applicable when:** never

## Evidence

- **Automated:** cross-browser end-to-end runs if configured; `browserslist` and build targets; device-farm results if available; API contract tests against old clients.
- **Manual:** core journeys on the support matrix, at minimum current Chrome, Safari (macOS and iOS), Firefox and Edge; a mid-range Android phone; the oldest supported OS versions for native apps. Throttle to slow 3G / high latency.

## Checks

### Support matrix
| ID | Check | Verify | Severity |
|---|---|---|---|
| CMP-01 | A support matrix (browsers, OS versions, devices, screen sizes) is defined and matches the audience (analytics or market data) | Document plus analytics | Medium |
| CMP-02 | Core journeys work on every browser in the matrix, with iOS Safari specifically tested | Walk on each | High; Critical if a major browser fails a core flow |
| CMP-03 | Core journeys work on the oldest supported OS/app-platform versions and on low-end devices | Oldest emulator plus a real low-end device | High |
| CMP-04 | Unsupported browsers and OS versions get a clear message, not a blank or broken page | Old browser/emulator | Low |

### Environments and conditions
| ID | Check | Verify | Severity |
|---|---|---|---|
| CMP-05 | Works on slow, high-latency and flaky networks without hanging or corrupting state | Throttle; toggle offline | High |
| CMP-06 | Works with common privacy settings and extensions (ad/tracker blockers, strict cookie modes, third-party cookies disabled) | Enable a blocker; strict mode | High if auth or checkout breaks |
| CMP-07 | Works in in-app browsers (social apps, email clients) for any links shared there, especially auth and payment links | Open from a social/email app | Medium |
| CMP-08 | Handles device settings: dark mode, large text, reduced motion, landscape, split screen or foldables where relevant | Toggle each | Low |
| CMP-09 | Printing or exporting to PDF works for pages users need on paper (invoices, receipts, tickets) | Print preview | Low |

### Versions and interoperability
| ID | Check | Verify | Severity |
|---|---|---|---|
| CMP-10 | Deployments stay compatible with clients still running the previous version (cached SPAs, old app builds, old SDKs) | Old client against new backend | High |
| CMP-11 | Data and file formats the product imports or exports interoperate with the tools users pair it with (CSV encodings, calendar, spreadsheets) | Round-trip with a common tool | Medium |
| CMP-12 | Integrations work against the current versions of the third-party APIs, and deprecation notices are handled | Provider changelogs vs. integration code | Medium |

## Severity notes

Breakage on a platform that serves a significant share of users (per analytics or market data) in a core flow is Critical. Where no analytics exist, treat Chrome, Safari/iOS and Android Chrome as major.
