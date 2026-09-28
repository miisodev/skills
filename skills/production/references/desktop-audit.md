# Desktop audit

What changes when the product ships as a Windows, macOS or Linux application (native, Electron, Tauri or similar)? Code signing, operating-system trust prompts, auto-update, installers, local attack surface, and long-lived installs. Apply this part **in addition to** the general parts for the desktop surface.

- **Check prefix:** `DSK`
- **Applies to:** desktop-app surfaces
- **Not applicable when:** no desktop app ships

## Evidence

- **Automated:** build and packaging configuration; signing and notarization steps in CI; the update feed configuration; the framework's security settings (for Electron: context isolation, node integration, sandbox, remote content); secrets search in source and packaged app.
- **Manual:** install the release build on a clean machine per OS; check for trust warnings; update from the oldest supported version; uninstall and inspect what remains.

## Checks

### Trust and distribution
| ID | Check | Verify | Severity |
|---|---|---|---|
| DSK-01 | Builds are code-signed on every OS (Authenticode on Windows, Developer ID and notarization on macOS, signed packages or checksums on Linux) | Inspect signatures | Critical on macOS (Gatekeeper blocks unsigned apps); High on Windows |
| DSK-02 | First-run trust prompts (SmartScreen reputation, Gatekeeper) are understood and acceptable, and download pages set expectations | Install on a clean machine | Medium |
| DSK-03 | Store packages (Microsoft Store/MSIX, Mac App Store) meet store rules where distributed there | Console | High where used |

### Updates
| ID | Check | Verify | Severity |
|---|---|---|---|
| DSK-04 | Auto-update is served over HTTPS and **signature-verified** before install | Config; code | Critical |
| DSK-05 | Update works from the oldest supported version to the current one, and a bad release can be rolled back or superseded quickly | Test | High |
| DSK-06 | Old clients remain compatible with the backend, or are told to update (CMP-10) | Old build test | High |

### Local security
| ID | Check | Verify | Severity |
|---|---|---|---|
| DSK-07 | Web-technology apps isolate untrusted content: context isolation on, no node integration in renderers, sandboxing on, no loading of remote code into privileged contexts | Framework config | Critical if remote content gets privileged access |
| DSK-08 | No secrets in the packaged app; credentials stored with the OS keychain/credential manager | Search package; code | Critical |
| DSK-09 | Local servers, ports and IPC channels are not reachable by other users or the network, and authenticate their callers | Port scan locally; code | High |
| DSK-10 | The app runs without elevated privileges unless strictly needed; installers do not leave writable privileged paths | Inspect | High |
| DSK-11 | Custom protocol handlers and file associations validate their input | Crafted link or file | High |

### Quality of installation
| ID | Check | Verify | Severity |
|---|---|---|---|
| DSK-12 | Installer and uninstaller are clean: no orphaned services, files or registry entries, and user data handling on uninstall is stated | Install/uninstall | Medium |
| DSK-13 | Crash reporting with symbols is live per release | Crash tool | High |
| DSK-14 | Performance is acceptable at idle and on low-spec hardware: startup time, CPU, memory, battery (PRF-20) | Measure | Medium |
| DSK-15 | High-DPI scaling, OS dark mode, OS accessibility settings and keyboard operation are respected (A11-21) | Test | Medium |
| DSK-16 | Telemetry is disclosed, with opt-out or consent where required, and third-party licence notices are bundled (LGL-10) | Inspect | Medium |

## Severity notes

Unsigned or unverified auto-updates (DSK-04) are Critical: a compromised update feed compromises every install.
