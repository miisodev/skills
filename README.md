# skills

Agent skills for building software products, from the first idea to the go/no-go decision.

[![skills.sh](https://skills.sh/b/miisodev/skills?style=for-the-badge)](https://skills.sh/miisodev/skills)
[![Release](https://img.shields.io/github/v/release/miisodev/skills?style=for-the-badge&labelColor=000000&color=0a0a0a)](https://github.com/miisodev/skills/releases)
[![License: MIT](https://img.shields.io/github/license/miisodev/skills?style=for-the-badge&labelColor=000000&color=0a0a0a)](LICENSE)
[![Sponsor](https://img.shields.io/github/sponsors/miisodev?style=for-the-badge&logo=githubsponsors&labelColor=000000&color=0a0a0a&label=Sponsor)](https://github.com/sponsors/miisodev)
[![PayPal](https://img.shields.io/badge/Donate-PayPal-0a0a0a?style=for-the-badge&logo=paypal&labelColor=000000)](https://paypal.me/miisodev)

The skills are plain Markdown following the open [Agent Skills](https://agentskills.io/) specification. They work in Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, OpenCode, Windsurf and [every other agent the `skills` CLI supports](https://github.com/vercel-labs/skills#supported-agents). They are independent of stack, vendor and region.

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
| [**production**](skills/production/SKILL.md) | An autonomous production readiness audit. In one run it inventories every surface and assesses 32 parts with 604 evidence-backed checks, from functional correctness, security and identity to billing, privacy, accessibility, AI, mobile and launch. It returns a structured JSON payload and report that rank parts and surfaces by risk, with a GO, GO WITH CONDITIONS, HOLD or NO-GO decision per surface and overall. | "Is this ready to launch?" · "Run a production readiness audit" · "Give me a go/no-go for the v2 release" · "Are these screens actually finished?" |

They work well together: the blueprint's `product.md` becomes the requirements standard the production audit checks against.

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

The `production` skill's legal, privacy, tax and accessibility-law material is a starting map for engineering audits, not legal advice. Regulations and thresholds change. Confirm them with the regulator or counsel before relying on them. Review any skill before installing it.

## License

[MIT](LICENSE) © Kevin Miiso Novo
