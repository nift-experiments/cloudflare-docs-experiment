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
  **8,631 tracked pages**, all built successfully on the development VPS.
- Full Nift build succeeds; **all 8,631 `index.html` routes** present with correct
  trailing-slash semantics (`/kv/get-started/` → `public/kv/get-started/index.html`).
- Route verifier: **missing routes = 0**.
- Link/asset verifier: `~/assets`/`src/assets`/`public/` references rewritten to
  `/assets/upstream/`/`/` and resolve; no broken ordinary-doc local links.
- Development-VPS build measurements (g6-standard-1, 1 vCPU / 2 GB, Nift v4.3.0):
  clean build ~17-19 s wall, no-op rebuild ~2.5 s, peak RSS ~10-22 MB. **These are
  development observations, not comparable to the frozen Astro baseline** (see HANDOVER).

## CP6B status — generated families and rendering

**Generated families:** `tools/generate_families.py` reads the frozen collections and
emits Nift content+tracked entries. Implemented: glossary, directory, field catalog,
Workers AI legacy models, catalog models, changelog (posts + paginated index + product
+ product-group pages), learning paths, and `llms.txt`. These add 1,748 tracked pages
(6,883 → 8,631), all built.

**API reference (`/api/resources/...`):** documented as a same-origin sibling application
outside the docs build (`src/util/sidebar.ts` `EXTERNAL_APP_PREFIXES`). Its OpenAPI
schema is fetched at build time from middlecache and is not committed; the family is
recorded, not generated.

**Rendering correctness:** the importer now converts titled directives
(`:::note[Title]` → `<aside>` with title), processes directive spans bottom-up (fixing
dropped component closing tags), and auto-closes unclosed directives. Conversion of
**all 6,882 docs remains zero-failure**. `tools/leak_scan.py` post-build checks confirm:
literal `:::` directives reduced 1,195 → 0; leaked imports/escaped-HTML resolved.

**Rendering correctness — residual defect (open):** Markdown inside component HTML
containers (`<aside>`, `<section>`, `<div class="nb-*">`) is not parsed by the single
CommonMark pass (HTML-block rule). The refined leak scan
(`tools/leak_scan.py`, output `reports/cp6/leak-scan-classified.json`) separates REAL
leakage from INTENTIONAL code/prose: ~97 REAL instances (fenced/inline code and
imports inside component bodies) plus ~3,500 intentional `**bold**`/backtick text
inside component bodies remain. This is a correctness defect, not visual parity.

**Architecture decision in progress:** `reports/CP6B-RENDERING-ARCHITECTURE.md`
analyses four options and recommends Option A: the importer emits Nift `@markup("md"){...}`
boundaries around component/directive bodies. Verified working against Nift v4.3.0:
content files are parsed as templates, so per-body `@markup` renders Markdown
correctly (including fenced code, nested components, directives, and lists) without
the malformed-HTML failure of the reverted cmarkgfm experiment. Corpus matrix and
escaping-risk evidence are committed (`reports/cp6/markdown-component-corpus-matrix.json`,
`reports/cp6/atmarkup-body-risk.json`). Implementation awaits review.

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
| Compatibility flags | `src/content/compatibility-flags/` | 125 | `/workers/platform/compatibility-flags.json` | Not yet generated |
| WARP releases | `src/content/warp-releases/` | 303 | synthesized changelog entries | Not yet generated |
| Release notes | `src/content/release-notes/` | 43 | `/changelog/...` | Not yet generated |
| Dash routes | `src/content/dash-routes/` | 3 | `/api/operations/...` | Not yet generated |
| Page build env | `src/content/pages-build-environment/` | 3 | `/pages/platform/...` | Not yet generated |
| Pages presets | `src/content/pages-framework-presets/` | 1 | `/pages/framework-guides/...` | Not yet generated |
| Notifications | `src/content/notifications/` | 1 | `/notifications/...` | Not yet generated |
| Agent setup | `src/content/agent-setup/` + `src/pages/agent-setup/` | 2 | `/agent-setup/` | Not yet generated |
| Videos | `src/content/stream/` + `src/pages/videos/` | 30 | `/videos/` | Not yet generated |
| RSS/sitemap/robots | `src/pages/*.ts` | n/a | `/changelog/rss/...`, `/sitemap-index.xml`, `/robots.txt` | Not yet generated |
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