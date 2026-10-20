# Real-time and event systems audit

Can persistent sessions and event flows maintain authority, bounded resources and correct effects under delay, replay and disconnect? Apply reliability/data/API checks too.

- **Check prefix:** `RTM`
- **Applies to:** WebSocket/SSE, pub-sub, collaboration sessions, multiplayer backends, streaming media and event-driven pipelines
- **Not applicable when:** the product has no persistent streams, interactive sessions or event-processing path

## Evidence

Use controlled producers/consumers, a slow client, disconnect/replay fixtures and realistic messages. Capture sequence IDs, delivery semantics, queue lag and memory use. Capacity tests belong in a non-shared test environment.

## Checks

### Connection and access

| ID | Check | Verify | Severity |
|---|---|---|---|
| RTM-01 | Each connection, subscription and message action is authenticated/authorized at its boundary | Connect as users A/B; attempt another channel and forbidden publish | Critical |
| RTM-02 | Expired or revoked credentials stop future access on existing streams | Revoke mid-stream; attempt publish and subscribe | Critical |
| RTM-03 | Reconnect resumption neither skips required events nor duplicates non-idempotent effects | Disconnect around acknowledgement and resume from cursor | High |
| RTM-04 | Dead peers and half-open connections are detected with bounded resource retention | Simulate a silent peer and observe cleanup | Medium |
| RTM-05 | Stream shutdown, deploy draining and client version changes preserve supported sessions | Deploy in a lab with active clients on old/new versions | High |

### Flow and semantics

| ID | Check | Verify | Severity |
|---|---|---|---|
| RTM-06 | Delivery, ordering and durability guarantees are explicit at producer, broker and external sink | Trace an event end to end; distinguish broker guarantees from side effects | High |
| RTM-07 | Slow consumers trigger backpressure, bounded buffering or an explicit loss policy | Pause a consumer; measure memory, dropped events and recovery | High |
| RTM-08 | Retries, poison messages and dead letters have bounded handling and safe replay | Inject malformed messages and replay corrected fixtures | High |
| RTM-09 | Schema evolution is compatible with retained events and supported consumers | Replay older event fixtures against the current consumer | High |
| RTM-10 | Transactions or deduplication protect external side effects across crash/retry boundaries | Crash between effect and offset/checkpoint commit | Critical |
| RTM-11 | Partitioning and consumer coordination preserve the required business ordering | Rebalance consumers during conflicting updates | High |
| RTM-12 | Lag, queue depth and end-to-end freshness alert before the user-facing objective fails | Inspect metrics and a delayed-processing test | High |

### Interactive and media behavior

| ID | Check | Verify | Severity |
|---|---|---|---|
| RTM-13 | Latency, jitter and loss targets follow the use case rather than generic page-load targets | Measure interaction/tick/media delays on supported networks | High |
| RTM-14 | Server authority or equivalent validation rejects impossible client state transitions | Try invalid gameplay/collaboration commands in a test session | Critical |
| RTM-15 | Presence and membership cleanup do not leave ghost users or reveal private rooms | Disconnect abruptly; revoke membership; inspect discovery/presence | Medium |
| RTM-16 | Media pipelines handle codec/device changes, denied permissions and relay failure | Exercise supported media devices and a failed relay in a lab | High |
| RTM-17 | Recording, chat and live user content honor privacy, moderation and retention commitments | Trace consent, reporting and deletion on test content | High |
| RTM-18 | Fan-out, hot partitions and connection counts have tested limits and overload behavior | Inspect capacity evidence and controlled peak scenarios | High |

## Severity notes

Cross-room data disclosure and duplicate financial or destructive effects are Critical. Invalid game state is Critical only when it destroys core fairness or valuable state; downgrade harmless cosmetic divergence. Hard real-time and life-critical deadlines need domain validation beyond these checks.

## Sources

Reviewed 2026-10-20. These sources inform the controls; the table is an engineering checklist, not a conformance certificate. Apply version-specific requirements only to versions the product claims.

- [Apache Kafka design](https://kafka.apache.org/41/design/design/): end-to-end delivery, ordering and processing boundaries.
- [WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket): lack of automatic backpressure in the browser API; buffering must be addressed by the application. Media and interactive scenarios are engineering tests for advertised capabilities, not claims of protocol certification.
