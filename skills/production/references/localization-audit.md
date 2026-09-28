# Localization audit

Does the product work correctly for every language, region, currency and writing system it serves or accepts? Even single-language products take international names, addresses, phone numbers, time zones and payments. Localization failures corrupt data and exclude customers silently.

- **Check prefix:** `LOC`
- **Applies to:** every user-facing surface; APIs for data formats (LOC-08 to LOC-12)
- **Not applicable when:** never entirely. Single-language products still apply LOC-08 to LOC-14. LOC-01 to LOC-07 apply only when more than one language or locale is offered or marketed

## Evidence

- **Automated:** search for hard-coded user-facing strings outside the translation system; missing-key reports from the i18n library; pseudo-localization build if available.
- **Manual:** switch to each supported locale and walk the core journey; enter names, addresses and numbers from several countries; use an RTL locale if supported; change the device time zone.

## Checks

### Languages
| ID | Check | Verify | Severity |
|---|---|---|---|
| LOC-01 | Every supported language is complete on core flows: no untranslated strings, fallback keys or mixed languages | Walk each locale | High |
| LOC-02 | Translations are accurate and reviewed by a fluent speaker for money, legal and safety copy | Evidence of review | Medium; High for legal/pricing |
| LOC-03 | Layouts tolerate text expansion (German, Finnish) and short or wide scripts (CJK) without clipping | Pseudo-localize or switch | Medium |
| LOC-04 | Right-to-left languages (if supported) mirror layouts, icons and input correctly | RTL locale | High if RTL supported |
| LOC-05 | Plurals, gender and grammatical forms use the i18n library's rules, not string concatenation | Code review; counts of 0/1/2/5/21 | Medium |
| LOC-06 | Locale is detected sensibly, can be changed by the user, and the choice persists | Change and return | Medium |
| LOC-07 | Emails, notifications, PDFs and store listings are localized to match the product | Trigger in each locale | Medium |

### Formats and data
| ID | Check | Verify | Severity |
|---|---|---|---|
| LOC-08 | Dates, times, numbers and currencies are formatted per locale, never hand-built | Inspect in two locales | Medium |
| LOC-09 | Time zones: stored in UTC, displayed in the user's zone, and scheduling/recurrence is correct across DST | Change device zone; DST boundary case | High |
| LOC-10 | Names, addresses and phone numbers accept international formats (single names, non-Latin scripts, no postcode, E.164 phones) | Enter samples from several countries | High |
| LOC-11 | Text encoding is UTF-8 end to end: emoji and non-Latin scripts survive storage, search, export and email | Round-trip samples | High |
| LOC-12 | Sorting and search behave sensibly for accented and non-Latin text | Search and sort samples | Low |

### Regional commerce
| ID | Check | Verify | Severity |
|---|---|---|---|
| LOC-13 | Prices display in the currency charged, with tax-inclusive or exclusive display per market norms (see BIL-18) | Checkout from two regions | High |
| LOC-14 | Region-specific features, payment methods and legal content appear only where they apply | VPN or locale switch | Medium |

## Severity notes

Data corruption (LOC-10, LOC-11) and wrong scheduling across time zones (LOC-09) are High, and Critical when they affect money, appointments or legal deadlines. An incomplete translation of a market the product actively sells into is High.
