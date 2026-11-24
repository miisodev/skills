# Compliance and threat modeling — as requirements, not a document

There is no eighth blueprint document. Compliance and threat modeling are requirements, and requirements live in `product.md` and `stack.md` — the same boundary that keeps a member's balance invisible in `product.md` rather than in a security spec. This reference is the checklist for establishing them with the owner, before building begins.

## Establish with the owner

**Data (into `product.md` as requirements):**

- The personal data the product collects, for each field: purpose, legal basis, where it is stored, how long it is kept, who can see it.
- Data residency and the markets that drive it (`product.markets`): GDPR, CCPA and their local analogues name the obligations; record them as engineering requirements with the regulator cited, not as legal conclusions.
- The deletion, export and correction flows users are promised.

**Access (into `product.md`):**

- The authentication flows: how users sign in, what each role can reach, where the boundaries are.
- The authorization model in one sentence per boundary: "a member's balance is never visible to anyone else in the room."

**Threats (into `stack.md` as constraints):**

- The first threat vectors for this product's shape: injection, broken access control, secret leakage, supply-chain compromise, and the one or two that are specific to what it does.
- What must never leak: the secrets policy in `stack.md` names every credential class and where it lives.
- The recovery position: what is backed up, how often, and what restore looks like.

## The boundary, stated

This is engineering intent, not counsel. The blueprint records what the owner requires and what the product must never do; the `production` audit checks the shipped product against those requirements (PRV, SEC, DAT, LGL); and regulatory confirmation stays with the regulator or counsel, as the production skill's disclaimer says.
