# Research and compute

What makes blueprint evidence trustworthy, and methods for the research the documents need most. The aim is decisions the owner can rely on, so rigour matters more than volume. Three well-sourced facts that change a decision beat thirty that decorate a page.

## Evidence standard

- **Primary over secondary.** A competitor's own pricing page beats an article about it. A government statistic beats a blog quoting it. Customer reviews beat a vendor's claims about customers.
- **Date everything.** Prices, sizes and rankings go stale. Record the date seen next to every sourced fact.
- **Label what kind of claim it is:**
  - **Fact:** sourced and checkable.
  - **Estimate:** derived from facts by a stated method.
  - **Assumption:** a belief not yet evidenced. It goes into the workbook's assumptions table with how and when it will be validated.
- **Triangulate numbers that matter.** Two independent routes to the same order of magnitude is the bar for anything a decision rests on.
- **Prefer behaviour to opinion.** What people paid for, signed up to, searched for or complained about outweighs what they say they would do.
- **Report what cuts against the idea too.** Evidence that the market is smaller, the competitor stronger or the price lower than hoped is the most valuable research you can bring.

When you have no web or data access, say so. Ask the owner for sources or access, or record the gap as an assumption to validate. Never present recall as current fact. Prices, competitors and regulations change after any model's training.

## Where research lives

One file per topic in `blueprint/research/`, named for the topic (`competitors.md`, `market-size.md`, `pricing.md`, `interviews.md`, `name-check.md`, `economics.py` or `economics.xlsx`). Each note opens with the question it answers and the date. It then gives findings with sources, and ends with the conclusion carried into the blueprint. The documents cite the file: `(research/market-size.md)`. Add each new file to the workbook's research log.

## Market sizing

1. **Bottom-up first.** Count the reachable customers in the beachhead from sourced data (registries, industry bodies, platform statistics, census and occupational data, directory counts). Multiply by a realistic annual price (`business.md`). Show each step.
2. **Top-down as a check.** Take a published category size and narrow it by segment and geography. If the two routes disagree by more than an order of magnitude, investigate before using either.
3. **Separate the layers:** the total market; the serviceable market (the segment, geography and model the project can serve); and a realistic obtainable share over the plan's horizon, justified by channel capacity rather than picked as a percentage.

## Competitor analysis

For each competitor that matters, from their own current materials: who they target, how they position, what they charge and how they package it (dated), and how they acquire customers (visible channels, marketing claims). Then take their **weaknesses in their customers' words** from app-store, review-site and community complaints, grouped by theme with rough counts. Finish with what they would do if this project succeeded. Keep only what informs a decision.

## Demand and customer evidence

- **Desk signals:** search volume trends, community size and activity, job postings mentioning the problem, marketplace listings, the traction of adjacent products.
- **Owner-run conversations:** where evidence is thin, recommend the owner speak to 5–15 potential customers before strategy or pricing is approved. Offer a short guide built on past behaviour ("walk me through the last time…", "what did you try?", "what did it cost you?") rather than hypotheticals ("would you use…?"). Summarise the transcripts or notes the owner provides into `research/interviews.md` with patterns and quotes.
- **Cheap tests:** a landing page with a price, a waitlist, a pre-sale, or a concierge version. Suggest them in `plan.md` when a critical assumption can be tested for little cost.

## Economic models

Do the arithmetic in code or a spreadsheet, never in prose. A model saved in `research/` can be re-run when an input changes. Prose arithmetic cannot, and is often wrong.

- **Inputs** in one clearly labelled block, each with its source or an "assumption" label: price per tier, tier mix, conversion rates, churn, acquisition cost per channel, cost to serve per customer (infrastructure, AI usage, third-party services, payment fees, support), fixed monthly costs, available capital.
- **Outputs:** revenue per customer, gross margin, contribution margin, payback period, lifetime value and LTV:CAC, monthly burn, runway, break-even (customers and month), and revenue at each plan horizon.
- **Sensitivity:** vary the uncertain inputs (conversion, churn, acquisition cost, usage cost) across pessimistic, expected and optimistic values, and report which ones move the outcome most.
- **Scenarios** where the owner is choosing between options (two prices, two segments, two stacks): run each and compare.

Put the headline inputs, formulas and results in `business.md`. The runnable model stays in `research/`.

## Using other tools and skills

Use whatever the environment offers: web search and fetch, data tools, spreadsheets, code execution, and specialised skills for market research, competitive analysis, pricing or financial modelling. The standards above apply to their output as well.
