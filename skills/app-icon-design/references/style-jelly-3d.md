# Style Module: Jelly 3D Icon

## Contents

- Aliases and triggers
- Intent
- Shape language
- Material and rendering
- Light and depth
- Color
- Composition
- Prompt additions
- Negative constraints
- Style-specific evaluation
- Compatibility notes

## Aliases and triggers

Use for requests mentioning Jelly 3D Icon, jelly icon, jelly-glass icon,
translucent gel icon, gummy glass, 果冻 3D 图标, 果冻玻璃, 半透明凝胶, or
软质透明图标.

Do not silently substitute glassmorphism, which depends on transparent panels
and background blur, or claymorphism, which is normally opaque and matte.

## Intent

Turn one clear symbol into a friendly, dimensional object made from softly
translucent gel or glassy jelly. Create clean separation, controlled internal
glow, and tactile depth while preserving the symbol's identity at small sizes.

## Shape language

- Preserve the source symbol's dominant silhouette and internal relationships.
- Extrude forms shallowly and round exposed edges without inflating the symbol
  into an unrelated blob.
- Use broad, clean surfaces; remove micro-details that become muddy through
  refraction or downsampling.
- Use a rounded-square base only when the chosen concept and active platform
  call for a visible tile. Do not treat a system-applied mask as artwork.

## Material and rendering

- Render the symbol as soft translucent jelly with a glass-like surface, smooth
  specular response, gentle subsurface color, and restrained internal glow.
- Keep enough opacity for a stable silhouette; allow light transmission mainly
  near edges and thinner regions.
- Use consistent thickness and refractive behavior across a matched icon set.
- Avoid photorealistic food texture, liquid drips, bubbles, glitter, scratches,
  or hard crystal facets unless explicitly requested.

## Light and depth

- Use a front orthographic or near-orthographic view with minimal perspective.
- Place one soft studio key light above and to the left.
- Add a broad highlight that follows the upper-left contour rather than a hard
  white outline.
- Place a low-opacity, softly blurred contact shadow directly beneath the
  symbol with a slight downward offset. Keep the shadow quieter than the form.
- Use restrained ambient occlusion where the symbol meets its base; do not use
  black creases or multiple conflicting shadows.

## Color

- Preserve owned brand colors when the symbol is supplied.
- Otherwise choose one vivid symbol color and a distinct base color with enough
  hue or value contrast to keep their translucent edges separate.
- Let color become brighter at illuminated edges and softly denser in thicker
  regions without turning every surface into a rainbow gradient.
- Use warm gray or pastel cream only for presentation previews. Let the active
  platform module control production background and transparency behavior.

## Composition

- Center one symbol with visually even padding and a stable front-facing pose.
- Keep the symbol large enough to read but leave room for extrusion, highlight,
  contact shadow, and any required platform mask.
- Use one focal point and no supporting props.
- Generate one icon per file; use a grid only when the user asks for a set or
  comparison board.

## Prompt additions

Add clauses like these to the core generation prompt:

```text
Visual style: a polished Jelly 3D Icon treatment. Reconstruct [SYMBOL] as one
shallowly extruded object made from softly translucent colored gel with rounded
edges, smooth glass-like reflections, controlled inner glow, and a crisp,
recognizable silhouette.

Lighting and depth: centered front orthographic view, one soft studio key light
from the upper left, a broad contour highlight, restrained contact occlusion,
and one low-opacity diffused shadow immediately below the object with a slight
downward offset.

Color and composition: preserve the owned symbol colors, or use [SYMBOL COLOR]
against a clearly contrasting [BASE COLOR]. Center one symbol with even visual
padding. Keep refraction and transparency subtle enough for launcher-size
clarity.
```

Use the active platform module for canvas, mask, layers, alpha, export size, and
file format.

## Negative constraints

Exclude flat vector rendering, opaque clay, inflatable plastic, rubber toy
texture, watery liquid, glassmorphism panels, frosted blur, hard crystal facets,
mirror chrome, harsh rim light, deep perspective, long hard shadows, black
contact seams, excessive bloom, noisy refraction, bubbles, text, watermark,
mockup scenery, copied branding, and multiple competing symbols.

## Style-specific evaluation

Verify that:

- the silhouette remains recognizable after transparency and refraction;
- the material reads as translucent jelly rather than opaque plastic or water;
- highlight, inner glow, contact shadow, and extrusion agree on one light setup;
- foreground and base remain separable where their colors overlap;
- a matched set keeps the same camera, material thickness, light direction, and
  shadow softness;
- removing the presentation background does not remove essential icon content.

## Compatibility notes

Reduce inner refraction, glow, extrusion, and shadow detail at small sizes. Build
monochrome variants from the identity silhouette rather than grayscale jelly.
For layered targets, keep base, symbol, highlight, and shadow separable when the
platform supports or requires independent layers. Never bake a platform mask or
system shadow into the source master.
