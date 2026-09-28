# Billing audit

Does money flow correctly? Customers can pay, entitlements stay in sync with billing state, failures and refunds are handled, taxes are right, and the books reconcile. Billing bugs cost revenue and trust at once, so most findings here are Critical or High. Webhook mechanics are in api-audit (API-10 to API-16) and apply throughout.

- **Check prefix:** `BIL`
- **Applies to:** any surface where money changes hands: web checkout, in-app purchases (with mobile-audit), subscriptions, usage billing, marketplaces
- **Not applicable when:** the product takes no payments

## Evidence

- **Automated:** payment-provider configuration in code (keys by mode, price/product IDs, webhook handlers); entitlement logic; reconciliation jobs; billing tests.
- **Manual:** walk checkout and every subscription transition in the provider's test mode; compare displayed and charged amounts.
- **Needs owner approval:** the single smallest real live-mode purchase and refund (BIL-06). In autonomous runs, record it as not verified unless evidence exists.

## Checks

### Provider readiness
| ID | Check | Verify | Severity |
|---|---|---|---|
| BIL-01 | Provider account onboarding/verification is complete and payouts are enabled to a connected account | Provider dashboard (or not verified) | Critical |
| BIL-02 | Production uses live keys and **live** product/price IDs (test-mode objects do not carry over) | Config vs. provider | Critical |
| BIL-03 | The live webhook endpoint is registered with its secret (API-10) | Provider dashboard | Critical |
| BIL-04 | The statement descriptor and customer-facing business name are recognisable (fewer chargebacks) | Provider settings | Low |
| BIL-05 | Card data never touches the product's servers (hosted checkout or provider fields), keeping PCI scope minimal | Inspect checkout | Critical |

### Checkout
| ID | Check | Verify | Severity |
|---|---|---|---|
| BIL-06 | One live purchase has been completed end to end with a real card and then refunded | Evidence or not verified | High |
| BIL-07 | Declines, 3-D Secure/SCA challenges and payment-method errors are recoverable with clear messages | Provider test cards | High |
| BIL-08 | Entitlement is granted from verified provider events or server-side verification, never from a client redirect to a success page | Code review; visit success URL directly | Critical |
| BIL-09 | The price shown before payment equals the amount charged, including currency, tax and discounts | Compare | High |

### Subscriptions and entitlements
| ID | Check | Verify | Severity |
|---|---|---|---|
| BIL-10 | Each transition updates access correctly: subscribe, trial→paid, upgrade, downgrade, cancel, expire, reactivate | Test-mode walk-through | High |
| BIL-11 | Plan limits are enforced server-side, and downgrades handle over-limit data gracefully (never silent deletion) | Test | High |
| BIL-12 | Cancellation is available in-app or self-serve without contacting support, and the effective date is stated | Walk it | High (legal in several markets) |
| BIL-13 | A scheduled reconciliation compares provider state with entitlements, and repairs or flags drift; support can resync a customer | Job and runbook | High |
| BIL-14 | Failed renewals trigger dunning: retries, an email with a working update-payment link, a stated grace period, then restriction that is visible in the UI, and restore on payment | Test-mode failed renewal | High |

### Refunds, disputes and fraud
| ID | Check | Verify | Severity |
|---|---|---|---|
| BIL-15 | Fraud tools are on, card-testing is rate-limited, and dispute notifications reach a person who knows the evidence process | Settings; process | High |
| BIL-16 | Refunds (full and partial) adjust or revoke entitlements, and behaviour matches the published policy | Test-mode refund | High |

### Tax, currency and invoices
| ID | Check | Verify | Severity |
|---|---|---|---|
| BIL-17 | A tax strategy exists for every market sold into (provider tax automation, a merchant of record, or registrations tracked with an advisor); see the table below | Decision and config | High |
| BIL-18 | Currency and tax display are consistent: tax-inclusive or exclusive per market norms, and charged currency equals displayed currency | Checkout from two regions | High |
| BIL-19 | Invoices/receipts carry required fields (legal entity, address, tax ID, line items, tax breakdown) and customers can retrieve them | Sample invoice | Medium |
| BIL-20 | Revenue reporting has one source of truth that reconciles with the provider; refunds, disputes, test and internal transactions are handled correctly | Compare a sample period | Medium |

### Trials, renewals and platform billing
| ID | Check | Verify | Severity |
|---|---|---|---|
| BIL-21 | Trial terms are clear before signup (when billing starts, the amount, how to cancel), with reminders before conversion where law or norms expect them | Walk trial signup | High |
| BIL-22 | Auto-renewal disclosures and consent meet consumer rules in the markets served (clear terms, affirmative consent, renewal reminders for longer terms) | Checkout copy | High |
| BIL-23 | Digital goods in mobile apps use the platform's in-app purchase where store rules require it, with server-side receipt validation and restore purchases (MOB-11) | Code; store rules | Critical if the store would reject it |

## Sales tax / VAT on digital products

Selling software, subscriptions or digital content to consumers usually creates an obligation **where the buyer is**. A merchant of record takes this over; a plain card processor does not. Verify current thresholds.

| Market | Rule of thumb |
|---|---|
| EU | B2C digital services are taxed at the customer's country rate via the One-Stop Shop (non-Union OSS for non-EU sellers; no threshold for non-EU sellers). B2B uses reverse charge with a validated VAT ID |
| UK | Non-UK sellers of B2C digital services register for UK VAT from the first sale |
| US | Per state: economic nexus is commonly around US$100 k of sales into the state. Whether SaaS is taxable varies by state |
| Canada | GST/HST for non-resident digital sellers above C$30 k, plus provincial rules |
| Australia | GST on imported digital services above A$75 k |
| South Africa | VAT on electronic services by foreign suppliers above R1 M in 12 months |
| India, Japan, Norway, Switzerland and others | Registration for foreign digital-service suppliers, often from the first sale or a low threshold |

## Severity notes

Anything that lets people use paid features without paying, charges without granting access, or double-charges is Critical and `core_flow: true`. Selling into several tax jurisdictions with no strategy is High.
