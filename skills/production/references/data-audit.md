# Data audit

Is the data correct, isolated, performant, protected and clean? The product can lose a server without losing data, no query can cross a tenant boundary, and production contains only real data. Backups and restores are in reliability-audit, and legal obligations about personal data in privacy-audit.

- **Check prefix:** `DAT`
- **Applies to:** every data store behind any surface: databases, file/object storage, caches, search indexes, queues, analytics warehouses, on-device storage (native apps also: MOB-05)
- **Not applicable when:** the product stores no data

## Evidence

- **Automated:** schema and migration files; database platform advisors/linters; the unindexed-foreign-key query for the database in use; slow-query statistics; migration state per environment.
- **Manual:** read the schema for integrity gaps; with test credentials per role, test isolation policies directly (anonymous, user A, user B, service); search production-facing data for test records where read access exists.

## Checks

### Integrity
| ID | Check | Verify | Severity |
|---|---|---|---|
| DAT-01 | Constraints enforce the rules the code relies on: foreign keys with deliberate `ON DELETE`, `NOT NULL`, uniqueness on natural keys, checks/enums for bounded values | Schema review | High |
| DAT-02 | Money is stored as integer minor units or exact decimals, never floats | Schema | Critical where money is stored |
| DAT-03 | Timestamps are stored in UTC with time-zone awareness | Schema | Medium |
| DAT-04 | Soft-delete (if used) is applied consistently on every read path | Code search | High |

### Migrations
| ID | Check | Verify | Severity |
|---|---|---|---|
| DAT-05 | Every schema change is a committed migration applied automatically, in order, with identical state across environments | Migration table per environment | High |
| DAT-06 | Destructive changes follow expand-and-contract; long migrations on large tables avoid blocking locks; each has a rollback or restore point | Migration review | High |

### Performance and capacity
| ID | Check | Verify | Severity |
|---|---|---|---|
| DAT-07 | Hot query paths are indexed, including every foreign-key column; top queries show no sequential scans on large tables | `EXPLAIN`; unindexed-FK query | High |
| DAT-08 | Connection pooling suits the runtime (essential for serverless), and pool sizes fit database limits across all services | Config | High |
| DAT-09 | Growth is planned: large and append-heavy tables have archival/TTL strategies; storage alerts precede limits | Size estimates; config | Medium |

### Isolation
| ID | Check | Verify | Severity |
|---|---|---|---|
| DAT-10 | Where the database enforces isolation (e.g., Postgres row-level security), it is **enabled** on every table with user data and covers select, insert, update and delete | Policies; platform advisor | Critical |
| DAT-11 | Isolation holds per role: anonymous sees nothing private; user A cannot read or write B's rows; inserts cannot claim another owner | Per-role tests | Critical |
| DAT-12 | Privileged/service credentials that bypass isolation are used only server-side and never reach clients | Code; bundles | Critical |
| DAT-13 | Object storage has its own access rules, and private files are not publicly guessable or listable | Try direct URLs | Critical for private user files |
| DAT-14 | Views, functions and stored procedures respect isolation (definer vs. invoker rights chosen deliberately) | Review | High |
| DAT-15 | Caches and search indexes do not leak data across users or tenants (cache keys include identity where needed) | Review | High |

### Protection
| ID | Check | Verify | Severity |
|---|---|---|---|
| DAT-16 | Connections to data stores use TLS | Connection config | High |
| DAT-17 | Encryption at rest is enabled; secrets and tokens the product stores are hashed or encrypted | Platform settings; schema | High |
| DAT-18 | Direct database access is limited to named people and systems, with no shared credentials or public endpoints without need | Access config | High |

### Hygiene
| ID | Check | Verify | Severity |
|---|---|---|---|
| DAT-19 | Account deletion removes or anonymises the user's data across the database, storage, search, caches and third parties | Delete a test account; inspect | High |
| DAT-20 | No test, seed or demo data in production; internal accounts are flagged and excluded from metrics | Query production (read-only) where permitted | Medium |
| DAT-21 | Retention is implemented, not just written: expired sessions, logs, soft-deleted rows and temporary files are actually purged | Scheduled jobs | Medium |
| DAT-22 | Data exports (user- or admin-facing) include only permitted data and are access-controlled and expiring | Test | High |

## Severity notes

Isolation disabled on a table containing user data, or a privileged key in a client, is Critical. Float money is Critical because errors accumulate silently.
