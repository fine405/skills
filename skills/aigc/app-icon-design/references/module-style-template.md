# Reusable Style Module Template

Create `references/style-<slug>.md` from this contract when the user asks to
add a reusable app-icon style. Keep the module independent of platform sizes,
file formats, safe zones, store rules, and packaging.

## Required sections

```markdown
# Style Module: <Human Name>

## Aliases and triggers
List the user phrases, translations, and adjacent names that should select this
module. Explain one or two nearby styles that must not be substituted silently.

## Intent
State the visual goal and emotional promise in two or three sentences.

## Shape language
Define silhouette, geometry, line/edge behavior, complexity, and characteristic
proportions using visible decisions rather than taste adjectives alone.

## Material and rendering
Define flat/vector/painted/3D/material treatment, texture, surface behavior, and
the allowed degree of realism.

## Light and depth
Define light direction, shadow behavior, perspective, volume, and motion cues.

## Color
Define palette roles, contrast, saturation, gradient behavior, and appearance
expectations without hard-coding a brand palette.

## Composition
Define focal-point count, crop, negative space, density, and use of supporting
objects. Defer safe-zone percentages to the active platform module.

## Prompt additions
Provide a compact positive clause that can be inserted into the generic app-icon
prompt. Use placeholders for concept-specific nouns.

## Negative constraints
List the visual failures and adjacent styles that cause drift.

## Style-specific evaluation
Add only checks not already covered by the universal quality gate.

## Compatibility notes
Explain how the style should simplify for small sizes, monochrome variants, or
layered assets. Do not repeat platform specifications.
```

## Authoring rules

- Derive rules from general visual principles or user-owned references; do not
  cite or copy private prompts, proprietary skill text, named artists, or a
  specific existing app's identity.
- Describe visible construction decisions instead of relying on adjectives such
  as "beautiful," "modern," or "premium."
- Keep the module narrow enough to reject nearby styles.
- Make the module useful across Apple, Android, Web, Windows, and future
  platform adapters.
- Link the new module directly from `SKILL.md` only when a stable user-facing
  catalog entry is useful; filename discovery must continue to work without it.
