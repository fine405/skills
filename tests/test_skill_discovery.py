from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import validate_repo


class SkillDiscoveryTests(unittest.TestCase):
    def test_nested_skill_entry_is_rejected_but_reference_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = root / 'skills' / 'apple-platform' / 'example'
            (skill / 'apple').mkdir(parents=True)
            (skill / 'agents').mkdir()
            content = '---\nname: example\ndescription: Example guidance.\n---\n'
            (skill / 'SKILL.md').write_text(content)
            (skill / 'agents/openai.yaml').write_text('default_prompt: Use $example\n')
            nested = skill / 'apple/SKILL.md'
            nested.write_text(content)
            with patch.object(validate_repo, 'ROOT', root):
                errors = validate_repo.validate_skill(skill)
                self.assertEqual(len(errors), 1)
                self.assertIn('nested SKILL.md causes duplicate discovery', errors[0])
                nested.rename(skill / 'apple/guide.md')
                self.assertEqual(validate_repo.validate_skill(skill), [])
