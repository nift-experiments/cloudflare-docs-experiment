# CP3 — content model and strict conversion contract

Pinned upstream: `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.

## Outcome

CP3 establishes the machine-enforced content-model boundary before bulk import. The repository now contains a compatibility registry (`compatibility/content-model.json`), deterministic route/link/asset rules, and an exhaustive corpus census/gate (`tools/content_model.py`). The gate is intentionally strict: a frontmatter key, named MDX component, container directive or route collision not classified in the registry makes the command exit non-zero. Unknown constructs are never flattened or dropped.

## Real-corpus execution (Linode, 2026-09-18)

The frozen upstream checkout is now physically available. The census was run against
`bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`:

- **6,882 docs files → 6,882 routes** (MD + MDX), zero route collisions.
- **114 components**, **55 frontmatter keys**, **5 named directives + bare `:::`** classified.
- **Unknown constructs: 0** → strict gate **PASSED**.
- 579 "unmatched capitalized tags" recorded but non-fatal: these are placeholder tokens,
  TypeScript types, and attribute values such as `<Type text="Array<String>" />` that the
  frozen upstream build renders as text — not MDX components. Proving they are not
  components: none are imported from a component module and the upstream Astro build
  renders them successfully (verified during CP3; Astro errors on any undefined component
  tag).

Full numbers: `reports/CP3-CENSUS.json` (schema 2) and `reports/CP3-CENSUS.md`.

### What the real corpus exposed

The original matrix was derived from the frozen component barrel and content schema.
The physical corpus added:

- **27 new MDX components**, all imported per-file (realtimekit, agent-setup, AI model
  catalogs, animated diagrams, data tables). Each has a disposition in the registry.
- **22 new frontmatter keys.** Upstream `src/content.config.ts` uses
  `strictFrontmatter: false` and passes untyped keys through unmodified, so these are
  classified as preserved Nift metadata (`nift-template`), except `redirect`
  (`data-generated`: a route-level redirect, e.g. `ai-gateway/models.mdx` →
  `/ai/models/`).
- **Directives** `note`, `caution`, `tip`, `warning`, `info` plus bare `:::` callouts.

### Census tooling corrections (made real by the corpus)

1. Fenced ``` / ~~~ and inline `` code are stripped before component/directive matching so
   shell tokens (`<API_TOKEN>`) and TS types inside code are not misclassified.
2. Component detection is import-aware: a capitalized tag is an MDX component only if it is
   in the matrix, exported by upstream `src/mdx-components.ts`, or imported in that file from
   a component module. Other capitalized tags are recorded as unmatched (non-fatal).
3. `mdx-components.ts` exports missing from the matrix are a hard gate.
4. Directive names are matched on the same line as the colons; bare `:::` blocks are counted
   as the known generic callout.
5. The report no longer truncates the unknown detail list.

These changes made the gate accurate; they did not weaken it. The gate still fails on any
imported-but-unclassified component, unknown directive, unknown frontmatter key, or route
collision.

## Classification model

- `markdown`: ordinary Markdown semantics retained through the markup pipeline.
- `nift-template`: document metadata/layout handled directly by Nift templates/metadata.
- `static-html`: component expands deterministically to HTML at build time.
- `browser-interactive`: static shell plus browser behaviour must be preserved.
- `data-generated`: depends on a content/data collection or generated route family.
- `explicit-implementation`: known syntax requiring a dedicated implementation before import.

The classification is a disposition, not a claim that CP4/CP5 has implemented the construct yet.

## Route contract

`src/content/docs/<path>.md[x]` maps to the same trailing-slash URL after stripping the content root, extension and terminal `index`. Collisions are fatal. `external_link` entries are navigation metadata rather than normal emitted documents. Dynamic `src/pages` families and collection-generated routes remain explicit generated-page work for CP5/CP6.

Relative links are resolved against the source document, then mapped through the same route function. Absolute local links and fragments are preserved. External schemes pass through. Local unresolved targets are fatal. Heading fragments are not rewritten because heading-ID parity is part of the rendered contract.

Assets distinguish source assets (`~/assets` → `src/assets`) from public-root assets (`/...` → `public/...`) and relative document assets. Missing assets are fatal. Any Astro image transformation must be represented by a deterministic manifest rather than approximated.

## Census and fixture generation

Run from the stage repository against the frozen checkout:

```sh
python3 tools/content_model.py /srv/cloudflare-docs-upstream
```

It scans every docs MD/MDX file, counts frontmatter keys, named components, imports, directives, literal HTML and fenced-code languages, detects MDX exports/JSX expressions, constructs the complete route map, checks collisions, and writes `reports/CP3-CENSUS.json` plus `reports/CP3-CENSUS.md`. It also writes a real-usage component fixture index under `fixtures/cp3/`.

Exit `0` means every discovered named construct is classified. Exit `2` means the compatibility gate failed and includes the unknown constructs/files in the JSON report. CP4/CP5 must not weaken this failure mode.

## CP4/CP5 handoff

Implement the compatibility registry by class, starting with high-frequency static primitives but retaining the zero-unknown gate. Every named component now has a real upstream example file recorded in `fixtures/cp3/README.md`. Data-generated constructs must identify their collection and route dependencies. Interactive constructs require behaviour tests in CP7. Only after the census returns zero unknowns and implementations cover the matrix may CP6 import the complete corpus.

**Census result on the pinned checkout: 0 unknown constructs — CP3 corpus gate GREEN.**