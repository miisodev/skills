# Analytics audit

Will the team know whether the product is working as a business: who arrives, who activates, who pays, who stays, and why? Without trustworthy product analytics, every post-launch decision is a guess. Runtime health is in observability-audit, and consent rules in privacy-audit.

- **Check prefix:** `ANL`
- **Applies to:** marketing site, web app, mobile app, desktop app, extension; server-side events from the backend and billing
- **Not applicable when:** the product deliberately collects no usage data. Record that as a decision, and still apply ANL-05 for revenue

## Evidence

- **Automated:** analytics SDK initialisation per surface and environment; the event names and properties defined in code; the tracking plan if one exists.
- **Manual:** perform the core journey on a non-production environment with the network inspector open and confirm each event fires once with correct properties; where access exists, confirm events arrive in the analytics project.

## Checks

### Setup
| ID | Check | Verify | Severity |
|---|---|---|---|
| ANL-01 | Analytics is installed on each user-facing surface, pointing at the production project, with environments separated | Config | Medium |
| ANL-02 | A tracking plan names every event, its trigger and its properties, and the code matches it | Plan vs. code | Low |
| ANL-03 | Internal, test and bot traffic is excluded or flagged | Filters; config | Medium |

### Coverage
| ID | Check | Verify | Severity |
|---|---|---|---|
| ANL-04 | Core lifecycle events fire exactly once with correct properties: signup, activation (the first core value action), key feature use, checkout started, purchase, cancellation | Network inspection | High |
| ANL-05 | Revenue events come from the server or billing provider (not the client) and reconcile with the provider (BIL-20) | Code; compare a sample | Medium |
| ANL-06 | Acquisition, activation, conversion and retention funnels are defined and measurable step by step | Funnel definitions | Medium |
| ANL-07 | Attribution (UTM parameters, referrer, campaign) is captured and carried through to signup | Test link with UTM | Low |
| ANL-08 | The product's success measures (from the project's stated requirements, wherever they live) can be answered from the data | Map each metric to events | Medium |
| ANL-09 | Client and server events are not double-counted, and identity is stitched across anonymous → signed-in and across devices | Inspect identify calls | Medium |

### Integrity and compliance
| ID | Check | Verify | Severity |
|---|---|---|---|
| ANL-10 | Analytics respects consent where required (PRV-05) and platform tracking rules (e.g., iOS App Tracking Transparency) | First-load inspection; app flows | High in consent regimes |
| ANL-11 | No personal data in event properties or URLs sent to analytics (PRV-09) | Inspect payloads | High |
| ANL-12 | Data retention in analytics tools is set to match the privacy policy | Tool settings (or not verified) | Low |
| ANL-13 | Experiments (if used) log assignments, avoid flicker, and have a documented analysis method | Config | Low |
| ANL-14 | Event names are stable: renaming is versioned so history is not broken | Code history; plan | Low |

## Severity notes

Missing activation and purchase events on a launched product is High because the team cannot see whether it works. Analytics firing without consent in a consent regime is Critical under privacy-audit, not here. Record it there and cross-reference.
