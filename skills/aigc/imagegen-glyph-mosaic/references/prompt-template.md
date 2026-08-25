# Glyph-mosaic prompt template

Use this template for full-color raster illustrations made from visible monospaced glyphs. Remove labels that do not help the current request.

```text
Use case: stylized-concept
Asset type: <standalone art print / cover / square illustration / other>
Input images: <Images 1–N: style references only; do not copy their subjects or geography>

Primary request:
Create <SUBJECT AND SCENE>.

Composition/framing:
<ASPECT RATIO, VIEWPOINT, FOREGROUND, FOCAL SUBJECT, MIDGROUND, BACKGROUND, AND VISUAL PATH>.

Style/medium:
A polychrome textmode glyph-mosaic illustration constructed entirely from small monospaced letters, digits, punctuation, and directional symbols on one strict rectangular character grid. Every visible surface, edge, shadow, cloud, and tonal transition must be formed through glyph cells rather than conventional brush strokes or a text overlay.

From a distance, the glyphs optically merge into a coherent, richly detailed scene. At close range, individual characters remain clearly visible.

Glyph logic:
Use sparse punctuation such as periods, commas, apostrophes, and colons for highlights, mist, and open atmosphere. Use slashes, backslashes, underscores, and dashes to follow slopes, roofs, roads, clouds, and directional contours. Use vertical bars and narrow letters for trunks, columns, and tall structures. Use dense glyphs such as hashes, percent signs, eights, and at-signs for foliage, rock, and deep shadows. Vary glyph density by luminance and align glyph direction with local geometry.

Lighting/mood:
<TIME OF DAY, LIGHT DIRECTION, WEATHER, AND EMOTIONAL TONE>.

Color palette:
Use approximately 8–12 colors.
Atmosphere: <COOL OR WARM DISTANT COLOR>.
Highlight: <LIGHT OR PAPER-LIKE COLOR>.
Midtone A: <PRIMARY LOCAL COLOR>.
Midtone B: <SECONDARY LOCAL COLOR>.
Shadow anchor: <DEEPEST STRUCTURAL DARK>.
Accent: <SMALL CONTROLLED ACCENT>.
Keep saturation <LOW / MODERATE / VIVID>. Create transitions through glyph density, optical color mixing, and stepped palette changes rather than smooth gradients.

Surface quality:
Crisp glyph shapes, tight monospaced spacing, matte printed finish, restrained grain, and slightly faded reproduction color.

Constraints:
Use one consistent character grid across the complete image. Include no meaningful sentences, large readable words, captions, logos, signatures, or watermarks.

Avoid:
ordinary pixel art; a normal painting or photograph with random text overlaid; smooth non-glyph areas; terminal screenshots; cyberpunk neon; green-on-black hacker aesthetics; UI chrome; large typography; random alphabet soup; plastic 3D rendering.
```

## Palette-role examples

These palettes are starting points, not part of the permanent style identity.

| Profile | Atmosphere | Highlight | Midtone A | Midtone B | Shadow anchor | Accent |
| --- | --- | --- | --- | --- | --- | --- |
| Forest | dusty teal | warm ivory | moss green | muted ochre | deep pine-umber | soft amber |
| Snow night | deep indigo | moonlit cream | slate blue | icy blue-gray | near-black blue | muted window amber |
| Golden mountain | powder blue | glacier ivory | warm gold | rose ochre | dark olive-umber | concentrated summit gold |

## Compact style suffix

```text
Render the scene as a polychrome textmode glyph mosaic: the entire image is constructed from crisp monospaced letters, digits, and punctuation on one strict character grid. Map glyph density to luminance and directional symbols to local contours. From a distance the glyphs merge into a coherent painterly image; at close range individual characters remain visible. Use a restrained 8–12 color palette, stepped tonal transitions, atmospheric depth, matte vintage-print softness, and no smooth non-glyph regions, terminal UI, large readable words, or random text overlay.
```
