# Mobile audit

What changes when the product ships as an iOS or Android app, native or cross-platform? Store review, binaries that can be decompiled, devices that stay on old versions for years, on-device data, platform billing rules, and permission prompts. Apply this part **in addition to** the general parts for the app surface. It follows the OWASP MASVS areas where security is concerned.

- **Check prefix:** `MOB`
- **Applies to:** mobile-app surfaces (iOS, Android, cross-platform frameworks, and PWAs installed to the home screen for MOB-14 to MOB-16)
- **Not applicable when:** no mobile app ships

## Evidence

- **Automated:** build configuration (bundle IDs, versioning, signing, entitlements, permissions in `Info.plist`/`AndroidManifest.xml`); secrets search in the app source **and** the built binary if available; crash-reporting and symbol upload setup; the OTA update configuration.
- **Manual:** install a release build on a real low-end device; walk core journeys; deny each permission; go offline; upgrade from the previous released version; compare the store listing and privacy declarations with actual behaviour.

## Checks

### Store readiness
| ID | Check | Verify | Severity |
|---|---|---|---|
| MOB-01 | Store listing is complete: name, subtitle, description, screenshots for required sizes, preview, category, age rating, support URL, privacy policy URL | Store console (or not verified) | High |
| MOB-02 | Privacy declarations (App Store privacy labels, Google Play Data safety) match what the app and its SDKs actually collect | Compare with network traffic and SDK list | Critical (rejection or enforcement) |
| MOB-03 | Review notes include working demo credentials and explain non-obvious features; review time is in the launch plan | Console | Medium |
| MOB-04 | Release uses staged/phased rollout, and the version/build numbering scheme is correct | Console config | Medium |

### Security (MASVS)
| ID | Check | Verify | Severity |
|---|---|---|---|
| MOB-05 | Sensitive data on the device is stored in the Keychain/Keystore or encrypted storage, never in plain preferences, logs or backups | Code; inspect storage | High |
| MOB-06 | No secrets or privileged keys in the binary (assume it will be decompiled) | Search source and binary | Critical |
| MOB-07 | Network traffic is TLS-only (no cleartext exceptions without reason); certificate pinning is a deliberate decision with a rotation plan | Config | High |
| MOB-08 | Deep links and universal/app links are verified, and their parameters are validated like any untrusted input | Test crafted links | High |

### Platform rules
| ID | Check | Verify | Severity |
|---|---|---|---|
| MOB-09 | Account deletion is available in-app wherever accounts can be created (required by both stores) | Walk it | Critical |
| MOB-10 | Store policies for the app's category are met: user-generated content needs reporting, blocking and moderation (SAF-02, SAF-03); sign-in rules, kids category, health, finance and crypto rules | Policy review vs. features | High |
| MOB-11 | Digital goods and subscriptions use platform in-app purchase where store rules require it (rules vary by region and change), with server-side receipt/notification validation, restore purchases, and entitlements synced with web billing | Code; store rules | Critical if non-compliant |
| MOB-12 | Permission prompts are requested in context, with clear purpose strings, and the app works (degraded) when permission is denied | Deny each permission | High |
| MOB-13 | Tracking across apps follows platform rules (iOS App Tracking Transparency prompt before tracking; Android advertising ID policies) | Inspect SDKs and prompts | High |

### Lifecycle
| ID | Check | Verify | Severity |
|---|---|---|---|
| MOB-14 | Old app versions keep working, or a tested forced/soft-update mechanism exists (CMP-10) | Old build against the new backend | High |
| MOB-15 | Crash reporting is live with symbolication (dSYMs/mapping files uploaded per release), with a crash-free-session target | Crash tool | High |
| MOB-16 | Over-the-air update channels (if used) point at production, are signed, comply with store policy, and can be rolled back | Config | High where used |
| MOB-17 | Upgrades from the previous released version migrate on-device data without loss or forced logout | Upgrade test | High |
| MOB-18 | Push notifications, background tasks and offline sync behave correctly after app kill, reboot and poor connectivity | Device test | Medium |
| MOB-19 | Remote kill switches or feature flags can disable broken features without a store release | Config | Medium |

## Severity notes

A crash on launch on any supported OS version, a secret in the binary, a privacy-label mismatch, or missing in-app account deletion is Critical: each leads to rejection, removal or a data incident.
