import json
import tempfile
import unittest
from argparse import Namespace
from contextlib import nullcontext
from pathlib import Path
from unittest import mock

from tools.cp10_astro_final_incremental import (
    ROUNDS,
    SCENARIO,
    SERIES,
    exact_command,
    outcome_payload,
    parse_args,
    preflight_evidence,
    record_run,
    run_campaign,
    summary_payload,
    validate_baseline,
)
from tools.cp10_benchmark import atomic_json, manifest_payload


def valid_normalization_report():
    return {
        "schema": "cp10-astro-normalization-report",
        "schema_version": 1,
        "normalized_equivalent": True,
        "rejected": [],
        "unclassified": [],
        "comparisons": [{"normalized": {"equal": True}, "unclassified": []}],
    }


class CP10AstroFinalIncrementalTests(unittest.TestCase):
    def test_fixed_three_rounds_and_cli_has_no_round_override(self):
        self.assertEqual(ROUNDS, (1, 2, 3))
        self.assertEqual(
            exact_command(Path("/opt/pnpm")),
            ["/opt/pnpm", "exec", "astro", "build"],
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "project"
            baseline = root / "baseline"
            archive = root / "archive"
            project.mkdir()
            baseline.mkdir()
            archive.mkdir()
            arguments = []
            for flag in ("harness", "normalizer", "remote-input-manifest", "pnpm"):
                path = root / flag
                path.write_text(flag)
                path.chmod(0o755)
                arguments.extend((f"--{flag}", str(path)))
            arguments.extend(
                (
                    "--astro-project",
                    str(project),
                    "--baseline",
                    str(baseline),
                    "--remote-input-archive",
                    str(archive),
                    "--evidence",
                    str(root / "evidence"),
                )
            )
            with self.assertRaises(SystemExit):
                parse_args([*arguments, "--rounds", "4"])

    def test_campaign_runs_exactly_three_records_and_no_setup_build(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            evidence = root / "evidence"
            project = root / "project"
            project.mkdir()
            args = Namespace(
                evidence=evidence,
                astro_project=project,
                baseline=root / "baseline",
            )
            git = {"head": "head", "tree": "tree", "status": ""}

            def fake_record(_args, round_number, *_rest):
                stem = f"astro-run{round_number:02d}"
                run_id = f"{SERIES}-run{round_number:02d}"
                command = ["/opt/pnpm", "exec", "astro", "build"]
                atomic_json(
                    evidence / f"{stem}-validation.json",
                    {
                        "schema": "cp10-astro-final-incremental-run-validation",
                        "round": round_number,
                        "run_id": run_id,
                        "command": command,
                        "formal_valid": True,
                    },
                )
                atomic_json(
                    evidence / f"{stem}.json",
                    {
                        "schema": "cp10-run",
                        "id": run_id,
                        "round": round_number,
                        "command": command,
                        "validity": {"infrastructure_valid": True},
                        "time": {"wall_seconds": round_number},
                        "cgroup": {"memory_peak_bytes": round_number * 100},
                    },
                )
                return {"formal_valid": True}

            with mock.patch(
                "tools.cp10_astro_final_incremental.git_state", return_value=git
            ), mock.patch(
                "tools.cp10_astro_final_incremental.remote_archive_root",
                return_value=nullcontext(root / "archive"),
            ), mock.patch(
                "tools.cp10_astro_final_incremental.bindings", return_value={"frozen": True}
            ), mock.patch(
                "tools.cp10_astro_final_incremental.record_run",
                side_effect=fake_record,
            ) as recorded, mock.patch(
                "tools.cp10_astro_final_incremental.run",
                side_effect=AssertionError("hidden build or warmup"),
            ):
                self.assertEqual(run_campaign(args), 0)

            self.assertEqual(
                [call.args[1] for call in recorded.call_args_list], [1, 2, 3]
            )
            summary = json.loads((evidence / "summary.json").read_text())
            self.assertEqual(summary["count"], 3)
            self.assertEqual(summary["rounds"], [1, 2, 3])

    def test_record_uses_one_exact_incremental_harness_command(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "project"
            output = project / "dist"
            metadata = project / "node_modules/.astro"
            output.mkdir(parents=True)
            metadata.mkdir(parents=True)
            (output / "index.html").write_text("same")
            (metadata / "state").write_text("state")
            evidence = root / "evidence"
            evidence.mkdir()
            harness = root / "cp10_benchmark.py"
            normalizer = root / "normalizer.py"
            pnpm = root / "pnpm"
            for path in (harness, normalizer, pnpm):
                path.write_text(path.name)
            args = Namespace(
                astro_project=project,
                baseline=root / "baseline",
                evidence=evidence,
                harness=harness,
                normalizer=normalizer,
                pnpm=pnpm,
            )
            git = {"head": "head", "tree": "tree", "status": ""}
            frozen = {"binding": "frozen"}
            calls = []

            def fake_run(command, **kwargs):
                calls.append((command, kwargs))
                record_path = Path(command[command.index("--output") + 1])
                round_number = int(command[command.index("--round") + 1])
                atomic_json(
                    record_path,
                    {
                        "schema": "cp10-run",
                        "schema_version": 1,
                        "id": f"{SERIES}-run{round_number:02d}",
                        "series": SERIES,
                        "scenario": SCENARIO,
                        "tool": "astro",
                        "round": round_number,
                        "warmth": "warm",
                        "working_directory": str(project),
                        "command": exact_command(pnpm),
                        "campaign_lock_inherited": True,
                        "validity": {"infrastructure_valid": True},
                    },
                )
                return Namespace(returncode=0)

            with mock.patch(
                "tools.cp10_astro_final_incremental.assert_no_stale_benchmark_processes"
            ), mock.patch(
                "tools.cp10_astro_final_incremental.bindings", return_value=frozen
            ), mock.patch(
                "tools.cp10_astro_final_incremental.restore_states"
            ), mock.patch(
                "tools.cp10_astro_final_incremental.restore_astro_remote_inputs"
            ), mock.patch(
                "tools.cp10_astro_final_incremental.git_state", return_value=git
            ), mock.patch(
                "tools.cp10_astro_final_incremental.verify_live_remote_inputs",
                return_value=True,
            ), mock.patch(
                "tools.cp10_astro_final_incremental.run_normalizer",
                return_value=(valid_normalization_report(), 0),
            ), mock.patch(
                "tools.cp10_astro_final_incremental.run", side_effect=fake_run
            ):
                validation = record_run(args, 2, git, frozen, root / "archive")

            self.assertTrue(validation["formal_valid"])
            self.assertEqual(len(calls), 1)
            harness_command, kwargs = calls[0]
            self.assertEqual(
                harness_command[harness_command.index("--") + 1 :],
                [str(pnpm), "exec", "astro", "build"],
            )
            self.assertEqual(kwargs["env"]["INCREMENTAL_BUILD"], "true")
            self.assertNotIn("warmup", " ".join(harness_command).lower())

    def test_refuses_nonempty_evidence_without_overwriting(self):
        with tempfile.TemporaryDirectory() as directory:
            evidence = Path(directory) / "evidence"
            evidence.mkdir()
            existing = evidence / "astro-run01.stdout.log"
            existing.write_text("preserve")
            with self.assertRaisesRegex(FileExistsError, "non-empty evidence"):
                preflight_evidence(evidence)
            self.assertEqual(existing.read_text(), "preserve")

    def test_baseline_requires_matching_output_and_metadata_archives(self):
        with tempfile.TemporaryDirectory() as directory:
            baseline = Path(directory) / "baseline"
            snapshot = baseline / "snapshots/astro-output"
            snapshot.mkdir(parents=True)
            (snapshot / "index.html").write_text("baseline")
            atomic_json(
                baseline / "astro-output-manifest.json", manifest_payload(snapshot)
            )
            with self.assertRaisesRegex(ValueError, "Astro metadata"):
                validate_baseline(baseline)

            metadata = baseline / "snapshots/astro-metadata"
            metadata.mkdir()
            (metadata / "state").write_text("baseline")
            atomic_json(
                baseline / "astro-metadata-manifest.json", manifest_payload(metadata)
            )
            self.assertTrue(validate_baseline(baseline)["metadata"]["present"])
            (snapshot / "index.html").write_text("changed")
            with self.assertRaisesRegex(ValueError, "snapshot differs"):
                validate_baseline(baseline)

    def test_summary_refuses_missing_or_invalid_run(self):
        with tempfile.TemporaryDirectory() as directory:
            evidence = Path(directory)
            with self.assertRaisesRegex(ValueError, "missing or malformed run 1"):
                summary_payload(evidence)

            for round_number in ROUNDS:
                stem = f"astro-run{round_number:02d}"
                run_id = f"run-{round_number}"
                command = ["pnpm", "exec", "astro", "build"]
                atomic_json(
                    evidence / f"{stem}-validation.json",
                    {
                        "schema": "cp10-astro-final-incremental-run-validation",
                        "round": round_number,
                        "run_id": run_id,
                        "command": command,
                        "formal_valid": round_number != 2,
                    },
                )
                atomic_json(
                    evidence / f"{stem}.json",
                    {
                        "schema": "cp10-run",
                        "id": run_id,
                        "round": round_number,
                        "command": command,
                        "validity": {"infrastructure_valid": True},
                        "time": {"wall_seconds": 1.0},
                        "cgroup": {"memory_peak_bytes": 1},
                    },
                )
            with self.assertRaisesRegex(ValueError, "invalid run 2"):
                summary_payload(evidence)

            outcome = outcome_payload(evidence)
            self.assertEqual(outcome["count"], 3)
            self.assertEqual(outcome["formal_valid_count"], 2)
            self.assertEqual(outcome["formal_invalid_rounds"], [2])
            self.assertFalse(outcome["all_formal_valid"])


if __name__ == "__main__":
    unittest.main()
