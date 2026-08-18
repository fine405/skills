# Android App Icon Platform Module

Use this module for Android launcher icons, adaptive icons, themed icons,
Android Studio assets, or Google Play listing icons.

## Verify current requirements

Check the official sources before production handoff:

- https://developer.android.com/develop/ui/compose/system/icon_design_adaptive
- https://developer.android.com/distribute/google-play/resources/icon-design-specifications

Keep launcher assets and Google Play listing assets separate.

## Adaptive launcher icon

Prepare three visual roles:

1. background layer;
2. foreground layer;
3. monochrome layer for themed presentation.

Use a 108 x 108 dp coordinate system for each layer. Keep essential foreground
content inside the centered 66 x 66 dp guaranteed safe zone. The main logo or
symbol should normally be at least 48 x 48 dp and must not exceed the 66 x 66 dp
safe area. Treat the outer 18 dp on each side as crop and motion territory.

- Prefer vector layers when practical.
- Use clean unmasked edges.
- Do not add a background shadow around the layer outline.
- Let the launcher apply circle, squircle, rounded-square, or OEM masks.
- Keep foreground and background visually useful when parallax or pulsing moves
  them relative to each other.
- Make the monochrome asset a deliberate silhouette, not a desaturated color
  icon with weak alpha.

Preview the adaptive icon under multiple masks and wallpaper-derived themed
colors. Reject any version whose identity depends on material texture or color
that disappears in the monochrome layer.

## Google Play listing icon

The Play listing icon is a separate full-square asset:

- 512 x 512 px;
- 32-bit PNG;
- sRGB;
- no more than 1024 KB;
- no baked rounded corners;
- no outer drop shadow because Google Play applies masking and shadowing.

Use the full asset space for illustrated artwork when appropriate. Place a
freeform logo using the official keyline guidance instead of stretching it.
Avoid transparent surroundings when a brand background produces a more stable
result across store contexts.

## Android QA

- Preview circle, squircle, rounded-square, and aggressive OEM masks.
- Inspect foreground/background separation during motion.
- Check the monochrome layer under several generated theme colors.
- Verify the foreground never leaves the guaranteed 66 dp safe zone.
- Inspect a real launcher after rebuilding when integration is in scope.
- Confirm the Play icon has no mask or outer shadow baked in.
