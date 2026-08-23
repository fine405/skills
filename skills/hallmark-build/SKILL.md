---
name: hallmark-build
description: Design and implement a distinctive web page, screen, or component while preserving an existing product's code, content, and design system. Use only when explicitly invoked as $hallmark-build for implementation work; do not use for audit-only reviews or design-source analysis.
---

# Hallmark Build

Build web interfaces that feel deliberately composed rather than assembled from
common AI defaults. Preserve the user's product and codebase; improve the
rendered experience without expanding the assignment.

Read [references/core-rules.md](references/core-rules.md) before editing. For a
page or multi-section screen, also read
[references/composition.md](references/composition.md). Skip the composition
catalog for a single component.

## Establish the target

1. Read applicable repository instructions, the requested route or component,
   existing tokens, global styles, fonts, framework conventions, and nearby UI.
2. State the intended user outcome, important assumptions, and exact files you
   expect to modify or create. Do not delete or replace existing files without
   explicit authorization.
3. Decide whether the request is component-scoped or page-scoped. Prefer the
   smaller scope when the prompt names one bounded element.
4. Ask one concise question only when a missing brand, content, or structural
   choice would materially change the result. Otherwise make a reversible
   assumption and disclose it.

## Choose a design fingerprint

For a page, choose a composition that fits the content instead of reflexively
using `centered hero -> three cards -> CTA -> four-column footer`. State the
chosen structure, type roles, color anchor, image strategy, and motion stance in
one short preview before implementation.

Use the existing product system when one exists. On a new surface, define only
the tokens the implementation needs. Do not create a second token system,
project memory file, preview file, or root-level stylesheet merely to satisfy
this skill.

For a component, design the states its semantics require:

- interactive controls: default, hover when relevant, `:focus-visible`, active,
  disabled, and any real loading/error/success states;
- informational components: empty, loading, error, and populated states only
  when the product can actually enter them;
- static decoration: no invented interactive states.

## Implement surgically

- Reuse established components and assets before adding new ones.
- Keep business logic, routing, data flow, ownership, copy intent, and brand
  unchanged unless the user requested those changes.
- Match the project's framework and styling conventions.
- Use semantic HTML and native controls before custom interaction code.
- Keep every changed line traceable to the requested outcome.
- Add no fabricated metrics, testimonials, customer logos, product screenshots,
  or unsupported claims.

## Verify before handoff

Verification happens after implementation; never print a quality score in the
pre-build preview.

1. Run the repository's relevant format, lint, type, unit, and build checks.
2. Run the bundled deterministic scan on the changed interface files:

   ```bash
   python3 <skill-dir>/scripts/hallmark_lint.py <changed-path> [...]
   ```

   Treat findings as review input. Fix confirmed issues and explain any
   intentional exceptions; a clean static scan does not prove visual quality.
3. Render the changed surface when a browser or simulator is available. Check
   the real result at a representative desktop viewport and at 320, 375, 414,
   and 768 CSS pixels when the surface is responsive.
4. Check keyboard order and focus, text and focus contrast, reduced motion,
   overflow, long content, empty/error states, and the primary task.
5. Do not claim a viewport, accessibility, contrast, or motion check passed
   unless it was actually performed. Name unavailable checks as gaps.

Return the working result first, followed by the chosen fingerprint, changed
files, exact verification results, and remaining risks.

This skill is adapted from
[Nutlope/hallmark](https://github.com/Nutlope/hallmark) at commit
`13ac0ec7e148655948100b6396439e481361d690`; see `UPSTREAM_LICENSE`.
