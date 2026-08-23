# Development Skills

[**English**](./README.md) | [简体中文](./README.zh-CN.md)

Reusable development workflow skills for coding agents.

## Available skills

| Skill | Purpose | Install |
| --- | --- | --- |
| [`eli5`](./skills/eli5/) | Turn a topic into a self-contained, picture-first HTML explainer for a complete beginner. | `npx skills add fine405/dev-skills --skill eli5` |
| [`hallmark-build`](./skills/hallmark-build/) | Design and implement distinctive web UI while preserving the existing product system and verifying the rendered result honestly. | `npx skills add fine405/dev-skills --skill hallmark-build` |
| [`hallmark-audit`](./skills/hallmark-audit/) | Audit UI code and rendered evidence for hierarchy, generic AI patterns, accessibility, responsiveness, trust, and implementation risks. | `npx skills add fine405/dev-skills --skill hallmark-audit` |
| [`hallmark-study`](./skills/hallmark-study/) | Extract reusable design DNA from a screenshot or public URL without cloning pixels, copy, or proprietary assets. | `npx skills add fine405/dev-skills --skill hallmark-study` |
| [`open-source-contribution`](./skills/open-source-contribution/) | Prepare compliant upstream contributions by checking repository rules, related issues and pull requests, conflicts, verification gates, attribution, and post-push CI. | `npx skills add fine405/dev-skills --skill open-source-contribution` |

## ELI5

Use `eli5` to explain a topic with three to five large visual scenes, very little text, and one faithful everyday analogy. It produces a responsive, standalone HTML file that works without a build step or network access.

Inspired by Anthropic's community [`eli5`](https://github.com/anthropics/claude-plugins-community/tree/main/eli5) plugin and rewritten for Codex Skills.

## Open Source Contribution

Use `open-source-contribution` for an end-to-end upstream contribution rather than only drafting the final pull request. The workflow:

1. Reads the target repository's contribution, security, branch, test, and attribution rules.
2. Searches open and closed issues and pull requests, then checks overlap and conflicts.
3. Decides whether a separate issue is useful or the pull request should be the public discussion surface.
4. Implements and verifies the smallest complete change.
5. Publishes only with authorization, follows the repository template, and reports CI and human follow-up honestly.

The skill has no runtime dependency. Publishing requires an authenticated GitHub-capable tool and explicit user authorization.

## Hallmark suite

The Hallmark suite turns the original multi-mode design skill into three
standalone, explicit-invocation skills:

```text
hallmark-study  -> extract abstract design DNA
hallmark-build  -> implement against the user's product system
hallmark-audit  -> inspect code plus rendered evidence without editing
```

Each skill carries the same compact core invariants but loads only the guidance
needed for its job. `hallmark-build` and `hallmark-audit` also include an
identical, zero-dependency static scanner:

```bash
python3 skills/hallmark-audit/scripts/hallmark_lint.py <path>
```

The scanner catches deterministic source signals such as missing image alt text,
duplicate IDs, broad transitions, missing reduced-motion fallbacks, raw colors,
and inaccessible custom buttons. It always returns a separate manual-check list;
a clean scan never claims that responsive behavior, contrast, accessibility, or
visual quality passed.

The skills do not create `tokens.css`, preview files, or project-memory files
unless the user's project actually needs them. Build verification runs after
implementation, so a pre-build preview cannot claim an unperformed quality
score.

These skills are adapted from
[`Nutlope/hallmark`](https://github.com/Nutlope/hallmark) commit
[`13ac0ec`](https://github.com/Nutlope/hallmark/commit/13ac0ec7e148655948100b6396439e481361d690)
under the MIT License. See [Third-party notices](./THIRD_PARTY_NOTICES.md); each
installed Hallmark skill also contains the upstream license.

## Repository structure

```text
skills/
├── eli5/
│   ├── SKILL.md
│   └── agents/
│       └── openai.yaml
├── hallmark-build/
│   ├── SKILL.md
│   ├── UPSTREAM_LICENSE
│   ├── agents/openai.yaml
│   ├── references/
│   └── scripts/hallmark_lint.py
├── hallmark-audit/
│   ├── SKILL.md
│   ├── UPSTREAM_LICENSE
│   ├── agents/openai.yaml
│   ├── references/
│   └── scripts/hallmark_lint.py
├── hallmark-study/
│   ├── SKILL.md
│   ├── UPSTREAM_LICENSE
│   ├── agents/openai.yaml
│   └── references/
└── open-source-contribution/
    ├── SKILL.md
    └── agents/
        └── openai.yaml
```

## License

[MIT](./LICENSE)
