"""Verify provenance without any package checkouts or network access."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import source_revisions


class SourceRevisionsTest(unittest.TestCase):
    def test_pages_and_sibling_modes_need_only_site_and_content(self):
        for sibling_mode in (False, True):
            with self.subTest(sibling_mode=sibling_mode), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary).resolve()
                site = root / "bagelquant.github.io"
                content = root / "bagelquant-content" if sibling_mode else site / "content"
                site.mkdir()
                content.mkdir()
                output = root / "evidence" / "source-revisions.json"
                arguments = ["source_revisions.py", "--output", str(output)]
                if sibling_mode:
                    arguments += ["--workspace", str(root)]
                expected = {site: "a" * 40, content: "b" * 40}

                def git(command, *, cwd, text):
                    self.assertTrue(text)
                    self.assertIn(cwd, expected)
                    if command == ["git", "rev-parse", "HEAD"]:
                        return expected[cwd] + "\n"
                    self.assertEqual(command, ["git", "status", "--porcelain", "--untracked-files=no"])
                    return " M index.md\n" if cwd == site else ""

                with (
                    patch.object(source_revisions, "__file__", str(site / "scripts" / "source_revisions.py")),
                    patch("sys.argv", arguments),
                    patch.object(source_revisions.subprocess, "check_output", side_effect=git) as calls,
                ):
                    source_revisions.main()
                self.assertEqual(calls.call_count, 4)
                self.assertEqual(json.loads(output.read_text()), {
                    "schema": "bagelquant-site-sources.v1",
                    "sources": {
                        "bagelquant.github.io": {"commit": "a" * 40, "tracked_changes": True},
                        "bagelquant-content": {"commit": "b" * 40, "tracked_changes": False},
                    },
                })


if __name__ == "__main__":
    unittest.main()
