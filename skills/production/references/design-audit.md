# Design audit

Is the interface *finished*? Beauty is a separate question. A design is complete when no reasonable user action, system state, data state, permission state, network state or failure state leaves the user uncertain about where they are, what is happening, what they can do, what happens next, or how they recover. This part is independent of visual style: a minimal product and a dense one can both pass. What neither can do is leave states undesigned.

- **Check prefix:** `DES`
- **Applies to:** marketing site, web app, admin console, mobile app, desktop app, extension
- **Not applicable when:** the product has no graphical interface

## Evidence

- **Automated:** component library or storybook inventory; design-token usage (search for hard-coded colours and spacing); visual-regression results if present.
- **Manual:** force every state on core screens: empty account, one item, many items, extreme content, loading (throttled network), error (blocked request), offline, read-only role, no-permission role. Compare every screen against the product's own best screen for consistency.

## Checks

### States
| ID | Check | Verify | Severity |
|---|---|---|---|
| DES-01 | Every data view has designed **loading** states (skeletons or progress sized like the content) with no layout jump | Throttle network | Medium |
| DES-02 | Every data view has an **empty** state that explains why and offers the first action, distinct from "no results for this filter" | Empty account; filter to nothing | High on core screens |
| DES-03 | Every data view has an **error** state with recovery (see UX-18) | Block the request | High on core screens |
| DES-04 | **Restricted** (no permission) and **read-only** states are designed, not just hidden buttons | Low-privilege role | Medium |
| DES-05 | **Offline** and degraded-network states are designed where the surface can be used offline or on mobile | Airplane mode | Medium |
| DES-06 | **Success** confirmation is visible for every consequential action | Complete actions | Medium |

### Component completeness
| ID | Check | Verify | Severity |
|---|---|---|---|
| DES-07 | Buttons/actions have default, hover, focus-visible, pressed, loading, disabled (with reason) and error states | Interact; keyboard-focus each | Medium |
| DES-08 | Inputs have empty, focus, filled, valid, invalid, disabled, read-only and async-validating states | Interact | Medium |
| DES-09 | Cards and list items handle long text, missing images, and hover/selected states without breaking | Extreme content | Medium |
| DES-10 | Dialogs trap and return focus, show submitting, error and success states, and say what is lost on close | Open, submit, fail, close | Medium |
| DES-11 | Navigation items show the current location, focus and badge states | Inspect | Low |

### Data surfaces
| ID | Check | Verify | Severity |
|---|---|---|---|
| DES-12 | Tables, lists and dashboards look intentional at 0, 1–3, typical, hundreds-plus and extreme volumes | Seed each volume | Medium |
| DES-13 | Long strings, large numbers and many columns truncate gracefully, with the full value available | Extreme content | Medium |
| DES-14 | Charts have labels, legends and non-colour differentiation, and read at small sizes | Inspect | Medium |

### Trust and recovery in the interface
| ID | Check | Verify | Severity |
|---|---|---|---|
| DES-15 | Save/sync status is visible wherever users create or edit | Edit and watch | High on core screens |
| DES-16 | Destructive actions have confirmation proportional to damage, or undo | Delete things | High |
| DES-17 | History, ownership and permission context are visible where users need them to trust the data | Inspect shared or collaborative objects | Low |

### Consistency and finish
| ID | Check | Verify | Severity |
|---|---|---|---|
| DES-18 | Repeated patterns (buttons, dialogs, forms, creation and deletion flows) behave identically everywhere | Compare across areas | Medium |
| DES-19 | A design system or token set exists and is used, with no one-off colours, sizes or spacing on core screens | Search code for hard-coded values | Low |
| DES-20 | No screen looks placeholder-like, unbalanced or unexplained-empty. Empty space is deliberate, not missing content | Visual review of every core screen | Medium |
| DES-21 | Every major page answers within seconds: where am I, what is this for, what matters, what can I do, what next | Five-second review per page | Medium |
| DES-22 | Light/dark themes (if offered) are both complete, including states, charts and images | Switch theme on each core screen | Medium |

## Completeness score

For each core screen or flow, also give a 0–5 score on eight dimensions: structure, visual completeness, interaction, workflow, state coverage, accessibility, trust and consistency (40 in total). Record it in the check's evidence for DES-21 or in the surface notes.

| Total | Level | Release implication |
|---|---|---|
| 38–40 | Exceptional | Benchmark |
| 34–37 | Mature | Target for core flows |
| 28–33 | Productized | Minimum for public release |
| 20–27 | Functional | Internal/beta only |
| < 20 | Prototype | Not releasable |

A core flow scoring below 28 is a High finding.

## Severity notes

The fix for a sparse screen is **useful** context (metadata, status, history, next steps), never filler. Do not raise findings that would push a deliberately minimal design toward clutter. A missing state that loses user data or money (no save indicator on an editor that silently fails, say) is Critical.
