# Legal audit

Is the product legally presentable and defensible in the markets it serves? Required policies and terms, consumer-protection rules, licences and intellectual property, sector regulation, and platform rules. Privacy law is in privacy-audit, tax in billing-audit, and accessibility law in accessibility-audit. This part confirms they have been scoped and covers everything else.

This is an engineering audit, not legal advice. Anything ambiguous becomes a finding with the recommendation "confirm with counsel", not a ruling. Regulations and thresholds change, so date the evidence.

- **Check prefix:** `LGL`
- **Applies to:** every product with users; distributed binaries and packages for licence checks (LGL-09, LGL-10)
- **Not applicable when:** never

## Evidence

- **Automated:** licence scan of dependencies for each ecosystem (e.g., `license-checker`, `pip-licenses`, `cargo-deny`, or SBOM tooling); search for policy pages and their links.
- **Manual:** read the privacy policy, terms and refund policy against actual behaviour; walk signup and checkout for legal disclosures; identify sector regulation from what the product does.

## Checks

### Policies and terms
| ID | Check | Verify | Severity |
|---|---|---|---|
| LGL-01 | A privacy policy, terms of service and cookie notice (where cookies/trackers are used) are published and linked from the footer, signup, checkout, app settings and store listings | Visit each | Critical if no privacy policy while collecting personal data |
| LGL-02 | The terms cover what the service is, acceptable use, user content and IP, liability limits, suspension and termination, governing law, and billing/renewal/refunds | Read | High |
| LGL-03 | Acceptance of terms is recorded at signup (clear action, version and timestamp stored) | Signup flow; schema | Medium |
| LGL-04 | Refund and cancellation policies are published and match actual behaviour (BIL-12, BIL-16) | Compare | High |
| LGL-05 | Company identity is published where required: legal name, registration number, address, contact (EU/UK e-commerce rules; e.g., Germany's Impressum) | Footer/about page | Medium |

### Consumer protection
| ID | Check | Verify | Severity |
|---|---|---|---|
| LGL-06 | Pricing is transparent (total price, recurring terms, taxes and fees shown before payment), and the product uses no dark patterns (hidden costs, confirm-shaming, obstructed cancellation) | Walk checkout and cancellation | High |
| LGL-07 | EU/UK consumers get their withdrawal-right information for digital content and services, and the waiver is captured properly where immediate access is given | Checkout | High for EU/UK B2C |
| LGL-08 | Reviews, testimonials, ratings and endorsements are genuine and disclosed where incentivised | Inspect | High |

### Licences and IP
| ID | Check | Verify | Severity |
|---|---|---|---|
| LGL-09 | Open-source licences are compatible with how the product is distributed. Copyleft (GPL/AGPL) use is analysed, especially AGPL in network services and GPL in distributed binaries | Licence scan | High if copyleft conflicts |
| LGL-10 | Attribution and licence notices are included where licences require them (bundled with apps and binaries, or in an open-source notices page) | Inspect | Medium |
| LGL-11 | Fonts, images, icons, audio and video are licensed for commercial use in this medium, and the name and marks have been checked for conflicts (BRD-06) | Asset licences | Medium |
| LGL-12 | Ownership of code and content created by contractors and agencies is assigned to the owner | Contracts (or not verified) | Medium; High before a sale or investment |

### Regulation and platforms
| ID | Check | Verify | Severity |
|---|---|---|---|
| LGL-13 | Applicable regimes are scoped and recorded: privacy (privacy-audit), accessibility law (accessibility-audit), tax (billing-audit), email/SMS law (below), AI regulation (below) | Scoping notes in the report | High |
| LGL-14 | Sector regulation is identified where the product touches it: health data (e.g., HIPAA), payments and financial services, education (FERPA/COPPA), gambling, age-restricted goods, telecoms, and security certifications buyers expect (SOC 2, ISO 27001) | Product review | High where applicable |
| LGL-15 | Platform and store policies are met for every distribution channel (MOB-10, EXT-06, marketplace listing rules) | Cross-check | High |
| LGL-16 | Business-customer paperwork is available where selling to businesses: DPA, MSA or terms for business, SLA, security overview, sub-processor list | Documents | Medium for B2B |
| LGL-17 | Export controls and sanctions are considered if the product includes strong cryptography, dual-use capabilities, or serves restricted regions | Review | Medium where relevant |

## Messaging law (summary; checks in MSG-09 and MSG-13)

| Rule | Scope | Requirement |
|---|---|---|
| CAN-SPAM (US) | Commercial email to US recipients | Accurate headers, postal address, opt-out honoured within 10 business days |
| CASL (Canada) | Commercial electronic messages to Canadians | Consent **before** sending, identification, unsubscribe |
| GDPR/PECR (EU/UK) | Marketing to individuals | Opt-in consent (the UK "soft opt-in" covers existing customers for similar products) |
| TCPA / 10DLC (US) and national equivalents | SMS marketing | Prior express written consent, registered sender, STOP handling |

## AI regulation (summary; checks in AIF-10 and AIF-19)

| Regime | What to check |
|---|---|
| EU AI Act | Transparency duties (disclose AI interaction; label synthetic content) and high-risk classification for uses affecting access to jobs, credit, education or essential services; obligations phase in 2025–2027, so check what applies on the audit date |
| US state laws and sector regulators (e.g., Colorado AI Act, NYC Local Law 144 for hiring) | Notices and anti-discrimination duties for consequential decisions |
| Privacy regimes | Automated decision-making and profiling rights (GDPR Art. 22 and equivalents) |

## Severity notes

Collecting personal data with no privacy policy, false claims that create consumer-protection exposure, and copyleft conflicts in distributed binaries are the usual Critical and High findings. Where legal status cannot be established from the repository and public pages, mark the check `not_verified` and route it to counsel in the recommendation.
