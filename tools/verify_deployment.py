#!/usr/bin/env python3
"""Attest that the deployed tree and representative HTTP responses match a candidate."""
import argparse
import hashlib
import json
import re
import shlex
import posixpath
import subprocess
import urllib.request
import urllib.error
from pathlib import Path
from urllib.parse import urlsplit

from artifact_provenance import tree_digest


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, file_pointer, code, message, headers, new_url):
        return None


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

    remote_host, separator, remote_root = args.remote.partition(':')
    if not separator or not remote_host or not remote_root.startswith('/'):
        parser.error('--remote must be in host:/absolute/path form')
    parsed_url = urlsplit(args.url)
    remote_hostname = remote_host.rsplit('@', 1)[-1]
    if (parsed_url.scheme != 'http' or parsed_url.hostname != remote_hostname or
            parsed_url.path not in ('', '/') or parsed_url.query or parsed_url.fragment):
        parser.error('--url must be the root HTTP URL for the --remote SSH host')
    port = parsed_url.port or 80
    process_result = subprocess.run(
        ['ssh', remote_host, 'ps', '-eo', 'pid=,args='], text=True,
        capture_output=True, check=True)
    server_processes = []
    expected_script = posixpath.join(posixpath.dirname(remote_root.rstrip('/')),
                                     'serve_candidate.py')
    local_server_sha = hashlib.sha256(
        (Path(__file__).resolve().parent / 'serve_candidate.py').read_bytes()).hexdigest()
    remote_server_sha = subprocess.check_output(
        ['ssh', remote_host, 'sha256sum', expected_script], text=True).split()[0]
    for line in process_result.stdout.splitlines():
        fields = line.strip().split(maxsplit=1)
        if len(fields) != 2:
            continue
        tokens = shlex.split(fields[1])
        if (len(tokens) != 8 or not tokens[0].endswith('python3') or
                tokens[1] != expected_script or
                any(tokens.count(option) != 1 for option in ('--root', '--bind', '--port'))):
            continue
        try:
            root = tokens[tokens.index('--root') + 1].rstrip('/')
            bind = tokens[tokens.index('--bind') + 1]
            process_port = int(tokens[tokens.index('--port') + 1])
        except (ValueError, IndexError):
            continue
        server_processes.append({'pid': int(fields[0]), 'command': fields[1],
                                 'root': root, 'bind': bind, 'port': process_port})
    listener_result = subprocess.run(
        ['ssh', remote_host, 'ss', '-ltnp'], text=True, capture_output=True, check=True)
    listener_lines = [line.strip() for line in listener_result.stdout.splitlines()
                      if re.search(rf':{port}\s', line)]
    listener_pids = {
        int(match)
        for line in listener_lines
        for match in re.findall(r'pid=(\d+)', line)
    }

    probes = []
    for relative in ('index.html', 'fundamentals/index.html', 'assets/cf-design.css',
                     'assets/cf-shell.js', 'assets/navigation.json'):
        local = (args.public / relative).read_bytes()
        request_path = '' if relative == 'index.html' else relative
        if request_path.endswith('/index.html'):
            request_path = request_path[:-10]
        url = args.url.rstrip('/') + '/' + request_path
        opener = urllib.request.build_opener(NoRedirect)
        with opener.open(url, timeout=30) as response:
            served = response.read()
            status = response.status
        probes.append({
            'path': '/' + relative,
            'status': status,
            'localSha256': hashlib.sha256(local).hexdigest(),
            'servedSha256': hashlib.sha256(served).hexdigest(),
            'matches': local == served,
        })
    denied_metadata = []
    for path in ('/.git/HEAD', '/CP6.md'):
        try:
            opener.open(args.url.rstrip('/') + path, timeout=30)
            status = 200
        except urllib.error.HTTPError as exc:
            status = exc.code
        denied_metadata.append({'path': path, 'status': status})

    report = {
        'schemaVersion': 1,
        'candidateProvenance': provenance,
        'remote': args.remote,
        'url': args.url,
        'rsyncChecksumDifferences': differences,
        'serverProcesses': server_processes,
        'serverScript': {'path': expected_script, 'localSha256': local_server_sha,
                         'remoteSha256': remote_server_sha,
                         'matches': local_server_sha == remote_server_sha},
        'listenerPids': sorted(listener_pids),
        'listenerLines': listener_lines,
        'httpProbes': probes,
        'deniedMetadata': denied_metadata,
        'verified': (not differences and len(server_processes) == 1 and
                     local_server_sha == remote_server_sha and
                     server_processes[0]['root'] == remote_root.rstrip('/') and
                     server_processes[0]['bind'] in ('0.0.0.0', parsed_url.hostname) and
                     server_processes[0]['port'] == port and
                     listener_pids == {server_processes[0]['pid']} and
                     all(probe['status'] == 200 and probe['matches'] for probe in probes) and
                     all(item['status'] == 404 for item in denied_metadata)),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    return 0 if report['verified'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
