# CP6B — Mixed Markdown/Component Rendering Architecture

Pinned upstream: `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.
Date: 2026-09-19.
Status: **IMPLEMENTED AND CERTIFIED — REAL leakage = 0.**

## 1. Problem

The importer converts MDX components (`<Steps>`, `<Tabs>`, `<Aside>`, directives,
etc.) into raw HTML *before* the CommonMark/Markup++ pass. CommonMark treats raw HTML
blocks as opaque: Markdown inside them (`**bold**`, `` `code` ``, fences, lists,
links) is **not parsed**, so source syntax leaks literally into rendered HTML.

The post-build leak scan (`tools/leak_scan.py`) classifies REAL leakage separately
from INTENTIONAL source-looking text. At the start of CP6B the refined scanner
reported **97 REAL** findings; the target is **REAL leakage = 0**.

## 2. Final architecture

The importer emits component/directive bodies as **file-based Nift
`@markup("md", "content/.markup/bodies/N.md")` references** (14,755 body files),
and the top-level Markdown is rendered by the importer itself before materializing
those references. The docs template is `@content` (no outer CommonMark pass).

Pipeline (`tools/import_cloudflare.py`, `convert()`):

1. Front matter stripped; component/directive imports removed; code protected as
   placeholders.
2. Directives (`:::` blocks) converted to `<aside>` shells with body markers;
   components reduced to HTML shells with body markers. Nested spans are
   processed once (inner directives are handled by recursion, never by stale
   top-level line indices).
3. Fenced code blocks are pre-rendered to `<pre><code class="language-...">`
   deterministically, so an irregular closing fence (indented deeper than the
   opener) cannot leave a fence open and swallow following component HTML.
4. Top-level Markdown is rendered with cmarkgfm (`render_markdown`, blocks=True).
   Body markers (`\x01BODY{n}\x02`) survive the render; `@markup("md", path)`
   references are materialized afterwards.
5. Each body is written to `content/.markup/bodies/N.md` and referenced from its
   parent:
   - **leaf** bodies (no nested references) use `@markup("md", path)` — rendered
     exactly once;
   - **pure-HTML containers** (a composition of component shells and nested body
     references, no own Markdown) use `@input(path)` — templated but not
     re-converted, so Nift never re-parses already-rendered nested HTML (which
     splits hostile fenced code such as Rust `r#"..."#` raw strings or JSX
     containing `</pre>`/`</code>` literals);
   - **mixed** bodies (own Markdown plus nested references) use `@markup`.
6. Source asset references (`~/assets/`, `src/assets/`, `public/...`) are
   rewritten in both the page content and every body file.

The docs template `templates/docs.html` inserts the already-rendered page content
via `@content`. Generated/data families that still emit raw Markdown use
`templates/docs-md.html` (`@markup("md"){@content}`).

## 3. Why file-based `@markup`, not inline `@markup("md"){...}`

The corpus demonstrated that arbitrary real-world Markdown is too hostile to embed
inside an inline `@markup("md"){...}` boundary: Nift's `find_balanced` must reason
about quotes, backticks, irregular fences, braces and code examples, and inline
bodies cannot be parsed deterministically across the corpus. The generated body-file
form keeps Nift responsible for Markdown rendering while giving it a much safer
file boundary. This finding is retained as experiment evidence for future Nift work
on `find_balanced` and `@markup`.

## 4. Correctness classes fixed during certification

Each class was reproduced as a minimal fixture, given a regression test, then fixed
generically (no page-specific exceptions):

| Class | Root cause | Generic fix |
|---|---|---|
| Nested directive reordering | A `:::caution` inside a `:::note` was double-processed with stale line indices | Skip spans contained inside an already-processed outer span |
| Irregular closing fence | A fence closed more indented than its opener is not a CommonMark closer, so it swallowed following component HTML | Pre-render fenced blocks to `<pre><code>` at restore time |
| Multiline HTML tag | A `<a\n\thref=...>` spanning lines is not a type-6 HTML block and renders escaped | Join lowercase multiline tags before rendering |
| Nested-body double conversion | `@markup("md", path)` re-converts already-rendered nested body HTML, splitting hostile code at depth ≥ 3 | Pure-HTML containers referenced via `@input` (no CommonMark pass) |
| Asset refs in bodies | `~/assets/` rewritten only in page content, not body files | Rewrite asset refs in every body during materialization |
| Legacy changelog route structure | Changelog posts served at `/changelog/post/<id>/` but upstream serves `/changelog/<product>/<name>/` | Generate posts at the upstream path; update index/product/group/RSS links |

Additional surface reproduced for fidelity: per-product `/<product>/llms.txt` and
`/llms-full.txt` routes, per-product changelog RSS feeds (`/changelog/rss/<id>.xml`),
and a clean-from-scratch reproduction that recreates all static/data endpoints.

## 5. Final gate results

- **Import**: 6,882/6,882 docs, 0 failures (routes 6,882).
- **Tracked pages**: 9,134 (8,952 previous + 107 per-entry llms.txt + 76 per-product
  llms-full.txt, net of changelog structure and RSS additions).
- **Build**: 9,134/9,134 files, 0 HTML-validation failures.
- **Routes**: 0 missing expected routes.
- **Tests**: 31/31 pass (25 original + 6 new root-cause regression tests).
- **Leak scan**: **REAL = 0**. INTENTIONAL: code-fence 187, code-import 62,
  prose-placeholder 19, ts-type-name 2 — all defensible.
- **Static/data endpoints** (survive clean-from-scratch): robots.txt, _headers,
  __redirects, shell assets, changelog RSS index + 75 product feeds,
  compatibility-flags.json, Pages build-configuration.json + language-support
  JSON, llms.txt + per-product llms.txt, llms-full.txt + per-product llms-full.txt.

## 6. Excluded families (documented)

- **API reference** (`/api/...`): same-origin sibling application with fetched
  OpenAPI data — cannot be reproduced from the frozen checkout.
- **Logpush datasets** (`/logs/logpush/.../datasets/...`): fetched at build from the
  Logpush API — live data, not in the frozen tree.
- **Proxied Workers AI models** (e.g. `uform-*`): live catalog data.
- **WARP changelog posts** (synthesized from warp-releases YAML): served under
  `/changelog/post/`; supplementary, not frozen-site routes.
- **Broken refs remaining** in the build are all upstream's own dead/legacy links
  (e.g. `/workers/runtime-apis/bindings/mtls/`, `/changelog/<name>/` links missing
  the product prefix) or the documented exclusions above — reproduced faithfully.

## 7. Evidence and artifacts

- `reports/cp6/markdown-component-corpus-matrix.json` — corpus nesting matrix.
- `reports/cp6/leak-scan-classified.json` — REAL vs INTENTIONAL classification.
- `tools/import_cloudflare.py` — importer (file-based `@markup`/`@input`,
  fence pre-rendering, multiline-tag join, asset rewrite, directive nesting fix).
- `tools/import_corpus.py` — full-corpus orchestrator.
- `tools/generate_families.py` — generated/data families.
- `tests/test_import_cloudflare.py` — 31 regression tests.