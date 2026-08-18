---
name: app-icon-design
description: Design, generate, edit, critique, and prepare app icons for Apple platforms, Android, Web/PWA, Windows, Linux, and other targets through independent platform and visual-style modules. Use for app-icon concepts, image-generation prompts or assets, launcher and store icons, adaptive or maskable variants, cross-platform identity systems, icon reviews, small-size and mask QA, production handoff, or adding a reusable icon style to the skill.
---

# App Icon Design

Create one recognizable product identity, then adapt it to each target platform
and visual style without mixing platform specifications into aesthetic rules.

## Resolve modules before designing

### Platform modules

Read only the files needed for the requested targets:

- Apple platforms: [references/platform-apple.md](references/platform-apple.md)
- Android and Google Play: [references/platform-android.md](references/platform-android.md)
- Web, PWA, and favicon: [references/platform-web.md](references/platform-web.md)
- Windows: [references/platform-windows.md](references/platform-windows.md)

For Linux, game consoles, browser extensions, embedded systems, or another
unlisted target, inspect the project and verify current official documentation.
Record the target's canvas, mask, safe zone, alpha, layer, appearance, smallest
rendered size, packaging, and store-listing requirements before producing final
assets. Do not guess platform specifications.

### Style modules

Find installed style modules with:

```bash
rg --files <skill-dir>/references | rg '/style-[^/]+\.md$'
```

Load the module matching the user's requested style. The initial module is:

- Soft neumorphic / soft skeuomorphic:
  [references/style-soft-neumorphic.md](references/style-soft-neumorphic.md)

If no installed module matches, build a task-local style brief from the user's
words or supplied reference. Do not silently substitute a nearby style. Create
a reusable style module only when the user asks to add or preserve that style;
then follow
[references/module-style-template.md](references/module-style-template.md).

Apply constraints in this order:

1. user-owned brand and supplied content;
2. product meaning and recognizable identity;
3. hard platform requirements;
4. selected visual style;
5. export and packaging convenience.

## Follow the workflow

1. **Inspect context.** Read the brief, repository metadata, screenshots,
   existing icons, brand assets, and platform configuration when available.
2. **Write the identity brief.** Reduce the app to:
   `audience + core job + promise + category cue + differentiator`.
3. **Choose the target matrix.** Separate launcher/system icons, store-listing
   icons, web icons, and marketing artwork; they are not interchangeable merely
   because they are square.
4. **Develop concepts.** When the metaphor is not already fixed, propose three
   directions that differ in metaphor or silhouette, not only color. Recommend
   one using product meaning, memorability, originality, and small-size clarity.
5. **Define the identity invariant.** Lock the main metaphor, dominant
   silhouette, proportion relationship, brand color role, and one signature
   detail before adapting platforms or styles.
6. **Generate or edit.** Use the available image-generation tool. Inspect an
   existing target image before editing it. If the user asks to proceed without
   selecting a direction, choose the recommended direction and continue.
7. **Adapt per platform.** Preserve the identity invariant while changing
   spacing, crop, layers, background behavior, monochrome treatment, or detail
   density to satisfy each platform module.
8. **Evaluate and refine.** Inspect the full-size artwork, the smallest relevant
   display sizes, required masks, light/dark contexts, and themed or monochrome
   variants. Revise the weakest dimension with one or two targeted changes.
9. **Prepare the handoff.** Export only the formats the target actually needs,
   preserve editable masters when available, and distinguish generated concept
   art from production-ready vector or layered assets.

## Resolve missing input

Infer low-risk details from workspace context. Ask one concise question only
when the target platform, product metaphor, or style choice would otherwise be
arbitrary.

When the user supplies only an app function, default to:

- three textual concepts before generation;
- one platform-neutral identity master;
- a clear, contemporary style brief rather than an arbitrary named trend;
- no text unless it is essential to an owned brand;
- a high-resolution square working canvas, followed by target-specific assets;
- sRGB unless a verified target explicitly benefits from another color space.

Do not ask the user to repeat information already present in the project.

## Generate assets honestly

When raster image generation is available, generate the requested concept
instead of returning only a prompt. Generate one candidate per file, not a grid
of several icons, unless the user explicitly wants a comparison board.

Every generation request must state:

- app purpose and chosen metaphor;
- selected style module or task-local style brief;
- target artifact and platform treatment;
- composition, palette, material/rendering, and lighting decisions;
- small-size and mask requirements;
- explicit exclusions: text, watermark, mockup, UI screenshot, extra icons,
  unintended symbols, and copied branding.

Do not claim a flattened raster is an editable vector, adaptive icon, or layered
Icon Composer asset. Create or separate the required layers when the target
format needs them.

## Preserve originality

Use reference images to infer general visual properties, not to reproduce a
known icon. Do not copy a trademark, mascot, signature silhouette, distinctive
layout, or color arrangement. Avoid prompts that request the style of a named
living artist, studio, or existing app.

## Apply the universal quality gate

Reject or revise an icon when any of these are true:

- product meaning is generic or requires lengthy explanation;
- more than one object competes for attention;
- the dominant silhouette fails at the platform's smallest important size;
- important content leaves a guaranteed safe zone;
- a system-applied mask or shadow is baked into source artwork;
- light, shadow, depth, or material cues contradict one another;
- contrast depends on a single background or appearance;
- a themed or monochrome variant loses the identity;
- unintended text, watermark, visual artifacts, or trademark resemblance appear;
- platform-specific assets drift into visibly different product identities.

For local raster files, verify dimensions, alpha behavior, and color mode. Build
temporary previews for the required small sizes and masks without overwriting
the source. Include circle, squircle, rounded-square, or unmasked previews when
the target can vary its mask.

Score candidates from 0-2 for product meaning, silhouette, memorability,
originality, style coherence, platform readiness, and craft. Require at least
12/14 and no hard rejection before calling an asset final.

## Deliver compactly

Return:

1. final asset links;
2. selected concept and identity invariant;
3. target/style matrix;
4. exact reusable prompt or construction specification;
5. QA results at relevant sizes, masks, and appearances;
6. remaining packaging or store steps that were not performed.

## Keep the architecture modular

- Keep `SKILL.md` independent of any particular visual style.
- Keep `platform-*.md` files free of aesthetic prescriptions.
- Keep `style-*.md` files free of platform sizes and packaging instructions.
- Add a new platform or style as a directly linked reference file; do not fork
  the complete workflow.
