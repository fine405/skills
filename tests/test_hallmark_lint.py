from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_LINT = ROOT / "skills" / "hallmark-build" / "scripts" / "hallmark_lint.py"
AUDIT_LINT = ROOT / "skills" / "hallmark-audit" / "scripts" / "hallmark_lint.py"


class HallmarkLintTests(unittest.TestCase):
    def run_lint(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(BUILD_LINT), *args],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_build_and_audit_copies_match(self) -> None:
        self.assertEqual(BUILD_LINT.read_bytes(), AUDIT_LINT.read_bytes())

    def test_clean_fixture_has_no_static_findings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "page.html").write_text(
                '<main><img src="owned.png" alt="Product dashboard">'
                '<svg aria-hidden="true"><image href="texture.png"></image></svg>'
                '<button>Save</button></main>',
                encoding="utf-8",
            )
            (root / "page.css").write_text(
                ":root { --color-ink: #18202a; --font-body: system-ui; }\n"
                "button { color: var(--color-ink); font-family: var(--font-body); }\n",
                encoding="utf-8",
            )
            result = self.run_lint("--format", "json", str(root))
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["summary"], {"errors": 0, "warnings": 0})
            self.assertTrue(payload["manual_checks"])

    def test_problem_fixture_reports_deterministic_rules(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "page.html").write_text(
                '<img src="missing-alt.png"><svg></svg>'
                '<div id="same"></div><span id="same"></span>'
                '<div role="button">Open</div>'
                '<video autoplay loop></video>',
                encoding="utf-8",
            )
            (root / "page.css").write_text(
                "h1 { font-style: italic; color: #fff; font-family: Inter; }\n"
                ".card { transition: all 200ms; outline: none; overflow-x: hidden; }\n",
                encoding="utf-8",
            )
            result = self.run_lint("--format", "json", str(root))
            self.assertEqual(result.returncode, 1)
            payload = json.loads(result.stdout)
            rules = {item["rule"] for item in payload["findings"]}
            self.assertTrue(
                {
                    "HM001",
                    "HM002",
                    "HM003",
                    "HM004",
                    "HM005",
                    "HM006",
                    "HM007",
                    "HM101",
                    "HM102",
                    "HM103",
                    "HM104",
                    "HM105",
                }.issubset(rules)
            )

    def test_warning_exit_is_configurable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            css = Path(tmp) / "page.css"
            css.write_text(".card { transition: all 200ms; }", encoding="utf-8")
            self.assertEqual(self.run_lint(str(css)).returncode, 0)
            self.assertEqual(
                self.run_lint("--fail-on-warning", str(css)).returncode, 1
            )

    def test_inline_style_uses_document_line_numbers(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            html = Path(tmp) / "page.html"
            html.write_text(
                "<html>\n<head>\n<style>\n.card { transition: all 200ms; }\n"
                "</style>\n</head>\n</html>\n",
                encoding="utf-8",
            )
            result = self.run_lint("--format", "json", str(html))
            self.assertEqual(result.returncode, 0)
            payload = json.loads(result.stdout)
            finding = next(
                item for item in payload["findings"] if item["rule"] == "HM001"
            )
            self.assertEqual(finding["line"], 4)


if __name__ == "__main__":
    unittest.main()
