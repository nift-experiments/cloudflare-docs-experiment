#!/usr/bin/env python3
"""Attest that the deployed tree and representative HTTP responses match a candidate."""
import argparse
import hashlib
import json
import subprocess
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote

from artifact_provenance import tree_digest


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--public', type=Path, required=True)
    parser.add_argument('--remote', required=True, help='rsync destination, for example host:/srv/site/')
    parser.add_argument('--url', required=True)
    parser.add_argument('--candidate-provenance', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)

    provenance = json.loads(args.candidate_provenance.read_text())
    digest, file_count = tree_digest(args.public)
    if (provenance.get('publicTreeSha256') != digest or
            provenance.get('publicFileCount') != file_count):
        parser.error('candidate provenance public tree mismatch')

    result = subprocess.run([
        'rsync', '-ani', '--checksum', '--delete', '--exclude=/.git/', '--exclude=/CP6.md',
        str(args.public) + '/', args.remote.rstrip('/') + '/',
    ], text=True, capture_output=True, check=True)
    differences = [line for line in result.stdout.splitlines() if line.strip()]

    files = sorted(path for path in args.public.rglob('*') if path.is_file())
    relative_paths = [path.relative_to(args.public).as_posix() for path in files]

    def verify_file(item):
        path, relative = item
        request_path = relative[:-10] if relative.endswith('/index.html') else relative
        if relative == 'index.html':
            request_path = ''
        url = args.url.rstrip('/') + '/' + quote(request_path, safe='/')
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                served = response.read()
                status = response.status
            local = path.read_bytes()
            if status == 200 and local == served:
                return None
            return {'path': '/' + relative, 'status': status,
                    'localSha256': hashlib.sha256(local).hexdigest(),
                    'servedSha256': hashlib.sha256(served).hexdigest()}
        except Exception as exc:
            return {'path': '/' + relative, 'error': str(exc)}

    with ThreadPoolExecutor(max_workers=32) as executor:
        http_mismatches = [result for result in executor.map(verify_file, zip(files, relative_paths))
                           if result is not None]

    report = {
        'schemaVersion': 1,
        'candidateProvenance': provenance,
        'remote': args.remote,
        'url': args.url,
        'rsyncChecksumDifferences': differences,
        'httpFileCount': len(files),
        'httpPathListSha256': hashlib.sha256('\n'.join(relative_paths).encode()).hexdigest(),
        'httpMismatches': http_mismatches,
        'verified': not differences and not http_mismatches,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    return 0 if report['verified'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
