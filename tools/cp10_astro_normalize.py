#!/usr/bin/env python3
"""Classify and narrowly normalize proven CP10 Astro output variance."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Callable


SCHEMA_VERSION = 1
UUID_RE = re.compile(
    rb"pm-[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
)
COMBOBOX_RE = re.compile(rb"nb-combobox-[0-9a-f]{8}")
CHECKBOX_RE = re.compile(rb"cb-[a-z0-9]{8}")
PLAYGROUND_RE = re.compile(
    rb"https://workers\.cloudflare\.com/playground#([A-Za-z0-9+\-$]+)"
)
SHIKI_RULE_RE = re.compile(rb"\.nb-shiki-[a-z0-9]+\{[^{}]*\}")
SVG_ASSET_RE = re.compile(r"^_astro/[^/]+\.([A-Za-z0-9_-]{8})\.svg$")
SITEMAP_ROOT_RE = re.compile(
    rb"<url><loc>https://developers\.cloudflare\.com/</loc>"
    rb"<lastmod>([^<]+)</lastmod></url>"
)
FORMDATA_BOUNDARY_RE = re.compile(rb"----formdata-undici-[0-9]{12}")


def atomic_output(path: Path, payload: dict[str, Any]) -> None:
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

# Frozen source: src/components/agent-setup/prompts.ts. Normalization is limited
# to these exact strings and the nine agent-setup output routes.
AGENT_PROMPTS = (
    "Build an AI chat agent using the Cloudflare Agents SDK with persistent conversation history stored in D1.",
    "Create a RAG pipeline using Vectorize and Workers AI to answer questions over my documentation.",
    "Set up AI Gateway to route requests across OpenAI and Workers AI with automatic fallback and cost tracking.",
    "Build a serverless AI inference endpoint on Workers AI with streaming responses.",
    "Deploy a full-stack React app to Cloudflare Pages with a Workers API backend and D1 database.",
    "Add a D1 database to my Worker and create a users table with full CRUD endpoints.",
    "Build an image upload and transformation service using R2 and Cloudflare Images.",
    "Add real-time collaboration to my app using Durable Objects with WebSocket hibernation.",
    "Set up a KV namespace for edge-cached session storage in my Worker.",
    "Add a cron trigger to my Worker that processes a job queue every hour.",
    "Deploy a globally distributed REST API on Workers with automatic scaling and zero cold starts.",
    "Connect my Worker to an existing Postgres database using Hyperdrive for connection pooling.",
    "Add mTLS authentication and schema validation to protect my API endpoints.",
    "Set up rate limiting and WAF rules to block abuse on my public API.",
    "Build a multi-tenant SaaS backend where each customer gets an isolated D1 database.",
    "Set up custom domains with automatic SSL for my SaaS customers using SSL for SaaS.",
    "Use Workers for Platforms to let my customers deploy their own code in isolated environments.",
    "Add bot protection and rate limiting to my login and checkout endpoints.",
    "Set up WAF rules to block SQL injection and XSS attacks on my application.",
    "Configure Zero Trust access policies to protect my internal staging environment.",
    "Configure caching rules and cache TTLs to reduce origin load for my e-commerce store.",
    "Set up a Waiting Room to handle flash sale traffic spikes without dropping requests.",
    "Optimize my Worker to serve WebP images with responsive resizing using Cloudflare Images.",
    "Check my Workers deployment logs for errors and suggest fixes.",
    "Set up GitHub Actions to deploy this Worker to staging and production on Cloudflare.",
    "Create a Logpush job to stream Workers analytics to my data warehouse.",
)
AGENT_ROUTES = {
    f"agent-setup/{name}/index.html"
    for name in (
        "bionic",
        "claude-code",
        "codex",
        "command-code",
        "cursor",
        "github-copilot",
        "opencode",
        "visual-studio-code",
        "windsurf",
    )
}


class NormalizationError(ValueError):
    """An apparent nondeterministic value failed its narrow contract."""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_digest(entries: list[dict[str, Any]]) -> str:
    data = json.dumps(
        entries, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    return sha256_bytes(data)


def parse_labeled_path(value: str) -> tuple[str, Path]:
    label, separator, raw_path = value.partition("=")
    if not separator or not label or not raw_path:
        raise argparse.ArgumentTypeError("expected LABEL=PATH")
    return label, Path(raw_path)


def inventory(root: Path) -> tuple[list[dict[str, Any]], dict[str, Path]]:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f"output root is not a directory: {root}")
    entries: list[dict[str, Any]] = []
    files: dict[str, Path] = {}
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
            if path.is_symlink():
                entry.update(type="symlink", target=os.readlink(path))
                if name in dirnames:
                    dirnames.remove(name)
            elif stat.S_ISDIR(item_stat.st_mode):
                entry["type"] = "directory"
            elif stat.S_ISREG(item_stat.st_mode):
                digest = hashlib.sha256()
                size = 0
                with path.open("rb") as handle:
                    while chunk := handle.read(1024 * 1024):
                        digest.update(chunk)
                        size += len(chunk)
                entry.update(type="file", size=size, sha256=digest.hexdigest())
                files[relative] = path
            else:
                raise ValueError(f"unsupported filesystem object: {path}")
            entries.append(entry)
    entries.sort(key=lambda item: item["path"])
    return entries, files


def raw_manifest(entries: list[dict[str, Any]], root: Path) -> dict[str, Any]:
    files = [entry for entry in entries if entry["type"] == "file"]
    return {
        "schema": "cp10-tree-manifest",
        "schema_version": 1,
        "root_label": root.name,
        "entries_sha256": canonical_digest(entries),
        "summary": {
            "entries": len(entries),
            "files": len(files),
            "bytes": sum(entry["size"] for entry in files),
        },
    }


def sequential_tokens(data: bytes, pattern: re.Pattern[bytes], prefix: bytes) -> bytes:
    seen: dict[bytes, bytes] = {}

    def replacement(match: re.Match[bytes]) -> bytes:
        token = match.group()
        if token not in seen:
            seen[token] = prefix + b"-%06d" % len(seen)
        return seen[token]

    return pattern.sub(replacement, data)


def _read_lz_bits(
    count: int, state: list[int], reset_value: int, get_value: Callable[[int], int]
) -> int:
    result = 0
    power = 1
    for _ in range(count):
        bit = state[0] & state[1]
        state[1] >>= 1
        if state[1] == 0:
            state[1] = reset_value
            state[0] = get_value(state[2])
            state[2] += 1
        if bit:
            result |= power
        power <<= 1
    return result


def lz_decompress_uri(value: bytes) -> bytes:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-$"
    try:
        encoded = value.decode("ascii").replace(" ", "+")
        values = [alphabet.index(character) for character in encoded]
    except (UnicodeDecodeError, ValueError) as error:
        raise NormalizationError("invalid lz-string URI alphabet") from error
    if not values:
        raise NormalizationError("empty playground fragment")
    state = [values[0], 32, 1]
    dictionary: dict[int, str] = {0: "", 1: "", 2: ""}
    next_code = _read_lz_bits(2, state, 32, values.__getitem__)
    if next_code == 0:
        first = chr(_read_lz_bits(8, state, 32, values.__getitem__))
    elif next_code == 1:
        first = chr(_read_lz_bits(16, state, 32, values.__getitem__))
    else:
        raise NormalizationError("playground fragment terminates before content")
    dictionary[3] = first
    result = [first]
    previous = first
    dictionary_size = 4
    number_bits = 3
    enlarge_in = 4
    while True:
        if state[2] > len(values):
            raise NormalizationError("truncated playground fragment")
        code = _read_lz_bits(number_bits, state, 32, values.__getitem__)
        if code == 0:
            dictionary[dictionary_size] = chr(
                _read_lz_bits(8, state, 32, values.__getitem__)
            )
            code = dictionary_size
            dictionary_size += 1
            enlarge_in -= 1
        elif code == 1:
            dictionary[dictionary_size] = chr(
                _read_lz_bits(16, state, 32, values.__getitem__)
            )
            code = dictionary_size
            dictionary_size += 1
            enlarge_in -= 1
        elif code == 2:
            try:
                return "".join(result).encode("utf-8")
            except UnicodeEncodeError as error:
                raise NormalizationError("playground payload is not UTF-8 text") from error
        if enlarge_in == 0:
            enlarge_in = 1 << number_bits
            number_bits += 1
        if code in dictionary:
            entry = dictionary[code]
        elif code == dictionary_size:
            entry = previous + previous[0]
        else:
            raise NormalizationError("invalid playground compression dictionary")
        result.append(entry)
        dictionary[dictionary_size] = previous + entry[0]
        dictionary_size += 1
        enlarge_in -= 1
        previous = entry
        if enlarge_in == 0:
            enlarge_in = 1 << number_bits
            number_bits += 1


def normalize_playground_links(data: bytes) -> bytes:
    def replacement(match: re.Match[bytes]) -> bytes:
        decoded = lz_decompress_uri(match.group(1))
        boundaries = set(FORMDATA_BOUNDARY_RE.findall(decoded))
        if len(boundaries) != 1:
            raise NormalizationError(
                "playground multipart payload does not have one Undici boundary"
            )
        boundary = next(iter(boundaries))
        expected_prefix = b"multipart/form-data; boundary=" + boundary + b":"
        closing = b"--" + boundary + b"--"
        if not decoded.startswith(expected_prefix) or not decoded.rstrip(b"\r\n").endswith(
            closing
        ):
            raise NormalizationError("playground multipart framing is malformed")
        canonical = decoded.replace(boundary, b"<UNDICI-MULTIPART-BOUNDARY>")
        return (
            b"https://workers.cloudflare.com/playground#cp10-sha256-"
            + sha256_bytes(canonical).encode()
        )

    return PLAYGROUND_RE.sub(replacement, data)


def discover_svg_aliases(
    metadata: dict[str, dict[str, dict[str, Any]]]
) -> tuple[dict[str, str], list[dict[str, Any]]]:
    by_hash: dict[str, set[str]] = defaultdict(set)
    for entries in metadata.values():
        for path, entry in entries.items():
            if entry["type"] == "file" and SVG_ASSET_RE.match(path):
                by_hash[entry["sha256"]].add(path)
    aliases: dict[str, str] = {}
    evidence: list[dict[str, Any]] = []
    for digest, paths in sorted(by_hash.items()):
        if len(paths) < 2:
            continue
        suffixes = {SVG_ASSET_RE.match(path).group(1) for path in paths}  # type: ignore[union-attr]
        presence = [sorted(paths & entries.keys()) for entries in metadata.values()]
        if len(suffixes) != 1 or any(len(items) != 1 for items in presence):
            continue
        canonical = f"_astro/cp10-content-{digest[:16]}.{next(iter(suffixes))}.svg"
        for path in paths:
            aliases[path] = canonical
        evidence.append(
            {
                "sha256": digest,
                "paths": sorted(paths),
                "canonical_path": canonical,
                "one_path_per_run": presence,
            }
        )
    return aliases, evidence


def normalize_content(
    path: str, data: bytes, aliases: dict[str, str]
) -> tuple[bytes, list[str]]:
    categories: list[str] = []
    transforms: tuple[tuple[str, Callable[[bytes], bytes]], ...] = (
        (
            "package-manager-uuid",
            lambda value: sequential_tokens(value, UUID_RE, b"pm-cp10"),
        ),
        (
            "combobox-random-id",
            lambda value: sequential_tokens(value, COMBOBOX_RE, b"nb-combobox-cp10"),
        ),
        (
            "checkbox-random-id",
            lambda value: sequential_tokens(value, CHECKBOX_RE, b"cb-cp10"),
        ),
        ("playground-multipart-boundary", normalize_playground_links),
    )
    for category, transform in transforms:
        changed = transform(data)
        if changed != data:
            categories.append(category)
            data = changed

    if path in AGENT_ROUTES:
        changed = data
        for prompt in AGENT_PROMPTS:
            changed = changed.replace(prompt.encode(), b"<CP10-RANDOM-AGENT-PROMPT>")
        if changed != data:
            categories.append("sampled-agent-prompts")
            data = changed

    if path == "_nimbus/shiki.css":
        rules = SHIKI_RULE_RE.findall(data)
        if len(rules) < 2 or b"".join(rules) + b"\n" != data:
            raise NormalizationError("Shiki stylesheet contains unexpected syntax")
        changed = b"".join(sorted(rules)) + b"\n"
        if changed != data:
            categories.append("shiki-rule-order")
            data = changed

    if path == "sitemap-0.xml":
        matches = SITEMAP_ROOT_RE.findall(data)
        if len(matches) != 1:
            raise NormalizationError("sitemap has no unique root fallback lastmod")
        timestamp = matches[0]
        changed = data.replace(timestamp, b"<CP10-BUILD-FALLBACK-LASTMOD>")
        if changed != data:
            categories.append("sitemap-build-time-fallback")
            data = changed

    changed = data
    for original, canonical in aliases.items():
        changed = changed.replace(original.encode(), canonical.encode())
        changed = changed.replace(
            Path(original).name.encode(), Path(canonical).name.encode()
        )
    if changed != data:
        categories.append("content-identical-svg-alias")
        data = changed
    return data, categories


def compare_raw(
    before: dict[str, dict[str, Any]], after: dict[str, dict[str, Any]]
) -> dict[str, list[str]]:
    before_paths = set(before)
    after_paths = set(after)
    return {
        "added": sorted(after_paths - before_paths),
        "removed": sorted(before_paths - after_paths),
        "changed": sorted(
            path
            for path in before_paths & after_paths
            if before[path]["type"] != after[path]["type"]
            or before[path].get("size") != after[path].get("size")
            or before[path].get("sha256") != after[path].get("sha256")
            or before[path].get("target") != after[path].get("target")
        ),
    }


def analyze(roots: list[tuple[str, Path]]) -> dict[str, Any]:
    if len(roots) < 2 or len({label for label, _ in roots}) != len(roots):
        raise ValueError("at least two roots with unique labels are required")
    raw_entries: dict[str, list[dict[str, Any]]] = {}
    file_paths: dict[str, dict[str, Path]] = {}
    metadata: dict[str, dict[str, dict[str, Any]]] = {}
    manifests: dict[str, dict[str, Any]] = {}
    for label, root in roots:
        entries, files = inventory(root)
        raw_entries[label] = entries
        file_paths[label] = files
        metadata[label] = {entry["path"]: entry for entry in entries}
        manifests[label] = raw_manifest(entries, root)

    aliases, alias_evidence = discover_svg_aliases(metadata)
    differing_paths: set[str] = set(aliases)
    labels = [label for label, _ in roots]
    for index, label in enumerate(labels):
        for other in labels[index + 1 :]:
            difference = compare_raw(metadata[label], metadata[other])
            differing_paths.update(difference["added"])
            differing_paths.update(difference["removed"])
            differing_paths.update(difference["changed"])

    normalized_entries: dict[str, list[dict[str, Any]]] = {}
    categories_by_run: dict[str, dict[str, list[str]]] = {}
    errors: list[dict[str, str]] = []
    for label in labels:
        normalized: dict[str, dict[str, Any]] = {}
        path_categories: dict[str, list[str]] = {}
        for entry in raw_entries[label]:
            path = entry["path"]
            normalized_path = aliases.get(path, path)
            if entry["type"] == "file":
                if path in differing_paths:
                    try:
                        data, categories = normalize_content(
                            path, file_paths[label][path].read_bytes(), aliases
                        )
                    except NormalizationError as error:
                        errors.append({"run": label, "path": path, "error": str(error)})
                        data = file_paths[label][path].read_bytes()
                        categories = []
                    item = {
                        "path": normalized_path,
                        "type": "file",
                        "size": len(data),
                        "sha256": sha256_bytes(data),
                    }
                    if normalized_path != path:
                        categories = sorted(
                            {*categories, "content-identical-svg-alias"}
                        )
                    if categories:
                        path_categories[path] = categories
                else:
                    item = {
                        "path": normalized_path,
                        "type": "file",
                        "size": entry["size"],
                        "sha256": entry["sha256"],
                    }
            elif entry["type"] == "symlink":
                item = {
                    "path": normalized_path,
                    "type": "symlink",
                    "target": entry["target"],
                }
            else:
                item = {"path": normalized_path, "type": "directory"}
            previous = normalized.get(normalized_path)
            if previous is not None and previous != item:
                errors.append(
                    {
                        "run": label,
                        "path": path,
                        "error": f"normalization collides at {normalized_path}",
                    }
                )
            normalized[normalized_path] = item
        normalized_entries[label] = sorted(
            normalized.values(), key=lambda item: item["path"]
        )
        categories_by_run[label] = path_categories

    comparisons = []
    all_categories: dict[str, set[str]] = defaultdict(set)
    all_unclassified: set[str] = set()
    for index, before_label in enumerate(labels):
        for after_label in labels[index + 1 :]:
            raw = compare_raw(metadata[before_label], metadata[after_label])
            before_normalized = {
                entry["path"]: entry for entry in normalized_entries[before_label]
            }
            after_normalized = {
                entry["path"]: entry for entry in normalized_entries[after_label]
            }
            normalized = compare_raw(before_normalized, after_normalized)
            raw_paths = set(raw["added"] + raw["removed"] + raw["changed"])
            category_paths: dict[str, set[str]] = defaultdict(set)
            for path in raw_paths:
                for category in categories_by_run[before_label].get(path, []):
                    category_paths[category].add(path)
                for category in categories_by_run[after_label].get(path, []):
                    category_paths[category].add(path)
            for evidence in alias_evidence:
                evidence_paths = set(evidence["paths"])
                if raw_paths & evidence_paths:
                    category_paths["content-identical-svg-alias"].update(
                        raw_paths & evidence_paths
                    )
            unclassified = sorted(
                set(normalized["added"])
                | set(normalized["removed"])
                | set(normalized["changed"])
            )
            all_unclassified.update(unclassified)
            for category, paths in category_paths.items():
                all_categories[category].update(paths)
            comparisons.append(
                {
                    "before": before_label,
                    "after": after_label,
                    "raw": raw | {"counts": {key: len(value) for key, value in raw.items()}},
                    "categories": {
                        category: {"count": len(paths), "paths": sorted(paths)}
                        for category, paths in sorted(category_paths.items())
                    },
                    "normalized": normalized
                    | {
                        "counts": {
                            key: len(value) for key, value in normalized.items()
                        },
                        "equal": not any(normalized.values()),
                    },
                    "unclassified": unclassified,
                }
            )

    normalized_manifests = {}
    for label, entries in normalized_entries.items():
        files = [entry for entry in entries if entry["type"] == "file"]
        normalized_manifests[label] = {
            "entries_sha256": canonical_digest(entries),
            "summary": {
                "entries": len(entries),
                "files": len(files),
                "bytes": sum(entry["size"] for entry in files),
            },
        }
    equivalent = (
        not errors
        and not all_unclassified
        and len(
            {
                manifest["entries_sha256"]
                for manifest in normalized_manifests.values()
            }
        )
        == 1
    )
    return {
        "schema": "cp10-astro-normalization-report",
        "schema_version": SCHEMA_VERSION,
        "runs": {
            label: {
                "root": str(root.resolve()),
                "raw_manifest": manifests[label],
                "normalized_manifest": normalized_manifests[label],
            }
            for label, root in roots
        },
        "comparisons": comparisons,
        "category_totals": {
            category: {"count": len(paths), "paths": sorted(paths)}
            for category, paths in sorted(all_categories.items())
        },
        "svg_alias_evidence": alias_evidence,
        "rejected": errors,
        "unclassified": sorted(all_unclassified),
        "normalized_equivalent": equivalent,
        "provenance": {
            "package-manager-uuid": "src/components/ui/package-managers/PackageManagers.astro:22",
            "combobox-random-id": "src/components/ui/combobox/Combobox.astro:79",
            "checkbox-random-id": "src/components/ui/checkbox/Checkbox.astro:48",
            "playground-multipart-boundary": "src/components/cf/TypeScriptExample.astro:65-82 (Undici FormData boundary)",
            "sampled-agent-prompts": "src/components/agent-setup/{ExamplePrompts,RandomPrompt}.astro and prompts.ts",
            "shiki-rule-order": "@cloudflare/nimbus-docs 0.14.1 code-style-registry and normalizeShikiCSS insertion order",
            "sitemap-build-time-fallback": "sitemap.serializer.ts:95-122",
            "content-identical-svg-alias": "cross-run identical SHA-256 plus mutually exclusive Vite hashed SVG paths",
        },
    }


def validate_manifests(
    report: dict[str, Any], manifest_paths: list[tuple[str, Path]]
) -> None:
    supplied = dict(manifest_paths)
    if set(supplied) != set(report["runs"]):
        raise ValueError("manifest labels must exactly match root labels")
    for label, path in supplied.items():
        expected = json.loads(path.read_text())
        actual = report["runs"][label]["raw_manifest"]
        if expected.get("entries_sha256") != actual["entries_sha256"]:
            raise ValueError(f"raw manifest digest mismatch for {label}: {path}")
        if expected.get("summary") != actual["summary"]:
            raise ValueError(f"raw manifest summary mismatch for {label}: {path}")
        report["runs"][label]["raw_manifest_validation"] = str(path)


def run_remote(args: argparse.Namespace) -> dict[str, Any]:
    command = [sys.executable, "-"]
    for label, root in args.root:
        command.extend(("--root", f"{label}={root}"))
    source = Path(__file__).read_bytes()
    completed = subprocess.run(
        ["ssh", args.ssh, *command],
        input=source,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode not in (0, 1):
        raise RuntimeError(
            f"remote analysis failed ({completed.returncode}): "
            f"{completed.stderr.decode(errors='replace')}"
        )
    try:
        return json.loads(completed.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError("remote analysis did not return JSON") from error


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", action="append", required=True, type=parse_labeled_path)
    parser.add_argument("--manifest", action="append", default=[], type=parse_labeled_path)
    parser.add_argument("--ssh", help="run the read-only scanner on HOST over SSH")
    parser.add_argument("--output", type=Path, help="write JSON here instead of stdout")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report = run_remote(args) if args.ssh else analyze(args.root)
    if args.manifest:
        validate_manifests(report, args.manifest)
    if args.output:
        atomic_output(args.output, report)
    else:
        sys.stdout.write(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return 0 if report["normalized_equivalent"] else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
