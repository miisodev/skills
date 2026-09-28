# Privacy audit

Does the product handle personal data lawfully, minimally and transparently, and can people exercise their rights over it? This part covers privacy engineering and the obligations of the privacy regimes that apply to the product's users. It sits between data-audit (how data is stored) and legal-audit (published policies and terms).

- **Check prefix:** `PRV`
- **Applies to:** every surface that collects, stores or shares personal data (nearly all)
- **Not applicable when:** the product processes no personal data at all (rare: IP addresses and emails count)

## Evidence

- **Automated:** inventory of data fields from schema and forms; third-party SDKs and requests in the client (network inspection on first load, **before** any consent); analytics event payloads; log samples.
- **Manual:** compare the privacy policy with actual collection and sharing; walk consent, access, export, correction and deletion flows; determine which regimes apply from where users are (scoping below).

## Scoping: which regimes apply

Decide from where the **users** are, not where the company is. Record assumptions in the report. The thresholds below are a starting map as of 2026 and change over time: confirm current thresholds before rating a finding Critical. This is an engineering audit, not legal advice. Ambiguous legal questions become findings for counsel.

| Regime | Scope trigger | Distinctive obligations | Breach notice |
|---|---|---|---|
| GDPR (EU/EEA) | Offering to, or monitoring, people in the EU | Lawful basis per purpose; prior consent for non-essential cookies/trackers (ePrivacy); EU representative if there is no EU establishment; DPO in some cases; DPIA for high-risk processing; rights answered within one month | 72 h to the supervisory authority |
| UK GDPR + DPA 2018 + PECR | Same test for UK users | Mirrors GDPR; PECR for cookies and e-marketing; UK representative; ICO fee | 72 h to the ICO |
| CCPA/CPRA (California) | Revenue above the inflation-adjusted threshold (≈ US$26.6 M in 2025), or 100,000+ consumers/households' PI, or 50%+ revenue from selling/sharing PI | Notice at collection; "Do Not Sell or Share" where applicable; honour Global Privacy Control; limit sensitive PI; rights within 45 days | State breach law |
| Other US state laws (VA, CO, CT, TX, OR and more) | Mostly volume thresholds | Opt-outs of targeted ads, sale and profiling; opt-in for sensitive data in several states; universal opt-out signals | State breach laws |
| PIPEDA + Quebec Law 25 (Canada) | Commercial activity with Canadians | Meaningful consent; Quebec: privacy officer, impact assessments, privacy by default | As soon as feasible (real risk of significant harm) |
| LGPD (Brazil) | Data of people in Brazil | Legal basis; DPO (encarregado) | 3 business days to the ANPD |
| POPIA (South Africa) | Processing in South Africa | Registered Information Officer; PAIA manual; opt-in for electronic direct marketing to non-customers | As soon as reasonably possible |
| Privacy Act 1988 (Australia) | Most businesses above A$3 M turnover, plus some smaller ones | Australian Privacy Principles | Notifiable Data Breaches scheme (assess within 30 days) |
| DPDP Act (India) | Digital personal data in India | Notice and consent; grievance officer; Rules phasing in (check status) | To the Board and affected people |
| PDPA (Singapore), APPI (Japan) | People in those countries | Consent/purpose; DPO (SG); consent for third-party and cross-border transfers (JP) | SG: 3 days after assessment; JP: promptly |

Children: COPPA (US, under 13: verifiable parental consent), GDPR Art. 8 (parental consent below 13–16 by country), and the UK Age Appropriate Design Code (high-privacy defaults for services likely accessed by children).

## Checks

### Inventory and minimisation
| ID | Check | Verify | Severity |
|---|---|---|---|
| PRV-01 | A data map exists: what personal data, where stored, why, the legal basis, retention, and which processors receive it | Document or build one in evidence | High |
| PRV-02 | Collection is minimal: every field and SDK has a purpose the product uses | Compare fields to features | Medium |
| PRV-03 | Special-category and sensitive data (health, biometrics, precise location, finance, children) is identified and has extra protection and a basis | Inventory | High where present |

### Transparency and consent
| ID | Check | Verify | Severity |
|---|---|---|---|
| PRV-04 | The privacy policy matches reality: data collected, purposes, processors, transfers, retention, rights and contact (legal presence: LGL-01) | Compare with the data map and network traffic | High |
| PRV-05 | Non-essential cookies, trackers, pixels and session replay load **only after** consent where the regime requires it | Network inspection on first load, with no consent given | Critical in consent regimes |
| PRV-06 | Consent UI offers reject as easily as accept, stores the choice, and allows withdrawal later | Test | High |
| PRV-07 | Opt-out signals (Global Privacy Control) and "Do Not Sell or Share" are honoured where US state laws apply | Send a GPC header; inspect | High where applicable |
| PRV-08 | Marketing consent is opt-in where required and never pre-checked (sending rules: MSG-09) | Signup forms | High |

### Handling
| ID | Check | Verify | Severity |
|---|---|---|---|
| PRV-09 | Personal data is not sent to analytics, error tracking or AI providers beyond what the policy states (no emails or names in events or URLs) | Inspect payloads and URLs | High |
| PRV-10 | Logs do not contain personal data beyond what is needed, and log retention is limited | Log samples | Medium |
| PRV-11 | Processor agreements (DPAs) are in place with every processor, and sub-processors are listed where required | Document (or not verified) | Medium |
| PRV-12 | International transfers use a recognised mechanism (adequacy, SCCs, the EU–US Data Privacy Framework) | Processor locations | Medium |
| PRV-13 | Data residency commitments (to customers or in contracts) are met by actual hosting regions, including processors | Region config (see INF-19) | High where committed |

### Rights
| ID | Check | Verify | Severity |
|---|---|---|---|
| PRV-14 | Users can access and export their data in a machine-readable format | Run an export | High in rights regimes |
| PRV-15 | Users can correct their data | Test | Medium |
| PRV-16 | Deletion requests are fulfilled end to end, including processors and backups policy (technical path: DAT-19) | Test deletion | High |
| PRV-17 | A route exists to receive rights requests, verify identity, and respond within the legal deadline | Contact route; process | Medium |

### Governance
| ID | Check | Verify | Severity |
|---|---|---|---|
| PRV-18 | Regime-specific roles and registrations are in place (EU/UK representative, DPO, Information Officer, ICO fee, PAIA manual) where applicable | Document (or not verified) | Medium |
| PRV-19 | High-risk processing has an impact assessment (DPIA/PIA) where required | Document | Medium |
| PRV-20 | A breach-notification procedure names the deadlines for each applicable regime | Document | Medium |
| PRV-21 | Age-gating and parental consent exist where children may use the product | Signup flow | High; Critical if directed at children |

## Severity notes

Trackers firing before consent in a consent regime, or data sold or shared without the required opt-out, is Critical, because regulators act on exactly these and they are easy to detect from outside.
