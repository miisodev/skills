# stack.md: what it is built with, and what is available to build it

The building blocks, where the project runs, the people, agents, time and money available, and the hard limits. Record decisions the owner has genuinely made, with their reasons. For everything else, give the **criteria** a choice must meet and leave the choice to the builder. Architecture, data models and code structure are the builder's, and stay out of this document.

## Establishes

| Section | Answers | Done when |
|---|---|---|
| **Stack** | The components that are decided (language, frameworks, platforms, key services), each with why and what the project requires of it. For undecided areas, the criteria a choice must meet | Each decided item has a reason tied to requirements, resources or constraints (team skill, existing accounts, cost, compliance). Open areas have criteria, not a guess. Versions, prices and quotas are anchored with a canonical link, not transcribed |
| **Infrastructure** | Where it runs and what it depends on: hosting, data storage, identity, payments, email and messaging, analytics, AI providers, domains. Environments. Data residency | Each dependency has the requirement it serves and the alternative if it fails or prices change. Shared infrastructure with other projects is named |
| **Run cost** | What the infrastructure costs at launch and at target scale | Computed from anchored provider rates and `product.md`/`business.md` usage assumptions, and consistent with `business.md → Unit economics` |
| **Resources** | Who and what builds and runs it: people and roles, AI agents and what they do, time available, budget, accounts and subscriptions already held, reusable code, assets and relationships | Honest about capacity: part-time is stated as part-time. Budget matches `business.md → Fixed costs and runway` |
| **Constraints** | Hard limits the build must respect: budget ceilings, compliance and certifications, platform policies, licence terms, hardware, deadlines imposed from outside, handover or acquisition requirements | Each has its source and the consequence of breaking it. Preferences are not dressed up as constraints |
| **Secrets** | Where credentials live and the policy for handling them | Location and policy only, never a value |

## From the owner

- What do they (or their team) already know well? What are they unwilling to learn right now?
- Which accounts, subscriptions, credits, code or assets do they already have?
- How many hours a week, and for how long? Who else is involved, and who are the AI agents?
- What is the monthly infrastructure budget ceiling, at launch and at scale?
- Are there compliance, residency or platform requirements (app stores, enterprise buyers, regulated data)?
- Must anything be portable, for example for a future sale, a client handover or avoiding lock-in?
- Which technology choices are firm preferences, and which are they happy to delegate?

Encourage delegation where the owner has no real constraint. A blueprint that fixes every library ages badly and blocks the builder from better options.

## Research and compute

- **Fit checks:** confirm each decided component meets the quality bar in `product.md` (platform support, performance, compliance, regions) from current official docs.
- **Pricing and limits:** anchor each paid service (name, link, the tier relied on) and compute run cost at launch and target scale in the economic model (`research/economics.*`).
- **Risk:** vendor lock-in, pricing volatility and single points of failure for critical dependencies. Note the fallback.

## Belongs / doesn't

| In | Out |
|---|---|
| Decided components and why; criteria for open ones | Architecture diagrams, service boundaries, data models, folder structure |
| Anchored providers with the requirement placed on each | Transcribed price tables, version numbers, quotas |
| Resources and budgets | Credentials, keys, tokens |
| Real constraints with sources | Preferences presented as constraints |

## Common weaknesses

- A stack chosen for fashion with no link to requirements or skills.
- Run cost missing, or inconsistent with the unit economics.
- Resources overstated: a solo part-time owner planning like a funded team.
- Every library pinned, leaving the builder no room.
