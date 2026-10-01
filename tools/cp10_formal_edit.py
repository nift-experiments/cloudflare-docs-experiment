#!/usr/bin/env python3
"""Collect CP10 methodology-v6 edit scenarios C through F."""

from __future__ import annotations

import argparse
import json
import os
import stat as stat_module
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from .cp10_benchmark import (
        atomic_json,
        campaign_lock,
        compare_manifests,
        load_manifest,
        manifest_payload,
        sha256_file,
    )
    from .cp10_formal_no_change import (
        clean_astro,
        clean_nift,
        assert_no_stale_benchmark_processes,
        command_for,
        copy_tree,
        git_state,
        normalization_passed,
        open_exclusive,
        restore_states,
        prepare_remote_archive,
        restore_astro_remote_inputs,
        run,
        run_normalizer,
        snapshot_states,
        StatePath,
        states_for,
    )
except ImportError:
    from cp10_benchmark import (  # type: ignore[no-redef]
        atomic_json,
        campaign_lock,
        compare_manifests,
        load_manifest,
        manifest_payload,
        sha256_file,
    )
    from cp10_formal_no_change import (  # type: ignore[no-redef]
        clean_astro,
        clean_nift,
        assert_no_stale_benchmark_processes,
        command_for,
        copy_tree,
        git_state,
        normalization_passed,
        open_exclusive,
        restore_states,
        prepare_remote_archive,
        restore_astro_remote_inputs,
        run,
        run_normalizer,
        snapshot_states,
        StatePath,
        states_for,
    )


MARKER = b"CP10 benchmark edit."
NIFT_SOURCE = Path("content/workers/get-started/guide/index.md")
ASTRO_SOURCE = Path("src/content/docs/workers/get-started/guide.mdx")
OUTPUT = Path("workers/get-started/guide/index.html")
NIFT_TARGET = "workers/get-started/guide/"
NORMAL_ORDER = ("nift", "astro", "astro")
NORMAL_RUNS = 3
TARGET_WARMUPS = 3
TARGET_RUNS = 30
SCHEMA_VERSION = 3
SHARED_MARKER = b'<meta name="cp10-benchmark" content="shared-template-edit">'
BATCH_TARGETS = (
    "workers/get-started/",
    "workers/get-started/guide/",
    "workers/get-started/dashboard/",
    "workers/get-started/prompting/",
    "workers/get-started/quickstarts/",
)
BATCH_OUTPUTS = tuple(Path(target) / "index.html" for target in BATCH_TARGETS)
BATCH_NIFT_SOURCES = tuple(Path("content") / target / "index.md" for target in BATCH_TARGETS)
BATCH_ASTRO_SOURCES = tuple(
    Path("src/content/docs/workers/get-started") / name
    for name in ("index.mdx", "guide.mdx", "dashboard.mdx", "prompting.mdx", "quickstarts.mdx")
)


@dataclass(frozen=True)
class SeriesSpec:
    mode: str
    scenario: str
    paired: bool
    warmups: int
    runs: int
    marker: bytes
    nift_sources: tuple[Path, ...]
    astro_sources: tuple[Path, ...]
    outputs: tuple[Path, ...]
    nift_targets: tuple[str, ...] = ()
    paragraph: bool = True


SERIES_SPECS = {
    "batch-normal": SeriesSpec(
        "batch-normal", "five-page-normal-incremental", True, 1, 3, MARKER,
        BATCH_NIFT_SOURCES, BATCH_ASTRO_SOURCES, BATCH_OUTPUTS,
    ),
    "batch-targeted": SeriesSpec(
        "batch-targeted", "five-page-explicit-target", False, 2, 20, MARKER,
        BATCH_NIFT_SOURCES, (), BATCH_OUTPUTS, BATCH_TARGETS,
    ),
    "shared-normal": SeriesSpec(
        "shared-normal", "shared-template-normal-incremental", True, 1, 3,
        SHARED_MARKER, (Path("templates/head.html"),),
        (Path("src/layouts/BaseLayout.astro"),), (OUTPUT,), paragraph=False,
    ),
}


@dataclass(frozen=True)
class SourceState:
    data: bytes
    mode: int
    atime_ns: int
    mtime_ns: int


def source_path(args: argparse.Namespace, tool: str) -> Path:
    project = args.nift_project if tool == "nift" else args.astro_project
    return project / (NIFT_SOURCE if tool == "nift" else ASTRO_SOURCE)


def capture_source(path: Path) -> SourceState:
    stat = path.stat()
    return SourceState(path.read_bytes(), stat.st_mode, stat.st_atime_ns, stat.st_mtime_ns)


def edited_bytes(original: bytes) -> bytes:
    separator = b"\n" if original.endswith(b"\n") else b"\n\n"
    return original + separator + MARKER + b"\n"


def series_edited_bytes(original: bytes, spec: SeriesSpec, tool: str) -> bytes:
    if spec.paragraph:
        separator = b"\n" if original.endswith(b"\n") else b"\n\n"
        return original + separator + spec.marker + b"\n"
    if tool == "astro" and not original.rstrip().endswith(b"</html>"):
        raise ValueError("Astro shared-template source does not end with </html>")
    separator = b"" if original.endswith(b"\n") else b"\n"
    return original + separator + spec.marker + b"\n"


def series_source_paths(args: argparse.Namespace, spec: SeriesSpec, tool: str) -> tuple[Path, ...]:
    project = args.nift_project if tool == "nift" else args.astro_project
    relative = spec.nift_sources if tool == "nift" else spec.astro_sources
    return tuple(project / path for path in relative)


def apply_series_edits(
    paths: tuple[Path, ...], states: dict[str, SourceState], spec: SeriesSpec, tool: str
) -> list[dict[str, Any]]:
    evidence = []
    for path in paths:
        original = states[str(path)]
        if path.read_bytes() != original.data:
            raise RuntimeError(f"source differs before edit: {path}")
        path.write_bytes(series_edited_bytes(original.data, spec, tool))
        os.chmod(path, original.mode)
        count = path.read_bytes().count(spec.marker)
        if count != 1:
            raise RuntimeError(f"source marker was not applied exactly once: {path}")
        evidence.append({"path": str(path), "marker_count": count, "sha256": sha256_file(path)})
    return evidence


def restore_series_sources(
    paths: tuple[Path, ...], states: dict[str, SourceState]
) -> bool:
    restored = [restore_source(path, states[str(path)]) for path in paths]
    return all(item["bytes_equal"] and item["mtime_equal"] for item in restored)


def series_marker_evidence(root: Path, spec: SeriesSpec) -> list[dict[str, Any]]:
    evidence = []
    for relative in spec.outputs:
        path = root / relative
        count = path.read_bytes().count(spec.marker) if path.is_file() else 0
        evidence.append(
            {
                "designated_path": relative.as_posix(),
                "path": str(path),
                "regular_file": path.is_file() and not path.is_symlink(),
                "marker_count": count,
                "passed": path.is_file() and not path.is_symlink() and count == 1,
            }
        )
    return evidence


def series_command(
    args: argparse.Namespace, spec: SeriesSpec, tool: str
) -> tuple[list[str], dict[str, str]]:
    command, environment = command_for(tool, args.nift_bin, args.pnpm_bin)
    if spec.mode == "batch-targeted":
        command = [str(args.nift_bin), "build", *spec.nift_targets]
    return command, environment


def apply_edit(path: Path, original: SourceState) -> dict[str, Any]:
    if path.read_bytes() != original.data:
        raise RuntimeError(f"source differs before edit: {path}")
    before_mtime = path.stat().st_mtime_ns
    path.write_bytes(edited_bytes(original.data))
    os.chmod(path, original.mode)
    data = path.read_bytes()
    if data.count(MARKER) != 1:
        raise RuntimeError(f"source marker was not applied exactly once: {path}")
    return {
        "path": str(path),
        "baseline_sha256": sha256_bytes(original.data),
        "edited_sha256": sha256_file(path),
        "baseline_mtime_ns": before_mtime,
        "edited_mtime_ns": path.stat().st_mtime_ns,
        "marker_count": data.count(MARKER),
    }


def restore_source(path: Path, original: SourceState) -> dict[str, Any]:
    path.write_bytes(original.data)
    os.chmod(path, original.mode)
    os.utime(path, ns=(original.atime_ns, original.mtime_ns))
    return {
        "bytes_equal": path.read_bytes() == original.data,
        "sha256": sha256_file(path),
        "mtime_ns": path.stat().st_mtime_ns,
        "mtime_equal": path.stat().st_mtime_ns == original.mtime_ns,
    }


def sha256_bytes(data: bytes) -> str:
    import hashlib

    return hashlib.sha256(data).hexdigest()


def project_for(args: argparse.Namespace, tool: str) -> Path:
    return args.nift_project if tool == "nift" else args.astro_project


def clean_reference_command(
    args: argparse.Namespace, tool: str
) -> tuple[list[str], dict[str, str]]:
    command, environment = command_for(tool, args.nift_bin, args.pnpm_bin)
    if tool == "nift":
        return [str(args.nift_bin), "build", "--all"], environment
    environment.pop("INCREMENTAL_BUILD", None)
    return command, environment


def recorded_command(
    args: argparse.Namespace, tool: str, targeted: bool = False
) -> tuple[list[str], dict[str, str]]:
    command, environment = command_for(tool, args.nift_bin, args.pnpm_bin)
    if targeted:
        if tool != "nift":
            raise ValueError("Astro has no explicit targeted production command")
        command = [str(args.nift_bin), "build", NIFT_TARGET]
    return command, environment


def relevant_environment(environment: dict[str, str]) -> dict[str, str | None]:
    return {
        "INCREMENTAL_BUILD": environment.get("INCREMENTAL_BUILD"),
        "NODE_OPTIONS": environment.get("NODE_OPTIONS"),
        "LC_ALL": environment.get("LC_ALL"),
    }


def untimed_command(
    label: str,
    command: list[str],
    project: Path,
    environment: dict[str, str],
    evidence: Path,
) -> None:
    with open_exclusive(evidence / f"{label}.stdout.log") as stdout, open_exclusive(
        evidence / f"{label}.stderr.log"
    ) as stderr:
        run(command, project, env=environment, stdout=stdout, stderr=stderr)


def expected_manifest(args: argparse.Namespace, tool: str) -> Path:
    return args.evidence / f"setup/references/{tool}-edited-manifest.json"


def changed_path_contract_path(args: argparse.Namespace, tool: str) -> Path:
    return args.evidence / f"setup/references/{tool}-changed-path-contract.json"


def copy_file_exact(source: Path, destination: Path) -> None:
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"refusing to overwrite snapshot: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    run(["cp", "-a", "--reflink=auto", "--", str(source), str(destination)])


def restore_file_exact(source: Path, destination: Path) -> None:
    if destination.is_dir() and not destination.is_symlink():
        raise RuntimeError(f"refusing to replace directory with file: {destination}")
    destination.unlink(missing_ok=True)
    copy_file_exact(source, destination)


def file_identity(path: Path) -> dict[str, Any]:
    stat = path.stat()
    return {
        "path": str(path),
        "mode": f"{stat.st_mode & 0o7777:04o}",
        "size": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
        "sha256": sha256_file(path, stat),
    }


def semantic_subset_digest(manifest: dict[str, Any], excluded: set[str]) -> str:
    entries = [
        {key: value for key, value in entry.items() if key not in {"mode", "mtime_ns"}}
        for entry in manifest["entries"]
        if entry["path"] not in excluded
    ]
    return sha256_bytes(
        json.dumps(entries, sort_keys=True, separators=(",", ":")).encode()
    )


def manifest_payload_reusing(
    root: Path,
    trusted: dict[str, Any],
    force_hash: set[str] | None = None,
) -> dict[str, Any]:
    """Build a complete manifest while rehashing only metadata-changed files."""
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f"manifest root is not a directory: {root}")
    previous = {entry["path"]: entry for entry in trusted["entries"]}
    force_hash = force_hash or set()
    entries: list[dict[str, Any]] = []
    hashed = 0
    reused = 0
    for current, dirnames, filenames in os.walk(root, followlinks=False):
        dirnames.sort()
        filenames.sort()
        current_path = Path(current)
        for name in [*dirnames, *filenames]:
            path = current_path / name
            relative = path.relative_to(root).as_posix()
            item_stat = path.lstat()
            entry: dict[str, Any] = {
                "path": relative,
                "mode": f"{item_stat.st_mode & 0o7777:04o}",
                "mtime_ns": item_stat.st_mtime_ns,
            }
            old = previous.get(relative)
            if path.is_symlink():
                entry.update(type="symlink", target=os.readlink(path))
                if name in dirnames:
                    dirnames.remove(name)
            elif stat_module.S_ISDIR(item_stat.st_mode):
                entry["type"] = "directory"
            elif stat_module.S_ISREG(item_stat.st_mode):
                entry.update(type="file", size=item_stat.st_size)
                if (
                    old
                    and relative not in force_hash
                    and old.get("type") == "file"
                    and old.get("size") == item_stat.st_size
                    and old.get("mtime_ns") == item_stat.st_mtime_ns
                ):
                    entry["sha256"] = old["sha256"]
                    reused += 1
                else:
                    entry["sha256"] = sha256_file(path, item_stat)
                    hashed += 1
            else:
                raise ValueError(f"unsupported filesystem object: {path}")
            entries.append(entry)
    entries.sort(key=lambda item: item["path"])
    files = [entry for entry in entries if entry["type"] == "file"]
    return {
        "schema": "cp10-tree-manifest",
        "schema_version": 1,
        "root_label": root.name,
        "entries_sha256": sha256_bytes(
            json.dumps(
                entries, sort_keys=True, separators=(",", ":"), ensure_ascii=True
            ).encode()
        ),
        "summary": {
            "entries": len(entries),
            "files": len(files),
            "bytes": sum(entry["size"] for entry in files),
        },
        "entries": entries,
        "hashing": {"files_hashed": hashed, "certified_hashes_reused": reused},
    }


def diff_path_sets(difference: dict[str, Any]) -> dict[str, list[str]]:
    return {
        key: sorted(difference[key]) for key in ("added", "removed", "changed")
    }


def changed_path_classification(
    expected: dict[str, list[str]], observed: dict[str, list[str]]
) -> dict[str, Any]:
    missing = {
        key: sorted(set(expected[key]) - set(observed[key]))
        for key in ("added", "removed", "changed")
    }
    unexpected = {
        key: sorted(set(observed[key]) - set(expected[key]))
        for key in ("added", "removed", "changed")
    }
    return {
        "expected": expected,
        "observed": observed,
        "missing_expected": missing,
        "unexpected_unclassified": unexpected,
        "all_expected_dependents_changed": not any(missing.values()),
        "no_unclassified_output_changed": not any(unexpected.values()),
        "matches": not any(missing.values()) and not any(unexpected.values()),
    }


def marker_evidence(root: Path) -> dict[str, Any]:
    page = root / OUTPUT
    if not page.is_file() or page.is_symlink():
        return {
            "designated_path": OUTPUT.as_posix(),
            "path": str(page),
            "regular_file": False,
            "marker_count": 0,
            "passed": False,
        }
    count = page.read_bytes().count(MARKER)
    return {
        "designated_path": OUTPUT.as_posix(),
        "path": str(page),
        "regular_file": True,
        "sha256": sha256_file(page),
        "marker_count": count,
        "passed": count == 1,
    }


def astro_normalized_change_set(
    report: dict[str, Any] | None, before: str, after: str
) -> dict[str, Any]:
    if not report or report.get("schema") != "cp10-astro-normalization-report":
        raise ValueError("missing Astro normalization classification report")
    if report.get("rejected"):
        raise ValueError("Astro normalization rejected a candidate difference")
    comparisons = [
        item
        for item in report.get("comparisons", [])
        if item.get("before") == before and item.get("after") == after
    ]
    if len(comparisons) != 1:
        raise ValueError("Astro normalization comparison labels are incomplete")
    comparison = comparisons[0]
    paths = diff_path_sets(comparison["normalized"])
    residual = sorted({path for values in paths.values() for path in values})
    if comparison.get("unclassified") != residual or report.get("unclassified") != residual:
        raise ValueError("Astro normalization residual classification is inconsistent")
    return {
        "paths": paths,
        "normalized_residual_paths": residual,
        "normalizer_categories": comparison.get("categories", {}),
        "normalizer_rejected": report["rejected"],
    }


def validate_changed_path_contract(contract: dict[str, Any], tool: str) -> None:
    expected = contract.get("expected_changed_paths")
    if (
        contract.get("schema") != "cp10-edit-changed-path-contract"
        or contract.get("schema_version") != 1
        or contract.get("tool") != tool
        or not isinstance(expected, dict)
        or set(expected) != {"added", "removed", "changed"}
        or any(values != sorted(set(values)) for values in expected.values())
        or OUTPUT.as_posix() not in expected["changed"]
        or contract.get("designated_output_marker", {}).get("passed") is not True
        or (
            tool == "astro"
            and not isinstance(contract.get("normalizer_report"), dict)
        )
    ):
        raise ValueError(f"invalid {tool} changed-path contract")


def freeze_changed_path_contract(
    args: argparse.Namespace, tool: str, reference_root: Path
) -> dict[str, Any]:
    marker = marker_evidence(reference_root)
    if not marker["passed"]:
        raise RuntimeError(f"edited {tool} designated output marker check failed")
    normalizer_evidence: dict[str, Any] | None = None
    normalizer_report_binding: dict[str, Any] | None = None
    if tool == "nift":
        expected = diff_path_sets(
            compare_manifests(
                load_manifest(args.nift_expected),
                load_manifest(expected_manifest(args, tool)),
            )
        )
        basis = "raw-content-manifest-diff"
    else:
        report_path = args.evidence / "setup/references/astro-clean-to-edited-normalization.json"
        report, returncode = run_normalizer(
            args.astro_normalizer,
            [
                ("clean-unedited-reference", args.astro_clean_reference),
                ("clean-edited-reference", reference_root),
            ],
            [
                ("clean-unedited-reference", args.astro_clean_reference_manifest),
                ("clean-edited-reference", expected_manifest(args, tool)),
            ],
            report_path,
        )
        if returncode != 1:
            raise RuntimeError("Astro clean-to-edited reference did not produce one declared edit")
        normalizer_evidence = astro_normalized_change_set(
            report, "clean-unedited-reference", "clean-edited-reference"
        )
        normalizer_report_binding = {
            "path": str(report_path),
            "sha256": sha256_file(report_path),
            "returncode": returncode,
        }
        expected = normalizer_evidence["paths"]
        basis = "strict-normalized-content-diff"
    if OUTPUT.as_posix() not in expected["changed"]:
        raise RuntimeError(f"{tool} clean reference did not change designated output page")
    contract = {
        "schema": "cp10-edit-changed-path-contract",
        "schema_version": 1,
        "tool": tool,
        "basis": basis,
        "clean_manifest": (
            str(args.nift_expected)
            if tool == "nift"
            else str(args.astro_clean_reference_manifest)
        ),
        "edited_manifest": str(expected_manifest(args, tool)),
        "expected_changed_paths": expected,
        "expected_dependents": sorted(
            {path for values in expected.values() for path in values}
        ),
        "designated_output_marker": marker,
        "normalizer_classification": normalizer_evidence,
        "normalizer_report": normalizer_report_binding,
    }
    validate_changed_path_contract(contract, tool)
    atomic_json(changed_path_contract_path(args, tool), contract)
    return contract


def series_contract_path(args: argparse.Namespace, tool: str) -> Path:
    return args.evidence / f"setup/references/{tool}-series-changed-path-contract.json"


def freeze_series_contract(
    args: argparse.Namespace,
    spec: SeriesSpec,
    tool: str,
    reference_root: Path,
    edited_manifest_path: Path,
) -> dict[str, Any]:
    markers = series_marker_evidence(reference_root, spec)
    if not all(item["passed"] for item in markers):
        raise RuntimeError(f"{tool} {spec.mode} designated marker check failed")
    normalizer = None
    if tool == "nift":
        paths = diff_path_sets(
            compare_manifests(load_manifest(args.nift_expected), load_manifest(edited_manifest_path))
        )
        basis = "raw-content-manifest-diff"
    else:
        report_path = args.evidence / "setup/references/astro-series-clean-to-edited-normalization.json"
        report, returncode = run_normalizer(
            args.astro_normalizer,
            [("clean-unedited-reference", args.astro_clean_reference), ("clean-edited-reference", reference_root)],
            [("clean-unedited-reference", args.astro_clean_reference_manifest), ("clean-edited-reference", edited_manifest_path)],
            report_path,
        )
        if returncode != 1:
            raise RuntimeError("Astro series reference did not contain a declared edit")
        normalizer = astro_normalized_change_set(report, "clean-unedited-reference", "clean-edited-reference")
        normalizer["report"] = {"path": str(report_path), "sha256": sha256_file(report_path)}
        paths = normalizer["paths"]
        basis = "strict-normalized-content-diff"
    expected = {path for values in paths.values() for path in values}
    missing_designated = sorted(path.as_posix() for path in spec.outputs if path.as_posix() not in expected)
    if missing_designated:
        raise RuntimeError(f"{tool} reference did not change designated output: {missing_designated[0]}")
    contract = {
        "schema": "cp10-series-changed-path-contract",
        "schema_version": 1,
        "mode": spec.mode,
        "tool": tool,
        "basis": basis,
        "expected_changed_paths": paths,
        "expected_dependents": sorted(expected),
        "designated_output_markers": markers,
        "normalizer_classification": normalizer,
    }
    atomic_json(series_contract_path(args, tool), contract)
    return contract


def validate_series_contract(contract: dict[str, Any], spec: SeriesSpec, tool: str) -> None:
    expected = contract.get("expected_changed_paths", {})
    all_paths = {path for values in expected.values() for path in values} if isinstance(expected, dict) else set()
    if (
        contract.get("schema") != "cp10-series-changed-path-contract"
        or contract.get("schema_version") != 1
        or contract.get("mode") != spec.mode
        or contract.get("tool") != tool
        or set(expected) != {"added", "removed", "changed"}
        or any(path.as_posix() not in all_paths for path in spec.outputs)
        or not all(item.get("passed") for item in contract.get("designated_output_markers", []))
    ):
        raise ValueError(f"invalid {spec.mode} {tool} changed-path contract")


def verify_target(project: Path) -> dict[str, str]:
    tracked_path = project / ".nift/tracked.json"
    tracked = json.loads(tracked_path.read_text()).get("tracked", [])
    matches = [item for item in tracked if item.get("name") == NIFT_TARGET]
    if len(matches) != 1 or matches[0].get("output") != OUTPUT.as_posix():
        raise ValueError(f"Nift target is not uniquely mapped to {OUTPUT}: {NIFT_TARGET}")
    return {"name": NIFT_TARGET, "output": OUTPUT.as_posix()}


def prepare_targeted_setup(
    args: argparse.Namespace,
    initial_git: dict[str, str],
    source_state: SourceState,
) -> None:
    setup = args.evidence / "setup"
    if setup.exists():
        raise FileExistsError(f"refusing existing setup evidence: {setup}")
    references = setup / "references"
    baseline = setup / "baseline-minimal"
    references.mkdir(parents=True)
    baseline.mkdir()
    target = verify_target(args.nift_project)
    source = source_path(args, "nift")
    output_root = args.nift_project / "public"
    output_page = output_root / OUTPUT
    reference_manifest_path = expected_manifest(args, "nift")

    try:
        edit_evidence = apply_edit(source, source_state)
        clean_nift(args.nift_project)
        command, environment = clean_reference_command(args, "nift")
        untimed_command(
            "setup/references/nift-clean-edited-build",
            command,
            args.nift_project,
            environment,
            args.evidence,
        )
        edited_manifest = manifest_payload(output_root)
        atomic_json(reference_manifest_path, edited_manifest)
        designated_root = references / "nift-edited-designated-output"
        copy_file_exact(output_page, designated_root / OUTPUT)
        contract = freeze_changed_path_contract(args, "nift", designated_root)
    finally:
        restored = restore_source(source, source_state)
        if not restored["bytes_equal"] or not restored["mtime_equal"]:
            raise RuntimeError("failed to restore Nift source after targeted reference")
    if git_state(args.nift_project) != initial_git:
        raise RuntimeError("Nift Git state changed while building targeted reference")

    clean_nift(args.nift_project)
    baseline_command = [str(args.nift_bin), "build", "--all"]
    _, baseline_environment = recorded_command(args, "nift")
    untimed_command(
        "setup/baseline-minimal/nift-unedited-build",
        baseline_command,
        args.nift_project,
        baseline_environment,
        args.evidence,
    )
    baseline_manifest = manifest_payload(output_root)
    baseline_manifest_path = baseline / "nift-output-manifest.json"
    atomic_json(baseline_manifest_path, baseline_manifest)
    certified = load_manifest(args.nift_expected)
    baseline_comparison = compare_manifests(certified, baseline_manifest)
    atomic_json(baseline / "nift-certified-comparison.json", baseline_comparison)
    if not baseline_comparison["equal_content"]:
        raise RuntimeError("targeted Nift baseline differs from certified manifest")

    metadata_state = StatePath("metadata", args.nift_project / ".nift/public")
    archived_metadata = snapshot_states("nift", [metadata_state], baseline)
    baseline_page = baseline / "nift-output" / OUTPUT
    copy_file_exact(output_page, baseline_page)
    if git_state(args.nift_project) != initial_git:
        raise RuntimeError("Nift Git state changed while building targeted baseline")

    unaffected_digest = semantic_subset_digest(baseline_manifest, {OUTPUT.as_posix()})
    certified_unaffected_digest = semantic_subset_digest(certified, {OUTPUT.as_posix()})
    if unaffected_digest != certified_unaffected_digest:
        raise RuntimeError("targeted Nift unaffected output differs from certification")
    setup_payload = {
        "schema": "cp10-formal-targeted-edit-setup",
        "schema_version": 1,
        "methodology_version": 6,
        "marker": MARKER.decode(),
        "harness": {"path": str(args.harness), "sha256": sha256_file(args.harness)},
        "project": {
            "path": str(args.nift_project),
            "git": initial_git,
            "source": str(source),
            "source_sha256": sha256_bytes(source_state.data),
            "source_mtime_ns": source_state.mtime_ns,
        },
        "commands": {
            "edited_reference": command,
            "baseline": baseline_command,
            "targeted": recorded_command(args, "nift", targeted=True)[0],
        },
        "environment": relevant_environment(
            recorded_command(args, "nift", targeted=True)[1]
        ),
        "nift_target": target,
        "certified_manifest": {
            "path": str(args.nift_expected),
            "entries_sha256": certified["entries_sha256"],
        },
        "edited_reference": {
            "manifest": str(reference_manifest_path),
            "entries_sha256": edited_manifest["entries_sha256"],
            "designated_output_root": str(designated_root),
            "changed_path_contract": str(changed_path_contract_path(args, "nift")),
            "changed_path_contract_sha256": sha256_file(
                changed_path_contract_path(args, "nift")
            ),
            "expected_changed_paths": contract["expected_changed_paths"],
            "source_edit": edit_evidence,
        },
        "baseline": {
            "manifest": str(baseline_manifest_path),
            "entries_sha256": baseline_manifest["entries_sha256"],
            "metadata": archived_metadata["metadata"],
            "designated_output": file_identity(baseline_page),
        },
        "unaffected_output": {
            "verified_once": True,
            "excluded": [OUTPUT.as_posix()],
            "semantic_sha256": unaffected_digest,
            "entries": len(baseline_manifest["entries"]) - 1,
        },
        "git_after": git_state(args.nift_project),
    }
    atomic_json(setup / "targeted-setup.json", setup_payload)


def targeted_setup_ready(
    args: argparse.Namespace,
) -> tuple[dict[str, str], SourceState]:
    marker = args.evidence / "setup/targeted-setup.json"
    payload = json.loads(marker.read_text())
    if (
        payload.get("schema") != "cp10-formal-targeted-edit-setup"
        or payload.get("schema_version") != 1
        or payload.get("methodology_version") != 6
        or payload.get("marker") != MARKER.decode()
    ):
        raise ValueError(f"invalid targeted setup marker: {marker}")
    if payload["harness"] != {
        "path": str(args.harness),
        "sha256": sha256_file(args.harness),
    }:
        raise ValueError("targeted harness binding differs")
    project_binding = payload["project"]
    current_git = git_state(args.nift_project)
    source_state = capture_source(source_path(args, "nift"))
    if (
        project_binding["path"] != str(args.nift_project)
        or current_git != project_binding["git"]
        or current_git != payload["git_after"]
        or project_binding["source"] != str(source_path(args, "nift"))
        or project_binding["source_sha256"] != sha256_bytes(source_state.data)
        or project_binding["source_mtime_ns"] != source_state.mtime_ns
    ):
        raise ValueError("targeted Nift project or source binding differs")
    commands = {
        "edited_reference": clean_reference_command(args, "nift")[0],
        "baseline": [str(args.nift_bin), "build", "--all"],
        "targeted": recorded_command(args, "nift", targeted=True)[0],
    }
    if payload["commands"] != commands or payload["environment"] != relevant_environment(
        recorded_command(args, "nift", targeted=True)[1]
    ):
        raise ValueError("targeted command binding differs")
    if payload["nift_target"] != verify_target(args.nift_project):
        raise ValueError("targeted Nift route binding differs")
    certified = load_manifest(args.nift_expected)
    if payload["certified_manifest"] != {
        "path": str(args.nift_expected),
        "entries_sha256": certified["entries_sha256"],
    }:
        raise ValueError("targeted certified manifest binding differs")

    reference = payload["edited_reference"]
    reference_manifest = load_manifest(Path(reference["manifest"]))
    contract_path = changed_path_contract_path(args, "nift")
    contract = json.loads(contract_path.read_text())
    validate_changed_path_contract(contract, "nift")
    if (
        reference["entries_sha256"] != reference_manifest["entries_sha256"]
        or reference["changed_path_contract"] != str(contract_path)
        or reference["changed_path_contract_sha256"] != sha256_file(contract_path)
        or reference["expected_changed_paths"] != contract["expected_changed_paths"]
        or contract["designated_output_marker"]
        != marker_evidence(Path(reference["designated_output_root"]))
    ):
        raise ValueError("targeted edited reference binding differs")

    baseline = args.evidence / "setup/baseline-minimal"
    baseline_manifest = load_manifest(Path(payload["baseline"]["manifest"]))
    observed = manifest_payload(args.nift_project / "public")
    if (
        baseline_manifest["entries_sha256"] != payload["baseline"]["entries_sha256"]
        or not compare_manifests(certified, baseline_manifest)["equal_content"]
        or not compare_manifests(baseline_manifest, observed)["equal_content"]
        or semantic_subset_digest(observed, {OUTPUT.as_posix()})
        != payload["unaffected_output"]["semantic_sha256"]
    ):
        raise ValueError("targeted baseline or unaffected output binding differs")
    metadata_manifest = baseline / "nift-metadata-manifest.json"
    metadata_snapshot = baseline / "snapshots/nift-metadata"
    if (
        manifest_payload(metadata_snapshot)["entries_sha256"]
        != load_manifest(metadata_manifest)["entries_sha256"]
        or payload["baseline"]["metadata"]["entries_sha256"]
        != load_manifest(metadata_manifest)["entries_sha256"]
    ):
        raise ValueError("targeted Nift metadata snapshot differs")
    baseline_page = baseline / "nift-output" / OUTPUT
    if file_identity(baseline_page) != payload["baseline"]["designated_output"]:
        raise ValueError("targeted Nift output snapshot differs")
    return current_git, source_state


def verify_series_targets(project: Path, spec: SeriesSpec) -> None:
    if not spec.nift_targets:
        return
    tracked = json.loads((project / ".nift/tracked.json").read_text())["tracked"]
    mapping = {item.get("name"): item.get("output") for item in tracked}
    for target, output in zip(spec.nift_targets, spec.outputs):
        if mapping.get(target) != output.as_posix():
            raise ValueError(f"Nift target mapping differs: {target}")


def prepare_paired_series_setup(
    args: argparse.Namespace,
    spec: SeriesSpec,
    initial_git: dict[str, dict[str, str]],
    source_states: dict[str, dict[str, SourceState]],
) -> None:
    setup = args.evidence / "setup"
    references = setup / "references"
    baseline = setup / "baseline"
    if setup.exists():
        raise FileExistsError(f"refusing existing setup evidence: {setup}")
    references.mkdir(parents=True)
    baseline.mkdir()
    bindings: dict[str, Any] = {
        "schema": "cp10-formal-paired-edit-series-setup",
        "schema_version": 1,
        "methodology_version": 6,
        "mode": spec.mode,
        "harness": {"path": str(args.harness), "sha256": sha256_file(args.harness)},
        "normalizer": {"path": str(args.astro_normalizer), "sha256": sha256_file(args.astro_normalizer)},
        "projects": {},
        "references": {},
        "baselines": {},
        "commands": {tool: series_command(args, spec, tool)[0] for tool in ("nift", "astro")},
        "environments": {
            tool: relevant_environment(series_command(args, spec, tool)[1])
            for tool in ("nift", "astro")
        },
        "external_references": {
            "nift_manifest": str(args.nift_expected),
            "nift_entries_sha256": load_manifest(args.nift_expected)["entries_sha256"],
            "astro_root": str(args.astro_clean_reference),
            "astro_manifest": str(args.astro_clean_reference_manifest),
            "astro_entries_sha256": load_manifest(args.astro_clean_reference_manifest)["entries_sha256"],
        },
        "astro_remote_inputs": {
            "archive": str(args.astro_remote_input_archive),
            "archive_sha256": (
                sha256_file(args.astro_remote_input_archive)
                if args.astro_remote_input_archive.is_file()
                else None
            ),
            "archive_root": str(args.astro_remote_archive_root),
            "manifest": str(args.astro_remote_input_manifest),
            "entries_sha256": load_manifest(args.astro_remote_input_manifest)["entries_sha256"],
        },
    }
    for tool in ("nift", "astro"):
        assert_no_stale_benchmark_processes((args.nift_project, args.astro_project))
        project = project_for(args, tool)
        paths = series_source_paths(args, spec, tool)
        bindings["projects"][tool] = {
            "path": str(project),
            "git": initial_git[tool],
            "sources": {
                str(path): {
                    "sha256": sha256_bytes(source_states[tool][str(path)].data),
                    "mtime_ns": source_states[tool][str(path)].mtime_ns,
                }
                for path in paths
            },
        }
        try:
            edits = apply_series_edits(paths, source_states[tool], spec, tool)
            if tool == "nift":
                clean_nift(project)
            else:
                clean_astro(project)
                restore_astro_remote_inputs(args, args.astro_remote_archive_root)
            command, environment = clean_reference_command(args, tool)
            untimed_command(f"setup/references/{tool}-clean-edited-build", command, project, environment, args.evidence)
            output_root = states_for(tool, args.nift_project, args.astro_project)[0].live
            reference_root = references / f"{tool}-edited-output"
            copy_tree(output_root, reference_root)
            edited_manifest_path = references / f"{tool}-edited-manifest.json"
            edited_manifest = manifest_payload(reference_root)
            atomic_json(edited_manifest_path, edited_manifest)
            contract = freeze_series_contract(args, spec, tool, reference_root, edited_manifest_path)
            bindings["references"][tool] = {
                "root": str(reference_root),
                "manifest": str(edited_manifest_path),
                "entries_sha256": edited_manifest["entries_sha256"],
                "contract": str(series_contract_path(args, tool)),
                "contract_sha256": sha256_file(series_contract_path(args, tool)),
                "expected_changed_paths": contract["expected_changed_paths"],
                "edits": edits,
            }
        finally:
            if not restore_series_sources(paths, source_states[tool]):
                raise RuntimeError(f"failed to restore {tool} series sources")
        if git_state(project) != initial_git[tool]:
            raise RuntimeError(f"{tool} Git state changed during edited reference")

        if tool == "nift":
            clean_nift(project)
            baseline_command = [str(args.nift_bin), "build", "--all"]
            _, environment = series_command(args, spec, tool)
        else:
            clean_astro(project)
            restore_astro_remote_inputs(args, args.astro_remote_archive_root)
            baseline_command, environment = series_command(args, spec, tool)
        untimed_command(f"setup/baseline/{tool}-unedited-build", baseline_command, project, environment, args.evidence)
        states = states_for(tool, args.nift_project, args.astro_project)
        output_manifest = manifest_payload(states[0].live)
        archived = snapshot_states(tool, states, baseline)
        if tool == "nift":
            valid = compare_manifests(load_manifest(args.nift_expected), output_manifest)["equal_content"]
        else:
            report, code = run_normalizer(
                args.astro_normalizer,
                [("clean-reference", args.astro_clean_reference), ("incremental-baseline", states[0].live)],
                [("clean-reference", args.astro_clean_reference_manifest), ("incremental-baseline", baseline / "astro-output-manifest.json")],
                baseline / "astro-clean-normalization.json",
            )
            valid = code == 0 and normalization_passed(report)
        if not valid or git_state(project) != initial_git[tool]:
            raise RuntimeError(f"{tool} series baseline failed correctness")
        bindings["baselines"][tool] = {
            "command": baseline_command,
            "states": archived,
            "output_entries_sha256": output_manifest["entries_sha256"],
        }
    bindings["git_after"] = {tool: git_state(project_for(args, tool)) for tool in ("nift", "astro")}
    atomic_json(setup / "series-setup.json", bindings)


def paired_series_setup_ready(
    args: argparse.Namespace, spec: SeriesSpec
) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, SourceState]]]:
    marker = args.evidence / "setup/series-setup.json"
    payload = json.loads(marker.read_text())
    if (
        payload.get("schema") != "cp10-formal-paired-edit-series-setup"
        or payload.get("schema_version") != 1
        or payload.get("mode") != spec.mode
        or payload.get("methodology_version") != 6
    ):
        raise ValueError(f"invalid paired series setup: {marker}")
    if payload["harness"] != {"path": str(args.harness), "sha256": sha256_file(args.harness)}:
        raise ValueError("series harness binding differs")
    if payload["normalizer"] != {"path": str(args.astro_normalizer), "sha256": sha256_file(args.astro_normalizer)}:
        raise ValueError("series normalizer binding differs")
    if payload["commands"] != {tool: series_command(args, spec, tool)[0] for tool in ("nift", "astro")}:
        raise ValueError("series command binding differs")
    if payload["environments"] != {
        tool: relevant_environment(series_command(args, spec, tool)[1])
        for tool in ("nift", "astro")
    }:
        raise ValueError("series command environment differs")
    external = payload["external_references"]
    if (
        external["nift_manifest"] != str(args.nift_expected)
        or external["nift_entries_sha256"] != load_manifest(args.nift_expected)["entries_sha256"]
        or external["astro_root"] != str(args.astro_clean_reference)
        or external["astro_manifest"] != str(args.astro_clean_reference_manifest)
        or external["astro_entries_sha256"] != load_manifest(args.astro_clean_reference_manifest)["entries_sha256"]
        or manifest_payload(args.astro_clean_reference)["entries_sha256"] != external["astro_entries_sha256"]
    ):
        raise ValueError("series external reference binding differs")
    remote = payload["astro_remote_inputs"]
    if (
        remote["archive"] != str(args.astro_remote_input_archive)
        or remote["archive_sha256"] != (
            sha256_file(args.astro_remote_input_archive)
            if args.astro_remote_input_archive.is_file()
            else None
        )
        or remote["archive_root"] != str(args.astro_remote_archive_root)
        or remote["manifest"] != str(args.astro_remote_input_manifest)
        or remote["entries_sha256"] != load_manifest(args.astro_remote_input_manifest)["entries_sha256"]
    ):
        raise ValueError("series Astro remote-input binding differs")
    source_states: dict[str, dict[str, SourceState]] = {}
    for tool in ("nift", "astro"):
        project = project_for(args, tool)
        if (
            payload["projects"][tool]["path"] != str(project)
            or git_state(project) != payload["projects"][tool]["git"]
            or git_state(project) != payload["git_after"][tool]
        ):
            raise ValueError(f"{tool} series Git binding differs")
        source_states[tool] = {}
        for path in series_source_paths(args, spec, tool):
            state = capture_source(path)
            source_states[tool][str(path)] = state
            if payload["projects"][tool]["sources"][str(path)] != {
                "sha256": sha256_bytes(state.data), "mtime_ns": state.mtime_ns
            }:
                raise ValueError(f"{tool} series source binding differs")
        reference = payload["references"][tool]
        if manifest_payload(Path(reference["root"]))["entries_sha256"] != load_manifest(Path(reference["manifest"]))["entries_sha256"]:
            raise ValueError(f"{tool} series reference differs")
        contract = json.loads(Path(reference["contract"]).read_text())
        validate_series_contract(contract, spec, tool)
        if reference["contract_sha256"] != sha256_file(Path(reference["contract"])):
            raise ValueError(f"{tool} series contract differs")
    restore_astro_remote_inputs(args, args.astro_remote_archive_root)
    return {tool: payload["projects"][tool]["git"] for tool in ("nift", "astro")}, source_states


def prepare_batch_targeted_setup(
    args: argparse.Namespace,
    spec: SeriesSpec,
    initial_git: dict[str, str],
    source_states: dict[str, SourceState],
) -> None:
    setup = args.evidence / "setup"
    references = setup / "references"
    baseline = setup / "baseline-minimal"
    if setup.exists():
        raise FileExistsError(f"refusing existing setup evidence: {setup}")
    references.mkdir(parents=True)
    baseline.mkdir()
    verify_series_targets(args.nift_project, spec)
    paths = series_source_paths(args, spec, "nift")
    output_root = args.nift_project / "public"
    try:
        edits = apply_series_edits(paths, source_states, spec, "nift")
        clean_nift(args.nift_project)
        command, environment = clean_reference_command(args, "nift")
        untimed_command("setup/references/nift-clean-edited-build", command, args.nift_project, environment, args.evidence)
        edited_manifest = manifest_payload(output_root)
        edited_manifest_path = references / "nift-edited-manifest.json"
        atomic_json(edited_manifest_path, edited_manifest)
        designated_root = references / "nift-edited-designated-outputs"
        for output in spec.outputs:
            copy_file_exact(output_root / output, designated_root / output)
        contract = freeze_series_contract(args, spec, "nift", designated_root, edited_manifest_path)
    finally:
        if not restore_series_sources(paths, source_states):
            raise RuntimeError("failed to restore batch-targeted sources")
    if git_state(args.nift_project) != initial_git:
        raise RuntimeError("Nift Git state changed during batch-targeted reference")
    clean_nift(args.nift_project)
    baseline_command = [str(args.nift_bin), "build", "--all"]
    _, environment = series_command(args, spec, "nift")
    untimed_command("setup/baseline-minimal/nift-unedited-build", baseline_command, args.nift_project, environment, args.evidence)
    baseline_manifest = manifest_payload(output_root)
    baseline_manifest_path = baseline / "nift-output-manifest.json"
    atomic_json(baseline_manifest_path, baseline_manifest)
    certified = load_manifest(args.nift_expected)
    if not compare_manifests(certified, baseline_manifest)["equal_content"]:
        raise RuntimeError("batch-targeted baseline differs from certification")
    metadata = snapshot_states("nift", [StatePath("metadata", args.nift_project / ".nift/public")], baseline)["metadata"]
    output_snapshots = {}
    for output in spec.outputs:
        snapshot = baseline / "nift-output" / output
        copy_file_exact(output_root / output, snapshot)
        output_snapshots[output.as_posix()] = file_identity(snapshot)
    excluded = {path.as_posix() for path in spec.outputs}
    unaffected = semantic_subset_digest(baseline_manifest, excluded)
    if unaffected != semantic_subset_digest(certified, excluded):
        raise RuntimeError("batch-targeted unaffected output differs from certification")
    atomic_json(
        setup / "series-setup.json",
        {
            "schema": "cp10-formal-lean-targeted-series-setup", "schema_version": 1,
            "methodology_version": 6, "mode": spec.mode,
            "harness": {"path": str(args.harness), "sha256": sha256_file(args.harness)},
            "project": {"path": str(args.nift_project), "git": initial_git, "sources": {
                str(path): {"sha256": sha256_bytes(source_states[str(path)].data), "mtime_ns": source_states[str(path)].mtime_ns}
                for path in paths
            }},
            "commands": {"reference": command, "baseline": baseline_command, "targeted": series_command(args, spec, "nift")[0]},
            "environment": relevant_environment(series_command(args, spec, "nift")[1]),
            "targets": list(spec.nift_targets),
            "reference": {"manifest": str(edited_manifest_path), "entries_sha256": edited_manifest["entries_sha256"],
                          "designated_root": str(designated_root), "contract": str(series_contract_path(args, "nift")),
                          "contract_sha256": sha256_file(series_contract_path(args, "nift")), "edits": edits},
            "baseline": {"manifest": str(baseline_manifest_path), "entries_sha256": baseline_manifest["entries_sha256"],
                         "metadata": metadata, "outputs": output_snapshots},
            "certified": {"path": str(args.nift_expected), "entries_sha256": certified["entries_sha256"]},
            "unaffected_output": {"verified_once": True, "semantic_sha256": unaffected, "excluded": sorted(excluded)},
            "git_after": git_state(args.nift_project),
        },
    )


def batch_targeted_setup_ready(
    args: argparse.Namespace, spec: SeriesSpec
) -> tuple[dict[str, str], dict[str, SourceState]]:
    payload = json.loads((args.evidence / "setup/series-setup.json").read_text())
    if payload.get("schema") != "cp10-formal-lean-targeted-series-setup" or payload.get("mode") != spec.mode:
        raise ValueError("invalid batch-targeted setup")
    if payload["harness"] != {"path": str(args.harness), "sha256": sha256_file(args.harness)}:
        raise ValueError("batch-targeted harness differs")
    verify_series_targets(args.nift_project, spec)
    current_git = git_state(args.nift_project)
    if (
        payload["project"]["path"] != str(args.nift_project)
        or current_git != payload["project"]["git"]
        or current_git != payload["git_after"]
        or payload["targets"] != list(spec.nift_targets)
    ):
        raise ValueError("batch-targeted Git binding differs")
    states = {}
    for path in series_source_paths(args, spec, "nift"):
        state = capture_source(path)
        states[str(path)] = state
        if payload["project"]["sources"][str(path)] != {"sha256": sha256_bytes(state.data), "mtime_ns": state.mtime_ns}:
            raise ValueError("batch-targeted source binding differs")
    if payload["commands"] != {
        "reference": clean_reference_command(args, "nift")[0],
        "baseline": [str(args.nift_bin), "build", "--all"],
        "targeted": series_command(args, spec, "nift")[0],
    } or payload["environment"] != relevant_environment(
        series_command(args, spec, "nift")[1]
    ):
        raise ValueError("batch-targeted command binding differs")
    certified = load_manifest(args.nift_expected)
    if payload["certified"] != {
        "path": str(args.nift_expected), "entries_sha256": certified["entries_sha256"]
    }:
        raise ValueError("batch-targeted certified manifest differs")
    contract = json.loads(Path(payload["reference"]["contract"]).read_text())
    validate_series_contract(contract, spec, "nift")
    if payload["reference"]["contract_sha256"] != sha256_file(Path(payload["reference"]["contract"])):
        raise ValueError("batch-targeted contract differs")
    reference_manifest = load_manifest(Path(payload["reference"]["manifest"]))
    if (
        reference_manifest["entries_sha256"] != payload["reference"]["entries_sha256"]
        or series_marker_evidence(Path(payload["reference"]["designated_root"]), spec)
        != contract["designated_output_markers"]
    ):
        raise ValueError("batch-targeted edited reference differs")
    baseline_manifest = load_manifest(Path(payload["baseline"]["manifest"]))
    observed = manifest_payload(args.nift_project / "public")
    if (
        baseline_manifest["entries_sha256"] != payload["baseline"]["entries_sha256"]
        or not compare_manifests(certified, baseline_manifest)["equal_content"]
        or not compare_manifests(baseline_manifest, observed)["equal_content"]
        or semantic_subset_digest(observed, set(payload["unaffected_output"]["excluded"])) != payload["unaffected_output"]["semantic_sha256"]
    ):
        raise ValueError("batch-targeted baseline differs")
    metadata_manifest = args.evidence / "setup/baseline-minimal/nift-metadata-manifest.json"
    metadata_snapshot = args.evidence / "setup/baseline-minimal/snapshots/nift-metadata"
    if (
        manifest_payload(metadata_snapshot)["entries_sha256"]
        != load_manifest(metadata_manifest)["entries_sha256"]
        or payload["baseline"]["metadata"]["entries_sha256"]
        != load_manifest(metadata_manifest)["entries_sha256"]
    ):
        raise ValueError("batch-targeted metadata snapshot differs")
    for output in spec.outputs:
        if file_identity(args.evidence / "setup/baseline-minimal/nift-output" / output) != payload["baseline"]["outputs"][output.as_posix()]:
            raise ValueError("batch-targeted output snapshot differs")
    return current_git, states


def restore_batch_targeted_state(project: Path, baseline: Path, spec: SeriesSpec) -> None:
    restore_states("nift", [StatePath("metadata", project / ".nift/public")], baseline)
    for output in spec.outputs:
        restore_file_exact(baseline / "nift-output" / output, project / "public" / output)


def prepare_setup(
    args: argparse.Namespace,
    initial_git: dict[str, dict[str, str]],
    sources: dict[str, SourceState],
) -> None:
    setup = args.evidence / "setup"
    if setup.exists():
        raise FileExistsError(f"refusing existing setup evidence: {setup}")
    (setup / "references").mkdir(parents=True)
    baseline = setup / "baseline"
    baseline.mkdir()
    target = verify_target(args.nift_project)

    bindings: dict[str, Any] = {
        "schema": "cp10-formal-edit-setup",
        "schema_version": SCHEMA_VERSION,
        "methodology_version": 6,
        "marker": MARKER.decode(),
        "harness": {
            "path": str(args.harness),
            "sha256": sha256_file(args.harness),
        },
        "projects": {
            tool: {
                "path": str(project_for(args, tool)),
                "git": initial_git[tool],
                "source": str(source_path(args, tool)),
                "source_sha256": sha256_bytes(sources[tool].data),
                "source_mtime_ns": sources[tool].mtime_ns,
            }
            for tool in ("nift", "astro")
        },
        "commands": {
            "normal": {
                tool: recorded_command(args, tool)[0] for tool in ("nift", "astro")
            },
            "targeted": {"nift": recorded_command(args, "nift", targeted=True)[0]},
            "edited_reference": {
                tool: clean_reference_command(args, tool)[0]
                for tool in ("nift", "astro")
            },
        },
        "environments": {
            "normal": {
                tool: relevant_environment(recorded_command(args, tool)[1])
                for tool in ("nift", "astro")
            },
            "targeted": relevant_environment(
                recorded_command(args, "nift", targeted=True)[1]
            ),
            "edited_reference": {
                tool: relevant_environment(clean_reference_command(args, tool)[1])
                for tool in ("nift", "astro")
            },
        },
        "nift_target": target,
        "normalizer": {
            "path": str(args.astro_normalizer),
            "sha256": sha256_file(args.astro_normalizer),
        },
        "external_references": {
            "nift_expected_manifest": str(args.nift_expected),
            "nift_expected_entries_sha256": load_manifest(args.nift_expected)[
                "entries_sha256"
            ],
            "astro_clean_root": str(args.astro_clean_reference),
            "astro_clean_manifest": str(args.astro_clean_reference_manifest),
            "astro_clean_entries_sha256": load_manifest(
                args.astro_clean_reference_manifest
            )["entries_sha256"],
            "astro_remote_input_archive": str(args.astro_remote_input_archive),
            "astro_remote_input_archive_sha256": (
                sha256_file(args.astro_remote_input_archive)
                if args.astro_remote_input_archive.is_file()
                else None
            ),
            "astro_remote_input_archive_root": str(args.astro_remote_archive_root),
            "astro_remote_input_manifest": str(args.astro_remote_input_manifest),
            "astro_remote_input_entries_sha256": load_manifest(
                args.astro_remote_input_manifest
            )["entries_sha256"],
        },
        "baselines": {},
        "edited_references": {},
    }

    observed_clean_astro = manifest_payload(args.astro_clean_reference)
    if (
        observed_clean_astro["entries_sha256"]
        != bindings["external_references"]["astro_clean_entries_sha256"]
    ):
        raise RuntimeError("retained Astro clean reference differs from its manifest")

    for tool in ("nift", "astro"):
        assert_no_stale_benchmark_processes(
            (args.nift_project, args.astro_project)
        )
        project = project_for(args, tool)
        source = source_path(args, tool)
        states = states_for(tool, args.nift_project, args.astro_project)
        edit_evidence: dict[str, Any] | None = None
        try:
            edit_evidence = apply_edit(source, sources[tool])
            if tool == "nift":
                clean_nift(project)
            else:
                clean_astro(project)
                restore_astro_remote_inputs(args, args.astro_remote_archive_root)
            command, environment = clean_reference_command(args, tool)
            untimed_command(
                f"setup/references/{tool}-clean-edited-build",
                command,
                project,
                environment,
                args.evidence,
            )
            reference_root = setup / f"references/{tool}-edited-output"
            copy_tree(states[0].live, reference_root)
            reference_manifest = manifest_payload(reference_root)
            atomic_json(expected_manifest(args, tool), reference_manifest)
            changed_path_contract = freeze_changed_path_contract(
                args, tool, reference_root
            )
            bindings["edited_references"][tool] = {
                "root": str(reference_root),
                "manifest": str(expected_manifest(args, tool)),
                "entries_sha256": reference_manifest["entries_sha256"],
                "changed_path_contract": str(
                    changed_path_contract_path(args, tool)
                ),
                "changed_path_contract_sha256": sha256_file(
                    changed_path_contract_path(args, tool)
                ),
                "expected_changed_paths": changed_path_contract[
                    "expected_changed_paths"
                ],
                "source_edit": edit_evidence,
            }
        finally:
            restored = restore_source(source, sources[tool])
            if not restored["bytes_equal"] or not restored["mtime_equal"]:
                raise RuntimeError(f"failed to restore source after {tool} reference")
        if git_state(project) != initial_git[tool]:
            raise RuntimeError(f"{tool} Git state changed while building reference")

        if tool == "nift":
            clean_nift(project)
            baseline_command = [str(args.nift_bin), "build", "--all"]
            _, baseline_environment = recorded_command(args, tool)
        else:
            clean_astro(project)
            restore_astro_remote_inputs(args, args.astro_remote_archive_root)
            baseline_command, baseline_environment = recorded_command(args, tool)
        untimed_command(
            f"setup/baseline/{tool}-unedited-incremental-build",
            baseline_command,
            project,
            baseline_environment,
            args.evidence,
        )
        baseline_manifest = manifest_payload(states[0].live)
        archived = snapshot_states(tool, states, baseline)
        if tool == "nift":
            comparison = compare_manifests(
                load_manifest(args.nift_expected), baseline_manifest
            )
            atomic_json(baseline / "nift-expected-comparison.json", comparison)
            baseline_valid = comparison["equal_content"]
        else:
            report, returncode = run_normalizer(
                args.astro_normalizer,
                [
                    ("clean-reference", args.astro_clean_reference),
                    ("incremental-baseline", states[0].live),
                ],
                [
                    ("clean-reference", args.astro_clean_reference_manifest),
                    ("incremental-baseline", baseline / "astro-output-manifest.json"),
                ],
                baseline / "astro-clean-normalization.json",
            )
            baseline_valid = returncode == 0 and normalization_passed(report)
        if not baseline_valid:
            raise RuntimeError(f"{tool} unedited baseline failed correctness")
        if git_state(project) != initial_git[tool]:
            raise RuntimeError(f"{tool} Git state changed while building baseline")
        bindings["baselines"][tool] = {
            "command": baseline_command,
            "states": archived,
            "output_entries_sha256": baseline_manifest["entries_sha256"],
        }

    bindings["git_after"] = {
        tool: git_state(project_for(args, tool)) for tool in ("nift", "astro")
    }
    if bindings["git_after"] != initial_git:
        raise RuntimeError("setup changed tracked Git state")
    atomic_json(setup / "setup.json", bindings)


def setup_ready(args: argparse.Namespace) -> tuple[dict[str, dict[str, str]], dict[str, SourceState]]:
    marker = args.evidence / "setup/setup.json"
    payload = json.loads(marker.read_text())
    if payload.get("schema") != "cp10-formal-edit-setup" or payload.get(
        "schema_version"
    ) != SCHEMA_VERSION:
        raise ValueError(f"invalid setup marker: {marker}")
    if payload.get("methodology_version") != 6 or payload.get("marker") != MARKER.decode():
        raise ValueError("setup methodology or edit marker differs")
    if payload["harness"] != {
        "path": str(args.harness),
        "sha256": sha256_file(args.harness),
    }:
        raise ValueError("harness binding differs")
    if payload["normalizer"] != {
        "path": str(args.astro_normalizer),
        "sha256": sha256_file(args.astro_normalizer),
    }:
        raise ValueError("Astro normalizer binding differs")
    expected_commands = {
        "normal": {tool: recorded_command(args, tool)[0] for tool in ("nift", "astro")},
        "targeted": {"nift": recorded_command(args, "nift", targeted=True)[0]},
        "edited_reference": {
            tool: clean_reference_command(args, tool)[0] for tool in ("nift", "astro")
        },
    }
    if payload["commands"] != expected_commands:
        raise ValueError("command binding differs")
    expected_environments = {
        "normal": {
            tool: relevant_environment(recorded_command(args, tool)[1])
            for tool in ("nift", "astro")
        },
        "targeted": relevant_environment(
            recorded_command(args, "nift", targeted=True)[1]
        ),
        "edited_reference": {
            tool: relevant_environment(clean_reference_command(args, tool)[1])
            for tool in ("nift", "astro")
        },
    }
    if payload.get("environments") != expected_environments:
        raise ValueError("command environment binding differs")
    if payload["nift_target"] != verify_target(args.nift_project):
        raise ValueError("Nift target binding differs")

    current_sources = {tool: capture_source(source_path(args, tool)) for tool in ("nift", "astro")}
    for tool in ("nift", "astro"):
        project_binding = payload["projects"][tool]
        if project_binding["path"] != str(project_for(args, tool)):
            raise ValueError(f"{tool} project binding differs")
        if git_state(project_for(args, tool)) != project_binding["git"]:
            raise ValueError(f"{tool} HEAD, tree, or worktree state differs")
        if project_binding["source"] != str(source_path(args, tool)) or project_binding[
            "source_sha256"
        ] != sha256_bytes(current_sources[tool].data):
            raise ValueError(f"{tool} source binding differs")
        if project_binding["source_mtime_ns"] != current_sources[tool].mtime_ns:
            raise ValueError(f"{tool} source mtime binding differs")
        reference = payload["edited_references"][tool]
        if (
            reference["root"]
            != str(args.evidence / f"setup/references/{tool}-edited-output")
            or reference["manifest"] != str(expected_manifest(args, tool))
        ):
            raise ValueError(f"{tool} edited reference root binding differs")
        contract_path = changed_path_contract_path(args, tool)
        contract = json.loads(contract_path.read_text())
        validate_changed_path_contract(contract, tool)
        if contract["designated_output_marker"] != marker_evidence(
            Path(reference["root"])
        ):
            raise ValueError(f"{tool} designated output marker binding differs")
        normalizer_report = contract.get("normalizer_report")
        if normalizer_report and (
            normalizer_report.get("path")
            != str(args.evidence / "setup/references/astro-clean-to-edited-normalization.json")
            or normalizer_report.get("sha256")
            != sha256_file(Path(normalizer_report["path"]))
            or normalizer_report.get("returncode") != 1
        ):
            raise ValueError("Astro clean-to-edited classification evidence differs")
        if (
            reference.get("changed_path_contract") != str(contract_path)
            or reference.get("changed_path_contract_sha256")
            != sha256_file(contract_path)
            or reference.get("expected_changed_paths")
            != contract["expected_changed_paths"]
        ):
            raise ValueError(f"{tool} changed-path contract binding differs")
        observed = manifest_payload(Path(reference["root"]))
        archived = load_manifest(Path(reference["manifest"]))
        if observed["entries_sha256"] != archived["entries_sha256"] or archived[
            "entries_sha256"
        ] != reference["entries_sha256"]:
            raise ValueError(f"{tool} edited reference digest differs")
        for state in states_for(tool, args.nift_project, args.astro_project):
            snapshot = args.evidence / f"setup/baseline/snapshots/{tool}-{state.name}"
            manifest = args.evidence / f"setup/baseline/{tool}-{state.name}-manifest.json"
            archived_state = payload["baselines"][tool]["states"][state.name]
            if archived_state.get("present") is not True:
                if state.required:
                    raise ValueError(f"required {tool} baseline state is absent")
                continue
            if not snapshot.is_dir() or not manifest.is_file():
                raise ValueError(f"{tool} baseline state archive is incomplete")
            if archived_state["snapshot"] != str(snapshot) or archived_state[
                "manifest"
            ] != str(manifest):
                raise ValueError(f"{tool} baseline state path binding differs")
            snapshot_digest = manifest_payload(snapshot)["entries_sha256"]
            manifest_digest = load_manifest(manifest)["entries_sha256"]
            if snapshot_digest != manifest_digest or manifest_digest != archived_state[
                "entries_sha256"
            ]:
                raise ValueError(f"{tool} baseline state digest differs")
        if (
            payload["baselines"][tool]["output_entries_sha256"]
            != payload["baselines"][tool]["states"]["output"]["entries_sha256"]
        ):
            raise ValueError(f"{tool} baseline output binding differs")
        expected_baseline_command = (
            [str(args.nift_bin), "build", "--all"]
            if tool == "nift"
            else recorded_command(args, tool)[0]
        )
        if payload["baselines"][tool]["command"] != expected_baseline_command:
            raise ValueError(f"{tool} baseline command binding differs")

    external = payload["external_references"]
    if (
        external["nift_expected_manifest"] != str(args.nift_expected)
        or external["nift_expected_entries_sha256"]
        != load_manifest(args.nift_expected)["entries_sha256"]
        or external["astro_clean_root"] != str(args.astro_clean_reference)
        or external["astro_clean_manifest"] != str(args.astro_clean_reference_manifest)
        or external["astro_clean_entries_sha256"]
        != load_manifest(args.astro_clean_reference_manifest)["entries_sha256"]
        or manifest_payload(args.astro_clean_reference)["entries_sha256"]
        != external["astro_clean_entries_sha256"]
        or external["astro_remote_input_archive"]
        != str(args.astro_remote_input_archive)
        or external["astro_remote_input_archive_sha256"]
        != (
            sha256_file(args.astro_remote_input_archive)
            if args.astro_remote_input_archive.is_file()
            else None
        )
        or external["astro_remote_input_archive_root"]
        != str(args.astro_remote_archive_root)
        or external["astro_remote_input_manifest"]
        != str(args.astro_remote_input_manifest)
        or external["astro_remote_input_entries_sha256"]
        != load_manifest(args.astro_remote_input_manifest)["entries_sha256"]
    ):
        raise ValueError("external correctness reference binding differs")
    restore_astro_remote_inputs(args, args.astro_remote_archive_root)
    return {tool: payload["projects"][tool]["git"] for tool in ("nift", "astro")}, current_sources


def changed_files(diff: dict[str, Any], manifest: dict[str, Any]) -> dict[str, list[str]]:
    files = {entry["path"] for entry in manifest["entries"] if entry["type"] == "file"}
    content = sorted(
        path for path in diff["added"] + diff["changed"] if path in files
    )
    touched = sorted(set(content) | (set(diff["mtime_only"]) & files))
    return {"content_changed": content, "touched": touched}


def refuse_attempt_collision(directory: Path, label: str) -> None:
    collision = next(directory.glob(f"{label}*"), None)
    if collision:
        raise FileExistsError(f"refusing to overwrite evidence: {collision}")


def baseline_states_equal(tool: str, states: list[Any], baseline: Path) -> bool:
    for state in states:
        manifest = baseline / f"{tool}-{state.name}-manifest.json"
        if manifest.exists():
            if not state.live.is_dir() or manifest_payload(state.live)[
                "entries_sha256"
            ] != load_manifest(manifest)["entries_sha256"]:
                return False
        elif state.live.exists() or state.required:
            return False
    return True


def restore_targeted_nift_state(project: Path, baseline: Path) -> None:
    restore_states(
        "nift", [StatePath("metadata", project / ".nift/public")], baseline
    )
    restore_file_exact(
        baseline / "nift-output" / OUTPUT,
        project / "public" / OUTPUT,
    )


def run_attempt(
    args: argparse.Namespace,
    *,
    tool: str,
    label: str,
    round_number: int,
    git_before: dict[str, str],
    original: SourceState,
    targeted: bool,
    measured: bool,
) -> bool:
    directory = args.evidence / ("targeted" if targeted else "normal")
    stem = directory / label
    refuse_attempt_collision(directory, label)
    project = project_for(args, tool)
    source = source_path(args, tool)
    states = states_for(tool, args.nift_project, args.astro_project)
    baseline = args.evidence / "setup/baseline"
    errors: list[str] = []
    record: dict[str, Any] | None = None
    pre_output: dict[str, Any] | None = None
    post_output: dict[str, Any] | None = None
    output_diff: dict[str, Any] | None = None
    expected_comparison: dict[str, Any] | None = None
    normalization_report: dict[str, Any] | None = None
    normalization_returncode: int | None = None
    change_normalization_report: dict[str, Any] | None = None
    change_normalization_returncode: int | None = None
    path_classification: dict[str, Any] | None = None
    marker_check: dict[str, Any] | None = None
    source_edit: dict[str, Any] | None = None
    source_restoration: dict[str, Any] | None = None
    metadata_diffs: dict[str, str] = {}
    baseline_restored = False
    source_marker = False
    output_marker = False
    command, environment = recorded_command(args, tool, targeted=targeted)

    try:
        assert_no_stale_benchmark_processes(
            (args.nift_project, args.astro_project)
        )
        restore_states(tool, states, baseline)
        if git_state(project) != git_before:
            raise RuntimeError(f"{tool} Git state differs before {label}")
        pre_output = manifest_payload(states[0].live)
        atomic_json(Path(f"{stem}-pre-output-manifest.json"), pre_output)
        contract_path = changed_path_contract_path(args, tool)
        contract = json.loads(contract_path.read_text())
        validate_changed_path_contract(contract, tool)
        metadata_before: dict[str, dict[str, Any]] = {}
        for state in states[1:]:
            if state.live.is_dir():
                metadata_before[state.name] = manifest_payload(state.live)
                atomic_json(
                    Path(f"{stem}-pre-{state.name}-manifest.json"),
                    metadata_before[state.name],
                )
        source_edit = apply_edit(source, original)
        if tool == "astro":
            restore_astro_remote_inputs(args, args.astro_remote_archive_root)
        source_marker = source.read_bytes().count(MARKER) == 1
        if measured:
            identifier = f"formal-{'targeted' if targeted else 'normal-edit'}-{tool}-{label}"
            harness_command = [
                sys.executable,
                str(args.harness),
                "run",
                "--id",
                identifier,
                "--series",
                "formal-targeted-edit" if targeted else "formal-normal-edit-paired",
                "--scenario",
                "one-page-explicit-target" if targeted else "one-page-normal-incremental",
                "--tool",
                tool,
                "--round",
                str(round_number),
                "--warmth",
                "warm",
                "--output",
                str(stem.with_suffix(".json")),
                "--cwd",
                str(project),
                "--",
                *command,
            ]
            completed = run(harness_command, env=environment, check=False)
            record_path = stem.with_suffix(".json")
            record = json.loads(record_path.read_text()) if record_path.exists() else None
            if completed.returncode != 0:
                errors.append(f"harness exit code {completed.returncode}")
        else:
            try:
                untimed_command(label, command, project, environment, directory)
            except Exception as error:
                errors.append(f"command failed: {error}")

        source_marker = source.read_bytes().count(MARKER) == 1
        if states[0].live.is_dir():
            post_output = manifest_payload(states[0].live)
            atomic_json(Path(f"{stem}-post-output-manifest.json"), post_output)
            output_diff = compare_manifests(pre_output, post_output)
            atomic_json(Path(f"{stem}-output-diff.json"), output_diff)
            marker_check = marker_evidence(states[0].live)
            output_marker = marker_check["passed"]
            if tool == "nift":
                expected_comparison = compare_manifests(
                    load_manifest(expected_manifest(args, tool)), post_output
                )
                atomic_json(
                    Path(f"{stem}-expected-comparison.json"), expected_comparison
                )
                observed_changes = diff_path_sets(output_diff)
            else:
                normalization_report, normalization_returncode = run_normalizer(
                    args.astro_normalizer,
                    [
                        (
                            "clean-edited-reference",
                            args.evidence / "setup/references/astro-edited-output",
                        ),
                        ("recorded-edited-output", states[0].live),
                    ],
                    [
                        ("clean-edited-reference", expected_manifest(args, tool)),
                        (
                            "recorded-edited-output",
                            Path(f"{stem}-post-output-manifest.json"),
                        ),
                    ],
                    Path(f"{stem}-astro-normalization.json"),
                )
                change_normalization_report, change_normalization_returncode = (
                    run_normalizer(
                        args.astro_normalizer,
                        [
                            (
                                "reconstructed-unedited-baseline",
                                baseline / "snapshots/astro-output",
                            ),
                            ("recorded-edited-output", states[0].live),
                        ],
                        [
                            (
                                "reconstructed-unedited-baseline",
                                baseline / "astro-output-manifest.json",
                            ),
                            (
                                "recorded-edited-output",
                                Path(f"{stem}-post-output-manifest.json"),
                            ),
                        ],
                        Path(f"{stem}-astro-change-normalization.json"),
                    )
                )
                if change_normalization_returncode != 1:
                    raise RuntimeError(
                        "Astro baseline-to-edited output did not contain exactly the declared edit"
                    )
                observed_changes = astro_normalized_change_set(
                    change_normalization_report,
                    "reconstructed-unedited-baseline",
                    "recorded-edited-output",
                )["paths"]
            classification = changed_path_classification(
                contract["expected_changed_paths"], observed_changes
            )
            path_classification = {
                "schema": "cp10-edit-run-changed-path-classification",
                "schema_version": 1,
                "tool": tool,
                "contract": str(contract_path),
                "contract_sha256": sha256_file(contract_path),
                "basis": contract["basis"],
                **classification,
                "expected_dependents": contract["expected_dependents"],
                "classified_expected_edit_paths": sorted(
                    {path for values in observed_changes.values() for path in values}
                    - {
                        path
                        for values in classification["unexpected_unclassified"].values()
                        for path in values
                    }
                ),
                "normalizer_classification": (
                    astro_normalized_change_set(
                        change_normalization_report,
                        "reconstructed-unedited-baseline",
                        "recorded-edited-output",
                    )
                    if tool == "astro"
                    else None
                ),
                "designated_output_marker": marker_check,
            }
            atomic_json(
                Path(f"{stem}-changed-path-classification.json"),
                path_classification,
            )
        for state in states[1:]:
            before = metadata_before.get(state.name)
            after = manifest_payload(state.live) if state.live.is_dir() else None
            if after:
                atomic_json(Path(f"{stem}-post-{state.name}-manifest.json"), after)
            if before and after:
                difference = compare_manifests(before, after)
                difference_path = Path(f"{stem}-{state.name}-diff.json")
                atomic_json(difference_path, difference)
                metadata_diffs[state.name] = difference_path.name
    except Exception as error:
        errors.append(f"attempt processing failed: {error}")
    finally:
        try:
            source_restoration = restore_source(source, original)
        except Exception as error:
            errors.append(f"source restoration failed: {error}")
        try:
            assert_no_stale_benchmark_processes(
                (args.nift_project, args.astro_project)
            )
            restore_states(tool, states, baseline)
            if tool == "astro":
                restore_astro_remote_inputs(args, args.astro_remote_archive_root)
            baseline_restored = baseline_states_equal(tool, states, baseline)
        except Exception as error:
            errors.append(f"baseline restoration failed: {error}")

    infrastructure_valid = bool(
        not measured
        or (
            record
            and record.get("validity", {}).get("infrastructure_valid") is True
        )
    )
    if tool == "nift":
        output_correct = bool(expected_comparison and expected_comparison["equal_content"])
    else:
        output_correct = bool(
            normalization_returncode == 0 and normalization_passed(normalization_report)
        )
    changed_paths_valid = bool(
        path_classification
        and path_classification["matches"]
        and path_classification["all_expected_dependents_changed"]
        and path_classification["no_unclassified_output_changed"]
        and not (
            path_classification.get("normalizer_classification") or {}
        ).get("normalizer_rejected")
    )
    source_restored = bool(
        source_restoration
        and source_restoration["bytes_equal"]
        and source_restoration["mtime_equal"]
        and git_state(project) == git_before
    )
    formal_valid = bool(
        not errors
        and infrastructure_valid
        and source_marker
        and output_marker
        and output_correct
        and changed_paths_valid
        and source_restored
        and baseline_restored
    )
    file_changes = changed_files(output_diff, post_output) if output_diff and post_output else {
        "content_changed": [],
        "touched": [],
    }
    validation = {
        "schema": "cp10-formal-edit-run-validation",
        "schema_version": SCHEMA_VERSION,
        "label": label,
        "tool": tool,
        "targeted": targeted,
        "measured": measured,
        "round": round_number,
        "command": command,
        "infrastructure_valid": infrastructure_valid,
        "formal_valid": formal_valid,
        "errors": errors,
        "source_edit": source_edit,
        "source_marker_present": source_marker,
        "designated_output_marker": marker_check,
        "output_marker_present": output_marker,
        "source_restoration": source_restoration,
        "source_and_git_restored": source_restored,
        "baseline_output_and_metadata_restored": baseline_restored,
        "output_correct": output_correct,
        "changed_paths_valid": changed_paths_valid,
        "changed_path_classification": (
            Path(f"{stem}-changed-path-classification.json").name
            if path_classification
            else None
        ),
        "normalization_returncode": normalization_returncode,
        "normalization_rejected": (
            normalization_report.get("rejected") if normalization_report else None
        ),
        "normalization_unclassified": (
            normalization_report.get("unclassified") if normalization_report else None
        ),
        "change_normalization_returncode": change_normalization_returncode,
        "change_normalization_rejected": (
            change_normalization_report.get("rejected")
            if change_normalization_report
            else None
        ),
        "change_normalization_residual_paths": (
            change_normalization_report.get("unclassified")
            if change_normalization_report
            else None
        ),
        "output_diff": Path(f"{stem}-output-diff.json").name if output_diff else None,
        "content_changed_paths": (
            {key: output_diff[key] for key in ("added", "removed", "changed")}
            if output_diff
            else None
        ),
        "mtime_only_paths": output_diff["mtime_only"] if output_diff else [],
        "regenerated_files": file_changes["content_changed"],
        "touched_files": file_changes["touched"],
        "metadata_diffs": metadata_diffs,
        "aggregate_peak_memory_bytes": (
            record.get("cgroup", {}).get("memory_peak_bytes") if record else None
        ),
    }
    atomic_json(Path(f"{stem}-validation.json"), validation)
    return formal_valid


def run_targeted_attempt(
    args: argparse.Namespace,
    *,
    label: str,
    run_number: int,
    git_before: dict[str, str],
    original: SourceState,
    measured: bool,
) -> bool:
    directory = args.evidence / "targeted"
    stem = directory / label
    refuse_attempt_collision(directory, label)
    project = args.nift_project
    source = source_path(args, "nift")
    output_root = project / "public"
    output_page = output_root / OUTPUT
    baseline = args.evidence / "setup/baseline-minimal"
    metadata_state = StatePath("metadata", project / ".nift/public")
    setup = json.loads((args.evidence / "setup/targeted-setup.json").read_text())
    contract_path = changed_path_contract_path(args, "nift")
    contract = json.loads(contract_path.read_text())
    command, environment = recorded_command(args, "nift", targeted=True)
    errors: list[str] = []
    record: dict[str, Any] | None = None
    pre_output: dict[str, Any] | None = None
    post_output: dict[str, Any] | None = None
    output_diff: dict[str, Any] | None = None
    expected_comparison: dict[str, Any] | None = None
    path_classification: dict[str, Any] | None = None
    marker_check: dict[str, Any] | None = None
    source_edit: dict[str, Any] | None = None
    source_restoration: dict[str, Any] | None = None
    metadata_diff: dict[str, Any] | None = None
    minimal_state_restored = False
    source_marker = False

    try:
        assert_no_stale_benchmark_processes((project,))
        restore_targeted_nift_state(project, baseline)
        if git_state(project) != git_before:
            raise RuntimeError(f"Nift Git state differs before {label}")
        validate_changed_path_contract(contract, "nift")
        baseline_manifest = load_manifest(Path(setup["baseline"]["manifest"]))
        expected_paths = {
            path
            for values in contract["expected_changed_paths"].values()
            for path in values
        }
        pre_output = manifest_payload_reusing(
            output_root, baseline_manifest, expected_paths
        )
        atomic_json(Path(f"{stem}-pre-output-manifest.json"), pre_output)
        if not compare_manifests(baseline_manifest, pre_output)["equal_content"]:
            raise RuntimeError("minimal targeted restore did not reconstruct baseline output")
        metadata_before = manifest_payload(metadata_state.live)
        atomic_json(Path(f"{stem}-pre-metadata-manifest.json"), metadata_before)

        source_edit = apply_edit(source, original)
        source_marker = source.read_bytes().count(MARKER) == 1
        if measured:
            identifier = f"formal-targeted-nift-{label}"
            completed = run(
                [
                    sys.executable,
                    str(args.harness),
                    "run",
                    "--id",
                    identifier,
                    "--series",
                    "formal-targeted-edit",
                    "--scenario",
                    "one-page-explicit-target",
                    "--tool",
                    "nift",
                    "--round",
                    str(run_number),
                    "--warmth",
                    "warm",
                    "--output",
                    str(stem.with_suffix(".json")),
                    "--cwd",
                    str(project),
                    "--",
                    *command,
                ],
                env=environment,
                check=False,
            )
            record_path = stem.with_suffix(".json")
            record = json.loads(record_path.read_text()) if record_path.exists() else None
            if completed.returncode != 0:
                errors.append(f"harness exit code {completed.returncode}")
        else:
            try:
                untimed_command(label, command, project, environment, directory)
            except Exception as error:
                errors.append(f"command failed: {error}")

        source_marker = source.read_bytes().count(MARKER) == 1
        post_output = manifest_payload_reusing(output_root, pre_output, expected_paths)
        atomic_json(Path(f"{stem}-post-output-manifest.json"), post_output)
        output_diff = compare_manifests(pre_output, post_output)
        atomic_json(Path(f"{stem}-output-diff.json"), output_diff)
        marker_check = marker_evidence(output_root)
        expected_comparison = compare_manifests(
            load_manifest(expected_manifest(args, "nift")), post_output
        )
        atomic_json(Path(f"{stem}-expected-comparison.json"), expected_comparison)
        classification = changed_path_classification(
            contract["expected_changed_paths"], diff_path_sets(output_diff)
        )
        path_classification = {
            "schema": "cp10-edit-run-changed-path-classification",
            "schema_version": 1,
            "tool": "nift",
            "contract": str(contract_path),
            "contract_sha256": sha256_file(contract_path),
            "basis": contract["basis"],
            **classification,
            "expected_dependents": contract["expected_dependents"],
            "classified_expected_edit_paths": sorted(
                path
                for values in classification["observed"].values()
                for path in values
                if path
                not in {
                    item
                    for extras in classification["unexpected_unclassified"].values()
                    for item in extras
                }
            ),
            "normalizer_classification": None,
            "designated_output_marker": marker_check,
        }
        atomic_json(
            Path(f"{stem}-changed-path-classification.json"), path_classification
        )
        metadata_after = manifest_payload(metadata_state.live)
        atomic_json(Path(f"{stem}-post-metadata-manifest.json"), metadata_after)
        metadata_diff = compare_manifests(metadata_before, metadata_after)
        atomic_json(Path(f"{stem}-metadata-diff.json"), metadata_diff)
    except Exception as error:
        errors.append(f"attempt processing failed: {error}")
    finally:
        try:
            source_restoration = restore_source(source, original)
        except Exception as error:
            errors.append(f"source restoration failed: {error}")
        try:
            assert_no_stale_benchmark_processes((project,))
            restore_targeted_nift_state(project, baseline)
            minimal_state_restored = bool(
                manifest_payload(metadata_state.live)["entries_sha256"]
                == load_manifest(baseline / "nift-metadata-manifest.json")[
                    "entries_sha256"
                ]
                and file_identity(output_page)["sha256"]
                == setup["baseline"]["designated_output"]["sha256"]
                and file_identity(output_page)["mtime_ns"]
                == setup["baseline"]["designated_output"]["mtime_ns"]
            )
        except Exception as error:
            errors.append(f"minimal baseline restoration failed: {error}")

    infrastructure_valid = bool(
        not measured
        or record
        and record.get("validity", {}).get("infrastructure_valid") is True
    )
    output_correct = bool(expected_comparison and expected_comparison["equal_content"])
    paths_valid = bool(path_classification and path_classification["matches"])
    source_restored = bool(
        source_restoration
        and source_restoration["bytes_equal"]
        and source_restoration["mtime_equal"]
        and git_state(project) == git_before
    )
    formal_valid = bool(
        not errors
        and infrastructure_valid
        and source_marker
        and marker_check
        and marker_check["passed"]
        and output_correct
        and paths_valid
        and source_restored
        and minimal_state_restored
    )
    file_changes = (
        changed_files(output_diff, post_output)
        if output_diff and post_output
        else {"content_changed": [], "touched": []}
    )
    atomic_json(
        Path(f"{stem}-validation.json"),
        {
            "schema": "cp10-formal-edit-run-validation",
            "schema_version": SCHEMA_VERSION,
            "label": label,
            "tool": "nift",
            "targeted": True,
            "measured": measured,
            "round": run_number,
            "command": command,
            "infrastructure_valid": infrastructure_valid,
            "formal_valid": formal_valid,
            "errors": errors,
            "source_edit": source_edit,
            "source_marker_present": source_marker,
            "designated_output_marker": marker_check,
            "source_restoration": source_restoration,
            "source_and_git_restored": source_restored,
            "minimal_nift_state_restored": minimal_state_restored,
            "restored_states": [".nift/public", OUTPUT.as_posix()],
            "unaffected_output_recopied": False,
            "output_correct": output_correct,
            "changed_paths_valid": paths_valid,
            "changed_path_classification": (
                Path(f"{stem}-changed-path-classification.json").name
                if path_classification
                else None
            ),
            "content_changed_paths": (
                diff_path_sets(output_diff) if output_diff else None
            ),
            "mtime_only_paths": output_diff["mtime_only"] if output_diff else [],
            "regenerated_files": file_changes["content_changed"],
            "touched_files": file_changes["touched"],
            "metadata_diff": (
                Path(f"{stem}-metadata-diff.json").name if metadata_diff else None
            ),
            "aggregate_peak_memory_bytes": (
                record.get("cgroup", {}).get("memory_peak_bytes") if record else None
            ),
        },
    )
    return formal_valid


def run_paired_series_attempt(
    args: argparse.Namespace,
    spec: SeriesSpec,
    tool: str,
    label: str,
    round_number: int,
    git_before: dict[str, str],
    source_states: dict[str, SourceState],
    measured: bool,
) -> bool:
    directory = args.evidence / spec.mode
    stem = directory / label
    refuse_attempt_collision(directory, label)
    project = project_for(args, tool)
    paths = series_source_paths(args, spec, tool)
    states = states_for(tool, args.nift_project, args.astro_project)
    baseline = args.evidence / "setup/baseline"
    command, environment = series_command(args, spec, tool)
    errors: list[str] = []
    record: dict[str, Any] | None = None
    pre: dict[str, Any] | None = None
    post: dict[str, Any] | None = None
    difference: dict[str, Any] | None = None
    classification: dict[str, Any] | None = None
    markers: list[dict[str, Any]] = []
    output_correct = False
    metadata_diffs: dict[str, Any] = {}
    source_restored = False
    baseline_restored = False
    try:
        assert_no_stale_benchmark_processes((args.nift_project, args.astro_project))
        restore_states(tool, states, baseline)
        if tool == "astro":
            restore_astro_remote_inputs(args, args.astro_remote_archive_root)
        if git_state(project) != git_before:
            raise RuntimeError(f"{tool} Git state differs before {label}")
        pre = manifest_payload(states[0].live)
        atomic_json(Path(f"{stem}-pre-output-manifest.json"), pre)
        metadata_before = {}
        for state in states[1:]:
            if state.live.is_dir():
                metadata_before[state.name] = manifest_payload(state.live)
                atomic_json(
                    Path(f"{stem}-pre-{state.name}-manifest.json"),
                    metadata_before[state.name],
                )
        apply_series_edits(paths, source_states, spec, tool)
        if tool == "astro":
            restore_astro_remote_inputs(args, args.astro_remote_archive_root)
        if measured:
            completed = run(
                [
                    sys.executable, str(args.harness), "run", "--id", f"formal-{spec.mode}-{tool}-{label}",
                    "--series", f"formal-{spec.mode}", "--scenario", spec.scenario,
                    "--tool", tool, "--round", str(round_number), "--warmth", "warm",
                    "--output", str(stem.with_suffix(".json")), "--cwd", str(project), "--", *command,
                ],
                env=environment,
                check=False,
            )
            record_path = stem.with_suffix(".json")
            record = json.loads(record_path.read_text()) if record_path.exists() else None
            if completed.returncode:
                errors.append(f"harness exit code {completed.returncode}")
        else:
            try:
                untimed_command(label, command, project, environment, directory)
            except Exception as error:
                errors.append(f"command failed: {error}")
        post = manifest_payload(states[0].live)
        atomic_json(Path(f"{stem}-post-output-manifest.json"), post)
        difference = compare_manifests(pre, post)
        atomic_json(Path(f"{stem}-output-diff.json"), difference)
        markers = series_marker_evidence(states[0].live, spec)
        reference = args.evidence / f"setup/references/{tool}-edited-manifest.json"
        if tool == "nift":
            expected_comparison = compare_manifests(load_manifest(reference), post)
            atomic_json(Path(f"{stem}-expected-comparison.json"), expected_comparison)
            output_correct = expected_comparison["equal_content"]
            observed_paths = diff_path_sets(difference)
            normalizer_classification = None
        else:
            report, code = run_normalizer(
                args.astro_normalizer,
                [("clean-edited-reference", args.evidence / "setup/references/astro-edited-output"), ("recorded-edited-output", states[0].live)],
                [("clean-edited-reference", reference), ("recorded-edited-output", Path(f"{stem}-post-output-manifest.json"))],
                Path(f"{stem}-astro-normalization.json"),
            )
            output_correct = code == 0 and normalization_passed(report)
            change_report, change_code = run_normalizer(
                args.astro_normalizer,
                [("reconstructed-unedited-baseline", baseline / "snapshots/astro-output"), ("recorded-edited-output", states[0].live)],
                [("reconstructed-unedited-baseline", baseline / "astro-output-manifest.json"), ("recorded-edited-output", Path(f"{stem}-post-output-manifest.json"))],
                Path(f"{stem}-astro-change-normalization.json"),
            )
            if change_code != 1:
                raise RuntimeError("Astro series changed-path normalization failed")
            normalizer_classification = astro_normalized_change_set(
                change_report, "reconstructed-unedited-baseline", "recorded-edited-output"
            )
            observed_paths = normalizer_classification["paths"]
        contract_path = series_contract_path(args, tool)
        contract = json.loads(contract_path.read_text())
        validate_series_contract(contract, spec, tool)
        classified = changed_path_classification(contract["expected_changed_paths"], observed_paths)
        classification = {
            "schema": "cp10-series-run-changed-path-classification", "schema_version": 1,
            "mode": spec.mode, "tool": tool, "contract": str(contract_path),
            "contract_sha256": sha256_file(contract_path), **classified,
            "expected_dependents": contract["expected_dependents"],
            "normalizer_classification": normalizer_classification,
            "designated_output_markers": markers,
        }
        atomic_json(Path(f"{stem}-changed-path-classification.json"), classification)
        for state in states[1:]:
            after = manifest_payload(state.live) if state.live.is_dir() else None
            before = metadata_before.get(state.name)
            if after:
                atomic_json(Path(f"{stem}-post-{state.name}-manifest.json"), after)
            if before and after:
                metadata_diffs[state.name] = compare_manifests(before, after)
                atomic_json(Path(f"{stem}-{state.name}-diff.json"), metadata_diffs[state.name])
    except Exception as error:
        errors.append(f"attempt processing failed: {error}")
    finally:
        try:
            source_restored = restore_series_sources(paths, source_states) and git_state(project) == git_before
        except Exception as error:
            errors.append(f"source restoration failed: {error}")
        try:
            assert_no_stale_benchmark_processes((args.nift_project, args.astro_project))
            restore_states(tool, states, baseline)
            if tool == "astro":
                restore_astro_remote_inputs(args, args.astro_remote_archive_root)
            baseline_restored = baseline_states_equal(tool, states, baseline)
        except Exception as error:
            errors.append(f"baseline restoration failed: {error}")
    infrastructure_valid = bool(not measured or record and record.get("validity", {}).get("infrastructure_valid") is True)
    paths_valid = bool(classification and classification["matches"])
    formal_valid = bool(
        not errors and infrastructure_valid and output_correct and paths_valid
        and markers and all(item["passed"] for item in markers) and source_restored and baseline_restored
    )
    files = changed_files(difference, post) if difference and post else {"content_changed": [], "touched": []}
    atomic_json(
        Path(f"{stem}-validation.json"),
        {
            "schema": "cp10-formal-series-run-validation", "schema_version": 1,
            "mode": spec.mode, "scenario": spec.scenario, "tool": tool,
            "round": round_number, "measured": measured, "command": command,
            "infrastructure_valid": infrastructure_valid, "formal_valid": formal_valid,
            "errors": errors, "output_correct": output_correct, "changed_paths_valid": paths_valid,
            "source_and_git_restored": source_restored, "baseline_restored": baseline_restored,
            "designated_output_markers": markers,
            "content_changed_paths": diff_path_sets(difference) if difference else None,
            "content_changed_count": len(files["content_changed"]),
            "mtime_only_paths": difference["mtime_only"] if difference else [],
            "mtime_only_count": len(difference["mtime_only"]) if difference else 0,
            "regenerated_files": files["content_changed"], "regenerated_file_count": len(files["content_changed"]),
            "touched_files": files["touched"], "touched_file_count": len(files["touched"]),
            "metadata_diffs": {key: value["counts"] for key, value in metadata_diffs.items()},
            "aggregate_peak_memory_bytes": record.get("cgroup", {}).get("memory_peak_bytes") if record else None,
        },
    )
    return formal_valid


def run_batch_targeted_attempt(
    args: argparse.Namespace,
    spec: SeriesSpec,
    label: str,
    run_number: int,
    git_before: dict[str, str],
    source_states: dict[str, SourceState],
    measured: bool,
) -> bool:
    directory = args.evidence / spec.mode
    stem = directory / label
    refuse_attempt_collision(directory, label)
    project = args.nift_project
    paths = series_source_paths(args, spec, "nift")
    output_root = project / "public"
    baseline = args.evidence / "setup/baseline-minimal"
    setup = json.loads((args.evidence / "setup/series-setup.json").read_text())
    contract_path = series_contract_path(args, "nift")
    contract = json.loads(contract_path.read_text())
    command, environment = series_command(args, spec, "nift")
    errors: list[str] = []
    record: dict[str, Any] | None = None
    pre = post = difference = classification = None
    markers: list[dict[str, Any]] = []
    source_restored = minimal_restored = False
    output_correct = False
    try:
        assert_no_stale_benchmark_processes((project,))
        restore_batch_targeted_state(project, baseline, spec)
        baseline_manifest = load_manifest(Path(setup["baseline"]["manifest"]))
        force = {path for values in contract["expected_changed_paths"].values() for path in values}
        pre = manifest_payload_reusing(output_root, baseline_manifest, force)
        atomic_json(Path(f"{stem}-pre-output-manifest.json"), pre)
        if not compare_manifests(baseline_manifest, pre)["equal_content"]:
            raise RuntimeError("batch-targeted minimal restore differs from baseline")
        metadata_before = manifest_payload(project / ".nift/public")
        apply_series_edits(paths, source_states, spec, "nift")
        if measured:
            completed = run(
                [sys.executable, str(args.harness), "run", "--id", f"formal-{spec.mode}-{label}",
                 "--series", f"formal-{spec.mode}", "--scenario", spec.scenario, "--tool", "nift",
                 "--round", str(run_number), "--warmth", "warm", "--output", str(stem.with_suffix(".json")),
                 "--cwd", str(project), "--", *command],
                env=environment, check=False,
            )
            record_path = stem.with_suffix(".json")
            record = json.loads(record_path.read_text()) if record_path.exists() else None
            if completed.returncode:
                errors.append(f"harness exit code {completed.returncode}")
        else:
            try:
                untimed_command(label, command, project, environment, directory)
            except Exception as error:
                errors.append(f"command failed: {error}")
        post = manifest_payload_reusing(output_root, pre, force)
        atomic_json(Path(f"{stem}-post-output-manifest.json"), post)
        difference = compare_manifests(pre, post)
        atomic_json(Path(f"{stem}-output-diff.json"), difference)
        expected = compare_manifests(load_manifest(Path(setup["reference"]["manifest"])), post)
        atomic_json(Path(f"{stem}-expected-comparison.json"), expected)
        output_correct = expected["equal_content"]
        markers = series_marker_evidence(output_root, spec)
        classified = changed_path_classification(contract["expected_changed_paths"], diff_path_sets(difference))
        classification = {"schema": "cp10-series-run-changed-path-classification", "schema_version": 1,
                          "mode": spec.mode, "tool": "nift", "contract": str(contract_path), **classified,
                          "expected_dependents": contract["expected_dependents"], "designated_output_markers": markers}
        atomic_json(Path(f"{stem}-changed-path-classification.json"), classification)
        metadata_after = manifest_payload(project / ".nift/public")
        atomic_json(Path(f"{stem}-metadata-diff.json"), compare_manifests(metadata_before, metadata_after))
    except Exception as error:
        errors.append(f"attempt processing failed: {error}")
    finally:
        try:
            source_restored = restore_series_sources(paths, source_states) and git_state(project) == git_before
        except Exception as error:
            errors.append(f"source restoration failed: {error}")
        try:
            assert_no_stale_benchmark_processes((project,))
            restore_batch_targeted_state(project, baseline, spec)
            minimal_restored = all(
                file_identity(project / "public" / output)["sha256"]
                == setup["baseline"]["outputs"][output.as_posix()]["sha256"]
                for output in spec.outputs
            ) and manifest_payload(project / ".nift/public")["entries_sha256"] == load_manifest(
                baseline / "nift-metadata-manifest.json"
            )["entries_sha256"]
        except Exception as error:
            errors.append(f"minimal restoration failed: {error}")
    infrastructure_valid = bool(not measured or record and record.get("validity", {}).get("infrastructure_valid") is True)
    paths_valid = bool(classification and classification["matches"])
    formal_valid = bool(not errors and infrastructure_valid and output_correct and paths_valid and markers
                        and all(item["passed"] for item in markers) and source_restored and minimal_restored)
    files = changed_files(difference, post) if difference and post else {"content_changed": [], "touched": []}
    atomic_json(Path(f"{stem}-validation.json"), {
        "schema": "cp10-formal-series-run-validation", "schema_version": 1, "mode": spec.mode,
        "scenario": spec.scenario, "tool": "nift", "round": run_number, "measured": measured,
        "command": command, "infrastructure_valid": infrastructure_valid, "formal_valid": formal_valid,
        "errors": errors, "output_correct": output_correct, "changed_paths_valid": paths_valid,
        "source_and_git_restored": source_restored, "minimal_nift_state_restored": minimal_restored,
        "restored_states": [".nift/public", *[path.as_posix() for path in spec.outputs]],
        "unaffected_output_recopied": False, "designated_output_markers": markers,
        "content_changed_paths": diff_path_sets(difference) if difference else None,
        "content_changed_count": len(files["content_changed"]),
        "mtime_only_paths": difference["mtime_only"] if difference else [],
        "mtime_only_count": len(difference["mtime_only"]) if difference else 0,
        "regenerated_files": files["content_changed"], "regenerated_file_count": len(files["content_changed"]),
        "touched_files": files["touched"], "touched_file_count": len(files["touched"]),
        "aggregate_peak_memory_bytes": record.get("cgroup", {}).get("memory_peak_bytes") if record else None,
    })
    return formal_valid


def ensure_warmups(
    args: argparse.Namespace,
    mode: str,
    git_before: dict[str, dict[str, str]],
    sources: dict[str, SourceState],
) -> None:
    directory = args.evidence / mode
    complete = directory / "warmups-complete.json"
    if complete.exists():
        payload = json.loads(complete.read_text())
        expected = ["nift", "astro"] if mode == "normal" else ["nift"] * TARGET_WARMUPS
        if payload.get("tools") != expected or payload.get("passed") is not True:
            raise ValueError(f"invalid warmup completion marker: {complete}")
        return
    tools = ["nift", "astro"] if mode == "normal" else ["nift"] * TARGET_WARMUPS
    results = []
    for index, tool in enumerate(tools, 1):
        label = f"warmup-{tool}-{index:02d}-a{args.attempt:02d}"
        if mode == "targeted":
            results.append(
                run_targeted_attempt(
                    args,
                    label=label,
                    run_number=index,
                    git_before=git_before["nift"],
                    original=sources["nift"],
                    measured=False,
                )
            )
        else:
            results.append(
                run_attempt(
                    args,
                    tool=tool,
                    label=label,
                    round_number=index,
                    git_before=git_before[tool],
                    original=sources[tool],
                    targeted=False,
                    measured=False,
                )
            )
    if all(results):
        atomic_json(complete, {"tools": tools, "passed": True})
    else:
        raise RuntimeError(
            f"{mode} warmup failed; preserve it and retry with a higher --attempt"
        )


def run_normal(
    args: argparse.Namespace,
    git_before: dict[str, dict[str, str]],
    sources: dict[str, SourceState],
) -> None:
    for round_number in range(args.start, args.end + 1):
        first = NORMAL_ORDER[round_number - 1]
        second = "astro" if first == "nift" else "nift"
        for tool in (first, second):
            refuse_attempt_collision(
                args.evidence / "normal",
                f"{tool}-r{round_number:02d}-a{args.attempt:02d}",
            )
    ensure_warmups(args, "normal", git_before, sources)
    invalid: list[str] = []
    for round_number in range(args.start, args.end + 1):
        first = NORMAL_ORDER[round_number - 1]
        second = "astro" if first == "nift" else "nift"
        for tool in (first, second):
            label = f"{tool}-r{round_number:02d}-a{args.attempt:02d}"
            if not run_attempt(
                args,
                tool=tool,
                label=label,
                round_number=round_number,
                git_before=git_before[tool],
                original=sources[tool],
                targeted=False,
                measured=True,
            ):
                invalid.append(label)
    if invalid:
        raise RuntimeError(
            f"invalid normal attempt(s) preserved: {', '.join(invalid)}; rerun each whole pair with a higher --attempt"
        )


def run_targeted(
    args: argparse.Namespace,
    git_before: dict[str, dict[str, str]],
    sources: dict[str, SourceState],
) -> None:
    for run_number in range(args.start, args.end + 1):
        refuse_attempt_collision(
            args.evidence / "targeted",
            f"nift-run{run_number:02d}-a{args.attempt:02d}",
        )
    ensure_warmups(args, "targeted", git_before, sources)
    invalid: list[str] = []
    for run_number in range(args.start, args.end + 1):
        label = f"nift-run{run_number:02d}-a{args.attempt:02d}"
        if not run_targeted_attempt(
            args,
            label=label,
            run_number=run_number,
            git_before=git_before["nift"],
            original=sources["nift"],
            measured=True,
        ):
            invalid.append(label)
    if invalid:
        raise RuntimeError(
            f"invalid targeted attempt(s) preserved: {', '.join(invalid)}; rerun those run numbers with a higher --attempt"
        )


def run_paired_series(
    args: argparse.Namespace,
    spec: SeriesSpec,
    git_before: dict[str, dict[str, str]],
    source_states: dict[str, dict[str, SourceState]],
) -> None:
    directory = args.evidence / spec.mode
    warmup_marker = directory / "warmups-complete.json"
    if not warmup_marker.exists():
        warmup_results = []
        for index, tool in enumerate(("nift", "astro"), 1):
            warmup_results.append(run_paired_series_attempt(
                args, spec, tool, f"warmup-{tool}-{index:02d}-a{args.attempt:02d}", index,
                git_before[tool], source_states[tool], False,
            ))
        if not all(warmup_results):
            raise RuntimeError(f"{spec.mode} warmup failed")
        atomic_json(warmup_marker, {"passed": True, "tools": ["nift", "astro"]})
    invalid = []
    for round_number in range(args.start, args.end + 1):
        first = NORMAL_ORDER[round_number - 1]
        second = "astro" if first == "nift" else "nift"
        for tool in (first, second):
            label = f"{tool}-r{round_number:02d}-a{args.attempt:02d}"
            if not run_paired_series_attempt(
                args, spec, tool, label, round_number, git_before[tool], source_states[tool], True
            ):
                invalid.append(label)
    if invalid:
        raise RuntimeError(f"invalid {spec.mode} attempts preserved: {', '.join(invalid)}")


def run_batch_targeted_series(
    args: argparse.Namespace,
    spec: SeriesSpec,
    git_before: dict[str, str],
    source_states: dict[str, SourceState],
) -> None:
    directory = args.evidence / spec.mode
    warmup_marker = directory / "warmups-complete.json"
    if not warmup_marker.exists():
        results = [
            run_batch_targeted_attempt(
                args, spec, f"warmup-nift-{index:02d}-a{args.attempt:02d}", index,
                git_before, source_states, False,
            )
            for index in range(1, spec.warmups + 1)
        ]
        if not all(results):
            raise RuntimeError("batch-targeted warmup failed")
        atomic_json(warmup_marker, {"passed": True, "count": spec.warmups})
    invalid = []
    for run_number in range(args.start, args.end + 1):
        label = f"nift-run{run_number:02d}-a{args.attempt:02d}"
        if not run_batch_targeted_attempt(
            args, spec, label, run_number, git_before, source_states, True
        ):
            invalid.append(label)
    if invalid:
        raise RuntimeError(f"invalid batch-targeted attempts preserved: {', '.join(invalid)}")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mode",
        choices=("normal", "targeted", "batch-normal", "batch-targeted", "shared-normal"),
    )
    parser.add_argument("--nift-project", required=True, type=Path)
    parser.add_argument("--astro-project", type=Path)
    parser.add_argument("--harness", required=True, type=Path)
    parser.add_argument("--evidence", required=True, type=Path)
    parser.add_argument("--nift-expected", required=True, type=Path)
    parser.add_argument("--astro-clean-reference", type=Path)
    parser.add_argument("--astro-clean-reference-manifest", type=Path)
    parser.add_argument("--astro-normalizer", type=Path)
    parser.add_argument("--astro-remote-input-archive", type=Path)
    parser.add_argument("--astro-remote-input-manifest", type=Path)
    parser.add_argument("--nift-bin", default=Path("/usr/local/bin/nift"), type=Path)
    parser.add_argument(
        "--pnpm-bin",
        default=Path("/root/.cache/node/corepack/v1/pnpm/12.4.2/pnpm-native"),
        type=Path,
    )
    parser.add_argument("--start", default=1, type=int)
    parser.add_argument("--end", type=int)
    parser.add_argument("--attempt", default=1, type=int)
    args = parser.parse_args(argv)
    maximum = (
        SERIES_SPECS[args.mode].runs
        if args.mode in SERIES_SPECS
        else NORMAL_RUNS if args.mode == "normal" else TARGET_RUNS
    )
    args.end = maximum if args.end is None else args.end
    if not 1 <= args.start <= args.end <= maximum:
        parser.error(f"run range must be within 1..{maximum} for {args.mode}")
    if args.attempt < 1:
        parser.error("--attempt must be positive")
    required_paths = [
        "nift_project",
        "harness",
        "nift_expected",
        "nift_bin",
    ]
    astro_paths = [
        "astro_project",
        "astro_clean_reference",
        "astro_clean_reference_manifest",
        "astro_normalizer",
        "astro_remote_input_archive",
        "astro_remote_input_manifest",
    ]
    paired_mode = args.mode == "normal" or (
        args.mode in SERIES_SPECS and SERIES_SPECS[args.mode].paired
    )
    if paired_mode:
        missing = [name for name in astro_paths if getattr(args, name) is None]
        if missing:
            parser.error(
                f"normal mode requires --{missing[0].replace('_', '-')}"
            )
        required_paths.extend(astro_paths)
        required_paths.append("pnpm_bin")
    for name in required_paths:
        value = getattr(args, name).resolve()
        if not value.exists():
            parser.error(f"--{name.replace('_', '-')} does not exist: {value}")
        setattr(args, name, value)
    required_files = ["harness", "nift_expected"]
    if paired_mode:
        required_files.extend(
            (
                "astro_clean_reference_manifest",
                "astro_normalizer",
                "astro_remote_input_manifest",
            )
        )
    for name in required_files:
        if not getattr(args, name).is_file():
            parser.error(f"--{name.replace('_', '-')} must be a file")
    if paired_mode:
        if not args.astro_clean_reference.is_dir():
            parser.error("--astro-clean-reference must be a directory")
        if (
            args.astro_clean_reference == args.astro_project
            or args.astro_project in args.astro_clean_reference.parents
            or args.astro_clean_reference in args.astro_project.parents
        ):
            parser.error(
                "--astro-clean-reference must be retained outside the Astro project"
            )
        if args.astro_remote_input_archive.is_dir() and (
            args.astro_remote_input_archive == args.astro_project
            or args.astro_project in args.astro_remote_input_archive.parents
            or args.astro_remote_input_archive in args.astro_project.parents
        ):
            parser.error(
                "--astro-remote-input-archive directory must be outside the Astro project"
            )
    executables = ["nift_bin"] + (["pnpm_bin"] if paired_mode else [])
    for name in executables:
        if not getattr(args, name).is_file() or not os.access(getattr(args, name), os.X_OK):
            parser.error(f"--{name.replace('_', '-')} is not executable")
    args.evidence = args.evidence.resolve()
    return args


def run_campaign(args: argparse.Namespace) -> int:
    if args.evidence.exists() and not args.evidence.is_dir():
        raise ValueError(f"evidence path is not a directory: {args.evidence}")
    args.evidence.mkdir(parents=True, exist_ok=True)
    if args.mode == "batch-targeted":
        spec = SERIES_SPECS[args.mode]
        marker = args.evidence / "setup/series-setup.json"
        if marker.exists():
            git_before, source_states = batch_targeted_setup_ready(args, spec)
        else:
            if any(args.evidence.iterdir()):
                raise FileExistsError("refusing non-empty batch-targeted evidence directory")
            if args.attempt != 1:
                raise ValueError("replacement attempts require existing batch-targeted setup")
            git_before = git_state(args.nift_project)
            if git_before["status"]:
                raise RuntimeError("benchmark Nift worktree is not clean")
            source_states = {
                str(path): capture_source(path)
                for path in series_source_paths(args, spec, "nift")
            }
            prepare_batch_targeted_setup(args, spec, git_before, source_states)
        (args.evidence / spec.mode).mkdir(exist_ok=True)
        run_batch_targeted_series(args, spec, git_before, source_states)
        return 0
    if args.mode == "targeted":
        marker = args.evidence / "setup/targeted-setup.json"
        if marker.exists():
            git_state_before, source_state = targeted_setup_ready(args)
        else:
            if any(args.evidence.iterdir()):
                raise FileExistsError(
                    "refusing non-empty evidence directory without complete targeted setup: "
                    f"{args.evidence}"
                )
            if args.attempt != 1:
                raise ValueError("replacement attempts require existing targeted setup")
            git_state_before = git_state(args.nift_project)
            if git_state_before["status"]:
                raise RuntimeError("benchmark Nift worktree is not clean")
            source_state = capture_source(source_path(args, "nift"))
            prepare_targeted_setup(args, git_state_before, source_state)
        (args.evidence / "targeted").mkdir(exist_ok=True)
        run_targeted(
            args,
            {"nift": git_state_before},
            {"nift": source_state},
        )
        return 0

    if args.mode in ("batch-normal", "shared-normal"):
        spec = SERIES_SPECS[args.mode]
        args.astro_remote_input_archive_sha256 = (
            sha256_file(args.astro_remote_input_archive)
            if args.astro_remote_input_archive.is_file()
            else None
        )
        marker = args.evidence / "setup/series-setup.json"
        if marker.exists():
            args.astro_remote_archive_root = (
                args.astro_remote_input_archive
                if args.astro_remote_input_archive.is_dir()
                else args.evidence / "astro-remote-input-archive"
            )
            git_before, source_states = paired_series_setup_ready(args, spec)
        else:
            if any(args.evidence.iterdir()):
                raise FileExistsError(f"refusing non-empty {spec.mode} evidence directory")
            if args.attempt != 1:
                raise ValueError("replacement attempts require existing series setup")
            args.astro_remote_archive_root = prepare_remote_archive(args)
            git_before = {tool: git_state(project_for(args, tool)) for tool in ("nift", "astro")}
            if any(state["status"] for state in git_before.values()):
                raise RuntimeError("benchmark worktree is not clean")
            source_states = {
                tool: {
                    str(path): capture_source(path)
                    for path in series_source_paths(args, spec, tool)
                }
                for tool in ("nift", "astro")
            }
            prepare_paired_series_setup(args, spec, git_before, source_states)
        (args.evidence / spec.mode).mkdir(exist_ok=True)
        run_paired_series(args, spec, git_before, source_states)
        return 0

    args.astro_remote_input_archive_sha256 = (
        sha256_file(args.astro_remote_input_archive)
        if args.astro_remote_input_archive.is_file()
        else None
    )
    setup_marker = args.evidence / "setup/setup.json"
    if setup_marker.exists():
        args.astro_remote_archive_root = (
            args.astro_remote_input_archive
            if args.astro_remote_input_archive.is_dir()
            else args.evidence / "astro-remote-input-archive"
        )
        git_before, sources = setup_ready(args)
    else:
        if any(args.evidence.iterdir()):
            raise FileExistsError(
                f"refusing non-empty evidence directory without complete setup: {args.evidence}"
            )
        if args.attempt != 1:
            raise ValueError("replacement attempts require existing setup evidence")
        args.astro_remote_archive_root = prepare_remote_archive(args)
        git_before = {
            tool: git_state(project_for(args, tool)) for tool in ("nift", "astro")
        }
        dirty = [tool for tool, state in git_before.items() if state["status"]]
        if dirty:
            raise RuntimeError(f"benchmark worktree is not clean: {', '.join(dirty)}")
        sources = {tool: capture_source(source_path(args, tool)) for tool in ("nift", "astro")}
        prepare_setup(args, git_before, sources)
        git_before, sources = setup_ready(args)
    (args.evidence / args.mode).mkdir(exist_ok=True)
    if args.mode == "normal":
        run_normal(args, git_before, sources)
    else:
        run_targeted(args, git_before, sources)
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    with campaign_lock():
        projects = (
            (args.nift_project, args.astro_project)
            if args.mode == "normal" or (args.mode in SERIES_SPECS and SERIES_SPECS[args.mode].paired)
            else (args.nift_project,)
        )
        assert_no_stale_benchmark_processes(projects)
        return run_campaign(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileExistsError, FileNotFoundError, RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
