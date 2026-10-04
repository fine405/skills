# Fine's Agent Skills

[**English**](./README.md) | [简体中文](./README.zh-CN.md)

[![skills.sh](https://skills.sh/b/fine405/skills)](https://skills.sh/fine405/skills)

A curated, installable collection of agent skills for creative production,
interface design, engineering, and visual explanation. This repository unifies
the former `fine405/skills` and `fine405/dev-skills` collections while keeping
each skill independently installable.

## Skills

### AIGC

| Skill | Purpose |
| --- | --- |
| [`app-icon-design`](./skills/aigc/app-icon-design/) | Orchestrate one app-icon identity across themes, visual styles, platforms, and production QA. |
| [`app-icon-theme`](./skills/aigc/app-icon-theme/) | Create coherent theme-driven variants of an existing app icon without losing its identity. |
| [`imagegen-ansi`](./skills/aigc/imagegen-ansi/) | Turn references or raster art into transparent ANSI-style assets and code-ready terminal previews. |
| [`imagegen-glyph-mosaic`](./skills/aigc/imagegen-glyph-mosaic/) | Generate full-color glyph-mosaic illustrations with a coherent character grid and palette logic. |
| [`imagegen-transparent`](./skills/aigc/imagegen-transparent/) | Generate or extract clean transparent assets with chroma-key removal, alpha cleanup, and validation. |

### Design

| Skill | Purpose |
| --- | --- |
| [`design-direction`](./skills/design/design-direction/) | Explore distinctive design directions, refine with independent screenshot critiques, and finish with restrained UI and copy. |
| [`hallmark-study`](./skills/design/hallmark-study/) | Extract reusable design DNA from a screenshot or public URL without cloning protected content. |
| [`hallmark-build`](./skills/design/hallmark-build/) | Design and implement distinctive web UI while preserving the existing product system. |
| [`hallmark-audit`](./skills/design/hallmark-audit/) | Audit UI code and rendered evidence for hierarchy, accessibility, responsiveness, trust, and implementation risk. |

The Hallmark workflow is intentionally split into three explicit skills:

```text
hallmark-study  -> extract abstract design DNA
hallmark-build  -> implement against the product system
hallmark-audit  -> inspect code and rendered evidence without editing
```

### Engineering

| Skill | Purpose |
| --- | --- |
| [`open-source-contribution`](./skills/engineering/open-source-contribution/) | Prepare compliant upstream contributions by checking repository rules, related work, verification gates, attribution, and CI. |

### Productivity

| Skill | Purpose |
| --- | --- |
| [`eli5`](./skills/productivity/eli5/) | Turn a topic into a self-contained, picture-first HTML explainer for a complete beginner. |
| [`write-explain`](./skills/productivity/write-explain/) | Draft and edit clear writing automatically; explain on explicit invocation, with optional HTML or captioned video proposed after delivery for the user to choose. |

## Install

List the available skills:

```bash
npx skills add fine405/skills --list
```

Install one skill:

```bash
npx skills add fine405/skills --skill app-icon-design
```

Install every skill:

```bash
npx skills add fine405/skills --skill '*'
```

The skills CLI discovers skills recursively, so category folders do not change
the installed skill name.

Existing `fine405/dev-skills` users can switch the package source to
`fine405/skills`; all five former development skill names remain unchanged.

## Repository structure

```text
skills/
├── aigc/
│   ├── app-icon-design/
│   ├── app-icon-theme/
│   ├── imagegen-ansi/
│   ├── imagegen-glyph-mosaic/
│   └── imagegen-transparent/
├── design/
│   ├── design-direction/
│   ├── hallmark-audit/
│   ├── hallmark-build/
│   └── hallmark-study/
├── engineering/
│   └── open-source-contribution/
└── productivity/
    ├── eli5/
    └── write-explain/
```

Every skill has a `SKILL.md` and Codex-facing `agents/openai.yaml`. Optional
`references/`, `scripts/`, `examples/`, and `assets/` stay inside the skill so
the directory remains portable when installed by itself. Some small utilities
are deliberately duplicated between independently installable skills; repository
validation prevents those copies from drifting.

## Validate

Run the same checks as CI:

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
python3 -m compileall -q skills scripts tests
```

The validator checks category structure, frontmatter, unique names, agent
metadata, bilingual index coverage, local Markdown links, and synchronized
shared utility copies.

## Attribution and license

The Hallmark skills are adapted from
[`Nutlope/hallmark`](https://github.com/Nutlope/hallmark) under the MIT License.
`eli5` was inspired by Anthropic's community
[`eli5`](https://github.com/anthropics/claude-plugins-community/tree/main/eli5)
plugin and rewritten for Codex Skills. See
[`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md) for details.

Original content is licensed under the [MIT License](./LICENSE).
