---
name: app-icon-theme
description: Create, generate, edit, critique, and systematize theme-driven variants of an existing app icon while preserving its owned identity. Use when an icon or logo should match a music genre, season, mood, event, sport, profession, culture, campaign, content category, or another semantic theme; when producing a coherent themed icon set; or when adding a reusable theme module without binding it to one rendering style or platform.
---

# App Icon Theme

Reinterpret an existing icon through a semantic theme while preserving the
features that make the original identity recognizable.

## Resolve the theme module

Find installed modules with:

```bash
rg --files <skill-dir>/references | rg '/theme-[^/]+\.md$'
```

Load only the module matching the request. Installed modules include:

- Music genres: [references/theme-music-genre.md](references/theme-music-genre.md)

If no module matches, create a task-local theme brief from the user's words and
references. Do not silently substitute a nearby theme. Add a reusable module
only when the user asks to preserve or extend that theme family; then follow
[references/module-theme-template.md](references/module-theme-template.md).

## Keep theme separate from style and platform

- A **theme** decides what the icon evokes: rock, winter, celebration, calm,
  sport, craft, or another semantic world.
- A **style** decides how it is rendered: soft-neumorphic, mirrored mosaic,
  translucent jelly, flat vector, or another visual treatment.
- A **platform** decides canvas, masks, layers, safe zones, appearances, export,
  and packaging.

Use `$app-icon-design` when it is installed and the request also needs a new
identity, multiple target platforms, production packaging, or full app-icon QA.
This skill remains usable alone for a platform-neutral theme master or when the
user supplies the necessary target constraints.

Apply constraints in this order:

1. user-owned identity and supplied content;
2. product meaning and recognizability;
3. verified hard platform requirements;
4. selected theme;
5. selected rendering style;
6. presentation convenience.

## Follow the workflow

1. **Inspect inputs.** Treat the source icon as an identity constraint. Label
   other images as theme, material, composition, or style references instead of
   merging their roles implicitly.
2. **Lock the identity invariant.** Record the dominant silhouette, internal
   cutouts, proportion relationships, layout, brand-color roles, and one
   signature detail that must survive every variant.
3. **Write the theme brief.** Name the theme, its intended emotional signal,
   one primary visible cue, up to two supporting cues, and associations to
   avoid. Prefer concrete materials, objects, construction, marks, or motion
   cues over labels alone.
4. **Choose one transformation mode.** Use surface/material substitution,
   structural analogy, or one controlled accessory. Combine modes only when the
   icon remains simpler than the theme explanation.
5. **Set intensity.** Use `subtle`, `balanced`, or `expressive`. Default to
   `balanced`: the theme reads without a caption, but the source identity reads
   first.
6. **Resolve the rendering style.** Load a requested style independently. If no
   style is requested, choose a restrained treatment that makes the selected
   theme cue visible without inventing another named trend.
7. **Generate or edit.** Use the available image-generation tool. Inspect an
   existing target image before editing it. Generate one candidate per file;
   create a grid only when the user asks for a comparison board.
8. **Evaluate and refine.** Inspect full size and the smallest relevant display
   size. Revise the weakest of identity recognition, theme legibility, style
   coherence, or craft rather than adding more cues.

## Resolve missing input

Ask one concise question only when the source identity or intended theme is
missing and cannot be inferred safely. If no existing icon or identity is
available, use `$app-icon-design` to establish one before making theme variants.

When intensity is unspecified, use `balanced`. When a theme is broad, propose
three cue directions that differ semantically, recommend one, and wait for a
choice only when selecting silently would materially change the identity.

## Build the generation prompt

State:

- the source symbol and identity invariant;
- the theme, emotional signal, and primary visible cue;
- transformation mode and intensity;
- selected rendering style or neutral rendering treatment;
- composition and brand-color behavior;
- active platform constraints when supplied;
- explicit exclusions: extra symbols, captions, watermarks, copied branding,
  stereotypes, and unrequested layout changes.

For reference-guided edits, preserve the original composition unless the user
asks for redesign. Do not claim exact brand-color preservation when a generated
raster has not been measured against an owned source.

## Preserve originality and cultural care

Use supplied references to infer general construction and semantic cues, not to
copy a known icon, campaign, mascot, costume, or distinctive composition. Avoid
reducing a culture, community, profession, or music genre to a caricature.
Prefer material, craft, instrument, environment, and motion associations over
faces, bodies, identity traits, or costume stereotypes.

## Apply the theme quality gate

Reject or revise a variant when:

- the source identity is recognizable only after seeing the original;
- the theme is understandable only from a caption;
- more than one cue competes with the main symbol;
- an accessory hides a critical contour or internal cutout;
- color or texture replaces silhouette as the only identity signal;
- the result depicts a themed object but no longer functions as the same icon;
- cultural shorthand becomes stereotyped, derogatory, or misleading;
- the selected style erases the theme cue, or the theme breaks style coherence;
- small-size simplification removes either identity or theme completely.

Score identity recognition, theme legibility, cue economy, originality,
style compatibility, small-size clarity, and craft from 0-2. Require at least
12/14 with no hard rejection before calling a theme variant final.

## Deliver compactly

Return:

1. generated or edited asset links;
2. the identity invariant;
3. theme, cue, mode, intensity, and optional style;
4. the exact reusable prompt or construction specification;
5. small-size and reference-preservation QA;
6. any platform production work that remains.

## Keep the architecture modular

- Keep `theme-*.md` files independent of named brands, rendering styles,
  platform sizes, and packaging instructions.
- Keep theme modules focused on semantic mapping and transformation choices.
- Add a new theme family as one directly linked reference file; do not fork the
  complete workflow.
