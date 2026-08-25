# Repository guidance

## Purpose

Maintain a portable collection of independently installable agent skills. Keep
the repository easy to scan as a catalog and keep every individual skill usable
when copied or symlinked on its own.

## Structure

```text
skills/
  <category>/
    <skill-name>/
      SKILL.md
      agents/openai.yaml
      references/   # optional, loaded only when needed
      scripts/      # optional, deterministic reusable tools
      examples/     # optional, complete working examples
      assets/       # optional, output resources and templates
```

Use a short, stable, kebab-case category and skill name. Add a category only
when it has a clear long-term meaning; do not create a new category merely for
one variation of an existing skill.

## Skill contract

- Start `SKILL.md` with YAML frontmatter containing `name` and `description`.
- Match `name` exactly to the skill directory.
- Make `description` specific enough to route real user requests. Add negative
  trigger conditions when nearby skills could be confused.
- Keep the main workflow in `SKILL.md`; move detailed reference material into
  `references/` and deterministic repeated work into `scripts/`.
- Keep all runtime files inside the skill. Do not introduce cross-skill file
  dependencies, because users can install one skill at a time.
- Include `agents/openai.yaml`; its default prompt must explicitly mention the
  skill as `$<skill-name>`.
- Avoid machine-specific absolute paths, hidden network dependencies, and claims
  of validation that the skill did not actually perform.

## Repository maintenance

When adding, renaming, moving, or removing a skill:

1. Update both `README.md` and `README.zh-CN.md` with the same skill inventory.
2. Preserve third-party license files inside independently installable skills
   and update `THIRD_PARTY_NOTICES.md` when attribution changes.
3. If a utility is intentionally duplicated to keep skills self-contained, add
   the copies to the synchronization check in `scripts/validate_repo.py`.
4. Make the smallest change needed; do not reformat or rewrite unrelated skills.

## Verification

Run all repository gates before committing:

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
python3 -m compileall -q skills scripts tests
npx skills add . --list
```

The final command must discover every skill by its frontmatter `name` despite
the category layer.
