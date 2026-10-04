# Fine 的 Agent Skills

[English](./README.md) | [**简体中文**](./README.zh-CN.md)

[![skills.sh](https://skills.sh/b/fine405/skills)](https://skills.sh/fine405/skills)

一个面向创意生产、界面设计、工程协作与可视化讲解的 Agent Skills
合集。此仓库统一了原来的 `fine405/skills` 与 `fine405/dev-skills`，同时保持每个
Skill 都可独立安装。

## Skills

### AIGC

| Skill | 用途 |
| --- | --- |
| [`app-icon-design`](./skills/aigc/app-icon-design/) | 编排统一的 App 图标身份、主题、视觉风格、目标平台与生产验收。 |
| [`app-icon-theme`](./skills/aigc/app-icon-theme/) | 在保留现有图标身份的前提下创建连贯的主题化变体。 |
| [`imagegen-ansi`](./skills/aigc/imagegen-ansi/) | 将参考图或栅格图转换为透明 ANSI 风格素材与可复现的终端预览。 |
| [`imagegen-glyph-mosaic`](./skills/aigc/imagegen-glyph-mosaic/) | 使用统一字符网格与色彩逻辑生成全彩字符镶嵌插画。 |
| [`imagegen-transparent`](./skills/aigc/imagegen-transparent/) | 通过色键移除、Alpha 清理与校验生成或提取透明素材。 |

### 设计

| Skill | 用途 |
| --- | --- |
| [`design-direction`](./skills/design/design-direction/) | 探索鲜明的设计方向，通过独立截图评审迭代，以界面减法与文案打磨完成交付。 |
| [`hallmark-study`](./skills/design/hallmark-study/) | 从截图或公开 URL 提取可复用的设计 DNA，同时避免复制受保护内容。 |
| [`hallmark-build`](./skills/design/hallmark-build/) | 在保留现有产品系统的前提下设计并实现有辨识度的 Web UI。 |
| [`hallmark-audit`](./skills/design/hallmark-audit/) | 从代码与渲染证据审计层级、可访问性、响应式、可信度和实现风险。 |

Hallmark 工作流被有意拆分为三个需要明确调用的 Skill：

```text
hallmark-study  → 提取抽象设计 DNA
hallmark-build  → 基于产品系统实施
hallmark-audit  → 结合代码与渲染证据审计，不修改文件
```

### 工程

| Skill | 用途 |
| --- | --- |
| [`open-source-contribution`](./skills/engineering/open-source-contribution/) | 通过检查仓库规约、关联工作、验证门槛、归因与 CI，准备合规的上游贡献。 |

### 效率

| Skill | 用途 |
| --- | --- |
| [`eli5`](./skills/productivity/eli5/) | 将主题制作成面向零基础读者、图片优先的独立 HTML 图解。 |
| [`write-explain`](./skills/productivity/write-explain/) | 按意图自动写作，手动触发解释；遵循中文写作与排版约束，交付后按收益建议 HTML 或字幕视频，由用户决定是否制作。 |

## 安装

查看所有可用 Skills：

```bash
npx skills add fine405/skills --list
```

安装单个 Skill：

```bash
npx skills add fine405/skills --skill app-icon-design
```

安装全部 Skills：

```bash
npx skills add fine405/skills --skill '*'
```

`skills` CLI 会递归发现 Skill，因此分类目录不会改变安装后的 Skill 名称。

原 `fine405/dev-skills` 用户只需将包来源替换为 `fine405/skills`；原来的五个开发类
Skill 名称均保持不变。

## 仓库结构

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

每个 Skill 都包含 `SKILL.md` 与面向 Codex 的 `agents/openai.yaml`。可选的
`references/`、`scripts/`、`examples/` 与 `assets/` 保留在 Skill 内部，确保目录
被单独安装时仍然完整。少量工具脚本会在可独立安装的 Skills 之间有意复制；仓库校验会
阻止这些副本产生漂移。

## 校验

运行与 CI 相同的检查：

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
python3 -m compileall -q skills scripts tests
```

校验器会检查分类结构、frontmatter、名称唯一性、Agent 元数据、中英文索引覆盖率、
本地 Markdown 链接，以及共享工具副本是否同步。

## 归因与许可证

Hallmark Skills 基于 MIT 许可改编自
[`Nutlope/hallmark`](https://github.com/Nutlope/hallmark)。`eli5` 的灵感来自
Anthropic 社区的
[`eli5`](https://github.com/anthropics/claude-plugins-community/tree/main/eli5)
插件，并针对 Codex Skills 重新编写。详见
[`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md)。

原创内容使用 [MIT 许可证](./LICENSE)。
