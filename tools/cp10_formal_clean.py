#!/usr/bin/env python3
"""Collect the predeclared CP10 clean-build paired rounds."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path

try:
    from .cp10_benchmark import CAMPAIGN_LOCK_FD_ENV, campaign_lock
except ImportError:
    from cp10_benchmark import CAMPAIGN_LOCK_FD_ENV, campaign_lock


ORDER = ("nift", "astro", "astro", "nift", "nift", "astro")


def run(command: list[str], cwd: Path | None = None) -> None:
    inherited = os.environ.get(CAMPAIGN_LOCK_FD_ENV)
    subprocess.run(
        command,
        cwd=cwd,
        check=True,
        pass_fds=(int(inherited),) if inherited is not None else (),
    )


def archive_if_present(path: Path, destination: Path) -> None:
    if path.exists():
        path.rename(destination)


def nift_clean(
    project: Path, harness: Path, evidence: Path, expected: Path, round_number: int
) -> None:
    metadata = project / ".nift/public"
    archive_if_present(metadata, evidence / f"nift-r{round_number:02d}-prestate")
    tracked = json.loads((project / ".nift/tracked.json").read_text())["tracked"]
    for item in tracked:
        configured = item.get("output", "index.html")
        relative = Path(configured.lstrip("/"))
        if configured.endswith("/"):
            relative /= "index.html"
        (project / "public" / relative).unlink(missing_ok=True)
    identifier = f"formal-clean-nift-r{round_number:02d}"
    record = evidence / f"nift-r{round_number:02d}.json"
    run(
        [
            "python3",
            str(harness),
            "run",
            "--id",
            identifier,
            "--series",
            "formal-clean-warm",
            "--scenario",
            "clean-full",
            "--tool",
            "nift",
            "--round",
            str(round_number),
            "--warmth",
            "warm",
            "--output",
            str(record),
            "--cwd",
            str(project),
            "--",
            "/usr/local/bin/nift",
            "build",
            "--all",
        ]
    )
    if not json.loads(record.read_text())["validity"]["infrastructure_valid"]:
        raise RuntimeError(f"invalid Nift run: {identifier}")
    manifest = evidence / f"nift-r{round_number:02d}-manifest.json"
    run(["python3", str(harness), "manifest", str(project / "public"), str(manifest)])
    run(
        [
            "python3",
            str(harness),
            "compare",
            str(expected),
            str(manifest),
            str(evidence / f"nift-r{round_number:02d}-comparison.json"),
        ]
    )


def astro_clean(project: Path, harness: Path, evidence: Path, round_number: int) -> None:
    archive_if_present(project / "dist", evidence / f"astro-r{round_number:02d}-pre-dist")
    archive_if_present(project / ".astro", evidence / f"astro-r{round_number:02d}-pre-dot-astro")
    archive_if_present(
        project / "node_modules/.astro",
        evidence / f"astro-r{round_number:02d}-pre-node-modules-astro",
    )
    identifier = f"formal-clean-astro-r{round_number:02d}"
    record = evidence / f"astro-r{round_number:02d}.json"
    run(
        [
            "python3",
            str(harness),
            "run",
            "--id",
            identifier,
            "--series",
            "formal-clean-warm",
            "--scenario",
            "clean-full",
            "--tool",
            "astro",
            "--round",
            str(round_number),
            "--warmth",
            "warm",
            "--output",
            str(record),
            "--cwd",
            str(project),
            "--",
            "/root/.cache/node/corepack/v1/pnpm/12.4.2/pnpm-native",
            "exec",
            "astro",
            "build",
        ]
    )
    if not json.loads(record.read_text())["validity"]["infrastructure_valid"]:
        raise RuntimeError(f"invalid Astro run: {identifier}")
    run(
        [
            "python3",
            str(harness),
            "manifest",
            str(project / "dist"),
            str(evidence / f"astro-r{round_number:02d}-manifest.json"),
        ]
    )


def run_campaign() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nift-project", required=True, type=Path)
    parser.add_argument("--astro-project", required=True, type=Path)
    parser.add_argument("--harness", required=True, type=Path)
    parser.add_argument("--evidence", required=True, type=Path)
    parser.add_argument("--nift-expected", required=True, type=Path)
    parser.add_argument("--start-round", default=1, type=int)
    parser.add_argument("--end-round", default=3, type=int)
    args = parser.parse_args()
    if not 1 <= args.start_round <= args.end_round <= len(ORDER):
        parser.error("round range must be within 1..6")
    args.evidence.mkdir(parents=True, exist_ok=True)

    with campaign_lock():
        for round_number in range(args.start_round, args.end_round + 1):
            first = ORDER[round_number - 1]
            second = "astro" if first == "nift" else "nift"
            for tool in (first, second):
                if tool == "nift":
                    nift_clean(
                        args.nift_project,
                        args.harness,
                        args.evidence,
                        args.nift_expected,
                        round_number,
                    )
                else:
                    astro_clean(
                        args.astro_project, args.harness, args.evidence, round_number
                    )
    return 0


def main() -> int:
    return run_campaign()


if __name__ == "__main__":
    raise SystemExit(main())
