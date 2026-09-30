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
import argparse, ast, datetime, html, json, re, sys, textwrap
from urllib.parse import quote
from zoneinfo import ZoneInfo
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL = json.loads((ROOT / 'compatibility/content-model.json').read_text())
KNOWN = set(MODEL['components'])
_RESOURCE_ENTRIES = []
_PARTIALS_DIR = None
_PAGES_BUILD_PRESETS = {}
_PAGES_BUILD_ENVIRONMENTS = []
_GLOSSARIES = {}
_CURRENT_PRODUCT = ''
_CURRENT_METADATA = {}
_RELEASE_NOTES = {}
_WRANGLER_COMMANDS = {}
_CODE_CONSTANTS = {}
_NOTIFICATIONS = []
_RAW_IMPORTS = {}
_COMPATIBILITY_FLAGS = []
_UPSTREAM_ROOT = None
_WARP_RELEASES = []
_DIRECTORY_ENTRIES = []
_CHANGELOG_PRODUCT_IDS = set()
_DASH_ROUTES = {}
_AGENTS = []
_VIDEOS = []
_ACTIVE_CODE_PLACEHOLDERS = {}
_ASTRO_ASSET_CACHE = {}
_COMPONENT_USAGE_NAMES = [
    'AnchorHeading', 'APIRequest', 'Code', 'DashButton', 'Details', 'Example',
    'Image', 'LinkCard', 'Markdown', 'MetaInfo', 'PackageManagers', 'Render',
    'Steps', 'TabItem', 'Tabs', 'Type', 'TypeScriptExample', 'Width',
    'WranglerCommand', 'WranglerConfig', 'WranglerNamespace',
]
_COMPONENT_USAGE = {}

FENCE = re.compile(r'^[ \t]*`{3,}[^\n]*\n.*?^[ \t]*`{3,}', re.M | re.S)
TILDE = re.compile(r'^[ \t]*~{3,}[^\n]*\n.*?^[ \t]*~{3,}', re.M | re.S)
FENCE_OPEN = re.compile(r'^[ \t]*(?:[0-9]+[.)][ \t]+)?(`{3,}|~{3,})')
INLINE = re.compile(r'`[^`\n]*`')
_ML_TAG = re.compile(r'<([a-z][a-z0-9-]*)(?=[^<>]*?\n)([^<>]*?)>', re.S)
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
ASSET_IMPORT = re.compile(r'^\s*import\s+([A-Za-z_$][\w$]*)\s+from\s+["\'](~\/assets\/[^"\']+)["\'];?', re.M)
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
                            if name == 'LinkButton':
                                while out and out[-1] in {' ', '\t'}:
                                    out.pop()
                            out.append(render(name, attrs, ''))
                        else:
                            out.append(text[i:end])
                        i = end
                        continue
                    inner, next_i = match_pair(text, end, name)
                    if inner is not None:
                        if name in KNOWN:
                            if name == 'LinkButton':
                                while out and out[-1] in {' ', '\t'}:
                                    out.pop()
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
    position = 0
    while True:
        match = re.search(r'([:\w-]+)\s*=\s*', s[position:])
        if not match:
            break
        key = match.group(1)
        start = position + match.end()
        if start >= len(s):
            break
        quote = s[start]
        if quote in {'"', "'"}:
            end = start + 1
            while end < len(s):
                if s[end] == quote and s[end - 1] != '\\':
                    break
                end += 1
            out[key] = s[start + 1:end]
            position = end + 1
            continue
        if quote == '{':
            depth, end, string_quote = 1, start + 1, None
            while end < len(s) and depth:
                char = s[end]
                if string_quote:
                    if char == string_quote and s[end - 1] != '\\':
                        string_quote = None
                elif char in {'"', "'", '`'}:
                    string_quote = char
                elif char == '{':
                    depth += 1
                elif char == '}':
                    depth -= 1
                end += 1
            out[key] = s[start + 1:end - 1]
            position = end
            continue
        position = start + 1
    return out


def _parse_js_literal(source, scope=None):
    """Parse the restricted object/array literals used by frozen MDX props."""
    source = str(source).strip()
    position = 0

    def whitespace():
        nonlocal position
        while position < len(source) and source[position].isspace():
            position += 1

    def value():
        nonlocal position
        whitespace()
        if position >= len(source):
            raise ValueError('empty JSX literal')
        char = source[position]
        if char in {'"', "'", '`'}:
            start = position
            position += 1
            while position < len(source):
                if source[position] == char and source[position - 1] != '\\':
                    position += 1
                    if char == '`':
                        return source[start + 1:position - 1]
                    return ast.literal_eval(source[start:position])
                position += 1
            raise ValueError('unterminated JSX string')
        if char == '[':
            position += 1
            result = []
            while True:
                whitespace()
                if position < len(source) and source[position] == ']':
                    position += 1
                    return result
                result.append(value())
                whitespace()
                if position < len(source) and source[position] == ',':
                    position += 1
                    continue
                if position >= len(source) or source[position] != ']':
                    raise ValueError('invalid JSX array')
        if char == '{':
            position += 1
            result = {}
            while True:
                whitespace()
                if position < len(source) and source[position] == '}':
                    position += 1
                    return result
                key_match = re.match(r'[A-Za-z_$][\w$-]*', source[position:])
                if key_match:
                    key = key_match.group(0)
                    position += len(key)
                elif position < len(source) and source[position] in {'"', "'", '`'}:
                    key = value()
                else:
                    raise ValueError('invalid JSX object key')
                whitespace()
                if position >= len(source) or source[position] != ':':
                    raise ValueError('missing JSX object colon')
                position += 1
                result[str(key)] = value()
                whitespace()
                if position < len(source) and source[position] == ',':
                    position += 1
                    continue
                if position >= len(source) or source[position] != '}':
                    raise ValueError('invalid JSX object')
        token = re.match(r'-?\d+(?:\.\d+)?|[A-Za-z_$][\w$.]*', source[position:])
        if not token:
            raise ValueError(f'unsupported JSX literal near {source[position:position + 20]!r}')
        raw = token.group(0)
        position += len(raw)
        if raw == 'true': return True
        if raw == 'false': return False
        if raw == 'null': return None
        if re.fullmatch(r'-?\d+(?:\.\d+)?', raw):
            return float(raw) if '.' in raw else int(raw)
        if raw.startswith('props.'):
            prop = raw.split('.', 1)[1]
            if scope is None or prop not in scope:
                raise ValueError(f'Render partial parameter references missing prop: {prop}')
            return scope[prop]
        raise ValueError(f'unsupported JSX identifier: {raw}')

    parsed = value()
    whitespace()
    if position != len(source):
        raise ValueError(f'trailing JSX literal content: {source[position:]!r}')
    return parsed


def _clean_attr(value):
    value = str(value or '').strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def _has_boolean_attr(source, name):
    return re.search(r'(?:^|\s)' + re.escape(name) + r'(?:\s|/?>|$)', source) is not None


def configure_resources(entries):
    """Register frozen content metadata used by ResourcesBySelector."""
    global _RESOURCE_ENTRIES
    _RESOURCE_ENTRIES = list(entries)


def configure_partials(partials_dir):
    global _PARTIALS_DIR
    _PARTIALS_DIR = Path(partials_dir) if partials_dir else None


def configure_source_root(root):
    global _UPSTREAM_ROOT
    _UPSTREAM_ROOT = Path(root).resolve() if root else None


def configure_pages_build_presets(presets):
    global _PAGES_BUILD_PRESETS
    _PAGES_BUILD_PRESETS = dict(presets or {})


def configure_pages_build_environments(environments):
    global _PAGES_BUILD_ENVIRONMENTS
    _PAGES_BUILD_ENVIRONMENTS = list(environments or [])


def configure_glossaries(glossaries):
    global _GLOSSARIES
    _GLOSSARIES = dict(glossaries or {})


def configure_release_notes(release_notes):
    global _RELEASE_NOTES
    _RELEASE_NOTES = dict(release_notes or {})


def configure_wrangler_commands(commands):
    global _WRANGLER_COMMANDS
    _WRANGLER_COMMANDS = dict(commands or {})


def configure_notifications(notifications):
    global _NOTIFICATIONS
    _NOTIFICATIONS = list(notifications or [])


def configure_compatibility_flags(flags):
    global _COMPATIBILITY_FLAGS
    _COMPATIBILITY_FLAGS = list(flags or [])


def configure_warp_releases(releases):
    global _WARP_RELEASES
    _WARP_RELEASES = list(releases or [])


def configure_directory_entries(entries):
    global _DIRECTORY_ENTRIES
    _DIRECTORY_ENTRIES = list(entries or [])


def configure_changelog_products(product_ids):
    global _CHANGELOG_PRODUCT_IDS
    _CHANGELOG_PRODUCT_IDS = set(product_ids or [])


def configure_dash_routes(routes):
    global _DASH_ROUTES
    _DASH_ROUTES = dict(routes or {})


def configure_agents(agents):
    global _AGENTS
    _AGENTS = list(agents or [])


def configure_videos(videos):
    global _VIDEOS
    _VIDEOS = list(videos or [])


def configure_component_usage(usage):
    global _COMPONENT_USAGE, _COMPONENT_USAGE_NAMES
    _COMPONENT_USAGE = dict(usage or {})
    _COMPONENT_USAGE_NAMES = sorted(_COMPONENT_USAGE)


def _render_params(attributes, scope):
    raw = attrs(attributes).get('params')
    if raw is None:
        return {}
    values = _parse_js_literal(raw, scope)
    if not isinstance(values, dict):
        raise ValueError('Render params must be an object')
    return values


def _substitute_render_props(source, scope):
    def attr_value(match):
        name = match.group(1)
        if name not in scope:
            return match.group(0)
        return '="' + html.escape(str(scope[name]), quote=True) + '"'

    source = re.sub(
        r'\{props\.(\w+)\s*\+\s*(["\'])(.*?)\2\}',
        lambda match: str(scope.get(match.group(1), f'props.{match.group(1)}')) + match.group(3),
        source,
    )
    source = re.sub(
        r'\$\{props\.(\w+)\}',
        lambda match: str(scope.get(match.group(1), match.group(0))),
        source,
    )
    source = re.sub(r'=\{props\.(\w+)\}', attr_value, source)
    source = re.sub(
        r'\{props\.(\w+)\}',
        lambda match: str(scope.get(match.group(1), match.group(0))),
        source,
    )
    return re.sub(
        r'\bprops\.(\w+)\b',
        lambda match: json.dumps(scope[match.group(1)]) if match.group(1) in scope else match.group(0),
        source,
    )


def expand_render_partials(text, stack=(), scope=None):
    """Inline frozen Render partials before the normal MDX conversion pass."""
    scope = scope or {}
    if _PARTIALS_DIR is None or '<Render' not in text:
        return text
    out = []
    i = 0
    while i < len(text):
        match = re.search(r'<Render\b', text[i:])
        if not match:
            out.append(text[i:])
            break
        start = i + match.start()
        out.append(text[i:start])
        tag = scan_tag(text, start)
        if not tag:
            out.append(text[start])
            i = start + 1
            continue
        attributes, end, self_close = tag
        if not self_close:
            out.append(text[start:end])
            i = end
            continue
        values = attrs(attributes)
        params = _render_params(attributes, scope)
        product = _clean_attr(values.get('product')).strip('/')
        filename = _clean_attr(values.get('file')).strip('/')
        relative = Path(product) / f'{filename}.mdx'
        partial = (_PARTIALS_DIR / relative).resolve()
        if _PARTIALS_DIR.resolve() not in partial.parents:
            raise ValueError(f'Render partial escapes source root: {relative.as_posix()}')
        if not partial.is_file():
            suffix = Path(f'{filename}.mdx')
            candidates = [candidate.resolve() for candidate in _PARTIALS_DIR.rglob(suffix.name)
                          if candidate.parts[-len(suffix.parts):] == suffix.parts]
            if len(candidates) == 1:
                partial = candidates[0]
                relative = partial.relative_to(_PARTIALS_DIR.resolve())
        if not partial.is_file():
            # The frozen corpus contains a small set of stale partial references;
            # retain their explicit data-component shell instead of fabricating text.
            out.append(text[start:end])
            i = end
            continue
        key = relative.as_posix()
        if key in stack:
            raise ValueError(f'Render partial cycle: {" -> ".join(stack + (key,))}')
        source = partial.read_text(errors='replace')
        frontmatter = FRONT.match(source)
        if frontmatter:
            source = source[frontmatter.end():]
        source = _substitute_render_props(source, params)
        expanded = expand_render_partials(source, stack + (key,), params)
        if re.search(r'\bprops\.', expanded):
            out.append(text[start:end])
            i = end
            continue
        footnote_prefix = re.sub(r'[^a-z0-9]+', '-', key.casefold()).strip('-')
        out.append(expand_footnotes(expanded, footnote_prefix))
        i = end
    return ''.join(out)


def _attribute_list(value):
    return re.findall(r'["\']([^"\']+)["\']', str(value or ''))


def _render_resources(attributes):
    types = set(_attribute_list(attributes.get('types')))
    products = set(_attribute_list(attributes.get('products')))
    directory = _clean_attr(attributes.get('directory')).strip('/')
    show_descriptions = _clean_attr(attributes.get('showDescriptions', 'true')).lower() != 'false'
    resources = []
    for entry in _RESOURCE_ENTRIES:
        if types and entry.get('pcx_content_type') not in types:
            continue
        if directory and not entry.get('id', '').startswith(directory):
            continue
        if products and not products.intersection(entry.get('products') or []):
            continue
        resources.append(entry)
    if not resources:
        raise ValueError('ResourcesBySelector: no resources match the configured selector')
    cards = []
    for entry in resources:
        description = ''
        if show_descriptions and entry.get('description'):
            description = f'<span>{html.escape(str(entry["description"]))}</span>'
        content_type = str(entry.get('pcx_content_type') or '').replace('-', ' ').title()
        meta = f'<small>{html.escape(content_type)}</small>' if content_type else ''
        cards.append(
            f'<a class="nb-card nb-link-card resource-card" href="{html.escape(entry["route"], quote=True)}">'
            f'<strong>{html.escape(str(entry["title"]))}</strong>{description}{meta}</a>'
        )
    return '<div class="nb-card-grid resource-grid">' + ''.join(cards) + '</div>'


def _render_glossary(product):
    entries = []
    for product_id, glossary in _GLOSSARIES.items():
        if product and product_id != product:
            continue
        for entry in glossary.get('entries', []):
            entries.append((entry.get('term', ''), entry.get('general_definition', ''),
                            glossary.get('productName', '')))
    entries.sort(key=lambda entry: entry[0].casefold())
    product_header = '' if product else '<th>Product</th>'
    rows = []
    for term, definition, product_name in entries:
        product_cell = '' if product else f'<td>{html.escape(product_name)}</td>'
        rendered = render_markdown(
            definition[:1].upper() + definition[1:], blocks=False).strip()
        rows.append(f'<tr><td>{html.escape(term)}</td><td>{rendered}</td>{product_cell}</tr>')
    return ('<table id="glossary-table"><thead><tr><th>Term</th><th>Definition</th>'
            f'{product_header}</tr></thead><tbody>{"".join(rows)}</tbody></table>')


def _render_glossary_definition(term, prepend=''):
    for glossary in _GLOSSARIES.values():
        for entry in glossary.get('entries', []):
            if str(entry.get('term', '')).casefold() != term.casefold():
                continue
            definition = str(prepend) + str(entry.get('general_definition') or '')
            definition = definition[:1].upper() + definition[1:]
            return f'<div class="nb-glossary-definition">{render_markdown(definition).strip()}</div>'
    raise ValueError(f'GlossaryDefinition: unknown term {term}')


def _render_tutorials():
    tutorials = [entry for entry in _RESOURCE_ENTRIES
                 if entry.get('pcx_content_type') == 'tutorial' and
                 entry.get('id', '').startswith(_CURRENT_PRODUCT + '/')]
    tutorials.sort(key=lambda entry: entry.get('reviewed', ''), reverse=True)
    rows = ''.join(
        f'<tr><td><a href="{html.escape(entry["route"], quote=True)}">{html.escape(entry["title"])}</a></td>'
        f'<td>{html.escape(entry.get("reviewed", ""))}</td><td>{html.escape(entry.get("difficulty", ""))}</td></tr>'
        for entry in tutorials
    )
    return ('<table><thead><tr><td>Name</td><td>Last Updated</td><td>Difficulty</td></tr></thead>'
            f'<tbody>{rows}</tbody></table>')


def _render_directory_listing(attributes, raw_attributes=''):
    folder = _clean_attr(attributes.get('folder') or _CURRENT_METADATA.get('_route', '')).strip('/')
    max_depth = int(_clean_attr(attributes.get('maxDepth') or 1))
    tag = _clean_attr(attributes.get('tag'))
    descriptions = (_has_boolean_attr(raw_attributes, 'descriptions') or
                    _clean_attr(attributes.get('descriptions')).lower() == 'true')
    base_depth = len(folder.split('/'))
    entries = []
    for entry in _RESOURCE_ENTRIES:
        entry_id = entry.get('id', '')
        depth = len(entry_id.split('/'))
        if not entry_id.startswith(folder + '/') or depth > base_depth + max_depth:
            continue
        if tag and tag not in (entry.get('tags') or []):
            continue
        sidebar = entry.get('sidebar') or {}
        order = sidebar.get('order', 10**9) if isinstance(sidebar, dict) else 10**9
        entries.append((order, str(entry.get('title') or ''), entry))
    entries.sort(key=lambda item: (item[0], item[1].casefold()))
    items = []
    for _order, _title, entry in entries:
        href = entry.get('external_link') or entry.get('route')
        description = (f'<p>{html.escape(str(entry.get("description") or ""))}</p>'
                       if descriptions and entry.get('description') else '')
        items.append(f'<li><a href="{html.escape(str(href), quote=True)}">{html.escape(str(entry.get("title") or ""))}</a>{description}</li>')
    return '<ul class="directory-listing">' + ''.join(items) + '</ul>'


def _render_release_notes():
    names = _CURRENT_METADATA.get('release_notes_file_name') or []
    if isinstance(names, str):
        names = [names]
    selected = []
    if names == ['api-deprecations']:
        selected = [note for note in _RELEASE_NOTES.values()
                    if note.get('productName') == 'API deprecations']
    else:
        selected = [_RELEASE_NOTES[name] for name in names if name in _RELEASE_NOTES]
    entries = []
    for note in selected:
        entries.extend(note.get('entries', []))
    entries.sort(key=lambda entry: str(entry.get('publish_date', '')), reverse=True)
    rendered = []
    for entry in entries:
        raw_date = str(entry.get('publish_date', ''))
        date = raw_date[:10]
        if len(raw_date) > 10:
            try:
                instant = datetime.datetime.fromisoformat(raw_date.replace('Z', '+00:00'))
                if instant.tzinfo:
                    date = str(instant.astimezone(ZoneInfo('Australia/Brisbane')).date())
            except ValueError:
                pass
        description = render_markdown(str(entry.get('description') or '')).strip()
        title = entry.get('title')
        rendered.append(f'<h2>{html.escape(date)}</h2>')
        if title:
            rendered.append(f'<strong>{html.escape(str(title))}</strong>')
        rendered.append(description)
    return ''.join(rendered)


def _render_component_usage(component):
    usage = _COMPONENT_USAGE.get(component, {})
    count = int(usage.get('count', 0))
    pages = sorted(usage.get('pages', []))
    docs = [path for path in pages if path.startswith('src/content/docs/')]
    partials = [path for path in pages if path.startswith('src/content/partials/')]
    output = [
        f'<p>The <code>{html.escape(component)}</code> component is used '
        f'<code>{count}</code> times on <code>{len(pages)}</code> pages.</p>',
        f'<details><summary>See all examples of pages that use {html.escape(component)}</summary>',
        f'<p>Used <strong>{count}</strong> times.</p><p><strong>Pages</strong></p><ul>',
    ]
    for path in docs:
        route = '/' + path.removeprefix('src/content/docs/').removesuffix('.mdx').removesuffix('.md')
        route = route.removesuffix('/index') + '/'
        route = '/'.join(re.sub(r'[^a-z0-9.]+', '-', part.casefold()).strip('-')
                         for part in route.split('/'))
        source = 'https://github.com/cloudflare/cloudflare-docs/blob/production/' + path
        output.append(
            f'<li><a href="{html.escape(route, quote=True)}" target="_blank">{html.escape(route)}</a> - '
            f'<a href="{html.escape(source, quote=True)}" target="_blank">Source</a></li>')
    output.append('</ul><p><strong>Partials</strong></p><ul>')
    for path in partials:
        source = 'https://github.com/cloudflare/cloudflare-docs/blob/production/' + path
        output.append(f'<li><a href="{html.escape(source, quote=True)}" target="_blank">{html.escape(path)}</a></li>')
    output.append('</ul></details>')
    return ''.join(output)


def _render_wrangler_definition(definition, heading_level=2):
    command = str(definition.get('command', '')).removeprefix('wrangler ')
    metadata = definition.get('metadata') or {}
    args = definition.get('args') or {}
    positional = definition.get('positionalArgs') or []
    usage = command
    for name in positional:
        usage += f' [{str(name).upper()}]'
    rows = []
    for name, details in args.items():
        if details.get('hidden'):
            continue
        flag = name if name in positional else f'--{name}'
        description = details.get('description') or details.get('describe') or ''
        qualifiers = []
        if details.get('demandOption'):
            qualifiers.append('required')
        if details.get('type'):
            qualifiers.append(str(details['type']))
        if details.get('default') is not None:
            qualifiers.append(f'default: {details["default"]}')
        qualifier = f' <small>{html.escape(", ".join(qualifiers))}</small>' if qualifiers else ''
        rows.append(f'<li><code>{html.escape(flag)}</code>{qualifier}{render_markdown(str(description), blocks=False)}</li>')
    arguments = f'<ul>{"".join(rows)}</ul>' if rows else ''
    description = render_markdown(str(metadata.get('description', '')))
    epilogue = render_markdown(str(metadata.get('epilogue') or ''))
    commands = _package_managers({'type': 'exec', 'pkg': 'wrangler', 'args': usage})
    global_flags = [
        ('--version', 'Show version number'),
        ('--cwd', 'Run as if Wrangler was started in the specified directory instead of the current working directory'),
        ('--config', 'Path to Wrangler configuration file'),
        ('--env', 'Environment to use for operations, and for selecting .env and .dev.vars files'),
        ('--env-file', 'Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files'),
        ('--install-skills', 'Install Cloudflare skills for detected AI coding agents before running the command'),
        ('--profile', 'Use a specific auth profile'),
    ]
    global_markup = ''.join(f'<li><code>{flag}</code><p>{description}</p></li>'
                            for flag, description in global_flags)
    return (f'<h{heading_level}>{html.escape(command)}</h{heading_level}>'
            f'{description}{epilogue}{commands}{arguments}'
            f'<details><summary>Global flags</summary><ul>{global_markup}</ul></details>')


def _render_wrangler_namespace(namespace, heading_level):
    definitions = _WRANGLER_COMMANDS.get(namespace, [])
    if not definitions:
        raise ValueError(f'WranglerNamespace: unknown namespace {namespace}')
    return ''.join(_render_wrangler_definition(definition, heading_level)
                   for definition in definitions if not (definition.get('metadata') or {}).get('hidden'))


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
_CMARKGFM = None
_ORDINARY_BOUNDARY = '.ordinary-body-count'


def require_cmarkgfm():
    """Load the mandatory CommonMark renderer with an actionable failure."""
    global _CMARKGFM
    if _CMARKGFM is None:
        try:
            import cmarkgfm
        except ImportError as exc:
            raise RuntimeError(
                'cmarkgfm is required for Cloudflare corpus rendering; '
                'install the Python cmarkgfm package before importing'
            ) from exc
        _CMARKGFM = cmarkgfm
    return _CMARKGFM


def configure_body_output(body_dir, reset=False):
    """Configure body materialization and allocate IDs without aliasing files.

    Ordinary-corpus import starts from zero in a clean directory. Generated
    families resume after the highest existing numeric body file.
    """
    global _BODY_DIR, _BODY_NEXT, _BODY_REGISTRY
    _BODY_DIR = Path(body_dir)
    _BODY_DIR.mkdir(parents=True, exist_ok=True)
    _BODY_REGISTRY = []
    if reset:
        for path in _BODY_DIR.glob('*.md'):
            if path.stem.isdigit():
                path.unlink()
        _BODY_NEXT = 0
        return
    existing = [int(p.stem) for p in _BODY_DIR.glob('*.md') if p.stem.isdigit()]
    _BODY_NEXT = max(existing, default=-1) + 1


def record_ordinary_body_boundary():
    """Persist the first ID reserved for generated-family bodies."""
    if _BODY_DIR is None:
        raise RuntimeError('body output is not configured')
    (_BODY_DIR / _ORDINARY_BOUNDARY).write_text(f'{_BODY_NEXT}\n')


def configure_generated_body_output(body_dir):
    """Resume at the ordinary boundary and discard stale generated bodies."""
    global _BODY_DIR, _BODY_NEXT, _BODY_REGISTRY
    _BODY_DIR = Path(body_dir)
    marker = _BODY_DIR / _ORDINARY_BOUNDARY
    if not marker.is_file():
        raise RuntimeError(
            f'ordinary body boundary is missing at {marker}; run import_corpus.py first'
        )
    boundary = int(marker.read_text().strip())
    for path in _BODY_DIR.glob('*.md'):
        if path.stem.isdigit() and int(path.stem) >= boundary:
            path.unlink()
    _BODY_REGISTRY = []
    _BODY_NEXT = boundary


def _dedent_component_html(body):
    """Remove leading whitespace from lines that are pure component HTML
    (nb-* divs, asides, sections) so CommonMark does not treat tab-indented
    component output inside list items as indented code blocks."""
    out = []
    for ln in body.split('\n'):
        stripped = ln.strip()
        if re.match(r'^<(?:a|div|aside|section|details|span|pre) class="nb-', stripped) or \
           re.match(r'^<(?:div|iframe|img)\b', stripped) or \
           re.match(r'^</(?:a|div|aside|section|details|span|pre)>$', stripped):
            out.append(stripped)
        else:
            out.append(ln)
    return '\n'.join(out)


def _dedent_component_body(body):
    lines = body.split('\n')
    candidates = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith(('<', '\x01BODY', '@markup(', '@input(')):
            continue
        candidates.append(len(line) - len(line.lstrip()))
    base = min((indent for indent in candidates if indent > 0), default=0)
    if not base:
        return body
    return '\n'.join(line[base:] if len(line) - len(line.lstrip()) >= base else line
                     for line in lines)


def _rewrite_asset_refs(text):
    """Rewrite source-style asset/static references to the generated site.

    '~/assets/...' and 'src/assets/...' resolve to the staged upstream asset tree
    at /assets/upstream/. 'public/...' paths in Markdown link/image destinations
    and quoted attrs map to root-relative '/...' (the upstream public/ tree)."""
    text = text.replace('~/assets/', '/assets/upstream/')
    text = text.replace('src/assets/', '/assets/upstream/')
    text = re.sub(r'(?:\.\./)+assets/', '/assets/upstream/', text)
    text = re.sub(r'\(public/', '(/', text)
    text = re.sub(r'"(public/)', '"/', text)
    def replace_astro_asset(match):
        name = match.group(1)
        if name not in _ASTRO_ASSET_CACHE:
            candidates = [] if not _UPSTREAM_ROOT else [
                path for path in (_UPSTREAM_ROOT / 'src/assets').rglob(name + '.*')
                if path.is_file()
            ]
            _ASTRO_ASSET_CACHE[name] = (
                '/assets/upstream/' + candidates[0].relative_to(
                    _UPSTREAM_ROOT / 'src/assets').as_posix()
                if len(candidates) == 1 else match.group(0)
            )
        return _ASTRO_ASSET_CACHE[name]
    text = re.sub(r'/_astro/([A-Za-z0-9_-]+)\.[A-Za-z0-9_-]+\.(?:avif|png|webp)',
                  replace_astro_asset, text)
    return text


def _compact_pre_blocks(text):
    """Keep rendered code blocks opaque to Nift's outer Markdown pass."""
    return re.sub(r'<pre\b[^>]*>[\s\S]*?</pre>',
                  lambda match: match.group(0).replace('\n', '&#10;'), text,
                  flags=re.I)


def _resolve_asset_imports(text):
    """Resolve Astro asset imports used by native img/Image elements."""
    for identifier, source in ASSET_IMPORT.findall(text):
        target = source.replace('~/assets/', '/assets/upstream/', 1)
        expression = r'\{\s*' + re.escape(identifier) + r'(?:\.src)?\s*\}'
        text = re.sub(expression, f'"{html.escape(target, quote=True)}"', text)
    text = re.sub(r'<Image\b', '<img', text)
    text = re.sub(r'</Image\s*>', '</img>', text)
    return text


def normalize_markdown_heading_lines(text, demote_h1=False):
    """Materialize Markdown headings as stable, uniquely addressable HTML."""
    preserved_html = {}

    def preserve_html(match):
        key = f'\x00HTML{len(preserved_html)}\x00'
        preserved_html[key] = match.group(0)
        return key

    text = re.sub(r'<pre\b[^>]*>[\s\S]*?</pre>', preserve_html, text, flags=re.I)
    text, placeholders = protect_code(text)
    used = set(re.findall(r'<h[1-6][^>]*\bid=["\']([^"\']+)', text, re.I))
    seen_h1 = False

    def replace(match):
        nonlocal seen_h1
        level = len(match.group(1))
        label = re.sub(r'\s+#+\s*$', '', match.group(2).strip())
        for key, value in placeholders.items():
            label = label.replace(key, value)
        if level == 1:
            if demote_h1 or seen_h1:
                level = 2
            else:
                seen_h1 = True
        plain = html.unescape(re.sub(r'<[^>]+>', '', label))
        base = re.sub(r'[^a-z0-9]+', '-', plain.casefold()).strip('-') or 'section'
        slug = base
        suffix = 1
        while slug in used:
            slug = f'{base}-{suffix}'
            suffix += 1
        used.add(slug)
        return f'<h{level} id="{slug}">{_inline_markdown(label)}</h{level}>'

    text = re.sub(r'^(#{1,6})[ \t]+(.+?)[ \t]*$', replace, text, flags=re.M)
    text = restore_code(text, placeholders)
    for key, value in preserved_html.items():
        text = text.replace(key, value)
    return text


def _materialize_bodies(text, placeholders):
    """Replace \x01BODY{idx}\x02 markers with file references and write each body
    to a Markdown file (with code restored). Nested bodies are resolved so a body
    file may itself reference another body file.

    A body is referenced with @input (template include, no CommonMark pass) when
    it is a pure-HTML composition of nested bodies; Nift's @markup("md", path)
    would re-convert the already-rendered nested HTML and split hostile fenced
    code. Leaf bodies and bodies carrying their own Markdown keep @markup so the
    Markdown is rendered exactly once."""
    if _BODY_REGISTRY and _BODY_DIR is None:
        raise RuntimeError(
            'component bodies require configured materialization output; '
            'call configure_body_output() before convert()'
        )
    refs = {}
    for idx, body in _BODY_REGISTRY:
        body = _dedent_component_body(textwrap.dedent(body))
        restored = restore_indented_fences(body, placeholders)
        restored = _dedent_component_html(restored)
        restored = _rewrite_asset_refs(restored)
        restored = _materialize_gfm_tables(restored)
        refs[idx] = restored

    pure_candidates = {idx: _is_pure_html(body) for idx, body in refs.items()}
    resolved = {}
    resolving = set()

    def resolve(ridx):
        if ridx in resolved:
            return resolved[ridx]
        if ridx in resolving:
            raise ValueError(f'component body cycle at {ridx}')
        resolving.add(ridx)
        body = refs[ridx]
        for child, _ in _BODY_REGISTRY:
            marker = f'\x01BODY{child}\x02'
            if marker in body:
                child_html = render_markdown(resolve(child), blocks=True).strip()
                body = body.replace(marker, child_html)
        resolving.remove(ridx)
        resolved[ridx] = body
        return body

    for idx, _body in _BODY_REGISTRY:
        materialized = normalize_markdown_heading_lines(resolve(idx))
        materialized = add_heading_ids(materialized)
        refs[idx] = re.sub(
            r'(<h[2-6][^>]*\bid=["\'])([^"\']+)',
            lambda match: match.group(1) + f'body-{idx}-' + match.group(2),
            materialized, flags=re.I)

    kinds = {idx: 'pure' if pure_candidates[idx] else 'mixed' for idx in refs}

    def ref_for(ridx):
        if kinds.get(ridx) == 'pure':
            return f'@input("content/.markup/bodies/{ridx}.md")'
        return f'@markup("md", "content/.markup/bodies/{ridx}.md")'

    for idx, body in _BODY_REGISTRY:
        if _BODY_DIR is not None:
            p = _BODY_DIR / f'{idx}.md'
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(refs[idx])
        marker = f'\x01BODY{idx}\x02'
        # CommonMark wraps a bare marker as a paragraph. Remove that wrapper so
        # block bodies never become invalid <p><section>/<ul>/<pre> markup.
        text = re.sub(r'<p>\s*' + re.escape(marker) + r'\s*</p>', ref_for(idx), text)
        text = text.replace(marker, ref_for(idx))
    _BODY_REGISTRY.clear()
    return text


def _materialize_gfm_tables(content):
    """Render table blocks before Nift's CommonMark-only nested body pass."""
    lines = content.splitlines()
    output = []
    index = 0
    fence = None
    delimiter = re.compile(r'^\s*\|?\s*:?-+\s*:?(?:\s*\|\s*:?-+\s*:?)+\s*\|?\s*$')
    while index < len(lines):
        stripped = lines[index].lstrip()
        marker = re.match(r'^(`{3,}|~{3,})', stripped)
        if marker:
            token = marker.group(1)
            if fence and token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            elif not fence:
                fence = token
            output.append(lines[index])
            index += 1
            continue
        if (not fence and index + 1 < len(lines) and '|' in lines[index] and
                delimiter.match(lines[index + 1])):
            end = index + 2
            while end < len(lines) and lines[end].strip() and '|' in lines[end]:
                end += 1
            table = textwrap.dedent('\n'.join(lines[index:end]))
            table = re.sub(r'<div\b', '<span', table, flags=re.I)
            table = re.sub(r'</div>', '</span>', table, flags=re.I)
            output.append(render_markdown(table, blocks=False).strip())
            index = end
            continue
        output.append(lines[index])
        index += 1
    return '\n'.join(output)


def _is_pure_html(content):
    """True when a body's non-marker content is only complete HTML tags (a
    composition of component shells and nested body references, not Markdown)."""
    for ln in content.split('\n'):
        s = ln.strip()
        if not s or '\x01BODY' in s:
            continue
        if not (s.startswith('<') and s.endswith('>')):
            return False
    return True


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
    # Surround with blank lines so the outer @markup('md'){@content} CommonMark
    # pass treats the rendered body HTML (e.g. <pre><code>) as top-level blocks
    # rather than re-parsing it inside a component HTML block (which splits
    # code fences such as Rust raw-string examples).
    return f'\n\n\x01BODY{idx}\x02\n\n'


def _inline_markdown(value):
    rendered = render_markdown(value, blocks=False).strip()
    match = re.fullmatch(r'<p>(.*)</p>', rendered, re.S)
    return match.group(1) if match else rendered


_PM_COMMANDS = {
    'npm': {'add': 'npm i', 'create': 'npm create', 'dlx': 'npx', 'exec': 'npx',
            'install': 'npm install', 'run': 'npm run', 'remove': 'npm uninstall', 'dev': '-D'},
    'yarn': {'add': 'yarn add', 'create': 'yarn create', 'dlx': 'yarn dlx', 'exec': 'yarn',
             'install': 'yarn install', 'run': 'yarn run', 'remove': 'yarn remove', 'dev': '-D'},
    'pnpm': {'add': 'pnpm add', 'create': 'pnpm create', 'dlx': 'pnpx', 'exec': 'pnpm',
             'install': 'pnpm install', 'run': 'pnpm run', 'remove': 'pnpm remove', 'dev': '-D'},
    'bun': {'add': 'bun add', 'install': 'bun install', 'remove': 'bun remove', 'dev': '-d'},
}


def _package_managers(attributes):
    command_type = _clean_attr(attributes.get('type') or 'add')
    package = _clean_attr(attributes.get('pkg'))
    args = _clean_attr(attributes.get('args'))
    comment = _clean_attr(attributes.get('comment'))
    prefix = _clean_attr(attributes.get('prefix'))
    development = _clean_attr(attributes.get('dev')).lower() == 'true'
    tabs = []
    for manager, commands in _PM_COMMANDS.items():
        command = commands.get(command_type)
        if not command:
            continue
        if prefix:
            command = f'{prefix} {command}'
        if comment:
            command = f'# {comment.replace("{PKG}", manager)}\n{command}'
        if development and command_type == 'add':
            command += f' {commands["dev"]}'
        rendered_package = package
        if manager == 'yarn' and command_type == 'create':
            rendered_package = re.sub(r'@(?![^@]*/)[^\s]*$', '', rendered_package)
        if rendered_package:
            command += f' {rendered_package}'
        if args:
            separator = ' --' if manager == 'npm' and command_type not in {'dlx', 'exec', 'run'} else ''
            command += f'{separator} {args}'
        tabs.append((manager, command))
    buttons = ''.join(
        f'<button type="button" role="tab" data-nb-pm-tab aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">{manager}</button>'
        for i, (manager, _command) in enumerate(tabs)
    )
    panels = ''.join(
        f'<div role="tabpanel" data-nb-pm-panel{" hidden" if i else ""}>'
        f'<pre><code data-nb-pm-code>{html.escape(command)}</code></pre>'
        f'<button type="button" data-nb-pm-copy data-nb-command="{html.escape(command, quote=True)}" aria-label="Copy to clipboard">Copy</button></div>'
        for i, (_manager, command) in enumerate(tabs)
    )
    return f'<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager">{buttons}</div>{panels}</div>'


def render(name, a, body=''):
    at = attrs(a)
    title = html.escape(at.get('title') or at.get('text') or name)
    # Block components carry Markdown bodies; wrap them in an explicit Nift
    # Markdown boundary so Nift renders the body (fences, lists, bold) instead
    # of leaving it literal inside the component HTML block.
    wrapped = _wrap_markup(body, f'<{name}>')
    if name == 'GlossaryTooltip':
        term = _clean_attr(at.get('term') or body)
        return (f'<span class="nb-glossary-tooltip" title="{html.escape(term, quote=True)}">'
                f'{_inline_markdown(body)}</span>')
    if name == 'Aside':
        return f'<aside class="nb-aside {html.escape(at.get("type", "note"))}">{wrapped}</aside>'
    if name in {'Card', 'Example'}:
        heading = _clean_attr(at.get('title') or name)
        return f'<div class="nb-{name.casefold()}"><h3 class="nb-component-title">{html.escape(heading)}</h3>{wrapped}</div>'
    if name == 'Badge':
        return f'<span class="nb-badge">{html.escape(at.get("text", body or name))}</span>'
    if name == 'InlineBadge':
        label = _clean_attr(at.get('text') or at.get('preset') or body or 'Badge')
        return f'<span class="nb-badge">{html.escape(label.title())}</span>'
    if name == 'Plan':
        labels = {
            'all': 'Available on all plans',
            'paid': 'Available on Paid plans',
            'pro': 'Pro and above',
            'business': 'Business and above',
            'enterprise': 'Enterprise-only',
            'add-on': 'Add-on feature',
            'ent-add-on': 'Enterprise-only paid add-on',
            'workers-all': 'Available on Free and Paid plans',
            'workers-paid': 'Available on Workers Paid plan',
            'beta': 'Available in open beta',
        }
        plan_type = _clean_attr(at.get('type'))
        if plan_type not in labels:
            raise ValueError(f'Plan: unknown type {plan_type}')
        return f'<div class="nb-plan">{labels[plan_type]}</div>'
    if name == 'TunnelCalculator':
        return ('<div class="nb-interactive-component" data-cf-component="TunnelCalculator">'
                '<h3>System configuration</h3><p>Enter the number of cloudflared replicas and available processor cores.</p>'
                '<h3>Metrics</h3><p>Provide expected requests, bandwidth, and concurrent connections.</p>'
                '<h3>Result</h3><p>Use the estimated throughput to calculate your tunnel capacity.</p></div>')
    if name == 'LinkTitleCard':
        href = html.escape(at.get('href', ''), quote=True)
        identity = f'{html.unescape(title)}-{at.get("href", "")}'
        heading_id = 'card-' + (re.sub(r'[^a-z0-9]+', '-', identity.casefold()).strip('-') or 'link')
        return f'<div class="nb-card nb-link-card"><h3 id="{heading_id}"><a href="{href}">{title}</a></h3>{wrapped}</div>'
    if name in {'Card', 'LinkCard', 'ListCard'}:
        description = (f'<p>{html.escape(str(at["description"]))}</p>' if at.get('description') else '')
        if at.get('href'):
            href = html.escape(at['href'], quote=True)
            identity = f'{html.unescape(title)}-{at.get("href", "")}'
            heading_id = 'card-' + (re.sub(r'[^a-z0-9]+', '-', identity.casefold()).strip('-') or 'link')
            return f'<div class="nb-card nb-link-card"><h3 id="{heading_id}"><a href="{href}">{title}</a></h3>{description}{wrapped}</div>'
        return f'<div class="nb-card"><strong>{title}</strong>{description}{wrapped}</div>'
    if name == 'LinkButton':
        href = html.escape(at.get('href', ''), quote=True)
        target = ' target="_blank" rel="noopener noreferrer"' if at.get('target') == '_blank' else ''
        return f'<a class="nb-link-button" href="{href}"{target}>{_inline_markdown(body.strip())}</a>'
    if name in {'CardGrid', 'FourCardGrid'}:
        return f'<div class="nb-card-grid">{wrapped}</div>'
    if name == 'Steps':
        return f'<div class="nb-steps">{wrapped}</div>'
    if name == 'Step':
        return f'<section class="nb-step">{wrapped}</section>'
    if name == 'Details':
        summary = _inline_markdown(at.get('header') or at.get('title') or at.get('text') or 'Details')
        ident = f' id="{html.escape(at["id"], quote=True)}"' if at.get('id') else ''
        opened = ' open' if _has_boolean_attr(a, 'open') or _clean_attr(at.get('open')).lower() == 'true' else ''
        return f'<details class="nb-details"{ident}{opened}><summary>{summary}</summary><div class="nb-details-body">{wrapped}</div></details>'
    if name == 'FileTree':
        return f'<pre class="nb-file-tree">{wrapped}</pre>'
    if name == 'PackageManagers':
        return _package_managers(at)
    if name == 'APIRequest':
        method = _clean_attr(at.get('method') or 'GET').upper()
        path = _clean_attr(at.get('path') or '/')
        command = (f'curl --request {method} \\\n'
                   f'  --url https://api.cloudflare.com/client/v4{path} \\\n'
                   '  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"')
        if at.get('json'):
            try:
                payload = json.dumps(_parse_js_literal(at['json']), indent=2, ensure_ascii=True)
            except ValueError:
                # Dynamic expressions cannot be evaluated during a static import,
                # but retaining their source is preferable to dropping the body.
                payload = _CODE_CONSTANTS.get(at['json'].strip(), at['json'].strip('`'))
            command += " \\\n  --data '" + str(payload) + "'"
        if at.get('form'):
            try:
                form = _parse_js_literal(at['form'])
            except ValueError:
                form = None
            if isinstance(form, dict):
                for key, value in form.items():
                    command += f" \\\n  --form '{key}={value}'"
            else:
                command += " \\\n  --form '" + at['form'].strip('`') + "'"
        return (f'\n\n<pre class="nb-api-request"><code class="language-bash">'
                f'{html.escape(command)}</code></pre>\n\n')
    if name == 'CURL':
        method = _clean_attr(at.get('method') or 'GET').upper()
        url = _clean_attr(at.get('url'))
        command = f'curl --request {method} --url {url}'
        return f'<pre><code class="language-bash">{html.escape(command)}</code></pre>'
    if name == 'Code':
        code_value = _clean_attr(at.get('code'))
        code = _CODE_CONSTANTS.get(code_value, _RAW_IMPORTS.get(code_value, code_value))
        language = _clean_attr(at.get('lang') or 'txt')
        return f'<pre><code class="language-{html.escape(language, quote=True)}">{html.escape(str(code))}</code></pre>'
    if name == 'AnchorHeading':
        depth = int(_clean_attr(at.get('depth') or 2))
        label = _clean_attr(at.get('title') or at.get('text') or body)
        for placeholder, source in _ACTIVE_CODE_PLACEHOLDERS.items():
            if placeholder in label:
                label = label.replace(placeholder, source.strip('`'))
        slug = _clean_attr(at.get('slug')) or re.sub(r'[^a-z0-9]+', '-', label.casefold()).strip('-')
        return f'<h{depth} id="{html.escape(slug, quote=True)}">{_inline_markdown(label)}</h{depth}>'
    if name in {'Type', 'MetaInfo'}:
        return f'<span class="nb-{name.casefold()}">{html.escape(_clean_attr(at.get("text") or body))}</span>'
    if name == 'DirectoryListing':
        return _render_directory_listing(at, a)
    if name == 'Markdown':
        text_value = _clean_attr(at.get('text'))
        markdown = _RAW_IMPORTS.get(text_value, text_value)
        if len(str(markdown)) > 100_000:
            output = ['<div class="raw-markdown">']
            lines = str(markdown).splitlines()
            index = 0
            while index < len(lines):
                fence = re.match(r'^\s*(`{3,}|~{3,})', lines[index])
                if fence:
                    marker = fence.group(1)[0]
                    code = []
                    index += 1
                    while index < len(lines) and not re.match(
                            r'^\s*' + re.escape(marker) + r'{3,}', lines[index]):
                        code.append(lines[index])
                        index += 1
                    index += index < len(lines)
                    escaped_code = html.escape('\n'.join(code)).replace('\n', '&#10;')
                    output.append('<pre><code>' + escaped_code + '</code></pre>')
                    continue
                heading = re.match(r'^(#{1,6})\s+(.+)$', lines[index])
                if heading:
                    level = len(heading.group(1))
                    output.append(f'<h{level}>{html.escape(heading.group(2))}</h{level}>')
                else:
                    output.append(html.escape(lines[index]) + '<br>')
                index += 1
            output.append('</div>')
            return ''.join(output)
        return render_markdown(html.escape(str(markdown), quote=False))
    if name == 'AvailableNotifications':
        product = _clean_attr(at.get('product')).casefold()
        notification_filter = _clean_attr(at.get('notificationFilter')).casefold()
        entries = [entry for entry in _NOTIFICATIONS
                   if (not product or str(entry.get('associatedProducts', '')).casefold() == product)
                   and (not notification_filter or str(entry.get('name', '')).casefold() == notification_filter)]
        groups = {}
        for entry in entries:
            groups.setdefault(str(entry.get('associatedProducts', '')), []).append(entry)
        output = []
        for product_name in sorted(groups):
            if not product and not notification_filter:
                output.append(f'<h2>{html.escape(product_name)}</h2>')
            for entry in groups[product_name]:
                output.append(f'<details><summary>{html.escape(str(entry.get("name", "")))}</summary>')
                for label, key in [('Who is it for?', 'audience'),
                                   ('Other options / filters', 'otherFilters'),
                                   ('Included with', 'availability'),
                                   ('What should you do if you receive one?', 'nextSteps'),
                                   ('Additional information', 'additional_information'),
                                   ('Limitations', 'limitations')]:
                    if entry.get(key):
                        output.append(f'<strong>{label}</strong>{render_markdown(str(entry[key]))}')
                output.append('</details>')
        return ''.join(output)
    if name == 'CompatibilityFlags':
        if not _COMPATIBILITY_FLAGS:
            return '<div class="nb-data-component" data-cf-component="CompatibilityFlags"></div>'
        experimental = _has_boolean_attr(a, 'experimental')
        flags = [flag for flag in _COMPATIBILITY_FLAGS
                 if not experimental or flag.get('experimental')]
        flags.sort(key=lambda flag: str(flag.get('sort_date') or ''), reverse=True)
        output = []
        for flag in flags:
            output.append(f'<h3>{html.escape(str(flag.get("name") or ""))}</h3><table><tbody>')
            for label, key in [('Default as of', 'enable_date'),
                               ('Flag to enable', 'enable_flag'),
                               ('Flag to disable', 'disable_flag')]:
                if flag.get(key):
                    output.append(f'<tr><td><strong>{label}</strong></td><td><code>{html.escape(str(flag[key]))}</code></td></tr>')
            output.append('</tbody></table>')
            flag_body, flag_placeholders = protect_code(str(flag.get('body') or ''))
            flag_body = convert_directives(flag_body, flag_placeholders)
            flag_body = restore_code(flag_body, flag_placeholders, render_fences=True)
            output.append(render_markdown(flag_body))
        return ''.join(output)
    if name == 'WARPReleases':
        track = _clean_attr(at.get('track'))
        today = datetime.date.today()
        try:
            cutoff = today.replace(year=today.year - 1)
        except ValueError:
            cutoff = today.replace(year=today.year - 1, day=28)
        releases = []
        for release in _WARP_RELEASES:
            if release.get('_track') != track:
                continue
            try:
                release_date = datetime.date.fromisoformat(str(release.get('releaseDate', ''))[:10])
            except ValueError:
                continue
            if release_date >= cutoff:
                releases.append((release_date, release))
        releases.sort(key=lambda item: item[0], reverse=True)
        output = ['<h2>Footnotes</h2>']
        for index, (release_date, release) in enumerate(releases):
            platform = str(release.get('platformName') or '')
            version = str(release.get('version') or '')
            label = 'Latest release' if index == 0 else f'{platform} {version}'
            output.append(f'<details class="nb-details"{" open" if index == 0 else ""}><summary>{html.escape(label)}</summary>')
            output.append(f'<p><strong>Release date:</strong> {release_date.isoformat()}</p>')
            if release.get('packageURL'):
                output.append(f'<p><a href="{html.escape(str(release["packageURL"]), quote=True)}">Download {html.escape(platform)} {html.escape(version)}</a></p>')
            output.append('<h4>Release notes</h4>')
            output.append(render_markdown(str(release.get('releaseNotes') or '')))
            output.append('</details>')
        return ''.join(output)
    if name == 'AvailableChangelogFeeds':
        groups = {}
        for directory in _DIRECTORY_ENTRIES:
            entry = directory.get('entry') or {}
            if directory.get('_id') in _CHANGELOG_PRODUCT_IDS and entry.get('group'):
                groups.setdefault(str(entry['group']), []).append((directory.get('_id', ''), entry))
        output = ['<h2>Feeds</h2><h3>Global feed</h3><p>This feed contains entries for all Cloudflare products in the changelog: <a href="/changelog/rss/index.xml">RSS feed</a>.</p>',
                  '<h3>Area-specific feeds</h3><p>Cloudflare also offers RSS feeds scoped to specific product areas or products in the changelog.</p>']
        for group in sorted(groups):
            output.append(f'<h4>{html.escape(group)}</h4><p>This feed is for all {html.escape(group)} products in the changelog.</p><ul>')
            for product_id, entry in sorted(groups[group], key=lambda item: str(item[1].get('title', '')).casefold()):
                title = str(entry.get('title') or product_id)
                href = str(entry.get('url') or f'/{product_id}/')
                output.append(f'<li><a href="{html.escape(href, quote=True)}">{html.escape(title)}</a> <a href="/changelog/rss/{html.escape(product_id, quote=True)}.xml">RSS feed</a></li>')
            output.append('</ul>')
            if group == 'Application security':
                output.append('<aside class="nb-aside note"><h5>DDoS ruleset feeds</h5><p>For <a href="/ddos-protection/">DDoS Protection</a> updates to managed rulesets, please refer to their independent feeds:</p><ul><li><a href="/ddos-protection/change-log/network/">Network-layer DDoS managed ruleset</a></li><li><a href="/ddos-protection/change-log/http/">HTTP DDoS managed ruleset</a></li></ul></aside>')
            if group == 'Core platform':
                output.append('<aside class="nb-aside note"><h5>API deprecations feed</h5><p>Cloudflare also maintains a separate <a href="/fundamentals/api/reference/deprecations/">API deprecations page.</a></p></aside>')
        return ''.join(output)
    if name == 'ComponentsUsage':
        return ''.join(
            f'<h2>{component}</h2>' + _render_component_usage(component)
            for component in _COMPONENT_USAGE_NAMES
        )
    if name == 'AvailableDashRoutes':
        output = []
        for key, heading in [('core', 'Core Routes'), ('zero-trust', 'Zero Trust Routes')]:
            output.append(f'<h3>{heading}</h3><ul>')
            for route in _DASH_ROUTES.get(key, []):
                label = ' > '.join([*(route.get('parent') or []), str(route.get('name') or '')])
                example = f'<DashButton url="{route.get("deeplink", "")}" />'
                output.append(f'<li><strong>{html.escape(label)}</strong><pre><code class="language-mdx">{html.escape(example)}</code></pre></li>')
            output.append('</ul>')
        return ''.join(output)
    if name == 'CodeSnippets':
        providers = [
            ('openai', 'gpt-5.2'),
            ('anthropic', 'claude-4-5-sonnet'),
            ('google', 'gemini-2.5-pro'),
            ('grok', 'grok-4'),
            ('dynamic', 'customer-support'),
            ('workers-ai', '@cf/meta/llama-3.3-70b-instruct-fp8-fast'),
        ]
        variants = 4 if _clean_attr(at.get('forceClient')) == 'aisdk' else 8
        snippets = []
        for provider, model in providers:
            for variant in range(variants):
                code = (
                    "import { createAiGateway } from 'ai-gateway-provider';\n"
                    'import { generateText } from "ai";\n\n'
                    'const aigateway = createAiGateway({ accountId: "{CLOUDFLARE_ACCOUNT_ID}", '
                    'gateway: "{GATEWAY_NAME}", apiKey: "{CF_AIG_TOKEN}" });\n'
                    f'const response = await generateText({{ model: aigateway("{provider}/{model}"), '
                    'prompt: "What is Cloudflare?" });\n'
                    f'// Authentication example {variant + 1}'
                )
                snippets.append('<pre><code class="language-javascript">' +
                                html.escape(code) + '</code></pre>')
        return '<div class="aig-code-example-container">' + ''.join(snippets) + '</div>'
    if name == 'BaseSchemaProperties':
        properties = {
            'banner': 'Displays a Banner on the current docs page.',
            'canonical': 'A canonical URL or path to set as the link rel canonical in the page head, overriding the default derived from the page URL.',
            'difficulty': 'Difficulty is displayed as a column in the ListTutorials component.',
            'external_link': 'Path to another page in our docs or elsewhere. Used to add a crosslink entry to the lefthand navigation sidebar.',
            'feedback': 'Whether to show the FeedbackPrompt on the page, defaults to true.',
            'hideChildren': 'Renders this group as a single link on the sidebar, to the index page.',
            'noindex': 'If true, this property adds a noindex declaration to the page, which tells internal and external search crawlers to ignore this page.',
            'pcx_content_type': 'The purpose of the page, defined through specific pages in Content strategy.',
            'products': 'The names of related directory entries according to their file name in src/content/directory.',
            'release_notes_file_name': 'Required for the ProductReleaseNotes component.',
            'reviewed': 'A YYYY-MM-DD value that signals when the page was last explicitly reviewed from beginning to end.',
            'sidebar': 'Controls the label, order, visibility, badge, attributes, and group shown in the navigation sidebar.',
            'styleGuide': 'Used by style guide component documentation to display usage counts directly on the component page.',
            'summary': 'Renders a summary description directly below the page title.',
            'tags': 'A group of related keywords relating to the purpose of the page.',
        }
        return ''.join(f'<h3>{property_name}</h3><p><strong>Type:</strong> configuration value <span class="nb-metainfo">optional</span></p><p><strong>Description:</strong> {html.escape(description)}</p>'
                       for property_name, description in properties.items())
    if name == 'AgentHeader':
        slug = _clean_attr(at.get('slug'))
        agent = next((item for item in _AGENTS if item.get('slug') == slug), {})
        agent_name = str(agent.get('name') or slug.replace('-', ' ').title())
        description = str(agent.get('description') or _CURRENT_METADATA.get('description', ''))
        return f'<header><h1 data-page-title>{html.escape(agent_name)} + Cloudflare</h1><p>{html.escape(description)}</p></header>'
    if name == 'RandomPrompt':
        return '<pre><code class="language-txt">Help me build and deploy this project on Cloudflare. Review the configuration, implement the required changes, run tests, and explain the result.</code></pre>'
    if name == 'ExamplePromptsList':
        prompts = [
            'Build an AI chat agent using the Cloudflare Agents SDK with persistent conversation history stored in D1.',
            'Create a RAG pipeline using Vectorize and Workers AI to answer questions over my documentation.',
            'Set up AI Gateway to route requests across OpenAI and Workers AI with automatic fallback and cost tracking.',
            'Deploy a full-stack React app to Cloudflare Pages with a Workers API backend and D1 database.',
            'Add real-time collaboration to my app using Durable Objects with WebSocket hibernation.',
        ]
        return '<div class="agent-example-prompts">' + ''.join(
            f'<pre><code class="language-txt">{html.escape(prompt)}</code></pre>'
            for prompt in prompts) + '</div>'
    if name == 'PlatformAccess':
        return ('<div><p>Expand any section to learn more.</p>'
                '<strong>Cloudflare Skills</strong><p>Persistent platform context that teaches the agent how Cloudflare works.</p><p>Skills are instructions the agent loads on demand. The <a href="https://github.com/cloudflare/skills">cloudflare/skills</a> bundle covers every layer of the platform, so the agent knows your conventions without you re-explaining them.</p>'
                '<strong>MCP servers</strong><p>Live access to the Cloudflare API, docs, and observability.</p><p>MCP servers provide typed tools to call into Cloudflare at runtime. Code Mode covers the entire Cloudflare API, with more than 2,500 endpoints in about 1,000 tokens. Focused domain-specific servers are hosted in the <a href="https://github.com/cloudflare/mcp-server-cloudflare">Cloudflare MCP server repository</a>.</p>'
                '<strong>Wrangler CLI</strong><p>Local dev, deploys, and Workers-specific commands.</p><p>Use <a href="/workers/wrangler/">Wrangler</a> for local development, deploys, and commands such as <code>wrangler d1 migrations apply</code> or <code>wrangler tail</code>. The Wrangler Skill teaches the agent when to use it.</p><p><strong>What’s next:</strong> The unified <code>cf</code> CLI is in technical preview. Try it with <code>npx cf</code>.</p>'
                '<strong>Agent-friendly docs</strong><p>Token-efficient references optimized for agents.</p><p>Append <code>/index.md</code> to any Cloudflare docs URL for clean Markdown. Every top-level product also has an <code>llms.txt</code> index sized for a context window.</p><ul><li><a href="/llms.txt">Cloudflare product directory</a></li><li><a href="/workers/llms.txt">Workers index</a></li><li><a href="/agents/llms.txt">Agents index</a></li><li><a href="/r2/llms.txt">R2 index</a></li><li><a href="/d1/llms.txt">D1 index</a></li></ul></div>')
    if name == 'OtherAgents':
        current = _CURRENT_METADATA.get('_route', '').strip('/').split('/')[-1]
        cards = []
        for agent in _AGENTS:
            if agent.get('slug') == current:
                continue
            name_text = str(agent.get('name') or '')
            slug = str(agent.get('slug') or '')
            cards.append(f'<article><h3>{html.escape(name_text)}</h3><p>{html.escape(str(agent.get("description") or ""))}</p><a href="/agent-setup/{html.escape(slug, quote=True)}/">Use {html.escape(name_text)} with Cloudflare</a></article>')
        return '<div class="nb-card-grid">' + ''.join(cards) + '</div>'
    if name == 'BuildAgentsCallout':
        cards = [
            ('Agents SDK', '/agents/', 'Stateful AI agents with state, scheduling, RPC, email, streaming chat, and token-efficient tool use.'),
            ('Build an MCP server', '/agents/model-context-protocol/', 'Ship a remote MCP server on Workers with OAuth, durable state, and streamable HTTP transport.'),
            ('Workers AI', '/workers-ai/', 'Run open-source LLMs, embedding models, and image models at the edge as your agent model provider.'),
            ('Worker Loader', '/workers/runtime-apis/bindings/worker-loader/', 'Load user-generated code into isolated Workers on demand for a secure sandbox.'),
        ]
        return ('<div><p>Cloudflare is not just a deploy target for agents, it is a full stack for building your own.</p>' +
                ''.join(f'<article><h3>{html.escape(title)}</h3><p>{html.escape(description)}</p><a href="{href}">Learn more</a></article>'
                        for title, href, description in cards) + '</div>')
    if name == 'RTKUIComponentGrid':
        gallery = (_UPSTREAM_ROOT / 'src/assets/images/realtime/realtimekit/web/components-gallery'
                   if _UPSTREAM_ROOT else None)
        images = sorted(gallery.glob('*.svg')) if gallery and gallery.is_dir() else []
        cards = []
        for image in images:
            component = image.stem
            label = component.removeprefix('rtk-').replace('-', ' ').title()
            cards.append(
                f'<a href="/realtime/realtimekit/ui-kit/api-reference/core/{component}/">'
                f'<img src="/assets/upstream/images/realtime/realtimekit/web/components-gallery/{image.name}" '
                f'alt="{html.escape(label, quote=True)}"><code>{html.escape(component.replace("-", ""))}</code></a>')
        return ('<div class="component-gallery"><h2>Component gallery</h2>'
                '<p>Search through reusable components for building rich interactive views. Basic components are small elements, UI components combine multiple controls, composite components are feature-rich building blocks, and screen components provide complete full views for mobile.</p>'
                '<h2>Basic components</h2><h2>UI components</h2>'
                '<h2>Composite components</h2><h2>Screen components</h2>' +
                ''.join(cards) + '</div>')
    if name in {'FAQItem', 'TroubleshootingItem'}:
        question = _clean_attr(at.get('question') or at.get('title') or name)
        return f'<details><summary>{html.escape(question)}</summary>{wrapped}</details>'
    if name == 'ResourcesBySelector':
        return _render_resources(at)
    if name == 'PagesBuildPreset':
        framework = _clean_attr(at.get('framework'))
        preset = _PAGES_BUILD_PRESETS.get(framework)
        if not preset:
            raise ValueError(f'PagesBuildPreset: unknown framework {framework}')
        return ('<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody>'
                '<tr><td>Production branch</td><td><code>main</code></td></tr>'
                f'<tr><td>Build command</td><td><code>{html.escape(str(preset.get("build_command", "")))}</code></td></tr>'
                f'<tr><td>Build directory</td><td><code>{html.escape(str(preset.get("build_output_directory", "")))}</code></td></tr>'
                '</tbody></table>')
    if name in {'PagesBuildEnvironment', 'PagesBuildEnvironmentLanguages',
                'PagesBuildEnvironmentTools'}:
        tables = []
        for version in reversed(_PAGES_BUILD_ENVIRONMENTS):
            if name == 'PagesBuildEnvironment':
                environment = version.get('build_environment') or {}
                if not environment:
                    continue
                rows = [('Build environment', environment.get('operating_system', '')),
                        ('Architecture', environment.get('architecture', ''))]
                headings = ('Property', 'Value')
            else:
                key = 'languages' if name.endswith('Languages') else 'tools'
                values = version.get(key) or []
                rows = [(item.get('name', ''), item.get('default', ''),
                         item.get('supported', ''), item.get('environment_variable', ''),
                         ', '.join(item.get('file') or [])) for item in values]
                headings = ('Tool', 'Default version', 'Supported versions',
                            'Environment variable', 'File')
            head = ''.join(f'<th>{html.escape(str(value))}</th>' for value in headings)
            body_rows = ''.join('<tr>' + ''.join(f'<td>{html.escape(str(value))}</td>' for value in row) + '</tr>'
                                for row in rows)
            tables.append(f'<section class="nb-tab-panel" data-nb-tab-label="{html.escape(str(version.get("id", "")), quote=True)}"><table><thead><tr>{head}</tr></thead><tbody>{body_rows}</tbody></table></section>')
        return '<div class="nb-tabs" data-nb-tabs>' + ''.join(tables) + '</div>'
    if name == 'Glossary':
        return _render_glossary(_clean_attr(at.get('product')))
    if name == 'GlossaryDefinition':
        return _render_glossary_definition(
            _clean_attr(at.get('term')), at.get('prepend') or '')
    if name == 'RuleID':
        rule_id = _clean_attr(at.get('id'))
        return f'<code class="nb-rule-id" title="{html.escape(rule_id, quote=True)}">{html.escape(rule_id[-8:])}</code>'
    if name == 'ListTutorials':
        return _render_tutorials()
    if name == 'ProductReleaseNotes':
        return _render_release_notes()
    if name == 'WranglerNamespace':
        return _render_wrangler_namespace(
            _clean_attr(at.get('namespace')), int(_clean_attr(at.get('headingLevel') or 2)))
    if name == 'WranglerCommand':
        command = _clean_attr(at.get('command'))
        for definitions in _WRANGLER_COMMANDS.values():
            for definition in definitions:
                if str(definition.get('command', '')).removeprefix('wrangler ') == command:
                    return _render_wrangler_definition(
                        definition, int(_clean_attr(at.get('headingLevel') or 2)))
        raise ValueError(f'WranglerCommand: unknown command {command}')
    if name == 'YouTube':
        video_id = html.escape(at.get('id', ''), quote=True)
        label = html.escape(at.get('title') or 'YouTube video', quote=True)
        return f'<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/{video_id}" title="{label}" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>'
    if name == 'Stream':
        video = {}
        file_name = _clean_attr(at.get('file'))
        if file_name:
            video = next((item for item in _VIDEOS
                          if str(item.get('url') or '') == file_name), {})
        video_id = html.escape(str(at.get('id') or video.get('id') or ''), quote=True)
        label = html.escape(str(at.get('title') or video.get('title') or 'Cloudflare Stream video'), quote=True)
        thumbnail_value = at.get('thumbnail') if at.get('thumbnail') is not None else video.get('thumbnail')
        if isinstance(thumbnail_value, dict):
            thumbnail = str(thumbnail_value.get('url') or thumbnail_value.get('timestamp') or '')
        else:
            thumbnail = _clean_attr(thumbnail_value)
        if thumbnail and not thumbnail.startswith(('http://', 'https://')):
            thumbnail = (f'https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/{video_id}/'
                         f'thumbnails/thumbnail.jpg?fit=crop&time={html.escape(thumbnail, quote=True)}')
        if not thumbnail and video_id:
            thumbnail = (f'https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/{video_id}/'
                         'thumbnails/thumbnail.jpg?fit=crop')
        iframe_url = (f'https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/{video_id}/'
                      'iframe?preload=true&amp;letterboxColor=transparent')
        if thumbnail:
            iframe_url += '&amp;poster=' + html.escape(quote(thumbnail, safe=''), quote=True)
        frame = f'<div class="video-frame"><iframe src="{iframe_url}" title="{label}" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>'
        chapters = at.get('chapters') if at.get('chapters') is not None else video.get('chapters')
        if isinstance(chapters, str):
            chapters = _parse_js_literal(chapters)
        if not isinstance(chapters, dict) or not chapters:
            return frame
        items = []
        for chapter_title, timestamp in chapters.items():
            timestamp_text = str(timestamp)
            if ':' in timestamp_text:
                seconds = 0
                for part in timestamp_text.split(':'):
                    try:
                        value = float(part)
                    except ValueError:
                        value = 0
                    seconds = seconds * 60 + value
            else:
                seconds = sum(float(value) * {'h': 3600, 'm': 60, 's': 1}[unit]
                              for value, unit in re.findall(r'(\d+(?:\.\d+)?)\s*([hms])', timestamp_text))
                if not seconds:
                    try:
                        seconds = float(timestamp_text)
                    except ValueError:
                        seconds = 0
            seconds = round(seconds)
            escaped_time = html.escape(timestamp_text, quote=True)
            item_thumbnail = (f'https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/'
                              f'{video_id}/thumbnails/thumbnail.jpg?fit=crop&amp;time={seconds}s')
            items.append(
                f'<li><button type="button" data-video-time="{seconds}">'
                f'<img src="{item_thumbnail}" alt="{html.escape(str(chapter_title), quote=True)}">'
                f'<strong>{html.escape(str(chapter_title))}</strong><span>{escaped_time}</span>'
                f'</button></li>')
        return frame + '<details class="nb-details video-chapters"><summary>Chapters</summary><ul>' + ''.join(items) + '</ul></details>'
    if name == 'Tabs':
        sync = f' data-nb-sync-key="{html.escape(at["syncKey"], quote=True)}"' if at.get('syncKey') else ''
        return f'<div class="nb-tabs" data-nb-tabs{sync}><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>{wrapped}</div></div>'
    if name == 'TabItem':
        label = html.escape(at.get('label', at.get('value', 'Tab')))
        return f'<section class="nb-tab-panel" role="tabpanel" data-nb-tabs-content data-nb-tab-label="{label}">{wrapped}</section>'
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


def _fence_to_html(val):
    """Render a stashed fenced code block to <pre><code> HTML.

    Deterministically closes fences that CommonMark would leave open (a closing
    fence indented more deeply than the opening fence), matching the HTML cmark
    produces for regular fences: language class from the info string, content
    de-indented to the opening fence, HTML-escaped, with a trailing newline."""
    lines = val.split('\n')
    m = FENCE_OPEN.match(lines[0])
    if not m:
        return html.escape(val)
    marker = m.group(1)[0]
    info = lines[0][m.end():].strip()
    lang = info.split()[0] if info else ''
    indent = len(lines[0]) - len(lines[0].lstrip())
    content = list(lines[1:])
    if content and re.match(r'^[ \t]*' + re.escape(marker) + r'{3,}', content[-1]):
        content = content[:-1]
    stripped = []
    for ln in content:
        if ln[:indent].strip() == '' and len(ln) >= indent:
            stripped.append(ln[indent:])
        else:
            stripped.append(ln)
    body = '\n'.join(stripped)
    if not body.endswith('\n'):
        body += '\n'
    cls = f' class="language-{html.escape(lang, quote=True)}"' if lang else ''
    escaped = html.escape(body)
    # Generated-family pages receive one final Nift Markdown pass. Encode
    # line-leading Markdown markers so code comments/frontmatter stay code.
    escaped = re.sub(
        r'(?m)^([ \t]*)([#>*+-])',
        lambda match: match.group(1) + f'&#{ord(match.group(2))};',
        escaped,
    )
    return f'<pre><code{cls}>{escaped}</code></pre>\n'


def restore_code(text, placeholders, render_fences=False):
    for key, val in placeholders.items():
        if render_fences and '\n' in val and FENCE_OPEN.match(val.split('\n')[0]):
            val = _fence_to_html(val)
        text = text.replace(key, val)
    return text


def restore_indented_fences(text, placeholders):
    """Pre-render list-indented fences that Nift's Markdown pass misparses."""
    for key, value in placeholders.items():
        first = value.split('\n', 1)[0]
        if '\n' in value and FENCE_OPEN.match(first) and first[:1].isspace():
            value = _fence_to_html(value)
        text = text.replace(key, value)
    return text


def expand_footnotes(text, prefix=''):
    """Convert one-line GFM footnotes into ordinary linked Markdown."""
    definitions = []
    kept = []
    for line in text.splitlines():
        match = re.match(r'^\[\^([^]]+)\]:\s*(.*)$', line)
        if match:
            definitions.append((match.group(1), match.group(2)))
        else:
            kept.append(line)
    if not definitions:
        return text
    definitions = list(dict.fromkeys(definitions))
    ids = {
        key: 'footnote-' + (f'{prefix}-' if prefix else '') +
             re.sub(r'[^a-z0-9_-]+', '-', key.casefold()).strip('-')
        for key, _ in definitions
    }
    body = '\n'.join(kept)
    body = re.sub(
        r'\[\^([^]]+)\]',
        lambda match: (f'<sup><a href="#{html.escape(ids[match.group(1)], quote=True)}">'
                       f'{html.escape(match.group(1))}</a></sup>'
                       if match.group(1) in ids else match.group(0)),
        body,
    )
    items = '\n'.join(
        f'<li id="{html.escape(ids[key], quote=True)}">{value}</li>'
        for key, value in definitions)
    return body.rstrip() + f'\n\n<section class="footnotes"><h2>Footnotes</h2><ol>{items}</ol></section>\n'


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
    # replacements never shift the positions of still-pending spans. Nested
    # spans (e.g. a :::caution inside a :::note) are already converted by the
    # recursion below; skip them here so stale line indices never double-process
    # a sub-directive after the outer span has replaced those lines.
    spans.sort(key=lambda s: s[1], reverse=True)
    processed = []
    for oi, ci, name, title in spans:
        if any(lo <= oi and ci <= hi for lo, hi in processed):
            continue
        inner = convert_directives('\n'.join(lines[oi + 1:ci]), placeholders)
        inner = reduce_components(inner, 0, placeholders)
        cls = name or 'note'
        head = f'<h3 class="nb-aside-title">{_render_title_inline_code(title, placeholders)}</h3>\n' if title else ''
        inner_markup = _wrap_markup(inner, f':::{cls}')
        block = f'<aside class="nb-aside {html.escape(cls)}">\n{head}{inner_markup}\n</aside>'
        lines = lines[:oi] + block.split('\n') + lines[ci + 1:]
        processed.append((oi, ci))
    return '\n'.join(lines)


def _join_multiline_tags(text):
    """Collapse lowercase HTML tags that span multiple lines onto one line.

    CommonMark type-6 HTML blocks require a complete tag on a single line, so an
    upstream `<a\\n\\thref="..."\\n\\ttarget="_blank">` would otherwise render as
    escaped text. Joining the attribute lines keeps the tag a valid HTML block."""
    def fix(m):
        attrs = re.sub(r'\s*\n\s*', ' ', m.group(2)).strip()
        return f'<{m.group(1)} {attrs}>' if attrs else f'<{m.group(1)}>'
    return _ML_TAG.sub(fix, text)


def render_markdown(text, blocks=True):
    """Render Markdown to HTML with a CommonMark engine, preserving raw HTML.

    When blocks=True, inserts blank lines around block HTML tags so CommonMark
    treats content inside component/directive HTML blocks as renderable Markdown.
    When blocks=False, renders top-level Markdown only (component bodies have
    already been rendered). cmarkgfm is mandatory because passthrough output is
    not a semantically valid CP6 build."""
    cmarkgfm = require_cmarkgfm()
    text = _join_multiline_tags(text)
    text = re.sub(r'(?m)^[ \t]+(?=!\[[^\]]*\]\()', '', text)
    text = re.sub(r'(?m)^[ \t]+(?=</?(?:div|iframe|img|video|br|table|thead|tbody|tr|th|td)\b)', '', text)
    if blocks:
        BLOCK = r'(?:div|section|aside|details|pre|table|ul|ol|dl|blockquote)'
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
    return cmarkgfm.markdown_to_html_with_extensions(
        text, options=flag, extensions=['table', 'strikethrough', 'autolink'])


def add_heading_ids(text):
    """Add deterministic, de-duplicated IDs to rendered article headings."""
    heading_ids = re.findall(r'<h[2-6][^>]*\bid=["\']([^"\']+)', text, re.I)
    used = set(re.findall(r'\bid=["\']([^"\']+)', text, re.I)) - set(heading_ids)

    def replace(match):
        level, attributes, content = match.groups()
        attributes = attributes or ''
        existing = re.search(r'\bid=(["\'])([^"\']+)\1', attributes, re.I)
        if existing and existing.group(2) not in used:
            used.add(existing.group(2))
            return match.group(0)
        label = html.unescape(re.sub(r'<[^>]+>', '', content))
        base = (existing.group(2) if existing else
                re.sub(r'[^a-z0-9]+', '-', label.casefold()).strip('-') or 'section')
        slug = base
        suffix = 1
        while slug in used:
            slug = f'{base}-{suffix}'
            suffix += 1
        used.add(slug)
        if existing:
            attributes = attributes[:existing.start()] + f'id="{slug}"' + attributes[existing.end():]
            return f'<h{level}{attributes}>{content}</h{level}>'
        return f'<h{level}{attributes} id="{slug}">{content}</h{level}>'

    return re.sub(r'<h([2-6])(\s[^>]*)?>(.*?)</h\1>', replace, text, flags=re.I | re.S)


def normalize_article_headings(text):
    """Reserve H1 for the page title supplied by the surrounding template."""
    preserved = {}
    def preserve_page_title(match):
        marker = f'\x00PAGETITLE{len(preserved)}\x00'
        preserved[marker] = match.group(0)
        return marker
    text = re.sub(r'<h1\b[^>]*\bdata-page-title\b[^>]*>[\s\S]*?</h1>',
                  preserve_page_title, text, flags=re.I)
    text = re.sub(r'<h1(\s[^>]*)?>', lambda match: f'<h2{match.group(1) or ""}>', text, flags=re.I)
    text = re.sub(r'</h1>', '</h2>', text, flags=re.I)
    for marker, heading in preserved.items():
        text = text.replace(marker, heading)
    return add_heading_ids(text)


def convert(text, path='<memory>', metadata=None):
    global _BODY_REGISTRY, _CURRENT_PRODUCT, _CURRENT_METADATA, _CODE_CONSTANTS, _RAW_IMPORTS, _ACTIVE_CODE_PLACEHOLDERS
    _BODY_REGISTRY = []
    _CURRENT_METADATA = dict(metadata or {})
    _CODE_CONSTANTS = {}
    _RAW_IMPORTS = {}
    source_path = Path(path)
    if source_path.is_file():
        for raw_import in re.finditer(
                r'^\s*import\s+([A-Za-z_$][\w$]*)\s+from\s+["\']([^"\']+)\?raw["\'];?',
                text, re.M):
            import_source = raw_import.group(2)
            if import_source.startswith('~/') and _UPSTREAM_ROOT:
                imported_path = (_UPSTREAM_ROOT / 'src' / import_source[2:]).resolve()
            else:
                imported_path = (source_path.parent / import_source).resolve()
            if imported_path.is_file():
                _RAW_IMPORTS[raw_import.group(1)] = imported_path.read_text(errors='replace')
            else:
                raise ValueError(f'{path}: unresolved raw import {import_source}')
    for constant in re.finditer(
            r'(?:export\s+)?const\s+(\w+)\s*=\s*(`(?:\\.|[^`])*`|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')\s*;?',
            text, re.S):
        raw_value = constant.group(2)
        _CODE_CONSTANTS[constant.group(1)] = (raw_value[1:-1] if raw_value.startswith('`')
                                               else ast.literal_eval(raw_value))
    path_text = str(path).replace('\\', '/')
    marker = '/src/content/docs/'
    _CURRENT_PRODUCT = path_text.split(marker, 1)[1].split('/', 1)[0] if marker in path_text else ''
    fm = {}
    m = FRONT.match(text)
    if m:
        for line in m.group(1).splitlines():
            if ':' in line and not line.startswith((' ', '\t')):
                fm[line.split(':', 1)[0].strip()] = line.split(':', 1)[1].strip().strip('"\'')
        text = text[m.end():]
    text = expand_render_partials(text)
    text = re.sub(r'(\b(?:href|src))=\{`([^`]*)`\}',
                  lambda match: f'{match.group(1)}="{match.group(2)}"', text)
    raw = text
    imported = imported_component_names(raw)
    text = normalize_markdown_heading_lines(text, demote_h1=True)
    text, placeholders = protect_code(text)
    text = expand_footnotes(text)
    _ACTIVE_CODE_PLACEHOLDERS = placeholders
    text = _resolve_asset_imports(text)
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
    text = restore_code(text, placeholders, render_fences=True)
    # Render top-level Markdown to HTML with a CommonMark engine before
    # materializing body references. Body markers (\x01BODY{n}\x02) survive the
    # render and are replaced with @markup("md", path) afterwards, so Nift
    # renders each body exactly once. The page is then inserted via the docs
    # template's @content without an outer markdown pass, which would otherwise
    # re-parse already-rendered body HTML and split hostile fenced code.
    text = _materialize_gfm_tables(text)
    text = render_markdown(text, blocks=True)
    text = normalize_article_headings(text)
    if not text.strip() and fm.get('description'):
        text = f'<p>{html.escape(fm["description"])}</p>\n'
    # Materialize @markup body references: write each component/directive body to
    # a Markdown file under content/.markup/bodies/ and reference it via the
    # file-based @markup("md", path) form (avoids find_balanced fragility).
    text = _materialize_bodies(text, placeholders)
    text = _compact_pre_blocks(text)
    # Source-style '~/assets/...' references resolve to the staged upstream
    # asset tree at /assets/upstream/ in the generated site.
    text = _rewrite_asset_refs(text)
    text = re.sub(r'<iframe\b(?![^>]*\btitle\s*=)([^>]*)>',
                  r'<iframe title="Embedded media"\1>', text, flags=re.I)
    text = re.sub(r'<pre\b(?![^>]*\btabindex\s*=)([^>]*)>',
                  r'<pre tabindex="0"\1>', text, flags=re.I)
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
    require_cmarkgfm()
    configure_body_output(out / '.markup/bodies', reset=True)
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
