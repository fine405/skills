---
name: imagegen-glyph-mosaic
description: Analyze visual references and generate new full-color glyph-mosaic, polychrome textmode, typographic-halftone, or painterly ASCII-like raster illustrations while preserving a coherent character grid, dual-scale readability, directional glyph logic, and adjustable palette roles. Use whenever the user asks to study or reproduce an image style made from visible letters, digits, or punctuation; create "彩色字符画", "字符镶嵌", "全彩 ASCII 风景", or textmode artwork; turn several references into a reusable style prompt; or generate multiple new scenes that share that style. Do not use for CLI banners, machine-readable terminal output, or transparent ANSI assets; route those to imagegen-ansi.
---

# ImageGen Glyph Mosaic

Create full-color raster illustrations whose image-forming marks are visible monospaced glyphs. Preserve the two readings that make this medium work: a coherent scene from a distance and an inspectable character grid at close range.

This workflow produces finished raster art. It does not produce executable terminal text or transparent ANSI assets. Keep that boundary explicit so painterly glyph mosaics do not accidentally become terminal screenshots or coarse block logos.

## Workflow

### 1. Classify and inspect the inputs

- Treat supplied images as style references unless the user explicitly asks to edit one of them.
- Label every input by role before generation, for example: `Images 1–4: style references only; do not copy their subjects or geography`.
- Inspect local references with `view_image` when available. Look at both the full composition and enlarged glyph texture.
- Separate observed evidence from inference. Do not attribute an unknown reference to an artist or movement without reliable provenance.
- Decide whether the request needs style analysis, a reusable prompt, generated images, or all three.

### 2. Extract the style system

Describe the references as two groups:

**Stable style DNA**

- one coherent rectangular monospaced grid across the full image;
- every visible surface formed from glyphs rather than text pasted over a normal painting;
- dual-scale readability: scene at a distance, characters at close range;
- glyph density mapped to luminance;
- directional glyphs aligned with edges, slopes, trunks, clouds, or motion;
- a restrained stepped palette, normally 8–12 colors;
- atmospheric depth and a matte printed surface.

**Adjustable variables**

- subject and environment;
- composition, viewpoint, and aspect ratio;
- time, weather, and mood;
- palette family, color temperature, saturation, and accent color;
- glyph density and apparent grid scale;
- strength of paper softness, fading, or print grain.

Keep hue choices out of the stable style DNA. This lets a forest, snow night, sunrise mountain, city, portrait, or still life remain visibly part of the same family.

### 3. Build the prompt

Read `references/prompt-template.md` when shaping a generation prompt. Use only the lines that materially help the request.

Define colors by role rather than by a single mood adjective:

- `atmosphere`: sky, haze, and distant forms;
- `highlight`: illuminated glyphs and paper-like light;
- `midtone_a` and `midtone_b`: local color and material separation;
- `shadow_anchor`: the deepest structural dark;
- `accent`: a small controlled warm or saturated note.

Make the construction rule explicit: the whole scene is built from glyphs on one grid. This prevents the common failure where an otherwise normal image receives a decorative text overlay.

Use punctuation for sparse light and air, directional marks for geometry, vertical glyphs for trunks or columns, and dense glyphs for foliage, rock, or deep shadow. The exact charset may vary; structural behavior matters more than forcing a particular sequence of characters.

### 4. Generate through the available image tool

- Prefer Codex's built-in ImageGen when available and follow the installed `imagegen` skill for reference-image roles, generation semantics, persistence, and fallbacks.
- Use another authorized generator only when it can accept the same prompt constraints and reference roles.
- For distinct scenes, issue one generation call per scene. Do not use a single multi-variation request as a substitute for scene-specific prompts.
- Reuse the same stable style block across a series, but give each image its own scene, composition, lighting, and palette-role block.
- Do not switch model providers, upload private references, or invoke a paid API beyond the user's authority.

### 5. Validate at two scales

Inspect every output and check:

- the subject and composition match the requested scene;
- the image reads clearly when viewed small;
- individual glyphs remain visible at full size;
- one consistent grid covers the scene;
- glyph orientation follows important contours;
- the palette is restrained and the dark anchor remains present;
- distant forms are lower contrast than foreground forms;
- there are no meaningful sentences, large words, logos, signatures, or watermarks.

Correct one failure at a time:

| Failure | Targeted correction |
| --- | --- |
| Ordinary painting with text on top | State that every surface and gradient must be formed from glyph cells; forbid smooth non-glyph regions. |
| Generic pixel art | Require clearly recognizable monospaced letters, digits, and punctuation at close range. |
| Random alphabet soup | Map glyph density to luminance and glyph direction to local geometry. |
| Terminal or cyberpunk look | Forbid terminal UI, green-on-black palettes, scanlines, neon glow, and interface chrome. |
| Palette drift | Restate the 8–12 color limit and assign every hue to a palette role. |
| Weak focal hierarchy | Increase value contrast at the focal subject and compress contrast in distant layers. |

Regenerate only the failed asset and repeat all stable constraints on the correction pass.

### 6. Persist and deliver

- Keep preview-only outputs in the generator-managed location when appropriate.
- Copy project-bound or multi-asset deliverables into the workspace with descriptive, non-overwriting filenames.
- Report the final paths, dimensions, formats, generator used, reference-image roles, and final prompt or concise prompt set.
- Mention any remaining limitation, especially when glyphs are visually convincing but not guaranteed to form a valid plain-text grid.

## Deterministic boundary

Direct image generation is appropriate when visual character texture matters more than exact text encoding. It cannot guarantee a specific charset, perfectly repeatable cell coordinates, or copyable plain-text output.

When the user needs a real terminal banner, executable renderer, transparent ANSI asset, or exact text, use `imagegen-ansi` or a deterministic converter. For high-fidelity full-color production that requires a mathematically exact grid, first create a posterized source image, then map cell luminance, color, and edge direction to glyphs with a dedicated textmode renderer.

## Bundled references and examples

- `references/prompt-template.md`: reusable generation prompt and palette-role system.
- `examples/prompts.md`: the shared style core and scene-specific prompt blocks used for the bundled examples.
- `examples/forest.png`: moss, pine, ochre, and ivory forest study.
- `examples/snow-night.png`: indigo snow scene with a restrained amber focal light.
- `examples/golden-mountain.png`: cool valley and concentrated golden summit at sunrise.
