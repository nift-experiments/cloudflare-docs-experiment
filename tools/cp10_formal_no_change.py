#!/usr/bin/env python3
"""Collect the three CP10 scenario-B no-change paired rounds."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tarfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from .cp10_benchmark import (
        atomic_json,
        campaign_lock,
        CAMPAIGN_LOCK_FD_ENV,
        compare_manifests,
        load_manifest,
        manifest_payload,
        sha256_file,
        tree_entries,
    )
except ImportError:
    from cp10_benchmark import (  # type: ignore[no-redef]
        atomic_json,
        campaign_lock,
        CAMPAIGN_LOCK_FD_ENV,
        compare_manifests,
        load_manifest,
        manifest_payload,
        sha256_file,
        tree_entries,
    )


ORDER = ("nift", "astro", "astro")
SERIES = "formal-no-change-warm"


@dataclass(frozen=True)
class StatePath:
    name: str
    live: Path
    required: bool = True


def run(
    command: list[str],
    cwd: Path | None = None,
    *,
    env: dict[str, str] | None = None,
    stdout: Any = None,
    stderr: Any = None,
    check: bool = True,
) -> subprocess.CompletedProcess[Any]:
    pass_fds: tuple[int, ...] = ()
    inherited_lock = (env or os.environ).get(CAMPAIGN_LOCK_FD_ENV)
    if inherited_lock is not None:
        pass_fds = (int(inherited_lock),)
    return subprocess.run(
        command,
        cwd=cwd,
        env=env,
        stdout=stdout,
        stderr=stderr,
        check=check,
        pass_fds=pass_fds,
    )


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def copy_tree(source: Path, destination: Path) -> None:
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"refusing to overwrite snapshot: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    run(["cp", "-a", "--reflink=auto", "--", str(source), str(destination)])


def git_state(project: Path) -> dict[str, str]:
    def capture(*arguments: str) -> str:
        return subprocess.check_output(
            ["git", *arguments], cwd=project, text=True
        ).rstrip("\n")

    return {
        "head": capture("rev-parse", "HEAD"),
        "tree": capture("rev-parse", "HEAD^{tree}"),
        "status": capture("status", "--porcelain=v1"),
    }


def command_for(tool: str, nift_bin: Path, pnpm_bin: Path) -> tuple[list[str], dict[str, str]]:
    environment = os.environ.copy()
    environment["LC_ALL"] = "C"
    if tool == "nift":
        environment.pop("INCREMENTAL_BUILD", None)
        return [str(nift_bin), "build"], environment
    environment["INCREMENTAL_BUILD"] = "true"
    return [str(pnpm_bin), "exec", "astro", "build"], environment


def states_for(tool: str, nift_project: Path, astro_project: Path) -> list[StatePath]:
    if tool == "nift":
        return [
            StatePath("output", nift_project / "public"),
            StatePath("metadata", nift_project / ".nift/public"),
        ]
    return [
        StatePath("output", astro_project / "dist"),
        StatePath("metadata", astro_project / "node_modules/.astro"),
        StatePath("root-metadata", astro_project / ".astro", required=False),
    ]


def snapshot_states(
    tool: str, states: list[StatePath], baseline: Path
) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for state in states:
        snapshot = baseline / "snapshots" / f"{tool}-{state.name}"
        manifest = baseline / f"{tool}-{state.name}-manifest.json"
        if not state.live.exists():
            if state.required:
                raise FileNotFoundError(f"baseline state is absent: {state.live}")
            result[state.name] = {"present": False}
            continue
        copy_tree(state.live, snapshot)
        payload = manifest_payload(state.live)
        atomic_json(manifest, payload)
        copied = manifest_payload(snapshot)
        if copied["entries_sha256"] != payload["entries_sha256"]:
            raise RuntimeError(f"snapshot did not preserve exact state: {state.live}")
        result[state.name] = {
            "present": True,
            "snapshot": str(snapshot),
            "manifest": str(manifest),
            "entries_sha256": payload["entries_sha256"],
        }
    return result


def restore_states(tool: str, states: list[StatePath], baseline: Path) -> None:
    for state in states:
        remove_path(state.live)
        snapshot = baseline / "snapshots" / f"{tool}-{state.name}"
        manifest = baseline / f"{tool}-{state.name}-manifest.json"
        if not snapshot.exists():
            if manifest.exists() or state.required:
                raise RuntimeError(f"incomplete archived baseline for {tool} {state.name}")
            continue
        if not manifest.exists():
            raise RuntimeError(f"missing archived manifest for {tool} {state.name}")
        copy_tree(snapshot, state.live)
        restored = manifest_payload(state.live)
        expected = load_manifest(manifest)
        if restored["entries_sha256"] != expected["entries_sha256"]:
            raise RuntimeError(f"restored state is not exact: {state.live}")


def clean_nift(project: Path) -> None:
    remove_path(project / ".nift/public")
    tracked = json.loads((project / ".nift/tracked.json").read_text())["tracked"]
    output_root = (project / "public").resolve()
    for item in tracked:
        configured = item.get("output", "index.html")
        relative = Path(configured.lstrip("/"))
        if configured.endswith("/"):
            relative /= "index.html"
        output = (output_root / relative).resolve()
        if output_root not in output.parents:
            raise ValueError(f"unsafe Nift output path: {relative}")
        output.unlink(missing_ok=True)


def clean_astro(project: Path) -> None:
    for path in (project / "dist", project / ".astro", project / "node_modules/.astro"):
        remove_path(path)


def open_exclusive(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    return path.open("x")


def untimed(
    label: str,
    command: list[str],
    project: Path,
    environment: dict[str, str],
    evidence: Path,
) -> None:
    stdout_path = evidence / f"{label}.stdout.log"
    stderr_path = evidence / f"{label}.stderr.log"
    with open_exclusive(stdout_path) as stdout, open_exclusive(stderr_path) as stderr:
        run(command, project, env=environment, stdout=stdout, stderr=stderr)


def preserve_expected(source: Path, destination: Path) -> dict[str, Any]:
    payload = load_manifest(source)
    atomic_json(destination, payload)
    return payload


REMOTE_DATASETS = Path(
    "src/content/docs/logs/logpush/logpush-job/datasets"
)


def remote_selected_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selected = []
    for entry in entries:
        path = Path(entry["path"])
        if path.parts and path.parts[0] in {"skills", ".tmp"}:
            selected.append(entry)
            continue
        try:
            relative = path.relative_to(REMOTE_DATASETS)
        except ValueError:
            continue
        if len(relative.parts) == 2 and relative.suffix == ".md":
            selected.append(entry)
    return sorted(selected, key=lambda item: item["path"])


def prefixed_tree_entries(project: Path, relative: Path) -> list[dict[str, Any]]:
    root = project / relative
    if not root.is_dir():
        raise RuntimeError(f"restored remote-input directory is absent: {root}")
    item_stat = root.lstat()
    entries = [
        {
            "path": relative.as_posix(),
            "mode": f"{item_stat.st_mode & 0o7777:04o}",
            "mtime_ns": item_stat.st_mtime_ns,
            "type": "directory",
        }
    ]
    for entry in tree_entries(root):
        entry = entry.copy()
        entry["path"] = (relative / entry["path"]).as_posix()
        entries.append(entry)
    return entries


def actual_remote_selected_entries(
    project: Path, expected: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    entries = [
        *prefixed_tree_entries(project, Path("skills")),
        *prefixed_tree_entries(project, Path(".tmp")),
    ]
    expected_generated = {
        entry["path"] for entry in expected if entry["path"].startswith(f"{REMOTE_DATASETS}/")
    }
    for relative in sorted(expected_generated):
        path = project / relative
        if not path.is_file() or path.is_symlink():
            raise RuntimeError(f"restored generated markdown is absent or invalid: {path}")
        item_stat = path.stat()
        entries.append(
            {
                "path": relative,
                "mode": f"{item_stat.st_mode & 0o7777:04o}",
                "mtime_ns": item_stat.st_mtime_ns,
                "type": "file",
                "size": item_stat.st_size,
                "sha256": sha256_file(path, item_stat),
            }
        )
    return sorted(entries, key=lambda item: item["path"])


def prepare_remote_archive(args: argparse.Namespace) -> Path:
    if args.astro_remote_input_archive.is_dir():
        return args.astro_remote_input_archive
    destination = args.evidence / "astro-remote-input-archive"
    if destination.exists():
        raise FileExistsError(f"refusing existing extracted archive: {destination}")
    destination.mkdir()
    with tarfile.open(args.astro_remote_input_archive, "r:*") as archive:
        archive.extractall(destination, filter="data")
    return destination


def verify_remote_archive(args: argparse.Namespace, archive_root: Path) -> dict[str, Any]:
    if args.astro_remote_input_archive.is_file() and sha256_file(
        args.astro_remote_input_archive
    ) != args.astro_remote_input_archive_sha256:
        raise RuntimeError("frozen Astro remote-input archive file changed")
    expected = load_manifest(args.astro_remote_input_manifest)
    for entry in expected["entries"]:
        path = Path(entry["path"])
        try:
            relative = path.relative_to(REMOTE_DATASETS)
        except ValueError:
            continue
        if path.suffix == ".md" and len(relative.parts) != 2:
            raise RuntimeError(
                f"canonical manifest has unexpected generated markdown: {path}"
            )
    observed = manifest_payload(archive_root)
    if observed["entries_sha256"] != expected["entries_sha256"]:
        raise RuntimeError("frozen Astro remote-input archive differs from its manifest")
    return expected


def restore_astro_remote_inputs(args: argparse.Namespace, archive_root: Path) -> None:
    manifest = verify_remote_archive(args, archive_root)
    expected = remote_selected_entries(manifest["entries"])
    expected_generated = {
        entry["path"] for entry in expected if entry["path"].startswith(f"{REMOTE_DATASETS}/")
    }
    datasets = args.astro_project / REMOTE_DATASETS
    actual_generated = {
        path.relative_to(args.astro_project).as_posix()
        for path in datasets.rglob("*.md")
    } if datasets.is_dir() else set()
    unexpected = sorted(actual_generated - expected_generated)
    if unexpected:
        raise RuntimeError(f"unexpected generated markdown: {unexpected[0]}")
    remove_path(args.astro_project / "skills")
    remove_path(args.astro_project / ".tmp")
    for relative in sorted(actual_generated):
        (args.astro_project / relative).unlink()
    copy_tree(archive_root / "skills", args.astro_project / "skills")
    copy_tree(archive_root / ".tmp", args.astro_project / ".tmp")
    for relative in sorted(expected_generated):
        source = archive_root / relative
        destination = args.astro_project / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination, follow_symlinks=False)
    actual = actual_remote_selected_entries(args.astro_project, expected)
    if actual != expected:
        raise RuntimeError("restored Astro remote-input selected state differs from manifest")


def assert_no_stale_benchmark_processes(projects: tuple[Path, ...]) -> None:
    cgroup_root = Path("/sys/fs/cgroup")
    if cgroup_root.is_dir():
        for cgroup in cgroup_root.glob("cp10-*"):
            events = cgroup / "cgroup.events"
            if events.is_file() and "populated 1" in events.read_text().splitlines():
                raise RuntimeError(f"stale populated benchmark cgroup: {cgroup}")
    for process in Path("/proc").glob("[0-9]*"):
        try:
            pid = int(process.name)
            if pid == os.getpid():
                continue
            cwd = (process / "cwd").resolve(strict=True)
            command = (process / "cmdline").read_bytes().split(b"\0")
        except (FileNotFoundError, PermissionError, ProcessLookupError, ValueError):
            continue
        if not any(cwd == project or project in cwd.parents for project in projects):
            continue
        arguments = [item.decode(errors="replace") for item in command if item]
        stale = any(
            Path(argument).name == "nift"
            and index + 1 < len(arguments)
            and arguments[index + 1] == "build"
            for index, argument in enumerate(arguments)
        ) or ("astro" in arguments and "build" in arguments) or any(
            Path(argument).name == "cp10_benchmark.py"
            and index + 1 < len(arguments)
            and arguments[index + 1] == "run"
            for index, argument in enumerate(arguments)
        )
        if stale:
            raise RuntimeError(
                f"stale benchmark build process pid={pid}: {' '.join(arguments)}"
            )


def normalization_passed(report: dict[str, Any] | None) -> bool:
    return bool(
        report
        and report.get("schema") == "cp10-astro-normalization-report"
        and report.get("schema_version") == 1
        and report.get("normalized_equivalent") is True
        and report.get("rejected") == []
        and report.get("unclassified") == []
        and report.get("comparisons")
        and all(
            comparison.get("normalized", {}).get("equal") is True
            and comparison.get("unclassified") == []
            for comparison in report["comparisons"]
        )
    )


def run_normalizer(
    normalizer: Path,
    roots: list[tuple[str, Path]],
    manifests: list[tuple[str, Path]],
    output: Path,
) -> tuple[dict[str, Any] | None, int]:
    if output.exists():
        raise FileExistsError(f"refusing to overwrite evidence: {output}")
    command = [sys.executable, str(normalizer)]
    for label, root in roots:
        command.extend(("--root", f"{label}={root}"))
    for label, manifest in manifests:
        command.extend(("--manifest", f"{label}={manifest}"))
    command.extend(("--output", str(output)))
    completed = run(command, check=False)
    report = json.loads(output.read_text()) if output.exists() else None
    return report, completed.returncode


def prepare_baselines(args: argparse.Namespace, initial_git: dict[str, dict[str, str]]) -> None:
    baseline = args.evidence / "baseline"
    if baseline.exists():
        raise FileExistsError(f"refusing existing baseline evidence: {baseline}")
    baseline.mkdir(parents=True)
    nift_expected = preserve_expected(
        args.nift_expected, baseline / "nift-expected.json"
    )
    astro_reference_manifest = preserve_expected(
        args.astro_clean_reference_manifest,
        baseline / "astro-clean-reference-raw-manifest.json",
    )
    observed_reference = manifest_payload(args.astro_clean_reference)
    atomic_json(
        baseline / "astro-clean-reference-observed-manifest.json",
        observed_reference,
    )
    if (
        observed_reference["entries_sha256"]
        != astro_reference_manifest["entries_sha256"]
    ):
        raise RuntimeError("retained Astro clean reference differs from its raw manifest")
    setup: dict[str, Any] = {
        "schema": "cp10-no-change-baseline",
        "schema_version": 3,
        "snapshot_strategy": "cp -a --reflink=auto (CoW when supported, full-copy fallback)",
        "harness": {
            "path": str(args.harness),
            "sha256": sha256_file(args.harness),
        },
        "projects": {
            "nift": str(args.nift_project),
            "astro": str(args.astro_project),
        },
        "nift_expected_entries_sha256": nift_expected["entries_sha256"],
        "astro_normalization": {
            "normalizer": str(args.astro_normalizer),
            "normalizer_sha256": sha256_file(args.astro_normalizer),
            "clean_reference": str(args.astro_clean_reference),
            "clean_reference_manifest": str(
                args.astro_clean_reference_manifest
            ),
            "clean_reference_raw_entries_sha256": astro_reference_manifest[
                "entries_sha256"
            ],
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
            "entries_sha256": load_manifest(args.astro_remote_input_manifest)[
                "entries_sha256"
            ],
        },
        "git_before": initial_git,
        "tools": {},
    }

    for tool, project in (("nift", args.nift_project), ("astro", args.astro_project)):
        assert_no_stale_benchmark_processes(
            (args.nift_project, args.astro_project)
        )
        command, environment = command_for(tool, args.nift_bin, args.pnpm_bin)
        if tool == "nift":
            clean_nift(project)
            baseline_command = [str(args.nift_bin), "build", "--all"]
            baseline_environment = environment
        else:
            clean_astro(project)
            restore_astro_remote_inputs(args, args.astro_remote_archive_root)
            baseline_command = command
            baseline_environment = environment
        untimed(
            f"baseline/{tool}-build",
            baseline_command,
            project,
            baseline_environment,
            args.evidence,
        )
        current_git = git_state(project)
        if current_git != initial_git[tool]:
            raise RuntimeError(f"{tool} tracked Git state changed during baseline setup")
        states = states_for(tool, args.nift_project, args.astro_project)
        output = manifest_payload(states[0].live)
        archived = snapshot_states(tool, states, baseline)
        if tool == "nift":
            comparison = compare_manifests(nift_expected, output)
            atomic_json(baseline / "nift-expected-comparison.json", comparison)
            if not comparison["equal_content"]:
                raise RuntimeError("Nift baseline output differs from expected manifest")
        else:
            report, returncode = run_normalizer(
                args.astro_normalizer,
                [
                    ("clean-reference", args.astro_clean_reference),
                    ("incremental-baseline", states[0].live),
                ],
                [
                    (
                        "clean-reference",
                        baseline / "astro-clean-reference-raw-manifest.json",
                    ),
                    ("incremental-baseline", baseline / "astro-output-manifest.json"),
                ],
                baseline / "astro-clean-reference-normalization.json",
            )
            if returncode != 0 or not normalization_passed(report):
                raise RuntimeError(
                    "Astro incremental baseline is not normalized-equivalent to the clean reference"
                )
        setup["tools"][tool] = {
            "baseline_command": baseline_command,
            "recorded_command": command,
            "environment": {
                "INCREMENTAL_BUILD": environment.get("INCREMENTAL_BUILD"),
                "NODE_OPTIONS": environment.get("NODE_OPTIONS"),
                "LC_ALL": environment["LC_ALL"],
            },
            "states": archived,
        }

    for tool, project in (("nift", args.nift_project), ("astro", args.astro_project)):
        assert_no_stale_benchmark_processes(
            (args.nift_project, args.astro_project)
        )
        states = states_for(tool, args.nift_project, args.astro_project)
        restore_states(tool, states, baseline)
        if tool == "astro":
            restore_astro_remote_inputs(args, args.astro_remote_archive_root)
        command, environment = command_for(tool, args.nift_bin, args.pnpm_bin)
        untimed(f"baseline/{tool}-warmup", command, project, environment, args.evidence)
        warmup_manifest = manifest_payload(states[0].live)
        atomic_json(baseline / f"{tool}-warmup-output-manifest.json", warmup_manifest)
        baseline_manifest = load_manifest(baseline / f"{tool}-output-manifest.json")
        warmup_raw_diff = compare_manifests(baseline_manifest, warmup_manifest)
        atomic_json(baseline / f"{tool}-warmup-raw-diff.json", warmup_raw_diff)
        if tool == "nift":
            warmup_comparison = compare_manifests(nift_expected, warmup_manifest)
            atomic_json(
                baseline / "nift-warmup-expected-comparison.json",
                warmup_comparison,
            )
            warmup_valid = warmup_comparison["equal_content"]
        else:
            report, returncode = run_normalizer(
                args.astro_normalizer,
                [
                    ("archived-pre-state", baseline / "snapshots/astro-output"),
                    ("warmup-output", states[0].live),
                ],
                [
                    ("archived-pre-state", baseline / "astro-output-manifest.json"),
                    ("warmup-output", baseline / "astro-warmup-output-manifest.json"),
                ],
                baseline / "astro-warmup-normalization.json",
            )
            warmup_valid = returncode == 0 and normalization_passed(report)
        if not warmup_valid or git_state(project) != initial_git[tool]:
            raise RuntimeError(f"{tool} warmup failed correctness validation")

    setup["git_after"] = {
        "nift": git_state(args.nift_project),
        "astro": git_state(args.astro_project),
    }
    atomic_json(baseline / "baseline.json", setup)


def baseline_ready(args: argparse.Namespace) -> dict[str, dict[str, str]]:
    marker = args.evidence / "baseline/baseline.json"
    payload = json.loads(marker.read_text())
    if payload.get("schema") != "cp10-no-change-baseline" or payload.get("schema_version") != 3:
        raise ValueError(f"invalid baseline marker: {marker}")
    expected_commands = {
        tool: command_for(tool, args.nift_bin, args.pnpm_bin)[0]
        for tool in ("nift", "astro")
    }
    for tool, command in expected_commands.items():
        if payload["tools"][tool]["recorded_command"] != command:
            raise ValueError(f"{tool} executable differs from archived baseline")
        environment = command_for(tool, args.nift_bin, args.pnpm_bin)[1]
        relevant_environment = {
            "INCREMENTAL_BUILD": environment.get("INCREMENTAL_BUILD"),
            "NODE_OPTIONS": environment.get("NODE_OPTIONS"),
            "LC_ALL": environment["LC_ALL"],
        }
        if payload["tools"][tool]["environment"] != relevant_environment:
            raise ValueError(f"{tool} environment differs from archived baseline")
    nift_expected = load_manifest(args.nift_expected)
    if payload["nift_expected_entries_sha256"] != nift_expected["entries_sha256"]:
        raise ValueError("Nift expected manifest differs from archived baseline")
    astro_reference_manifest = load_manifest(args.astro_clean_reference_manifest)
    astro_binding = payload["astro_normalization"]
    if (
        astro_binding["normalizer"] != str(args.astro_normalizer)
        or astro_binding["normalizer_sha256"] != sha256_file(args.astro_normalizer)
        or astro_binding["clean_reference"] != str(args.astro_clean_reference)
        or astro_binding["clean_reference_manifest"]
        != str(args.astro_clean_reference_manifest)
        or astro_binding["clean_reference_raw_entries_sha256"]
        != astro_reference_manifest["entries_sha256"]
    ):
        raise ValueError("Astro normalizer or clean reference binding differs")
    observed_reference = manifest_payload(args.astro_clean_reference)
    if observed_reference["entries_sha256"] != astro_reference_manifest["entries_sha256"]:
        raise ValueError("retained Astro clean reference differs from its raw manifest")
    if payload["harness"] != {
        "path": str(args.harness),
        "sha256": sha256_file(args.harness),
    } or payload["projects"] != {
        "nift": str(args.nift_project),
        "astro": str(args.astro_project),
    }:
        raise ValueError("project or harness path differs from archived baseline")
    remote = payload["astro_remote_inputs"]
    if (
        remote["archive"] != str(args.astro_remote_input_archive)
        or remote["archive_sha256"]
        != (
            sha256_file(args.astro_remote_input_archive)
            if args.astro_remote_input_archive.is_file()
            else None
        )
        or remote["archive_root"] != str(args.astro_remote_archive_root)
        or remote["manifest"] != str(args.astro_remote_input_manifest)
        or remote["entries_sha256"]
        != load_manifest(args.astro_remote_input_manifest)["entries_sha256"]
    ):
        raise ValueError("Astro remote-input binding differs")
    verify_remote_archive(args, args.astro_remote_archive_root)
    if payload["git_before"] != payload["git_after"]:
        raise ValueError("baseline setup changed tracked Git state")
    return payload["git_before"]


def artifact_paths(evidence: Path, tool: str, round_number: int, attempt: int) -> list[Path]:
    stem = f"{tool}-r{round_number:02d}-a{attempt:02d}"
    return [
        evidence / f"{stem}.json",
        evidence / f"{stem}.stdout.log",
        evidence / f"{stem}.stderr.log",
        evidence / f"{stem}.time.txt",
        evidence / f"{stem}-pre-output-manifest.json",
        evidence / f"{stem}-post-output-manifest.json",
        evidence / f"{stem}-output-diff.json",
        evidence / f"{stem}-expected-comparison.json",
        evidence / f"{stem}-astro-normalization.json",
        evidence / f"{stem}-validation.json",
        *[
            evidence / f"{stem}-{phase}-{name}-{kind}.json"
            for name in ("metadata", "root-metadata")
            for phase, kind in (("pre", "manifest"), ("post", "manifest"))
        ],
        *[
            evidence / f"{stem}-{name}-diff.json"
            for name in ("metadata", "root-metadata")
        ],
    ]


def preflight_attempt(args: argparse.Namespace) -> None:
    collisions = [
        path
        for round_number in range(args.start_round, args.end_round + 1)
        for tool in (ORDER[round_number - 1], "astro" if ORDER[round_number - 1] == "nift" else "nift")
        for path in artifact_paths(args.evidence, tool, round_number, args.attempt)
        if path.exists()
    ]
    if collisions:
        raise FileExistsError(f"refusing to overwrite evidence: {collisions[0]}")


def record_run(args: argparse.Namespace, tool: str, round_number: int, git_before: dict[str, str]) -> None:
    project = args.nift_project if tool == "nift" else args.astro_project
    baseline = args.evidence / "baseline"
    states = states_for(tool, args.nift_project, args.astro_project)
    assert_no_stale_benchmark_processes((args.nift_project, args.astro_project))
    restore_states(tool, states, baseline)
    if tool == "astro":
        restore_astro_remote_inputs(args, args.astro_remote_archive_root)
    if git_state(project) != git_before:
        raise RuntimeError(f"{tool} tracked Git state differs before recorded run")

    stem = f"{tool}-r{round_number:02d}-a{args.attempt:02d}"
    pre_manifest = manifest_payload(states[0].live)
    atomic_json(args.evidence / f"{stem}-pre-output-manifest.json", pre_manifest)
    metadata_before: dict[str, dict[str, Any]] = {}
    for state in states[1:]:
        if state.live.is_dir():
            payload = manifest_payload(state.live)
            metadata_before[state.name] = payload
            atomic_json(args.evidence / f"{stem}-pre-{state.name}-manifest.json", payload)
    command, environment = command_for(tool, args.nift_bin, args.pnpm_bin)
    identifier = f"formal-no-change-{tool}-r{round_number:02d}-a{args.attempt:02d}"
    harness_command = [
        sys.executable,
        str(args.harness),
        "run",
        "--id",
        identifier,
        "--series",
        SERIES,
        "--scenario",
        "no-change",
        "--tool",
        tool,
        "--round",
        str(round_number),
        "--warmth",
        "warm",
        "--output",
        str(args.evidence / f"{stem}.json"),
        "--cwd",
        str(project),
        "--",
        *command,
    ]
    completed = run(harness_command, env=environment, check=False)

    record_path = args.evidence / f"{stem}.json"
    record = json.loads(record_path.read_text()) if record_path.exists() else None
    infrastructure_valid = bool(
        completed.returncode == 0
        and record
        and record.get("validity", {}).get("infrastructure_valid") is True
    )
    post_manifest = manifest_payload(states[0].live) if states[0].live.is_dir() else None
    output_diff = compare_manifests(pre_manifest, post_manifest) if post_manifest else None
    expected_comparison = None
    normalization_report = None
    normalization_returncode = None
    if tool == "nift" and post_manifest:
        expected = load_manifest(baseline / "nift-expected.json")
        expected_comparison = compare_manifests(expected, post_manifest)
    if post_manifest:
        atomic_json(args.evidence / f"{stem}-post-output-manifest.json", post_manifest)
    if output_diff:
        atomic_json(args.evidence / f"{stem}-output-diff.json", output_diff)
    if expected_comparison:
        atomic_json(args.evidence / f"{stem}-expected-comparison.json", expected_comparison)
    if tool == "astro" and post_manifest:
        normalization_report, normalization_returncode = run_normalizer(
            args.astro_normalizer,
            [
                ("archived-pre-state", baseline / "snapshots/astro-output"),
                ("recorded-output", states[0].live),
            ],
            [
                ("archived-pre-state", baseline / "astro-output-manifest.json"),
                ("recorded-output", args.evidence / f"{stem}-post-output-manifest.json"),
            ],
            args.evidence / f"{stem}-astro-normalization.json",
        )
    metadata_diffs: dict[str, str] = {}
    for state in states[1:]:
        before = metadata_before.get(state.name)
        after = manifest_payload(state.live) if state.live.is_dir() else None
        if after:
            atomic_json(args.evidence / f"{stem}-post-{state.name}-manifest.json", after)
        if before and after:
            difference = compare_manifests(before, after)
            difference_path = args.evidence / f"{stem}-{state.name}-diff.json"
            atomic_json(difference_path, difference)
            metadata_diffs[state.name] = difference_path.name
    source_unchanged = git_state(project) == git_before
    if tool == "nift":
        output_valid = bool(
            expected_comparison and expected_comparison["equal_content"]
        )
    else:
        output_valid = bool(
            normalization_returncode == 0
            and normalization_passed(normalization_report)
        )
    content_valid = output_valid and source_unchanged
    validation = {
        "schema": "cp10-no-change-run-validation",
        "schema_version": 1,
        "run_id": identifier,
        "logical_round": round_number,
        "attempt": args.attempt,
        "infrastructure_valid": infrastructure_valid,
        "content_valid": content_valid,
        "formal_valid": infrastructure_valid and content_valid,
        "source_unchanged": source_unchanged,
        "output_diff": f"{stem}-output-diff.json" if output_diff else None,
        "expected_comparison": f"{stem}-expected-comparison.json" if expected_comparison else None,
        "normalization_report": (
            f"{stem}-astro-normalization.json" if normalization_report else None
        ),
        "normalization_returncode": normalization_returncode,
        "metadata_diffs": metadata_diffs,
        "mtime_only_paths": output_diff["mtime_only"] if output_diff else [],
        "raw_output_diff_counts": output_diff["counts"] if output_diff else None,
        "content_changed_paths": {
            key: output_diff[key] if output_diff else []
            for key in ("added", "removed", "changed")
        },
    }
    atomic_json(args.evidence / f"{stem}-validation.json", validation)
    if not validation["formal_valid"]:
        raise RuntimeError(
            f"invalid {tool} run {identifier}; preserve this attempt and replace the whole "
            f"round with --start-round {round_number} --end-round {round_number} "
            f"--attempt {args.attempt + 1}"
        )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nift-project", required=True, type=Path)
    parser.add_argument("--astro-project", required=True, type=Path)
    parser.add_argument("--harness", required=True, type=Path)
    parser.add_argument("--evidence", required=True, type=Path)
    parser.add_argument("--nift-expected", required=True, type=Path)
    parser.add_argument("--astro-clean-reference", required=True, type=Path)
    parser.add_argument(
        "--astro-clean-reference-manifest", required=True, type=Path
    )
    parser.add_argument("--astro-normalizer", required=True, type=Path)
    parser.add_argument("--astro-remote-input-archive", required=True, type=Path)
    parser.add_argument("--astro-remote-input-manifest", required=True, type=Path)
    parser.add_argument("--nift-bin", default=Path("/usr/local/bin/nift"), type=Path)
    parser.add_argument(
        "--pnpm-bin",
        default=Path("/root/.cache/node/corepack/v1/pnpm/12.4.2/pnpm-native"),
        type=Path,
    )
    parser.add_argument("--start-round", default=1, type=int)
    parser.add_argument("--end-round", default=3, type=int)
    parser.add_argument("--attempt", default=1, type=int)
    args = parser.parse_args(argv)
    if not 1 <= args.start_round <= args.end_round <= len(ORDER):
        parser.error("round range must be within 1..3")
    if args.attempt < 1:
        parser.error("attempt must be positive")
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
    ):
        value = getattr(args, name).resolve()
        if not value.exists():
            parser.error(f"--{name.replace('_', '-')} does not exist: {value}")
        setattr(args, name, value)
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
    for name in (
        "harness",
        "nift_expected",
        "astro_clean_reference_manifest",
        "astro_normalizer",
        "astro_remote_input_manifest",
    ):
        if not getattr(args, name).is_file():
            parser.error(f"--{name.replace('_', '-')} must be a file")
    args.nift_bin = args.nift_bin.resolve()
    args.pnpm_bin = args.pnpm_bin.resolve()
    for name in ("nift_bin", "pnpm_bin"):
        value = getattr(args, name)
        if not value.is_file() or not os.access(value, os.X_OK):
            parser.error(f"--{name.replace('_', '-')} is not executable: {value}")
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
    marker = args.evidence / "baseline/baseline.json"
    if marker.exists():
        args.astro_remote_archive_root = (
            args.astro_remote_input_archive
            if args.astro_remote_input_archive.is_dir()
            else args.evidence / "astro-remote-input-archive"
        )
        initial_git = baseline_ready(args)
    else:
        if any(args.evidence.iterdir()):
            raise FileExistsError(
                f"refusing non-empty evidence directory without a complete baseline: {args.evidence}"
            )
        if args.attempt != 1:
            raise ValueError("replacement attempts require an existing archived baseline")
        args.astro_remote_archive_root = prepare_remote_archive(args)
        initial_git = {
            "nift": git_state(args.nift_project),
            "astro": git_state(args.astro_project),
        }
        dirty = [tool for tool, state in initial_git.items() if state["status"]]
        if dirty:
            raise RuntimeError(f"benchmark worktree is not clean: {', '.join(dirty)}")
        prepare_baselines(args, initial_git)
        initial_git = baseline_ready(args)
    preflight_attempt(args)

    for round_number in range(args.start_round, args.end_round + 1):
        first = ORDER[round_number - 1]
        second = "astro" if first == "nift" else "nift"
        for tool in (first, second):
            record_run(args, tool, round_number, initial_git[tool])
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
