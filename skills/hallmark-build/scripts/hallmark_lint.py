#!/usr/bin/env python3
"""Static UI checks for Hallmark skills.

The scan intentionally reports only source-level signals. It never claims that
visual quality, accessibility, contrast, or responsive behavior passed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


SUPPORTED = {
    ".astro",
    ".css",
    ".htm",
    ".html",
    ".jsx",
    ".less",
    ".scss",
    ".svelte",
    ".tsx",
    ".vue",
}
SKIP_DIRS = {
    ".git",
    ".next",
    ".nuxt",
    ".output",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "vendor",
}
CSS_LIKE = {".css", ".less", ".scss"}
MANUAL_CHECKS = [
    "Render the primary task at a representative desktop viewport.",
    "For responsive surfaces, inspect 320, 375, 414, and 768 CSS-pixel widths.",
    "Complete the primary task with keyboard-only navigation and visible focus.",
    "Measure text, icon, control, and focus contrast against computed backgrounds.",
    "Enable reduced motion and verify media, transitions, and scroll effects.",
    "Test long content plus real empty, loading, error, success, and recovery states.",
    "Confirm metrics, logos, testimonials, screenshots, and capabilities are sourced.",
    "Judge hierarchy, rhythm, and structural fit from the rendered result.",
]


@dataclass(frozen=True)
class Finding:
    rule: str
    severity: str
    path: str
    line: int
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan web UI source for deterministic Hallmark risk signals."
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to scan")
    parser.add_argument(
        "--format", choices=("text", "json"), default="text", dest="output_format"
    )
    parser.add_argument(
        "--fail-on-warning",
        action="store_true",
        help="Exit non-zero when warnings are present",
    )
    return parser.parse_args()


def iter_source_files(inputs: Iterable[str]) -> tuple[list[Path], list[str]]:
    files: set[Path] = set()
    missing: list[str] = []
    for raw in inputs:
        path = Path(raw).expanduser()
        if not path.exists():
            missing.append(raw)
            continue
        if path.is_file():
            if path.suffix.lower() in SUPPORTED:
                files.add(path.resolve())
            continue
        for candidate in path.rglob("*"):
            if not candidate.is_file() or candidate.suffix.lower() not in SUPPORTED:
                continue
            if any(part in SKIP_DIRS for part in candidate.parts):
                continue
            files.add(candidate.resolve())
    return sorted(files), missing


def line_at(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(Path.cwd()))
    except ValueError:
        return str(path)


def strip_css_comments(text: str) -> str:
    def preserve_lines(match: re.Match[str]) -> str:
        value = match.group(0)
        return "".join("\n" if char == "\n" else " " for char in value)

    return re.sub(r"/\*.*?\*/", preserve_lines, text, flags=re.DOTALL)


def scan_css(path: Path, text: str, line_offset: int = 0) -> list[Finding]:
    findings: list[Finding] = []
    clean = strip_css_comments(text)
    shown = display_path(path)

    rules = [
        (
            "HM001",
            "warning",
            r"\btransition\s*:\s*all\b|\btransition-all\b",
            "Broad transition animates unrelated properties; name the intended properties.",
        ),
        (
            "HM002",
            "warning",
            r"\boverflow-x\s*:\s*hidden\b",
            "Horizontal overflow is hidden rather than resolved; inspect clipping and sticky behavior.",
        ),
    ]
    for rule, severity, pattern, message in rules:
        for match in re.finditer(pattern, clean, flags=re.IGNORECASE):
            findings.append(
                Finding(
                    rule,
                    severity,
                    shown,
                    line_offset + line_at(clean, match.start()),
                    message,
                )
            )

    if re.search(r"\b(?:animation|transition)\s*:", clean, re.IGNORECASE) or re.search(
        r"@keyframes\b", clean, re.IGNORECASE
    ):
        if "prefers-reduced-motion" not in clean:
            findings.append(
                Finding(
                    "HM003",
                    "warning",
                    shown,
                    line_offset + 1,
                    "Motion is declared without a prefers-reduced-motion fallback in this file.",
                )
            )

    if re.search(r"\boutline\s*:\s*(?:0|none)\b", clean, re.IGNORECASE) and not re.search(
        r":focus-visible\b", clean, re.IGNORECASE
    ):
        findings.append(
            Finding(
                "HM004",
                "warning",
                shown,
                line_offset + 1,
                "Outline is removed without a focus-visible replacement in this file.",
            )
        )

    color_pattern = re.compile(
        r"#[0-9a-f]{3,8}\b|\b(?:rgb|rgba|hsl|hsla|oklch|oklab)\s*\(",
        re.IGNORECASE,
    )
    for number, line in enumerate(clean.splitlines(), start=1):
        if not color_pattern.search(line):
            continue
        if re.search(r"--[\w-]+\s*:", line):
            continue
        findings.append(
            Finding(
                "HM005",
                "warning",
                shown,
                line_offset + number,
                "Raw color appears outside a custom-property declaration; prefer an existing semantic token.",
            )
        )

    for match in re.finditer(r"([^{}]+)\{([^{}]*)\}", clean, flags=re.DOTALL):
        selector, body = match.groups()
        if not re.search(r"font-style\s*:\s*italic\b", body, re.IGNORECASE):
            continue
        if re.search(
            r"\bh[1-6]\b|(?:title|heading|display|wordmark|headline|stat)",
            selector,
            re.IGNORECASE,
        ):
            findings.append(
                Finding(
                    "HM006",
                    "warning",
                    shown,
                    line_offset + line_at(clean, match.start()),
                    "A heading/display selector uses italic; confirm this is an intentional brand choice.",
                )
            )

    for match in re.finditer(r"font-family\s*:\s*([^;}{]+)", clean, re.IGNORECASE):
        line_start = clean.rfind("\n", 0, match.start()) + 1
        prefix = clean[line_start : match.start()]
        value = match.group(1)
        if "var(" in value or re.search(r"--[\w-]+\s*:\s*$", prefix):
            continue
        findings.append(
            Finding(
                "HM007",
                "warning",
                shown,
                line_offset + line_at(clean, match.start()),
                "Font family bypasses a semantic font token; confirm it belongs to the active system.",
            )
        )

    return findings


def scan_markup(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []
    shown = display_path(path)

    for match in re.finditer(r"<(?:img|IMG|Image)\b[^>]*>", text, re.DOTALL):
        if re.search(r"\balt\s*=", match.group(0), re.IGNORECASE):
            continue
        findings.append(
            Finding(
                "HM101",
                "error",
                shown,
                line_at(text, match.start()),
                "Image has no alt attribute; provide useful alternative text or alt=\"\" for decoration.",
            )
        )

    for match in re.finditer(r"<video\b[^>]*>", text, re.IGNORECASE | re.DOTALL):
        tag = match.group(0)
        if re.search(r"\bautoplay\b", tag, re.IGNORECASE) and re.search(
            r"\bloop\b", tag, re.IGNORECASE
        ):
            if not re.search(r"\bposter\s*=", tag, re.IGNORECASE):
                findings.append(
                    Finding(
                        "HM102",
                        "warning",
                        shown,
                        line_at(text, match.start()),
                        "Autoplaying loop has no poster; provide a static reduced-motion fallback.",
                    )
                )

    for match in re.finditer(r"<svg\b[^>]*>", text, re.IGNORECASE | re.DOTALL):
        tag = match.group(0)
        if re.search(r"\baria-(?:label|labelledby|hidden)\s*=", tag, re.IGNORECASE):
            continue
        findings.append(
            Finding(
                "HM103",
                "warning",
                shown,
                line_at(text, match.start()),
                "SVG has no accessible name or aria-hidden marker; determine whether it is content or decoration.",
            )
        )

    ids: dict[str, int] = {}
    for match in re.finditer(r"\bid\s*=\s*[\"']([^\"']+)[\"']", text, re.IGNORECASE):
        value = match.group(1)
        line = line_at(text, match.start())
        if value in ids:
            findings.append(
                Finding(
                    "HM104",
                    "error",
                    shown,
                    line,
                    f'Duplicate id "{value}"; first occurrence is on line {ids[value]}.',
                )
            )
        else:
            ids[value] = line

    for match in re.finditer(
        r"<(?:div|span)\b[^>]*\brole\s*=\s*[\"']button[\"'][^>]*>",
        text,
        re.IGNORECASE | re.DOTALL,
    ):
        if re.search(r"\btabIndex\s*=|\btabindex\s*=", match.group(0)):
            continue
        findings.append(
            Finding(
                "HM105",
                "warning",
                shown,
                line_at(text, match.start()),
                "Non-native button role has no explicit keyboard focus; prefer a native button.",
            )
        )

    return findings


def scan_file(path: Path) -> list[Finding]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [
            Finding(
                "HM000",
                "warning",
                display_path(path),
                1,
                "File is not valid UTF-8 and was not scanned.",
            )
        ]

    findings: list[Finding] = []
    if path.suffix.lower() in CSS_LIKE:
        findings.extend(scan_css(path, text))
    else:
        findings.extend(scan_markup(path, text))
        for block in re.finditer(r"<style\b[^>]*>(.*?)</style>", text, re.I | re.S):
            line_offset = text.count("\n", 0, block.start(1))
            findings.extend(scan_css(path, block.group(1), line_offset=line_offset))
    return findings


def emit_text(files: list[Path], findings: list[Finding]) -> None:
    print(f"Hallmark static scan: {len(files)} file(s)")
    if findings:
        for finding in findings:
            print(
                f"{finding.path}:{finding.line}: "
                f"{finding.severity} {finding.rule} {finding.message}"
            )
    else:
        print("No static findings.")
    errors = sum(item.severity == "error" for item in findings)
    warnings = sum(item.severity == "warning" for item in findings)
    print(f"Summary: {errors} error(s), {warnings} warning(s)")
    print("Manual checks still required:")
    for check in MANUAL_CHECKS:
        print(f"- {check}")


def main() -> int:
    args = parse_args()
    files, missing = iter_source_files(args.paths)
    if missing:
        for path in missing:
            print(f"Path does not exist: {path}", file=sys.stderr)
        return 2
    if not files:
        print("No supported UI source files found.", file=sys.stderr)
        return 2

    findings = sorted(
        (item for path in files for item in scan_file(path)),
        key=lambda item: (item.path, item.line, item.rule),
    )
    if args.output_format == "json":
        payload = {
            "files_scanned": len(files),
            "findings": [asdict(item) for item in findings],
            "summary": {
                "errors": sum(item.severity == "error" for item in findings),
                "warnings": sum(item.severity == "warning" for item in findings),
            },
            "manual_checks": MANUAL_CHECKS,
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        emit_text(files, findings)

    has_errors = any(item.severity == "error" for item in findings)
    has_warnings = any(item.severity == "warning" for item in findings)
    return int(has_errors or (args.fail_on_warning and has_warnings))


if __name__ == "__main__":
    raise SystemExit(main())
