import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class FoundationTests(unittest.TestCase):
    def test_required_files_exist(self):
        for path in [
            "config/system.json",
            "config/providers.json",
            "config/limits.json",
            "engine/run.py",
            "engine/research.py",
            "engine/content.py",
            "engine/validator.py",
            "engine/decision.py",
            "engine/logger.py",
        ]:
            self.assertTrue((ROOT / path).is_file(), path)

    def test_zero_payment_guard(self):
        config = json.loads((ROOT / "config/system.json").read_text(encoding="utf-8"))
        providers = json.loads((ROOT / "config/providers.json").read_text(encoding="utf-8"))
        self.assertTrue(config["no_payment_guard"])
        self.assertEqual(config["budget_thb"], 0)
        self.assertFalse(providers["paid_provider_allowed"])

    def test_config_is_valid(self):
        config = json.loads((ROOT / "config/system.json").read_text(encoding="utf-8"))
        self.assertIsInstance(config["rss_feeds"], list)
        self.assertIsInstance(config["keywords"], list)
        self.assertGreaterEqual(config["max_drafts_per_run"], 1)

if __name__ == "__main__":
    unittest.main()
