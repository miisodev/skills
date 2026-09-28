---
name: blueprint
description: "Establish a project's blueprint together with its owner: seven documents (vision, market, business, product, brand, stack, plan) holding the core idea, vision, philosophy, market research and strategy, business model, economics, targets, user and product requirements, brand, stack, infrastructure, resources and grand plan. It is collaborative and iterative, not one-shot. Each document is discussed, researched and computed, drafted, critiqued and approved by the owner, and progress is kept in a workbook so any later session can resume. The blueprint sets intent and leaves design, architecture, schemas, APIs and copy to the builder. Use it when starting, validating or planning a product, business or project idea; when resuming or revising a blueprint; when a project's market, pricing, requirements, brand, stack or plan changes; when replacing a bloated spec or PRD library; or when the user mentions a blueprint, business plan, PRD, product brief, brand brief, go-to-market, unit economics or roadmap."
license: MIT
metadata:
  author: miisodev
  version: "1.0.0"
---

# Blueprint

A blueprint is the foundation a project is built on: the context that only the owner, the market and the money can supply, established carefully enough that anyone who builds, markets or runs the project can reason from it. It answers *why this exists, for whom, what they need, how it wins, whether it makes money, what it is made of, what it may spend, how it should feel, and where it is going*.

It is established **with** the owner, not written **for** them. The value is partly in the documents and partly in the understanding the two of you build while producing them. The owner sharpens an idea they may never have fully articulated. You learn the project well enough to make good calls later, and so does every model and person who reads it afterward.

## What a blueprint holds, and what it leaves to the builder

| File | Establishes | Leaves to the builder |
|---|---|---|
| `vision.md` | Core idea · vision · philosophy · why us | Feature ideas, solutions |
| `market.md` | Market research (segments, size, alternatives, competitors, evidence of demand) · market strategy (wedge, positioning, channels, moat) | Campaign plans, content calendars |
| `business.md` | Business model and pricing · economics · targets | Payment-provider implementation |
| `product.md` | Users and their requirements · product requirements · quality bar · boundaries · success measures | Screens, flows, components, schemas, routes, APIs, copy |
| `brand.md` | Name · positioning · personality and voice · visual direction · assets | Design tokens, type scales, component styling, layouts |
| `stack.md` | Stack decisions and the criteria for open ones · infrastructure · resources · constraints · secrets policy | Architecture, data models, service boundaries, code structure |
| `plan.md` | Mission · phases and exit criteria · milestones · bets · risks · kill criteria · deferrals | Task lists, sprints, tickets, status |

**The boundary follows from what models are now good at.** Frontier models design interfaces, architect systems, model data, write copy and plan implementation well, often better than a specification written months earlier by someone who could not see the build. A blueprint that pre-decides those things caps the work at its author's level and goes stale the moment the build improves on it. What no model can work out is the owner's intent, the market's reality and the money's limits. The blueprint holds exactly that, thoroughly, and nothing else.

An owner's decision that *looks* like design stays, stated as the requirement it protects: "a member's balance is never visible to anyone else in the room" belongs in `product.md`, but a spec of the balance widget does not.

## Files

```
blueprint/
  README.md       index: what the blueprint is, reading order, each document's status
  vision.md
  market.md
  business.md
  product.md
  brand.md
  stack.md
  plan.md
  workbook.md     the working record: stages, open questions, decisions, assumptions, sessions
  research/       evidence: one file per topic, sources dated; models (e.g. economics) kept runnable
```

Use `blueprint/` at the repository root unless the project already has a convention. Create `README.md` and `workbook.md` from `assets/index-template.md` and `assets/workbook-template.md` when the work begins.

The documents hold conclusions. The workbook holds the process. `research/` holds the evidence. Keeping them apart is what lets the documents stay short and decided while nothing that was learned is lost.

## How a blueprint is established

### The working relationship

Act as the owner's most capable co-founder would: someone who knows markets, pricing, product and engineering, researches rather than guesses, does the arithmetic, and says plainly when something does not hold up. Bring evidence and a recommendation to every decision so the owner spends their attention on judgment, not on legwork. The owner has the final word on intent, taste, commitments and money. You are responsible for making sure each of those decisions is informed.

Honesty matters more here than anywhere else in a project. A blueprint built on a flattering reading of the market or an unexamined price wastes everything built on top of it. If the evidence says the market is small, the price is too low, the plan is too long for the runway, or the idea overlaps an entrenched competitor, say so early, show the evidence, and help the owner decide what to do about it.

### The cycle, per document

Each document moves through five stages. Record the current stage in the workbook and the index. Other skills or tools may help at any stage. The stages describe what must be true before moving on, not a script.

1. **Discuss.** Establish what the owner knows, believes, wants and will not accept for this document's subject. Open with what you already understand (from earlier documents, the repository and anything they have shared) so they correct rather than repeat. Ask a few focused questions at a time, each with your recommended answer where you can form one. Follow the interesting threads. The reference file for each document lists what must be established, with sample questions that are starting points, not a questionnaire.
2. **Research and compute.** Close the gaps the discussion exposed: market facts, competitors, prices, sizes, provider limits, and the arithmetic of economics and costs. `references/research.md` sets the evidence standard. Save findings to `research/` and give the owner a summary of what changed their picture.
3. **Draft.** Write the document from the discussion and evidence, to the standards below. Anything still undecided goes into the workbook as an open question with a recommended answer. It never goes into the document.
4. **Review.** Critique the draft before the owner sees it as final: challenge it as a skeptical investor, an experienced operator and a target user would; check it against every approved document; run the sweeps in `references/review.md`. Then walk the owner through what the document commits them to and what you would push back on.
5. **Approve.** The owner confirms, or sends it back to an earlier stage. Record the approval and the key decisions, with their rationale, in the workbook.

### Order and reopening

Work in index order: vision → market → business → product → brand → stack → plan. Each document depends on the ones before it: pricing needs the market, requirements need the users and the model, the stack needs the requirements and the budget, and the plan needs everything. Starting elsewhere is fine when the owner arrives with a document half-formed. Capture what they have, then return to order.

Later work often exposes a problem in an approved document: market research undermines the vision's "why now", or the economics break the price. **Reopen it.** Record why in the workbook, move it back to Discuss, and resolve the conflict before continuing. A blueprint whose documents disagree is worse than an unfinished one.

### Pacing

This is deliberately not a one-shot. A thorough blueprint usually takes several sessions, and the owner may need time to think, talk to customers or check numbers between them. Keep each turn digestible: a handful of questions, one research summary, or one draft section at a time, unless the owner asks for more. Close every session by updating the workbook: stages, new decisions, open questions, and what happens next.

### Starting and resuming

At the start of any session, read `blueprint/README.md` and `blueprint/workbook.md` if they exist, plus any documents in progress. Tell the owner where things stand and what you recommend doing next, and ask. With no blueprint yet, begin with the owner's idea in their own words, gather what already exists (repository, README, docs, prior specs, live site or store listing), create the index and workbook, and start Discuss on `vision.md`.

When there is nobody to collaborate with (an autonomous run, an owner who asks for a quick draft), you may draft ahead. Record every choice made on the owner's behalf in the workbook as an open question with your recommendation, leave each document at Review rather than Approved, and say so.

## Standards for the documents

1. **Context, not instructions.** For every sentence ask: *could a capable builder produce this well from the rest of the blueprint?* If yes, it does not belong. What survives is what only the owner or the world can supply: taste, commitments, non-negotiables, market facts, money, and the reasons behind them.
2. **Decided and current.** Approved documents state the intent in the present tense. They contain no TBDs, no open questions, no status ("not yet built", "currently"), and no decision history ("we chose X after…"). Open items live in the workbook, progress lives wherever the project tracks it, and history lives in the workbook's decision log. A constraint carries its reason and the cost of breaking it.
3. **Evidence-backed.** Market facts, prices and rates carry their source and date. Estimates show their method. Assumptions are labelled as such and appear in the workbook's assumptions table with how they will be validated. A number that cannot be traced is a guess wearing a costume.
4. **One home per fact.** Each fact is stated in exactly one document and referenced from others (`see business.md → Targets`). This matters most for numbers: a target restated elsewhere drifts.
5. **Own what you control; anchor what you do not.** The product's own prices, targets and requirements are stated in full. A vendor's price, a framework's version or a plan's quota is anchored with its name, a canonical link and the requirement the project places on it. Economics inputs are the exception: they sit in the computation with source and date.
6. **Specific.** Every sentence should be false for some other project. "Delight users with a seamless experience" says nothing. "A clerk records a sale one-handed, offline, in under ten seconds" says a great deal.
7. **Complete, then lean.** Completeness comes first: a missing price, target, non-goal or constraint is a defect. Once complete, cut whatever a builder could derive. Length is a symptom worth checking (`references/review.md → Completeness`): a very long document has usually started specifying the build, and a very short one is usually missing facts.

## After approval

A blueprint changes when **intent** changes: a new market, a new price, a requirement that proved wrong, a new constraint. Progress alone is never a reason to touch it. Take a revision through the same cycle at the scale it needs. A price change gets a short discussion, research, a draft, a review and approval, and then a check of every document that references the changed facts.

Point the project's agent instruction files (e.g., `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursor/rules`, `.github/copilot-instructions.md`, whichever exist) at `blueprint/README.md` with one line saying it is the source of intent and should be read before making product, design or architecture decisions. Don't copy content into them.

## Adopting existing material

When a project already has PRDs, specs, business plans or design docs, `references/migration.md` covers extracting their intent into the blueprint, leaving the record of what was built with the build, and retiring the rest. The extracted material still goes through Discuss and Review. Legacy documents are evidence, not approval.

## When to push back

- **Design or implementation proposed for the blueprint.** Capture the requirement behind it. The design is the builder's to make.
- **A decision without evidence** where evidence is obtainable: a price with no comparison, a market size with no method, a target with no path from the economics.
- **Enthusiasm outrunning the numbers.** Show the arithmetic and let the owner decide with it in view.
- **Rushing an approval.** A document the owner has not really read is not approved. Summarise what it commits them to and ask again.

## References

| File | Read when |
|---|---|
| `references/vision.md` … `references/plan.md` | Working on that document: what it must establish, what to learn from the owner, what to research, and what "done" looks like |
| `references/research.md` | Any Research-and-compute stage: evidence standards, market sizing, competitor analysis, economic models |
| `references/review.md` | Every Review stage, and whenever asked to check a blueprint |
| `references/migration.md` | Adopting an existing spec library, PRD or business plan |
| `assets/index-template.md`, `assets/workbook-template.md` | Creating `blueprint/README.md` and `blueprint/workbook.md` |
