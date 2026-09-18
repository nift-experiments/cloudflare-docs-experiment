#!/usr/bin/env python3
"""CP6B corpus matrix: characterize mixed Markdown/component nesting across the
frozen Cloudflare docs corpus (pinned bc2bdaee).

Outputs a machine-readable JSON matrix of how often each nesting combination
occurs in real source, so the rendering architecture is designed from corpus
evidence rather than isolated fixtures.
"""
import argparse, json, re, sys
from pathlib import Path

TAG_START = re.compile(r'<([A-Z][A-Za-z0-9_.]*)\b')
TAG_CLOSE = re.compile(r'</\s*([A-Z][A-Za-z0-9_.]*)\s*>')
FENCE = re.compile(r'^[ \t]*`{3,}[^\n]*\n.*?^[ \t]*`{3,}', re.M | re.S)
INLINE = re.compile(r'`[^`\n]*`')

# Component classes by name (from compatibility/content-model.json where present)
KNOWN_BLOCK = {
    'Steps', 'Step', 'Tabs', 'TabItem', 'Aside', 'Details', 'Card', 'CardGrid',
    'LinkCard', 'LinkTitleCard', 'ListCard', 'FourCardGrid', 'TypeScriptExample',
    'WranglerConfig', 'PackageManagers', 'FAQList', 'FAQItem', 'TroubleshootingList',
    'TroubleshootingItem', 'FileTree', 'Code', 'Example', 'Render', 'Feature',
    'Plan', 'Description', 'RelatedProduct', 'Badge', 'InlineBadge', 'Icon',
    'MetaInfo', 'GlossaryTooltip', 'APIRequest', 'DashButton', 'LinkButton',
    'DirectoryListing', 'ProductChangelog', 'ProductReleaseNotes', 'ListTutorials',
    'PublicStats', 'RuleID', 'CURL', 'YouTube', 'Flex', 'Width', 'Markdown',
    'WranglerCommand', 'WranglerNamespace', 'AnchorHeading', 'ResourcesBySelector',
    'CompatibilityFlags', 'TunnelCalculator', 'Glossary', 'GlossaryDefinition',
    'Example', 'SubtractIPCalculator', 'Stream', 'RSSButton',
}


def strip_code(s):
    s = FENCE.sub('', s)
    s = INLINE.sub('', s)
    return s


def scan(text):
    """Walk the doc, tracking component nesting and markdown signals.

    Returns a dict of nesting-pattern counts and per-component markdown/code
    presence tallies."""
    i = 0
    n = len(text)
    stack = []  # stack of open component names
    code_in = {}          # component name -> bool (fenced code inside)
    md_in = {}            # component name -> bool (bold/link/heading inside)
    list_in = {}          # component name -> bool (list marker inside)
    directive_in = {}     # component name -> bool (::: directive inside)
    nested = {}           # component name -> set of component names seen inside
    stack_snapshot = []   # snapshot of stack when a nested component opens
    while i < n:
        c = text[i]
        # directives
        if c == ':' and text.startswith(':::', i):
            # directive line
            if stack:
                directive_in[stack[-1]] = True
            # skip to end of line
            nl = text.find('\n', i)
            i = nl + 1 if nl >= 0 else n
            continue
        if c == '<':
            cm = TAG_START.match(text, i)
            if cm:
                name = cm.group(1)
                j = cm.end()
                quote = None
                brace = 0
                while j < n:
                    ch = text[j]
                    if quote:
                        if ch == quote:
                            quote = None
                    elif ch in ('"', "'"):
                        quote = ch
                    elif ch == '{':
                        brace += 1
                    elif ch == '}':
                        brace -= 1
                    elif ch == '>' and brace == 0:
                        break
                    j += 1
                self_close = bool(re.search(r'/\s*>$', text[cm.start():j + 1]))
                if name in KNOWN_BLOCK and not self_close:
                    if stack:
                        nested.setdefault(stack[-1], set()).add(name)
                    stack.append(name)
                    code_in.setdefault(name, False)
                    md_in.setdefault(name, False)
                    list_in.setdefault(name, False)
                    directive_in.setdefault(name, False)
                i = j + 1
                continue
            ccm = TAG_CLOSE.match(text, i)
            if ccm:
                name = ccm.group(1)
                if stack and stack[-1] == name:
                    stack.pop()
                elif name in stack:
                    try:
                        idx = len(stack) - 1 - stack[::-1].index(name)
                        stack = stack[:idx]
                    except ValueError:
                        pass
                i = ccm.end()
                continue
        fm = FENCE.match(text, i)
        if fm and stack:
            for name in stack:
                code_in[name] = True
            i = fm.end()
            continue
        if stack:
            line_start = text.rfind('\n', 0, i) + 1
            nl = text.find('\n', i)
            line = text[line_start:nl] if nl >= 0 else text[line_start:]
            if re.search(r'\*\*[^*]+\*\*', line):
                md_in[stack[-1]] = True
            if re.search(r'^#{1,6}\s', line):
                md_in[stack[-1]] = True
            if re.search(r'^[-*+]\s|^\d+\.\s', line):
                list_in[stack[-1]] = True
        i += 1
    return {'code_in': code_in, 'md_in': md_in, 'list_in': list_in,
            'directive_in': directive_in, 'nested': nested}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('upstream', type=Path)
    a = ap.parse_args()
    docs = a.upstream.resolve() / 'src/content/docs'
    files = sorted([*docs.rglob('*.md'), *docs.rglob('*.mdx')])
    # aggregate: per component, count docs where markdown/code/lists appear inside
    md_counts = {}
    code_counts = {}
    list_counts = {}
    directive_counts = {}
    nested_counts = {}   # (outer, inner) -> docs
    docs_with_md_inside = 0
    for p in files:
        raw = p.read_text(errors='replace')
        res = scan(raw)
        doc_has_md_inside = False
        for name, has in res['md_in'].items():
            if has:
                md_counts[name] = md_counts.get(name, 0) + 1
                doc_has_md_inside = True
        if doc_has_md_inside:
            docs_with_md_inside += 1
        for name, has in res['code_in'].items():
            if has:
                code_counts[name] = code_counts.get(name, 0) + 1
        for name, has in res['list_in'].items():
            if has:
                list_counts[name] = list_counts.get(name, 0) + 1
        for name, has in res['directive_in'].items():
            if has:
                directive_counts[name] = directive_counts.get(name, 0) + 1
        for outer, inners in res['nested'].items():
            for inner in inners:
                key = (outer, inner)
                nested_counts[key] = nested_counts.get(key, 0) + 1
    report = {
        'docs': len(files),
        'markdown_inside_component_by_component': dict(sorted(md_counts.items(), key=lambda x: -x[1])),
        'fenced_code_inside_component_by_component': dict(sorted(code_counts.items(), key=lambda x: -x[1])),
        'list_inside_component_by_component': dict(sorted(list_counts.items(), key=lambda x: -x[1])),
        'directive_inside_component_by_component': dict(sorted(directive_counts.items(), key=lambda x: -x[1])),
        'nested_component_pairs': {f'{a}->{b}': v for (a, b), v in
                                   sorted(nested_counts.items(), key=lambda x: -x[1])},
        'total_docs_with_markdown_inside_component': docs_with_md_inside,
    }
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()