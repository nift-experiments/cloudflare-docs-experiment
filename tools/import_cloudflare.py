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


# Backtick-delimited spans (inline code and whole fenced blocks) are opaque to
# Nift's find_balanced, so braces inside them never affect an @markup boundary.
# This masks them for the deterministic pre-emission brace-balance guard.
_BT_SPAN = re.compile(r'`[^`\n]*`|^[ \t]*`{3,}[^\n]*\n.*?^[ \t]*`{3,}', re.M | re.S)


def _guard_balanced_braces(body, what):
    """Raise ValueError if the non-code portion of a body is brace- or
    quote-unbalanced.

    Mirrors Nift's find_balanced rule (backtick spans and comments opaque) so an
    @markup boundary can be emitted safely. Deterministic; no per-page
    special-casing. A stray double-quote would also break the boundary, so it is
    guarded here."""
    masked = _BT_SPAN.sub('', body)
    masked = re.sub(r'<!--[\s\S]*?-->', '', masked)
    masked = re.sub(r'@/\*[\s\S]*?\*/', '', masked)
    depth = 0
    quote = None
    for ch in masked:
        if quote:
            if ch == '\\':
                continue
            if ch == quote:
                quote = None
            continue
        if ch == '"':
            quote = '"'
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth < 0:
                raise ValueError(f'{what}: unbalanced prose "}}" would break an @markup boundary')
    if depth != 0:
        raise ValueError(f'{what}: unbalanced prose braces would break an @markup boundary')
    if quote is not None:
        raise ValueError(f'{what}: unbalanced double-quote would break an @markup boundary')




_BODY_REGISTRY = []  # list of (idx, body_with_placeholders)
_BODY_NEXT = 0       # global monotonically increasing body id
_BODY_DIR = None      # set by import_corpus to content/.markup/bodies


def _dedent_component_html(body):
    """Remove leading whitespace from lines that are pure component HTML
    (nb-* divs, asides, sections) so CommonMark does not treat tab-indented
    component output inside list items as indented code blocks."""
    out = []
    for ln in body.split('\n'):
        stripped = ln.strip()
        if re.match(r'^<(?:div|aside|section|details|span|pre) class="nb-', stripped) or \
           re.match(r'^</(?:div|aside|section|details|span|pre)>$', stripped):
            out.append(stripped)
        else:
            out.append(ln)
    return '\n'.join(out)


def _materialize_bodies(text, placeholders):
    """Replace \x01BODY{idx}\x02 markers with @markup("md", path) references and
    write each body to a Markdown file (with code restored). Nested bodies are
    resolved so a body file may itself reference another body file."""
    refs = {}
    for idx, body in _BODY_REGISTRY:
        restored = restore_code(body, placeholders)
        restored = _dedent_component_html(restored)
        refs[idx] = restored
    # resolve nested markers recursively
    def resolve(body):
        if '\x01BODY' not in body:
            return body
        for ridx, _ in _BODY_REGISTRY:
            marker = f'\x01BODY{ridx}\x02'
            body = body.replace(marker, f'@markup("md", "content/.markup/bodies/{ridx}.md")')
        return body
    for idx, body in _BODY_REGISTRY:
        refs[idx] = resolve(refs[idx])
        if _BODY_DIR is not None:
            p = _BODY_DIR / f'{idx}.md'
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(refs[idx])
        text = text.replace(f'\x01BODY{idx}\x02', f'@markup("md", "content/.markup/bodies/{idx}.md")')
    _BODY_REGISTRY.clear()
    return text


def _wrap_markup(body, what):
    """Emit the body through an explicit Nift Markdown boundary as a file-based
    @markup("md", path) reference.

    The component HTML shell is preserved while the body is rendered by Nift from
    a generated Markdown file. Using the file form avoids Nift's find_balanced
    parsing of arbitrary Markdown bodies (apostrophes, stray backticks, irregular
    fences), which the inline form cannot handle deterministically across the
    corpus."""
    if not body.strip():
        return body
    _guard_balanced_braces(body, what)
    global _BODY_NEXT
    idx = _BODY_NEXT
    _BODY_NEXT += 1
    _BODY_REGISTRY.append((idx, body))
    return f'\x01BODY{idx}\x02'


def render(name, a, body=''):
    at = attrs(a)
    title = html.escape(at.get('title') or at.get('text') or name)
    # Block components carry Markdown bodies; wrap them in an explicit Nift
    # Markdown boundary so Nift renders the body (fences, lists, bold) instead
    # of leaving it literal inside the component HTML block.
    wrapped = _wrap_markup(body, f'<{name}>')
    if name == 'Aside':
        return f'<aside class="nb-aside {html.escape(at.get("type", "note"))}">{wrapped}</aside>'
    if name == 'Badge' or name == 'InlineBadge':
        return f'<span class="nb-badge">{html.escape(at.get("text", body or name))}</span>'
    if name in {'Card', 'LinkCard', 'LinkTitleCard', 'ListCard'}:
        href = html.escape(at.get('href', '#'), quote=True)
        return f'<a class="nb-card nb-link-card" href="{href}"><strong>{title}</strong>{wrapped}</a>'
    if name in {'CardGrid', 'FourCardGrid'}:
        return f'<div class="nb-card-grid">{wrapped}</div>'
    if name == 'Steps':
        return f'<div class="nb-steps">{wrapped}</div>'
    if name == 'Step':
        return f'<section class="nb-step">{wrapped}</section>'
    if name == 'Details':
        return f'<details class="nb-details"><summary>{title}</summary>{wrapped}</details>'
    if name == 'FileTree':
        return f'<pre class="nb-file-tree">{wrapped}</pre>'
    if name in {'Tabs', 'PackageManagers'}:
        return f'<div class="nb-tabs" data-nb-tabs>{wrapped}</div>'
    if name == 'TabItem':
        label = html.escape(at.get('label', at.get('value', 'Tab')))
        ident = 'tab-' + re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-')
        return f'<section class="nb-tab-panel" id="{ident}" data-tab-label="{label}">{wrapped}</section>'
    cls = MODEL['components'][name]
    if cls == 'browser-interactive':
        return f'<div class="nb-interactive-component" data-cf-component="{name}">{wrapped}</div>'
    if cls == 'data-generated':
        return f'<div class="nb-data-component" data-cf-component="{name}">{wrapped}</div>'
    return f'<div class="nb-{re.sub(r"(?<!^)(?=[A-Z])", "-", name).lower()}">{wrapped}</div>'


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


def _render_title_inline_code(title, placeholders=None):
    """Render a directive title, restoring inline code placeholders and keeping
    the upstream's raw HTML (e.g. <code>traceroute</code>) intact."""
    if placeholders:
        title = re.sub(r'\x00CODE(\d+)\x00', lambda m: placeholders.get(f'\x00CODE{m.group(1)}\x00', ''), title)
    return title


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
        inner = reduce_components(inner, 0, placeholders)
        cls = name or 'note'
        head = f'<h3 class="nb-aside-title">{_render_title_inline_code(title, placeholders)}</h3>\n' if title else ''
        inner_markup = _wrap_markup(inner, f':::{cls}')
        block = f'<aside class="nb-aside {html.escape(cls)}">\n{head}{inner_markup}\n</aside>'
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
    global _BODY_REGISTRY
    _BODY_REGISTRY = []
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
    # Materialize @markup body references: write each component/directive body to
    # a Markdown file under content/.markup/bodies/ and reference it via the
    # file-based @markup("md", path) form (avoids find_balanced fragility).
    text = _materialize_bodies(text, placeholders)
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