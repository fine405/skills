# Audit checklist

Use only the lenses relevant to the surface and its user goal.

## Task and structure

- Is the primary task discoverable and does the hierarchy support it?
- Does the information shape justify the composition, or has content been forced
  into a centered hero, equal cards, CTA, and generic footer?
- Are navigation and exit paths proportional to the real information
  architecture?
- Are empty, loading, error, success, and recovery states present where the
  product can enter them?

## Trust and content

- Are quantitative claims, logos, testimonials, screenshots, and capabilities
  supplied or sourced rather than invented?
- Does the copy say what happens next, especially around forms and destructive
  or irreversible actions?
- Do decorative assets masquerade as real product evidence?

## Visual system

- Do type roles, tokens, spacing, radii, dividers, images, and motion align with
  the existing product system?
- Is contrast and emphasis concentrated on important decisions?
- Are repeated sections genuinely different in purpose, not arbitrary style
  changes or color-swapped templates?

## Interaction and accessibility

- Semantic structure and reading order.
- Keyboard access, visible focus, target size, and control labels.
- Instructions, validation, error association, and recovery.
- Text, icon, and focus contrast against computed backgrounds.
- State-change announcements and motion alternatives.
- Responsive reflow, zoom resilience, long content, and localization pressure.

## Performance and implementation

- LCP media priority, dimensions, format, and static fallback.
- Layout-triggering animation, unbounded observers/listeners, and unnecessary
  client code.
- CSS values that bypass tokens, broad transitions, hidden overflow, or brittle
  intrinsic grid sizing.

## Evidence limits

Screenshots cannot confirm semantics, keyboard behavior, announcements, or all
responsive widths. Source cannot confirm final rhythm, contrast against rendered
layers, clipping, or motion feel. Name the missing verification rather than
converting uncertainty into a pass.
