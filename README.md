# skills

Agent skills for building software products, from the first idea to the go/no-go decision.

[![skills.sh](https://skills.sh/b/miisodev/skills?style=for-the-badge)](https://skills.sh/miisodev/skills)
[![Release](https://img.shields.io/github/v/release/miisodev/skills?style=for-the-badge&labelColor=000000&color=0a0a0a)](https://github.com/miisodev/skills/releases)
[![License: MIT](https://img.shields.io/github/license/miisodev/skills?style=for-the-badge&labelColor=000000&color=0a0a0a)](LICENSE)
[![Sponsor](https://img.shields.io/github/sponsors/miisodev?style=for-the-badge&logo=githubsponsors&labelColor=000000&color=0a0a0a&label=Sponsor)](https://github.com/sponsors/miisodev)
[![PayPal](https://img.shields.io/badge/Donate-PayPal-0a0a0a?style=for-the-badge&logo=paypal&labelColor=000000)](https://paypal.me/miisodev)

The skills are plain Markdown following the open [Agent Skills](https://agentskills.io/) specification. They work in Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, OpenCode, Windsurf and [every other agent the `skills` CLI supports](https://github.com/vercel-labs/skills#supported-agents). They are independent of stack, vendor and region.

Find [blueprint](https://mcprush.com/miisodev/blueprint), [production](https://mcprush.com/miisodev/production) and [BrainLLM](https://mcprush.com/miisodev/brainllm-mcp) together on the [MCPRush publisher page](https://mcprush.com/miisodev). The commands below install the complete skill folders from this repository.

## Install

```bash
npx skills add miisodev/skills
```

Install a single skill:

```bash
npx skills add miisodev/skills --skill blueprint
npx skills add miisodev/skills --skill production
```

Install globally for a specific agent without prompts:

```bash
npx skills add miisodev/skills --skill '*' -g -a claude-code -y
```

Update later with `npx skills update`.

<details>
<summary>Other ways to install</summary>

**Claude Code plugin marketplace**

```
/plugin marketplace add miisodev/skills
/plugin install miisodev-skills@miisodev-skills
```

**Manually:** copy a folder from [`skills/`](skills) into your agent's skills directory (for example `.claude/skills/`, `.agents/skills/` or `~/.codex/skills/`).

</details>

## Skills

| Skill | What it does | Try |
|---|---|---|
| [**blueprint**](skills/blueprint/SKILL.md) | Establishes a project's foundation together with you in seven documents: vision, market, business, product, brand, stack and plan. It covers the core idea, market research and strategy, the business model and unit economics, targets, requirements, brand, stack, resources and the grand plan. Each document is discussed, researched and computed, drafted, critiqued and approved by you, with a workbook so the work resumes in any session. It sets intent and leaves design and implementation to the model that builds. | "Let's blueprint this idea" · "Continue the blueprint" · "Our pricing changed, update the blueprint" · "Turn our PRDs into a blueprint" |
| [**production**](skills/production/SKILL.md) | An autonomous readiness audit across 39 parts with 753 evidence-backed checks. It inventories surfaces, assesses applicable checks and returns a structured JSON payload and report ranking parts and surfaces by risk. Decisions are GO, GO WITH CONDITIONS, HOLD or NO-GO per surface and overall. | "Is this ready to launch?" · "Run a production readiness audit" · "Give me a go/no-go for the v2 release" · "Are these screens actually finished?" · "Audit this MCP server before release" |

They work well together: the production audit finds the blueprint wherever the project keeps it, and its `product.md` becomes the requirements standard the audit checks against.

### Production coverage

The shared checks cover functional behavior, UX, accessibility, security, identity, data, privacy, reliability, operations, AI, billing and launch. Version 1.1.0 adds dedicated coverage for:

| Boundary | What the audit examines |
|---|---|
| MCP servers, clients and hosts | Protocol versions, tool/resource contracts, permissions, transports and supported extensions |
| Agents and automation | Delegated authority, approvals, budgets, cancellation and recovery without duplicated actions |
| Self-hosted deployments | Installation, configuration, upgrades, recovery and disconnected operation |
| Offline synchronization | Durable local work, conflicts, reconnects and revoked access |
| Real-time and event systems | Delivery guarantees, stream access, backpressure and replay |
| Device and embedded software | Identity, pairing, authenticated updates and failure recovery |
| Software supply chains | Build provenance, artifact verification and compromised-release response |

Apply these to the capabilities a product actually has. A static site does not need billing; a local MCP server does not need a cloud deployment. Existing mobile, desktop, extension and package checks remain, with added data-pipeline, model-lifecycle, SDK/CLI and non-web accessibility checks. See the [product routing guide](skills/production/references/product-routing.md).

### Requirements

- `blueprint`: none beyond an agent that can read and write files. Web access improves market research.
- `production`: Python 3.8+ for the scoring script (standard library only). Without it, the agent applies the documented decision rules by hand.

## Versioning

Releases follow [Semantic Versioning](https://semver.org/) and are listed in the [changelog](CHANGELOG.md) and on [GitHub Releases](https://github.com/miisodev/skills/releases). Each skill's version is in its `SKILL.md` frontmatter (`metadata.version`).

## Support this work

If these skills save you time, you can support further work:

- [GitHub Sponsors](https://github.com/sponsors/miisodev)
- [PayPal](https://paypal.me/miisodev)

## Contributions

This repository does not accept contributions. Pull requests are closed automatically, and issues are disabled. The skills are MIT licensed: fork the repository and do whatever you like with your copy. Security reports are welcome privately (see [SECURITY.md](SECURITY.md)).

## Disclaimer

The `production` skill's legal, privacy, tax and accessibility-law material is a starting map for engineering audits, not legal advice. Regulations and thresholds change. Confirm them with the regulator or counsel before relying on them. The audit is an engineering assessment, not a regulatory, functional-safety or platform certification. Its [source register](skills/production/references/standards-sources.md) records the expanded coverage baseline and how to check applicability/currentness. Review any skill before installing it.

## License

[MIT](LICENSE) © Kevin Miiso Novo
