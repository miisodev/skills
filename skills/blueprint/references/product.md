# product.md: what it must do, for whom, and how well

The requirements the builder works to. This is the document most tempted to over-specify. Hold the line: it states **outcomes and qualities**, and leaves interfaces, flows, data models and technical approach to the builder, who will usually design them better with the full blueprint in hand.

Two kinds of requirement live here, kept distinct:
- **User requirements:** what each kind of user needs to be able to do or experience, in their terms.
- **Product requirements:** what the product must provide to meet those needs *and* the business's needs (billing, administration, compliance, analytics, support), stated as capabilities.

## Establishes

| Section | Answers | Done when |
|---|---|---|
| **Users** | Each user type: who they are, their context (device, environment, skill, time pressure), the job they hire the product for, what hurts today, and what success feels like | Traceable to `market.md → Segments`. Buyer and user separated where they differ. Admins, operators and support staff included if they exist |
| **User requirements** | Per user type, the outcomes they need, including the conditions that make them hard | Each is an observable outcome with its hard conditions ("a clerk records a sale in under ten seconds, one-handed, with no signal"), marked **must** / **should** / **could** |
| **Product requirements** | The capabilities the product must provide, including business-driven ones (accounts, billing and entitlements, admin, compliance, analytics, notifications, data export/deletion) | Each traces to a user requirement or to `business.md`, carries a priority, and is stated as a capability, not a design |
| **Quality bar** | The non-functional requirements that define "good enough": performance, reliability and availability, security, privacy and data handling, accessibility, platforms and devices, localisation, offline behaviour, compliance obligations | Each is measurable or checkable ("works on a 4-year-old mid-range Android phone", "WCAG 2.2 AA", "data stays in the EU") |
| **Boundaries** | What the product will never do, and what is out of scope | Each non-goal has its reason. Features merely not built yet belong in `plan.md → Not yet` |
| **Success measures** | The few product metrics that show it is working (activation, engagement, retention, a north-star), and what each should reach | Each connects to a `business.md` target or a user outcome |

**Priority is explicit and scarce.** If everything is a must, the builder has nothing to trade. The musts should be the smallest set without which the product fails its beachhead users (`market.md → Beachhead`).

## From the owner

- Walk through a real day for each user type. Where does the product enter it?
- What must be true for a user to say "I can't go back"?
- What are they certain the product must never do (sell data, send notifications at night, require an account to try it)?
- Which requirements are non-negotiable, and which are hopes?
- What quality bars matter most to their users: speed, privacy, reliability, accessibility, offline use?
- What regulated data or obligations are involved (health, finance, children, payments)?

Watch for design disguised as a requirement ("a dashboard with three charts"). Ask what the user needs to know or decide, and record that.

## Research and compute

- Carry the user research from `market.md` (reviews, interviews, forums) into concrete requirements and hard conditions.
- Check the quality bar against reality: devices and connectivity in the target market, accessibility law (`market.md → Forces`), privacy regimes for the markets served, platform policies (app stores, marketplaces).
- Confirm business-driven capabilities with `business.md`: every paid tier implies entitlements, and every market implies tax, invoicing and data-rights obligations.

## Belongs / doesn't

| In | Out |
|---|---|
| Outcomes, conditions, capabilities, qualities, priorities | Screens, wireframes, flows, component specs |
| "Must work offline for a full shift" | The sync algorithm |
| "Users can export all their data in an open format" | The export endpoint or file schema |
| Non-goals with reasons | A backlog or feature list |
| The owner's fixed decisions, stated as requirements | UI copy, microcopy, error messages |

## Common weaknesses

- Requirements with no conditions, so they are trivially met and uninformative ("users can log in").
- Missing non-user actors: admins, support, finance, compliance.
- A quality bar of adjectives ("fast", "secure") instead of checks.
- Must-haves for every conceivable segment instead of the beachhead.
