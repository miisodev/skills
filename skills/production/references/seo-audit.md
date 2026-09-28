# SEO audit

Can people and machines (search engines, AI answer engines, social previews, app stores) find, understand and cite the product? The classic invisible-launch bug is a staging `noindex` shipped to production. This part catches it, and everything else that decides discoverability.

- **Check prefix:** `SEO`
- **Applies to:** marketing site, docs/help center, public web-app pages, store listings (SEO-17), API/SDK docs
- **Not applicable when:** the product is entirely private (internal tools, fully authenticated apps with no public pages). Still apply SEO-01 and SEO-15 so private areas stay unindexed

## Evidence

- **Automated:** `curl` the production `robots.txt`, `sitemap.xml` and `llms.txt`; fetch core pages and inspect `<head>` (titles, descriptions, canonicals, robots meta, Open Graph, `hreflang`, structured data); a crawler for status codes, redirects and duplicates; structured-data validation.
- **Manual:** share a production URL in a social or chat app and look at the preview; search for the brand name; inspect staging/preview domains for indexability.

## Checks

### Indexability
| ID | Check | Verify | Severity |
|---|---|---|---|
| SEO-01 | Production `robots.txt` and meta robots/`X-Robots-Tag` allow indexing of public pages, with no stray `noindex` | `curl`; view source | Critical on a public launch |
| SEO-02 | A valid sitemap on the production domain lists canonical public URLs and is referenced from `robots.txt` | Fetch and validate | Medium |
| SEO-03 | Public content is present in the server-rendered HTML (not only after client-side JavaScript) for core pages | Fetch without JS | High for content/marketing pages |
| SEO-04 | Canonical tags point to the single canonical host and URL form (https, apex or www, trailing-slash rule) | Inspect | Medium |
| SEO-05 | Moved URLs use 301 redirects; missing pages return a real 404 status (no soft 404s); no redirect chains | Crawler | Medium |
| SEO-06 | Search engine webmaster tools are verified for the domain and the sitemap is submitted | Tool access (or not verified) | Low |

### On-page
| ID | Check | Verify | Severity |
|---|---|---|---|
| SEO-07 | Every indexable page has a unique, descriptive title and meta description | Crawler | Medium |
| SEO-08 | One H1 per page and a logical heading structure | Crawler | Low |
| SEO-09 | Open Graph and social card tags produce a correct preview with an image for key pages | Share a link; validator | Medium |
| SEO-10 | Structured data (Organization, WebSite, SoftwareApplication/Product, FAQ, Breadcrumb as relevant) is valid | Validator | Low |
| SEO-11 | Key intent pages exist and are linked: home, pricing, features, use cases, comparison/alternatives, docs, and help | Site review | Medium |
| SEO-12 | Public pages pass Core Web Vitals on mobile (PRF-01 to PRF-03) | Field data | Medium |
| SEO-13 | `hreflang` is correct for multi-language or multi-region sites | Inspect | Medium where localized |

### AI and answer engines
| ID | Check | Verify | Severity |
|---|---|---|---|
| SEO-14 | AI crawler access is a deliberate policy (allowed or blocked per crawler in `robots.txt`), and an `llms.txt` summarising the product and key docs is published where useful | `robots.txt`; `/llms.txt` | Low |

### Hygiene
| ID | Check | Verify | Severity |
|---|---|---|---|
| SEO-15 | Staging, preview and internal environments are not indexable (auth, `noindex`, or blocked) | Search for the staging host; inspect headers | Medium |
| SEO-16 | Pages behind login or with user data are not indexable | Inspect headers | High if user data is exposed |
| SEO-17 | App-store listings (if any) have optimised titles, subtitles, keywords, screenshots, preview video and localized metadata | Store console or listing | Medium for mobile-first products |

## Severity notes

A production `noindex` or a `robots.txt` blocking everything on a product that relies on search is Critical. It is silent and costs weeks of traffic.
