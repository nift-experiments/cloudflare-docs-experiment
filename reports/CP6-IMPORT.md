# CP6 — Full-corpus import and route verification report

Pinned upstream: `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.

## Status

**CP6A — ordinary documentation corpus: CERTIFIED.**

**CP6 — complete Cloudflare site surface: PENDING (CP6B required).**

CP6 is deliberately split: CP6A covers the 6,882 ordinary docs; CP6B covers the
generated/data-driven route families and rendering correctness needed for the
complete frozen site. CP6A is green; CP6B is in progress.

- Importer converts **all 6,882 frozen docs** with **zero unknown/unresolved constructs**.
- Nift generates **6,883 tracked pages** (6,882 docs + bespoke `/` landing page).
- **CP6B generated families implemented** (see table below) raise the total to
  **8,952 tracked pages**, all built successfully on the development VPS.
- Full Nift build succeeds; **all 8,952 `index.html` routes** present with correct
  trailing-slash semantics (`/kv/get-started/` → `public/kv/get-started/index.html`).
- Route verifier: **missing routes = 0**.
- Link/asset verifier: `~/assets`/`src/assets`/`public/` references rewritten to
  `/assets/upstream/`/`/` and resolve; no broken ordinary-doc local links.
- **Rendering architecture implemented (CP6B):** component/directive bodies are
  emitted as file-based `@markup("md", "content/.markup/bodies/N.md")` references so
  Nift renders each body's Markdown (avoiding find_balanced fragility). REAL rendering
  leakage dropped from 97 (baseline) to 18, each remnant individually classified.
- Development-VPS build measurements (g6-standard-1, 1 vCPU / 2 GB, Nift v4.3.0):
  clean build ~18-26 s wall, no-op rebuild ~2.5-3 s, peak RSS ~66 MB. **These are
  development observations, not comparable to the frozen Astro baseline** (see HANDOVER).

## CP6B status — generated families and rendering

**Generated families:** `tools/generate_families.py` reads the frozen collections and
emits Nift content+tracked entries. Implemented: glossary, directory, field catalog,
Workers AI legacy models, catalog models, changelog (posts + paginated index + product
+ product-group pages), learning paths, `llms.txt`, videos, agent-setup, synthesized
WARP-release changelog posts, compatibility-flags.json, and changelog RSS. These add
2,069 tracked pages (6,883 → 8,952), all built.

**API reference (`/api/resources/...`):** documented as a same-origin sibling application
outside the docs build (`src/util/sidebar.ts` `EXTERNAL_APP_PREFIXES`). Its OpenAPI
schema is fetched at build time from middlecache and is not committed; the family is
recorded, not generated.

**Rendering correctness — implemented:** the importer converts titled directives
(`:::note[Title]` → `<aside>` with title), processes directive spans bottom-up (fixing
dropped component closing tags), auto-closes unclosed directives, and emits
component/directive bodies as **file-based nested `@markup("md", path)` boundaries**
(`content/.markup/bodies/N.md`), so Nift renders each body's Markdown with Markup++
directly (no find_balanced fragility). Conversion of **all 6,882 docs remains
zero-failure**. `tools/leak_scan.py` confirms: literal `:::` directives 1,195 → 0;
**REAL rendering leakage 97 → 18** (the residuals are code-content-with-HTML-looking
edge cases and scanner false positives on unclosed `<pre>`, each individually
classified). Component bodies render correctly (lists, bold, inline code, fenced
code, nested components, directive titles with `<code>`) as verified on representative
pages through the real Nift binary.

**Architecture:** `reports/CP6B-RENDERING-ARCHITECTURE.md` analysed four options and
recommended the nested-Nift-`@markup` design. The implementation uses the **file-based**
`@markup("md", path)` form (rather than inline `@markup("md"){...}`) because Nift's
`find_balanced` cannot deterministically parse arbitrary Markdown bodies inline
(apostrophes, stray backticks, irregular fences). The file form reads the body file
directly, avoiding that fragility while preserving nested Markdown composition. Corpus
matrix and escaping-risk evidence: `reports/cp6/markdown-component-corpus-matrix.json`,
`reports/cp6/atmarkup-body-risk.json`.

## Generated/data-driven families (G6 findings)

The 6,882 ordinary docs represent the `src/content/docs` corpus. The upstream site
also serves generated families from other content collections and Astro dynamic
routes. Each is recorded below with its data source and route contract.

| Family | Data source (frozen checkout) | Files | Route pattern | Status |
|---|---|---|---|---|
| API reference | OpenAPI spec (fetched by `bin/fetch-openapi.ts`) | n/a | `/api/resources/...` | **External sibling app** — documented, not generated (same-origin app outside the docs build) |
| Changelog | `src/content/changelog/` | 1,180 | `/changelog/post/<id>/`, `/changelog/` (48 pages), `/changelog/product/<id>/` (76), `/changelog/product-group/<slug>/` (8) | **Generated** |
| Glossary | `src/content/glossary/` | 35 | `/glossary/` | **Generated** |
| Directory | `src/content/directory/` | 188 | `/directory/` | **Generated** |
| Learning paths | `src/content/learning-paths/` | 20 | `/learning-paths/<slug>/` | **Generated** |
| Workers AI models | `src/content/workers-ai-models/` | 65 | `/workers-ai/models/<short-slug>/` | **Generated** |
| AI model catalog | `src/content/catalog-models/` | 161 | `/ai/models/<model_id>/` | **Generated** |
| Fields catalog | `src/content/fields/` | 1 | `/ruleset-engine/rules-language/fields/reference/<name>/` (176) | **Generated** |
| llms.txt | `src/content/directory/` + docs | n/a | `/llms.txt` | **Generated** |
| Compatibility flags | `src/content/compatibility-flags/` | 125 | `/workers/platform/compatibility-flags.json` | **Generated** (124 flags) |
| WARP releases | `src/content/warp-releases/` | 303 | synthesized changelog posts under `/changelog/post/<date>-warp-.../` | **Generated** (292 synthesized) |
| Release notes | `src/content/release-notes/` | 43 | `/changelog/...` | Not yet generated |
| Dash routes | `src/content/dash-routes/` | 3 | `/api/operations/...` | Not yet generated |
| Page build env | `src/content/pages-build-environment/` | 3 | `/pages/platform/language-support-and-tools.json` | **Generated** (3 versions) |
| Pages presets | `src/content/pages-framework-presets/` | 1 | `/pages/platform/build-configuration.json` | **Generated** (28 presets) |
| Notifications | `src/content/notifications/` | 1 | `/notifications/...` | Not yet generated |
| Agent setup | `src/content/agent-setup/` + `src/pages/agent-setup/` | 2 | `/agent-setup/` (prompt, tracing) | **Generated** |
| Videos | `src/content/stream/` + `src/pages/videos/` | 30 | `/videos/<url>/` | **Generated** |
| RSS | `src/content/changelog/` | n/a | `/changelog/rss/index.xml` | **Generated** |
| robots.txt/_headers/redirects | upstream `public/` | n/a | `/robots.txt`, `/_headers`, `/__redirects` | **Generated** (copied static) |
| Sitemap | generated | n/a | `/sitemap-index.xml` | Not yet generated |
| Logpush datasets | fetched at build (`bin/fetch-logpush-datasets.ts`) | n/a | `/logs/logpush/...` | Not yet generated (fetched data) |
| Partials (reusable) | `src/content/partials/` | 1,366 | — (included in docs) | **Used via CP5 Render placeholder** |

### Verifier status for generated families

The route verifier (`tools/verify_routes.py`) reports **0 missing ordinary-doc routes**.
The remaining "broken" local references (1,999 after generated-family expansion,
`reports/cp6/generated-family-links.json`) are links from ordinary docs and generated
pages to still-missing generated families and to the external `/api/` sibling app:

- `/api/resources/...` + `/api/*`: ~1,600 (external sibling application)
- `/logs/logpush/...`: ~133 (logpush datasets, fetched at build)
- `/workers-ai/models/uform-*`: 21 (live/proxied model data, not in frozen tree)
- `/ruleset-engine/rules-language/fields/reference/...`: 166 (fields catalog)
- `/llms.txt`/`/llms-full.txt` + per-product llms.txt: ~30
- `/agent-setup/`, `/learning-paths/`, `/realtime/realtimekit/`, `/changelog/` area
  links (upstream permalink mismatch), `/workers/runtime-apis/...`: small counts
- Relative asset refs (`public/images`, `src/assets`): a few (asset-path artifacts)

Each remaining family is classified (frozen-committed data / pinned external /
live-fetched / external-sibling / upstream-stale) in the family table above; the
verifier is not made green by excluding known generated families.

### G6 decision

**CP6A (ordinary docs) is certified.** The 6,882-document corpus is fully imported,
built and route-verified. **CP6B is in progress.** Generated families with committed
data (changelog, glossary, directory, fields, Workers AI models, catalog models,
learning paths, llms.txt) are implemented and built; remaining generated families
(compatibility flags, WARP/release, agent-setup, videos, RSS/sitemap, logpush) and the
markdown-inside-component-HTML rendering limitation are recorded above and remain
CP6B work. The API-reference family is an external sibling app, not generated.

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

All covered by regression tests (12 tests pass). CP3 census remains green and
deterministic after the scanner mirroring these fixes (0 unknown, 573 unmatched prose).

## Test suite

`python3 -m unittest discover -s tests -v` → 12/12 pass on the development VPS.