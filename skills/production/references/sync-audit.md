# Offline and synchronization audit

Does work remain durable and authorized when devices disagree or the network disappears? A merge algorithm alone does not prove domain invariants or access control.

- **Check prefix:** `SYN`
- **Applies to:** offline-capable web/native apps, local-first products, replicated files and collaboration stores
- **Not applicable when:** the product has neither offline writes nor replicated client state

## Evidence

Use two disposable devices/profiles and controlled partitions. Inspect local durability, operation logs, merge rules and authorization on reconnection. Repeat scenarios across old/new app versions and clock skew.

## Checks

### Durability and convergence

| ID | Check | Verify | Severity |
|---|---|---|---|
| SYN-01 | Offline capabilities and limits match the product promise | Disconnect before launch and during each advertised core action | High |
| SYN-02 | Saved work survives crash or power interruption before synchronization | Kill the process after save and reopen the local store | Critical |
| SYN-03 | Concurrent edits converge according to documented conflict rules without silent loss | Edit the same object on disconnected clients, reconnect in both orders | Critical |
| SYN-04 | Delete/edit conflicts and tombstone expiry do not resurrect deleted private data | Delete offline on one device and edit on another; reconnect after retention | Critical |
| SYN-05 | Duplicate and reordered operations preserve application invariants | Replay a fixture operation log with duplicates and reordered deliveries | High |
| SYN-06 | Clock skew does not silently decide ownership or discard newer intent | Shift client clocks and compare final state | High |
| SYN-07 | Queued attachments and metadata remain consistent across interrupted transfer | Interrupt upload/download and resume; verify hashes and references | High |
| SYN-08 | Local schema upgrades preserve unsynced work and support the declared version window | Upgrade with pending writes; reconnect an older client | High |

### Identity and lifecycle

| ID | Check | Verify | Severity |
|---|---|---|---|
| SYN-09 | Revoked access is enforced when offline work reconnects; rejected writes are visible | Revoke membership while offline and synchronize test changes | Critical |
| SYN-10 | Account switching cannot expose another account local records or pending operations | Switch profiles with pending work and inspect storage/requests | Critical |
| SYN-11 | Local caches, keys and exported replicas match the privacy and encryption promise | Inspect storage, backup and key lifecycle | High |
| SYN-12 | Partial sync and filters enforce permission boundaries before data reaches devices | Request another tenant partition and inspect local replicas | Critical |
| SYN-13 | A lost device can be revoked and its limitations are disclosed | Revoke a test device and test reconnect; document offline revocation limits | High |
| SYN-14 | Resync/reset repair corruption without discarding the only copy of unsynced work | Corrupt a disposable replica; run repair and compare recovered work | High |

### Experience and scale

| ID | Check | Verify | Severity |
|---|---|---|---|
| SYN-15 | Pending, synced, failed and conflicting work are distinguishable and recoverable | Exercise each state and resolve a conflict | Medium |
| SYN-16 | Backlogs, replication logs and caches are bounded without deleting needed history | Use long-offline fixtures; inspect compaction and quota behavior | High |
| SYN-17 | Reconnect uses bounded retries and does not overload peers or servers | Reconnect a controlled group of clients in a lab | High |
| SYN-18 | Export/import and service shutdown preserve useful access to owned data as promised | Round-trip a representative document without the sync service | High |

## Severity notes

Silent loss of committed work, unauthorized replication and deleted private data returning are Critical. A product that explicitly does not support offline writes can mark those rows inapplicable, but still assess its cached-data privacy and reconnect behavior.

## Sources

Reviewed 2026-10-20. These sources inform the controls; the table is an engineering checklist, not a conformance certificate. Apply version-specific requirements only to versions the product claims.

- [Ink & Switch local-first research](https://www.inkandswitch.com/essay/local-first/): offline access, collaboration, ownership and preservation principles. The partition, conflict, revocation and repair scenarios operationalize those principles as engineering judgments; they do not require CRDTs.
- [Apache Kafka delivery semantics](https://kafka.apache.org/41/design/design/): useful contrast for replay and duplicate handling; do not assume broker guarantees prove client convergence.
