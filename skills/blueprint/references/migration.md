# Adopting existing material

Many projects already have PRDs, specs, business plans, pitch decks, design docs or an earlier blueprint. They usually mix three things:
- **intent**, which belongs in the blueprint
- **a record of what was built**, which belongs with the build
- **history**, which belongs in the workbook's decision log or in version control

Adoption separates them, and then the extracted intent goes through the normal cycle. Legacy documents are evidence, not approval. The owner confirms every document as usual.

Tell the owner what you plan to move, keep and retire before you move, archive or delete anything.

## 1. Inventory

List every source document with its size and last-modified date, and **everything that loads it**: agent instruction files (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursor/rules`, `.github/copilot-instructions.md`), scripts, CI, prompts, docs sites and README links. Search the repository for each file's name. What loads a file matters as much as what it says, because anything still loading a retired spec will keep feeding it to agents.

## 2. Classify each passage

| Tag | Test | Destination |
|---|---|---|
| **Intent** | Only the owner, the market or the money could supply it, and it would still be true if the build were redone differently | The matching blueprint document, as input to Discuss |
| **Built** | Describes what exists: the design system as implemented, schema, routes, architecture, integrations | Stays with the build (code, README, architecture docs), but only if it is still true |
| **History** | What happened, what was decided and when, status, progress | The workbook's decision log if it explains a live decision; otherwise leave it to version control |
| **Stale** | Contradicted by the code, the market or later decisions | Delete. If it looks like intent the build ignored, ask the owner which is right |
| **Derivable** | A capable builder would produce it from the intent | Delete |

Split passages that mix tags. "Checkout is a three-step modal (built) because buyers abandon when forced to create an account first (intent)" yields one requirement in `product.md` ("buyers can purchase without creating an account"). The modal is visible in the code.

## 3. Verify "Built" against reality

Check every passage you keep as a record of the build against the code, database or live product. A spec describing a design system that is no longer the one in the code is worse than none, because it gets trusted.

## 4. Run the cycle

Create `blueprint/README.md` and `workbook.md` from the templates. Seed each document's Discuss stage with its extracted intent, list the gaps (sections the legacy material never covered: often economics, kill criteria, quality bar and non-goals), and take each document through Research, Draft, Review and Approve with the owner. Expect the result to be far shorter than the legacy set, and more complete where it counts.

## 5. Retire the old set

Move the legacy material **out of every loader's path**: an archive folder excluded from agent context, a tagged commit before removal, or deletion if the owner prefers (version control keeps it). Then repoint everything found in step 1 at `blueprint/README.md`, and search again for every legacy filename. No live reference should remain outside the archive. Two competing sources of intent are worse than either alone.

## 6. Report

```
Adoption: <project>
Sources: <n> files, <words> words
Intent extracted → <documents seeded>; gaps to establish: <list>
Built → kept with the build: <where>
Deleted as stale or derivable: <n> passages (examples)
Retired to: <archive path or commit>
Loaders repointed: <list>
```
