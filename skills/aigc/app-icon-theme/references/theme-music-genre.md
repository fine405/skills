# Theme Module: Music Genre

## Contents

- [Aliases and triggers](#aliases-and-triggers)
- [Theme scope](#theme-scope)
- [Identity invariant contract](#identity-invariant-contract)
- [Semantic cue palette](#semantic-cue-palette)
- [Transformation modes](#transformation-modes)
- [Intensity scale](#intensity-scale)
- [Style combination](#style-combination)
- [Prompt additions](#prompt-additions)
- [Negative constraints](#negative-constraints)
- [Theme-specific evaluation](#theme-specific-evaluation)
- [Compatibility notes](#compatibility-notes)

## Aliases and triggers

Use for requests to make an app icon match a music taste, genre, playlist,
concert, listening mode, or sonic mood; genre-themed icons; music skins; 按曲风
设计图标; 音乐类型主题; 摇滚、古典、嘻哈、爵士、乡村、电子、迪斯科或
氛围音乐主题图标.

Do not treat a general mood request as a music genre unless listening context is
clear. Do not silently replace a named genre with a nearby genre or subculture.

## Theme scope

Translate the selected genre into one dominant visual association while keeping
the source icon recognizable. Use material, fabrication, instrument-adjacent
construction, performance marks, or characteristic motion as cues. Avoid
turning the result into a poster, album cover, musician portrait, or scene.

## Identity invariant contract

Preserve the source mark's dominant silhouette, internal cutouts, proportion
relationships, orientation, and brand-color roles. A genre may change material,
surface, depth, or one controlled structural feature; it must not replace the
mark with an unrelated instrument or performer.

## Semantic cue palette

Treat these as optional starting families, not fixed formulas:

| Genre family | Possible primary cues | Avoid defaulting to |
| --- | --- | --- |
| Classical | carved stone, cast bronze, engraved medallion, instrument craft, architectural rhythm | a recognizable statue, composer portrait, or ornate collage |
| Rock | speaker cone, amplifier grille, road-worn metal, cable rhythm, stage-hardware construction | skulls, hand signs, fire, or destructive clichés |
| Hip-hop | aerosol stencil, vinyl groove, sampler-pad geometry, bold cut-paper rhythm | caricature, imitation tags, jewelry overload, or copied streetwear marks |
| Country / folk | tooled leather, warm wood, stitched textile, instrument-case craft, weathered enamel | costume stereotypes, flags, weapons, or a mandatory cowboy hat |
| Disco | mirrored facets, rhythmic glints, polished dance-floor geometry, circular repetition | nightclub scenery, confetti, or a generic sphere replacing the source mark |
| Electronic / acid | phosphor glow, synthetic resin, modular-grid rhythm, controlled liquid geometry | pill imagery, random neon cyberpunk, or unreadable distortion |
| Jazz / soul | brushed brass, dark lacquer, velvet contrast, syncopated curves, club-sign craft | performer silhouettes, smoke-filled scenes, or generic retro pastiche |
| Ambient / lo-fi | frosted surfaces, soft diffusion, worn media texture, quiet loops, restrained haze | muddy blur, illegible low contrast, or a complete loss of structure |

Select cues that fit the requested subgenre and audience. When the label is
ambiguous, offer three cue directions instead of asserting one visual truth.

## Transformation modes

- **Surface/material:** map the source mark to one genre-linked material or mark
  system while preserving its geometry. This is the safest default.
- **Structural analogy:** let the source form borrow construction from one
  relevant artifact, such as a speaker diaphragm or engraved medallion, without
  becoming that artifact entirely.
- **Controlled accessory:** add one compact cue only when it does not obscure
  the mark. Prefer construction details over costume-like decoration.

Use one primary mode. A secondary mode may support it at `expressive` intensity
when identity remains obvious at small size.

## Intensity scale

- **Subtle:** preserve geometry and composition; change material, surface marks,
  or edge treatment only.
- **Balanced:** use one material cue plus one restrained structural analogy. The
  genre reads without a label, while the source identity reads first.
- **Expressive:** allow stronger depth, deformation, or one accessory, but keep
  critical contours and cutouts unchanged.

## Style combination

The genre supplies semantic cues; the selected style supplies the rendering
grammar. Translate the cue into that grammar instead of replacing it.

- With mirrored-mosaic rendering, express disco through tile rhythm and glints;
  express rock through darker tinted facets and speaker-like depth without
  abandoning the tile construction.
- With soft-neumorphic rendering, express classical through shallow carved
  relief or rock through restrained recessed hardware.
- With translucent-jelly rendering, express genres through color roles, embedded
  rhythm, or controlled inner structures rather than swapping to opaque metal.

When theme and style conflict, preserve identity first, then use the smallest
theme cue that remains coherent with the style.

## Prompt additions

Add a block like this to the core prompt:

```text
Theme: reinterpret the user-owned [SOURCE SYMBOL] through a [MUSIC GENRE]
theme. Preserve [IDENTITY INVARIANT]. Use [PRIMARY CUE] as the single dominant
genre signal through [TRANSFORMATION MODE] at [INTENSITY] intensity. The source
identity must read before the genre treatment, and the genre should remain
understandable without a caption.

Theme boundaries: do not replace the symbol with an instrument, performer, or
scene. Avoid genre stereotypes, copied cultural marks, extra text, and unrelated
decoration. Apply the separately selected [RENDERING STYLE] consistently.
```

## Negative constraints

Exclude album-cover layouts, performers, portraits, copied graffiti tags,
recognizable sculptures, costume caricatures, genre captions, equalizer
wallpaper, instrument collages, random musical notes, skull-and-fire shorthand,
drug imagery, flags, weapons, unrelated neon, extra app marks, and changes that
make the source identity dependent on its original color alone.

## Theme-specific evaluation

Verify that:

- viewers can identify the source mark before reading the genre label;
- viewers can infer the genre family from the primary cue without a caption;
- the cue is materially or structurally integrated rather than pasted on;
- the result avoids cultural caricature and unlicensed distinctive marks;
- a set of genres shares the same camera, scale, spacing, and identity invariant;
- differences among variants come from semantic cues, not arbitrary palettes;
- removing the theme cue would reveal a coherent version of the original mark.

## Compatibility notes

At small sizes, preserve the primary material or structural cue and remove
supporting texture, seams, haze, and accessories. Build monochrome variants from
the identity silhouette; do not expect genre-specific material to survive.
For layered outputs, keep the invariant mark, theme treatment, and optional
accessory separable when the target format permits it.
