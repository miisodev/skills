# Deployment and operability audit

Can the supported operator install, run, upgrade and recover the product away from the author deployment? Shared infrastructure checks remain applicable; this part tests what is delivered to an operator.

- **Check prefix:** `DEP`
- **Applies to:** services, self-hosted software, containers, appliances and customer-managed or disconnected installations
- **Not applicable when:** the product ships no deployed runtime; use package checks for libraries

## Evidence

Follow installation instructions in a fresh disposable environment matching the supported matrix. Read manifests, service units, config validation, upgrade scripts, health probes and operator docs. Rehearse updates and recovery on test data.

## Checks

### Installation and configuration

| ID | Check | Verify | Severity |
|---|---|---|---|
| DEP-01 | Supported deployment modes, resource minima and external dependencies are explicit | Compare docs with startup behavior on the smallest supported environment | Medium |
| DEP-02 | A clean installation reaches a useful core action without undocumented operator steps | Follow the shipped guide on an empty instance | High |
| DEP-03 | Invalid or missing configuration fails with actionable errors before accepting work | Start with invalid URLs, credentials, ports and storage paths | High |
| DEP-04 | First-run access has no shared default credential or exposed unauthenticated admin setup | Install on a test network and inspect bootstrap access | Critical |
| DEP-05 | Runtime permissions, filesystem ownership and network access are minimized | Inspect effective user, capabilities, mounts and listener bindings | High |
| DEP-06 | Proxy prefixes, TLS termination and trusted forwarding headers work without bypasses | Test supported reverse-proxy configurations and spoofed forwarding headers | High |
| DEP-07 | Disconnected or private-network promises hold with egress denied | Block outbound traffic and exercise install, license checks, updates and core work | High |
| DEP-08 | Secrets and identity are configurable and rotatable without rebuilding the artifact | Rotate a test credential; inspect mounted config and restart behavior | High |

### Runtime and upgrades

| ID | Check | Verify | Severity |
|---|---|---|---|
| DEP-09 | Startup, readiness and liveness distinguish slow boot, temporary unavailability and a dead process | Inject startup delay and a failed dependency; inspect probe decisions | High |
| DEP-10 | Graceful shutdown stops admission, drains work and flushes durable state within the runtime deadline | Terminate during a test request/job and inspect completion | High |
| DEP-11 | CPU, memory, disk, file-descriptor and process limits have predictable failure behavior | Bound resources in a lab; inspect errors and state integrity | High |
| DEP-12 | Persistent volumes, permissions and backup scope survive instance replacement | Replace the runtime while retaining supported storage | Critical |
| DEP-13 | Upgrade from supported previous versions handles data migration and mixed versions | Upgrade realistic test data; run old and new clients concurrently | High |
| DEP-14 | Failed upgrades leave a documented rollback or forward-recovery path for both data and binaries | Interrupt an upgrade and execute recovery on test data | Critical |
| DEP-15 | Replicas coordinate singleton work and avoid assuming process-local session state | Route related requests to different instances; inspect duplicate jobs | High |
| DEP-16 | Optional services can be absent without preventing unrelated core work | Disable each optional integration in a test deployment | Medium |

### Operator handoff

| ID | Check | Verify | Severity |
|---|---|---|---|
| DEP-17 | Operator docs cover ports, storage, backup, restore, monitoring and incident ownership | Operate an instance using the delivered docs only | Medium |
| DEP-18 | Export, uninstall and end-of-service paths preserve customer data as promised | Export and remove a disposable install; inspect remnants | High |
| DEP-19 | Telemetry and remote support access match disclosures and can be controlled as promised | Inspect network behavior and support-access lifecycle | High |
| DEP-20 | Health/config diagnostics are useful without disclosing secrets or private records | Review diagnostic bundle and failed-start output | Medium |

## Severity notes

Exposed bootstrap administration, lost persistent data and unrecoverable upgrades are Critical. No clustering, autoscaling or cloud dependency is required when the product promises a single local process. Test the deployment model it actually sells.

## Sources

Reviewed 2026-10-20. These sources inform the controls; the table is an engineering checklist, not a conformance certificate. Apply version-specific requirements only to versions the product claims.

- [Kubernetes probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/): readiness/startup/liveness distinctions, applicable beyond this example platform.
- [NIST SSDF](https://csrc.nist.gov/Projects/ssdf): secure defaults and delivered configuration context. Installation, upgrade and operator-recovery scenarios are product-specific engineering tests, not a requirement to use orchestration.
