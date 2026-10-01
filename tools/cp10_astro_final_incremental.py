#!/usr/bin/env python3
"""Collect the final exactly three CP10 Astro scenario-B incremental builds."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

try:
    from .cp10_benchmark import (
        atomic_json,
        campaign_lock,
        compare_manifests,
        load_manifest,
        manifest_payload,
        metric_summary,
        sha256_file,
    )
    from .cp10_formal_no_change import (
        StatePath,
        actual_remote_selected_entries,
        assert_no_stale_benchmark_processes,
        git_state,
        normalization_passed,
        remote_selected_entries,
        restore_astro_remote_inputs,
        restore_states,
        run,
        run_normalizer,
        verify_remote_archive,
    )
except ImportError:
    from cp10_benchmark import (  # type: ignore[no-redef]
        atomic_json,
        campaign_lock,
        compare_manifests,
        load_manifest,
        manifest_payload,
        metric_summary,
        sha256_file,
    )
    from cp10_formal_no_change import (  # type: ignore[no-redef]
        StatePath,
        actual_remote_selected_entries,
        assert_no_stale_benchmark_processes,
        git_state,
        normalization_passed,
        remote_selected_entries,
        restore_astro_remote_inputs,
        restore_states,
        run,
        run_normalizer,
        verify_remote_archive,
    )


ROUNDS = (1, 2, 3)
SERIES = "final-astro-scenario-b-no-change-incremental"
SCENARIO = "scenario-b-no-change-incremental"
SUMMARY_NAME = "summary.json"


def states_for(project: Path) -> list[StatePath]:
    return [
        StatePath("output", project / "dist"),
        StatePath("metadata", project / "node_modules/.astro"),
        StatePath("root-metadata", project / ".astro", required=False),
    ]


def exact_command(pnpm: Path) -> list[str]:
    return [str(pnpm), "exec", "astro", "build"]


def command_environment() -> dict[str, str]:
    environment = os.environ.copy()
    environment["INCREMENTAL_BUILD"] = "true"
    environment["LC_ALL"] = "C"
    return environment


def environment_binding(environment: dict[str, str]) -> dict[str, Any]:
    canonical = json.dumps(
        sorted(environment.items()), separators=(",", ":"), ensure_ascii=True
    ).encode()
    return {
        "sha256": hashlib.sha256(canonical).hexdigest(),
        "variable_names": sorted(environment),
        "required": {
            "INCREMENTAL_BUILD": environment.get("INCREMENTAL_BUILD"),
            "LC_ALL": environment.get("LC_ALL"),
            "NODE_OPTIONS": environment.get("NODE_OPTIONS"),
        },
    }


def validate_baseline(baseline: Path) -> dict[str, Any]:
    if not baseline.is_dir() or baseline.is_symlink():
        raise ValueError(f"--baseline must be a directory: {baseline}")
    bindings: dict[str, Any] = {}
    for name, required in (("output", True), ("metadata", True), ("root-metadata", False)):
        snapshot = baseline / "snapshots" / f"astro-{name}"
        manifest_path = baseline / f"astro-{name}-manifest.json"
        snapshot_present = snapshot.exists() or snapshot.is_symlink()
        manifest_present = manifest_path.exists() or manifest_path.is_symlink()
        if snapshot_present != manifest_present or (required and not snapshot_present):
            raise ValueError(f"incomplete archived baseline for Astro {name}")
        if not snapshot_present:
            bindings[name] = {"present": False}
            continue
        if snapshot.is_symlink() or not snapshot.is_dir() or not manifest_path.is_file():
            raise ValueError(f"invalid archived baseline object for Astro {name}")
        expected = load_manifest(manifest_path)
        observed = manifest_payload(snapshot)
        if observed["entries_sha256"] != expected["entries_sha256"]:
            raise ValueError(f"Astro {name} snapshot differs from its manifest")
        bindings[name] = {
            "present": True,
            "snapshot": str(snapshot),
            "manifest": str(manifest_path),
            "manifest_file_sha256": sha256_file(manifest_path),
            "entries_sha256": expected["entries_sha256"],
        }
    marker = baseline / "baseline.json"
    if marker.exists():
        if not marker.is_file() or marker.is_symlink():
            raise ValueError("invalid archived baseline marker")
        bindings["marker"] = {
            "path": str(marker),
            "sha256": sha256_file(marker),
        }
    return bindings


def remote_binding(args: argparse.Namespace, archive_root: Path) -> dict[str, Any]:
    manifest = verify_remote_archive(args, archive_root)
    return {
        "archive": str(args.remote_input_archive),
        "archive_file_sha256": (
            sha256_file(args.remote_input_archive)
            if args.remote_input_archive.is_file()
            else None
        ),
        "archive_tree_entries_sha256": manifest_payload(archive_root)[
            "entries_sha256"
        ],
        "manifest": str(args.remote_input_manifest),
        "manifest_file_sha256": sha256_file(args.remote_input_manifest),
        "manifest_entries_sha256": manifest["entries_sha256"],
    }


def bindings(args: argparse.Namespace, archive_root: Path) -> dict[str, Any]:
    environment = command_environment()
    return {
        "harness": {
            "path": str(args.harness),
            "sha256": sha256_file(args.harness),
        },
        "normalizer": {
            "path": str(args.normalizer),
            "sha256": sha256_file(args.normalizer),
        },
        "pnpm": {
            "path": str(args.pnpm),
            "sha256": sha256_file(args.pnpm),
        },
        "baseline": {
            "path": str(args.baseline),
            "states": validate_baseline(args.baseline),
        },
        "remote_inputs": remote_binding(args, archive_root),
        "command": exact_command(args.pnpm),
        "environment": environment_binding(environment),
    }


@contextmanager
def remote_archive_root(args: argparse.Namespace) -> Iterator[Path]:
    if args.remote_input_archive.is_dir():
        args.astro_remote_archive_root = args.remote_input_archive
        yield args.remote_input_archive
        return
    with tempfile.TemporaryDirectory(prefix="cp10-astro-remote-") as directory:
        import tarfile

        root = Path(directory)
        with tarfile.open(args.remote_input_archive, "r:*") as archive:
            archive.extractall(root, filter="data")
        args.astro_remote_archive_root = root
        yield root


def artifact_paths(evidence: Path, round_number: int) -> list[Path]:
    stem = f"astro-run{round_number:02d}"
    return [
        evidence / f"{stem}.json",
        evidence / f"{stem}.stdout.log",
        evidence / f"{stem}.stderr.log",
        evidence / f"{stem}.time.txt",
        evidence / f"{stem}-pre-output-manifest.json",
        evidence / f"{stem}-post-output-manifest.json",
        evidence / f"{stem}-output-diff.json",
        evidence / f"{stem}-normalization.json",
        evidence / f"{stem}-validation.json",
        *[
            evidence / f"{stem}-{phase}-{name}-manifest.json"
            for name in ("metadata", "root-metadata")
            for phase in ("pre", "post")
        ],
        *[
            evidence / f"{stem}-{name}-diff.json"
            for name in ("metadata", "root-metadata")
        ],
    ]


def preflight_evidence(evidence: Path) -> None:
    if evidence.exists() and not evidence.is_dir():
        raise ValueError(f"evidence path is not a directory: {evidence}")
    if evidence.exists() and any(evidence.iterdir()):
        raise FileExistsError(
            f"refusing non-empty evidence directory: {evidence}"
        )
    evidence.mkdir(parents=True, exist_ok=True)
    collisions = [
        path for round_number in ROUNDS for path in artifact_paths(evidence, round_number)
        if path.exists()
    ]
    if collisions or (evidence / SUMMARY_NAME).exists():
        raise FileExistsError(
            f"refusing to overwrite evidence: {(collisions or [evidence / SUMMARY_NAME])[0]}"
        )


def verify_live_remote_inputs(args: argparse.Namespace, archive_root: Path) -> bool:
    manifest = verify_remote_archive(args, archive_root)
    expected = remote_selected_entries(manifest["entries"])
    return actual_remote_selected_entries(args.astro_project, expected) == expected


def record_run(
    args: argparse.Namespace,
    round_number: int,
    initial_git: dict[str, str],
    expected_bindings: dict[str, Any],
    archive_root: Path,
) -> dict[str, Any]:
    stem = f"astro-run{round_number:02d}"
    states = states_for(args.astro_project)
    assert_no_stale_benchmark_processes((args.astro_project,))
    if bindings(args, archive_root) != expected_bindings:
        raise RuntimeError("campaign binding changed before recorded run")
    restore_states("astro", states, args.baseline)
    restore_astro_remote_inputs(args, archive_root)
    git_before = git_state(args.astro_project)
    if git_before != initial_git or git_before["status"]:
        raise RuntimeError("Astro tracked Git state differs before recorded run")

    pre_manifests: dict[str, dict[str, Any]] = {}
    for state in states:
        if state.live.is_dir():
            payload = manifest_payload(state.live)
            pre_manifests[state.name] = payload
            atomic_json(
                args.evidence / f"{stem}-pre-{state.name}-manifest.json", payload
            )

    identifier = f"{SERIES}-run{round_number:02d}"
    command = exact_command(args.pnpm)
    environment = command_environment()
    harness_command = [
        sys.executable,
        str(args.harness),
        "run",
        "--id",
        identifier,
        "--series",
        SERIES,
        "--scenario",
        SCENARIO,
        "--tool",
        "astro",
        "--round",
        str(round_number),
        "--warmth",
        "warm",
        "--output",
        str(args.evidence / f"{stem}.json"),
        "--cwd",
        str(args.astro_project),
        "--",
        *command,
    ]
    completed = None
    failures: list[str] = []
    try:
        completed = run(harness_command, env=environment, check=False)
    except BaseException as error:
        failures.append(f"harness invocation failed: {type(error).__name__}: {error}")

    record_path = args.evidence / f"{stem}.json"
    record: dict[str, Any] | None = None
    try:
        record = json.loads(record_path.read_text())
    except (FileNotFoundError, json.JSONDecodeError, OSError) as error:
        failures.append(f"missing or malformed harness record: {error}")

    post_manifests: dict[str, dict[str, Any]] = {}
    for state in states:
        if not state.live.is_dir():
            if state.required:
                failures.append(f"required post-build state is absent: {state.name}")
            continue
        try:
            payload = manifest_payload(state.live)
            post_manifests[state.name] = payload
            atomic_json(
                args.evidence / f"{stem}-post-{state.name}-manifest.json", payload
            )
            if state.name in pre_manifests:
                difference = compare_manifests(pre_manifests[state.name], payload)
                atomic_json(
                    args.evidence / f"{stem}-{state.name}-diff.json", difference
                )
        except BaseException as error:
            failures.append(f"post-build {state.name} capture failed: {error}")

    normalization_report = None
    normalization_returncode = None
    if "output" in post_manifests:
        try:
            normalization_report, normalization_returncode = run_normalizer(
                args.normalizer,
                [
                    ("archived-pre-state", args.baseline / "snapshots/astro-output"),
                    ("recorded-output", states[0].live),
                ],
                [
                    ("archived-pre-state", args.baseline / "astro-output-manifest.json"),
                    ("recorded-output", args.evidence / f"{stem}-post-output-manifest.json"),
                ],
                args.evidence / f"{stem}-normalization.json",
            )
        except BaseException as error:
            failures.append(f"normalization failed: {type(error).__name__}: {error}")

    source_unchanged = False
    try:
        source_unchanged = git_state(args.astro_project) == initial_git
    except BaseException as error:
        failures.append(f"post-build Git verification failed: {error}")
    remote_inputs_unchanged = False
    bindings_unchanged = False
    try:
        remote_inputs_unchanged = verify_live_remote_inputs(args, archive_root)
    except BaseException as error:
        failures.append(f"remote-input verification failed: {error}")
    try:
        bindings_unchanged = bindings(args, archive_root) == expected_bindings
    except BaseException as error:
        failures.append(f"binding verification failed: {error}")

    infrastructure_valid = bool(
        completed is not None
        and completed.returncode == 0
        and record
        and record.get("schema") == "cp10-run"
        and record.get("schema_version") == 1
        and record.get("id") == identifier
        and record.get("series") == SERIES
        and record.get("scenario") == SCENARIO
        and record.get("tool") == "astro"
        and record.get("round") == round_number
        and record.get("warmth") == "warm"
        and record.get("working_directory") == str(args.astro_project)
        and record.get("command") == command
        and record.get("campaign_lock_inherited") is True
        and record.get("validity", {}).get("infrastructure_valid") is True
    )
    output_valid = bool(
        normalization_returncode == 0 and normalization_passed(normalization_report)
    )
    formal_valid = bool(
        not failures
        and infrastructure_valid
        and output_valid
        and source_unchanged
        and remote_inputs_unchanged
        and bindings_unchanged
    )
    validation = {
        "schema": "cp10-astro-final-incremental-run-validation",
        "schema_version": 1,
        "series": SERIES,
        "scenario": SCENARIO,
        "run_id": identifier,
        "round": round_number,
        "command": command,
        "environment": environment_binding(environment),
        "infrastructure_valid": infrastructure_valid,
        "normalized_output_valid": output_valid,
        "source_unchanged": source_unchanged,
        "remote_inputs_unchanged": remote_inputs_unchanged,
        "bindings_unchanged": bindings_unchanged,
        "formal_valid": formal_valid,
        "failures": failures,
        "normalization_report": f"{stem}-normalization.json",
        "normalization_returncode": normalization_returncode,
        "pre_output_manifest": f"{stem}-pre-output-manifest.json",
        "post_output_manifest": f"{stem}-post-output-manifest.json",
        "harness_record": f"{stem}.json",
    }
    atomic_json(args.evidence / f"{stem}-validation.json", validation)
    if not formal_valid:
        raise RuntimeError(
            f"invalid final Astro run preserved: {stem}; no summary was emitted"
        )
    return validation


def summary_payload(evidence: Path) -> dict[str, Any]:
    validations: list[dict[str, Any]] = []
    observations: list[dict[str, Any]] = []
    for round_number in ROUNDS:
        stem = f"astro-run{round_number:02d}"
        validation_path = evidence / f"{stem}-validation.json"
        record_path = evidence / f"{stem}.json"
        try:
            validation = json.loads(validation_path.read_text())
            record = json.loads(record_path.read_text())
        except (FileNotFoundError, json.JSONDecodeError, OSError) as error:
            raise ValueError(f"missing or malformed run {round_number} evidence") from error
        if (
            validation.get("schema")
            != "cp10-astro-final-incremental-run-validation"
            or validation.get("round") != round_number
            or validation.get("formal_valid") is not True
            or record.get("schema") != "cp10-run"
            or record.get("id") != validation.get("run_id")
            or record.get("round") != round_number
            or record.get("command") != validation.get("command")
            or record.get("validity", {}).get("infrastructure_valid") is not True
        ):
            raise ValueError(f"refusing to summarize invalid run {round_number}")
        wall_seconds = record.get("time", {}).get("wall_seconds")
        peak_memory = record.get("cgroup", {}).get("memory_peak_bytes")
        if not isinstance(wall_seconds, (int, float)) or not isinstance(peak_memory, int):
            raise ValueError(f"run {round_number} lacks timing or memory evidence")
        validations.append(validation)
        observations.append(
            {
                "round": round_number,
                "run_id": validation["run_id"],
                "wall_seconds": wall_seconds,
                "cgroup_peak_memory_bytes": peak_memory,
                "validation": validation_path.name,
                "record": record_path.name,
            }
        )
    if [item["round"] for item in validations] != list(ROUNDS):
        raise ValueError("summary requires exactly rounds 1..3")
    return {
        "schema": "cp10-astro-final-incremental-summary",
        "schema_version": 1,
        "series": SERIES,
        "scenario": SCENARIO,
        "tool": "astro",
        "count": 3,
        "rounds": list(ROUNDS),
        "all_formal_valid": True,
        "observations": observations,
    }


def outcome_payload(evidence: Path) -> dict[str, Any]:
    observations: list[dict[str, Any]] = []
    for round_number in ROUNDS:
        stem = f"astro-run{round_number:02d}"
        try:
            validation = json.loads(
                (evidence / f"{stem}-validation.json").read_text()
            )
            record = json.loads((evidence / f"{stem}.json").read_text())
        except (FileNotFoundError, json.JSONDecodeError, OSError) as error:
            raise ValueError(
                f"missing or malformed run {round_number} evidence"
            ) from error
        if (
            validation.get("schema")
            != "cp10-astro-final-incremental-run-validation"
            or validation.get("round") != round_number
            or record.get("schema") != "cp10-run"
            or record.get("id") != validation.get("run_id")
            or record.get("round") != round_number
            or record.get("command") != validation.get("command")
        ):
            raise ValueError(f"invalid run {round_number} evidence identity")
        wall_seconds = record.get("time", {}).get("wall_seconds")
        peak_memory = record.get("cgroup", {}).get("memory_peak_bytes")
        if not isinstance(wall_seconds, (int, float)) or not isinstance(peak_memory, int):
            raise ValueError(f"run {round_number} lacks timing or memory evidence")
        observations.append(
            {
                "round": round_number,
                "run_id": validation["run_id"],
                "wall_seconds": wall_seconds,
                "cgroup_peak_memory_bytes": peak_memory,
                "infrastructure_valid": validation.get("infrastructure_valid") is True,
                "normalized_output_valid": validation.get("normalized_output_valid")
                is True,
                "formal_valid": validation.get("formal_valid") is True,
                "validation": f"{stem}-validation.json",
                "record": f"{stem}.json",
            }
        )
    formal_valid = [item for item in observations if item["formal_valid"]]
    return {
        "schema": "cp10-astro-final-incremental-outcome",
        "schema_version": 1,
        "series": SERIES,
        "scenario": SCENARIO,
        "tool": "astro",
        "count": len(observations),
        "rounds": list(ROUNDS),
        "all_infrastructure_valid": all(
            item["infrastructure_valid"] for item in observations
        ),
        "all_formal_valid": len(formal_valid) == len(observations),
        "formal_valid_count": len(formal_valid),
        "formal_invalid_rounds": [
            item["round"] for item in observations if not item["formal_valid"]
        ],
        "observed_metrics_all_invocations": {
            "wall_seconds": metric_summary(
                [float(item["wall_seconds"]) for item in observations]
            ),
            "cgroup_peak_memory_bytes": metric_summary(
                [float(item["cgroup_peak_memory_bytes"]) for item in observations]
            ),
        },
        "observations": observations,
    }


def run_campaign(args: argparse.Namespace) -> int:
    preflight_evidence(args.evidence)
    initial_git = git_state(args.astro_project)
    if initial_git["status"]:
        raise RuntimeError("Astro benchmark worktree is not clean")
    with remote_archive_root(args) as archive_root:
        expected_bindings = bindings(args, archive_root)
        campaign = {
            "schema": "cp10-astro-final-incremental-campaign",
            "schema_version": 1,
            "series": SERIES,
            "scenario": SCENARIO,
            "fixed_rounds": list(ROUNDS),
            "no_warmup": True,
            "no_clean_build": True,
            "project": str(args.astro_project),
            "git": initial_git,
            "bindings": expected_bindings,
        }
        atomic_json(args.evidence / "campaign.json", campaign)
        for round_number in ROUNDS:
            record_run(
                args, round_number, initial_git, expected_bindings, archive_root
            )
        atomic_json(args.evidence / SUMMARY_NAME, summary_payload(args.evidence))
    return 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--astro-project", required=True, type=Path)
    parser.add_argument("--baseline", required=True, type=Path)
    parser.add_argument("--harness", required=True, type=Path)
    parser.add_argument("--normalizer", required=True, type=Path)
    parser.add_argument("--remote-input-archive", required=True, type=Path)
    parser.add_argument("--remote-input-manifest", required=True, type=Path)
    parser.add_argument("--evidence", required=True, type=Path)
    parser.add_argument("--pnpm", required=True, type=Path)
    args = parser.parse_args(argv)
    for name in (
        "astro_project",
        "baseline",
        "harness",
        "normalizer",
        "remote_input_archive",
        "remote_input_manifest",
        "pnpm",
    ):
        value = getattr(args, name).resolve()
        if not value.exists():
            parser.error(f"--{name.replace('_', '-')} does not exist: {value}")
        setattr(args, name, value)
    if not args.astro_project.is_dir():
        parser.error("--astro-project must be a directory")
    if not args.baseline.is_dir():
        parser.error("--baseline must be a directory")
    for name in ("harness", "normalizer", "remote_input_manifest"):
        if not getattr(args, name).is_file():
            parser.error(f"--{name.replace('_', '-')} must be a file")
    if not args.remote_input_archive.is_dir() and not args.remote_input_archive.is_file():
        parser.error("--remote-input-archive must be a file or directory")
    if not args.pnpm.is_file() or not os.access(args.pnpm, os.X_OK):
        parser.error("--pnpm must be an executable file")
    args.evidence = args.evidence.resolve()
    args.astro_remote_input_archive = args.remote_input_archive
    args.astro_remote_input_manifest = args.remote_input_manifest
    args.astro_remote_input_archive_sha256 = (
        sha256_file(args.remote_input_archive)
        if args.remote_input_archive.is_file()
        else None
    )
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    with campaign_lock():
        assert_no_stale_benchmark_processes((args.astro_project,))
        return run_campaign(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileExistsError, FileNotFoundError, RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
