# 开发 Skills

[English](./README.md) | [**简体中文**](./README.zh-CN.md)

面向编码 Agent 的可复用开发工作流 Skills。

## 可用 Skills

| Skill | 用途 | 安装 |
| --- | --- | --- |
| [`open-source-contribution`](./skills/open-source-contribution/) | 通过检查目标仓库规约、关联 issues/PRs、冲突、验证门槛、归因和推送后的 CI，准备合规的上游贡献。 | `npx skills add fine405/dev-skills --skill open-source-contribution` |

## Open Source Contribution

使用 `open-source-contribution` 处理端到端的上游贡献，而不只是起草最终 PR。工作流会：

1. 读取目标仓库的贡献、安全、分支、测试和归因规则。
2. 搜索开放与关闭的 issues/PRs，并检查重叠工作和冲突。
3. 判断是否值得单独创建 issue，或直接以 PR 作为公开讨论入口。
4. 实现并验证最小完整改动。
5. 仅在获得授权后发布，遵循目标仓库模板，并如实报告 CI 和人工后续事项。

该 Skill 没有运行时依赖。发布时需要已认证的 GitHub 工具和用户的明确授权。

## 仓库结构

```text
skills/
└── open-source-contribution/
    ├── SKILL.md
    └── agents/
        └── openai.yaml
```

## 许可证

[MIT](./LICENSE)
