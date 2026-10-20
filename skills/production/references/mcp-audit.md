# MCP audit

Does the complete MCP boundary work safely, from host intent through transport and handler to upstream services? Apply API, identity, security, package and deployment checks too; MCP is not merely an HTTP endpoint.

- **Check prefix:** `MCP`
- **Applies to:** MCP servers, clients, hosts, gateways and MCP Apps, local or remote
- **Not applicable when:** the product neither implements nor embeds MCP

## Evidence

Capture protocol traces, declared revisions, capabilities, schemas and client/transport test matrices. Exercise a disposable server and test credentials; inspect host policy as well as handlers. Listing a tool is not proof it can be called correctly. A server need not invoke a model itself for this part to apply.

## Checks

### Protocol and interoperability

| ID | Check | Verify | Severity |
|---|---|---|---|
| MCP-01 | Supported protocol revisions, transports, roles and extensions are explicit and exercised | Run each advertised combination, including unsupported-version handling | High |
| MCP-02 | Lifecycle follows the selected revision: legacy initialization versus modern per-request metadata and discovery | Trace startup and a request after reconnect; do not require sessions on stateless revisions | High |
| MCP-03 | JSON-RPC framing, IDs, errors and malformed-message handling match the revision | Protocol fixtures for invalid params, unknown methods and concurrent IDs | High |
| MCP-04 | stdio keeps diagnostic output off stdout and exits cleanly at EOF | Launch from a clean process; capture both streams; close stdin | High |
| MCP-05 | HTTP transport handles content negotiation, version/routing metadata and disconnects through the actual proxy | Integration trace through deployed ingress using test traffic | High |
| MCP-06 | Capabilities and optional features are truthful; unsupported features fail predictably | Compare advertised capabilities with calls; test extension opt-in | Medium |
| MCP-07 | Tools have valid input/output schemas and return the documented content and error semantics | Validate schemas; call valid and invalid arguments; distinguish protocol errors from tool failures | High |
| MCP-08 | Resource URIs/templates and prompt arguments resolve with correct content types and access rules | Enumerate and read resources; resolve templates; retrieve a prompt with missing arguments | High |
| MCP-09 | Catalog pagination, ordering and any caching or change notifications stay correct across authorization changes | Page catalogs with two permission sets; invalidate a cached definition | High |
| MCP-10 | Interoperability is demonstrated with supported hosts/clients, not just an in-process SDK test | Run a core workflow on the declared support matrix | High |

### Authority and trust boundaries

| ID | Check | Verify | Severity |
|---|---|---|---|
| MCP-11 | Every tool call and resource read enforces the caller permissions at execution | Use isolated users A/B and a revoked credential; directly call an undisclosed tool | Critical |
| MCP-12 | Protected HTTP deployments implement the applicable authorization discovery and registration flow | Trace challenge, resource metadata, issuer discovery and supported registration path | High |
| MCP-13 | Tokens are validated for intended resource, issuer, scope and lifetime; upstream tokens are not passed through as MCP authority | Negative token tests; inspect upstream credential separation | Critical |
| MCP-14 | Clients bind credentials to their issuer and validate redirects, state, PKCE and authorization responses as required | Review OAuth flow and wrong-issuer/redirect test cases | High |
| MCP-15 | Gateway and proxy consent cannot turn one client into a confused deputy for another | Test changed client identity and upstream account selection with test accounts | Critical |
| MCP-16 | Discovery, redirects, resource URLs and tool URL arguments cannot reach unintended network destinations | Inspect URL validation and isolated SSRF fixtures, including redirect chains | High |
| MCP-17 | HTTP origins and local listeners resist browser-to-local abuse; stdio launch avoids untrusted command interpolation | Inspect binding/origin policy and argument-array process launch | High |
| MCP-18 | Tool descriptions, annotations, prompts and returned resources cannot grant themselves host authority | Plant hostile instructions in a fixture tool result; inspect host policy enforcement | Critical |
| MCP-19 | Destructive tool behavior matches annotations and requires the product authorization policy at execution | Compare declarations with effects; test denial and changed arguments after approval | High |
| MCP-20 | Filesystem roots and resource identifiers are constraints enforced by code, not assumed sandboxes | Test traversal, symlinks and unauthorized resource identifiers on a fixture filesystem | Critical |

### Operation and extensions

| ID | Check | Verify | Severity |
|---|---|---|---|
| MCP-21 | Cancellation, deadlines and concurrency limits bound backend work and result sizes | Cancel a slow test tool and observe cleanup and quotas | High |
| MCP-22 | Retries and multi-round continuations do not duplicate effects or reuse another caller state | Repeat after simulated disconnect; tamper with or swap continuation handles | Critical |
| MCP-23 | Sampling, elicitation and external navigation respect consent, secret handling and supported capabilities | Decline input; inspect context sent upstream; test unsupported client capability | High |
| MCP-24 | Task handles and any subscriptions are authorized, expiring and cleaned up across restarts | Use another caller handle; expire a handle; restart a test instance | High |
| MCP-25 | MCP Apps isolate UI code and constrain network, navigation and resource access to the declared policy | Inspect app sandbox/CSP; test hostile content and denied destinations | High |
| MCP-26 | Logs redact credentials and private arguments while retaining tool outcome, latency and caller attribution | Inspect successful, failed and denied test-call logs | High |
| MCP-27 | Install/listing instructions reproduce the shipped artifact, transport and required permissions | Follow quickstart from a clean profile; compare marketplace claims with actual server | Medium |
| MCP-28 | Shutdown/restart and catalog changes recover without leaking state between users or processes | Restart during reads/writes; change a catalog and reconnect | High |

## Severity notes

Cross-user access, unauthorized execution and duplicated irreversible effects are Critical. Set core_flow for the tools and resources that deliver the product value. Mark host behavior not_verified when only the server is available; do not infer host consent from tool annotations. OAuth-specific rows do not apply to a local stdio-only server, but its local authority still does.

## Sources

Reviewed 2026-10-20. These sources inform the controls; the table is an engineering checklist, not a conformance certificate. Apply version-specific requirements only to versions the product claims.

- [Versioning](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning) and [transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports), including [stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio): lifecycle and transport rows.
- [Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) and [resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources): contract/discovery rows.
- [Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization): protected HTTP rows; do not impose HTTP OAuth on stdio.
- [Security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices): deputy, token, network and state boundaries.
- [Extensions](https://modelcontextprotocol.io/extensions/overview): inspect the revision of each implemented extension; unsupported extensions are inapplicable.
