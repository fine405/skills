# Design DNA extraction

## Read in order

1. **Canvas:** viewport, fold, background, page edge behavior, dominant masses.
2. **Sequence:** first attention target, reading path, major transitions, exit.
3. **Structure:** primary composition, grid, alignment breaks, density changes,
   sticky or overlapping relationships.
4. **Type roles:** display, body, labels, metadata, data/code; note size contrast,
   width, weight, case, line height, and measure before naming fonts.
5. **Color roles:** paper, ink, muted ink, accent, rules, surfaces, semantic state.
6. **Components:** identify visible navigation, hero, feature, proof, form, CTA,
   and footer behaviors without naming unseen states.
7. **Imagery and material:** crop, scale, framing, illustration language, texture,
   shadows, borders, and radii.
8. **Motion:** only report observed or source-confirmed motion. Separate entrance,
   state, scroll, and decorative motion.
9. **Responsive clues:** fluid sizing, reordering, collapse strategy, and likely
   pressure points. Do not claim other widths were tested unless they were.

## Diagnosis format

```text
Source: screenshot | public URL
Confidence: high | mixed | low, with reason
Composition: ...
Reading sequence: ...
Type roles: ...
Color roles: ...
Spacing and rhythm: ...
Component language: ...
Imagery and motion: ...
Transfer: three reusable principles
Do not copy: source-specific content and assets
Limits: checks the evidence cannot support
```

For a portable `design.md`, convert the diagnosis into semantic tokens, type
roles, layout ranges, component behavior, motion rules, and provenance. Do not
include source screenshots, source copy, or proprietary assets unless the user
owns and supplies them for that purpose.
