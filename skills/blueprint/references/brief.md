# The brief — one-page intent

The brief is the blueprint's lightweight artifact: one page of decided intent for work where the seven-document cycle is ceremony. Internal tools, open-source libraries, migrations, spikes, automations — work that deserves real intent but not a market study.

## What a brief holds, in this order

| Section | Establishes | The question it answers |
|---|---|---|
| Problem | What is wrong or missing, observed | Why does this exist? |
| Users or consumers | Who uses it and what they do with it | Who is it for? |
| Constraints | Stack, budget, time, policy, environment | What is fixed? |
| Non-goals | What it deliberately does not do | What will we refuse to build? |
| Acceptance criteria | Measurable, checkable outcomes | How do we know it worked? |
| Owner | One name | Who decides? |
| Rollout or reversal | How it ships and how it is undone | What happens when it lands — and if it fails? |

## The rules

- **Approved, then built.** The owner reads and approves the brief before implementation. It reopens like any blueprint document when intent changes.
- **No invented economics.** Internal-tool economics are time saved and maintenance cost; there is no pricing section to fake. This is the same exemption `business.md` records for the skills themselves.
- **It feeds the audit.** The production audit accepts an approved brief as the requirements standard for its scope; the acceptance criteria become the functional standard. A brief that says "v2 reads v1 project files without data loss" is a checkable requirement.
- **It can grow up.** When a brief-scope project becomes a product, the brief is the seed of `vision.md` and `product.md` — migrate, don't restart.
- **A typo fix triggers neither.** Work too small for a brief needs no skill run at all; that is a deliberate boundary, not a gap.
