# Development Skills

[**English**](./README.md) | [简体中文](./README.zh-CN.md)

Reusable development workflow skills for coding agents.

## Available skills

| Skill | Purpose | Install |
| --- | --- | --- |
| [`open-source-contribution`](./skills/open-source-contribution/) | Prepare compliant upstream contributions by checking repository rules, related issues and pull requests, conflicts, verification gates, attribution, and post-push CI. | `npx skills add fine405/dev-skills --skill open-source-contribution` |

## Open Source Contribution

Use `open-source-contribution` for an end-to-end upstream contribution rather than only drafting the final pull request. The workflow:

1. Reads the target repository's contribution, security, branch, test, and attribution rules.
2. Searches open and closed issues and pull requests, then checks overlap and conflicts.
3. Decides whether a separate issue is useful or the pull request should be the public discussion surface.
4. Implements and verifies the smallest complete change.
5. Publishes only with authorization, follows the repository template, and reports CI and human follow-up honestly.

The skill has no runtime dependency. Publishing requires an authenticated GitHub-capable tool and explicit user authorization.

## Repository structure

```text
skills/
└── open-source-contribution/
    ├── SKILL.md
    └── agents/
        └── openai.yaml
```

## License

[MIT](./LICENSE)
