---
name: hallmark-audit
description: Audit existing web UI code and rendered evidence for generic AI patterns, hierarchy, interaction, responsiveness, accessibility, and content-trust risks. Use only when explicitly invoked as $hallmark-audit; report findings without editing unless the user separately requests implementation.
---

# Hallmark Audit

Return an evidence-backed punch list, not a redesign pitch. Read
[references/core-rules.md](references/core-rules.md) and
[references/audit-checklist.md](references/audit-checklist.md) before grading.

## Establish evidence

1. Identify the surface, user goal, relevant files, and expected states.
2. Read applicable repository instructions and existing design-system sources.
   Judge drift against the product's own system before applying general taste.
3. Run the bundled static scan when local code is available:

   ```bash
   python3 <skill-dir>/scripts/hallmark_lint.py <target-path> [...]
   ```

4. Capture the rendered flow when a browser, simulator, Storybook, screenshot,
   or supplied image is available. Inspect each accepted state before using it
   as evidence.
5. If rendering is unavailable, label the result a code audit. Do not claim
   visual, responsive, keyboard, contrast, or assistive-technology behavior was
   confirmed from source alone.

Static findings are leads, not verdicts. Confirm them in context and discard
false positives.

## Report findings

Order findings by impact on the primary task:

- **critical:** blocks the task, makes content unusable, creates false trust, or
  introduces a serious accessibility failure;
- **major:** materially weakens comprehension, navigation, state recovery,
  responsive behavior, or the product's visual identity;
- **minor:** local inconsistency or polish issue with limited user impact.

For every finding include:

1. **Evidence** — screenshot/state or file and tight line range.
2. **Problem** — the observed behavior or named pattern.
3. **Impact** — what becomes harder or misleading for the user.
4. **Fix** — the smallest concrete correction; avoid prescribing a full redesign
   when a local change resolves it.
5. **Confidence** — confirmed, likely, or needs runtime verification.

Also report strengths worth preserving, the audited steps with their general
health, exact checks run, and evidence limits. End with counts by severity. Do
not edit files during an audit-only request.

This skill is adapted from
[Nutlope/hallmark](https://github.com/Nutlope/hallmark) at commit
`13ac0ec7e148655948100b6396439e481361d690`; see `UPSTREAM_LICENSE`.
