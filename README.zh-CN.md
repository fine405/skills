# ImageGen Transparent

[English](./README.md) | [**简体中文**](./README.zh-CN.md)

[![skills.sh](https://skills.sh/b/fine405/skills)](https://skills.sh/fine405/skills)

在可控的色键背景上生成图像，在本地移除背景，并交付经过验证的透明 PNG 或 WebP。

## 安装

```bash
npx skills add fine405/skills --skill imagegen-transparent
```

Skill 源码：[`skills/imagegen-transparent`](./skills/imagegen-transparent/)

## 图像生成工具兼容性

**默认实现依赖：** 使用 Codex 内置 ImageGen 生成源图像。ImageGen 是本 Skill 默认使用的第一方适配器，色键抠图流程则独立于具体的图像生成工具。

[`agents/openai.yaml`](./skills/imagegen-transparent/agents/openai.yaml) 提供面向 Codex 的展示元数据和默认调用提示词。其他兼容 Agent 可以忽略此文件，直接使用 `SKILL.md`。

只要满足以下条件，也可以替换为其他本地或远程图像工具：

- 能够遵循经过约束的生成提示词；
- 能够保留参考图像的角色和用途；
- 能够生成完全平坦、颜色一致的色键背景；
- 能够将生成的栅格图像保存到本地路径。

抠图阶段需要 Python 3 和 [Pillow](https://pillow.readthedocs.io/)。本 Skill 会先检查依赖。在明确启用 Auto 或 Full Access 权限时，它只会在作用域最小的环境中安装缺失依赖；在受限或需要先询问的权限模式下，它会说明安装命令并请求批准。

## 工作流程

1. 选择主体中不存在的色键颜色，通常使用 `#00ff00`。
2. 在精确、纯色的色键背景上生成主体，不包含阴影或反射。
3. 采样实际边框颜色并构建柔和的 Alpha 蒙版。
4. 移除色键溢色，并可选择将边缘向内收缩 1 px。
5. 验证 RGBA 模式、四角透明度、主体覆盖率、裁切情况和边缘质量。

## 雪花雪碧图示例

示例需求提供了四种蓝色雕刻风格的雪花作为样式和形状参考。输出需要仅保留雪花，补充其他常见雪晶形态，按照视觉美感排序，并交付一张透明雪碧图。

处理过程：

1. 在 `#00ff00` 背景上生成正好 16 枚钴蓝色雪晶，并严格排列为 4×4 网格。
2. 采样生成图的实际边框颜色（本次为 `#05ef04`），然后使用柔和蒙版和去溢色处理移除背景。
3. 检测到轻微绿色边缘后，将边缘向内收缩 1 px。
4. 将结果扩展为 1256×1256，使 16 个单元格的尺寸均为 314×314 px。
5. 确认输出为 RGBA，并验证四个角完全透明。

提示词摘要：

> 匹配参考图中的钴蓝色雕刻冰晶风格。将其中四种雪花复刻到第一行，增加十二种易于辨认的雪晶形态，按美观程度排序，使用等大的 4×4 单元格，并且不包含邮票、文字、边框、阴影或装饰。

| 生成的色键源图 | 验证后的透明图 |
| --- | --- |
| <img src="./skills/imagegen-transparent/examples/snowflake-sprite-sheet-chroma.png" alt="绿色色键背景上的蓝色雪花雪碧图" width="560"> | <img src="./skills/imagegen-transparent/examples/snowflake-sprite-sheet.png" alt="透明的 4×4 蓝色雪花雪碧图" width="560"> |
| 在纯绿色背景上生成的 1254×1254 RGB 源图 | 1256×1256 RGBA 输出，每个雪碧图单元格为 314×314 |

## 仓库结构

```text
skills/
└── imagegen-transparent/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── scripts/
    │   └── remove_chroma_key.py
    └── examples/
        ├── snowflake-sprite-sheet-chroma.png
        └── snowflake-sprite-sheet.png
```

## 许可证

MIT
