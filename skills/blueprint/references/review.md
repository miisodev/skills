# Review

Review happens twice: once as the Review stage of each document, before the owner is asked to approve it, and again across the whole blueprint when the last document is approved, when anything is revised, or when someone asks for a check. The aim is a set of documents that are **true, decided, consistent and within their boundary**. Fix what you can. Take what needs the owner to them in one batch, each item with your recommendation.

## 1. Challenge

Before checking form, test the substance. Read the draft as each of these readers and write down the strongest objection each would raise:

- **A skeptical investor:** is the market real and reachable, do the economics work, and why will this team win?
- **An experienced operator in this category:** what has been missed about how customers buy, how the work gets done, or what it costs to serve and support?
- **A target user:** would I recognise my problem here? Would I switch? What would stop me?
- **The builder:** could I make good decisions from this, and is anything here deciding things that should be mine?

Resolve each objection with evidence, a change to the draft, or an explicit decision by the owner recorded in the workbook. An objection that cannot be resolved becomes an assumption with a validation plan, or a risk in `plan.md`.

## 2. Boundary: has the build crept in?

For each sentence ask: *could a capable builder produce this well from the rest of the blueprint?* If yes, cut it, or rewrite it as the requirement it serves.

Signals worth searching for, then reading around each hit:

| Signal | Usually means |
|---|---|
| Hex colours, px/rem sizes, spacing values | Design tokens. Keep only colours or typefaces the owner has fixed, in `brand.md` |
| Paths like `/api/…`, HTTP verbs, table or column names, SQL, JSON shapes | Architecture, API or schema design |
| "button", "modal", "screen", "page", "tab", "sidebar", "dashboard shows" | Interface design. Rewrite as the outcome the user needs |
| "the user clicks… then…" | Flow design. Keep the outcome and its conditions |
| Headlines, taglines beyond the name, full paragraphs of product copy | Copywriting. Keep voice traits and sample lines |
| Library pins with no reason; version numbers; transcribed price tables | Over-specified stack. Anchor it or give criteria |

Keep an owner's decision that protects something only they can judge, phrased as the requirement.

## 3. Register: status, history and hedges

Approved documents contain none of these. Move them to the workbook, or resolve them:

- **Status:** "currently", "not yet", "so far", "in progress", "done", "WIP", ✅/❌, "(shipped)"
- **History:** "we decided", "originally", "after trying", "moved from", "v2", "previously"
- **Hedges and open items:** "TBD", "TBC", "maybe", "consider", "might", "?", "open question"
- **Filler that fits any project:** "seamless", "delightful", "best-in-class", "innovative", "user-friendly", "scalable"

## 4. Figures: one number, one home, one source

1. List every number across the documents: prices, sizes, rates, costs, targets, budgets, horizons.
2. Check that each is **stated once** and referenced elsewhere, that repeated values **match exactly**, and that each carries a source and date or is labelled an estimate (with method) or an assumption (tracked in the workbook).
3. Re-run the economic model in `research/` and confirm `business.md`, `stack.md → Run cost` and `plan.md → Milestones` agree with its current output.

## 5. Consistency across documents

| Check | Documents |
|---|---|
| The core idea's users are the market's segments, and the beachhead's users are product's primary users | vision · market · product |
| Positioning is the same claim in market and brand | market · brand |
| Pricing is justified by the competitor and value evidence | market · business |
| Business-driven capabilities (billing, entitlements, compliance) appear as product requirements | business · product |
| The quality bar is achievable with the stack and budget | product · stack · business |
| Run cost matches the unit economics' cost to serve | stack · business |
| Phases fit the resources and runway, and milestones reference the targets | plan · stack · business |
| Philosophy principles are honoured, not contradicted, by every later choice | vision · all |

## 6. Completeness

Each document's reference file has a "Done when" column. Walk every row. A missing price, target, non-goal, constraint or kill criterion is a defect, however polished the rest is. Then check size as a symptom. Most finished documents land between roughly 500 and 2,500 words. Well above that usually means specification has crept in (go back to §2); well below usually means facts are missing.

## Presenting the review

When asking the owner to approve, summarise in a few lines: what the document commits them to, the strongest objection raised and how it was resolved, any assumptions still open, and anything you would push back on. Then ask for approval. Record the outcome in the workbook.

For a whole-blueprint check, report per document:

```
Blueprint review: <project> (<date>)
<document>: <approved/needs work>. <issues fixed>; <issues needing the owner, each with a recommendation>
Cross-document: <conflicts found and resolved>
Assumptions still open: <n> (highest-risk first)
```
