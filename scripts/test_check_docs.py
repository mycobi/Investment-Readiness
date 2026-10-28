from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from check_docs import check

class DocumentationChecks(unittest.TestCase):
    def test_valid_relative_link(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "target.md").write_text("# Target\n", encoding="utf-8")
            (root / "README.md").write_text("[Target](target.md)\n", encoding="utf-8")
            self.assertEqual(check(root), [])

    def test_missing_link_and_malformed_table(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "README.md").write_text(
                "[Missing](absent.md)\n\n| A | B |\n| --- | --- |\n| one |\n",
                encoding="utf-8")
            errors = check(root)
            self.assertTrue(any("missing internal target" in item for item in errors))
            self.assertTrue(any("table column" in item for item in errors))

    def test_unclosed_fence_and_em_dash(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "README.md").write_text("Text\u2014text\n" + chr(96)*3 + "\nunclosed\n", encoding="utf-8")
            errors = check(root)
            self.assertTrue(any("em dash" in item for item in errors))
            self.assertTrue(any("unclosed" in item for item in errors))

if __name__ == "__main__":
    unittest.main()
