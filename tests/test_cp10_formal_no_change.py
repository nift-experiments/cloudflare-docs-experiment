import json
import os
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

from tools.cp10_benchmark import atomic_json, manifest_payload, sha256_file
from tools.cp10_formal_no_change import (
    ORDER,
    StatePath,
    baseline_ready,
    clean_nift,
    command_for,
    normalization_passed,
    preflight_attempt,
    restore_states,
    run_normalizer,
    snapshot_states,
)


class CP10FormalNoChangeTests(unittest.TestCase):
    def test_fixed_order_and_exact_recorded_commands(self):
        self.assertEqual(ORDER, ("nift", "astro", "astro"))
        nift, nift_environment = command_for(
            "nift", Path("/opt/nift"), Path("/opt/pnpm")
        )
        astro, astro_environment = command_for(
            "astro", Path("/opt/nift"), Path("/opt/pnpm")
        )
        self.assertEqual(nift, ["/opt/nift", "build"])
        self.assertEqual(astro, ["/opt/pnpm", "exec", "astro", "build"])
        self.assertNotIn("INCREMENTAL_BUILD", nift_environment)
        self.assertEqual(astro_environment["INCREMENTAL_BUILD"], "true")

    def test_snapshot_restore_reconstructs_exact_archived_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            live = root / "project/output"
            live.mkdir(parents=True)
            target = live / "index.html"
            target.write_text("baseline")
            os.utime(target, ns=(1_700_000_000_000_000_000,) * 2)
            baseline = root / "evidence/baseline"

            snapshot_states("nift", [StatePath("output", live)], baseline)
            expected_digest = manifest_payload(live)["entries_sha256"]
            target.write_text("mutated")
            (live / "extra").write_text("extra")
            restore_states("nift", [StatePath("output", live)], baseline)

            self.assertEqual(target.read_text(), "baseline")
            self.assertFalse((live / "extra").exists())
            self.assertEqual(manifest_payload(live)["entries_sha256"], expected_digest)

    def test_attempt_preflight_refuses_any_artifact_collision(self):
        with tempfile.TemporaryDirectory() as directory:
            evidence = Path(directory)
            (evidence / "nift-r01-a01.json").write_text("existing")
            args = Namespace(
                evidence=evidence,
                start_round=1,
                end_round=1,
                attempt=1,
            )
            with self.assertRaisesRegex(FileExistsError, "refusing to overwrite"):
                preflight_attempt(args)

    def test_nift_cleanup_rejects_output_path_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / ".nift").mkdir()
            (project / "public").mkdir()
            (project / ".nift/tracked.json").write_text(
                json.dumps({"tracked": [{"output": "../source.md"}]})
            )
            with self.assertRaisesRegex(ValueError, "unsafe Nift output path"):
                clean_nift(project)

    def test_astro_normalizer_accepts_classified_variance_without_mutation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            before = root / "before"
            after = root / "after"
            before.mkdir()
            after.mkdir()
            before_bytes = b"pm-12345678-1234-4123-8123-123456789abc"
            after_bytes = b"pm-abcdefab-cdef-4abc-9abc-abcdefabcdef"
            (before / "index.html").write_bytes(before_bytes)
            (after / "index.html").write_bytes(after_bytes)
            before_manifest = root / "before.json"
            after_manifest = root / "after.json"
            atomic_json(before_manifest, manifest_payload(before))
            atomic_json(after_manifest, manifest_payload(after))

            report, returncode = run_normalizer(
                Path(__file__).parents[1] / "tools/cp10_astro_normalize.py",
                [("before", before), ("after", after)],
                [("before", before_manifest), ("after", after_manifest)],
                root / "report.json",
            )

            self.assertEqual(returncode, 0)
            self.assertTrue(normalization_passed(report))
            self.assertEqual((before / "index.html").read_bytes(), before_bytes)
            self.assertEqual((after / "index.html").read_bytes(), after_bytes)

    def test_astro_normalizer_preserves_and_rejects_unclassified_difference(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            before = root / "before"
            after = root / "after"
            before.mkdir()
            after.mkdir()
            (before / "index.html").write_text("expected")
            (after / "index.html").write_text("unexpected")
            before_manifest = root / "before.json"
            after_manifest = root / "after.json"
            atomic_json(before_manifest, manifest_payload(before))
            atomic_json(after_manifest, manifest_payload(after))
            report_path = root / "report.json"

            report, returncode = run_normalizer(
                Path(__file__).parents[1] / "tools/cp10_astro_normalize.py",
                [("before", before), ("after", after)],
                [("before", before_manifest), ("after", after_manifest)],
                report_path,
            )

            self.assertEqual(returncode, 1)
            self.assertTrue(report_path.exists())
            self.assertFalse(normalization_passed(report))
            self.assertEqual(report["unclassified"], ["index.html"])

    def test_baseline_ready_binds_normalizer_reference_and_raw_digest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            evidence = root / "evidence"
            (evidence / "baseline").mkdir(parents=True)
            reference = root / "reference"
            nift_output = root / "nift-output"
            reference.mkdir()
            nift_output.mkdir()
            (reference / "index.html").write_text("astro")
            (nift_output / "index.html").write_text("nift")
            reference_manifest = root / "astro.json"
            nift_manifest = root / "nift.json"
            atomic_json(reference_manifest, manifest_payload(reference))
            atomic_json(nift_manifest, manifest_payload(nift_output))
            normalizer = root / "normalizer.py"
            normalizer.write_text("# frozen normalizer\n")
            args = Namespace(
                evidence=evidence,
                nift_bin=Path("/opt/nift"),
                pnpm_bin=Path("/opt/pnpm"),
                nift_expected=nift_manifest,
                astro_clean_reference_manifest=reference_manifest,
                astro_normalizer=normalizer,
                astro_clean_reference=reference,
                harness=root / "harness.py",
                nift_project=root / "nift-project",
                astro_project=root / "astro-project",
            )
            tools = {}
            for tool in ("nift", "astro"):
                command, environment = command_for(
                    tool, args.nift_bin, args.pnpm_bin
                )
                tools[tool] = {
                    "recorded_command": command,
                    "environment": {
                        "INCREMENTAL_BUILD": environment.get(
                            "INCREMENTAL_BUILD"
                        ),
                        "NODE_OPTIONS": environment.get("NODE_OPTIONS"),
                        "LC_ALL": environment["LC_ALL"],
                    },
                }
            git_state = {"nift": {"head": "n"}, "astro": {"head": "a"}}
            marker = {
                "schema": "cp10-no-change-baseline",
                "schema_version": 2,
                "harness": str(args.harness),
                "projects": {
                    "nift": str(args.nift_project),
                    "astro": str(args.astro_project),
                },
                "nift_expected_entries_sha256": manifest_payload(nift_output)[
                    "entries_sha256"
                ],
                "astro_normalization": {
                    "normalizer": str(normalizer),
                    "normalizer_sha256": sha256_file(normalizer),
                    "clean_reference": str(reference),
                    "clean_reference_manifest": str(reference_manifest),
                    "clean_reference_raw_entries_sha256": manifest_payload(
                        reference
                    )["entries_sha256"],
                },
                "git_before": git_state,
                "git_after": git_state,
                "tools": tools,
            }
            (evidence / "baseline/baseline.json").write_text(json.dumps(marker))

            self.assertEqual(baseline_ready(args), git_state)
            normalizer.write_text("# changed normalizer\n")
            with self.assertRaisesRegex(ValueError, "normalizer or clean reference"):
                baseline_ready(args)


if __name__ == "__main__":
    unittest.main()
