#!/usr/bin/env python3
"""Strict Cloudflare MDX -> Nift staging importer.

Unknown JSX components are fatal; no silent flattening is permitted.
This is intentionally dependency-free so the migration does not acquire a Node
toolchain.

Real-corpus corrections (Linode validation, pinned bc2bdaee):
- Fenced ``` / ~~~ and inline `` code are protected before any component,
  directive or expression processing, so shell tokens and TS types inside code
  are never mistaken for MDX components and never rewritten.
- MDX comments `{/* ... */}` and build-only `import`/`export` lines are removed.
- Container directives (`:::note`, `:::caution`, `:::tip`, `:::warning`,
  `:::info` and bare `:::` callouts) are converted to `<aside class="nb-aside ...">`
  blocks with a line-count-preserving pairing so nested callouts survive.
- Unknown-component detection is import-aware, matching the CP3 census: a
  capitalized tag is treated as an MDX component only when it is registered in
  the compatibility matrix, exported by upstream `src/mdx-components.ts`, or
  imported in that file from a component module. Other capitalized tags are
  literal prose/placeholder text and are preserved verbatim.
"""
from __future__ import annotations
import argparse, html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL = json.loads((ROOT / 'compatibility/content-model.json').read_text())
KNOWN = set(MODEL['components'])

FENCE = re.compile(r'^```[^\n]*\n.*?^```', re.M | re.S)
TILDE = re.compile(r'^~~~[^\n]*\n.*?^~~~', re.M | re.S)
INLINE = re.compile(r'`[^`]*`')
MDX_COMMENT = re.compile(r'\{/\*[\s\S]*?\*/\}')
IMPORT_RE = re.compile(r'^\s*import\s+[^\n]*;?\s*$', re.M)
EXPORT_RE = re.compile(r'^\s*export\s+[^\n]*;?\s*$', re.M)
FRONT = re.compile(r'^---\n([\s\S]*?)\n---\n?')
TAG = re.compile(r'<([A-Z][A-Za-z0-9_.:-]*)\b')
COMPONENT_SRC = re.compile(r'^~/components|^@cloudflare/realtimekit')
IMPORT_STATEMENT = re.compile(r'^\s*import\s+([^;\n]+?)\s+from\s+["\']([^"\']+)["\']', re.M)
SELF_CLOSING = None  # replaced by balanced scanner (see reduce_components)
PAIR = None
TAG_START = re.compile(r'<([A-Z][A-Za-z0-9_.]*)\b')
TAG_CLOSE = re.compile(r'</([A-Z][A-Za-z0-9_.]*)\s*>')
DIRECTIVE_LINE = re.compile(r'^[ \t]*:::[ \t]*([a-zA-Z][\w-]*)?[ \t]*$')


def scan_tag(text, i):
    """Scan a component tag starting at text[i]. Returns (attrs, end, self_close)
    or None. Handles quoted strings and {..} expression attributes, so angle
    brackets inside attribute values (e.g. `<Type text="Array<String>" />` or a
    `json={{ content: "<TUNNEL_ID>..." }}` body) do not truncate the scan."""
    m = TAG_START.match(text, i)
    if not m:
        return None
    j = m.end()
    brace = 0
    quote = None
    while j < len(text):
        c = text[j]
        if quote:
            if c == quote:
                quote = None
        elif c in ('"', "'"):
            quote = c
        elif c == '{':
            brace += 1
        elif c == '}':
            if brace:
                brace -= 1
        elif c == '>' and brace == 0:
            attrs = text[m.end():j]
            self_close = bool(re.search(r'/\s*$', attrs))
            return attrs, j + 1, self_close
        j += 1
    return None


def match_pair(text, start, name):
    """Find the balanced closing </name> for a tag whose content starts at `start`.
    Returns (inner_text, index_after_close) or (None, None) when unbalanced."""
    brace = 0
    quote = None
    i = start
    depth = 0
    n = len(text)
    while i < n:
        c = text[i]
        if quote:
            if c == quote:
                quote = None
            i += 1
            continue
        if c in ('"', "'"):
            quote = c
            i += 1
            continue
        if c == '{':
            brace += 1
            i += 1
            continue
        if c == '}':
            if brace:
                brace -= 1
            i += 1
            continue
        if c == '<' and brace == 0:
            if i + 1 < n and text[i + 1] == '/':
                cm = TAG_CLOSE.match(text, i)
                if cm:
                    if cm.group(1) == name and depth == 0:
                        return text[start:i], cm.end()
                    depth = max(0, depth - 1)
                    i = cm.end()
                    continue
            m = TAG_START.match(text, i)
            if m:
                t = scan_tag(text, i)
                if t:
                    _, end, sc = t
                    if not sc:
                        depth += 1
                    i = end
                    continue
        i += 1
    return None, None


def reduce_components(text, depth=0):
    if depth > 200:
        return text
    out = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] == '<':
            m = TAG_START.match(text, i)
            if m:
                name = m.group(1)
                tag = scan_tag(text, i)
                if tag:
                    attrs, end, sc = tag
                    if sc:
                        if name in KNOWN:
                            out.append(render(name, attrs, ''))
                        else:
                            out.append(text[i:end])
                        i = end
                        continue
                    inner, next_i = match_pair(text, end, name)
                    if inner is not None:
                        if name in KNOWN:
                            out.append(render(name, attrs, reduce_components(inner, depth + 1)))
                        else:
                            out.append(text[i:next_i])
                        i = next_i
                        continue
            # unmatched uppercase tag: literal prose, preserve verbatim
            out.append(text[i])
            i += 1
            continue
        out.append(text[i])
        i += 1
    return ''.join(out)


def attrs(s):
    out = {}
    for m in re.finditer(r'([:\w-]+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|\{([^{}]*)\})', s):
        out[m.group(1)] = next((x for x in m.groups()[1:] if x is not None), '')
    return out


def render(name, a, body=''):
    at = attrs(a)
    title = html.escape(at.get('title') or at.get('text') or name)
    if name == 'Aside':
        return f'<aside class="nb-aside {html.escape(at.get("type", "note"))}">{body}</aside>'
    if name == 'Badge' or name == 'InlineBadge':
        return f'<span class="nb-badge">{html.escape(at.get("text", body or name))}</span>'
    if name in {'Card', 'LinkCard', 'LinkTitleCard', 'ListCard'}:
        href = html.escape(at.get('href', '#'), quote=True)
        return f'<a class="nb-card nb-link-card" href="{href}"><strong>{title}</strong>{body}</a>'
    if name in {'CardGrid', 'FourCardGrid'}:
        return f'<div class="nb-card-grid">{body}</div>'
    if name == 'Steps':
        return f'<div class="nb-steps">{body}</div>'
    if name == 'Step':
        return f'<section class="nb-step">{body}</section>'
    if name == 'Details':
        return f'<details class="nb-details"><summary>{title}</summary>{body}</details>'
    if name == 'FileTree':
        return f'<pre class="nb-file-tree">{body}</pre>'
    if name in {'Tabs', 'PackageManagers'}:
        return f'<div class="nb-tabs" data-nb-tabs>{body}</div>'
    if name == 'TabItem':
        label = html.escape(at.get('label', at.get('value', 'Tab')))
        ident = 'tab-' + re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-')
        return f'<section class="nb-tab-panel" id="{ident}" data-tab-label="{label}">{body}</section>'
    cls = MODEL['components'][name]
    if cls == 'browser-interactive':
        return f'<div class="nb-interactive-component" data-cf-component="{name}">{body}</div>'
    if cls == 'data-generated':
        return f'<div class="nb-data-component" data-cf-component="{name}">{body}</div>'
    return f'<div class="nb-{re.sub(r"(?<!^)(?=[A-Z])", "-", name).lower()}">{body}</div>'


def imported_component_names(text):
    names = set()
    for spec, src in IMPORT_STATEMENT.findall(text):
        if COMPONENT_SRC.search(src):
            for ident in re.findall(r'\b[A-Z][A-Za-z0-9_]*\b', spec):
                names.add(ident)
    return names


def protect_code(text):
    """Replace fenced and inline code with single-line placeholders."""
    placeholders = {}

    def stash(m):
        key = f'\x00CODE{len(placeholders)}\x00'
        placeholders[key] = m.group(0)
        return key

    text = FENCE.sub(stash, text)
    text = TILDE.sub(stash, text)
    text = INLINE.sub(stash, text)
    return text, placeholders


def restore_code(text, placeholders):
    for key, val in placeholders.items():
        text = text.replace(key, val)
    return text


def convert_directives(text):
    """Convert ::: directives to aside blocks (line-count preserving, nested-safe)."""
    lines = text.split('\n')
    delims = []
    for i, ln in enumerate(lines):
        m = DIRECTIVE_LINE.match(ln)
        if m:
            delims.append((i, m.group(1)))
    stack = []
    spans = []
    for i, name in delims:
        if name:
            stack.append((i, name))
        else:
            if stack:
                oi, oname = stack.pop()
                spans.append((oi, i, oname))
            else:
                stack.append((i, None))
    if not spans:
        return text
    spans.sort(key=lambda s: s[1] - s[0], reverse=True)
    for oi, ci, name in spans:
        inner = convert_directives('\n'.join(lines[oi + 1:ci]))
        cls = name or 'note'
        block = f'<aside class="nb-aside {html.escape(cls)}">\n{inner}\n</aside>'
        lines = lines[:oi] + block.split('\n') + lines[ci + 1:]
    return '\n'.join(lines)


def convert(text, path='<memory>'):
    fm = {}
    m = FRONT.match(text)
    if m:
        for line in m.group(1).splitlines():
            if ':' in line and not line.startswith((' ', '\t')):
                fm[line.split(':', 1)[0].strip()] = line.split(':', 1)[1].strip().strip('"\'')
        text = text[m.end():]
    raw = text
    imported = imported_component_names(raw)
    text, placeholders = protect_code(text)
    text = MDX_COMMENT.sub('', text)
    text = IMPORT_RE.sub('', text)
    text = EXPORT_RE.sub('', text)
    text = convert_directives(text)
    # Unknown-component gate on non-code content, import-aware.
    names = set(re.findall(r'</?([A-Z][A-Za-z0-9_.]*)\b', text))
    unknown = sorted((names - KNOWN) & imported)
    if unknown:
        raise ValueError(f'{path}: unknown MDX components: {", ".join(unknown)}')
    text = reduce_components(text)
    remain = re.findall(r'</?([A-Z][A-Za-z0-9_.]*)\b', text)
    # Only matrix components that fail to reduce are fatal; unmatched prose tags
    # (placeholders, TS types, attribute text) are preserved verbatim.
    unresolved = sorted({c for c in remain if c in KNOWN})
    if unresolved:
        raise ValueError(f'{path}: unresolved MDX components: {", ".join(unresolved)}')
    text = restore_code(text, placeholders)
    return fm, text.strip() + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('source')
    ap.add_argument('output')
    args = ap.parse_args()
    src, out = Path(args.source), Path(args.output)
    failures = []
    count = 0
    for p in src.rglob('*'):
        if p.suffix not in {'.md', '.mdx'}:
            continue
        try:
            fm, body = convert(p.read_text(), p)
            q = out / p.relative_to(src)
            q = q.with_suffix('.md')
            q.parent.mkdir(parents=True, exist_ok=True)
            q.write_text(body)
            count += 1
        except Exception as e:
            failures.append(str(e))
    if failures:
        print('\n'.join(failures), file=sys.stderr)
        return 2
    print(f'imported {count} files')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())