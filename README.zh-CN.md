# 开发 Skills

[English](./README.md) | [**简体中文**](./README.zh-CN.md)

面向编码 Agent 的可复用开发工作流 Skills。

## 可用 Skills

| Skill | 用途 | 安装 |
| --- | --- | --- |
| [`eli5`](./skills/eli5/) | 将主题制作成面向零基础读者、图片优先的独立 HTML 图解。 | `npx skills add fine405/dev-skills --skill eli5` |
| [`hallmark-build`](./skills/hallmark-build/) | 在保留现有产品系统的前提下设计并实现有明确结构的 Web UI，并如实验证渲染结果。 | `npx skills add fine405/dev-skills --skill hallmark-build` |
| [`hallmark-audit`](./skills/hallmark-audit/) | 从代码与渲染证据审计层级、AI 默认模式、可访问性、响应式、可信度和实现风险。 | `npx skills add fine405/dev-skills --skill hallmark-audit` |
| [`hallmark-study`](./skills/hallmark-study/) | 从截图或公开 URL 提取可复用的设计 DNA，同时避免复制像素、文案或专有资产。 | `npx skills add fine405/dev-skills --skill hallmark-study` |
| [`open-source-contribution`](./skills/open-source-contribution/) | 通过检查目标仓库规约、关联 issues/PRs、冲突、验证门槛、归因和推送后的 CI，准备合规的上游贡献。 | `npx skills add fine405/dev-skills --skill open-source-contribution` |

## ELI5

使用 `eli5` 将一个主题拆成三到五个大幅视觉场景，配合极少文字和一个准确的日常类比。它会生成响应式、无需构建步骤或网络连接即可打开的独立 HTML 文件。

灵感来自 Anthropic 社区的 [`eli5`](https://github.com/anthropics/claude-plugins-community/tree/main/eli5) 插件，并针对 Codex Skills 重新编写。

## Open Source Contribution

使用 `open-source-contribution` 处理端到端的上游贡献，而不只是起草最终 PR。工作流会：

1. 读取目标仓库的贡献、安全、分支、测试和归因规则。
2. 搜索开放与关闭的 issues/PRs，并检查重叠工作和冲突。
3. 判断是否值得单独创建 issue，或直接以 PR 作为公开讨论入口。
4. 实现并验证最小完整改动。
5. 仅在获得授权后发布，遵循目标仓库模板，并如实报告 CI 和人工后续事项。

该 Skill 没有运行时依赖。发布时需要已认证的 GitHub 工具和用户的明确授权。

## Hallmark 套件

Hallmark 套件将原来包含多种模式的设计 Skill 拆成三个可独立安装、仅显式调用的 Skills：

```text
hallmark-study  → 提取抽象设计 DNA
hallmark-build  → 基于用户自己的产品系统实施
hallmark-audit  → 结合代码和渲染证据审计，不修改文件
```

每个 Skill 都携带相同的精简核心不变量，但只加载当前任务需要的细节。`hallmark-build`
与 `hallmark-audit` 还包含完全相同、零依赖的静态扫描器：

```bash
python3 skills/hallmark-audit/scripts/hallmark_lint.py <path>
```

扫描器可以确定性发现图片缺少 `alt`、重复 ID、过宽 transition、缺少减少动态效果
回退、绕过 token 的颜色和不可访问的自定义按钮等源码信号。它始终单独列出仍需人工执行的
检查；静态扫描干净不代表响应式、对比度、可访问性或视觉质量已经通过。

这些 Skills 不会仅为了维护自身状态就创建 `tokens.css`、预览文件或项目记忆文件。
质量验证发生在实现之后，因此构建前预览不会声明尚未执行的分数。

这些 Skills 基于 MIT 许可改编自
[`Nutlope/hallmark`](https://github.com/Nutlope/hallmark) 的
[`13ac0ec`](https://github.com/Nutlope/hallmark/commit/13ac0ec7e148655948100b6396439e481361d690)
提交。详见[第三方声明](./THIRD_PARTY_NOTICES.md)；每个 Hallmark Skill 内也保留了上游许可证。

## 仓库结构

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

## 许可证

[MIT](./LICENSE)
