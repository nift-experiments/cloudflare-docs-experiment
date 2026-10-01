#!/usr/bin/env python3
"""CP10 benchmark runner and evidence utilities.

The timed runner requires root on cgroup v2. It places the complete measured
process tree in a dedicated cgroup, captures aggregate memory evidence, and
retains stdout/stderr beside an atomic JSON record.
"""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import math
import os
import random
import re
import stat as stat_module
import statistics
import sys
import tempfile
import threading
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA_VERSION = 1
CHUNK_SIZE = 1024 * 1024


def sha256_file(path: Path, expected: os.stat_result | None = None) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        before = os.fstat(handle.fileno())
        if expected and (before.st_dev, before.st_ino) != (expected.st_dev, expected.st_ino):
            raise RuntimeError(f"file changed during manifest traversal: {path}")
        while chunk := handle.read(CHUNK_SIZE):
            digest.update(chunk)
        after = os.fstat(handle.fileno())
    identity = lambda value: (
        value.st_dev,
        value.st_ino,
        value.st_mode,
        value.st_size,
        value.st_mtime_ns,
    )
    if identity(before) != identity(after):
        raise RuntimeError(f"file changed while hashing: {path}")
    return digest.hexdigest()


def tree_entries(root: Path) -> list[dict[str, Any]]:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f"manifest root is not a directory: {root}")
    entries: list[dict[str, Any]] = []
    def walk_error(error: OSError) -> None:
        raise error

    for current, dirnames, filenames in os.walk(
        root, followlinks=False, onerror=walk_error
    ):
        dirnames.sort()
        filenames.sort()
        current_path = Path(current)
        for name in [*dirnames, *filenames]:
            path = current_path / name
            relative = path.relative_to(root).as_posix()
            stat = path.lstat()
            entry: dict[str, Any] = {
                "path": relative,
                "mode": f"{stat.st_mode & 0o7777:04o}",
                "mtime_ns": stat.st_mtime_ns,
            }
            if path.is_symlink():
                entry.update(type="symlink", target=os.readlink(path))
                if name in dirnames:
                    dirnames.remove(name)
            elif stat_module.S_ISDIR(stat.st_mode):
                entry["type"] = "directory"
            elif stat_module.S_ISREG(stat.st_mode):
                entry.update(
                    type="file",
                    size=stat.st_size,
                    sha256=sha256_file(path, stat),
                )
            else:
                raise ValueError(f"unsupported filesystem object: {path}")
            entries.append(entry)
    entries.sort(key=lambda entry: entry["path"])
    return entries


def manifest_payload(root: Path) -> dict[str, Any]:
    entries = tree_entries(root)
    canonical = json.dumps(
        entries, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    files = [entry for entry in entries if entry["type"] == "file"]
    return {
        "schema": "cp10-tree-manifest",
        "schema_version": SCHEMA_VERSION,
        "root_label": root.name,
        "entries_sha256": hashlib.sha256(canonical).hexdigest(),
        "summary": {
            "entries": len(entries),
            "files": len(files),
            "bytes": sum(entry["size"] for entry in files),
        },
        "entries": entries,
    }


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"refusing to overwrite evidence: {path}")
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent, delete=False
    ) as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
        temporary = Path(handle.name)
    try:
        os.link(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)
    directory_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)


def load_manifest(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text())
    if (
        payload.get("schema") != "cp10-tree-manifest"
        or payload.get("schema_version") != SCHEMA_VERSION
    ):
        raise ValueError(f"not a CP10 tree manifest: {path}")
    entries = payload.get("entries")
    if not isinstance(entries, list):
        raise ValueError(f"manifest has no entry list: {path}")
    entry_paths = [entry.get("path") for entry in entries]
    if len(entry_paths) != len(set(entry_paths)) or any(
        not isinstance(item, str) or item.startswith("/") or ".." in Path(item).parts
        for item in entry_paths
    ):
        raise ValueError(f"manifest has duplicate or unsafe paths: {path}")
    canonical = json.dumps(
        entries, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    if hashlib.sha256(canonical).hexdigest() != payload.get("entries_sha256"):
        raise ValueError(f"manifest digest mismatch: {path}")
    files = [entry for entry in entries if entry.get("type") == "file"]
    expected_summary = {
        "entries": len(entries),
        "files": len(files),
        "bytes": sum(entry.get("size", 0) for entry in files),
    }
    if payload.get("summary") != expected_summary:
        raise ValueError(f"manifest summary mismatch: {path}")
    return payload


def semantic_entry(entry: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value for key, value in entry.items() if key not in {"mode", "mtime_ns"}
    }


def compare_manifests(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    old = {entry["path"]: entry for entry in before["entries"]}
    new = {entry["path"]: entry for entry in after["entries"]}
    added = sorted(new.keys() - old.keys())
    removed = sorted(old.keys() - new.keys())
    changed = sorted(
        path
        for path in old.keys() & new.keys()
        if semantic_entry(old[path]) != semantic_entry(new[path])
    )
    mtime_only = sorted(
        path
        for path in old.keys() & new.keys()
        if semantic_entry(old[path]) == semantic_entry(new[path])
        and old[path].get("mtime_ns") != new[path].get("mtime_ns")
    )
    return {
        "schema": "cp10-manifest-diff",
        "schema_version": SCHEMA_VERSION,
        "equal_content": not (added or removed or changed),
        "added": added,
        "removed": removed,
        "changed": changed,
        "mtime_only": mtime_only,
        "counts": {
            "added": len(added),
            "removed": len(removed),
            "changed": len(changed),
            "mtime_only": len(mtime_only),
        },
    }


def parse_time_verbose(path: Path) -> dict[str, Any]:
    values: dict[str, str] = {}
    for line in path.read_text(errors="replace").splitlines():
        if not line or "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key in values:
            raise ValueError(f"duplicate GNU time field: {key}")
        values[key] = value
    integer_fields = {
        "maximum_rss_kib",
        "major_page_faults",
        "minor_page_faults",
        "voluntary_context_switches",
        "involuntary_context_switches",
        "filesystem_inputs",
        "filesystem_outputs",
        "swaps",
        "exit_status",
    }
    float_fields = {"user_seconds", "system_seconds", "wall_seconds"}
    required = integer_fields | float_fields | {"cpu_percent"}
    if set(values) != required:
        raise ValueError(
            f"GNU time fields differ: missing={sorted(required - set(values))}, "
            f"extra={sorted(set(values) - required)}"
        )
    result: dict[str, Any] = {key: int(values[key]) for key in integer_fields}
    result.update({key: float(values[key]) for key in float_fields})
    result["cpu_percent"] = float(values["cpu_percent"].rstrip("%"))
    if any(
        not isinstance(value, int) and not math.isfinite(value)
        for value in result.values()
    ) or any(value < 0 for value in result.values()):
        raise ValueError("GNU time contains non-finite or negative values")
    return result


def read_key_values(path: Path) -> dict[str, int]:
    result: dict[str, int] = {}
    for line in path.read_text().splitlines():
        key, value = line.split()
        result[key] = int(value)
    return result


def read_pressure(path: Path) -> dict[str, dict[str, float | int]]:
    result: dict[str, dict[str, float | int]] = {}
    for line in path.read_text().splitlines():
        fields = line.split()
        values: dict[str, float | int] = {}
        for field in fields[1:]:
            key, raw = field.split("=", 1)
            values[key] = int(raw) if key == "total" else float(raw)
        result[fields[0]] = values
    return result


def host_sample() -> dict[str, Any]:
    meminfo: dict[str, int] = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, raw = line.split(":", 1)
        meminfo[key] = int(raw.strip().split()[0]) * 1024
    vmstat = read_key_values(Path("/proc/vmstat"))
    frequencies: dict[str, int] = {}
    for path in sorted(Path("/sys/devices/system/cpu").glob("cpu[0-9]*/cpufreq/scaling_cur_freq")):
        try:
            frequencies[path.parts[-3]] = int(path.read_text().strip())
        except (OSError, ValueError):
            pass
    diskstats: dict[str, list[int]] = {}
    for line in Path("/proc/diskstats").read_text().splitlines():
        fields = line.split()
        if len(fields) >= 14 and fields[2].startswith(("sd", "vd", "nvme")):
            diskstats[fields[2]] = [int(value) for value in fields[3:]]
    swap_lines = Path("/proc/swaps").read_text().splitlines()
    return {
        "monotonic_seconds": time.monotonic(),
        "load_average": os.getloadavg(),
        "memory_available_bytes": meminfo.get("MemAvailable"),
        "swap_total_bytes": meminfo.get("SwapTotal"),
        "swap_free_bytes": meminfo.get("SwapFree"),
        "active_swap_devices": swap_lines[1:],
        "pswpin": vmstat.get("pswpin"),
        "pswpout": vmstat.get("pswpout"),
        "cpu_frequency_khz": frequencies,
        "diskstats": diskstats,
        "memory_pressure": read_pressure(Path("/proc/pressure/memory")),
        "cpu_pressure": read_pressure(Path("/proc/pressure/cpu")),
        "io_pressure": read_pressure(Path("/proc/pressure/io")),
    }


def read_int(path: Path) -> int | None:
    try:
        return int(path.read_text().strip())
    except (FileNotFoundError, ValueError):
        return None


def safe_id(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-.")
    if not cleaned:
        raise ValueError("run id contains no safe characters")
    return cleaned[:80]


def cgroup_populated(cgroup: Path) -> bool:
    return read_key_values(cgroup / "cgroup.events").get("populated") == 1


def wait_cgroup_empty(cgroup: Path, timeout: float) -> bool:
    deadline = time.monotonic() + timeout
    while cgroup_populated(cgroup) and time.monotonic() < deadline:
        time.sleep(0.05)
    return not cgroup_populated(cgroup)


def artifact_record(path: Path) -> dict[str, Any]:
    return {
        "name": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def execute_run(args: argparse.Namespace) -> int:
    if os.geteuid() != 0:
        raise PermissionError("the timed runner must be root for cgroup accounting")
    cgroup_root = Path("/sys/fs/cgroup")
    if not (cgroup_root / "cgroup.controllers").exists():
        raise RuntimeError("cgroup v2 is required")
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    identifier = safe_id(args.id)
    artifact_stem = output.name.removesuffix(".json")
    stdout_path = output.parent / f"{artifact_stem}.stdout.log"
    stderr_path = output.parent / f"{artifact_stem}.stderr.log"
    time_path = output.parent / f"{artifact_stem}.time.txt"
    for path in (output, stdout_path, stderr_path, time_path):
        if path.exists():
            raise FileExistsError(f"refusing artifact collision: {path}")
    for path in (stdout_path, stderr_path, time_path):
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
        os.close(descriptor)
    cgroup = cgroup_root / f"cp10-{identifier}-{os.getpid()}"
    lock_path = Path("/run/lock/cp10-benchmark.lock")
    start_utc = datetime.now(timezone.utc).isoformat()
    samples: list[dict[str, Any]] = []
    monitor_errors: list[str] = []
    stop_sampling = threading.Event()
    sampling_thread: threading.Thread | None = None
    lock = None
    pid: int | None = None
    reaped = False
    exit_code = 125
    wait_status: int | None = None
    command_started: float | None = None
    command_reaped: float | None = None
    before: dict[str, Any] | None = None
    after: dict[str, Any] | None = None
    cgroup_evidence: dict[str, Any] = {}
    time_evidence: dict[str, Any] | None = None
    execution_error: str | None = None
    descendants_timed_out = False
    descendants_after_parent = False

    def sampler() -> None:
        while not stop_sampling.is_set():
            try:
                samples.append(host_sample())
            except BaseException:
                monitor_errors.append(traceback.format_exc())
                stop_sampling.set()
                return
            stop_sampling.wait(1.0)

    try:
        lock = lock_path.open("w")
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        cgroup.mkdir()
        if (cgroup / "memory.swap.max").exists():
            (cgroup / "memory.swap.max").write_text("0")
        if (cgroup / "memory.oom.group").exists():
            (cgroup / "memory.oom.group").write_text("1")
        before = host_sample()
        command_started = time.monotonic()
        pid = os.fork()
        if pid == 0:
            try:
                os.chdir(args.cwd)
                (cgroup / "cgroup.procs").write_text(str(os.getpid()))
                stdout_fd = os.open(stdout_path, os.O_WRONLY | os.O_TRUNC)
                stderr_fd = os.open(stderr_path, os.O_WRONLY | os.O_TRUNC)
                os.dup2(stdout_fd, 1)
                os.dup2(stderr_fd, 2)
                environment = os.environ.copy()
                environment["LC_ALL"] = "C"
                time_format = "\n".join(
                    (
                        "user_seconds=%U",
                        "system_seconds=%S",
                        "cpu_percent=%P",
                        "wall_seconds=%e",
                        "maximum_rss_kib=%M",
                        "major_page_faults=%F",
                        "minor_page_faults=%R",
                        "voluntary_context_switches=%w",
                        "involuntary_context_switches=%c",
                        "filesystem_inputs=%I",
                        "filesystem_outputs=%O",
                        "swaps=%W",
                        "exit_status=%x",
                    )
                )
                os.execvpe(
                    "/usr/bin/time",
                    [
                        "/usr/bin/time",
                        "-f",
                        time_format,
                        "-o",
                        str(time_path),
                        "--",
                        *args.command,
                    ],
                    environment,
                )
            except BaseException as error:
                os.write(2, f"runner child failed: {error}\n".encode())
                os._exit(125)

        sampling_thread = threading.Thread(target=sampler, daemon=True)
        sampling_thread.start()
        _, wait_status = os.waitpid(pid, 0)
        reaped = True
        command_reaped = time.monotonic()
        exit_code = os.waitstatus_to_exitcode(wait_status)
        descendants_after_parent = cgroup_populated(cgroup)
        if not wait_cgroup_empty(cgroup, 10.0):
            descendants_timed_out = True
            if (cgroup / "cgroup.kill").exists():
                (cgroup / "cgroup.kill").write_text("1")
            wait_cgroup_empty(cgroup, 5.0)
    except BaseException:
        execution_error = traceback.format_exc()
    finally:
        stop_sampling.set()
        if sampling_thread:
            sampling_thread.join(timeout=5.0)
            if sampling_thread.is_alive():
                monitor_errors.append("sampler thread did not stop")
        if pid is not None and not reaped:
            try:
                if cgroup.exists() and (cgroup / "cgroup.kill").exists():
                    (cgroup / "cgroup.kill").write_text("1")
                os.waitpid(pid, 0)
                reaped = True
            except (ChildProcessError, OSError):
                pass
        if cgroup.exists() and cgroup_populated(cgroup):
            try:
                if (cgroup / "cgroup.kill").exists():
                    (cgroup / "cgroup.kill").write_text("1")
                wait_cgroup_empty(cgroup, 5.0)
            except OSError:
                monitor_errors.append(traceback.format_exc())
        try:
            after = host_sample()
        except BaseException:
            monitor_errors.append(traceback.format_exc())
        if cgroup.exists():
            try:
                cgroup_evidence = {
                    "memory_current_bytes": read_int(cgroup / "memory.current"),
                    "memory_peak_bytes": read_int(cgroup / "memory.peak"),
                    "memory_swap_current_bytes": read_int(cgroup / "memory.swap.current"),
                    "memory_swap_peak_bytes": read_int(cgroup / "memory.swap.peak"),
                    "memory_swap_max": (cgroup / "memory.swap.max").read_text().strip()
                    if (cgroup / "memory.swap.max").exists()
                    else None,
                    "memory_events": read_key_values(cgroup / "memory.events"),
                    "memory_swap_events": read_key_values(cgroup / "memory.swap.events")
                    if (cgroup / "memory.swap.events").exists()
                    else {},
                    "memory_pressure": read_pressure(cgroup / "memory.pressure"),
                    "cgroup_events": read_key_values(cgroup / "cgroup.events"),
                    "remaining_direct_processes": (cgroup / "cgroup.procs").read_text().split(),
                }
            except BaseException:
                monitor_errors.append(traceback.format_exc())
        try:
            time_evidence = parse_time_verbose(time_path)
        except BaseException:
            monitor_errors.append(traceback.format_exc())

    invalid_reasons: list[str] = []
    if execution_error:
        invalid_reasons.append("runner execution error")
    if exit_code != 0:
        invalid_reasons.append(f"command exit code {exit_code}")
    if time_evidence is None:
        invalid_reasons.append("missing or malformed GNU time evidence")
    elif time_evidence["exit_status"] != exit_code:
        invalid_reasons.append("GNU time and wait status disagree")
    if monitor_errors:
        invalid_reasons.append("monitoring failure")
    if descendants_timed_out:
        invalid_reasons.append("process tree did not exit within 10 seconds")
    if descendants_after_parent:
        invalid_reasons.append("process tree outlived the timed parent")
    events = cgroup_evidence.get("memory_events", {})
    if any(events.get(key, 0) for key in ("oom", "oom_kill", "oom_group_kill")):
        invalid_reasons.append("cgroup OOM event")
    if cgroup_evidence.get("cgroup_events", {}).get("populated"):
        invalid_reasons.append("cgroup remained populated")
    if cgroup_evidence.get("memory_swap_max") != "0":
        invalid_reasons.append("cgroup swap maximum was not zero")
    if any(
        (cgroup_evidence.get(key) or 0) != 0
        for key in ("memory_swap_current_bytes", "memory_swap_peak_bytes")
    ):
        invalid_reasons.append("cgroup used swap")
    if before and after:
        if before["swap_total_bytes"] or after["swap_total_bytes"]:
            invalid_reasons.append("host had configured swap")
        if before["active_swap_devices"] or after["active_swap_devices"]:
            invalid_reasons.append("host had active swap devices")
        if before["pswpin"] != after["pswpin"] or before["pswpout"] != after["pswpout"]:
            invalid_reasons.append("host swap counters changed")
    else:
        invalid_reasons.append("missing host boundary samples")
    if not samples:
        invalid_reasons.append("no interval host samples")
    elif any(
        later["monotonic_seconds"] - earlier["monotonic_seconds"] > 2.5
        for earlier, later in zip(samples, samples[1:])
    ):
        invalid_reasons.append("host sampling cadence gap exceeded 2.5 seconds")

    evidence = {
        "schema": "cp10-run",
        "schema_version": SCHEMA_VERSION,
        "id": args.id,
        "series": args.series,
        "scenario": args.scenario,
        "tool": args.tool,
        "round": args.round,
        "warmth": args.warmth,
        "started_at_utc": start_utc,
        "working_directory": str(args.cwd.resolve()),
        "command": args.command,
        "exit_code": exit_code,
        "fork_to_reap_seconds": (
            command_reaped - command_started
            if command_started is not None and command_reaped is not None
            else None
        ),
        "time": time_evidence,
        "cgroup": cgroup_evidence,
        "host_before": before,
        "host_after": after,
        "host_samples": samples,
        "validity": {
            "infrastructure_valid": not invalid_reasons,
            "correctness_verified": False,
            "formal_valid": False,
            "invalid_reasons": invalid_reasons,
            "monitor_errors": monitor_errors,
            "execution_error": execution_error,
        },
        "artifacts": {
            "stdout": artifact_record(stdout_path),
            "stderr": artifact_record(stderr_path),
            "gnu_time": artifact_record(time_path),
        },
    }
    try:
        atomic_json(output, evidence)
    finally:
        if cgroup.exists() and not cgroup_populated(cgroup):
            try:
                cgroup.rmdir()
            except OSError:
                pass
        if lock:
            fcntl.flock(lock, fcntl.LOCK_UN)
            lock.close()
    return exit_code


def metric_summary(values: list[float]) -> dict[str, float]:
    return {
        "median": statistics.median(values),
        "mean": statistics.fmean(values),
        "minimum": min(values),
        "maximum": max(values),
        "population_standard_deviation": statistics.pstdev(values),
    }


def summarize(paths: list[Path], correctness_path: Path) -> dict[str, Any]:
    records = [json.loads(path.read_text()) for path in paths]
    if not records:
        raise ValueError("no run records supplied")
    if any(
        record.get("schema") != "cp10-run"
        or record.get("schema_version") != SCHEMA_VERSION
        for record in records
    ):
        raise ValueError("unsupported run record")
    if any(not record["validity"]["infrastructure_valid"] for record in records):
        raise ValueError("refusing to summarize infrastructure-invalid runs")
    identities = {
        (record["series"], record["scenario"], record["tool"], record["warmth"])
        for record in records
    }
    if len(identities) != 1:
        raise ValueError("summary inputs are not one homogeneous series")
    ids = [record["id"] for record in records]
    rounds = [record["round"] for record in records]
    if len(ids) != len(set(ids)) or len(rounds) != len(set(rounds)):
        raise ValueError("summary has duplicate run ids or rounds")
    correctness = json.loads(correctness_path.read_text())
    comparisons = correctness.get("comparisons", [])
    if (
        correctness.get("schema") != "cp10-correctness"
        or correctness.get("schema_version") != SCHEMA_VERSION
        or correctness.get("passed") is not True
        or sorted(correctness.get("run_ids", [])) != sorted(ids)
        or not correctness.get("checks")
        or any(check.get("passed") is not True for check in correctness["checks"])
        or sorted(item.get("run_id") for item in comparisons) != sorted(ids)
    ):
        raise ValueError("correctness attestation is absent, failed, or mismatched")
    for comparison in comparisons:
        expected_path = correctness_path.parent / comparison["expected_manifest"]
        actual_path = correctness_path.parent / comparison["actual_manifest"]
        expected = load_manifest(expected_path)
        actual = load_manifest(actual_path)
        if (
            expected["entries_sha256"] != comparison.get("expected_entries_sha256")
            or actual["entries_sha256"] != comparison.get("actual_entries_sha256")
            or not comparison.get("output_path")
            or not compare_manifests(expected, actual)["equal_content"]
        ):
            raise ValueError("correctness manifests are mismatched or unequal")
    metrics = {
        "wall_seconds": [float(record["time"]["wall_seconds"]) for record in records],
        "user_seconds": [float(record["time"]["user_seconds"]) for record in records],
        "system_seconds": [float(record["time"]["system_seconds"]) for record in records],
        "cpu_percent": [float(record["time"]["cpu_percent"]) for record in records],
        "gnu_peak_rss_kib": [float(record["time"]["maximum_rss_kib"]) for record in records],
        "cgroup_peak_memory_bytes": [float(record["cgroup"]["memory_peak_bytes"]) for record in records],
    }
    return {
        "schema": "cp10-summary",
        "schema_version": SCHEMA_VERSION,
        "identity": dict(zip(("series", "scenario", "tool", "warmth"), next(iter(identities)))),
        "count": len(records),
        "metrics": {key: metric_summary(values) for key, values in metrics.items()},
        "correctness_attestation": correctness_path.name,
        "observations": [
            {
                "id": record["id"],
                "round": record["round"],
                "wall_seconds": record["time"]["wall_seconds"],
            }
            for record in sorted(records, key=lambda item: item["round"])
        ],
        "runs": ids,
    }


def percentile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (position - lower)


def paired_comparison(nift_path: Path, astro_path: Path) -> dict[str, Any]:
    nift = json.loads(nift_path.read_text())
    astro = json.loads(astro_path.read_text())
    if nift.get("schema") != "cp10-summary" or astro.get("schema") != "cp10-summary":
        raise ValueError("paired comparison requires CP10 summaries")
    if nift["identity"]["tool"] != "nift" or astro["identity"]["tool"] != "astro":
        raise ValueError("paired comparison tool identities are wrong")
    for field in ("series", "scenario", "warmth"):
        if nift["identity"][field] != astro["identity"][field]:
            raise ValueError(f"paired comparison differs in {field}")
    nift_rounds = {item["round"]: item["wall_seconds"] for item in nift["observations"]}
    astro_rounds = {item["round"]: item["wall_seconds"] for item in astro["observations"]}
    if nift_rounds.keys() != astro_rounds.keys() or not nift_rounds:
        raise ValueError("paired comparison rounds do not match")
    rounds = sorted(nift_rounds)
    ratios = [astro_rounds[index] / nift_rounds[index] for index in rounds]
    rng = random.Random(20261001)
    bootstrap: list[float] = []
    for _ in range(10_000):
        sample = [rng.randrange(len(rounds)) for _ in rounds]
        sample_nift = [nift_rounds[rounds[index]] for index in sample]
        sample_astro = [astro_rounds[rounds[index]] for index in sample]
        bootstrap.append(statistics.median(sample_astro) / statistics.median(sample_nift))
    lower = percentile(bootstrap, 0.025)
    upper = percentile(bootstrap, 0.975)
    return {
        "schema": "cp10-paired-comparison",
        "schema_version": SCHEMA_VERSION,
        "ratio_direction": "astro_wall_seconds / nift_wall_seconds",
        "rounds": rounds,
        "per_round_ratios": ratios,
        "ratio_of_medians": statistics.median(astro_rounds.values())
        / statistics.median(nift_rounds.values()),
        "paired_ratio_summary": metric_summary(ratios),
        "bootstrap": {
            "resamples": 10000,
            "seed": 20261001,
            "statistic": "ratio of paired-resample medians",
            "confidence_level": 0.95,
            "lower": lower,
            "upper": upper,
            "crosses_parity": lower <= 1.0 <= upper,
        },
        "nift_summary": nift_path.name,
        "astro_summary": astro_path.name,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="action", required=True)

    manifest = subparsers.add_parser("manifest")
    manifest.add_argument("root", type=Path)
    manifest.add_argument("output", type=Path)

    compare = subparsers.add_parser("compare")
    compare.add_argument("before", type=Path)
    compare.add_argument("after", type=Path)
    compare.add_argument("output", type=Path)

    run = subparsers.add_parser("run")
    run.add_argument("--id", required=True)
    run.add_argument("--series", required=True)
    run.add_argument("--scenario", required=True)
    run.add_argument("--tool", choices=("nift", "astro", "setup"), required=True)
    run.add_argument("--round", type=int, required=True)
    run.add_argument("--warmth", choices=("warm", "guest-page-cache-dropped", "setup"), required=True)
    run.add_argument("--output", type=Path, required=True)
    run.add_argument("--cwd", type=Path, required=True)
    run.add_argument("command", nargs=argparse.REMAINDER)

    summary = subparsers.add_parser("summarize")
    summary.add_argument("output", type=Path)
    summary.add_argument("--correctness", required=True, type=Path)
    summary.add_argument("runs", nargs="+", type=Path)

    paired = subparsers.add_parser("paired")
    paired.add_argument("nift_summary", type=Path)
    paired.add_argument("astro_summary", type=Path)
    paired.add_argument("output", type=Path)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.action == "manifest":
        atomic_json(args.output, manifest_payload(args.root))
        return 0
    if args.action == "compare":
        payload = compare_manifests(
            load_manifest(args.before), load_manifest(args.after)
        )
        atomic_json(args.output, payload)
        return 0 if payload["equal_content"] else 1
    if args.action == "summarize":
        atomic_json(args.output, summarize(args.runs, args.correctness))
        return 0
    if args.action == "paired":
        atomic_json(
            args.output, paired_comparison(args.nift_summary, args.astro_summary)
        )
        return 0
    if not args.command:
        raise ValueError("run requires a command after --")
    if args.command[0] == "--":
        args.command = args.command[1:]
    if not args.command:
        raise ValueError("run requires a non-empty command")
    return execute_run(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (BlockingIOError, FileExistsError, PermissionError, RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
