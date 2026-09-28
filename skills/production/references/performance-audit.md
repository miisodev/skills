# Performance audit

Is the product fast and responsive for real users on real devices and networks, and does it stay that way under expected load? Speed drives conversion, retention and search ranking. A slow core flow is a product defect, not a polish item.

- **Check prefix:** `PRF`
- **Applies to:** marketing site, web app, admin console, public API, mobile app, desktop app, extension, background jobs (throughput)
- **Not applicable when:** never

## Evidence

- **Automated:** Lighthouse (mobile profile) on core pages; field data from the Chrome UX Report or the product's real-user monitoring; bundle analysis for the framework in use; API latency percentiles from observability; database slow-query logs; platform profilers for native apps.
- **Manual:** core journeys on a mid-range phone over a throttled network; interaction responsiveness on heavy screens; cold-start timing for apps and serverless functions.
- **Needs owner approval:** load tests against shared or production environments (see REL-10).

## Checks

### Web vitals (at the 75th percentile, mobile)
| ID | Check | Verify | Severity |
|---|---|---|---|
| PRF-01 | LCP < 2.5 s on core pages | Field data first, lab if none | High on core/landing pages |
| PRF-02 | INP < 200 ms on interactive screens | Field data or manual profiling | High |
| PRF-03 | CLS < 0.1; images and embeds reserve space; fonts don't shift layout | Lighthouse, visual check | Medium |
| PRF-04 | TTFB < 800 ms; HTML is cached or streamed where possible | Measure from target regions | Medium |

### Frontend weight
| ID | Check | Verify | Severity |
|---|---|---|---|
| PRF-05 | JavaScript shipped on initial load is justified: code-split routes, heavy modules lazy-loaded, no duplicate libraries | Bundle analyzer | Medium |
| PRF-06 | Images are responsive, compressed and served in modern formats; the LCP image is prioritised and below-fold images lazy-loaded | Inspect | Medium |
| PRF-07 | Third-party scripts (analytics, chat, tag managers, A/B tools) are deferred and their cost is measured | Performance panel / request waterfall | Medium |
| PRF-08 | Fonts are subset, preloaded where critical, and use `font-display` | Inspect | Low |
| PRF-09 | Static assets are served from a CDN with long-lived cache headers and hashed filenames | Response headers | Medium |
| PRF-10 | Animations use compositor-friendly properties and hold frame rate on mid-range devices | Performance panel | Low |

### Backend and API
| ID | Check | Verify | Severity |
|---|---|---|---|
| PRF-11 | API p95 latency is within target for core endpoints (typical guide: reads < 500 ms, writes < 800 ms, search < 1 s) | Observability or measurement | High on core flows |
| PRF-12 | No N+1 query patterns on list and detail endpoints | Query logs; ORM inspection | Medium |
| PRF-13 | Hot queries use indexes; there are no sequential scans on large tables (see DAT-07) | `EXPLAIN` on top queries | High |
| PRF-14 | Caching exists where data is read far more than written (HTTP, CDN, application cache), with correct invalidation | Inspect | Medium |
| PRF-15 | Every list endpoint and query is bounded (pagination, limits) | Route inventory | High |
| PRF-16 | Serverless/container cold starts on core routes are measured and acceptable | Measure after idle | Medium |
| PRF-17 | Slow work (email, exports, AI calls, media processing) runs asynchronously with progress, not in the request | Inspect handlers | Medium |

### Native and other surfaces
| ID | Check | Verify | Severity |
|---|---|---|---|
| PRF-18 | App cold start, time to interactive and scroll/frame rate meet targets on a low-end supported device | Platform profiler | High |
| PRF-19 | App binary/download size is reasonable for the market (cellular download limits, install conversion) | Build output | Low |
| PRF-20 | Memory, CPU and battery use at idle and in core flows are reasonable; no leaks over a long session | Profiler over a 15-minute session | Medium |
| PRF-21 | Background jobs keep up with expected volume; queue latency is bounded | Queue metrics | Medium |

### Budgets
| ID | Check | Verify | Severity |
|---|---|---|---|
| PRF-22 | Performance budgets or regression checks run in CI (Lighthouse CI, bundle-size limits, benchmark tests) | CI config | Low |

## Severity notes

Use field data over lab data when it exists and say which you used. A core page failing two or more vitals is High. A landing page failing them hurts acquisition and search (SEO-12). Where the product serves markets with low-end devices or slow networks, grade against those conditions.
