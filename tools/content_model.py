#!/usr/bin/env python3
"""CP3 Cloudflare content-model census and strict compatibility gate.

Runs against the frozen upstream checkout. This deliberately fails if it sees a
construct that is not present in compatibility/content-model.json; unknown MDX
is never silently flattened.

Real-corpus corrections (Linode validation, pinned bc2bdaee):
- Fenced ``` and ~~~ code blocks plus inline `` code are stripped before
  component/directive matching so shell tokens (<API_TOKEN> etc.) and TS types
  inside code are not mistaken for MDX components.
- A capitalized tag counts as an MDX component only when it is registered in
  the compatibility matrix, exported by upstream src/mdx-components.ts, or
  imported in that file from a component module (~/components, realtimekit).
  Any OTHER capitalized tag is recorded as an "unmatched tag" (prose / inline
  attribute text such as <Type text="Array<String>" />) and is not fatal,
  because upstream itself builds the corpus successfully.
- mdx-components.ts exports missing from the matrix are a hard gate so the
  global component surface cannot drift out of sync.
- Directives are matched by their same-line name only; bare `:::` blocks are
  counted as the known generic callout and never guessed from content words.
- The report no longer truncates the unknown detail list.
"""
from __future__ import annotations
import argparse, collections, json, re, sys
from pathlib import Path

TAG = re.compile(r'<([A-Z][A-Za-z0-9_.:-]*)\b')
IMPORT_RE = re.compile(r'^\s*import\s+([^;\n]+?)\s+from\s+["\']([^"\']+)["\'];?', re.M | re.S)
COMPONENT_SRC = re.compile(r'^~/components|^@cloudflare/realtimekit')
FRONT = re.compile(r'^---\s*\n(.*?)\n---(?:\n|$)', re.S)
KEY = re.compile(r'^([A-Za-z_][\w-]*):(?:\s|$)', re.M)
FENCE = re.compile(r'^[ \t]*`{3,}[^\n]*\n.*?^[ \t]*`{3,}', re.M | re.S)
TILDE = re.compile(r'^[ \t]*~{3,}[^\n]*\n.*?^[ \t]*~{3,}', re.M | re.S)
INLINE = re.compile(r'`[^`\n]*`')
DIRECTIVE = re.compile(r'(^|\n)\s*:::([a-zA-Z][\w-]*)')
BARE_DIRECTIVE = re.compile(r'(^|\n)\s*:::\s*$')
MDX_BARREL = re.compile(r'^\s*export\s+(?:const|let)\s+components\b', re.M)

# Syntax intrinsic to MDX/Markdown, not a named imported component.
INTRINSIC = {"Fragment"}

def route_for(rel: str) -> str:
    x = rel.removeprefix('src/content/docs/')
    x = re.sub(r'\.(md|mdx)$', '', x)
    x = re.sub(r'(^|/)index$', '', x).strip('/')
    return '/' + (x + '/' if x else '')

def load_matrix(p: Path):
    d = json.loads(p.read_text())
    return d, set(d['components']), set(d['frontmatter']), set(d['directives'])

def upstream_global_components(root: Path):
    """Parse src/mdx-components.ts export names (authoritative global surface)."""
    f = root / 'src/mdx-components.ts'
    if not f.exists():
        return set()
    s = f.read_text(errors='replace')
    names = set()
    for m in re.finditer(r'^\s*([A-Z][A-Za-z0-9_]*)\s*[,}]', s, re.M):
        names.add(m.group(1))
    return names

def imported_components(s: str):
    names = set()
    for spec, src in IMPORT_RE.findall(s):
        if COMPONENT_SRC.search(src):
            for ident in re.findall(r'\b[A-Z][A-Za-z0-9_]*\b', spec):
                names.add(ident)
    return names

def strip_code(s: str):
    lines = s.split('\n')
    out = []
    i = 0
    n = len(lines)
    fence_open = re.compile(r'^[ \t]*(?:[0-9]+[.)][ \t]+)?(`{3,}|~{3,})')
    while i < n:
        ln = lines[i]
        m = fence_open.match(ln)
        if m:
            marker = m.group(1)[0]
            i += 1
            while i < n:
                if re.match(r'^[ \t]*' + re.escape(marker) + r'{3,}', lines[i]):
                    i += 1
                    break
                i += 1
            continue
        out.append(ln)
        i += 1
    s = '\n'.join(out)
    s = INLINE.sub('', s)
    return s

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('upstream', type=Path)
    ap.add_argument('--matrix', type=Path, default=Path('compatibility/content-model.json'))
    ap.add_argument('-o', '--output', type=Path, default=Path('reports/CP3-CENSUS.json'))
    ap.add_argument('--fixtures', type=Path, default=Path('fixtures/cp3'))
    a = ap.parse_args()
    root = a.upstream.resolve()
    docs = root / 'src/content/docs'
    if not docs.is_dir():
        raise SystemExit('expected src/content/docs in upstream checkout')
    matrix, known_components, known_front, known_directives = load_matrix(a.matrix)
    global_components = upstream_global_components(root)
    matrix_gap = sorted(global_components - known_components)
    known_components = known_components | global_components
    counts = {k: collections.Counter() for k in
              ['components', 'frontmatter', 'imports', 'directives', 'html', 'fences',
               'bare-directives', 'features']}
    examples = {k: {} for k in ['components', 'frontmatter', 'directives', 'unmatched-tags']}
    routes = {}
    unknown = []
    unmatched = collections.Counter()
    files = sorted([*docs.rglob('*.md'), *docs.rglob('*.mdx')])
    for p in files:
        rel = p.relative_to(root).as_posix()
        s = p.read_text(errors='replace')
        route = route_for(rel)
        if route in routes:
            unknown.append({'kind': 'route-collision', 'value': route, 'files': [routes[route], rel]})
        routes[route] = rel
        fm = FRONT.match(s)
        for key in KEY.findall(fm.group(1) if fm else ''):
            counts['frontmatter'][key] += 1
            examples['frontmatter'].setdefault(key, rel)
            if key not in known_front:
                unknown.append({'kind': 'frontmatter', 'value': key, 'file': rel})
        t = strip_code(s)
        file_comps = imported_components(s)
        for c in TAG.findall(t):
            if c in INTRINSIC:
                continue
            counts['components'][c] += 1
            examples['components'].setdefault(c, rel)
            if c in known_components:
                continue
            if c in file_comps:
                unknown.append({'kind': 'component', 'value': c, 'file': rel,
                                'reason': 'imported from component module but not classified in matrix'})
            else:
                unmatched[c] += 1
                examples['unmatched-tags'].setdefault(c, rel)
        for _, src in IMPORT_RE.findall(s):
            counts['imports'][src] += 1
        for _, d in DIRECTIVE.findall(t):
            counts['directives'][d] += 1
            examples['directives'].setdefault(d, rel)
            if d not in known_directives:
                unknown.append({'kind': 'directive', 'value': d, 'file': rel})
        counts['bare-directives']['(bare)'] += len(BARE_DIRECTIVE.findall(t))
        counts['html'].update(re.findall(r'<([a-z][a-z0-9-]*)\b', t))
        counts['fences'].update(x or '(plain)' for x in
                                re.findall(r'^```\s*([^\s{]*)', s))
        if re.search(r'^\s*export\s+(?:const|let|var|function|class|default)\b', s, re.M):
            counts['features']['mdx-export'] += 1
        if re.search(r'(?<!\\)\{(?![\{#])', t):
            counts['features']['jsx-expression'] += 1
    report = {
        'schema': 2,
        'pinned_upstream': matrix['pinned_upstream'],
        'docs': len(files),
        'routes': len(routes),
        'route_sample': dict(list(sorted(routes.items()))[:20]),
        'global_components_from_mdx_components_ts': sorted(global_components),
        'global_components_missing_from_matrix': matrix_gap,
        'counts': {k: v.most_common() for k, v in counts.items()},
        'examples': examples,
        'unmatched_tags': unmatched.most_common(),
        'unmatched_tags_total': sum(unmatched.values()),
        'unknown_count': len(unknown),
        'unknown': unknown,
    }
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(report, indent=2) + '\n')
    a.fixtures.mkdir(parents=True, exist_ok=True)
    (a.fixtures / 'README.md').write_text(
        '# CP3 real-usage fixture index\n\nGenerated by `tools/content_model.py` '
        'from the frozen upstream checkout.\n\n'
        + ''.join(f'- `{k}` — `{v}`\n' for k, v in sorted(examples['components'].items())))
    print(f"scanned {len(files)} docs / {len(routes)} routes; unknown={len(unknown)}"
          f"; unmatched_tags={sum(unmatched.values())}")
    if matrix_gap:
        print('STRICT GATE FAILED: mdx-components.ts exports missing from matrix: '
              + ', '.join(matrix_gap), file=sys.stderr)
        return 2
    if unknown:
        print('STRICT GATE FAILED: compatibility matrix has unknown constructs', file=sys.stderr)
        return 2
    print('STRICT GATE PASSED: every discovered named construct is classified')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())