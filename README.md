# Image Skills

[**English**](./README.md) | [简体中文](./README.zh-CN.md)

[![skills.sh](https://skills.sh/b/fine405/skills)](https://skills.sh/fine405/skills)

Reusable image-generation workflows for transparent raster assets and code-ready ANSI terminal art.

## Available skills

| Skill | Purpose | Install |
| --- | --- | --- |
| [`imagegen-transparent`](./skills/imagegen-transparent/) | Generate or extract clean transparent PNG/WebP assets with chroma-key removal, soft alpha matting, despill, and validation. | `npx skills add fine405/skills --skill imagegen-transparent` |
| [`imagegen-ansi`](./skills/imagegen-ansi/) | Convert references or generated raster art into transparent ANSI-style assets, terminal half-block output, and executable JavaScript previews. | `npx skills add fine405/skills --skill imagegen-ansi` |

## ImageGen Transparent

Use Codex ImageGen or a compatible image generator to create a controlled chroma-key source, then remove the background locally and validate the result.

### Workflow

1. Choose a key color absent from the subject, normally `#00ff00`.
2. Generate the subject on an exact, flat key background with no shadows or reflections.
3. Sample the actual border color and build a soft alpha matte.
4. Remove key-color spill and optionally contract the edge by 1 px.
5. Validate RGBA mode, transparent corners, subject coverage, clipping, and edge quality.

### Snowflake sprite-sheet example

The example recreates four supplied snowflake forms, adds twelve common snow-crystal forms, and produces a ranked 4×4 transparent sprite sheet.

| Generated chroma-key source | Validated transparent output |
| --- | --- |
| <img src="./skills/imagegen-transparent/examples/snowflake-sprite-sheet-chroma.png" alt="Blue snowflake sprite sheet on a green chroma-key background" width="560"> | <img src="./skills/imagegen-transparent/examples/snowflake-sprite-sheet.png" alt="Transparent 4 by 4 blue snowflake sprite sheet" width="560"> |
| 1254×1254 RGB source | 1256×1256 RGBA output with 314×314 cells |

## ImageGen ANSI

Use direct alpha conversion when a source already has a clean silhouette. Use ImageGen when the request needs a deliberate terminal-cell reinterpretation, then derive both the raster asset and executable terminal renderer from the same sampled bitmap.

### Workflow

1. Inspect the reference and preserve its silhouette, proportions, spacing, and exact text when present.
2. Generate white terminal-cell geometry on a flat removable key background.
3. Extract and validate a transparent RGBA raster.
4. Sample its alpha channel and pack two vertical pixels into `█`, `▀`, and `▄`.
5. Preview directly in the terminal or emit an executable `.mjs` module.

### Mountain-and-sun example

This example uses an original, generic mountain-and-rising-sun badge with no text or brand identity.

1. Generate a flat reference badge.
2. Reinterpret it as coarse white ANSI cell geometry on `#00ff00`.
3. Sample the generated border (`#03ed0b`), remove it, and validate four transparent corners.
4. Convert the alpha mask to a 48×50 bitmap and 25 terminal rows.
5. Emit both plain ANSI text and an adaptive JavaScript renderer.

Prompt summary:

> Preserve the generic circular badge, two mountain peaks, and rising sun while translating all curves into deliberate terminal-cell steps. Render pure white on a perfectly flat green key background with no text, brand identity, shadows, gradients, or decoration.

<table>
  <thead>
    <tr>
      <th>Original reference</th>
      <th>Generated chroma-key ANSI art</th>
      <th>Validated transparent ANSI art</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="./skills/imagegen-ansi/examples/mountain-sun-reference.png" alt="Generic mountain and rising sun badge reference" width="300"></td>
      <td><img src="./skills/imagegen-ansi/examples/mountain-sun-ansi-chroma.png" alt="White ANSI mountain and sun badge on a green chroma-key background" width="300"></td>
      <td bgcolor="#0d1117"><img src="./skills/imagegen-ansi/examples/mountain-sun-ansi.png" alt="Transparent white ANSI mountain and sun badge" width="300"></td>
    </tr>
  </tbody>
</table>

Run the code-generated terminal preview:

```bash
node ./skills/imagegen-ansi/examples/mountain-sun-ansi.mjs
```

The corresponding plain-text output is available at [`mountain-sun-ansi.txt`](./skills/imagegen-ansi/examples/mountain-sun-ansi.txt).

## Compatibility and requirements

- Codex's built-in ImageGen is the default generator; another authorized generator may be used when it can produce a uniformly keyed local raster.
- Extraction and ANSI conversion require Python 3 and [Pillow](https://pillow.readthedocs.io/).
- [`agents/openai.yaml`](./skills/imagegen-ansi/agents/openai.yaml) and [`agents/openai.yaml`](./skills/imagegen-transparent/agents/openai.yaml) provide Codex-facing display metadata.

## Repository structure

```text
skills/
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
└── imagegen-transparent/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── scripts/remove_chroma_key.py
    └── examples/
        ├── snowflake-sprite-sheet-chroma.png
        └── snowflake-sprite-sheet.png
```

## License

MIT
