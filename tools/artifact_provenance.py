#!/usr/bin/env python3
"""Create a stable identity for the exact candidate public tree."""
import argparse
import datetime
import hashlib
import json
import subprocess
from pathlib import Path


def tree_digest(root):
    files = sorted(path for path in root.rglob('*') if path.is_file())
    digest = hashlib.sha256()
    for path in files:
        relative = path.relative_to(root).as_posix().encode()
        digest.update(len(relative).to_bytes(8, 'big'))
        digest.update(relative)
        content = path.read_bytes()
        digest.update(len(content).to_bytes(8, 'big'))
        digest.update(content)
    return digest.hexdigest(), len(files)


def git_head(worktree):
    return subprocess.check_output(
        ['git', '-C', str(worktree), 'rev-parse', 'HEAD'], text=True).strip()


def require_clean(worktree):
    changes = subprocess.check_output(
        ['git', '-C', str(worktree), 'status', '--porcelain'], text=True).strip()
    if changes:
        raise RuntimeError(f'{worktree}: provenance requires a clean source worktree')


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--public', type=Path, required=True)
    parser.add_argument('--upstream-sha', required=True)
    parser.add_argument('--experiment-worktree', type=Path, required=True)
    parser.add_argument('--shell-worktree', type=Path, required=True)
    parser.add_argument('--upstream-worktree', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    require_clean(args.experiment_worktree)
    require_clean(args.shell_worktree)
    require_clean(args.upstream_worktree)
    if git_head(args.upstream_worktree) != args.upstream_sha:
        parser.error('upstream worktree HEAD does not match --upstream-sha')
    public_digest, file_count = tree_digest(args.public)
    report = {
        'schemaVersion': 2,
        'generatedAt': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'upstreamSha': args.upstream_sha,
        'upstreamTree': subprocess.check_output(
            ['git', '-C', str(args.upstream_worktree), 'rev-parse', 'HEAD^{tree}'],
            text=True).strip(),
        'experimentHead': git_head(args.experiment_worktree),
        'shellHead': git_head(args.shell_worktree),
        'publicTreeSha256': public_digest,
        'publicFileCount': file_count,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
