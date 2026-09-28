# Cost audit

Can the product run without a surprise bill ending it? This covers spend visibility, caps, cost per user, and the usage-based amplifiers that turn a traffic spike or an abuse pattern into an invoice. For self-funded products, a runaway bill is a production incident.

- **Check prefix:** `CST`
- **Applies to:** every hosted surface and every metered third-party service (hosting, database, storage, bandwidth, email, SMS, AI/LLM APIs, maps, search, monitoring)
- **Not applicable when:** the product has no metered or paid dependencies

## Evidence

- **Automated:** the list of paid services from configuration and dependencies; provider usage and billing APIs where credentials allow; cost-related configuration (caps, quotas, rate limits).
- **Manual:** estimate cost per active user from provider pricing (anchored with links) and expected usage. Compare with the product's price (from the project's pricing page or any stated business model).

## Checks

### Visibility
| ID | Check | Verify | Severity |
|---|---|---|---|
| CST-01 | Every paid and metered service is inventoried, with its plan, pricing link and owner | Inventory | Medium |
| CST-02 | Billing alerts are set on every paid service at thresholds below the acceptable monthly spend | Provider settings (or not verified) | High |
| CST-03 | Cost per active user or per core action is estimated and is below what the product earns per user | Calculation shown in evidence | High for paid products |
| CST-04 | Free-tier limits and overage behaviour (hard stop vs. automatic billing) are known for each service | Provider docs | Medium |

### Caps and amplifiers
| ID | Check | Verify | Severity |
|---|---|---|---|
| CST-05 | Hard spend caps or usage limits are set where providers offer them (AI APIs, hosting spend management) | Provider settings | High |
| CST-06 | AI/LLM usage has per-user and global limits in the product, with model and context choices sized to the task (see AIF-14) | Code and config | High for AI products |
| CST-07 | Actions that send email, SMS or push, or call paid APIs, are rate-limited per user (cost and abuse vector) | Code | High |
| CST-08 | Known amplifiers are bounded: image transformations, egress on large media, function→webhook loops, log ingestion volume, unbounded exports | Config and code review | Medium |
| CST-09 | Free tiers and trials cannot be farmed cheaply (sign-up abuse, see SAF-09) | Signup protections | Medium |

### Efficiency
| ID | Check | Verify | Severity |
|---|---|---|---|
| CST-10 | Idle and unused resources are removed (stale environments, unattached volumes, forgotten preview deployments) | Provider inventory | Low |
| CST-11 | Storage has lifecycle rules (old exports, temporary files, orphaned uploads) | Config | Low |
| CST-12 | Committed or reserved pricing is considered only where usage is stable and known | Decision noted | Low |
| CST-13 | Cost is reviewed on a schedule, and spend per user is tracked over time | Process evidence | Low |

## Severity notes

No caps and no alerts on an uncapped metered service reachable by anonymous users (AI endpoints, SMS, email sends) is Critical, because one abuser can create an unbounded bill. Cost per user above revenue per user for a paid product is High and belongs in the business conversation, not only the infrastructure one.
