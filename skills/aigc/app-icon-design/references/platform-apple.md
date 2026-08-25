# Apple App Icon Platform Module

Use this module for iOS, iPadOS, macOS, watchOS, tvOS, visionOS, App Store
assets, Xcode asset catalogs, or Icon Composer handoff.

## Verify current requirements

Apple's formats and rendering behavior evolve. Before production packaging,
check:

- https://developer.apple.com/design/human-interface-guidelines/app-icons/
- https://developer.apple.com/documentation/Xcode/creating-your-app-icon-using-icon-composer
- https://developer.apple.com/documentation/xcode/configuring-your-app-icon

Treat the values below as the current working profile, not timeless rules.

## Current design canvases

| Target | Working layout | System result |
| --- | --- | --- |
| iOS, iPadOS, macOS | 1024 x 1024 square, layered | rounded-square mask applied by the system |
| watchOS | 1088 x 1088 square, layered | circular mask applied by the system |
| tvOS | 800 x 480 landscape, layered | rounded rectangular parallax icon |
| visionOS | 1024 x 1024 square, layered | circular three-dimensional icon |

Keep the primary identity consistent across supported Apple platforms while
adjusting scale, placement, layer behavior, and platform appearance in the
appropriate tool.

## Source artwork

- Supply unmasked artwork. Do not export the final canvas mask.
- Keep primary content centered and away from mask-sensitive corners.
- Prefer SVG for scalable shape layers and PNG for raster or mesh-gradient art.
- Name layers by back-to-front order and visual role.
- Separate only elements that need independent material, placement, appearance,
  or platform adjustment.
- Keep foreground edges clean. Avoid feathered edges that weaken system effects.

When preparing Icon Composer sources, defer final shadows, blur, specular,
refraction, opacity, translucency, and platform masking to Icon Composer where
possible. Define simple background colors or gradients there rather than
baking them into unrelated foreground layers. If importing a raster background,
make it full-bleed and opaque.

## Flattened compatibility master

When the actual project still uses a single raster asset rather than layered
artwork:

- use a 1024 x 1024 square source for iOS, iPadOS, or compatible catalog flows;
- keep canvas corners unmasked;
- avoid an outer shadow or transparent corner halo;
- export an opaque fallback unless the verified target pipeline permits alpha;
- let Xcode generate smaller variants when the project supports that flow.

Do not confuse a standalone presentation rendering with a production source
layer.

## Appearance QA

Preview every appearance supported by the chosen tool and deployment target,
including Default, Dark, Clear, Tinted, or Mono as applicable.

- Preserve the same core features in every appearance.
- Avoid swapping the metaphor between modes.
- Verify subdued modes still retain enough value separation.
- Inspect Home Screen/Dock scale, Settings, search, notifications, and the
  smallest relevant rendered size.
- Build and inspect the installed app when integration is in scope; image-file
  inspection alone does not catch stale caches or configuration mistakes.

## Target-specific cautions

- tvOS: preserve a generous safe zone because parallax and focus can crop
  foreground layers differently.
- visionOS: avoid treating a hole in the background as a concave effect; system
  shadows can reverse the intended depth.
- watchOS: avoid a pure-black background that disappears into the display.
- macOS/iOS: do not pre-shape current source layers merely to imitate a historic
  platform icon silhouette.
