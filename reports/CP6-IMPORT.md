# CP6 — Full-corpus import and route verification report

Pinned upstream: `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.

## Status

**CP6A — ordinary documentation corpus: CERTIFIED.**

**CP6B — complete Cloudflare site surface: CERTIFIED (REAL leakage = 0).**

CP6 is deliberately split: CP6A covers the 6,882 ordinary docs; CP6B covers the
generated/data-driven route families and rendering correctness needed for the
complete frozen site.

- Importer converts **all 6,882 frozen docs** with **zero unknown/unresolved constructs**.
- Nift generates **9,134 tracked pages**, all built successfully on the development VPS.
- Full Nift build succeeds; **all 9,134 `index.html` routes** present with correct
  trailing-slash semantics.
- Route verifier: **missing routes = 0**.
- **Rendering architecture implemented (CP6B):** component/directive bodies are
  emitted as file-based `@markup("md", "content/.markup/bodies/N.md")` references
  (14,755 body files); pure-HTML containers use `@input` so Nift never re-converts
  already-rendered nested HTML; top-level Markdown is rendered by the importer and
  inserted via the docs template's `@content`. **REAL rendering leakage = 0.**
- Development-VPS build measurements (g6-standard-1, 1 vCPU / 2 GB, Nift v4.3.0):
  clean build ~18-27 s wall, peak RSS ~66 MB. **These are development observations,
  not comparable to the frozen Astro baseline** (see HANDOVER).

## CP6B status — generated families and rendering

**Generated families:** `tools/generate_families.py` reads the frozen collections and
emits Nift content+tracked entries. Implemented: glossary, directory, field catalog,
Workers AI legacy models, catalog models, changelog (posts + paginated index + product
+ product-group pages), learning paths, `llms.txt` + per-product `llms.txt`,
`llms-full.txt` + per-product `llms-full.txt`, videos, agent-setup, synthesized
WARP-release changelog posts, compatibility-flags.json, changelog RSS index + per-product
feeds, and Pages JSON endpoints. These add 2,251 tracked pages (6,883 → 9,134), all built.

**Rendering correctness — certified:** the importer converts titled directives
(`:::note[Title]` → `<aside>` with title), processes directive spans bottom-up (fixing
dropped component closing tags), auto-closes unclosed directives, and emits
component/directive bodies as **file-based `@markup("md", path)` boundaries**, so Nift
renders each body's Markdown directly (no find_balanced fragility). Conversion of **all
6,882 docs remains zero-failure**. `tools/leak_scan.py` confirms: **REAL rendering
leakage = 0**. INTENTIONAL code/prose findings remain classified (code-fence 187,
code-import 62, prose-placeholder 19, ts-type-name 2). The correctness classes fixed
during certification (nested-directive reordering, irregular closing fences, multiline
HTML tags, nested-body double conversion, asset refs in bodies, legacy changelog route
structure) each have a regression test and a generic fix — see
`reports/CP6B-RENDERING-ARCHITECTURE.md`.

**Architecture:** `reports/CP6B-RENDERING-ARCHITECTURE.md` documents the final design:
file-based `@markup("md", path)` for bodies, `@input` for pure-HTML containers,
importer-rendered top-level Markdown, and the docs template `@content`. The file form
is used rather than inline `@markup("md"){...}` because Nift's `find_balanced` cannot
deterministically parse arbitrary Markdown bodies inline (apostrophes, stray backticks,
irregular fences) — a finding retained as evidence for future Nift work. Corpus matrix
and escaping-risk evidence: `reports/cp6/markdown-component-corpus-matrix.json`,
`reports/cp6/atmarkup-body-risk.json`.

## Generated/data-driven families (G6 findings)

The 6,882 ordinary docs represent the `src/content/docs` corpus. The upstream site
also serves generated families from other content collections and Astro dynamic
routes. Each is recorded below with its data source and route contract.

| Family | Data source (frozen checkout) | Files | Route pattern | Status |
|---|---|---|---|---|
| API reference | OpenAPI spec (fetched by `bin/fetch-openapi.ts`) | n/a | `/api/resources/...` | **External sibling app** — documented, not generated (same-origin app outside the docs build) |
| Changelog | `src/content/changelog/` | 1,180 | `/changelog/<product>/<name>/`, `/changelog/`, `/changelog/product/<id>/`, `/changelog/product-group/<slug>/` | **Generated** |
| Glossary | `src/content/glossary/` | 35 | `/glossary/` | **Generated** |
| Directory | `src/content/directory/` | 188 | `/directory/` | **Generated** |
| Learning paths | `src/content/learning-paths/` | 20 | `/learning-paths/<slug>/` | **Generated** |
| Workers AI models | `src/content/workers-ai-models/` | 65 | `/workers-ai/models/<short-slug>/` | **Generated** |
| AI model catalog | `src/content/catalog-models/` | 161 | `/ai/models/<model_id>/` | **Generated** |
| Fields catalog | `src/content/fields/` | 1 | `/ruleset-engine/rules-language/fields/reference/<name>/` (176) | **Generated** |
| llms.txt | `src/content/directory/` + docs | n/a | `/llms.txt`, `/<product>/llms.txt`, `/llms-full.txt`, `/<product>/llms-full.txt` | **Generated** |
| Compatibility flags | `src/content/compatibility-flags/` | 125 | `/workers/platform/compatibility-flags.json` | **Generated** (124 flags) |
| WARP releases | `src/content/warp-releases/` | 303 | synthesized changelog posts under `/changelog/post/<date>-warp-.../` | **Generated** (292 synthesized) |
| Release notes | `src/content/release-notes/` | 43 | `/changelog/...` | **External collection** — feeds changelog RSS; recorded |
| Dash routes | `src/content/dash-routes/` | 3 | `/api/operations/...` | **External sibling app** — same-origin app outside the docs build |
| Page build env | `src/content/pages-build-environment/` | 3 | `/pages/platform/language-support-and-tools.json` | **Generated** (3 versions) |
| Pages presets | `src/content/pages-framework-presets/` | 1 | `/pages/platform/build-configuration.json` | **Generated** (28 presets) |
| Notifications | `src/content/notifications/` | 1 | `/notifications/...` | **External collection** — consumes an email/RSS index, no standalone route |
| Agent setup | `src/content/agent-setup/` + `src/pages/agent-setup/` | 2 | `/agent-setup/` (prompt, tracing) | **Generated** |
| Videos | `src/content/stream/` + `src/pages/videos/` | 30 | `/videos/<url>/` | **Generated** |
| RSS | `src/content/changelog/` | n/a | `/changelog/rss/index.xml` + `<product>.xml` (76) | **Generated** |
| robots.txt/_headers/redirects | upstream `public/` | n/a | `/robots.txt`, `/_headers`, `/__redirects` | **Generated** (copied static) |
| Sitemap | generated | n/a | `/sitemap-index.xml` | **Not yet generated** — derived from tracked routes; low value for a fidelity gate |
| Logpush datasets | fetched at build (`bin/fetch-logpush-datasets.ts`) | n/a | `/logs/logpush/...` | **Fetched live data** — not in frozen tree |
| API reference | OpenAPI spec (fetched by `bin/fetch-openapi.ts`) | n/a | `/api/resources/...` | **External sibling app** — documented, not generated |
| Partials (reusable) | `src/content/partials/` | 1,366 | — (included in docs) | **Used via CP5 Render placeholder** |

### Verifier status for generated families

The route verifier (`tools/verify_routes.py`) reports **0 missing expected routes**.
The remaining "broken" local references (~1,860) are links from ordinary docs and
generated pages to documented exclusions and to upstream's own dead/legacy links
(reproduced faithfully):

- `/api/*`: ~1,585 (external sibling application — documented)
- `/logs/logpush/.../datasets/...`: ~136 (logpush datasets, fetched at build)
- `/workers-ai/models/uform-*` etc.: 21 (live/proxied model data, not in frozen tree)
- Upstream dead links: `/workers/runtime-apis/bindings/mtls/`, `/containers/...`,
  `/realtime/realtimekit/...`, `/changelog/<name>/` links missing the product prefix,
  legacy `/changelog/post/` links inside upstream changelog post bodies, etc.

Each remaining family is classified (frozen-committed data / pinned external /
live-fetched / external-sibling / upstream-stale) in the family table above; the
verifier is not made green by excluding known generated families.

### G6 decision

**CP6A (ordinary docs) is certified.** The 6,882-document corpus is fully imported,
built and route-verified. **CP6B is certified.** Generated families with committed
data (changelog, glossary, directory, fields, Workers AI models, catalog models,
learning paths, llms.txt/llms-full.txt, RSS, compatibility flags, Pages JSON,
agent-setup, videos, WARP) are implemented and built; rendering leakage is zero; the
API-reference family and logpush datasets are external sibling / live-fetched data,
documented rather than fabricated.

## Importer fixes made during CP6

1. `match_pair` no longer treats prose apostrophes as quote mode.
2. Fences pair sequentially, tolerate indented / 4-backtick / list-marker prefixes.
3. Inline code cannot span newlines.
4. Escaped `\<` tokens protected.
5. `</ Component>` (space) closing tags handled.
6. Multi-line `import { ... } from "~/components"` stripped from content.
7. Blockquote-prefixed multi-line components tolerated.
8. Leading `---` HR stripped so Nift does not misread front matter.
9. `~/assets/`/`src/assets/`/`public/` references rewritten to `/assets/upstream/`/`/`.
10. Titled directives `:::note[Title]` render as `<aside>` with an `nb-aside-title`.
11. Directive spans processed bottom-up so component closing tags are not dropped.
12. Unclosed directives auto-close at end-of-text (upstream omits some closes).

All covered by regression tests (31 tests pass). CP3 census remains green and
deterministic after the scanner mirroring these fixes (0 unknown, 573 unmatched prose).

## CP6B certification fixes

13. Directive spans nested inside an outer directive are converted once (recursion),
    never double-processed with stale top-level line indices.
14. Fenced code blocks are pre-rendered to `<pre><code class="language-...">` at
    restore time, so an irregular closing fence (indented deeper than the opener)
    cannot leave a fence open and swallow following component HTML.
15. Multiline lowercase HTML tags (e.g. `<a\n\thref=...>`) are joined onto one line
    so CommonMark treats them as type-6 HTML blocks.
16. Pure-HTML container bodies (component-shell composition with nested body
    references, no own Markdown) are referenced via `@input` instead of `@markup`,
    eliminating Nift's re-conversion of already-rendered nested HTML.
17. `~/assets/` / `src/assets/` / `public/...` rewrites are applied inside body files
    as well as the page content.
18. Changelog posts are served at the upstream route `/changelog/<product>/<name>/`
    (was `/changelog/post/<name>/`); index/product/product-group/RSS links updated.
19. Per-product `/<product>/llms.txt` and `/llms-full.txt` routes and per-product
    changelog RSS feeds (`/changelog/rss/<id>.xml`) generated so the links emitted
    by the root llms.txt and changelog pages resolve.

## Test suite

`python3 -m unittest discover -s tests -v` → **31/31 pass** on the development VPS
(25 importer/conversion tests + 6 root-cause regression tests added during CP6B
certification: nested-directive double processing, irregular closing fences,
multiline HTML tags, pure-container `@input`, asset refs in bodies, importer-rendered
top-level Markdown).