---
name: imagegen-ansi
description: Convert reference images, wordmarks, icons, or generated raster art into transparent ANSI-style assets and code-ready terminal previews using ImageGen when stylistic reinterpretation is needed, deterministic chroma-key extraction, alpha validation, bitmap sampling, and Unicode half-block rendering. Use when the user asks for ANSI art, ASCII-style image conversion, terminal banners, CLI logos, white-on-transparent pixel lettering, code-reproducible terminal graphics, "转 ANSI 图片", "终端字符画", or "CLI 启动图".
---

# ImageGen ANSI

Create a transparent raster reference and a deterministic terminal rendering from the same sampled bitmap. Keep machine-readable CLI output separate from decorative help or interactive UI.

## Workflow

### 1. Classify the input

- Treat a supplied image as a reference unless the user explicitly asks to edit it.
- Inspect every local input with `view_image` when available.
- Use direct deterministic conversion when the source already has a clean, high-contrast silhouette. This preserves typography and spelling better than regeneration.
- Use ImageGen when the user wants a stylistic ANSI reinterpretation, coarse terminal-cell geometry, or cleanup that direct thresholding cannot provide.
- Decide whether the deliverables include the transparent PNG, ANSI text, embeddable source code, or all three.

Never include a user's brand asset, wordmark, prompt, or generated output as a reusable example in this skill.

### 2. Check dependencies

Resolve `<skill-root>` as the folder containing this `SKILL.md`.

```bash
command -v python3
python3 "<skill-root>/scripts/remove_chroma_key.py" --check
python3 "<skill-root>/scripts/raster_to_ansi.py" --check
```

Both helpers require Python 3 and Pillow. Prefer the active project environment:

```bash
uv pip install pillow
```

If `uv` is unavailable:

```bash
python3 -m pip install pillow
```

Follow the current permission policy before installing. Install only the missing dependency and avoid changing a global environment when a project environment exists.

### 3. Prepare the transparent ANSI-style raster

For direct conversion, use the supplied transparent image and continue to step 5. If it has a flat background, extract it in step 4.

For stylistic conversion, follow the installed `imagegen` skill and label the source as a reference image. Preserve exact text, capitalization, silhouette, proportions, spacing, and baseline when the source is a wordmark.

Use a prompt shaped like this neutral example:

```text
Use case: stylized-concept
Asset type: transparent ANSI terminal graphic and code reconstruction reference
Primary request: reinterpret the generic mountain-and-sun badge from Image 1 as crisp terminal block art
Input images: Image 1: silhouette and proportion reference
Style/medium: monochrome ANSI art made only from a regular grid of solid rectangular cells
Composition/framing: centered with safe padding; deliberate stepped geometry
Color palette: pure white #ffffff subject on flat #00ff00
Constraints: preserve the recognizable mountain and sun silhouette; no text; no blur; no shadows; no reflections; no watermark
```

Add these extraction constraints:

```text
Create the subject on a perfectly flat solid <KEY_COLOR> chroma-key background.
Use one exact background color with no gradient, texture, shadow, glow, reflection, or lighting variation.
Keep the subject separated from every canvas edge with crisp edges and generous padding.
Do not use <KEY_COLOR> inside the subject.
```

Use `#00ff00` by default and `#ff00ff` when green appears in the subject. Reject outputs with clipped parts, spelling drift, nonuniform backgrounds, or unwanted decoration.

### 4. Extract and validate transparency

Copy the generated source into the workspace or a task-specific temporary directory, then run:

```bash
python3 "<skill-root>/scripts/remove_chroma_key.py" \
  --input <chroma-source.png> \
  --out <transparent.png> \
  --auto-key border \
  --despill
```

Inspect the result and confirm RGBA mode, transparent corners, plausible visible coverage, intact interior holes, and no key-colored fringe. Retry once with `--edge-contract 1` only when a thin fringe remains.

Do not switch to model-native transparency or another paid API without the user's authority. Chroma keying is unsuitable for hair, fur, smoke, glass, liquids, translucency, reflections, and soft shadows.

### 5. Compare with the reference

Before generating code, compare the transparent ANSI raster with the source:

- exact spelling and capitalization for text;
- normalized subject width-to-height ratio;
- baseline, letter spacing, negative space, and stroke coverage;
- recognizable outer silhouette and intentional terminal-cell stepping;
- appearance on both light and dark backgrounds.

Make only one targeted regeneration change at a time. Prefer the closer faithful version over a more decorative result.

### 6. Create and run the ANSI preview

The converter crops transparent padding for sampling and packs two vertical pixels into each terminal row with `█`, `▀`, and `▄`.

Preview directly in bright white on the terminal's existing background:

```bash
python3 "<skill-root>/scripts/raster_to_ansi.py" \
  --input <transparent.png> \
  --width 96 \
  --format ansi
```

Generate an embeddable, executable JavaScript module:

```bash
python3 "<skill-root>/scripts/raster_to_ansi.py" \
  --input <transparent.png> \
  --width 96 \
  --format js \
  --out <preview.mjs>

node <preview.mjs>
```

Use `--format plain` for uncolored terminal text. Adjust `--width` once if the preview wraps or loses important detail; do not repeatedly tune thresholds without evidence.

### 7. Integrate safely

- Put decorative ANSI art only in human-facing help, splash, or interactive UI.
- Keep JSON, shell completion, and other machine-readable output free of banners and escape sequences.
- Emit color only for a TTY and respect `NO_COLOR`.
- Reset ANSI state after the graphic.
- Keep the transparent raster as the visual source of truth and the sampled bitmap as the code source of truth.

### 8. Deliver

Report the transparent asset path, dimensions, alpha validation result, preview/code path, launch command, generator used, and final prompt summary. State whether the current CLI UI was changed.

## Helper reference

- `scripts/remove_chroma_key.py`: sample a key background, build a soft alpha matte, despill edges, and validate transparency.
- `scripts/raster_to_ansi.py`: validate an RGBA asset, sample its alpha channel, render half-block ANSI text, or emit an executable JavaScript module.

## Bundled example

Inspect `examples/` for a complete, copyright-safe mountain-and-sun conversion:

- `mountain-sun-reference.png`: original generic reference image.
- `mountain-sun-ansi-chroma.png`: ImageGen output on a removable key background.
- `mountain-sun-ansi.png`: validated transparent ANSI-style raster.
- `mountain-sun-ansi.txt`: deterministic half-block terminal output.
- `mountain-sun-ansi.mjs`: executable and embeddable JavaScript renderer.

Run the example with:

```bash
node "<skill-root>/examples/mountain-sun-ansi.mjs"
```
