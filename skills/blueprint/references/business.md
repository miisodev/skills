# business.md: how it makes money, and whether it does

The model, the economics that test it, and the targets that define success. This is where enthusiasm meets arithmetic. The job is to make sure the owner decides with the numbers in view: is this worth doing at the price, cost and scale the market supports?

For projects that do not sell anything (internal tools, open source, personal projects), the same questions apply in a different form. The model becomes how the project is funded or sustained, the economics become what it costs against the value it creates, and the targets become adoption or outcomes.

## Establishes

| Section | Answers | Done when |
|---|---|---|
| **Model** | Who pays, for what, how often, and through which revenue streams | Buyer, unit of value and billing shape are explicit. Free tiers and trials are defined by what they are for (acquisition, conversion) |
| **Pricing** | The prices the project charges, per tier, and why | Stated in full with currency and tax treatment. Justified against the alternatives (`market.md → Competitors`) and the value delivered. Discounting policy stated |
| **Unit economics** | What one customer is worth and costs: revenue per customer, gross margin (including infrastructure, AI and payment costs per customer), acquisition cost by channel, retention/churn, payback period, lifetime value | Computed in a saved, runnable model (`research/economics.*`). Every input carries a source or is labelled an assumption. The formula and result appear in the document |
| **Fixed costs and runway** | What it costs to exist each month, the money available, how long it lasts | Ties to `stack.md → Resources`. Break-even stated in customers and months |
| **Sensitivity** | Which assumptions the outcome depends on most | The two or three inputs that swing the result are named, with the result at pessimistic and optimistic values |
| **Targets** | What success is worth in numbers: revenue, customers, margin, and exit where relevant | Each target has a horizon and the decision it drives. Targets are consistent with the unit economics and runway |
| **Structure** | Entity, jurisdiction, ownership, and for acquisition-built products: the buyer, why they buy, and what they receive | Only what affects decisions (tax, payments, contracts, handover) |

## From the owner

- What do they want this to become: a lifestyle business, a venture-scale company, an acquisition, a side income, a public good? This changes every target.
- What money and time can they commit, and for how long before they need it to pay?
- What would they charge today, and what makes them nervous about charging more?
- Are there revenue sources they refuse (ads, selling data, enterprise sales)?
- What number, reached by when, would make this a success? What would make them stop?

## Research and compute

- **Pricing evidence:** competitors' current prices and packaging (dated), what the segment pays for alternatives, and willingness-to-pay signals.
- **Cost per customer:** infrastructure, third-party and AI-model costs per active user at expected usage, and payment-processing fees. Anchor the provider rates and compute the result.
- **Acquisition cost:** benchmarks per channel from credible sources, labelled as benchmarks, then replaced by the project's own data when it exists.
- **Churn and conversion:** benchmarks for the category, labelled as such.
- **Build the model in code or a spreadsheet** saved to `research/`, so the owner can change an input and see the effect. Do arithmetic in the model, never in your head. See `references/research.md → Economic models`.

Walk the owner through the model's result before drafting. If the economics do not work at the proposed price, that is the most important finding in the blueprint. Explore the options (a higher price, a different segment, lower cost to serve, a different model) with them before moving on.

## Belongs / doesn't

| In | Out |
|---|---|
| Prices the project charges, in full | Payment-provider fee tables (anchor in `stack.md`; use them as model inputs) |
| The economic model's inputs, formulas and results | Figures nobody can recompute |
| Targets with horizons and consequences | Vanity metrics with no decision attached |
| The owner's financial constraints and ambitions | Personal financial details beyond what decisions need |

## Common weaknesses

- Pricing set by gut, or by undercutting competitors without a cost-to-serve check.
- AI or infrastructure cost per user missing, which is fatal for usage-heavy products.
- A lifetime value that assumes near-zero churn.
- Targets that the unit economics and channels cannot reach within the runway.
