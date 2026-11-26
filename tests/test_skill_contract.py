from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_FILES = (
    "SKILL.md",
    "work.md",
    "persona.md",
    "work_skill.md",
    "persona_skill.md",
    "README.md",
    "manifest.json",
    "meta.json",
)
OBSOLETE_MARKERS = (
    "首次执行前展示重构后的提示词",
    "refine_then_",
    "gpt-5.6-",
    "输入重构与 Goal 反应",
)


class SkillContractTests(unittest.TestCase):
    def test_canonical_files_exist(self) -> None:
        for name in CANONICAL_FILES:
            with self.subTest(name=name):
                self.assertTrue((ROOT / name).is_file())

    def test_metadata_and_manifest_are_consistent(self) -> None:
        meta = json.loads((ROOT / "meta.json").read_text(encoding="utf-8"))
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))

        self.assertEqual(meta["version"], "v2.5")
        self.assertEqual(meta["lifecycle"]["version"], "v2.5")
        self.assertEqual(meta["classification"]["language"], "zh")
        self.assertEqual(meta["schema_version"], "3")

        for entrypoint in manifest["entrypoints"].values():
            self.assertTrue((ROOT / entrypoint).is_file())

    def test_default_router_contains_required_contracts(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for heading in (
            "## Core contract",
            "## Request contract",
            "## Progressive loading",
            "## Skill routing",
            "## Execution loop",
            "## Explicit orchestration contract",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, text)

    def test_work_and_persona_are_canonical_documents(self) -> None:
        work = (ROOT / "work.md").read_text(encoding="utf-8")
        persona = (ROOT / "persona.md").read_text(encoding="utf-8")

        for heading in ("## 工程工作流", "## 学术工作流", "## 多代理协作规范", "## 完成定义"):
            self.assertIn(heading, work)
        for heading in ("## Layer 1：可证实的工作身份", "## Layer 2：表达风格", "## Layer 3：决策与判断"):
            self.assertIn(heading, persona)

        self.assertNotIn("## 自动输入重构与 Codex Goal 边界", work)
        self.assertNotIn("## 输入重构与 Goal 反应", persona)

    def test_thin_entrypoints_do_not_copy_canonical_body(self) -> None:
        work_entry = (ROOT / "work_skill.md").read_text(encoding="utf-8")
        persona_entry = (ROOT / "persona_skill.md").read_text(encoding="utf-8")

        self.assertIn("Read `SKILL.md` completely", work_entry)
        self.assertIn("Read `SKILL.md` completely", persona_entry)
        self.assertLess(len(work_entry), 2000)
        self.assertLess(len(persona_entry), 2000)

    def test_obsolete_prompt_and_model_rules_are_removed(self) -> None:
        checked = "\n".join(
            (ROOT / name).read_text(encoding="utf-8")
            for name in ("SKILL.md", "work.md", "persona.md", "work_skill.md", "persona_skill.md")
        )
        for marker in OBSOLETE_MARKERS:
            with self.subTest(marker=marker):
                self.assertNotIn(marker, checked)


if __name__ == "__main__":
    unittest.main()
