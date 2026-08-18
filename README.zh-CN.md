# App 图标与图像 Skills

[English](./README.md) | [**简体中文**](./README.zh-CN.md)

[![skills.sh](https://skills.sh/b/fine405/skills)](https://skills.sh/fine405/skills)

以模块化 App 图标系统为核心的创意生产 Skills，同时提供透明栅格素材、可用代码复刻的 ANSI 终端字符画，以及具有绘画感的全彩字符镶嵌图工作流。

## 可用 Skills

| Skill | 用途 | 安装 |
| --- | --- | --- |
| [`app-icon-design`](./skills/app-icon-design/) | 编排统一的 App 图标身份、可选主题、视觉风格，以及 Apple、Android、Web/PWA、Windows 等目标平台。 | `npx skills add fine405/skills --skill app-icon-design` |
| [`app-icon-theme`](./skills/app-icon-theme/) | 在保留现有图标身份的前提下创建连贯的主题化变体，并保持主题与风格、平台相互独立。 | `npx skills add fine405/skills --skill app-icon-theme` |
| [`imagegen-transparent`](./skills/imagegen-transparent/) | 使用色键移除、柔和 Alpha 蒙版、去溢色和结果校验，生成或提取干净的透明 PNG/WebP。 | `npx skills add fine405/skills --skill imagegen-transparent` |
| [`imagegen-ansi`](./skills/imagegen-ansi/) | 将参考图或生成的栅格图转换为透明 ANSI 风格素材、终端半块字符输出和可执行 JavaScript 预览。 | `npx skills add fine405/skills --skill imagegen-ansi` |
| [`imagegen-glyph-mosaic`](./skills/imagegen-glyph-mosaic/) | 分析视觉参考，并使用统一字符网格、方向性 glyph 与可调色彩角色生成全彩字符镶嵌插画。 | `npx skills add fine405/skills --skill imagegen-glyph-mosaic` |

## App 图标系统

App 图标 Skills 将稳定的产品身份与语义主题、视觉风格、平台生产规范分开处理：

```text
身份 → 可选 theme-* → 可选 style-* → platform-* → 最终验收
```

### App Icon Design

使用 `app-icon-design` 作为总编排入口。先建立统一、可识别的产品身份，再针对不同目标平台分别适配，避免将平台规范混入主题或风格规则。

#### 工作流程

1. 将应用提炼为受众、核心任务、价值承诺、品类信号与差异点。
2. 锁定身份不变量：隐喻、轮廓、比例、品牌色角色与一个标志性细节。
3. 仅加载所需的 Apple、Android、Web/PWA 或 Windows 平台模块。
4. 使用 `app-icon-theme` 解析可选语义主题，再应用已安装的风格模块或任务级风格简报。
5. 生成或编辑图像，测试目标遮罩与小尺寸效果，并如实说明尚未完成的封装步骤。

内置风格包括柔和轻拟物、迪斯科拟态与 Jelly 3D，后续视觉方向继续使用独立的 `style-*.md` 模块。

### App Icon Theme

使用 `app-icon-theme` 通过音乐类型、季节、情绪、活动、运动、职业或内容分类重新解释用户拥有的图标，同时保留源图标身份。

#### 工作流程

1. 锁定源图标的轮廓、内部留白、比例、构图与品牌色角色。
2. 选择一个主要语义线索，以及材质替换、结构类比或受控配饰之一。
3. 设置克制、平衡或强表达级别；默认使用平衡级别。
4. 独立应用所选渲染风格，并在小尺寸下检查身份与主题辨识度。

首个内置主题族为 `theme-music-genre.md`，后续主题族继续使用独立的 `theme-*.md` 模块。

## ImageGen Transparent

使用 Codex ImageGen 或兼容的图像生成工具创建可控的色键源图，再在本地移除背景并校验结果。

### 工作流程

1. 选择主体中不存在的色键颜色，通常使用 `#00ff00`。
2. 在精确、平坦的色键背景上生成主体，不包含阴影或反射。
3. 采样实际边框颜色并构建柔和的 Alpha 蒙版。
4. 移除色键溢色，并可选择将边缘向内收缩 1 px。
5. 验证 RGBA 模式、四角透明度、主体覆盖率、裁切情况和边缘质量。

### 雪花雪碧图示例

示例复刻了提供的四种雪花形态，补充十二种常见雪晶，并生成按照视觉效果排序的 4×4 透明雪碧图。

| 生成的色键源图 | 验证后的透明图 |
| --- | --- |
| <img src="./skills/imagegen-transparent/examples/snowflake-sprite-sheet-chroma.png" alt="绿色色键背景上的蓝色雪花雪碧图" width="560"> | <img src="./skills/imagegen-transparent/examples/snowflake-sprite-sheet.png" alt="透明的 4×4 蓝色雪花雪碧图" width="560"> |
| 1254×1254 RGB 源图 | 1256×1256 RGBA 输出，每个单元格为 314×314 |

## ImageGen ANSI

如果源图已经具有干净轮廓，优先直接转换 Alpha；如果需要明确的终端单元格再设计，则使用 ImageGen。透明图片和可执行终端渲染器都由同一份采样点阵派生。

### 工作流程

1. 检查参考图；保留轮廓、比例、间距，以及文字存在时的准确拼写。
2. 在可移除的纯色色键背景上生成白色终端单元格几何。
3. 提取并校验透明 RGBA 栅格图。
4. 采样 Alpha 通道，并使用 `█`、`▀` 和 `▄` 将两个垂直像素压缩到一行终端字符。
5. 在终端直接预览，或生成可执行的 `.mjs` 模块。

### 山峰与日出示例

这个示例使用完全原创、没有文字和品牌身份的通用“山峰与日出”徽章。

1. 生成平面参考徽章。
2. 将其重新解释为 `#00ff00` 背景上的粗粒度白色 ANSI 单元格几何。
3. 采样生成后的边框颜色（`#03ed0b`），移除背景并确认四角完全透明。
4. 将 Alpha 蒙版转换为 48×50 点阵和 25 行终端输出。
5. 同时生成纯字符画和能够自适应终端宽度的 JavaScript 渲染器。

提示词摘要：

> 保留通用圆形徽章、两座山峰和升起的太阳，将所有曲线转换为明确的终端单元格阶梯。主体使用纯白色，背景使用完全平坦的绿色色键；不包含文字、品牌身份、阴影、渐变或额外装饰。

<table>
  <thead>
    <tr>
      <th>原创参考图</th>
      <th>生成的 ANSI 色键图</th>
      <th>验证后的透明 ANSI 图</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="./skills/imagegen-ansi/examples/mountain-sun-reference.png" alt="通用山峰与日出徽章参考图" width="300"></td>
      <td><img src="./skills/imagegen-ansi/examples/mountain-sun-ansi-chroma.png" alt="绿色色键背景上的白色 ANSI 山峰与日出徽章" width="300"></td>
      <td bgcolor="#0d1117"><img src="./skills/imagegen-ansi/examples/mountain-sun-ansi.png" alt="透明的白色 ANSI 山峰与日出徽章" width="300"></td>
    </tr>
  </tbody>
</table>

运行代码生成的终端预览：

```bash
node ./skills/imagegen-ansi/examples/mountain-sun-ansi.mjs
```

对应的纯文本输出位于 [`mountain-sun-ansi.txt`](./skills/imagegen-ansi/examples/mountain-sun-ansi.txt)。

## ImageGen Glyph Mosaic

从风格参考中分离稳定的视觉 DNA 与可调的主体、构图和色调参数，再生成由可见等宽字符构成、同时具有绘画感的栅格场景。

### 工作流程

1. 明确输入图片是风格参考还是编辑目标。
2. 提取稳定的网格、双尺度可读性、方向性字符规则、受限调色板与印刷表面。
3. 保持主体、构图、天气和色彩角色可调整。
4. 复用同一个风格核，为每个不同场景单独生成提示词和图片。
5. 同时用缩略图和原尺寸检查场景识别度与字符网格质量。

### 全彩字符镶嵌示例

三张示例共享同一个风格核，并分别使用独立的构图和色彩角色配置。它们均为本 Skill 生成的原创结果。

| 森林 | 雪夜 | 日照金山 |
| --- | --- | --- |
| <img src="./skills/imagegen-glyph-mosaic/examples/forest.png" alt="使用全彩字符镶嵌方式表现的原始森林" width="360"> | <img src="./skills/imagegen-glyph-mosaic/examples/snow-night.png" alt="使用全彩字符镶嵌方式表现的月光雪谷与木屋" width="360"> | <img src="./skills/imagegen-glyph-mosaic/examples/golden-mountain.png" alt="使用全彩字符镶嵌方式表现的日照金山" width="360"> |
| 苔藓绿、灰青、赭石与象牙白 | 靛蓝、冰灰蓝、乳白与克制琥珀色 | 雾蓝、冰川白、暖金与深棕 |

可复用模板位于 [`references/prompt-template.md`](./skills/imagegen-glyph-mosaic/references/prompt-template.md)，示例场景提示词位于 [`examples/prompts.md`](./skills/imagegen-glyph-mosaic/examples/prompts.md)。

## 兼容性与依赖

- 默认使用 Codex 内置 ImageGen；经过授权的其他生成工具只要能够保留当前 Skill 的提示词约束、参考图角色和本地输出流程，也可以接入。
- 色键背景提取与 ANSI 转换需要 Python 3 和 [Pillow](https://pillow.readthedocs.io/)；字符镶嵌图生成不需要额外的本地运行依赖。
- App 图标概念设计不需要额外的本地运行依赖；生产交付前必须核对各目标平台当前的官方规范。
- 每个 Skill 都包含 `agents/openai.yaml`，用于提供面向 Codex 的展示元数据。

## 仓库结构

```text
skills/
├── app-icon-design/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── platform-android.md
│       ├── platform-apple.md
│       ├── platform-web.md
│       ├── platform-windows.md
│       ├── module-style-template.md
│       ├── style-discomorphism.md
│       ├── style-jelly-3d.md
│       └── style-soft-neumorphic.md
├── app-icon-theme/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── module-theme-template.md
│       └── theme-music-genre.md
├── imagegen-ansi/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── scripts/
│   │   ├── raster_to_ansi.py
│   │   └── remove_chroma_key.py
│   └── examples/
│       ├── mountain-sun-reference.png
│       ├── mountain-sun-ansi-chroma.png
│       ├── mountain-sun-ansi.png
│       ├── mountain-sun-ansi.txt
│       └── mountain-sun-ansi.mjs
├── imagegen-glyph-mosaic/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/prompt-template.md
│   └── examples/
│       ├── prompts.md
│       ├── forest.png
│       ├── snow-night.png
│       └── golden-mountain.png
└── imagegen-transparent/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── scripts/remove_chroma_key.py
    └── examples/
        ├── snowflake-sprite-sheet-chroma.png
        └── snowflake-sprite-sheet.png
```

## 许可证

MIT
