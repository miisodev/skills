# Product and platform routing

Select checks from capabilities, data and failure impact, not a product label. Start with functional, compatibility, engineering, security and launch; assess each other part for applicability. A component can have multiple surfaces. Apply identity to local privileges and device ownership as well as login screens. UX means developer/operator experience for headless products. No billing, marketing site, telemetry, account system, browser, cloud or particular stack is required.

Use this table to avoid missing specialized boundaries. The named parts are additions to applicable general parts, not exhaustive presets; use part IDs from the payload schema in `run.parts_in_scope`.

| Product or behavior | Additional parts to inspect | Evidence that changes the audit |
|---|---|---|
| Static/content site | accessibility, content, SEO, privacy | Real pages, publishing path, external scripts; no invented database/billing requirement |
| SaaS, internal/admin tool, commerce or marketplace | identity, data, API, deployment; billing/messaging/safety when present | Tenant/role boundaries, entitlements and money flows, operator access; internal users still need usable and accessible flows |
| MCP server, client, host or gateway | mcp, package, deployment, supply-chain; agent/AI only when implemented | Role, transport, protocol revision, host matrix, tool/resource authority, upstream credentials; separate local stdio from protected HTTP |
| Agent/automation platform | agent, AI where model-backed, MCP where implemented, cost, observability | Delegated identity, policy enforcement, task effects, schedules, aggregate budgets, checkpoints and stop/revoke behavior |
| CLI, SDK, library, plugin, editor extension or developer tool | package, supply-chain, extension where embedded, compatibility | Actual packed artifact, clean import/install, non-TTY output, host/runtime ABI, permission model; apply accessibility to human interaction |
| Self-hosted, on-premises, appliance or air-gapped software | deployment, supply-chain, reliability, support | Customer installation and upgrade, persistent volumes, minimum resources, reverse proxy, disconnected mode; author's hosted demo is insufficient |
| Mobile, desktop, PWA or local-first editor | mobile/desktop as applicable, sync where offline/replicated, data, accessibility | Shipped binary/app, local save/restore, OS permission lifecycle, supported devices, unsynced upgrades and account switching |
| Messaging, collaborative workspace, live media or multiplayer backend | realtime, safety, privacy, reliability, data | Per-channel authorization, reconnect/replay, lag, backpressure, authoritative state, abuse/reporting and recording consent |
| Batch worker, event processor, analytics/ETL or search service | data, reliability, realtime where streaming, observability, cost | Source/sink contracts, freshness, lineage, correction/deletion, poison records, backfills and reconciliation |
| Model training, inference or recommendation service | AI, data, supply-chain, performance, cost, safety | Dataset rights/lineage, cohort quality, drift, feature compatibility, model rollback, out-of-distribution handling |
| Games, consoles, XR, kiosks or spatial experiences | compatibility, performance, accessibility, safety; realtime/device when present | Real input devices, frame/tick pacing, resume, saves, motion/physical context and platform-specific requirements; do not replace these with browser tests |
| Embedded/IoT, device companion or physical control | device, deployment, security, reliability, supply-chain | Firmware/board matrix, device identity, pairing, authenticated updates, loss of power/network, simulated safe outputs |
| Regulated, financial, health, industrial or other high-consequence software | safety, legal, privacy, security, data, reliability, plus relevant platform parts | Establish jurisdiction, intended use, harm and applicable standards with specialist owners; product-specific checks and independent evidence are required |

## Boundaries and gaps

- Inventory producer/consumer, local/remote, operator/customer and physical/software boundaries separately. A game may have client, matchmaking, chat, store and dedicated-server surfaces. An MCP may have stdio, HTTP, a hosted UI and an upstream data service.
- Read each applicable `*-audit.md` from the parts table. Shared checks still apply to new surface kinds even where an older reference names only web/native examples. Web-only checks (DOM, cookies, CSP, page-load timings) are inapplicable to a headless process; record the reason instead of forcing them onto it.
- For human interfaces without a DOM use platform accessibility and interaction evidence. For background systems use latency/freshness/throughput objectives; for games/media use frame/tick/jitter objectives. Derive thresholds from requirements and risk, not a universal target.
- Record the release artifact, runtime, deployment model, protocol revisions and hardware tested in `run.environments_examined` and `surfaces[].notes`. Put unreachable surfaces, hardware and provider settings in limitations and relevant checks as `not_verified`.
- Add custom IDs under the closest existing part for risks unique to a product: e.g. `SAF-C01` for actuator interlock evidence or `DAT-C01` for financial reconciliation. State the standard/source, applicability, test and impact in evidence and findings. A custom check is not certified coverage of the whole domain.
- A broad audit cannot establish medical, aviation, automotive, industrial, payment-network or console certification by itself. Missing required specialist evidence on a critical/core risk holds the decision; the audit cannot silently declare such evidence inapplicable.
