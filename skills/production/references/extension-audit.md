# Extension audit

What changes when the product ships as a browser extension, or as a plugin for another platform (IDE, design tool, office suite, chat workspace)? Store review, permission scrutiny, hostile host pages, and a host platform that can change underneath the product. Apply this part **in addition to** the general parts for the extension surface.

- **Check prefix:** `EXT`
- **Applies to:** browser extensions (Chrome, Edge, Firefox, Safari) and platform plugins/apps (e.g., IDE extensions, Figma, Slack, Office, Shopify apps)
- **Not applicable when:** no extension or plugin ships

## Evidence

- **Automated:** the manifest (permissions, host permissions, content-security policy, manifest version); the bundle, checked for remote code loading; secrets search.
- **Manual:** install the packaged build; use it on typical and hostile pages; review the store listing and privacy disclosures against behaviour.

## Checks

### Permissions and code
| ID | Check | Verify | Severity |
|---|---|---|---|
| EXT-01 | Permissions and host permissions are the minimum needed, and optional permissions are requested at the moment of use | Manifest | High (store rejection and user trust) |
| EXT-02 | No remotely hosted code is executed (store policies forbid it), and a strict content-security policy is set | Bundle; manifest | Critical |
| EXT-03 | Content scripts treat page content as hostile: messages between page, content script and background are validated, and page data is never executed | Code review | High |
| EXT-04 | Secrets are not bundled; authentication uses the platform's recommended flow | Search; code | Critical |
| EXT-05 | The current manifest/platform API version is used (Manifest V3 for Chromium stores) with no deprecated APIs pending removal | Manifest | High |

### Store and platform
| ID | Check | Verify | Severity |
|---|---|---|---|
| EXT-06 | Store policies are met: a single clear purpose, accurate description, privacy disclosures matching behaviour, a privacy policy URL, and justification for each permission | Listing vs. behaviour | High |
| EXT-07 | Review lead time is in the launch plan, and updates are staged where the store allows | Plan | Medium |
| EXT-08 | Platform plugins (IDE, SaaS marketplaces) meet their marketplace's security review requirements (OAuth scopes, data handling, uninstall webhooks) | Marketplace docs vs. implementation | High where applicable |

### Behaviour
| ID | Check | Verify | Severity |
|---|---|---|---|
| EXT-09 | The extension does not noticeably slow down or break host pages, and it cleans up after itself | Test on heavy sites | Medium |
| EXT-10 | Updates migrate stored settings and data safely | Update test | Medium |
| EXT-11 | Data sent off-device is disclosed and minimal (browsing data is highly sensitive) | Network inspection | High |

## Severity notes

Remote code execution and undisclosed collection of browsing data are Critical, because stores remove extensions for both and users are harmed.
