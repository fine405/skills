# Style Module: Discomorphism

## Contents

- [Aliases and triggers](#aliases-and-triggers)
- [Intent](#intent)
- [Shape language](#shape-language)
- [Material and rendering](#material-and-rendering)
- [Light and depth](#light-and-depth)
- [Color](#color)
- [Composition](#composition)
- [Prompt additions](#prompt-additions)
- [Negative constraints](#negative-constraints)
- [Style-specific evaluation](#style-specific-evaluation)
- [Compatibility notes](#compatibility-notes)

## Aliases and triggers

Use for requests mentioning discomorphism, disco-mosaic, mirrored-tile mosaic,
mirror-ball material, tiled chrome, reflective square tiles, 迪斯科拟态,
迪斯科马赛克, 镜面马赛克, 镜面方砖, or a logo reconstructed from tiny
mirrored squares.

Do not silently substitute plain chrome, glitter, sequins, rhinestones, glass
beads, pixel art, or a spherical disco ball. Those treatments do not provide
the same contour-following square-mirror construction.

## Intent

Reconstruct the primary symbol as a dimensional, reflective mosaic while
preserving its identity, silhouette, color roles, and composition. The result
should feel like a precisely fabricated icon-scale object, with enough optical
energy to feel celebratory but enough control to remain readable.

## Shape language

- Preserve the source symbol's outer contour, internal cutouts, proportions,
  and spatial relationships when restyling an existing identity.
- Give the symbol shallow-to-moderate volume only where volume helps explain
  the original shape; do not inflate every mark into a ball or pillow.
- Tessellate visible surfaces with small square or near-square mirror tiles.
- Clip tiles cleanly at outer edges and holes. Let their orientation follow
  local planes and curvature instead of projecting one flat grid across the
  entire object.
- Keep tile scale consistent enough to read as fabrication, then simplify it
  when dense tiling would damage the silhouette at the target display size.
- Preserve sharp corners, narrow bridges, counters, and asymmetric details that
  make the symbol recognizable.

## Material and rendering

- Use beveled mirrored tiles with controlled seams and a reflective metal or
  tinted-mirror finish.
- Let adjacent tiles vary through physically plausible reflections, not random
  checkerboard coloring.
- Use small gaps, bevels, and changing reflection angles to reveal the mosaic;
  avoid heavy grout or dark outlines that fragment the symbol.
- Keep the underlying object visually solid. Do not expose a cage, wireframe,
  hollow shell, or broken facets unless the concept requires it.
- Render at polished product-visualization realism. Avoid dirty mirrors,
  scratched metal, distressed texture, or liquid-metal deformation unless the
  user explicitly combines those treatments.

## Light and depth

- Use a broad studio key and restrained fill to describe the full silhouette.
- Add a few deliberate specular glints at high points or outer edges; keep them
  sparse enough that they do not hide contours or internal negative space.
- Allow tile-to-tile reflection changes to explain curvature and facet
  orientation.
- Use restrained contact shadow or ambient occlusion only when the symbol is a
  separate foreground object.
- Keep camera perspective shallow and icon-like. Avoid dramatic wide-angle
  distortion, deep scenes, floating debris, or stage-light backgrounds.

## Color

- Preserve the source identity's color roles by mapping each original region to
  a corresponding mirror tint.
- Render white or neutral-light regions as silver or neutral chrome unless an
  owned brand specification says otherwise.
- Render colored regions as tinted reflective tiles whose average perceived hue
  remains close to the source color.
- Preserve intentional gradients as controlled regional tint transitions, not
  unrelated rainbow reflections.
- Preserve the original background role and sampled color when restyling an
  existing icon. Do not replace it with black merely to increase reflections.
- Maintain separation between neighboring color regions after highlights and
  reflections are applied.

## Composition

- When editing an existing icon, keep symbol position, scale, orientation,
  negative space, and background layout unchanged unless the user requests a
  redesign.
- Use one primary tiled symbol and no decorative disco balls, spotlights,
  confetti, extra tiles, or duplicate marks.
- Keep reflections inside the symbol except for restrained glints and a natural
  contact shadow.
- Defer mask clearance and platform-specific spacing to the active platform
  module.

## Prompt additions

Add clauses like these to the core generation or edit prompt, adapting
placeholders to the identity:

```text
Visual style: discomorphic mirrored-tile construction. Rebuild [SYMBOL] as a
coherent three-dimensional object whose visible surfaces are tessellated with
small beveled square mirror tiles. The tile grid follows every plane, curve,
outer contour, and internal cutout of the original symbol.

Identity preservation: retain the original silhouette, proportions, position,
orientation, negative space, and background composition. Map each source color
region to matching tinted mirror tiles; use neutral silver chrome for
[LIGHT/NEUTRAL REGION]. Preserve the sampled background color and do not add
new objects.

Rendering: polished product-visualization realism, broad studio key light,
controlled fill, physically plausible tile-to-tile reflections, fine seams,
and only a few crisp specular glints. Keep the complete symbol readable at app
icon size.
```

For reference-guided editing, identify the source image as an identity and
layout constraint, not as permission to invent or copy unrelated branding.
Use the active platform module to supply canvas, mask, layer, safe-zone, alpha,
and packaging clauses.

## Negative constraints

Exclude a generic spherical disco ball, plain unsegmented chrome, liquid metal,
glitter dust, sequins, rhinestones, round mirror pieces, glass beads, pixel art,
random checkerboard colors, rainbow drift, oversized grout, broken tiles,
missing counters, warped lettering, inflated blob geometry, excessive bloom,
lens-flare clutter, nightclub scenery, spotlights, confetti, extra symbols,
layout changes, background recoloring, unintended text, watermarks, and copied
branding.

## Style-specific evaluation

In addition to the universal quality gate, verify:

- the untiled silhouette would still match the intended identity;
- tiles remain square-like, individually legible, and clipped to precise edges;
- tile orientation changes coherently across planes and curved surfaces;
- internal holes and narrow bridges remain open and recognizable;
- average tile color preserves each source color region;
- the background and composition remain stable in reference-guided edits;
- reflections and glints reveal material without erasing the symbol;
- at small size, the tiles merge into a controlled reflective texture rather
  than visual noise.

## Compatibility notes

For small variants, reduce tile count, widen important gaps, simplify reflection
variation, and retain only one or two glints while preserving the main contour.
For monochrome treatments, derive a clean silhouette rather than flattening the
mirror rendering into noisy grayscale. For layered deliverables, keep the
background, tiled symbol, contact shadow, and optional glints separable when the
target format supports independent layers.
