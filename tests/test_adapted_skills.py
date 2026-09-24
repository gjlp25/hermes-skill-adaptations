"""Static contract tests for the approved Hermes skill adaptation bundle."""
from __future__ import annotations

import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).parents[1]
SKILLS = ROOT / "skills"
APPROVED = {"theme-factory", "internal-comms", "canvas-design"}
EXCLUDED = {
    "academy-guide",
    "algorithmic-art",
    "brand-guidelines",
    "claude-api",
    "discernment-nudge",
    "doc-coauthoring",
    "docx",
    "frontend-design",
    "mcp-builder",
    "pdf",
    "pptx",
    "skill-creator",
    "slack-gif-creator",
    "web-artifacts-builder",
    "webapp-testing",
    "xlsx",
}


class AdaptedSkillsTests(unittest.TestCase):
    def test_only_the_three_approved_skill_directories_exist(self) -> None:
        self.assertEqual({path.name for path in SKILLS.iterdir() if path.is_dir()}, APPROVED)
        self.assertFalse(EXCLUDED & {path.name for path in SKILLS.iterdir() if path.is_dir()})

    def test_every_skill_has_narrow_hermes_frontmatter(self) -> None:
        for name in APPROVED:
            content = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            match = re.match(r"\A---\n(?P<frontmatter>.*?)\n---\n(?P<body>.+)", content, re.S)
            self.assertIsNotNone(match, name)
            assert match is not None
            frontmatter = match.group("frontmatter")
            self.assertRegex(frontmatter, rf"(?m)^name: {re.escape(name)}$")
            description = re.search(r"(?m)^description: (.+)$", frontmatter)
            self.assertIsNotNone(description, name)
            assert description is not None
            self.assertLessEqual(len(description.group(1).strip('"')), 60, name)
            self.assertTrue(description.group(1).strip('"').endswith("."), name)
            self.assertRegex(frontmatter, r"(?m)^license: Apache-2\.0$")
            self.assertRegex(frontmatter, r"(?m)^platforms: \[linux, macos, windows\]$")
            self.assertIn("Hermes", content, name)

    def test_provenance_security_and_rollback_are_present(self) -> None:
        for name in APPROVED:
            content = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("34040c9c568585f6929bedeaad110ad08f079624", content)
            self.assertIn("## Security and Privacy", content)
            self.assertIn("## Rollback", content)
            self.assertIn("do not", content.lower())

    def test_bundle_is_text_only_and_has_no_helper_or_network_code(self) -> None:
        forbidden_suffixes = {".py", ".js", ".sh", ".ttf", ".otf", ".pdf", ".png", ".woff", ".woff2"}
        for path in SKILLS.rglob("*"):
            self.assertFalse(path.is_file() and path.suffix.lower() in forbidden_suffixes, path)
        combined = "\n".join(path.read_text(encoding="utf-8") for path in SKILLS.rglob("*.md"))
        self.assertNotRegex(combined, r"https?://|`curl\b|`wget\b|`requests\b|fetch\(")
        self.assertNotIn("browser_vault", combined)
        self.assertNotIn("credential", combined.lower())

    def test_readme_documents_profile_default_staging(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("profile-default", readme.lower())
        self.assertIn("staging", readme.lower())
        self.assertIn("Apache-2.0", readme)


if __name__ == "__main__":
    unittest.main()
