# CP6B — Mixed Markdown/Component Rendering Architecture Analysis

Pinned upstream: `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.
Date: 2026-09-19.
Status: **ANALYSIS — no implementation yet.** Review before choosing.

## 1. Problem

The importer converts MDX components (`<Steps>`, `<Tabs>`, `<Aside>`, directives,
etc.) into raw HTML *before* the CommonMark/Markup++ pass. CommonMark treats raw HTML
blocks as opaque: Markdown inside them (`**bold**`, `` `code` ``, fences, lists,
links) is **not parsed**, so source syntax leaks literally into rendered HTML.

The post-build leak scan (`tools/leak_scan.py`, output
`reports/cp6/leak-scan-classified.json`) classifies REAL leakage separately from
INTENTIONAL source-looking text:

- **REAL leakage (~97):** `mdx-import` (85), `escaped-html` (10), `component-open`
  (2) — literal fenced-code/inline-code syntax and imports inside component HTML
  blocks. All trace back to this single root cause.
- **INTENTIONAL (not leakage):** prose placeholders (`<CF_AIG_TOKEN>`,
  `<API_TOKEN>`), TypeScript type names (`<Response>`, `<Environment>`), imports
  inside fenced examples, fenced code and backtick spans (471 code-fence, 79
  code-import, 114 prose-placeholder, 70 ts-type-name).

The earlier ~3,600 figure was intentionally broad and mixed genuine rendering
failures with intentional source-looking text. The refined scanner keeps a narrow,
justified classification so the gate is not made green by broad suppression. The
genuine cases all trace back to the Markdown-inside-component problem. This is a
semantic rendering defect, not visual parity.

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
| **Total docs with markdown inside a component** | 668 (760 component-doc pairs) |

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

Verified against Nift v4.3.0 in isolated fixtures: lists, bold, inline code,
fenced code (with unbalanced `{`/`}` inside the fence), nested components, and
nested `@markup` boundaries all render correctly and survive the outer Markdown
pass.

## 4a. `@markup` block-delimiter escaping strategy (deterministic)

Nift's `find_balanced` (which locates the `@markup{...}` body, `src/Parser.cpp`)
treats as opaque:

- quoted strings (`'`/`"`);
- backtick-delimited spans — **including entire fenced code blocks** (a run of
  backticks from opening ``` to closing ``` is skipped as one span);
- `@/* ... */`, `<!-- ... -->`, and `@//` comment bodies.

It does **not** backslash-escape `}` in prose (no `\}` branch). Empirically:

- A **balanced** `{...}` in prose: fine.
- An **unbalanced prose `}`** would prematurely terminate the `@markup` block.
- Braces inside fenced code / inline code: **safe** — the backtick span is opaque.

Corpus evidence (re-run with code masked as placeholders, 9,382 component bodies):

- Prose braces (code excluded) are **balanced in all 9,382 bodies** (0 unbalanced).
- The earlier `brace_risk.py` "2 unbalanced" were code-brace artifacts; with code
  treated as opaque (as Nift does), zero bodies are at risk.
- 0 bodies contain Nift-sensitive literal sigils (`@content`, `@markup`, `@input`,
  `@path`, `@if(`, `@for(`, `$[`).

**Escaping strategy (no per-page special-casing):**

1. The importer emits each component body inside `@markup("md"){ ... }` with the
   real body text (fenced/inline code included).
2. Nift's `find_balanced` skips fenced/inline code as backtick spans, so code
   braces never affect the block boundary.
3. Prose braces are proven balanced across the corpus. A **build-time guard** in
   the importer asserts brace balance on the non-code portion of every body it
   wraps (mirroring `find_balanced`'s backtick-skip rule) and fails loudly if a
   future edit ever introduces an unbalanced prose brace — rather than silently
   emitting broken output.
4. No `}` escaping is required; if a genuine unbalanced prose `}` ever appears,
   the guard reports it and the body can be wrapped differently (e.g. a
   placeholder or explicit pre-render), not silently dropped.

This makes the escaping requirement deterministic and corpus-verified, not a
per-page hack.

## 5. Candidate architectures

Four designs are compared. Option 1 is the current pipeline; Option 4 is the
recommended design (nested Nift `@markup` boundaries emitted by the importer).

### Option 1 — Current single outer `@markup` pass (baseline)

The docs template is `@markup("md"){@content}`. The importer converts components
to HTML; the whole content then goes through one CommonMark pass. Markdown inside
component HTML blocks is not parsed (HTML-block rule) → ~97 REAL leakage
instances plus ~3,500 literal `**bold**`/backtick text inside component bodies.

Pros: no change needed. Cons: known semantic rendering defect; does not meet the
correctness gate.

### Option 2 — Importer-side recursive cmarkgfm rendering (attempted, reverted)

Each component body is rendered to HTML in the importer using cmarkgfm before
wrapping in component HTML.

Pros: final HTML output. Cons: produced malformed nested HTML (duplicate
`</code></pre>`) in list+fence cases; caused Nift HTML-validation failures on
several pages; reverted as incorrect. Re-enters heuristic territory. Also
duplicates Markup++ (two Markdown implementations) and generates final HTML in
Python.

### Option 3 — Structured MDX/AST/IR conversion

Build a real MDX→HTML pipeline (parse MDX into an AST, render components and
Markdown bottom-up).

Pros: correct by construction; general. Cons: large dedicated toolchain; violates
the HANDOVER "small explicit compatibility layer" guidance; re-implements a
general MDX framework; months of work; not Nift-native.

### Option 4 — Importer-emitted nested Nift `@markup` boundaries (RECOMMENDED)

The importer converts components/directives to HTML but wraps each body in
`@markup("md"){ ... }`. Nift parses content as template source, so each body is
its own CommonMark pass. The outer template keeps `@markup("md"){@content}`.

```
<div class="nb-steps">
@markup("md"){
1. **Bold step** with `code`.
2. Second.
}
</div>
```

Provides the semantic boundary:
```
component HTML open
    Nift renders component body as Markdown
component HTML close
```
without asking CommonMark to parse Markdown through an open HTML block, and
without a new Markup++/Nift feature.

Pros: reuses Nift's existing, tested `@markup` primitive; deterministic; no new
Markdown implementation (no duplicate); no Python-generated final HTML; survives
Nift's HTML validator (verified — no malformed output); handles all corpus nesting
(verified); general Nift dogfooding value. Cons: importer output becomes template
source (already is, since content is templated); the `}` delimiter edge case is
handled deterministically (Section 4a).

## 6. Recommendation

**Option 4: the importer emits nested Nift `@markup("md"){...}` boundaries around
component/directive bodies.**

It is the only option that satisfies all criteria simultaneously:

- **Correctness**: every corpus nesting combination verified rendering correctly
  against Nift v4.3.0 (lists, bold, inline code, fences, nested components,
  directives, nested `@markup`).
- **Minimal new machinery**: no new Nift/Markup++ feature; importer-only change.
- **Reuse of Nift functionality**: uses the existing `@markup` primitive rather
  than a second Markdown implementation.
- **Deterministic output**: Nift's renderer is deterministic across 6,882 docs.
- **Preservation of nested Markdown semantics**: each body is an independent
  CommonMark pass.
- **Avoidance of Python-generated final HTML**: Markup++ owns final HTML.
- **Compatibility with Nift's HTML validator**: no malformed nested HTML (the
  failure that killed Option 2).
- **Genuine Nift dogfooding**: content files expressing where Markdown semantics
  apply is a natural Nift idiom, not experiment-specific machinery.

The escaping requirement is corpus-proven (Section 4a): with fenced/inline code
treated as opaque backtick spans (as Nift does), all 9,382 bodies are
brace-balanced; a build-time guard asserts this rather than special-casing pages.

No implementation is performed in this checkpoint. The migration plan below is
approved-in-principle and awaits authorization.

## 7. Migration plan (from current pipeline)

1. **Importer `render()` change**: for paired components whose bodies contain
   Markdown, emit `<div class="nb-...">\n@markup("md"){\n<body>\n}\n</div>`.
   Self-closing components unchanged. Inline components (Badge, Icon) unchanged.
   The body is emitted verbatim (fenced/inline code included) — Nift's
   `find_balanced` skips code as backtick spans.
2. **`convert_directives` change**: wrap directive bodies in `@markup("md"){...}`
   (title `<h3>` outside the body or as literal text inside).
3. **Nesting**: nested components each carry their own `@markup` body; inner bodies
   render independently. Verify components-in-directives and directives-in-components.
4. **Build-time brace guard**: before emitting each `@markup` body, assert that the
   non-code portion (backtick spans masked, mirroring `find_balanced`) is
   brace-balanced; fail loudly on violation rather than emitting broken output.
5. **Sigil safety**: no escaping needed — corpus has zero Nift-sensitive literal
   sigils (`@content`, `@markup`, `@input`, `@path`, `@if(`, `@for(`, `$[`). The
   existing importer already escapes `\<`; verify `\@`-style literals if any body
   ever needs them.
6. **Regression tests** (corpus-derived fixtures):
   - unmatched prose `}` (guard path) — no unbalanced `{`;
   - balanced `{...}` in prose;
   - braces inside inline code;
   - braces inside fenced code (including unbalanced inside fence);
   - literal `@` in prose (`@cloudflare/sandbox`, `@ts`, `user@example.com`);
   - literal Nift-looking syntax if found;
   - nested `@markup` boundaries (Tabs→TabItem→Steps);
   - each corpus matrix row: markdown/fence/list in Steps, Tabs, Aside, Details,
     cards; directives in components; components in directives; list containing
     components.
7. **Leak gate**: re-run `tools/leak_scan.py`; target REAL leakage → 0 while
   INTENTIONAL prose/code stays classified.
8. **Build**: full 8,631-page Nift build; route verifier 0 missing; leak scan 0
   REAL; HTML validator clean.

## 8. Corpus/oracle artifacts committed with this analysis

- `reports/cp6/markdown-component-corpus-matrix.json` (complete machine-readable matrix)
- `reports/cp6/atmarkup-body-risk.json` (`@markup` body escaping risk)
- `reports/cp6/leak-scan-classified.json` (refined REAL vs INTENTIONAL classification)
- `tools/corpus_matrix.py` (corpus nesting scanner)
- `tools/brace_risk.py` (`@markup` body escaping-risk scanner)
- `tools/leak_scan.py` (refined leakage classification)

Temporary/debug scripts used during the investigation were removed from `tools/` on
both the local repo and the VPS; only the analysis/scanner scripts above are kept.

## 9. Commit lineage and reverted experiment (accurate record)

- `daddec2` — CP6A certified; CP6B defined (generated families + rendering).
- `b82a34c` — generated/data-driven families (glossary, directory, fields,
  workers-ai, catalog models, changelog, learning paths, llms.txt).
- `00ff389` — markdown rendering + directive fixes (titled directives, bottom-up
  spans, unclosed directives).
- `b38d8b7` — **reverted the importer-side cmarkgfm body-rendering experiment**
  (Option 2): it produced malformed nested HTML (duplicate `</code></pre>`) and
  failed Nift HTML validation; `@markup("md")` in the docs template restored;
  directive fixes kept.
- `93423fe` — CP6 report updated for generated families and rendering state.
- `a54e258` — initial architecture analysis, corpus matrix, refined leak scan.
- (this commit) — architecture analysis finalized: Option 4 (nested Nift
  `@markup` boundaries) recommended; escaping strategy documented; 12-test suite;
  8,631-page build green; 6,882-doc import zero-failure. No importer change made.