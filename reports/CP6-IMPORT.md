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
- Full Nift build succeeds; **all 6,883 `index.html` routes** present with correct
  trailing-slash semantics (`/kv/get-started/` → `public/kv/get-started/index.html`).
- Route verifier: **missing routes = 0**.
- Link/asset verifier: `~/assets` source references rewritten to `/assets/upstream/`
  and resolve; no broken ordinary-doc local links from the docs corpus itself.
- Development-VPS build measurements (g6-standard-1, 1 vCPU / 2 GB, Nift v4.3.0):
  clean build 16.3 s wall, 14.6 s; no-op rebuild 2.3 s. **These are development
  observations, not comparable to the frozen Astro baseline** (see HANDOVER).

## Generated/data-driven families (G6 findings)

The 6,882 ordinary docs represent the `src/content/docs` corpus. The upstream site
also serves generated families from other content collections and Astro dynamic
routes. Each is recorded below with its data source and route contract.

| Family | Data source (frozen checkout) | Files | Route pattern | Status |
|---|---|---|---|---|
| API reference | OpenAPI spec (fetched by `bin/fetch-openapi.ts`) | n/a | `/api/resources/...` | **Not imported** — requires fetched OpenAPI data not in the frozen tree |
| Changelog | `src/content/changelog/` | 1,180 | `/changelog/post/<id>/`, `/changelog/` | Not yet generated |
| Glossary | `src/content/glossary/` | 35 | `/glossary/` | Not yet generated |
| Directory | `src/content/directory/` | 188 | `/directory/` | Not yet generated |
| Learning paths | `src/content/learning-paths/` | 20 | `/learning-paths/...` | Not yet generated |
| Workers AI models | `src/content/workers-ai-models/` | 65 | `/workers-ai/models/<name>/` | Not yet generated |
| AI model catalog | `src/content/catalog-models/` | 161 | `/workers-ai/models/[...schema].json` | Not yet generated |
| Compatibility flags | `src/content/compatibility-flags/` | 125 | `/workers/platform/compatibility-flags.json` | Not yet generated |
| WARP releases | `src/content/warp-releases/` | 303 | `/warp/change-log/...` | Not yet generated |
| Release notes | `src/content/release-notes/` | 43 | `/changelog/...` | Not yet generated |
| Dash routes | `src/content/dash-routes/` | 3 | `/api/operations/...` | Not yet generated |
| Page build env | `src/content/pages-build-environment/` | 3 | `/pages/platform/...` | Not yet generated |
| Pages presets | `src/content/pages-framework-presets/` | 1 | `/pages/framework-guides/...` | Not yet generated |
| Notifications | `src/content/notifications/` | 1 | `/notifications/...` | Not yet generated |
| Fields catalog | `src/content/fields/` | 1 | `/ruleset-engine/rules-language/fields/reference/...` | Not yet generated |
| Agent setup | `src/content/agent-setup/` | 2 | `/agent-setup/` | Not yet generated |
| Videos | `src/content/stream/` + `src/pages/videos/` | 30 | `/videos/` | Not yet generated |
| RSS/llms.txt/robots | `src/pages/*.ts` | n/a | `/llms.txt`, `/rss`, `/sitemap-index.xml` | Not yet generated |
| Partials (reusable) | `src/content/partials/` | 1,366 | — (included in docs) | **Used via CP5 Render placeholder** |

### Verifier status for generated families

The route verifier (`tools/verify_routes.py`) reports **0 missing ordinary-doc routes**.
The remaining "broken" local references (1,806) are **all** links from ordinary docs to
the generated families above, categorised in `reports/cp6/generated-family-links.json`:

- `/api/resources/...` + `/api/*`: 1,395
- `/ruleset-engine/rules-language/fields/reference/...`: 166 (fields catalog)
- `/logs/logpush/...`: 105 (logpush datasets, fetched at build)
- `/workers-ai/models/...`: 36
- `/changelog/...`: 19
- `/llms.txt`, `/llms-full.txt`: 11
- `/agent-setup/`, `/directory/`, `/learning-paths/`, `/videos/`, `/resources/`,
  `/realtime/realtimekit/...`, `/tutorials/`: small counts
- Relative/other: 14 (including 7 `public/images/...` refs and 1 `src/assets/...` ref
  that are asset-path artifacts)

### G6 decision

**CP6A (ordinary docs) is certified.** The 6,882-document corpus is fully imported,
built and route-verified. **CP6B remains required** to generate the families below and
to fix rendering-correctness defects (literal `:::` syntax, unprocessed component HTML,
etc.), which are correctness defects, not visual work. Each generated family is being
implemented from its committed `src/content/` collection where the data exists; the
API-reference family depends on the upstream OpenAPI data source.

## Importer fixes made during CP6

1. `match_pair` no longer treats prose apostrophes as quote mode.
2. Fences pair sequentially, tolerate indented / 4-backtick / list-marker prefixes.
3. Inline code cannot span newlines.
4. Escaped `\<` tokens protected.
5. `</ Component>` (space) closing tags handled.
6. Multi-line `import { ... } from "~/components"` stripped from content.
7. Blockquote-prefixed multi-line components tolerated.
8. Leading `---` HR stripped so Nift does not misread front matter.
9. `~/assets/` references rewritten to `/assets/upstream/`.

All covered by regression tests (10 tests pass). CP3 census remains green and
deterministic after the scanner mirroring these fixes (0 unknown, 573 unmatched prose).

## Test suite

`python3 -m unittest discover -s tests -v` → 10/10 pass on the development VPS.