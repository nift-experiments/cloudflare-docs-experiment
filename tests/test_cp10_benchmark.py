import json
import os
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

from tools.cp10_benchmark import (
    compare_manifests,
    execute_run,
    manifest_payload,
    paired_comparison,
    parse_time_verbose,
    summarize,
)


class CP10BenchmarkTests(unittest.TestCase):
    def test_manifest_comparison_ignores_mtime_only_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "page.html"
            target.write_text("same")
            before = manifest_payload(root)
            original = target.stat().st_mtime_ns
            target.touch()
            target_stat = target.stat()
            target.chmod(target_stat.st_mode)
            target_time = original + 1_000_000_000
            target.touch()
            os.utime(target, ns=(target_time, target_time))
            after = manifest_payload(root)
            comparison = compare_manifests(before, after)
            self.assertTrue(comparison["equal_content"])
            self.assertEqual(comparison["mtime_only"], ["page.html"])
            target.write_text("changed")
            changed = compare_manifests(before, manifest_payload(root))
            self.assertFalse(changed["equal_content"])
            self.assertEqual(changed["changed"], ["page.html"])

    def test_verbose_time_and_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            timing = root / "time.txt"
            timing.write_text(
                "user_seconds=1.20\n"
                "system_seconds=0.30\n"
                "cpu_percent=150%\n"
                "wall_seconds=1.00\n"
                "maximum_rss_kib=4096\n"
                "major_page_faults=0\n"
                "minor_page_faults=10\n"
                "voluntary_context_switches=2\n"
                "involuntary_context_switches=1\n"
                "filesystem_inputs=0\n"
                "filesystem_outputs=8\n"
                "swaps=0\n"
                "exit_status=0\n"
            )
            parsed = parse_time_verbose(timing)
            self.assertEqual(parsed["wall_seconds"], 1.0)
            self.assertEqual(parsed["maximum_rss_kib"], 4096)
            runs = []
            run_ids = []
            for index, wall in enumerate((1.0, 2.0, 3.0)):
                path = root / f"run-{index}.json"
                run_id = f"run-{index}"
                path.write_text(
                    json.dumps(
                        {
                            "schema": "cp10-run",
                            "schema_version": 1,
                            "id": run_id,
                            "series": "test",
                            "scenario": "test",
                            "tool": "nift",
                            "warmth": "warm",
                            "round": index,
                            "validity": {"infrastructure_valid": True},
                            "time": {
                                "wall_seconds": wall,
                                "user_seconds": wall,
                                "system_seconds": 0.1,
                                "cpu_percent": 100,
                                "maximum_rss_kib": 1000,
                            },
                            "cgroup": {"memory_peak_bytes": 100 + index},
                        }
                    )
                )
                runs.append(path)
                run_ids.append(run_id)
            correctness = root / "correctness.json"
            expected_root = root / "expected"
            actual_root = root / "actual"
            expected_root.mkdir()
            actual_root.mkdir()
            (expected_root / "index.html").write_text("correct")
            (actual_root / "index.html").write_text("correct")
            expected_manifest = manifest_payload(expected_root)
            actual_manifest = manifest_payload(actual_root)
            (root / "expected.json").write_text(json.dumps(expected_manifest))
            (root / "actual.json").write_text(json.dumps(actual_manifest))
            correctness.write_text(
                json.dumps(
                    {
                        "schema": "cp10-correctness",
                        "schema_version": 1,
                        "passed": True,
                        "run_ids": run_ids,
                        "checks": [{"name": "tree", "passed": True}],
                        "comparisons": [
                            {
                                "run_id": run_id,
                                "output_path": str(actual_root),
                                "expected_manifest": "expected.json",
                                "actual_manifest": "actual.json",
                                "expected_entries_sha256": expected_manifest[
                                    "entries_sha256"
                                ],
                                "actual_entries_sha256": actual_manifest[
                                    "entries_sha256"
                                ],
                            }
                            for run_id in run_ids
                        ],
                    }
                )
            )
            result = summarize(runs, correctness)
            self.assertEqual(result["metrics"]["wall_seconds"]["median"], 2.0)
            self.assertEqual(
                result["metrics"]["cgroup_peak_memory_bytes"]["maximum"], 102
            )

    def test_paired_bootstrap_is_deterministic(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            base = {
                "schema": "cp10-summary",
                "schema_version": 1,
                "identity": {
                    "series": "clean",
                    "scenario": "clean",
                    "warmth": "warm",
                },
            }
            nift = root / "nift.json"
            astro = root / "astro.json"
            nift.write_text(
                json.dumps(
                    base
                    | {
                        "identity": base["identity"] | {"tool": "nift"},
                        "observations": [
                            {"round": index, "wall_seconds": value}
                            for index, value in enumerate((1.0, 1.1, 0.9))
                        ],
                    }
                )
            )
            astro.write_text(
                json.dumps(
                    base
                    | {
                        "identity": base["identity"] | {"tool": "astro"},
                        "observations": [
                            {"round": index, "wall_seconds": value}
                            for index, value in enumerate((2.0, 2.2, 1.8))
                        ],
                    }
                )
            )
            result = paired_comparison(nift, astro)
            self.assertEqual(result["ratio_of_medians"], 2.0)
            self.assertFalse(result["bootstrap"]["crosses_parity"])

    def test_time_parser_rejects_incomplete_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            timing = Path(directory) / "time.txt"
            timing.write_text("wall_seconds=1.0\nexit_status=0\n")
            with self.assertRaises(ValueError):
                parse_time_verbose(timing)

    def test_summary_rejects_invalid_or_unattested_runs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run = root / "run.json"
            run.write_text(
                json.dumps(
                    {
                        "schema": "cp10-run",
                        "schema_version": 1,
                        "id": "bad-run",
                        "series": "test",
                        "scenario": "test",
                        "tool": "nift",
                        "warmth": "warm",
                        "round": 1,
                        "validity": {"infrastructure_valid": False},
                        "time": {"wall_seconds": 1.0},
                        "cgroup": {"memory_peak_bytes": 1},
                    }
                )
            )
            correctness = root / "correctness.json"
            correctness.write_text(
                json.dumps(
                    {
                        "schema": "cp10-correctness",
                        "schema_version": 1,
                        "passed": True,
                        "run_ids": ["bad-run"],
                        "checks": [{"name": "tree", "passed": True}],
                        "comparisons": [],
                    }
                )
            )
            with self.assertRaisesRegex(ValueError, "infrastructure-invalid"):
                summarize([run], correctness)

    @unittest.skipUnless(
        os.geteuid() == 0 and os.access("/sys/fs/cgroup", os.W_OK),
        "requires root with writable cgroup v2",
    )
    def test_background_descendant_invalidates_run(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "background.json"
            result = execute_run(
                Namespace(
                    id="background-test",
                    series="test",
                    scenario="test",
                    tool="setup",
                    round=1,
                    warmth="setup",
                    output=output,
                    cwd=root,
                    command=["/bin/sh", "-c", "sleep 0.2 &"],
                )
            )
            self.assertEqual(result, 0)
            evidence = json.loads(output.read_text())
            self.assertFalse(evidence["validity"]["infrastructure_valid"])
            self.assertIn(
                "process tree outlived the timed parent",
                evidence["validity"]["invalid_reasons"],
            )


if __name__ == "__main__":
    unittest.main()
