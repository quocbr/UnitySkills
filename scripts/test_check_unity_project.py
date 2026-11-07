"""Behavior checks for the vendored, read-only Unity asset checker."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "unity-skills" / "scripts" / "check_unity_project.py"


class UnityAssetCheckerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix=".asset-check-", dir=ROOT)
        self.assertTrue(Path(self.temp.name).resolve().is_relative_to(ROOT.resolve()))
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name)
        (self.project / "Assets").mkdir()
        (self.project / "ProjectSettings").mkdir()
        (self.project / "Packages").mkdir()
        (self.project / "Packages" / "manifest.json").write_text(
            '{"dependencies": {}}', encoding="utf-8"
        )

    def asset(self, name, content, guid=None):
        path = self.project / "Assets" / name
        path.write_text(content, encoding="utf-8")
        if guid is not None:
            path.with_name(path.name + ".meta").write_text(
                f"fileFormatVersion: 2\nguid: {guid}\n", encoding="utf-8"
            )
        return path

    def scan(self):
        result = subprocess.run(
            [sys.executable, str(CHECKER), str(self.project), "--json"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertFalse(result.stderr, result.stderr)
        return result.returncode, json.loads(result.stdout)

    def test_clean_project_and_new_asset_warning(self):
        self.asset("Player.cs", "public class Player : MonoBehaviour {}", "a" * 32)
        code, report = self.scan()
        self.assertEqual((code, report["error_count"]), (0, 0))
        self.asset("New.asset", "%YAML 1.1\n")
        code, report = self.scan()
        self.assertEqual(code, 0)
        self.assertIn("missing-meta", {w["code"] for w in report["warnings"]})

    def test_duplicate_guid_is_error(self):
        self.asset("A.asset", "%YAML 1.1\n", "a" * 32)
        self.asset("B.asset", "%YAML 1.1\n", "a" * 32)
        code, report = self.scan()
        self.assertEqual(code, 1)
        self.assertIn("duplicate-guid", {e["code"] for e in report["errors"]})

    def test_rename_without_meta_is_detected(self):
        self.asset("Old.asset", "%YAML 1.1\n", "b" * 32)
        (self.project / "Assets" / "Old.asset").rename(self.project / "Assets" / "New.asset")
        code, report = self.scan()
        self.assertEqual(code, 1)
        self.assertIn("moved-without-meta", {e["code"] for e in report["errors"]})

    def test_missing_script_depends_on_package_resolution(self):
        self.asset(
            "Scene.unity",
            "%YAML 1.1\n--- !u!114 &1\nMonoBehaviour:\n"
            "  m_Script: {fileID: 11500000, guid: " + "c" * 32 + ", type: 3}\n",
            "d" * 32,
        )
        code, report = self.scan()
        self.assertEqual(code, 1)
        self.assertIn("missing-script", {e["code"] for e in report["errors"]})
        (self.project / "Packages" / "manifest.json").write_text(
            '{"dependencies": {"com.example.unavailable": "1.0.0"}}',
            encoding="utf-8",
        )
        code, report = self.scan()
        self.assertEqual(code, 0)
        self.assertIn("missing-script", {w["code"] for w in report["warnings"]})


if __name__ == "__main__":
    unittest.main()
