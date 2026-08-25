---
name: imagegen-transparent
description: Generate or edit raster images with Codex ImageGen or a compatible image generator, then deliver clean transparent PNG or WebP assets by using a removable chroma-key background, local soft-matte extraction, despill, edge cleanup, and alpha validation. Use when the user asks to "generate a transparent image", "remove the background from an ImageGen result", "make a transparent PNG", "create transparent sprites", "生成透明底图片", "抠成透明背景", or combine image generation with background removal.
---

# ImageGen Transparent

Create transparent raster assets with Codex's built-in ImageGen tool by default, then remove a deliberately flat chroma-key background with the bundled deterministic helper.

Treat Codex ImageGen as the default adapter, not as a hard dependency of the extraction pipeline. Adapt another local or remote image tool when it can produce the same flat chroma-key source image and the user has authorized its use.

Prefer this workflow for opaque illustrations, icons, sprites, product-like cutouts, and other subjects with crisp boundaries. Avoid chroma keying for hair, fur, feathers, smoke, liquids, glass, realistic translucency, reflections, or soft shadows; those cases need model-native transparency or dedicated alpha matting.

## Workflow

### 1. Classify the request

- Treat a supplied image as an edit target only when the user asks to preserve and change it.
- Treat supplied images as references when they provide style, composition, or subject guidance.
- Load local reference or edit-target images with `view_image` when the active agent provides it.
- Decide whether the asset is preview-only or project-bound. Save project-bound outputs inside the workspace.

### 2. Select the image generator

- Prefer Codex's built-in ImageGen tool when available. Follow the current installed `imagegen` skill for generation and edit semantics.
- Use another local or remote image tool when ImageGen is unavailable or the user requests an alternative. Require the tool to accept the shaped prompt, preserve reference-image roles, produce a uniformly keyed raster image, and expose the output as a local file.
- Translate the prompt to the alternative tool without weakening the flat-background, padding, no-shadow, and no-key-color-in-subject constraints.
- Do not install a generator, invoke a paid API, upload private references, or switch model providers beyond the authority granted by the user and the current permission policy.
- Keep the extraction and validation steps unchanged regardless of the generator.

### 3. Check local dependencies

Resolve `<skill-root>` as the directory containing this `SKILL.md`; do not assume an agent-specific installation directory. Check the local runtime before generating:

```bash
command -v python3
python3 "<skill-root>/scripts/remove_chroma_key.py" --check
```

If `python3` is missing, select the install command appropriate to the detected platform:

```bash
# macOS with Homebrew
brew install python

# Debian or Ubuntu
sudo apt install python3 python3-venv

# Windows PowerShell
winget install Python.Python.3.12
```

If Pillow is missing, prefer installing it in the active project environment with:

```bash
uv pip install pillow
```

When `uv` is unavailable, offer:

```bash
python3 -m pip install pillow
```

Apply the current permission policy before installing:

- Under an explicit Auto, Full Access, or equivalent unattended permission mode, install automatically with the least-scoped available option, report what is being changed, rerun `--check`, and continue.
- Under a manual, restricted, ask-first, or ambiguous permission mode, explain what is missing, name the target environment and exact command, ask for approval, and wait for confirmation.
- When the environment blocks installation and cannot request elevation, give the user the exact command to run locally and stop until installation is confirmed.
- Prefer an active project virtual environment. Avoid modifying global Python when a project environment exists.
- Install only the missing dependency. Do not upgrade unrelated packages.
- Never use `sudo`, create a new global environment, or change the system package manager beyond the authority explicitly granted by the current permission mode.

After installation, rerun the same `--check` command and require a successful result before generation. Do not ask for an API key when using the built-in ImageGen tool.

### 4. Choose the key color

- Use `#00ff00` by default.
- Use `#ff00ff` for green subjects.
- Avoid any key color present in the subject.
- Never use blue as the key for blue, icy, watery, or cool-toned subjects.

When all practical key colors conflict with the subject, stop and explain that chroma-key extraction is unsafe. Consult the current installed `imagegen` skill before offering a model-native transparency fallback; request user confirmation before changing model or API path.

### 5. Generate the removable-background source

Use the selected image generator. Add these constraints to the shaped prompt:

```text
Create the subject on a perfectly flat solid <KEY_COLOR> chroma-key background for background removal.
The background must be one exact uniform color with no shadows, gradients, texture, reflections, floor plane, glow, or lighting variation.
Keep the subject fully separated from the background with crisp edges and generous padding.
Do not use <KEY_COLOR> anywhere in the subject.
No cast shadow, contact shadow, reflection, watermark, signature, or extra decoration.
```

Preserve all user constraints. For edits, repeat the invariants explicitly. For sprite sheets, require equal cells, consistent scale, generous padding, no overlap, and canvas dimensions divisible by the row and column counts.

After generation, inspect the source. Reject and regenerate when the background is not visually uniform, the subject touches an edge, required parts are clipped, or shadows contaminate the background.

### 6. Persist and extract

When using Codex ImageGen, copy the selected generated source from `$CODEX_HOME/generated_images/...` into the workspace or a task-specific temporary directory. When using another generator, resolve its local output path. Never leave a project-referenced asset only in a tool-managed cache.

Run the helper with border key sampling, soft matte, and despill:

```bash
python3 "<skill-root>/scripts/remove_chroma_key.py" \
  --input <source.png> \
  --out <transparent.png> \
  --auto-key border \
  --despill
```

Do not overwrite an existing user asset. Choose a versioned filename unless replacement was explicitly requested.

### 7. Validate the alpha result

Inspect the transparent output with `view_image` and confirm:

- The file is RGBA PNG or WebP.
- All four corner alpha values are zero.
- The visible subject coverage is plausible.
- No part is clipped or unintentionally erased.
- No key-colored fringe is visible on both light and dark backgrounds.
- Fine branches, holes, and antialiased edges remain intact.

The helper prints size, alpha counts, corner alpha, and visible coverage. Treat nonzero corner alpha or zero visible coverage as failure.

If a thin key-colored fringe remains, retry once with:

```bash
python3 "<skill-root>/scripts/remove_chroma_key.py" \
  --input <source.png> \
  --out <transparent-v2.png> \
  --auto-key border \
  --despill \
  --edge-contract 1
```

Use `--edge-feather 0.25` only for visibly stair-stepped opaque edges. Avoid feathering shiny or reflective subjects.

If extraction damages the subject, regenerate with a cleaner key background or stop and recommend native transparency or alpha matting. Do not keep increasing tolerances blindly.

### 8. Deliver

Keep only requested deliverables unless intermediates are useful to the user. Report:

- The final absolute path.
- Dimensions and format.
- Whether transparency validation passed.
- The final generation prompt or a concise prompt summary.
- The image generator used and that local chroma-key extraction was applied.

## Helper reference

Run `scripts/remove_chroma_key.py --help` for all options. The helper requires Python 3 and Pillow, performs automatic border or corner key sampling, creates a soft alpha matte, removes key-color spill, supports edge contraction and feathering, and refuses to overwrite files without `--force`.
