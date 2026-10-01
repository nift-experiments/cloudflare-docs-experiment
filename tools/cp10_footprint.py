#!/usr/bin/env python3
"""Collect deterministic CP10 checkout, dependency, and output footprints."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = 1
NIFT_SOURCE_EXCLUSIONS = (".git", ".nift", "node_modules", "public")
ASTRO_SOURCE_EXCLUSIONS = (".astro", ".git", "dist", "node_modules")


def _empty_footprint(path: Path, exclusions: Iterable[str]) -> dict[str, Any]:
    return {
        "path": str(path),
        "present": False,
        "exclusions": sorted(exclusions),
        "logical_bytes": 0,
        "allocated_bytes": 0,
        "regular_file_count": 0,
        "directory_count": 0,
        "symlink_count": 0,
        "other_count": 0,
        "unique_inode_count": 0,
        "duplicate_hardlink_count": 0,
    }


def measure_tree(root: Path, exclusions: Iterable[str] = ()) -> dict[str, Any]:
    """Measure root using lstat, without traversing links or repeated inodes."""
    root = root.absolute()
    excluded = frozenset(exclusions)
    result = _empty_footprint(root, excluded)
    try:
        root.lstat()
    except FileNotFoundError:
        return result

    result["present"] = True
    seen: set[tuple[int, int]] = set()

    def visit(path: Path, relative: str | None) -> None:
        if relative is not None and relative in excluded:
            return
        metadata = path.lstat()
        identity = (metadata.st_dev, metadata.st_ino)
        if identity in seen:
            result["duplicate_hardlink_count"] += 1
            return
        seen.add(identity)
        result["logical_bytes"] += metadata.st_size
        result["allocated_bytes"] += metadata.st_blocks * 512
        result["unique_inode_count"] += 1

        mode = metadata.st_mode
        if stat.S_ISREG(mode):
            result["regular_file_count"] += 1
        elif stat.S_ISDIR(mode):
            result["directory_count"] += 1
            try:
                children = sorted(
                    path.iterdir(), key=lambda item: os.fsencode(item.name)
                )
            except OSError as error:
                raise OSError(
                    f"cannot list measured directory {path}: {error}"
                ) from error
            for child in children:
                child_relative = (
                    child.name if relative is None else f"{relative}/{child.name}"
                )
                visit(child, child_relative)
        elif stat.S_ISLNK(mode):
            result["symlink_count"] += 1
        else:
            result["other_count"] += 1

    visit(root, None)
    return result


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def binary_evidence(path: Path) -> dict[str, Any]:
    invocation = path.absolute()
    invocation_lstat = measure_tree(invocation)
    resolved = invocation.resolve(strict=True)
    metadata = resolved.stat()
    if not stat.S_ISREG(metadata.st_mode):
        raise ValueError(f"Nift binary is not a regular file: {resolved}")
    return {
        "invocation_path": str(invocation),
        "invocation_path_lstat": invocation_lstat,
        "resolved_path": str(resolved),
        "resolved_file_stat": {
            "logical_bytes": metadata.st_size,
            "allocated_bytes": metadata.st_blocks * 512,
            "sha256": _sha256(resolved),
        },
    }


def _mapping_key(line: str) -> bool:
    if not line or line[0] in "-?:&*!|>{[":
        return False
    quote: str | None = None
    escaped = False
    for index, character in enumerate(line):
        if escaped:
            escaped = False
            continue
        if quote == '"' and character == "\\":
            escaped = True
            continue
        if character in {"'", '"'}:
            if quote is None:
                quote = character
            elif quote == character:
                quote = None
            continue
        if character == ":" and quote is None:
            following = line[index + 1 :]
            return bool(line[:index].strip()) and (
                not following or following[0].isspace() or following.startswith("#")
            )
    return False


def yaml_top_level_mapping_count(text: str, section: str) -> int | None:
    """Count direct mapping keys in one simple top-level YAML section."""
    lines = text.splitlines()
    header_pattern = re.compile(rf"^{re.escape(section)}:\s*(?:#.*)?$")
    inline_empty_pattern = re.compile(
        rf"^{re.escape(section)}:\s*\{{\s*\}}\s*(?:#.*)?$"
    )
    headers = [
        index for index, line in enumerate(lines) if header_pattern.fullmatch(line)
    ]
    empty_headers = [
        index for index, line in enumerate(lines) if inline_empty_pattern.fullmatch(line)
    ]
    if len(headers) + len(empty_headers) != 1:
        return None
    if empty_headers:
        return 0

    body: list[str] = []
    for line in lines[headers[0] + 1 :]:
        if line and not line[0].isspace():
            break
        if line.strip() and not line.lstrip().startswith("#"):
            body.append(line)
    if not body or any(
        "\t" in line[: len(line) - len(line.lstrip())] for line in body
    ):
        return 0 if not body else None
    indentation = min(len(line) - len(line.lstrip(" ")) for line in body)
    if indentation <= 0:
        return None
    direct = [
        line[indentation:]
        for line in body
        if line.startswith(" " * indentation)
        and not line.startswith(" " * (indentation + 1))
    ]
    if not direct or any(not _mapping_key(line) for line in direct):
        return None
    return len(direct)


def lockfile_snapshot_evidence(path: Path) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    for section in ("snapshots", "packages"):
        if not re.search(rf"^{section}:", text, re.MULTILINE):
            continue
        count = yaml_top_level_mapping_count(text, section)
        if count is None:
            return None
        return {
            "path": str(path.absolute()),
            "count": count,
            "source_section": section,
            "definition": (
                f"direct mapping entries in the top-level {section!r} section"
            ),
        }
    return None


def pnpm_store_entries(path: Path) -> dict[str, Any]:
    path = path.absolute()
    try:
        root_metadata = path.lstat()
    except FileNotFoundError:
        root_metadata = None
    if root_metadata is None or not stat.S_ISDIR(root_metadata.st_mode):
        return {
            "path": str(path),
            "present": False,
            "count": 0,
            "definition": (
                "immediate real directories except the pnpm linking directory "
                "named node_modules"
            ),
        }
    count = 0
    for child in sorted(path.iterdir(), key=lambda item: os.fsencode(item.name)):
        metadata = child.lstat()
        if child.name != "node_modules" and stat.S_ISDIR(metadata.st_mode):
            count += 1
    return {
        "path": str(path),
        "present": True,
        "count": count,
        "definition": (
            "immediate real directories except the pnpm linking directory named "
            "node_modules"
        ),
    }


def package_evidence(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    result: dict[str, Any] = {"path": str(path.absolute())}
    for key in ("dependencies", "devDependencies"):
        value = payload.get(key, {})
        if not isinstance(value, dict) or any(
            not isinstance(name, str) for name in value
        ):
            raise ValueError(f"package.json {key} must be an object")
        result[key] = {
            "count": len(value),
            "definition": f"number of direct keys in package.json {key}",
        }
    result["declared_versions"] = {
        "astro": payload.get("dependencies", {}).get("astro")
        or payload.get("devDependencies", {}).get("astro"),
        "package_manager": payload.get("packageManager"),
    }
    return result


def _version(command: list[str], cwd: Path | None = None) -> str | None:
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=10,
            env=os.environ | {"LC_ALL": "C"},
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    output = completed.stdout.strip()
    return output if completed.returncode == 0 and output else None


def git_head(project: Path) -> str | None:
    value = _version(["git", "rev-parse", "HEAD"], cwd=project)
    return value if value and re.fullmatch(r"[0-9a-fA-F]{40,64}", value) else None


def collect(
    nift_project: Path, astro_project: Path, nift_bin: Path
) -> dict[str, Any]:
    nift_project = nift_project.resolve(strict=True)
    astro_project = astro_project.resolve(strict=True)
    if not nift_project.is_dir() or not astro_project.is_dir():
        raise ValueError("Nift and Astro project paths must be directories")

    package_path = astro_project / "package.json"
    if not package_path.is_file():
        raise FileNotFoundError(f"Astro package.json is absent: {package_path}")
    lockfile = lockfile_snapshot_evidence(astro_project / "pnpm-lock.yaml")
    node_modules = astro_project / "node_modules"
    nift_node_modules = nift_project / "node_modules"

    payload: dict[str, Any] = {
        "schema": "cp10-footprint",
        "schema_version": SCHEMA_VERSION,
        "definitions": {
            "traversal": (
                "sorted recursive lstat; roots are included; symlinks are counted "
                "but never followed"
            ),
            "logical_bytes": (
                "sum of lstat st_size for unique filesystem object identities"
            ),
            "allocated_bytes": (
                "sum of lstat st_blocks multiplied by 512 for unique filesystem "
                "object identities"
            ),
            "counts": (
                "counts of unique (st_dev, st_ino) identities by lstat type; "
                "other_count covers non-file, non-directory, non-symlink objects"
            ),
            "hardlinks": (
                "an identity is counted once per footprint; "
                "duplicate_hardlink_count records later directory entries"
            ),
            "exclusions": (
                "root-relative paths omitted with their complete subtrees; each "
                "footprint lists its exact exclusions"
            ),
            "absence": (
                "absent footprints have present=false and zero byte and object "
                "counts"
            ),
        },
        "source_heads": {
            "nift": git_head(nift_project),
            "astro": git_head(astro_project),
        },
        "versions": {
            "python": sys.version.split()[0],
            "nift": _version([str(nift_bin.absolute()), "--version"]),
            "node": _version(["node", "--version"]),
            "pnpm": _version(["pnpm", "--version"], cwd=astro_project),
        },
        "nift_binary": binary_evidence(nift_bin),
        "package_json": package_evidence(package_path),
        "pnpm_resolved_store_entries": pnpm_store_entries(node_modules / ".pnpm"),
        "nift_node_modules": {
            "path": str(nift_node_modules),
            "present": nift_node_modules.exists() or nift_node_modules.is_symlink(),
        },
        "footprints": {
            "astro_node_modules_excluding_dot_astro": measure_tree(
                node_modules, (".astro",)
            ),
            "astro_node_modules_dot_astro": measure_tree(node_modules / ".astro"),
            "astro_dist": measure_tree(astro_project / "dist"),
            "nift_public": measure_tree(nift_project / "public"),
            "nift_dot_nift_metadata": measure_tree(nift_project / ".nift"),
            "nift_source_checkout": measure_tree(
                nift_project, NIFT_SOURCE_EXCLUSIONS
            ),
            "astro_source_checkout": measure_tree(
                astro_project, ASTRO_SOURCE_EXCLUSIONS
            ),
        },
    }
    if nift_node_modules.exists() or nift_node_modules.is_symlink():
        payload["nift_node_modules"]["footprint"] = measure_tree(nift_node_modules)
    if lockfile is not None:
        payload["lockfile_package_snapshots"] = lockfile
    return payload


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nift-project", required=True, type=Path)
    parser.add_argument("--astro-project", required=True, type=Path)
    parser.add_argument("--nift-bin", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    payload = collect(args.nift_project, args.astro_project, args.nift_bin)
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True, ensure_ascii=True)
        handle.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
