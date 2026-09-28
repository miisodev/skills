# Package audit

What changes when the product ships as something developers install: a CLI, an SDK, a library, a container image or a plugin published to a registry? Supply-chain integrity, compatibility promises, safe defaults and clear versioning matter most, because every consumer inherits the package's problems. Apply this part **in addition to** the general parts. For packages, read UX as developer experience.

- **Check prefix:** `PKG`
- **Applies to:** CLIs, SDKs, libraries, container images, and anything published to npm, PyPI, crates.io, Maven, NuGet, Homebrew, Docker Hub or similar registries
- **Not applicable when:** nothing is published for others to install

## Evidence

- **Automated:** package manifest (name, version, files included, entry points, engines, install scripts); publish workflow; the built artifact's contents (for example `npm pack --dry-run`); CI matrix; secrets search in the artifact.
- **Manual:** install from the registry, or the packed artifact, on a clean machine; follow the README quickstart; run `--help` and the common commands.

## Checks

### Supply chain and publishing
| ID | Check | Verify | Severity |
|---|---|---|---|
| PKG-01 | Publishing happens from CI with provenance/attestations where the registry supports them (npm provenance, PyPI trusted publishing, signed images) | Publish workflow | High |
| PKG-02 | Registry accounts use 2FA, and publish tokens are scoped and stored only in CI | Settings (or not verified) | High |
| PKG-03 | The published artifact contains only what it should: no secrets, tests with credentials, `.env` files or source maps with private paths | Inspect the packed artifact | Critical if secrets are found |
| PKG-04 | No install scripts that download or run unpinned remote code | Manifest | High |
| PKG-05 | Dependencies are minimal, and ranges are appropriate for a library (not over-pinned, not unbounded) | Manifest | Medium |

### Compatibility and versioning
| ID | Check | Verify | Severity |
|---|---|---|---|
| PKG-06 | Semantic versioning is followed, and breaking changes come with a major version and migration notes | Changelog | High |
| PKG-07 | The supported runtime/OS/architecture matrix is declared (for example `engines`, `python_requires`) and tested in CI | CI matrix | Medium |
| PKG-08 | Public API surface is intentional: private internals are not exported, and deprecations warn before removal | Exports review | Medium |
| PKG-09 | Types (TypeScript declarations, type hints) are shipped and accurate for typed ecosystems | Inspect | Low |

### CLI behaviour
| ID | Check | Verify | Severity |
|---|---|---|---|
| PKG-10 | Destructive commands confirm or require an explicit flag (`--yes`/`--force`), and offer a dry run where it makes sense | Run | High |
| PKG-11 | Exit codes are meaningful and documented; output works without a TTY (CI) and respects `NO_COLOR`; `--help` and `--version` work | Run | Medium |
| PKG-12 | Credentials are stored securely (OS keychain or permission-restricted files), never echoed, and never printed in debug output | Inspect | High |
| PKG-13 | Telemetry is disclosed, with an opt-out documented, and nothing is sent before the first-run notice where consent is required | Inspect | Medium |

### Documentation
| ID | Check | Verify | Severity |
|---|---|---|---|
| PKG-14 | The README quickstart works verbatim on a clean machine | Follow it | High |
| PKG-15 | A changelog, licence file and contribution/security policy exist | Repository | Medium |

## Severity notes

A secret in a published artifact is Critical and must be rotated. Unpublishing does not undo downloads or registry mirrors.
