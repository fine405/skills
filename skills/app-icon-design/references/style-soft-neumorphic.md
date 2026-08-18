# Style Module: Soft Neumorphic

## Aliases and triggers

Use for requests mentioning soft neumorphism, soft skeuomorphism, 轻拟物,
软拟物, soft UI, tactile relief, embossed surfaces, recessed controls, or a
quiet crafted-object icon treatment.

## Intent

Create gentle physical depth through coherent light, raised or recessed forms,
and restrained material cues. The result should feel tactile without becoming
a low-contrast interface control, cartoon clay object, or heavy 3D render.

## Shape language

- Use one dominant metaphor and 2-5 broad forms.
- Prefer shallow extrusion, soft bevels, controlled recesses, and clear edge
  transitions.
- Preserve a recognizable silhouette before adding surface treatment.
- Use rounded geometry selectively; do not round every element into a blob.
- Keep decorative seams, grooves, or embossing subordinate to the main shape.

## Material and rendering

Choose one primary material that reinforces the product meaning, such as matte
polymer, ceramic, paper, leather, fabric, frosted acrylic, wood, or restrained
metal. Describe only the visible evidence needed to sell it: roughness, edge
softness, translucency, fiber, grain, seam, or reflection.

- Keep depth shallow and physically coherent.
- Use localized ambient occlusion at overlaps and recesses.
- Avoid mixing unrelated materials for decoration.
- Avoid uniformly glossy plastic, inflatable clay, jelly, chrome, or cinematic
  photorealism unless the user explicitly combines styles.

## Light

- Use one broad soft key light, normally from the upper left.
- Keep contact shadows short and quiet.
- Use highlights to explain curvature and material, not as decoration.
- Maintain the same light direction across every layer.
- Preserve enough value and color contrast that the icon remains understandable
  after its softest shadows disappear.

## Color

- Use 2-4 functional colors.
- Begin with one quiet base or surface color.
- Add one dominant brand hue and at most one small accent.
- Prefer tonal separation and material contrast over rainbow gradients, neon
  rims, or extreme saturation.
- Test the icon in grayscale and against both light and dark surroundings.

## Composition

- Keep one focal point.
- Let the main subject use roughly two-thirds to four-fifths of the available
  safe area, adjusted by the active platform module.
- Use quiet background treatment and enough negative space for the required
  masks.
- Do not place a second decorative app tile behind the subject unless the
  product metaphor itself requires a container.

## Prompt additions

Add clauses like these to the core generation prompt, adapting nouns to the
chosen concept:

```text
Visual style: restrained soft-neumorphic / soft-skeuomorphic icon design with
shallow tactile relief, precise softened edges, coherent material cues, and a
quiet premium finish. The main silhouette remains crisp at launcher size.

Depth and light: one broad soft key light from the upper left, short contact
shadows, subtle localized ambient occlusion, and controlled highlights that
explain form. No deep extrusion or conflicting shadows.

Material: one primary [MATERIAL], visible through [TWO OR THREE MATERIAL CUES].
Do not mix unrelated decorative materials.
```

Use the active platform module to supply canvas, mask, layer, safe-zone, alpha,
and packaging clauses.

## Negative constraints

Exclude flat generic glyphs, low-contrast shadow-only separation, cartoon
stickers, inflatable clay, glossy jelly, chrome overload, neon rim light, deep
perspective, feature collages, noisy microtexture, inconsistent light,
unintended text, watermarks, and copied branding.

## Style-specific evaluation

In addition to the universal quality gate, verify:

- the material remains identifiable without excessive texture;
- raised and recessed areas agree with the light direction;
- foreground/background separation does not depend only on a faint shadow;
- the icon remains clear when rendered flat or monochrome by a platform;
- removing one decorative detail makes the result no less understandable.

## Compatibility notes

Platform constraints take priority. Reduce texture and depth for tiny Windows
or favicon sizes, create a deliberate silhouette for Android or web monochrome
variants, and avoid baking system masks or shadows into any source asset.
