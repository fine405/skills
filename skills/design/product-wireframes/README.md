# 产品线框稿

把产品需求变成可点击、可播放的二维线框。内容用骨架占位，重点说明页面关系、操作结果和动效。

## 安装到 Codex

通过公开仓库安装：

```bash
npx skills add fine405/skills --skill product-wireframes
```

也可以手动安装分享包：

1. 解压分享包，得到 `product-wireframes` 文件夹。
2. 把整个文件夹放进 `~/.codex/skills/`。
3. 如果设置了 `CODEX_HOME`，改放到该目录的 `skills/` 下。
4. 新建聊天，输入 `$product-wireframes` 调用。

若技能列表尚未刷新，重新打开 Codex。保持文件夹结构完整；入口应为 `product-wireframes/SKILL.md`。

## 直接这样说

```text
请用 $product-wireframes，把下面的需求做成可交互的手机线框。
内容用骨架占位，保留必要操作标签，演示主要交互和动效。
交付独立 HTML 和少量关键图，保持首版范围。

需求：粘贴 PRD、页面说明，或附上已有文件。
```

也可以要求桌面线框、只画某条流程，或修改已有 HTML。无需自己写代码。明确的页面、交互和范围能减少反复；没有完整 PRD 也可以从需求描述开始。

## 会得到什么

- 一个可用浏览器直接打开的 HTML，内含示例数据。
- 需要时附少量关键截图，方便放进 PRD。
- 简短的已覆盖流程、验证结果与限制说明。

随包的 `assets/wireframe-starter.html` 可直接打开，查看基本交互。它是通用示例，实际交付会按需求删改。

## 飞书可选

默认只交付本地文件，不需要飞书账号。需要合并时，再说明“把结果放到这份飞书 PRD”，并提供目标链接。

飞书写入使用你自己的连接和授权。没有接入也能正常绘制；HTML 文件可以直接分享给同事，本机预览链接不能代替文件。

## 灵感与实现

本 skill 受 [Hairline](https://hairline.lucasmarkes.com/) 及其 [skills 工作流](https://hairline.lucasmarkes.com/skills) 启发，借鉴细线表达、交互反馈、浏览器检查和单文件交付的方法。

这里采用适合产品评审的二维页面、骨架内容和页面状态管理。流程说明与 HTML 模板为独立编写，未使用 Hairline 的绘图引擎，也不需要安装 Hairline。
