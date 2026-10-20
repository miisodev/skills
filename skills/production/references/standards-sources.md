# Coverage sources and currentness

Research baseline for the expanded coverage: **2026-10-20**. Links are references for an auditor using their available tools, never a runtime dependency. The shipped scorer performs no network access and needs only Python's standard library. If sources cannot be reached, disclose the currentness limit; do not invent a newer requirement.

The checks combine source-backed protocol distinctions with engineering test scenarios. They do not claim exhaustive control mappings, legal advice or certification. A source's latest revision is not automatically the revision a deployed product promises.

| Area | Primary source | Use and limits |
|---|---|---|
| MCP core | [2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28), [versioning](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning), [transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports) | Distinguish modern per-request/stateless behavior from legacy initialization; audit the advertised versions, including interoperability only where claimed |
| MCP contracts | [Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools), [resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources), [stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio) | Schema, catalog, URI and process/wire boundaries; validate the implemented revision's exact contract |
| MCP authority | [Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization), [security guidance](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) | Protected HTTP discovery, token/resource/issuer checks, proxy consent, URL and continuation-state boundaries; OAuth is not a requirement for stdio |
| MCP extensions | [Extensions framework](https://modelcontextprotocol.io/extensions/overview) | Tasks, Apps and other extensions are optional and independently evolving; inspect the supported extension revision before asserting conformance |
| Agentic systems | [OWASP Agentic Top 10 for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | Threat-model context for authority, tool, memory and multi-agent failure; the agent checklist is an engineering selection rather than a complete framework crosswalk |
| AI baseline | [OWASP September 2026 announcement](https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/) | A newer LLM Top 10 exists; the inherited AIF rows retain the 2025 baseline. No complete 2026 mapping is claimed. Reconcile the applicable newer controls during an audit |
| Agent traces | [OpenTelemetry GenAI observability](https://opentelemetry.io/blog/2026/genai-observability/) | Correlated model/tool context and sensitive-content tradeoffs; implementation examples, not a required vendor or stable attribute contract |
| Supply chain | [SLSA v1.2](https://slsa.dev/spec/v1.2/), [NIST SSDF](https://csrc.nist.gov/Projects/ssdf) | Source/build provenance and consumer verification, secure delivery and vulnerability response; a signature does not establish a SLSA level |
| Runtime probes | [Kubernetes probe guidance](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/) | Distinguish readiness, liveness and startup; apply the principle to the actual runtime without requiring Kubernetes |
| Local-first | [Ink & Switch research](https://www.inkandswitch.com/essay/local-first/) | Offline ownership, collaboration and preservation; conflict/partition/repair test scenarios are engineering derivations and do not require CRDTs |
| Streaming | [Apache Kafka design](https://kafka.apache.org/41/design/design/), [WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) | Delivery guarantees have boundaries; browser WebSocket buffering needs application handling. Neither source proves correctness for another broker/protocol |
| Device software | [NISTIR 8259A](https://csrc.nist.gov/pubs/ir/8259/a/final) | Device cybersecurity starting baseline; physical safety, radio and hardware testing remain separate |
| Non-web accessibility | [W3C WCAG2ICT](https://www.w3.org/TR/wcag2ict-22/) | Guidance on applying WCAG to non-web ICT; not a standalone conformance standard or proof of legal compliance |

## Review practice

For a release or an audit relying on an external requirement, record the applicable edition, source URL, date checked and which checks it affects. Recheck when the implemented protocol, platform, supported market or material threat model changes. Review this register and cited regimes at least quarterly; legal/provider tables elsewhere are inherited baseline material and were not all revalidated by this expansion. Verify their current applicability before making a compliance claim.

An unreachable source is a research limitation. Missing runtime evidence is a check outcome. Keep those distinct: a protocol document describes required behavior but cannot prove the installed server implements it. A marketplace listing or security grade cannot replace tool, package or deployment tests.
