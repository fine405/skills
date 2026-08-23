#!/usr/bin/env python3
"""Validate repository skill structure without third-party dependencies."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    try:
        header = text.split("---\n", 2)[1]
    except IndexError:
        return {}
    values: dict[str, str] = {}
    for line in header.splitlines():
        match = re.match(r"([a-zA-Z_][\w-]*):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"')
    return values


def markdown_link_errors(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        target = target.split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        if not (path.parent / target).exists():
            errors.append(f"{path.relative_to(ROOT)}: missing link target {target}")
    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return [f"{skill_dir.relative_to(ROOT)}: missing SKILL.md"]
    text = skill_file.read_text(encoding="utf-8")
    meta = frontmatter(text)
    if meta.get("name") != skill_dir.name:
        errors.append(
            f"{skill_file.relative_to(ROOT)}: name must match folder {skill_dir.name}"
        )
    if not meta.get("description"):
        errors.append(f"{skill_file.relative_to(ROOT)}: missing description")
    if re.search(r"\bTODO\b|\[TODO", text, re.IGNORECASE):
        errors.append(f"{skill_file.relative_to(ROOT)}: unfinished TODO marker")

    agent_file = skill_dir / "agents" / "openai.yaml"
    if not agent_file.exists():
        errors.append(f"{skill_dir.relative_to(ROOT)}: missing agents/openai.yaml")
    else:
        agent_text = agent_file.read_text(encoding="utf-8")
        if f"${skill_dir.name}" not in agent_text:
            errors.append(
                f"{agent_file.relative_to(ROOT)}: default prompt must mention ${skill_dir.name}"
            )
    return errors


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    for markdown in ROOT.rglob("*.md"):
        if ".git" not in markdown.parts:
            errors.extend(markdown_link_errors(markdown))

    lint_paths = [
        ROOT / "skills" / "hallmark-build" / "scripts" / "hallmark_lint.py",
        ROOT / "skills" / "hallmark-audit" / "scripts" / "hallmark_lint.py",
    ]
    if all(path.exists() for path in lint_paths):
        digests = {
            hashlib.sha256(path.read_bytes()).hexdigest() for path in lint_paths
        }
        if len(digests) != 1:
            errors.append("Hallmark build and audit linter copies have drifted")

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skill(s); links and Hallmark linter copies pass.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
