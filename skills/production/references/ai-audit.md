# AI audit

If the product calls a language model or other ML system, are those features secure, reliable, affordable, honest and measured? Model output is probabilistic and model inputs can be hostile, so AI features need their own checks on top of the rest. This part follows the OWASP Top 10 for LLM Applications (2025) and adds quality, cost and transparency checks.

- **Check prefix:** `AIF`
- **Applies to:** any surface exposing a model-backed feature: chat, generation, summarisation, search/RAG, agents and tool use, classification, recommendations
- **Not applicable when:** the product uses no ML/AI features at runtime

## Evidence

- **Automated:** model/provider calls in code (SDKs, endpoints, model IDs); prompt templates and tool definitions; eval suites and their latest results; usage and cost configuration.
- **Manual:** exercise each AI feature with normal inputs, edge inputs, and adversarial inputs **against test data** (planted instructions in documents, attempts to reach another user's data, attempts to trigger tools).

## Checks

### Security (OWASP LLM Top 10)
| ID | Check | Verify | Severity |
|---|---|---|---|
| AIF-01 | Prompt injection is assumed: untrusted content (user input, retrieved documents, web pages, emails, tool output) cannot trigger privileged actions or change policy | Plant instructions in content the model reads | Critical if it leads to data access or actions |
| AIF-02 | Tools and actions available to the model are scoped to the current user's permissions and enforced server-side, not by the prompt | Review tool handlers | Critical |
| AIF-03 | Consequential or irreversible actions (sending, purchasing, deleting, external writes) need user confirmation or a server-side policy check (excessive agency) | Test | High |
| AIF-04 | Model output is treated as untrusted before it reaches HTML, SQL, shell, file paths, URLs or other systems (improper output handling) | Code review | High |
| AIF-05 | Sensitive data, other users' data and secrets are not placed where the model can reveal them to the wrong user; the system prompt contains nothing that would harm if leaked | Review context assembly | High |
| AIF-06 | Retrieval (RAG/vector search) filters by the requesting user's permissions **before** results reach the model | Two-account test | Critical for multi-tenant RAG |
| AIF-07 | Models, weights, datasets and AI dependencies come from trusted sources with pinned versions (supply chain, data poisoning) | Inventory | Medium |

### Quality and honesty
| ID | Check | Verify | Severity |
|---|---|---|---|
| AIF-08 | An evaluation set covers the feature's core tasks and known failure cases, and the current model/prompt passes the defined bar | Eval results | High for AI-core products |
| AIF-09 | Answers that make factual claims are grounded (citations, retrieval) or clearly framed, and the product does not overstate reliability (misinformation) | Test factual prompts | Medium; High in health, legal or finance |
| AIF-10 | AI-generated content and AI interactions are disclosed where users would otherwise be misled, and where law requires it (EU AI Act transparency duties phasing in) | Inspect UI | Medium |
| AIF-11 | Users can give feedback on outputs, and there is a way to correct or report harmful outputs | Inspect | Low |
| AIF-12 | Refusals and failures are handled gracefully in the UI (a refusal, safety block, truncation or empty output never looks like a crash or a success) | Trigger each | Medium |

### Reliability and cost
| ID | Check | Verify | Severity |
|---|---|---|---|
| AIF-13 | Provider errors, rate limits and outages have handling: retries with backoff, fallback model or degraded mode, and a clear message | Simulate failure | High for AI-core products |
| AIF-14 | Per-user and global usage limits exist; the model and effort level suit the task; context is not needlessly large (unbounded consumption) | Code/config; cost estimate | High |
| AIF-15 | Long-running generations stream or show progress, with timeouts sized for the model | Test | Medium |
| AIF-16 | Model versions are pinned or tracked, and a model change is re-evaluated before rollout | Config; process | Medium |

### Data and governance
| ID | Check | Verify | Severity |
|---|---|---|---|
| AIF-17 | Provider data use is known and disclosed: retention, training on customer data, zero-retention options where promised | Provider terms; privacy policy (PRV-09) | High where customers were promised no training |
| AIF-18 | Prompts, completions and tool calls are logged for debugging and abuse review, with PII handling matching the privacy policy | Logging config | Medium |
| AIF-19 | Use cases that affect people's access to jobs, credit, housing, education or essential services are classified for regulatory risk (EU AI Act high-risk, US state laws) and have human oversight | Review | High where applicable |

## Severity notes

Prompt injection that reaches another user's data or an irreversible action is Critical. A missing eval set is High only where AI is the core value. Otherwise it is Medium.
