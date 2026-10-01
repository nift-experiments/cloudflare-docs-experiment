import tempfile
import unittest
from argparse import Namespace
from contextlib import nullcontext
from pathlib import Path
from unittest.mock import patch

from tools.cp10_benchmark import sha256_file
from tools.cp10_formal_edit import BATCH_NIFT_SOURCES, BATCH_OUTPUTS, MARKER
from tools.cp10_nift_edit import (
    MODE_SPECS,
    SHARED_REPRESENTATIVE_OUTPUTS,
    main,
    parse_args,
    parse_nift_stdout,
    validate_outputs,
)


class CP10NiftEditTests(unittest.TestCase):
    def test_parse_nift_stdout_extracts_built_and_up_to_date_counts(self):
        self.assertEqual(
            parse_nift_stdout(
                "📦 5 files built successfully\n✓ 8798 tracked files are up to date\n"
            ),
            {"built": 5, "up_to_date": 8798},
        )
        self.assertEqual(
            parse_nift_stdout("📦 all 1 specified files built successfully\n"),
            {"built": 1, "up_to_date": 0},
        )
        self.assertEqual(
            parse_nift_stdout("📦 1 file rebuilt successfully\n"),
            {"built": 1, "up_to_date": 0},
        )
        self.assertEqual(
            parse_nift_stdout("✓ 8803 tracked files are up to date\n"),
            {"built": 0, "up_to_date": 8803},
        )
        with self.assertRaisesRegex(ValueError, "missing or ambiguous"):
            parse_nift_stdout("time taken: 1 second\n")
        with self.assertRaisesRegex(ValueError, "missing or ambiguous"):
            parse_nift_stdout(
                "1 file built successfully\n2 files built successfully\n"
            )

    def test_designated_output_validation_requires_one_marker_and_changed_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            one = root / "one/index.html"
            two = root / "two/index.html"
            one.parent.mkdir(parents=True)
            two.parent.mkdir(parents=True)
            one.write_bytes(b"baseline one")
            two.write_bytes(b"baseline two")
            hashes = {
                "one/index.html": sha256_file(one),
                "two/index.html": sha256_file(two),
            }
            one.write_bytes(b"<p>" + MARKER + b"</p>")
            two.write_bytes(b"baseline two")

            result = validate_outputs(
                root,
                (Path("one/index.html"), Path("two/index.html")),
                MARKER,
                hashes,
            )

            self.assertTrue(result[0]["passed"])
            self.assertFalse(result[1]["passed"])
            self.assertFalse(result[1]["hash_changed"])
            two.write_bytes(MARKER + MARKER)
            self.assertFalse(
                validate_outputs(
                    root, (Path("two/index.html"),), MARKER, hashes
                )[0]["passed"]
            )

    def test_modes_freeze_sources_outputs_and_shared_representatives(self):
        self.assertEqual(MODE_SPECS["batch-normal"].sources, BATCH_NIFT_SOURCES)
        self.assertEqual(MODE_SPECS["batch-normal"].outputs, BATCH_OUTPUTS)
        self.assertEqual(len(SHARED_REPRESENTATIVE_OUTPUTS), 5)
        self.assertIn(
            Path("workers/get-started/guide/index.html"),
            SHARED_REPRESENTATIVE_OUTPUTS,
        )
        self.assertGreaterEqual(
            len(set(path.parts[0] for path in SHARED_REPRESENTATIVE_OUTPUTS)), 5
        )

    def test_cli_resolves_required_paths_and_dispatches_under_campaign_lock(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "project"
            project.mkdir()
            harness = root / "cp10_benchmark.py"
            harness.write_text("# harness\n")
            evidence = root / "evidence"
            parsed = parse_args(
                [
                    "one-normal",
                    "--project",
                    str(project),
                    "--harness",
                    str(harness),
                    "--evidence",
                    str(evidence),
                    "--nift-bin",
                    "/bin/true",
                ]
            )
            self.assertEqual(parsed.mode, "one-normal")
            self.assertEqual(parsed.project, project.resolve())
            self.assertEqual(parsed.evidence, evidence.resolve())

            args = Namespace(project=project, mode="one-normal")
            with (
                patch("tools.cp10_nift_edit.parse_args", return_value=args),
                patch("tools.cp10_nift_edit.campaign_lock", return_value=nullcontext()) as lock,
                patch("tools.cp10_nift_edit.assert_no_stale_benchmark_processes") as stale,
                patch("tools.cp10_nift_edit.run_campaign", return_value=0) as campaign,
            ):
                self.assertEqual(main(["ignored"]), 0)
            lock.assert_called_once_with()
            stale.assert_called_once_with((project,))
            campaign.assert_called_once_with(args)


if __name__ == "__main__":
    unittest.main()
