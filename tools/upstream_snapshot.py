"""Materialize a tracked-only snapshot of a pinned Git revision."""
import atexit
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path


def tracked_snapshot(repository, revision):
    destination = Path(tempfile.mkdtemp(prefix='cp8-upstream-'))
    atexit.register(shutil.rmtree, destination, ignore_errors=True)
    process = subprocess.Popen(
        ['git', '-C', str(repository), 'archive', '--format=tar', revision],
        stdout=subprocess.PIPE,
    )
    try:
        with tarfile.open(fileobj=process.stdout, mode='r|') as archive:
            archive.extractall(destination, filter='data')
    finally:
        process.stdout.close()
    if process.wait() != 0:
        raise RuntimeError(f'could not archive upstream revision {revision}')
    (destination / '.upstream-sha').write_text(revision + '\n')
    return destination
