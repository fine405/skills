# Windows App Icon Platform Module

Use this module for WinUI, UWP, WPF, Win32, Microsoft Store, Start, taskbar,
title-bar, system-tray, or ICO assets.

## Verify current requirements

Inspect the actual project type and current Microsoft documentation:

- https://learn.microsoft.com/windows/apps/design/iconography/app-icons
- https://learn.microsoft.com/windows/apps/design/iconography/app-icon-construction

Windows asset names and required variants differ across packaging systems. Do
not generate a generic folder of files before resolving the project type.

## Size system

Windows prefers exact-size matches and otherwise scales down from a larger
asset. At minimum, prepare intentional artwork for:

- 16 x 16;
- 24 x 24;
- 32 x 32;
- 48 x 48;
- 256 x 256.

Do not treat the 16 px and 24 px versions as automatic reductions of a detailed
master. Simplify shapes, merge tiny gaps, strengthen key contrast, and preserve
the identifying feature.

For Win32 `.ico`, package the exact sizes required by the application and its
supported Windows versions. For packaged Windows apps, follow the project's
manifest asset names, scale factors, target-size assets, and theme variants.

## Background and theme behavior

- Prefer a transparent/unplated icon when the identity works without a tile.
- When a background plate is essential, provide deliberate light and dark
  variants rather than trusting one plate everywhere.
- Verify whether the packaging flow needs default, light-theme, dark-theme, or
  unplated alternatives.
- Keep Store logos, splash assets, tiles, and the primary app icon distinct;
  they occupy different contexts even if they share a mark.

## Windows QA

- Inspect 16, 24, 32, 48, and 256 px assets individually.
- Test Start, taskbar, search, title bar, system tray, and context menus that are
  in scope.
- Preview light, dark, and high-contrast environments as supported.
- Reject accidental system backplates caused by missing unplated assets.
- Confirm the packaged application and Store submission reference the intended
  files.
