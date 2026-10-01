import json
import os
import subprocess
import tempfile
import time
import unittest
from argparse import Namespace
from contextlib import nullcontext
from pathlib import Path
from unittest import mock

from tools.cp10_benchmark import atomic_json, manifest_payload, sha256_file
from tools.cp10_formal_no_change import (
    ORDER,
    StatePath,
    assert_no_stale_benchmark_processes,
    baseline_ready,
    clean_nift,
    command_for,
    normalization_passed,
    preflight_attempt,
    remote_selected_entries,
    restore_astro_remote_inputs,
    restore_states,
    run_normalizer,
    snapshot_states,
    actual_remote_selected_entries,
    compare_output_stats,
    main,
    nift_only_bindings,
    output_stat_payload,
    record_nift_only_run,
    verify_nift_only_prestate,
)


class CP10FormalNoChangeTests(unittest.TestCase):
    def test_nift_only_dispatch_requires_no_astro_arguments_or_actions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "nift"
            project.mkdir()
            harness = root / "harness.py"
            expected = root / "expected.json"
            harness.write_text("harness")
            expected.write_text("expected")
            argv = [
                "--nift-only",
                "--nift-project",
                str(project),
                "--harness",
                str(harness),
                "--evidence",
                str(root / "evidence"),
                "--nift-expected",
                str(expected),
                "--nift-bin",
                "/bin/true",
            ]
            with mock.patch(
                "tools.cp10_formal_no_change.campaign_lock",
                return_value=nullcontext(),
            ), mock.patch(
                "tools.cp10_formal_no_change.assert_no_stale_benchmark_processes"
            ), mock.patch(
                "tools.cp10_formal_no_change.run_campaign",
                side_effect=AssertionError("paired campaign invoked"),
            ), mock.patch(
                "tools.cp10_formal_no_change.run_nift_only", return_value=0
            ) as nift_only:
                self.assertEqual(main(argv), 0)
            args = nift_only.call_args.args[0]
            self.assertTrue(args.nift_only)
            self.assertIsNone(args.astro_project)
            self.assertIsNone(args.astro_normalizer)

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

    def test_nift_only_reconstructs_metadata_and_public_output_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "project"
            output = project / "public"
            metadata = project / ".nift/public"
            output.mkdir(parents=True)
            metadata.mkdir(parents=True)
            page = output / "index.html"
            page.write_text("certified")
            (metadata / "state.json").write_text("baseline")
            evidence = root / "evidence"
            baseline = evidence / "baseline"
            baseline.mkdir(parents=True)
            snapshot_states(
                "nift", [StatePath("metadata", metadata)], baseline
            )
            baseline_stat = output_stat_payload(output)
            baseline_manifest = manifest_payload(output)
            original_mode = page.stat().st_mode & 0o777
            (metadata / "state.json").write_text("mutated")
            original_mtime = page.stat().st_mtime_ns
            page.chmod(0o600)
            os.utime(page, ns=(original_mtime + 1_000_000_000,) * 2)
            args = Namespace(nift_project=project, evidence=evidence)

            reconstructed, restoration_diff = verify_nift_only_prestate(
                args, baseline_stat, baseline_manifest
            )

            self.assertEqual((metadata / "state.json").read_text(), "baseline")
            self.assertEqual(page.stat().st_mtime_ns, original_mtime)
            self.assertEqual(page.stat().st_mode & 0o777, original_mode)
            self.assertEqual(restoration_diff["touched"], ["index.html"])
            self.assertTrue(restoration_diff["content_unchanged"])
            changed_time = page.stat().st_mtime_ns + 1_000_000_000
            os.utime(page, ns=(changed_time, changed_time))
            difference = compare_output_stats(
                baseline_stat,
                output_stat_payload(output),
                output,
                baseline_manifest,
            )
            self.assertEqual(difference["touched"], ["index.html"])
            self.assertEqual(difference["mtime_only"], ["index.html"])
            self.assertEqual(difference["content_changed"], [])
            self.assertEqual(difference["counts"]["selectively_hashed_files"], 1)

    def test_nift_only_changed_output_is_preserved_and_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "project"
            output = project / "public"
            metadata = project / ".nift/public"
            output.mkdir(parents=True)
            metadata.mkdir(parents=True)
            page = output / "index.html"
            page.write_text("baseline")
            (metadata / "state.json").write_text("baseline")
            evidence = root / "evidence"
            baseline = evidence / "baseline"
            baseline.mkdir(parents=True)
            snapshot_states("nift", [StatePath("metadata", metadata)], baseline)
            baseline_stat = output_stat_payload(output)
            baseline_manifest = manifest_payload(output)
            harness = root / "harness.py"
            harness.write_text("# harness\n")
            nift = root / "nift"
            nift.write_text("#!/bin/sh\nexit 0\n")
            nift.chmod(0o755)
            expected = root / "expected.json"
            atomic_json(expected, baseline_manifest)
            args = Namespace(
                nift_project=project,
                evidence=evidence,
                harness=harness,
                nift_bin=nift,
                nift_expected=expected,
            )
            bindings = nift_only_bindings(args)
            git = {"head": "h", "tree": "t", "status": ""}

            def fake_run(command, *_args, **_kwargs):
                if command[0] == "cp":
                    return subprocess.run(command, check=True)
                record_path = Path(command[command.index("--output") + 1])
                page.write_text("changed!")
                atomic_json(
                    record_path,
                    {
                        "campaign_lock_inherited": True,
                        "validity": {"infrastructure_valid": True},
                        "time": {"wall_seconds": 0.1},
                        "cgroup": {"memory_peak_bytes": 1024},
                    },
                )
                return Namespace(returncode=0)

            with mock.patch(
                "tools.cp10_formal_no_change.assert_no_stale_benchmark_processes"
            ), mock.patch(
                "tools.cp10_formal_no_change.git_state", return_value=git
            ), mock.patch(
                "tools.cp10_formal_no_change.run", side_effect=fake_run
            ):
                with self.assertRaisesRegex(RuntimeError, "invalid Nift-only run preserved"):
                    record_nift_only_run(
                        args,
                        1,
                        git,
                        baseline_stat,
                        baseline_manifest,
                        bindings,
                    )

            difference = json.loads(
                (evidence / "nift-run01-output-diff.json").read_text()
            )
            validation = json.loads(
                (evidence / "nift-run01-validation.json").read_text()
            )
            self.assertEqual(difference["content_changed"], ["index.html"])
            self.assertFalse(validation["output_content_unchanged"])
            self.assertFalse(validation["formal_valid"])
            self.assertEqual(page.read_text(), "changed!")

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

    def test_stale_build_process_is_rejected_before_restore(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            executable = project / "nift"
            executable.write_text(
                "#!/usr/bin/env python3\nimport time\ntime.sleep(30)\n"
            )
            executable.chmod(0o755)
            process = subprocess.Popen([str(executable), "build"], cwd=project)
            try:
                for _ in range(50):
                    try:
                        assert_no_stale_benchmark_processes((project,))
                    except RuntimeError:
                        break
                    time.sleep(0.01)
                else:
                    self.fail("stale benchmark process was not detected")
            finally:
                process.terminate()
                process.wait(timeout=5)

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

    def test_nift_cleanup_maps_route_style_output_to_index(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / ".nift").mkdir()
            output = project / "public/glossary/index.html"
            output.parent.mkdir(parents=True)
            output.write_text("generated")
            (project / ".nift/tracked.json").write_text(
                json.dumps({"tracked": [{"output": "/glossary/"}]})
            )

            clean_nift(project)

            self.assertFalse(output.exists())

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

    def test_remote_inputs_restore_exact_selected_state_and_reject_extra_markdown(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archive = root / "archive"
            project = root / "project"
            (archive / "skills").mkdir(parents=True)
            (archive / ".tmp").mkdir()
            generated = archive / (
                "src/content/docs/logs/logpush/logpush-job/datasets/account/generated.md"
            )
            generated.parent.mkdir(parents=True)
            generated.write_text("frozen")
            generated.chmod(0o640)
            os.utime(generated, ns=(1_700_000_000_000_000_000,) * 2)
            (archive / "skills/SKILL.md").write_text("skill")
            (archive / ".tmp/cache").write_text("cache")
            manifest_path = root / "remote.json"
            manifest = manifest_payload(archive)
            atomic_json(manifest_path, manifest)
            datasets = project / (
                "src/content/docs/logs/logpush/logpush-job/datasets/account"
            )
            datasets.mkdir(parents=True)
            (datasets / "index.mdx").write_text("tracked")
            (datasets / "generated.md").write_text("stale")
            (project / "skills").mkdir()
            (project / ".tmp").mkdir()
            args = Namespace(
                astro_project=project,
                astro_remote_input_archive=archive,
                astro_remote_input_archive_sha256=None,
                astro_remote_input_manifest=manifest_path,
            )

            restore_astro_remote_inputs(args, archive)

            expected = remote_selected_entries(manifest["entries"])
            self.assertEqual(
                actual_remote_selected_entries(project, expected), expected
            )
            self.assertEqual((datasets / "index.mdx").read_text(), "tracked")
            self.assertEqual((datasets / "generated.md").stat().st_mode & 0o777, 0o640)
            extra = datasets / "unexpected.md"
            extra.write_text("unexpected")
            with self.assertRaisesRegex(RuntimeError, "unexpected generated markdown"):
                restore_astro_remote_inputs(args, archive)
            self.assertTrue(extra.exists())

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
            harness = root / "harness.py"
            harness.write_text("# frozen harness\n")
            remote_archive = root / "remote-inputs"
            (remote_archive / "skills").mkdir(parents=True)
            (remote_archive / ".tmp").mkdir()
            generated = remote_archive / (
                "src/content/docs/logs/logpush/logpush-job/datasets/account/generated.md"
            )
            generated.parent.mkdir(parents=True)
            generated.write_text("generated")
            (remote_archive / "skills/SKILL.md").write_text("skill")
            (remote_archive / ".tmp/cache").write_text("cache")
            remote_manifest = root / "remote.json"
            atomic_json(remote_manifest, manifest_payload(remote_archive))
            args = Namespace(
                evidence=evidence,
                nift_bin=Path("/opt/nift"),
                pnpm_bin=Path("/opt/pnpm"),
                nift_expected=nift_manifest,
                astro_clean_reference_manifest=reference_manifest,
                astro_normalizer=normalizer,
                astro_clean_reference=reference,
                harness=harness,
                nift_project=root / "nift-project",
                astro_project=root / "astro-project",
                astro_remote_input_archive=remote_archive,
                astro_remote_archive_root=remote_archive,
                astro_remote_input_manifest=remote_manifest,
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
                "schema_version": 3,
                "harness": {
                    "path": str(args.harness),
                    "sha256": sha256_file(args.harness),
                },
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
                "astro_remote_inputs": {
                    "archive": str(remote_archive),
                    "archive_sha256": None,
                    "archive_root": str(remote_archive),
                    "manifest": str(remote_manifest),
                    "entries_sha256": manifest_payload(remote_archive)[
                        "entries_sha256"
                    ],
                },
                "git_before": git_state,
                "git_after": git_state,
                "tools": tools,
            }
            (evidence / "baseline/baseline.json").write_text(json.dumps(marker))

            self.assertEqual(baseline_ready(args), git_state)
            harness.write_text("# changed harness\n")
            with self.assertRaisesRegex(ValueError, "project or harness"):
                baseline_ready(args)
            harness.write_text("# frozen harness\n")
            normalizer.write_text("# changed normalizer\n")
            with self.assertRaisesRegex(ValueError, "normalizer or clean reference"):
                baseline_ready(args)


if __name__ == "__main__":
    unittest.main()
