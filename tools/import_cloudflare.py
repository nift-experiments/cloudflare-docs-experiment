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

FENCE = re.compile(r'^[ \t]*`{3,}[^\n]*\n.*?^[ \t]*`{3,}', re.M | re.S)
TILDE = re.compile(r'^[ \t]*~{3,}[^\n]*\n.*?^[ \t]*~{3,}', re.M | re.S)
INLINE = re.compile(r'`[^`\n]*`')
MDX_COMMENT = re.compile(r'\{/\*[\s\S]*?\*/\}')
IMPORT_RE = re.compile(r'^\s*import\s+[^\n]*;?\s*$', re.M)
EXPORT_RE = re.compile(r'^\s*export\s+[^\n]*;?\s*$', re.M)
# Multi-line ES module statements: 'import {\n  A,\n  B\n} from "~/components";'
# and 'export { ... } from ...' forms are build-time only and must not leak into
# generated content. Scoped to component-module sources we own.
MULTILINE_IMPORT = re.compile(
    r'^\s*(?:import|export)\s*\{[^}]*\}\s*from\s*["\'][^"\']+["\'];?',
    re.M | re.S)
MULTILINE_IMPORT2 = re.compile(
    r'^\s*import\s+[A-Za-z0-9_$]+\s*,\s*\{[^}]*\}\s*from\s*["\'][^"\']+["\'];?',
    re.M | re.S)
FRONT = re.compile(r'^---\n([\s\S]*?)\n---\n?')
ESCAPED_LT = re.compile(r'\\<')
COMPONENT_SRC = re.compile(r'^~/components|^@cloudflare/realtimekit')
IMPORT_STATEMENT = re.compile(r'^\s*import\s+([^;\n]+?)\s+from\s+["\']([^"\']+)["\']', re.M)
SELF_CLOSING = None  # replaced by balanced scanner (see reduce_components)
PAIR = None
TAG_START = re.compile(r'<([A-Z][A-Za-z0-9_.]*)\b')
TAG_CLOSE = re.compile(r'</\s*([A-Z][A-Za-z0-9_.]*)\s*>')
DIRECTIVE_LINE = re.compile(r'^[ \t]*:::([a-zA-Z][\w-]*)?(?:\[[^\]]*\])?[ \t]*$')


def _line_blockquote(text, i):
    """Number of leading '>' blockquote markers on the line containing text[i].
    Returns 0 when the line does not begin with a '>' marker."""
    j = i
    while j > 0 and text[j - 1] != '\n':
        j -= 1
    k = j
    depth = 0
    while k < len(text):
        if text[k] != '>':
            break
        depth += 1
        if k + 1 < len(text) and text[k + 1] in (' ', '\t'):
            k += 2
        else:
            k += 1
    return depth if k > j else 0


def _is_blockquote_marker(text, j):
    """True when text[j] == '>' is a blockquote marker: the first non-whitespace
    character of its line, followed by space/tab/newline/end. Only used to
    tolerate multi-line component tags written inside Markdown blockquotes."""
    k = j
    while k > 0 and text[k - 1] != '\n':
        if text[k - 1] not in ' \t':
            return False
        k -= 1
    nxt = text[j + 1] if j + 1 < len(text) else ''
    return nxt in ('', ' ', '\t', '\n')


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
    # Only tolerate '>' blockquote markers when the tag itself opens on a line
    # that is blockquote-prefixed (e.g. '> <PackageManagers ...').
    in_bq = _line_blockquote(text, i) > 0
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
            if in_bq and _is_blockquote_marker(text, j):
                j += 1
                continue
            attrs = text[m.end():j]
            self_close = bool(re.search(r'/\s*$', attrs))
            return attrs, j + 1, self_close
        j += 1
    return None


def match_pair(text, start, name):
    """Find the balanced closing </name> for a tag whose content starts at `start`.
    Returns (inner_text, index_after_close) or (None, None) when unbalanced.

    Body text between tags is scanned only for '<'; quote and {..} tracking
    applies strictly inside a tag (between '<' and its '>'), so prose
    apostrophes such as "SDK's" or "Don't" never enter quote mode."""
    i = start
    depth = 0
    n = len(text)
    while i < n:
        if text[i] != '<':
            i += 1
            continue
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


def reduce_components(text, depth=0, placeholders=None):
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
                            out.append(render(name, attrs, reduce_components(inner, depth + 1, placeholders)))
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
    """Replace fenced and inline code with single-line placeholders.

    Fences are paired sequentially: each opening fence is closed by the very
    next line that is a run of 3+ backticks (or tildes), regardless of its
    length, so adjacent/indented fences never merge across content."""
    placeholders = {}

    def stash(m):
        key = f'\x00CODE{len(placeholders)}\x00'
        val = m.group(0) if hasattr(m, 'group') else m
        placeholders[key] = val
        return key

    lines = text.split('\n')
    out = []
    i = 0
    n = len(lines)
    FENCE_OPEN = re.compile(r'^[ \t]*(?:[0-9]+[.)][ \t]+)?(`{3,}|~{3,})')
    while i < n:
        ln = lines[i]
        m = FENCE_OPEN.match(ln)
        if m:
            start = i
            marker = m.group(1)[0]
            i += 1
            while i < n:
                cm = re.match(r'^[ \t]*' + re.escape(marker) + r'{3,}', lines[i])
                if cm:
                    i += 1
                    break
                i += 1
            out.append(stash('\n'.join(lines[start:i])))
            continue
        out.append(ln)
        i += 1
    text = '\n'.join(out)
    text = INLINE.sub(stash, text)
    text = ESCAPED_LT.sub(stash, text)
    return text, placeholders


def restore_code(text, placeholders):
    for key, val in placeholders.items():
        text = text.replace(key, val)
    return text


def convert_directives(text, placeholders=None):
    """Convert ::: directives to aside blocks (line-count preserving, nested-safe).

    Handles both bare ':::note' / ':::' and titled ':::note[Title]' forms."""
    lines = text.split('\n')
    delims = []
    for i, ln in enumerate(lines):
        m = DIRECTIVE_LINE.match(ln)
        if m:
            name = m.group(1)
            title = ''
            tm = re.match(r'^[ \t]*:::[a-zA-Z][\w-]*(\[[^\]]*\])?', ln)
            if tm and tm.group(1):
                title = tm.group(1)[1:-1]
            delims.append((i, name, title))
    stack = []
    spans = []
    for i, name, title in delims:
        if name:
            stack.append((i, name, title))
        else:
            if stack:
                oi, oname, otitle = stack.pop()
                spans.append((oi, i, oname, otitle))
            else:
                stack.append((i, None, None))
    # Unclosed directives (upstream corpus occasionally omits the closing ':::')
    # are closed at end-of-text rather than left as literal source.
    for oi, oname, otitle in stack:
        spans.append((oi, len(lines), oname, otitle))
    if not spans:
        return text
    # Process spans from the highest closing index downward so earlier index
    # replacements never shift the positions of still-pending spans.
    spans.sort(key=lambda s: s[1], reverse=True)
    for oi, ci, name, title in spans:
        inner = convert_directives('\n'.join(lines[oi + 1:ci]), placeholders)
        cls = name or 'note'
        head = f'<h3 class="nb-aside-title">{html.escape(title)}</h3>\n' if title else ''
        block = f'<aside class="nb-aside {html.escape(cls)}">\n{head}{inner}\n</aside>'
        lines = lines[:oi] + block.split('\n') + lines[ci + 1:]
    return '\n'.join(lines)


def render_markdown(text, blocks=True):
    """Render Markdown to HTML with a CommonMark engine, preserving raw HTML.

    When blocks=True, inserts blank lines around block HTML tags so CommonMark
    treats content inside component/directive HTML blocks as renderable Markdown.
    When blocks=False, renders top-level Markdown only (component bodies have
    already been rendered). Falls back to passthrough if no engine is available."""
    try:
        import cmarkgfm
    except ImportError:
        return text
    if blocks:
        BLOCK = r'(?:div|section|aside|details|pre|table|ul|ol|dl|blockquote|h[1-6])'
        text = re.sub(r'(<' + BLOCK + r'[^>]*>)(?=[^\s<])', r'\1\n', text)
        text = re.sub(r'(?<=[^\s>])(</' + BLOCK + r'>)', r'\n\1', text)
        lines = []
        for ln in text.split('\n'):
            stripped = ln.strip()
            if re.match(r'^<' + BLOCK + r'[^>]*>\s*$', stripped):
                lines.append(ln)
                lines.append('')
            elif re.match(r'^\s*</' + BLOCK + r'>$', stripped):
                lines.append('')
                lines.append(ln)
            else:
                lines.append(ln)
        text = '\n'.join(lines)
    opts = getattr(cmarkgfm, 'Options', None)
    flag = getattr(opts, 'CMARK_OPT_UNSAFE', 0) if opts else 0
    return cmarkgfm.markdown_to_html(text, options=flag)


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
    text = MULTILINE_IMPORT.sub('', text)
    text = MULTILINE_IMPORT2.sub('', text)
    text = IMPORT_RE.sub('', text)
    text = EXPORT_RE.sub('', text)
    text = convert_directives(text, placeholders)
    # Unknown-component gate on non-code content, import-aware.
    names = set(re.findall(r'</?([A-Z][A-Za-z0-9_.]*)\b', text))
    unknown = sorted((names - KNOWN) & imported)
    if unknown:
        raise ValueError(f'{path}: unknown MDX components: {", ".join(unknown)}')
    text = reduce_components(text, 0, placeholders)
    # The unresolved check must ignore component-looking tags that live inside
    # code (restored into bodies and rendered as <pre>/<code>). Strip code
    # blocks from the check text.
    check_text = re.sub(r'<pre>[\s\S]*?</pre>', '', text)
    check_text = re.sub(r'<code>[\s\S]*?</code>', '', check_text)
    remain = re.findall(r'</?([A-Z][A-Za-z0-9_.]*)\b', check_text)
    # Only matrix components that fail to reduce are fatal; unmatched prose tags
    # (placeholders, TS types, attribute text) are preserved verbatim.
    unresolved = sorted({c for c in remain if c in KNOWN})
    if unresolved:
        raise ValueError(f'{path}: unresolved MDX components: {", ".join(unresolved)}')
    text = restore_code(text, placeholders)
    # Source-style '~/assets/...' references resolve to the staged upstream
    # asset tree at /assets/upstream/ in the generated site.
    text = text.replace('~/assets/', '/assets/upstream/')
    # 'src/assets/...' references (upstream source-tree paths) resolve to the
    # same staged /assets/upstream/ tree.
    text = text.replace('src/assets/', '/assets/upstream/')
    # 'public/images/...' and other 'public/...' references in Markdown are
    # root-relative to the upstream public/ static tree, so map them to '/...'
    # only inside Markdown link/image destinations and quoted attrs.
    text = re.sub(r'\(public/', '(/', text)
    text = re.sub(r'"(public/)', '"/', text)
    # A bare '---' horizontal rule left at the start of the body would be
    # misread by Nift as an unterminated front-matter block. Drop a leading
    # standalone '---' line (it was an HR after the stripped import block).
    body = text.strip() + '\n'
    if body.startswith('---\n'):
        body = body[4:].lstrip('\n')
        if not body:
            body = '\n'
    return fm, body


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