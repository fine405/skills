# Web, PWA, and Favicon Platform Module

Use this module for web app manifests, installable PWAs, favicons, bookmarks,
pinned tabs, browser shortcuts, or web launch surfaces.

## Verify current requirements

Use current browser and standards documentation:

- https://www.w3.org/TR/appmanifest/
- https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Define_app_icons
- https://web.dev/articles/maskable-icon

Browser behavior varies. Inspect the target browser matrix and existing manifest
before changing assets.

## Keep icon purposes separate

Provide distinct assets when the contexts differ:

- `any`: general-purpose icon with no assumption that a mask will crop it;
- `maskable`: opaque square designed for user-agent masks;
- `monochrome`: alpha silhouette intended for a system-selected solid fill;
- favicon/pinned-tab: simplified browser chrome variants.

Do not reuse a heavily padded maskable icon as the only `any` icon; it often
appears unnecessarily small where no mask is applied.

## PWA maskable icon

- Use an opaque square image.
- Keep all essential content inside the centered circular safe zone whose radius
  is 40% of the icon width.
- Treat the outer area as expendable background or nonessential decoration.
- Test circle, squircle, rounded-square, and full-bleed masks.
- Use `purpose: "maskable"` for the dedicated manifest entry.

For Chromium-oriented installability, include at least 192 x 192 and 512 x 512
manifest icons. Provide a maskable icon of at least 512 x 512 when that platform
is in scope. Verify actual requirements for the target browser rather than
assuming Chromium rules apply everywhere.

## Favicons and browser surfaces

- Preserve a simple silhouette at 16 px and 32 px.
- Prefer an SVG favicon when supported and useful, with raster/ICO fallbacks for
  the project's browser matrix.
- Hand-tune small raster sizes instead of relying on one detailed illustration
  to downsample cleanly.
- Use a dedicated monochrome mask for pinned-tab or solid-fill contexts when the
  browser expects one.

## Web QA

- Validate manifest paths, MIME types, declared sizes, and purposes.
- Inspect the Application/Manifest panel in supported browser developer tools.
- Test install surfaces, tabs, bookmarks, shortcuts, and light/dark browser UI.
- Confirm maskable safe-zone content survives every previewed mask.
- Check cache invalidation when an old icon persists after deployment.
