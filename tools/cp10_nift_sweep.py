#!/usr/bin/env python3
"""Run the predeclared CP10 Nift worker qualification series."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--harness", required=True, type=Path)
    parser.add_argument("--evidence", required=True, type=Path)
    parser.add_argument("--threads", required=True, choices=(-1, -2), type=int)
    parser.add_argument("--runs", default=8, type=int)
    parser.add_argument("--start", default=1, type=int)
    args = parser.parse_args()

    project = args.project.resolve()
    evidence = args.evidence.resolve()
    config_path = project / ".nift/config.json"
    original_config = config_path.read_bytes()
    config = json.loads(original_config)
    config["config"]["build-threads"] = args.threads
    config_path.write_text(json.dumps(config, indent=2) + "\n")
    tracked = json.loads((project / ".nift/tracked.json").read_text())["tracked"]
    label = f"minus{abs(args.threads)}"

    try:
        for run in range(args.start, args.start + args.runs):
            run_id = f"nift-workers-{label}-run{run:02d}"
            metadata = project / ".nift/public"
            if metadata.exists():
                metadata.rename(evidence / f"{label}-run{run:02d}-prestate")
            for item in tracked:
                output = item.get("output", "index.html")
                (project / "public" / output).unlink(missing_ok=True)
            result = subprocess.run(
                [
                    "python3",
                    str(args.harness),
                    "run",
                    "--id",
                    run_id,
                    "--series",
                    "nift-worker-sweep",
                    "--scenario",
                    "full-build-all",
                    "--tool",
                    "nift",
                    "--round",
                    str(run),
                    "--warmth",
                    "warm",
                    "--output",
                    str(evidence / f"{label}-run{run:02d}.json"),
                    "--cwd",
                    str(project),
                    "--",
                    "/usr/local/bin/nift",
                    "build",
                    "--all",
                ]
            )
            record = json.loads((evidence / f"{label}-run{run:02d}.json").read_text())
            if result.returncode or not record["validity"]["infrastructure_valid"]:
                return 1
    finally:
        config_path.write_bytes(original_config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
