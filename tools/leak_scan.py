#!/usr/bin/env python3
"""CP6B post-build conversion-leakage scan.

Searches generated HTML for literal source syntax that should have been rendered
semantically, and classifies findings as REAL leakage versus INTENTIONAL
code/prose text. The correctness gate is the REAL-leakage count; intentional
prose/code is reported separately so the scanner is never made green by broadly
suppressing classes.

Classification rules (narrow, corpus-justified):

REAL leakage (must be fixed):
  - mdx-directive        : literal ':::note[...]' / ':::caution[...]' etc.
  - mdx-bare-directive   : literal ':::' opening a directive block
  - mdx-import           : 'import ... from "..."' outside a code element
  - component-open       : a known MDX component tag (Steps, Tabs, Aside, ...)
                           rendered literally instead of as semantic HTML
  - escaped-html         : '&lt;div' / '&lt;p' / '&lt;a' from over-escaped HTML

INTENTIONAL (not leakage; must remain in output):
  - prose-placeholder    : '<UPPER_SNAKE>' such as <CF_AIG_TOKEN>, <API_TOKEN>,
                           <DISPATCH_NAMESPACE>, <ACCOUNT_ID> (literal prose)
  - ts-type-name         : TypeScript/response type tokens like <Response>,
                           <Environment>, <Schedule<T>> that are inline text
  - code-import          : 'import ...' inside <pre>/<code> (code examples)
  - code-placeholder     : markdown/fences inside <pre>/<code> (already rendered
                           by the code highlighter)
"""
import re, sys, json
from pathlib import Path

KNOWN_COMPONENTS = {
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
    'SubtractIPCalculator', 'Stream', 'RSSButton', 'LinkTitleCard',
}

UPPER_SNAKE = re.compile(r'<[A-Z][A-Z0-9_]{2,}>')

REAL = {
    'mdx-directive': re.compile(r':::(?:note|caution|tip|warning|info)\['),
    'mdx-bare-directive': re.compile(r'^\s*:::\s*$', re.M),
    'mdx-import': re.compile(r'^\s*(?:import|export)\s+[\w{*].*?\bfrom\s+["\']', re.M),
    'component-open': re.compile(r'<(Steps|Tabs|TabItem|Aside|Details|Card|CardGrid|'
                                 r'LinkCard|LinkTitleCard|ListCard|TypeScriptExample|'
                                 r'WranglerConfig|PackageManagers|FAQList|FAQItem|'
                                 r'TroubleshootingList|TroubleshootingItem|FileTree|'
                                 r'Steps)\b'),
    'escaped-html': re.compile(r'&lt;(div|section|aside|details|p|a|h[1-6]|pre|code)\b'),
}

INTENTIONAL = {
    'prose-placeholder': UPPER_SNAKE,
    'ts-type-name': re.compile(r'<(Response|Environment|Request|Schedule|State|T)\b'),
    'code-import': re.compile(r'^\s*(?:import|export)\s+[\w{*].*?\bfrom\s+["\']', re.M),
    'code-fence': re.compile(r'^```', re.M),
}


def strip_code(html):
    """Remove <pre>/<code> regions (tolerating unclosed tags)."""
    def remove_regions(s, tag):
        out = []
        i = 0
        n = len(s)
        while i < n:
            m = re.search(r'<' + tag + r'[\s>]', s[i:])
            if not m:
                out.append(s[i:])
                break
            start = i + m.start()
            out.append(s[i:start])
            close = re.search(r'</' + tag + r'>', s[start:])
            if close:
                i = start + close.end()
            else:
                i = n
        return ''.join(out)
    html = remove_regions(html, 'pre')
    html = remove_regions(html, 'code')
    return html


def scan(html):
    """Return {'real': {...}, 'intentional': {...}} for one html doc."""
    plain = strip_code(html)  # for REAL leakage: code removed
    real = {}
    for name, rx in REAL.items():
        ms = list(rx.finditer(plain))
        if ms:
            real[name] = [m.group(0)[:70] for m in ms[:3]]
    # INTENTIONAL
    intentional = {}
    full = html
    for name, rx in INTENTIONAL.items():
        if name == 'code-import':
            ms = []
            for cm in re.finditer(r'<pre>[\s\S]*?</pre>|<code>[\s\S]*?</code>', full):
                ms.extend(rx.finditer(cm.group(0)))
        else:
            ms = list(rx.finditer(full))
        if ms:
            intentional[name] = len(ms)
    return {'real': real, 'intentional': intentional}


def main():
    pub = Path(sys.argv[1] if len(sys.argv) > 1 else "public")
    real_total = {}
    intentional_total = {}
    real_files = set()
    real_examples = {}
    for f in sorted(pub.rglob('*.html')):
        html = f.read_text(errors='ignore')
        res = scan(html)
        for name, ex in res['real'].items():
            real_total[name] = real_total.get(name, 0) + len(ex)
            real_files.add(name)
            real_examples.setdefault(name, []).append((str(f.relative_to(pub)), ex[0]))
        for name, cnt in res['intentional'].items():
            intentional_total[name] = intentional_total.get(name, 0) + cnt
    print(json.dumps({
        'scanned_html': sum(1 for _ in pub.rglob('*.html')),
        'REAL_leakage': real_total,
        'REAL_leakage_files_affected': sorted(real_files),
        'REAL_leakage_examples': {k: v[:3] for k, v in real_examples.items()},
        'INTENTIONAL_text': intentional_total,
    }, indent=2))


if __name__ == '__main__':
    main()