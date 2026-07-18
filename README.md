# ImageGen Transparent

[![skills.sh](https://skills.sh/b/fine405/skills)](https://skills.sh/fine405/skills)

Generate an image on a controlled chroma-key background, remove that background locally, and deliver a validated transparent PNG or WebP.

## Install

```bash
npx skills add fine405/skills --skill imagegen-transparent
```

Skill source: [`skills/imagegen-transparent`](./skills/imagegen-transparent/)

## Image generator compatibility

The skill uses **Codex's built-in ImageGen by default**. ImageGen is the default adapter, not a hard dependency of the transparency pipeline.

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
2. Remove the sampled background using a soft matte and despill.
3. Apply a 1 px edge contraction after detecting a faint green fringe.
4. Pad the result to 1256×1256, giving 16 cells of 314×314 px.
5. Confirm RGBA output and four fully transparent corners.

Prompt summary:

> Match the reference's cobalt-blue engraved ice-crystal style. Recreate its four snowflakes as the first row, add twelve recognizable snow-crystal forms, rank them by beauty, use equal 4×4 cells, and include no stamps, text, borders, shadows, or decoration.

<p align="center">
  <img src="./skills/imagegen-transparent/examples/snowflake-sprite-sheet.png" alt="Transparent 4 by 4 blue snowflake sprite sheet" width="760">
</p>

## Repository structure

```text
skills/
└── imagegen-transparent/
    ├── SKILL.md
    ├── scripts/
    │   └── remove_chroma_key.py
    └── examples/
        └── snowflake-sprite-sheet.png
```

## License

MIT
