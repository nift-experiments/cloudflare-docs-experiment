import json
import os
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

from tools.cp10_benchmark import atomic_json, manifest_payload
from tools.cp10_formal_edit import (
    ASTRO_SOURCE,
    MARKER,
    NIFT_SOURCE,
    NIFT_TARGET,
    NORMAL_ORDER,
    TARGET_RUNS,
    TARGET_WARMUPS,
    apply_edit,
    astro_normalized_change_set,
    baseline_states_equal,
    capture_source,
    changed_path_classification,
    changed_files,
    edited_bytes,
    freeze_changed_path_contract,
    marker_evidence,
    recorded_command,
    refuse_attempt_collision,
    restore_source,
    verify_target,
)


class CP10FormalEditTests(unittest.TestCase):
    def test_frozen_sources_schedule_and_exact_commands(self):
        self.assertEqual(NIFT_SOURCE.as_posix(), "content/workers/get-started/guide/index.md")
        self.assertEqual(
            ASTRO_SOURCE.as_posix(), "src/content/docs/workers/get-started/guide.mdx"
        )
        self.assertEqual(MARKER, b"CP10 benchmark edit.")
        self.assertEqual(NORMAL_ORDER, ("nift", "astro", "astro"))
        self.assertEqual((TARGET_WARMUPS, TARGET_RUNS), (3, 30))
        args = Namespace(nift_bin=Path("/opt/nift"), pnpm_bin=Path("/opt/pnpm"))
        nift, nift_env = recorded_command(args, "nift")
        astro, astro_env = recorded_command(args, "astro")
        targeted, _ = recorded_command(args, "nift", targeted=True)
        self.assertEqual(nift, ["/opt/nift", "build"])
        self.assertEqual(astro, ["/opt/pnpm", "exec", "astro", "build"])
        self.assertEqual(targeted, ["/opt/nift", "build", NIFT_TARGET])
        self.assertNotIn("INCREMENTAL_BUILD", nift_env)
        self.assertEqual(astro_env["INCREMENTAL_BUILD"], "true")
        with self.assertRaisesRegex(ValueError, "Astro has no explicit"):
            recorded_command(args, "astro", targeted=True)

    def test_edit_is_an_ordinary_paragraph_and_restores_bytes_mtime_and_mode(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "page.md"
            path.write_bytes(b"body\n")
            path.chmod(0o640)
            os.utime(path, ns=(1_700_000_000_000_000_000,) * 2)
            original = capture_source(path)

            evidence = apply_edit(path, original)

            self.assertEqual(path.read_bytes(), b"body\n\nCP10 benchmark edit.\n")
            self.assertEqual(evidence["marker_count"], 1)
            restored = restore_source(path, original)
            self.assertTrue(restored["bytes_equal"])
            self.assertTrue(restored["mtime_equal"])
            self.assertEqual(path.stat().st_mode & 0o777, 0o640)
            self.assertEqual(edited_bytes(b"body"), b"body\n\nCP10 benchmark edit.\n")

    def test_target_must_have_the_frozen_name_and_output(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / ".nift").mkdir()
            tracked = project / ".nift/tracked.json"
            tracked.write_text(
                json.dumps(
                    {
                        "tracked": [
                            {
                                "name": NIFT_TARGET,
                                "output": "workers/get-started/guide/index.html",
                            }
                        ]
                    }
                )
            )
            self.assertEqual(verify_target(project)["name"], NIFT_TARGET)
            tracked.write_text(
                json.dumps({"tracked": [{"name": NIFT_TARGET, "output": "wrong.html"}]})
            )
            with self.assertRaisesRegex(ValueError, "not uniquely mapped"):
                verify_target(project)

    def test_changed_files_separates_content_and_mtime_only_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "content.html").write_text("changed")
            (root / "touched.html").write_text("same")
            (root / "folder").mkdir()
            manifest = manifest_payload(root)
            diff = {
                "added": [],
                "removed": [],
                "changed": ["content.html", "folder"],
                "mtime_only": ["touched.html"],
            }
            self.assertEqual(
                changed_files(diff, manifest),
                {
                    "content_changed": ["content.html"],
                    "touched": ["content.html", "touched.html"],
                },
            )

    def test_attempt_collision_refuses_partial_invalid_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            evidence = Path(directory)
            (evidence / "nift-run01-a01.stderr.log").write_text("failed")
            with self.assertRaisesRegex(FileExistsError, "refusing to overwrite"):
                refuse_attempt_collision(evidence, "nift-run01-a01")
            refuse_attempt_collision(evidence, "nift-run01-a02")

    def test_baseline_restoration_requires_optional_state_to_remain_absent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            baseline = root / "baseline"
            baseline.mkdir()
            optional = Namespace(name="root-metadata", live=root / "live", required=False)
            self.assertTrue(baseline_states_equal("astro", [optional], baseline))
            optional.live.mkdir()
            self.assertFalse(baseline_states_equal("astro", [optional], baseline))

    def test_changed_path_classification_accepts_exact_and_rejects_missing_or_extra(self):
        expected = {
            "added": [],
            "removed": [],
            "changed": ["dependent.html", "workers/get-started/guide/index.html"],
        }
        accepted = changed_path_classification(expected, expected)
        self.assertTrue(accepted["matches"])
        self.assertTrue(accepted["all_expected_dependents_changed"])
        self.assertTrue(accepted["no_unclassified_output_changed"])

        missing = changed_path_classification(
            expected,
            {"added": [], "removed": [], "changed": ["workers/get-started/guide/index.html"]},
        )
        self.assertFalse(missing["matches"])
        self.assertEqual(missing["missing_expected"]["changed"], ["dependent.html"])

        extra = changed_path_classification(
            expected,
            {
                "added": [],
                "removed": [],
                "changed": [
                    "dependent.html",
                    "unexpected.html",
                    "workers/get-started/guide/index.html",
                ],
            },
        )
        self.assertFalse(extra["matches"])
        self.assertEqual(extra["unexpected_unclassified"]["changed"], ["unexpected.html"])

    def test_astro_change_classification_exposes_categories_and_rejects_bad_evidence(self):
        report = {
            "schema": "cp10-astro-normalization-report",
            "rejected": [],
            "unclassified": ["workers/get-started/guide/index.html"],
            "comparisons": [
                {
                    "before": "clean",
                    "after": "edited",
                    "normalized": {
                        "added": [],
                        "removed": [],
                        "changed": ["workers/get-started/guide/index.html"],
                    },
                    "unclassified": ["workers/get-started/guide/index.html"],
                    "categories": {
                        "package-manager-uuid": {
                            "count": 1,
                            "paths": ["other.html"],
                        }
                    },
                }
            ],
        }
        classified = astro_normalized_change_set(report, "clean", "edited")
        self.assertEqual(
            classified["paths"]["changed"],
            ["workers/get-started/guide/index.html"],
        )
        self.assertIn("package-manager-uuid", classified["normalizer_categories"])

        report["rejected"] = [{"path": "other.html", "error": "bad"}]
        with self.assertRaisesRegex(ValueError, "rejected"):
            astro_normalized_change_set(report, "clean", "edited")

    def test_marker_must_appear_once_on_designated_output_page(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            other = root / "other.html"
            other.write_bytes(MARKER)
            self.assertFalse(marker_evidence(root)["passed"])
            designated = root / "workers/get-started/guide/index.html"
            designated.parent.mkdir(parents=True)
            designated.write_bytes(b"<p>" + MARKER + b"</p>")
            self.assertTrue(marker_evidence(root)["passed"])
            designated.write_bytes(MARKER + b" " + MARKER)
            self.assertFalse(marker_evidence(root)["passed"])

    def test_nift_setup_freezes_clean_to_edited_dependents(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            evidence = root / "evidence"
            references = evidence / "setup/references"
            references.mkdir(parents=True)
            clean = root / "clean"
            edited = root / "edited"
            for output in (clean, edited):
                page = output / "workers/get-started/guide/index.html"
                page.parent.mkdir(parents=True)
                page.write_text("unedited")
                (output / "dependent.txt").write_text("before")
            (edited / "workers/get-started/guide/index.html").write_bytes(MARKER)
            (edited / "dependent.txt").write_text("after")
            clean_manifest = root / "clean.json"
            edited_manifest = references / "nift-edited-manifest.json"
            atomic_json(clean_manifest, manifest_payload(clean))
            atomic_json(edited_manifest, manifest_payload(edited))
            args = Namespace(evidence=evidence, nift_expected=clean_manifest)

            contract = freeze_changed_path_contract(args, "nift", edited)

            self.assertEqual(
                contract["expected_changed_paths"]["changed"],
                ["dependent.txt", "workers/get-started/guide/index.html"],
            )
            self.assertTrue(contract["designated_output_marker"]["passed"])


if __name__ == "__main__":
    unittest.main()
