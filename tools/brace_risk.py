#!/usr/bin/env python3
"""CP6B: quantify @markup-body escaping risk in the corpus.

Counts component bodies that contain characters which could break Nift's
@markup('md'){...} block parsing if emitted verbatim:
  - a lone unbalanced '}' (would terminate the block early)
  - a literal '@' sigil or '$[' that Nift would try to interpret
  - HTML-comment or quote edge cases
This determines the escaping burden for the importer->@markup migration.
"""
import argparse, json, re, sys
from pathlib import Path

TAG_START = re.compile(r'<([A-Z][A-Za-z0-9_.]*)\b')
TAG_CLOSE = re.compile(r'</\s*([A-Z][A-Za-z0-9_.]*)\s*>')

KNOWN = {
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
    'SubtractIPCalculator', 'Stream', 'RSSButton',
}


def component_bodies(text):
    """Yield (name, body) for each non-self-closing KNOWN component."""
    i = 0
    n = len(text)
    stack = []  # (name, open_pos_of_body)
    while i < n:
        c = text[i]
        if c == '<':
            m = TAG_START.match(text, i)
            if m:
                name = m.group(1)
                j = m.end()
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
                self_close = bool(re.search(r'/\s*>$', text[i:j + 1]))
                if name in KNOWN and not self_close:
                    stack.append((name, j + 1))
                i = j + 1
                continue
            cm = TAG_CLOSE.match(text, i)
            if cm:
                name = cm.group(1)
                if stack and stack[-1][0] == name:
                    _, body_start = stack.pop()
                    yield name, text[body_start:i]
                i = cm.end()
                continue
        i += 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('upstream', type=Path)
    a = ap.parse_args()
    docs = a.upstream.resolve() / 'src/content/docs'
    files = sorted([*docs.rglob('*.md'), *docs.rglob('*.mdx')])
    stats = {
        'bodies_total': 0,
        'bodies_with_unbalanced_brace': 0,
        'bodies_with_at_sigil': 0,
        'bodies_with_dollar_sigil': 0,
        'bodies_with_quote_issues': 0,
        'examples_unbalanced_brace': [],
        'examples_at_sigil': [],
    }
    for p in files:
        raw = p.read_text(errors='replace')
        for name, body in component_bodies(raw):
            stats['bodies_total'] += 1
            # unbalanced brace: count opens/closes outside backtick spans
            brace = 0
            unbalanced = False
            for ch in body:
                if ch == '`':
                    continue
                if ch == '{':
                    brace += 1
                elif ch == '}':
                    brace -= 1
                    if brace < 0:
                        unbalanced = True
                        break
            if unbalanced:
                stats['bodies_with_unbalanced_brace'] += 1
                if len(stats['examples_unbalanced_brace']) < 5:
                    stats['examples_unbalanced_brace'].append(
                        f'{p.relative_to(docs)} <{name}>: {body[:60]!r}')
            if '@' in body:
                stats['bodies_with_at_sigil'] += 1
                if len(stats['examples_at_sigil']) < 5:
                    stats['examples_at_sigil'].append(
                        f'{p.relative_to(docs)} <{name}>: {body[:60]!r}')
            if '$[' in body:
                stats['bodies_with_dollar_sigil'] += 1
    print(json.dumps(stats, indent=2))


if __name__ == '__main__':
    main()