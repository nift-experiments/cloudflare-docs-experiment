# CP6B — Mixed Markdown/Component Rendering Architecture Analysis

Pinned upstream: `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.
Date: 2026-09-19.
Status: **ANALYSIS — no implementation yet.** Review before choosing.

## 1. Problem

The importer converts MDX components (`<Steps>`, `<Tabs>`, `<Aside>`, directives,
etc.) into raw HTML *before* the CommonMark/Markup++ pass. CommonMark treats raw HTML
blocks as opaque: Markdown inside them (`**bold**`, `` `code` ``, fences, lists,
links) is **not parsed**, so source syntax leaks literally into rendered HTML.

The post-build leak scan reports ~97 REAL leakage instances (fenced code, inline
code, imports inside component bodies) — all traced to this single root cause. The
remaining ~3,500 `**bold**`/backtick instances are the same defect at scale once the
directive-specific fixes (already done: `:::note[Title]`, bottom-up spans) are
excluded. This is a semantic rendering defect, not visual parity.

## 2. Corpus evidence (what the architecture must support)

`reports/cp6/markdown-component-corpus-matrix.json` (from `tools/corpus_matrix.py`,
6,882 docs):

| Pattern | Occurrences (docs) |
|---|---|
| Markdown inside Steps | 266 |
| Markdown inside TabItem | 228 |
| Markdown inside Details | 82 |
| Markdown inside Example | 82 |
| Markdown inside GlossaryTooltip | 57 |
| Markdown inside Card | 16 |
| Markdown inside Aside (directives) | 8 |
| Fenced code inside Tabs/TabItem | 342/341 |
| Fenced code inside WranglerConfig | 320 |
| Fenced code inside TypeScriptExample | 260 |
| Fenced code inside Details | 104 |
| Fenced code inside Steps | 101 |
| Lists inside Steps/TabItem/Details | 270/215/100 |
| Directives inside TabItem/Steps/Details | 89/30/17 |
| Nested component pairs (Tabs→TabItem) | 536 |
| Nested (TabItem→Steps / TabItem→Details) | 43/32 |
| Nested (Steps→WranglerConfig / Tabs→TSE) | 26/11 |
| Nested FAQList→FAQItem, TroubleshootingList→Item | 9/9 |
| **Total docs with markdown inside a component** | 745 |

`reports/cp6/atmarkup-body-risk.json` (from `tools/brace_risk.py`, 9,382 component
bodies):

- Unbalanced `}` in a component body: **2** (rare; escape or special-case)
- `@` sigil in a body: 816 (all safe — no `@content`/`@markup`/`@input`/`@path`/
  `@if(`/`@for(` etc. anywhere in the corpus; bare `@word` passes through Nift)
- `$[` sigil in a body: **0**
- Risky Nift template sigils in any file: **0**

The corpus requires full general nesting: markdown in components, components in
components, directives in components, components in directives, fences in
components, lists in components, and lists containing components.

## 3. How Markup++/Nift actually work (verified from source)

- `@markup("md"){...}` in a template runs Nift template parsing on the block body
  first, then passes the *result* to `markup::convert` (cmark, CommonMark)
  (`src/Parser.cpp:4846-4990`).
- The docs template is `@markup("md"){@content}`. `@content` inserts the imported
  content (which already contains component HTML). The whole thing then goes
  through cmark **once**.
- cmark's HTML-block rule: content inside a raw HTML block is not markdown-parsed.
- Crucially: **content files are themselves parsed as Nift templates**
  (`src/Parser.cpp:4613`: `parse(content_source, ...)`). So `@markup` works inside
  content files, not just templates.
- Nift's `find_balanced` (which locates the `@markup{...}` body) skips quoted
  strings and backtick code spans, and handles nested braces. It does not skip
  fenced blocks, but balanced braces inside them are fine; only an unbalanced `}`
  is a risk (2 corpus bodies).

## 4. Verified key fact

Content files can contain `@markup("md"){...}` around component bodies. When the
importer emits component HTML as:

```
<div class="nb-steps">
@markup("md"){
1. **Bold step** with `code`.
2. Second.
}
</div>
```

Nift renders the body correctly (list, bold, inline code). Fenced code, nested
components, directives inside components, and deeply nested cases all render
correctly. The outer template `@markup("md"){@content}` still renders top-level
markdown; inner `@markup` bodies are independent CommonMark passes. No
double-rendering occurs (rendered HTML passes through unchanged).

## 5. Candidate architectures

### Option A — Nift `@markup` boundaries emitted by the importer (RECOMMENDED)

The importer continues converting components/directives to HTML, but wraps each
component body (and each directive body) in `@markup("md"){ ... }`. The content
file remains Nift-template source; Nift renders each body's Markdown independently
at build time. The docs template keeps `@markup("md"){@content}` for top-level
Markdown.

- Uses Nift's own, already-correct `@markup` primitive (the "render this component
  body as Markdown" boundary the problem statement hypothesised).
- No cmarkgfm in the importer; no CommonMark HTML-block fighting; no malformed
  nested HTML (the failure that killed the cmarkgfm experiment).
- Deterministic: Nift's renderer is deterministic across the corpus.
- Directives inside components: importer emits `@markup` body with the converted
  `<aside>` nested inside (or converts the directive inside the body first).
- Fenced code inside bodies: emitted verbatim inside `@markup("md"){...}`; Nift's
  `find_balanced` handles balanced braces; the 2 unbalanced-brace bodies are
  escaped (`\}`) or special-cased.
- Cost: the importer's `render()` and `convert_directives` must wrap bodies with
  `@markup("md"){...}`; regression tests for escaping.

Pros: minimal new machinery; reuses Nift's tested Markdown path; general (works for
any component). Cons: importer output is no longer "final HTML" but template source
(acceptable — content already is); must handle the `}` escaping edge case; `@` and
`$[` sigils verified safe.

### Option B — Importer renders bodies with cmarkgfm (attempted, reverted)

Each component body is rendered to HTML in the importer using cmarkgfm before
wrapping in component HTML.

Pros: final HTML output. Cons: produced malformed nested HTML (duplicate
`</code></pre>`) in list+fence cases; caused Nift HTML-validation failures on
several pages; reverted as incorrect. Could be fixed with more careful
per-fragment rendering, but that re-enters heuristic territory the review rejects.

### Option C — New Markup++/Nift primitive for nested Markdown boundaries

Add a Nift/`@markup` feature (e.g. `@markupBody` or an `@markup` mode) that renders
Markdown inside explicit HTML-block boundaries. Investigated: Markup++ is a
single-pass cmark wrapper with no boundary concept. Adding one means either
pre-splitting input around HTML blocks (importer-side logic) or extending cmark
(upstream dependency, large). This could become generally useful Nift
functionality, but it is a Nift-source change requiring a rebuild of the VPS Nift
binary and is more invasive than Option A.

Pros: would be reusable Nift functionality; clean if maintained upstream. Cons:
requires modifying/rebuilding Nift (v4.3.0); larger blast radius; not needed for
this corpus since Option A works with the existing binary.

### Option D — Fully structured intermediate representation (MDX AST)

Build a real MDX→HTML pipeline (parse MDX into an AST, render components and
Markdown bottom-up). This is the "proper" long-term solution but is a large
dedicated toolchain (MDX parser, JSX tokenizer, renderer). Overkill for the finite
Cloudflare construct set, and risks re-implementing a general MDX framework that
the HANDOVER explicitly warns against.

Pros: correct by construction; general. Cons: large; violates "small explicit
compatibility layer" guidance; months of work.

## 6. Recommendation

**Option A: Nift `@markup` boundaries emitted by the importer.**

It is the smallest change that uses Nift's already-correct rendering primitive, is
deterministic, avoids the malformed-HTML failure, needs no Nift rebuild, and
matches the corpus evidence (all required nesting combinations verified working).
It also has a plausible general-Nift story: content files expressing per-region
Markdown rendering is a natural, reusable pattern — a candidate for documenting as
a supported Nift idiom rather than experiment-specific machinery.

Risk to retire before implementation: the 2 unbalanced-brace bodies. Mitigation:
escape `\}` in the `@markup` body (Nift's `find_balanced` handles `\{`...`\}`?
verify) or use a deterministic body-trim for those two files.

## 7. Migration plan (from current pipeline)

1. **Importer `render()` change**: for paired components whose bodies contain
   Markdown, emit `<div class="nb-...">\n@markup("md"){\n<body>\n}\n</div>`.
   Self-closing components unchanged. Inline components (Badge, Icon) unchanged.
2. **`convert_directives` change**: wrap directive bodies in `@markup("md"){...}`
   (title `<h3>` outside the body or as literal text inside).
3. **Nesting**: because Nift parses content as a template, nested components each
   carry their own `@markup` body; inner bodies render independently. Verify
   components-in-directives and directives-in-components both render.
4. **Code/placeholder handling**: keep `protect_code` placeholders for the
   unknown-tag gate and asset rewrites, but do NOT restore fences inside an
   `@markup` body before Nift (Nift must see the real fenced block to render it).
   Adjust restore order accordingly.
5. **Escaping**: escape `\}` for the 2 unbalanced-brace bodies; leave `@`/`$[`
   (verified safe); verify `\@content`-style literal sigils are escaped in bodies
   that contain them (the existing importer already handles `\<`).
6. **Regression tests**: add corpus-derived tests for each matrix row (bold/code/
   fence/list in Steps, Tabs, Aside, Details, cards; directives in components;
   components in directives; nested Tabs→TabItem→Steps; list containing
   components).
7. **Leak gate**: re-run `tools/leak_scan.py`; target REAL leakage → 0 while
   INTENTIONAL prose/code stays classified.
8. **Build**: full 8,631-page Nift build; route verifier 0 missing; leak scan 0
   REAL.

## 8. Corpus/oracle artifacts committed with this analysis

- `reports/cp6/markdown-component-corpus-matrix.json`
- `reports/cp6/atmarkup-body-risk.json`
- `reports/cp6/leak-scan-classified.json`
- `tools/corpus_matrix.py`
- `tools/brace_risk.py`
- `tools/leak_scan.py` (refined classification)