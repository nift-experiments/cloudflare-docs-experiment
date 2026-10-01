#!/usr/bin/env python3
"""Run the missing CP10 Nift-only normal-edit scenarios without tree manifests."""

from __future__ import annotations

import argparse
import json
import os
import re
import stat
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from .cp10_benchmark import atomic_json, campaign_lock, metric_summary, sha256_file
    from .cp10_formal_edit import (
        BATCH_NIFT_SOURCES,
        BATCH_OUTPUTS,
        MARKER,
        NIFT_SOURCE,
        OUTPUT,
    )
    from .cp10_formal_no_change import (
        assert_no_stale_benchmark_processes,
        copy_tree,
        git_state,
        remove_path,
        run,
    )
except ImportError:
    from cp10_benchmark import (  # type: ignore[no-redef]
        atomic_json,
        campaign_lock,
        metric_summary,
        sha256_file,
    )
    from cp10_formal_edit import (  # type: ignore[no-redef]
        BATCH_NIFT_SOURCES,
        BATCH_OUTPUTS,
        MARKER,
        NIFT_SOURCE,
        OUTPUT,
    )
    from cp10_formal_no_change import (  # type: ignore[no-redef]
        assert_no_stale_benchmark_processes,
        copy_tree,
        git_state,
        remove_path,
        run,
    )


SCHEMA_VERSION = 1
SERIES = "cp10-nift-only-normal-edit"
RUNS = 3
SHARED_META_MARKER = b'<meta name="cp10-benchmark" content="shared-template-edit">'
SHARED_REPRESENTATIVE_OUTPUTS = (
    OUTPUT,
    Path("d1/index.html"),
    Path("ssl/index.html"),
    Path("pages/index.html"),
    Path("radar/index.html"),
)
BUILT_RE = re.compile(
    r"\b(?P<count>\d+)\s+(?:specified\s+)?files?\s+(?:built|rebuilt)\s+successfully\b",
    re.I,
)
UP_TO_DATE_RE = re.compile(
    r"\b(?P<count>\d+)\s+(?:tracked\s+)?files?\s+(?:are\s+)?up[ -]to[ -]date\b",
    re.I,
)


@dataclass(frozen=True)
class ModeSpec:
    mode: str
    scenario: str
    sources: tuple[Path, ...]
    outputs: tuple[Path, ...]
    marker: bytes
    shared: bool = False


@dataclass(frozen=True)
class SourceState:
    data: bytes
    mode: int
    atime_ns: int
    mtime_ns: int


MODE_SPECS = {
    "one-normal": ModeSpec(
        "one-normal",
        "one-page-normal-incremental-nift-only",
        (NIFT_SOURCE,),
        (OUTPUT,),
        MARKER,
    ),
    "batch-normal": ModeSpec(
        "batch-normal",
        "five-page-normal-incremental-nift-only",
        BATCH_NIFT_SOURCES,
        BATCH_OUTPUTS,
        MARKER,
    ),
    "shared-normal": ModeSpec(
        "shared-normal",
        "shared-template-normal-incremental-nift-only",
        (Path("templates/head.html"),),
        SHARED_REPRESENTATIVE_OUTPUTS,
        SHARED_META_MARKER,
        shared=True,
    ),
}


def capture_source(path: Path) -> SourceState:
    item_stat = path.stat()
    data = path.read_bytes()
    return SourceState(
        data=data,
        mode=item_stat.st_mode,
        atime_ns=item_stat.st_atime_ns,
        mtime_ns=item_stat.st_mtime_ns,
    )


def source_identity(path: Path, state: SourceState) -> dict[str, Any]:
    item_stat = path.stat()
    return {
        "path": str(path),
        "bytes": len(state.data),
        "sha256": sha256_file(path, item_stat),
        "mode": f"{stat.S_IMODE(item_stat.st_mode):04o}",
        "atime_ns": state.atime_ns,
        "mtime_ns": state.mtime_ns,
    }


def restore_source(path: Path, state: SourceState) -> bool:
    path.write_bytes(state.data)
    os.chmod(path, stat.S_IMODE(state.mode))
    bytes_equal = path.read_bytes() == state.data
    os.utime(path, ns=(state.atime_ns, state.mtime_ns))
    restored = path.stat()
    return bool(
        bytes_equal
        and restored.st_mode == state.mode
        and restored.st_atime_ns == state.atime_ns
        and restored.st_mtime_ns == state.mtime_ns
    )


def edited_bytes(original: bytes, spec: ModeSpec) -> bytes:
    if spec.shared:
        separator = b"" if original.endswith(b"\n") else b"\n"
    else:
        separator = b"\n" if original.endswith(b"\n") else b"\n\n"
    return original + separator + spec.marker + b"\n"


def apply_edits(
    project: Path, spec: ModeSpec, states: dict[Path, SourceState]
) -> list[dict[str, Any]]:
    evidence = []
    for relative in spec.sources:
        path = project / relative
        original = states[relative]
        if path.read_bytes() != original.data:
            raise RuntimeError(f"source differs before edit: {path}")
        path.write_bytes(edited_bytes(original.data, spec))
        os.chmod(path, stat.S_IMODE(original.mode))
        count = path.read_bytes().count(spec.marker)
        if count != 1:
            raise RuntimeError(f"source marker was not applied exactly once: {path}")
        evidence.append(
            {"path": relative.as_posix(), "marker_count": count, "sha256": sha256_file(path)}
        )
    return evidence


def parse_nift_stdout(text: str) -> dict[str, int]:
    built = [int(match.group("count")) for match in BUILT_RE.finditer(text)]
    up_to_date = [int(match.group("count")) for match in UP_TO_DATE_RE.finditer(text)]
    if len(built) > 1 or len(up_to_date) > 1 or not (built or up_to_date):
        raise ValueError("Nift stdout has missing or ambiguous built/up-to-date counts")
    return {
        "built": built[0] if built else 0,
        "up_to_date": up_to_date[0] if up_to_date else 0,
    }


def output_hash(path: Path) -> str:
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"designated output is not a regular file: {path}")
    return sha256_file(path)


def validate_outputs(
    output_root: Path,
    outputs: tuple[Path, ...],
    marker: bytes,
    baseline_hashes: dict[str, str],
) -> list[dict[str, Any]]:
    validations = []
    for relative in outputs:
        path = output_root / relative
        regular_file = path.is_file() and not path.is_symlink()
        data = path.read_bytes() if regular_file else b""
        observed_hash = sha256_file(path) if regular_file else None
        marker_count = data.count(marker)
        changed = (
            observed_hash is not None
            and observed_hash != baseline_hashes[relative.as_posix()]
        )
        validations.append(
            {
                "path": relative.as_posix(),
                "regular_file": regular_file,
                "marker_count": marker_count,
                "baseline_sha256": baseline_hashes[relative.as_posix()],
                "observed_sha256": observed_hash,
                "hash_changed": changed,
                "passed": regular_file and marker_count == 1 and changed,
            }
        )
    return validations


def copy_file_exact(source: Path, destination: Path) -> None:
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"refusing to overwrite snapshot: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    run(["cp", "-a", "--reflink=auto", "--", str(source), str(destination)])


def replace_file_exact(source: Path, destination: Path) -> None:
    if destination.is_dir() and not destination.is_symlink():
        raise RuntimeError(f"refusing to replace directory with file: {destination}")
    destination.unlink(missing_ok=True)
    copy_file_exact(source, destination)


def restore_baseline(project: Path, baseline: Path, spec: ModeSpec) -> None:
    metadata = project / ".nift/public"
    remove_path(metadata)
    copy_tree(baseline / "nift-metadata", metadata)
    if spec.shared:
        output_root = project / "public"
        remove_path(output_root)
        copy_tree(baseline / "public", output_root)
        return
    for relative in spec.outputs:
        replace_file_exact(baseline / "outputs" / relative, project / "public" / relative)


def baseline_restored(
    project: Path, spec: ModeSpec, baseline_hashes: dict[str, str]
) -> bool:
    if not (project / ".nift/public").is_dir():
        return False
    return all(
        output_hash(project / "public" / relative) == baseline_hashes[relative.as_posix()]
        for relative in spec.outputs
    )


def tracked_count(project: Path) -> int:
    tracked = json.loads((project / ".nift/tracked.json").read_text()).get("tracked")
    if not isinstance(tracked, list) or not tracked:
        raise ValueError(".nift/tracked.json has no non-empty tracked list")
    return len(tracked)


def prepare_baseline(
    args: argparse.Namespace,
    spec: ModeSpec,
    git_before: dict[str, str],
    states: dict[Path, SourceState],
) -> tuple[dict[str, str], int]:
    baseline = args.evidence / "baseline"
    baseline.mkdir(parents=True)
    metadata = args.project / ".nift/public"
    if not metadata.is_dir():
        raise FileNotFoundError(f"Nift baseline metadata is absent: {metadata}")
    copy_tree(metadata, baseline / "nift-metadata")
    if spec.shared:
        copy_tree(args.project / "public", baseline / "public")
    else:
        for relative in spec.outputs:
            copy_file_exact(args.project / "public" / relative, baseline / "outputs" / relative)

    source_records = []
    for relative, state in states.items():
        path = args.project / relative
        copy_file_exact(path, baseline / "sources" / relative)
        source_records.append(source_identity(path, state))

    hashes = {
        relative.as_posix(): output_hash(args.project / "public" / relative)
        for relative in spec.outputs
    }
    if any(
        (args.project / "public" / relative).read_bytes().count(spec.marker)
        for relative in spec.outputs
    ):
        raise RuntimeError("edit marker is already present in a designated baseline output")
    count = tracked_count(args.project)
    scope = (
        "Shared fan-out is inferred from Nift's reported regenerated count and marker/hash "
        "checks on the frozen representative set; outputs outside that set are not hashed."
        if spec.shared
        else "Only intended outputs are marker-checked and hashed; the remaining output tree is not walked."
    )
    atomic_json(
        args.evidence / "setup.json",
        {
            "schema": "cp10-nift-edit-setup",
            "schema_version": SCHEMA_VERSION,
            "mode": spec.mode,
            "series": SERIES,
            "scenario": spec.scenario,
            "git": git_before,
            "command": [str(args.nift_bin), "build"],
            "harness": {"path": str(args.harness), "sha256": sha256_file(args.harness)},
            "sources": source_records,
            "source_byte_snapshots": [
                str((baseline / "sources" / relative).relative_to(args.evidence))
                for relative in spec.sources
            ],
            "designated_outputs": [relative.as_posix() for relative in spec.outputs],
            "baseline_output_sha256": hashes,
            "tracked_count": count,
            "baseline_restore": (
                "one-time reflink snapshot of .nift/public and public"
                if spec.shared
                else "one-time reflink snapshot of .nift/public and intended outputs only"
            ),
            "validation_scope": scope,
            "whole_site_manifests_or_per_run_scans": False,
        },
    )
    return hashes, count


def metric_with_range(values: list[float]) -> dict[str, float]:
    summary = metric_summary(values)
    return {
        "median": summary["median"],
        "mean": summary["mean"],
        "minimum": summary["minimum"],
        "maximum": summary["maximum"],
        "range": summary["maximum"] - summary["minimum"],
        "population_standard_deviation": summary["population_standard_deviation"],
    }


def execute_attempt(
    args: argparse.Namespace,
    spec: ModeSpec,
    states: dict[Path, SourceState],
    baseline_hashes: dict[str, str],
    expected_tracked_count: int,
    *,
    label: str,
    round_number: int,
    measured: bool,
) -> dict[str, Any]:
    baseline = args.evidence / "baseline"
    stem = args.evidence / label
    errors: list[str] = []
    record: dict[str, Any] | None = None
    counts: dict[str, int] | None = None
    outputs: list[dict[str, Any]] = []
    edit_evidence: list[dict[str, Any]] = []
    source_restored = False
    state_restored = False
    infrastructure_valid = not measured
    try:
        assert_no_stale_benchmark_processes((args.project,))
        restore_baseline(args.project, baseline, spec)
        if not baseline_restored(args.project, spec, baseline_hashes):
            raise RuntimeError("Nift baseline was not restored before edit")
        edit_evidence = apply_edits(args.project, spec, states)
        environment = os.environ.copy()
        environment["LC_ALL"] = "C"
        environment.pop("INCREMENTAL_BUILD", None)
        command = [str(args.nift_bin), "build"]
        if measured:
            completed = run(
                [
                    sys.executable,
                    str(args.harness),
                    "run",
                    "--id",
                    f"{SERIES}-{spec.mode}-run{round_number:02d}",
                    "--series",
                    SERIES,
                    "--scenario",
                    spec.scenario,
                    "--tool",
                    "nift",
                    "--round",
                    str(round_number),
                    "--warmth",
                    "warm",
                    "--output",
                    str(stem.with_suffix(".json")),
                    "--cwd",
                    str(args.project),
                    "--",
                    *command,
                ],
                env=environment,
                check=False,
            )
            if stem.with_suffix(".json").is_file():
                record = json.loads(stem.with_suffix(".json").read_text())
                infrastructure_valid = record.get("validity", {}).get("infrastructure_valid") is True
            if completed.returncode:
                errors.append(f"harness exit code {completed.returncode}")
        else:
            with (args.evidence / f"{label}.stdout.log").open("x") as stdout, (
                args.evidence / f"{label}.stderr.log"
            ).open("x") as stderr:
                completed = run(
                    command,
                    args.project,
                    env=environment,
                    stdout=stdout,
                    stderr=stderr,
                    check=False,
                )
            if completed.returncode:
                errors.append(f"warmup exit code {completed.returncode}")
        counts = parse_nift_stdout(
            (args.evidence / f"{label}.stdout.log").read_text(errors="replace")
        )
        outputs = validate_outputs(
            args.project / "public", spec.outputs, spec.marker, baseline_hashes
        )
        expected_built = expected_tracked_count if spec.shared else len(spec.outputs)
        if counts["built"] != expected_built:
            errors.append(
                f"Nift reported {counts['built']} built files; expected {expected_built}"
            )
        if not all(item["passed"] for item in outputs):
            errors.append("designated output marker/hash validation failed")
    except Exception as error:
        errors.append(f"attempt failed: {error}")
    finally:
        try:
            source_results = [
                restore_source(args.project / relative, states[relative])
                for relative in spec.sources
            ]
            source_restored = all(source_results)
            if not source_restored:
                errors.append("source restoration was not byte/mode/time exact")
        except Exception as error:
            errors.append(f"source restoration failed: {error}")
        try:
            assert_no_stale_benchmark_processes((args.project,))
            restore_baseline(args.project, baseline, spec)
            state_restored = baseline_restored(args.project, spec, baseline_hashes)
            if not state_restored:
                errors.append("Nift baseline restoration failed")
        except Exception as error:
            errors.append(f"Nift baseline restoration failed: {error}")

    formal_valid = bool(
        not errors
        and infrastructure_valid
        and counts is not None
        and outputs
        and all(item["passed"] for item in outputs)
        and source_restored
        and state_restored
    )
    validation = {
        "schema": "cp10-nift-edit-run-validation",
        "schema_version": SCHEMA_VERSION,
        "mode": spec.mode,
        "label": label,
        "round": round_number,
        "measured": measured,
        "formal_valid": formal_valid,
        "infrastructure_valid": infrastructure_valid,
        "errors": errors,
        "reported_counts": counts,
        "source_edits": edit_evidence,
        "designated_outputs": outputs,
        "source_restored_exactly": source_restored,
        "baseline_restored": state_restored,
        "validation_scope": (
            "frozen representative set; no all-page hashes"
            if spec.shared
            else "intended outputs only; no output-tree walk"
        ),
        "wall_seconds": record.get("time", {}).get("wall_seconds") if record else None,
        "aggregate_peak_memory_bytes": (
            record.get("cgroup", {}).get("memory_peak_bytes") if record else None
        ),
        "gnu_peak_rss_kib": (
            record.get("time", {}).get("maximum_rss_kib") if record else None
        ),
    }
    atomic_json(args.evidence / f"{label}-validation.json", validation)
    if not formal_valid:
        raise RuntimeError(f"invalid {label} evidence preserved")
    return validation


def run_campaign(args: argparse.Namespace) -> int:
    if args.evidence.exists() and not args.evidence.is_dir():
        raise ValueError(f"evidence path is not a directory: {args.evidence}")
    args.evidence.mkdir(parents=True, exist_ok=True)
    if any(args.evidence.iterdir()):
        raise FileExistsError(f"evidence directory must be empty: {args.evidence}")
    git_before = git_state(args.project)
    if git_before["status"]:
        raise RuntimeError("Nift benchmark worktree is not clean")
    spec = MODE_SPECS[args.mode]
    states = {relative: capture_source(args.project / relative) for relative in spec.sources}
    baseline_hashes, expected_tracked_count = prepare_baseline(
        args, spec, git_before, states
    )
    execute_attempt(
        args,
        spec,
        states,
        baseline_hashes,
        expected_tracked_count,
        label="warmup",
        round_number=0,
        measured=False,
    )
    validations = [
        execute_attempt(
            args,
            spec,
            states,
            baseline_hashes,
            expected_tracked_count,
            label=f"run{number:02d}",
            round_number=number,
            measured=True,
        )
        for number in range(1, RUNS + 1)
    ]
    metrics = {
        "wall_seconds": metric_with_range([item["wall_seconds"] for item in validations]),
        "aggregate_peak_memory_bytes": metric_with_range(
            [item["aggregate_peak_memory_bytes"] for item in validations]
        ),
        "gnu_peak_rss_kib": metric_with_range(
            [item["gnu_peak_rss_kib"] for item in validations]
        ),
    }
    atomic_json(
        args.evidence / "summary.json",
        {
            "schema": "cp10-nift-edit-summary",
            "schema_version": SCHEMA_VERSION,
            "mode": spec.mode,
            "series": SERIES,
            "scenario": spec.scenario,
            "count": RUNS,
            "runs": [f"run{number:02d}" for number in range(1, RUNS + 1)],
            "metrics": metrics,
            "reported_counts": [item["reported_counts"] for item in validations],
            "validation_scope": validations[0]["validation_scope"],
            "shared_fanout_limitation": (
                "Regeneration outside the representative set is supported by Nift stdout only; "
                "those pages were not individually hashed or marker-checked."
                if spec.shared
                else None
            ),
            "whole_site_manifests_or_per_run_scans": False,
        },
    )
    return 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=tuple(MODE_SPECS))
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--harness", required=True, type=Path)
    parser.add_argument("--evidence", required=True, type=Path)
    parser.add_argument("--nift-bin", default=Path("/usr/local/bin/nift"), type=Path)
    args = parser.parse_args(argv)
    for name in ("project", "harness", "nift_bin"):
        value = getattr(args, name).resolve()
        if not value.exists():
            parser.error(f"--{name.replace('_', '-')} does not exist: {value}")
        setattr(args, name, value)
    if not args.project.is_dir():
        parser.error("--project must be a directory")
    if not args.harness.is_file():
        parser.error("--harness must be a file")
    if not args.nift_bin.is_file() or not os.access(args.nift_bin, os.X_OK):
        parser.error("--nift-bin must be executable")
    args.evidence = args.evidence.resolve()
    if args.evidence == args.project or args.evidence in args.project.parents:
        parser.error("--evidence must not contain --project")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    with campaign_lock():
        assert_no_stale_benchmark_processes((args.project,))
        return run_campaign(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileExistsError, FileNotFoundError, RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
