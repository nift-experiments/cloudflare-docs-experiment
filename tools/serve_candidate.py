#!/usr/bin/env python3
"""Serve a candidate tree without exposing deployment metadata."""
import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class CandidateHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        root = Path(self.directory).resolve()
        target = Path(self.translate_path(self.path)).resolve()
        try:
            relative = target.relative_to(root)
        except ValueError:
            relative = Path('..')
        first = relative.parts[0] if relative.parts else ''
        if first in {'.git', 'CP6.md', '..'}:
            self.send_error(404)
            return None
        return super().send_head()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', required=True)
    parser.add_argument('--bind', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()
    handler = lambda *values, **options: CandidateHandler(
        *values, directory=args.root, **options)
    ThreadingHTTPServer((args.bind, args.port), handler).serve_forever()


if __name__ == '__main__':
    main()
