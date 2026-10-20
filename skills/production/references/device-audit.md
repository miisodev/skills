# Device and embedded software audit

Can the device remain controllable, authentic and recoverable throughout its service life? This is a software engineering baseline, not a functional-safety, radio or hardware certification.

- **Check prefix:** `DEV`
- **Applies to:** firmware, embedded/IoT software, gateways, device companions and software controlling physical outputs
- **Not applicable when:** the product has no device runtime or physical control boundary

## Evidence

Inspect firmware/update artifacts, identity provisioning, supported boards and device threat model. Use an emulator or isolated device fixture with actuators disabled. Hardware-dependent evidence unavailable in this run is not_verified.

## Checks

### Identity and protection

| ID | Check | Verify | Severity |
|---|---|---|---|
| DEV-01 | Devices have distinct identities and avoid fleet-wide shared administrative secrets | Inspect provisioning and two-device credentials | Critical |
| DEV-02 | Pairing and ownership transfer authenticate the intended physical device and owner | Attempt unauthorized pairing and transfer on test devices | Critical |
| DEV-03 | Unused interfaces and production debug access are disabled or access-controlled | Inspect release configuration and exposed interfaces | High |
| DEV-04 | Boot/update trust rejects unauthorized images and protects signing keys | Verify a modified image is rejected on a test target | Critical |
| DEV-05 | Device secrets and private data resist the stated physical/network threat model | Inspect key storage and extraction assumptions; cite hardware evidence | High |
| DEV-06 | Commands and telemetry validate bounds, identity, sequence and freshness | Replay and alter safe fixture commands | Critical |

### Updates and lifecycle

| ID | Check | Verify | Severity |
|---|---|---|---|
| DEV-07 | Interrupted update or power loss recovers to a usable authenticated state | Cut simulated power during update in a hardware-safe fixture | Critical |
| DEV-08 | Rollback prevents known-vulnerable firmware while retaining a supported recovery path | Try a signed older image and the recovery procedure | High |
| DEV-09 | Battery, storage wear, memory and bandwidth fit supported duty cycles | Measure resource use and inspect endurance evidence | High |
| DEV-10 | Loss of network/time service enters a defined safe state | Disconnect dependencies with physical outputs isolated | Critical |
| DEV-11 | Units, calibration, sensor faults and stale readings cannot trigger unsafe outputs | Inject out-of-range/stale data with actuator simulation | Critical |
| DEV-12 | Reset, resale and decommissioning remove credentials and private data | Reset a test unit and attempt former-owner access | High |
| DEV-13 | Support period, vulnerability reporting and update delivery are clear to operators | Compare policy with update infrastructure and inventory | Medium |
| DEV-14 | Fleet rollout can detect regressions, stop deployment and identify affected devices | Review staged-update and failure telemetry evidence | High |

## Severity notes

Unsafe physical effects, unauthorized control and unrecoverable fleet updates are Critical. Never energize actuators or alter live safety systems for an audit. Record the specialist/hardware validation required; an emulator passing does not prove real-device behavior.

## Sources

Reviewed 2026-10-20. These sources inform the controls; the table is an engineering checklist, not a conformance certificate. Apply version-specific requirements only to versions the product claims.

- [NISTIR 8259A](https://csrc.nist.gov/pubs/ir/8259/a/final): device identity, configuration, data protection, interface restriction, software update and cybersecurity-state baseline.
- [NIST SSDF](https://csrc.nist.gov/Projects/ssdf): release/update security context. Physical fault and endurance scenarios are additional engineering judgments and need product-specific test evidence.
