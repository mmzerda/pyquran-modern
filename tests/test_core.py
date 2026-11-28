import importlib.util
import pathlib
import sys
import types
import unittest
from unittest.mock import patch

class CoreContractTests(unittest.TestCase):
    def setUp(self):
        upstream = types.ModuleType("pyquran")
        upstream.quran = types.SimpleNamespace(
            get_verse=lambda s, v, with_tashkeel=True: "fixture" if (s, v) == (1, 1) else ""
        )
        path = pathlib.Path(__file__).resolve().parents[1] / "pyquran_modern" / "core.py"
        spec = importlib.util.spec_from_file_location("core_under_test", path)
        self.core = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {"pyquran": upstream}):
            spec.loader.exec_module(self.core)

    def test_index_complete(self):
        self.assertEqual(len(self.core.SURAH_MAP), 114)
        self.assertEqual(set(self.core.SURAH_MAP.values()), set(range(1, 115)))

    def test_regression_boundaries(self):
        for name, number in [("نوح", 71), ("المرسلات", 77), ("النبأ", 78), ("الفيل", 105), ("الناس", 114)]:
            self.assertEqual(self.core.SURAH_MAP[name], number)

    def test_valid_delegation(self):
        self.assertEqual(self.core.get_verse_text(1, 1), "fixture")
        self.assertEqual(self.core.get_verse_by_name("الفاتحة", 1), "fixture")

    def test_invalid_and_missing_verses(self):
        for args in [(0, 1), (115, 1), (1, 0), (1, 999), (True, 1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                self.core.get_verse_text(*args)

    def test_unknown_name(self):
        with self.assertRaises(ValueError):
            self.core.get_verse_by_name("unknown", 1)

    def test_unsupported_root(self):
        with self.assertRaises(NotImplementedError):
            self.core.get_word_root("الحمد")

if __name__ == "__main__":
    unittest.main()
