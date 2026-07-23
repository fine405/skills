# ImageGen Transparent

[**English**](./README.md) | [简体中文](./README.zh-CN.md)

[![skills.sh](https://skills.sh/b/fine405/skills)](https://skills.sh/fine405/skills)

Generate an image on a controlled chroma-key background, remove that background locally, and deliver a validated transparent PNG or WebP.

## Install

### ImageGen Transparent

```bash
npx skills add fine405/skills --skill imagegen-transparent
```

Skill source: [`skills/imagegen-transparent`](./skills/imagegen-transparent/)

### ImageGen ANSI

Convert a reference image or generated raster into transparent ANSI-style art, terminal half-block output, and an executable JavaScript preview.

```bash
npx skills add fine405/skills --skill imagegen-ansi
```

Skill source: [`skills/imagegen-ansi`](./skills/imagegen-ansi/)

## Image generator compatibility

**Default implementation dependency:** Codex's built-in ImageGen supplies the generated source image. ImageGen is the first-party adapter used by this skill, while the chroma-key extraction pipeline remains independent of the generator.

[`agents/openai.yaml`](./skills/imagegen-transparent/agents/openai.yaml) provides Codex-facing display metadata and a default invocation prompt. Other compatible agents can ignore this file and use `SKILL.md` directly.

Another local or remote image tool can be substituted when it can:

- follow the shaped generation prompt;
- preserve reference-image roles;
- produce a perfectly flat chroma-key background;
- save the generated raster image to a local path.

The extraction stage requires Python 3 and [Pillow](https://pillow.readthedocs.io/). The skill checks dependencies first. Under explicit Auto or Full Access permissions it installs only missing dependencies into the least-scoped environment; under restricted or ask-first permissions it explains the command and requests approval.

## Workflow

1. Choose a key color absent from the subject, normally `#00ff00`.
2. Generate the subject on an exact, flat key background with no shadows or reflections.
3. Sample the actual border color and build a soft alpha matte.
4. Remove key-color spill and optionally contract the edge by 1 px.
5. Validate RGBA mode, transparent corners, subject coverage, clipping, and edge quality.

## Snowflake sprite-sheet example

The example request supplied four blue engraved snowflake designs as a style-and-shape reference. The output needed to keep only the snowflakes, add other common snow-crystal forms, rank them by visual appeal, and deliver one transparent sprite sheet.

Process:

1. Generate exactly 16 cobalt-blue crystals in a strict 4×4 layout on `#00ff00`.
2. Sample the generated border color (`#05ef04` in this run), then remove it using a soft matte and despill.
3. Apply a 1 px edge contraction after detecting a faint green fringe.
4. Pad the result to 1256×1256, giving 16 cells of 314×314 px.
5. Confirm RGBA output and four fully transparent corners.

Prompt summary:

> Match the reference's cobalt-blue engraved ice-crystal style. Recreate its four snowflakes as the first row, add twelve recognizable snow-crystal forms, rank them by beauty, use equal 4×4 cells, and include no stamps, text, borders, shadows, or decoration.

| Generated chroma-key source | Validated transparent output |
| --- | --- |
| <img src="./skills/imagegen-transparent/examples/snowflake-sprite-sheet-chroma.png" alt="Blue snowflake sprite sheet on a green chroma-key background" width="560"> | <img src="./skills/imagegen-transparent/examples/snowflake-sprite-sheet.png" alt="Transparent 4 by 4 blue snowflake sprite sheet" width="560"> |
| 1254×1254 RGB source generated on a flat green background | 1256×1256 RGBA output with 314×314 sprite cells |

## Repository structure

```text
skills/
├── imagegen-ansi/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── scripts/
│       ├── raster_to_ansi.py
│       └── remove_chroma_key.py
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

## License

MIT
