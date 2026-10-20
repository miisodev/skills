# Software supply chain audit

Can the consumer establish what was shipped, who built it and whether it has been altered? Package checks cover developer usability; these controls apply to applications and internal delivery too.

- **Check prefix:** `SCH`
- **Applies to:** all shipped source, binaries, containers, dependencies, models, plugins and update channels
- **Not applicable when:** no software or executable artifact is delivered or operated

## Evidence

Inspect the actual release artifact and its build/publish route. Verify a provenance/signature fixture with the consumer verification path, including a deliberately modified artifact. CI claims alone are documented evidence until verified.

## Checks

### Build and provenance

| ID | Check | Verify | Severity |
|---|---|---|---|
| SCH-01 | The release artifact can be traced to intended source, build configuration and builder identity | Compare artifact digest with provenance and source revision | High |
| SCH-02 | Build inputs and downloaded tools are pinned with an update process appropriate to their ecosystem | Review clean-build resolution, lockfiles and fetched build tools | High |
| SCH-03 | Untrusted contribution builds cannot access release credentials or influence trusted artifacts | Inspect pipeline trust boundaries and cache permissions | Critical |
| SCH-04 | Build environments are isolated and cleaned between trust domains | Inspect runner lifecycle and shared workspace/cache boundaries | High |
| SCH-05 | An inventory/SBOM identifies shipped components and versions, including bundled/transitive artifacts | Compare inventory with unpacked binary/image and dependency graph | Medium |
| SCH-06 | Supported vulnerability feeds are triaged for actual reachability and remediation deadlines | Inspect a current finding and its closure/exception evidence | High |

### Distribution and response

| ID | Check | Verify | Severity |
|---|---|---|---|
| SCH-07 | Consumers verify release/update integrity and publisher identity before execution | Tamper with a test artifact and exercise the real install/update verifier | Critical |
| SCH-08 | Provenance verification checks expected builder, source and artifact digest rather than signature existence only | Try a valid signature from an unexpected builder/source | High |
| SCH-09 | Publishing authority uses least privilege and recoverable, audited credential rotation | Inspect release identities, scopes and rotation evidence | High |
| SCH-10 | Versioned artifacts are immutable or changes are transparently identified and rejected when unexpected | Compare registry/tag behavior with pinned digest and rollback policy | High |
| SCH-11 | Licenses and redistribution obligations cover every bundled dependency, model and asset | Compare notices/licensing inventory with shipped contents | High |
| SCH-12 | A compromised release can be identified, withdrawn and replaced with consumer guidance | Tabletop a signing-key compromise and list affected versions | High |
| SCH-13 | End-of-support and known-vulnerable releases have an explicit consumer response path | Inspect support policy, advisories and upgrade guidance | Medium |
| SCH-14 | The shipped artifact is exercised after packaging, including offline/runtime dependencies | Install the release output in a clean supported environment | High |

## Severity notes

An attacker-controlled release path or accepted tampered update is Critical. A missing SBOM by itself is Medium unless a contractual obligation raises impact. Do not claim a SLSA level from the presence of an attestation; verify the requirements for the claimed track and level.

## Sources

Reviewed 2026-10-20. These sources inform the controls; the table is an engineering checklist, not a conformance certificate. Apply version-specific requirements only to versions the product claims.

- [SLSA v1.2](https://slsa.dev/spec/v1.2/): source/build trust, provenance and consumer verification.
- [NIST SSDF](https://csrc.nist.gov/Projects/ssdf): protect software and respond to vulnerabilities. These checks do not imply certification or prescribe a particular CI vendor.
