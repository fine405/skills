#!/usr/bin/env python3
"""Validate the repository's categorized skill structure."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SLUG_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*$")


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


def discover_skills() -> tuple[list[Path], list[str]]:
    errors: list[str] = []
    skill_dirs: list[Path] = []

    direct_skills = sorted(SKILLS_ROOT.glob("*/SKILL.md"))
    for skill_file in direct_skills:
        errors.append(
            f"{skill_file.relative_to(ROOT)}: skill must be inside a category directory"
        )

    categories = sorted(
        path
        for path in SKILLS_ROOT.iterdir()
        if path.is_dir() and path.name != "__pycache__" and not path.name.startswith(".")
    )
    for category in categories:
        if not SLUG_RE.fullmatch(category.name):
            errors.append(f"{category.relative_to(ROOT)}: category must be kebab-case")
        children = sorted(
            path
            for path in category.iterdir()
            if path.is_dir()
            and path.name != "__pycache__"
            and not path.name.startswith(".")
        )
        if not children:
            errors.append(f"{category.relative_to(ROOT)}: empty category")
        for child in children:
            if (child / "SKILL.md").exists():
                skill_dirs.append(child)
            else:
                errors.append(f"{child.relative_to(ROOT)}: missing SKILL.md")

    return skill_dirs, errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    text = skill_file.read_text(encoding="utf-8")
    meta = frontmatter(text)

    if not SLUG_RE.fullmatch(skill_dir.name):
        errors.append(f"{skill_dir.relative_to(ROOT)}: skill directory must be kebab-case")
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


def index_errors(skill_dirs: list[Path]) -> list[str]:
    errors: list[str] = []
    for index_name in ("README.md", "README.zh-CN.md"):
        index_text = (ROOT / index_name).read_text(encoding="utf-8")
        for skill_dir in skill_dirs:
            target = f"./{skill_dir.relative_to(ROOT).as_posix()}/"
            if target not in index_text:
                errors.append(f"{index_name}: missing skill link {target}")
    return errors


def synchronized_copy_errors() -> list[str]:
    groups = {
        "Hallmark linter": [
            ROOT / "skills" / "design" / "hallmark-build" / "scripts" / "hallmark_lint.py",
            ROOT / "skills" / "design" / "hallmark-audit" / "scripts" / "hallmark_lint.py",
        ],
        "chroma-key remover": [
            ROOT / "skills" / "aigc" / "imagegen-ansi" / "scripts" / "remove_chroma_key.py",
            ROOT / "skills" / "aigc" / "imagegen-transparent" / "scripts" / "remove_chroma_key.py",
        ],
    }
    errors: list[str] = []
    for label, paths in groups.items():
        missing = [path for path in paths if not path.exists()]
        if missing:
            for path in missing:
                errors.append(f"{path.relative_to(ROOT)}: missing synchronized {label} copy")
            continue
        digests = {hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
        if len(digests) != 1:
            errors.append(f"{label} copies have drifted")
    return errors


def main() -> int:
    skill_dirs, errors = discover_skills()
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    names = [skill_dir.name for skill_dir in skill_dirs]
    duplicates = sorted(name for name in set(names) if names.count(name) > 1)
    for name in duplicates:
        errors.append(f"duplicate skill name: {name}")

    errors.extend(index_errors(skill_dirs))
    errors.extend(synchronized_copy_errors())
    for markdown in ROOT.rglob("*.md"):
        if ".git" not in markdown.parts:
            errors.extend(markdown_link_errors(markdown))

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    category_count = len({skill_dir.parent for skill_dir in skill_dirs})
    print(
        f"Validated {len(skill_dirs)} skill(s) in {category_count} categories; "
        "metadata, indexes, links, and synchronized copies pass."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
