#!/usr/bin/env python3
"""Collect CP10 scenario C normal-edit and scenario D targeted-edit runs."""

from __future__ import annotations

import argparse
import json
import os
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


def verify_target(project: Path) -> dict[str, str]:
    tracked_path = project / ".nift/tracked.json"
    tracked = json.loads(tracked_path.read_text()).get("tracked", [])
    matches = [item for item in tracked if item.get("name") == NIFT_TARGET]
    if len(matches) != 1 or matches[0].get("output") != OUTPUT.as_posix():
        raise ValueError(f"Nift target is not uniquely mapped to {OUTPUT}: {NIFT_TARGET}")
    return {"name": NIFT_TARGET, "output": OUTPUT.as_posix()}


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
        results.append(
            run_attempt(
                args,
                tool=tool,
                label=label,
                round_number=index,
                git_before=git_before[tool],
                original=sources[tool],
                targeted=mode == "targeted",
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
        if not run_attempt(
            args,
            tool="nift",
            label=label,
            round_number=run_number,
            git_before=git_before["nift"],
            original=sources["nift"],
            targeted=True,
            measured=True,
        ):
            invalid.append(label)
    if invalid:
        raise RuntimeError(
            f"invalid targeted attempt(s) preserved: {', '.join(invalid)}; rerun those run numbers with a higher --attempt"
        )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("normal", "targeted"))
    parser.add_argument("--nift-project", required=True, type=Path)
    parser.add_argument("--astro-project", required=True, type=Path)
    parser.add_argument("--harness", required=True, type=Path)
    parser.add_argument("--evidence", required=True, type=Path)
    parser.add_argument("--nift-expected", required=True, type=Path)
    parser.add_argument("--astro-clean-reference", required=True, type=Path)
    parser.add_argument("--astro-clean-reference-manifest", required=True, type=Path)
    parser.add_argument("--astro-normalizer", required=True, type=Path)
    parser.add_argument("--astro-remote-input-archive", required=True, type=Path)
    parser.add_argument("--astro-remote-input-manifest", required=True, type=Path)
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
    maximum = NORMAL_RUNS if args.mode == "normal" else TARGET_RUNS
    args.end = maximum if args.end is None else args.end
    if not 1 <= args.start <= args.end <= maximum:
        parser.error(f"run range must be within 1..{maximum} for {args.mode}")
    if args.attempt < 1:
        parser.error("--attempt must be positive")
    for name in (
        "nift_project",
        "astro_project",
        "harness",
        "nift_expected",
        "astro_clean_reference",
        "astro_clean_reference_manifest",
        "astro_normalizer",
        "astro_remote_input_archive",
        "astro_remote_input_manifest",
        "nift_bin",
        "pnpm_bin",
    ):
        value = getattr(args, name).resolve()
        if not value.exists():
            parser.error(f"--{name.replace('_', '-')} does not exist: {value}")
        setattr(args, name, value)
    for name in (
        "harness",
        "nift_expected",
        "astro_clean_reference_manifest",
        "astro_normalizer",
        "astro_remote_input_manifest",
    ):
        if not getattr(args, name).is_file():
            parser.error(f"--{name.replace('_', '-')} must be a file")
    if not args.astro_clean_reference.is_dir():
        parser.error("--astro-clean-reference must be a directory")
    if (
        args.astro_clean_reference == args.astro_project
        or args.astro_project in args.astro_clean_reference.parents
        or args.astro_clean_reference in args.astro_project.parents
    ):
        parser.error("--astro-clean-reference must be retained outside the Astro project")
    if args.astro_remote_input_archive.is_dir() and (
        args.astro_remote_input_archive == args.astro_project
        or args.astro_project in args.astro_remote_input_archive.parents
        or args.astro_remote_input_archive in args.astro_project.parents
    ):
        parser.error(
            "--astro-remote-input-archive directory must be outside the Astro project"
        )
    for name in ("nift_bin", "pnpm_bin"):
        if not getattr(args, name).is_file() or not os.access(getattr(args, name), os.X_OK):
            parser.error(f"--{name.replace('_', '-')} is not executable")
    args.evidence = args.evidence.resolve()
    return args


def run_campaign(args: argparse.Namespace) -> int:
    if args.evidence.exists() and not args.evidence.is_dir():
        raise ValueError(f"evidence path is not a directory: {args.evidence}")
    args.evidence.mkdir(parents=True, exist_ok=True)
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
        assert_no_stale_benchmark_processes(
            (args.nift_project, args.astro_project)
        )
        return run_campaign(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileExistsError, FileNotFoundError, RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
