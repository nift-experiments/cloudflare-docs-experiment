import json
import os
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from unittest.mock import patch

from tools.cp10_benchmark import atomic_json, manifest_payload
from tools.cp10_formal_no_change import StatePath, snapshot_states
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
    copy_file_exact,
    edited_bytes,
    freeze_changed_path_contract,
    marker_evidence,
    manifest_payload_reusing,
    parse_args,
    recorded_command,
    refuse_attempt_collision,
    restore_targeted_nift_state,
    restore_source,
    run_campaign,
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

    def test_targeted_cli_does_not_require_any_astro_or_pnpm_argument(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "nift"
            project.mkdir()
            harness = root / "harness.py"
            harness.write_text("# harness\n")
            executable = root / "nift-bin"
            executable.write_text("#!/bin/sh\nexit 0\n")
            executable.chmod(0o755)
            expected_root = root / "expected"
            expected_root.mkdir()
            expected = root / "expected.json"
            atomic_json(expected, manifest_payload(expected_root))

            args = parse_args(
                [
                    "targeted",
                    "--nift-project",
                    str(project),
                    "--harness",
                    str(harness),
                    "--evidence",
                    str(root / "evidence"),
                    "--nift-expected",
                    str(expected),
                    "--nift-bin",
                    str(executable),
                ]
            )

            self.assertIsNone(args.astro_project)
            self.assertIsNone(args.astro_normalizer)

    def test_targeted_campaign_never_dispatches_astro_setup(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            evidence = root / "evidence"
            project = root / "nift"
            project.mkdir()
            args = Namespace(
                mode="targeted",
                evidence=evidence,
                attempt=1,
                nift_project=project,
            )
            git = {"head": "h", "tree": "t", "status": ""}
            source = Namespace(data=b"source", mtime_ns=1)

            def create_setup(*_args):
                (evidence / "setup").mkdir()
                (evidence / "setup/targeted-setup.json").write_text("{}")

            with (
                patch("tools.cp10_formal_edit.git_state", return_value=git),
                patch("tools.cp10_formal_edit.capture_source", return_value=source),
                patch(
                    "tools.cp10_formal_edit.prepare_targeted_setup",
                    side_effect=create_setup,
                ) as targeted_setup,
                patch(
                    "tools.cp10_formal_edit.targeted_setup_ready",
                    return_value=(git, source),
                ) as targeted_ready,
                patch("tools.cp10_formal_edit.run_targeted") as targeted_runs,
                patch("tools.cp10_formal_edit.prepare_setup") as astro_setup,
                patch("tools.cp10_formal_edit.prepare_remote_archive") as remote_setup,
                patch("tools.cp10_formal_edit.restore_astro_remote_inputs") as remote_restore,
            ):
                self.assertEqual(run_campaign(args), 0)

            targeted_setup.assert_called_once()
            targeted_ready.assert_not_called()
            targeted_runs.assert_called_once()
            astro_setup.assert_not_called()
            remote_setup.assert_not_called()
            remote_restore.assert_not_called()

    def test_targeted_restore_replaces_only_metadata_and_designated_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "project"
            metadata = project / ".nift/public"
            metadata.mkdir(parents=True)
            (metadata / "state.json").write_text("baseline metadata")
            page = project / "public/workers/get-started/guide/index.html"
            page.parent.mkdir(parents=True)
            page.write_text("baseline page")
            unrelated = project / "public/static/large.bin"
            unrelated.parent.mkdir(parents=True)
            unrelated.write_text("baseline static")
            baseline = root / "baseline-minimal"
            snapshot_states("nift", [StatePath("metadata", metadata)], baseline)
            copy_file_exact(page, baseline / "nift-output/workers/get-started/guide/index.html")

            (metadata / "state.json").write_text("mutated metadata")
            page.write_text("mutated page")
            unrelated.write_text("must remain untouched")
            restore_targeted_nift_state(project, baseline)

            self.assertEqual((metadata / "state.json").read_text(), "baseline metadata")
            self.assertEqual(page.read_text(), "baseline page")
            self.assertEqual(unrelated.read_text(), "must remain untouched")

    def test_targeted_manifest_rehashes_only_metadata_changed_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "workers/get-started/guide/index.html"
            page.parent.mkdir(parents=True)
            page.write_text("baseline")
            static = root / "static/large.bin"
            static.parent.mkdir()
            static.write_bytes(b"x" * 1024)
            baseline = manifest_payload(root)
            page.write_text("edited")

            observed = manifest_payload_reusing(root, baseline)

            self.assertEqual(observed["hashing"]["files_hashed"], 1)
            self.assertEqual(observed["hashing"]["certified_hashes_reused"], 1)
            self.assertEqual(
                {entry["path"] for entry in observed["entries"] if entry["type"] == "file"},
                {"static/large.bin", "workers/get-started/guide/index.html"},
            )


if __name__ == "__main__":
    unittest.main()
