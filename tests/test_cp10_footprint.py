import json
import os
import tempfile
import unittest
from pathlib import Path

from tools.cp10_footprint import (
    collect,
    lockfile_snapshot_evidence,
    main,
    measure_tree,
    pnpm_store_entries,
    yaml_top_level_mapping_count,
)


class CP10FootprintTests(unittest.TestCase):
    def test_tree_uses_lstat_does_not_follow_links_and_deduplicates_hardlinks(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root = base / "tree"
            outside = base / "outside"
            root.mkdir()
            outside.mkdir()
            original = root / "original"
            original.write_bytes(b"content")
            os.link(original, root / "hardlink")
            (outside / "not-counted").write_bytes(b"outside content")
            (root / "external-link").symlink_to(outside, target_is_directory=True)

            result = measure_tree(root)
            expected_logical = (
                root.lstat().st_size
                + original.lstat().st_size
                + (root / "external-link").lstat().st_size
            )
            expected_allocated = (
                root.lstat().st_blocks
                + original.lstat().st_blocks
                + (root / "external-link").lstat().st_blocks
            ) * 512
            self.assertEqual(result["logical_bytes"], expected_logical)
            self.assertEqual(result["allocated_bytes"], expected_allocated)
            self.assertEqual(result["regular_file_count"], 1)
            self.assertEqual(result["directory_count"], 1)
            self.assertEqual(result["symlink_count"], 1)
            self.assertEqual(result["duplicate_hardlink_count"], 1)

    def test_tree_exclusions_are_root_relative_and_remove_subtrees(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "dist").mkdir()
            (root / "dist/output").write_text("excluded")
            (root / "nested").mkdir()
            (root / "nested/dist").mkdir()
            (root / "nested/dist/source").write_text("included")

            result = measure_tree(root, ("dist",))
            self.assertEqual(result["regular_file_count"], 1)
            self.assertEqual(result["directory_count"], 3)
            self.assertEqual(result["exclusions"], ["dist"])

    def test_pnpm_store_count_has_a_narrow_immediate_child_definition(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Path(directory)
            (store / "pkg-a@1.0.0").mkdir()
            (store / "pkg-b@2.0.0").mkdir()
            (store / "node_modules").mkdir()
            (store / "lock.yaml").write_text("lockfileVersion: 9\n")
            (store / "linked").symlink_to(store / "pkg-a@1.0.0")
            self.assertEqual(pnpm_store_entries(store)["count"], 2)

    def test_lockfile_snapshot_parser_is_conservative(self):
        lockfile = """\
lockfileVersion: '9.0'
packages:
  pkg-a@1.0.0:
    resolution: {integrity: value}
snapshots:
  '@scope/pkg@2.0.0':
    dependencies:
      pkg-a: 1.0.0
  pkg-a@1.0.0: {}
"""
        self.assertEqual(yaml_top_level_mapping_count(lockfile, "snapshots"), 2)
        self.assertIsNone(
            yaml_top_level_mapping_count("snapshots:\n  - not-a-mapping\n", "snapshots")
        )
        self.assertIsNone(
            yaml_top_level_mapping_count("snapshots:\n  - package: value\n", "snapshots")
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pnpm-lock.yaml"
            path.write_text(lockfile)
            evidence = lockfile_snapshot_evidence(path)
            self.assertIsNotNone(evidence)
            self.assertEqual(evidence["source_section"], "snapshots")
            self.assertEqual(evidence["count"], 2)
            path.write_text("packages:\n  pkg@1: {}\nsnapshots:\n  - bad: value\n")
            self.assertIsNone(lockfile_snapshot_evidence(path))

    def test_collect_separates_all_requested_footprints_and_counts_packages(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            nift = root / "nift"
            astro = root / "astro"
            nift.mkdir()
            astro.mkdir()
            (nift / "source.txt").write_text("source")
            (nift / "public").mkdir()
            (nift / "public/output.html").write_text("output")
            (nift / ".nift").mkdir()
            (nift / ".nift/tracked.json").write_text("{}")
            (astro / "src").mkdir()
            (astro / "src/page.md").write_text("source")
            (astro / "dist").mkdir()
            (astro / "dist/index.html").write_text("output")
            (astro / "node_modules/.astro").mkdir(parents=True)
            (astro / "node_modules/.astro/cache").write_text("cache")
            (astro / "node_modules/package.txt").write_text("dependency")
            (astro / "node_modules/.pnpm/pkg@1").mkdir(parents=True)
            (astro / "package.json").write_text(
                json.dumps(
                    {
                        "dependencies": {"one": "1"},
                        "devDependencies": {"astro": "7.3.2", "two": "2"},
                        "packageManager": "pnpm@10.0.0",
                    }
                )
            )
            (astro / "pnpm-lock.yaml").write_text("snapshots:\n  pkg@1: {}\n")

            payload = collect(nift, astro, Path("/bin/true"))
            footprints = payload["footprints"]
            self.assertFalse(payload["nift_node_modules"]["present"])
            self.assertEqual(payload["package_json"]["dependencies"]["count"], 1)
            self.assertEqual(payload["package_json"]["devDependencies"]["count"], 2)
            self.assertEqual(payload["pnpm_resolved_store_entries"]["count"], 1)
            self.assertEqual(payload["lockfile_package_snapshots"]["count"], 1)
            self.assertEqual(footprints["nift_source_checkout"]["regular_file_count"], 1)
            self.assertEqual(footprints["astro_source_checkout"]["regular_file_count"], 3)
            self.assertEqual(
                footprints["astro_node_modules_excluding_dot_astro"]["regular_file_count"],
                1,
            )
            self.assertEqual(
                footprints["astro_node_modules_dot_astro"]["regular_file_count"], 1
            )

    def test_cli_output_is_deterministic_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            nift = root / "nift"
            astro = root / "astro"
            nift.mkdir()
            astro.mkdir()
            (astro / "package.json").write_text("{}")
            first = root / "first.json"
            second = root / "second.json"
            arguments = [
                "--nift-project",
                str(nift),
                "--astro-project",
                str(astro),
                "--nift-bin",
                "/bin/true",
            ]
            self.assertEqual(main([*arguments, "--output", str(first)]), 0)
            self.assertEqual(main([*arguments, "--output", str(second)]), 0)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with self.assertRaises(FileExistsError):
                main([*arguments, "--output", str(first)])


if __name__ == "__main__":
    unittest.main()
