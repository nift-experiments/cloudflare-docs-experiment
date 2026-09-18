# CP3 — content model and strict conversion contract

Pinned upstream: `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.

## Outcome

CP3 establishes the machine-enforced content-model boundary before bulk import. The repository now contains a compatibility registry (`compatibility/content-model.json`), deterministic route/link/asset rules, and an exhaustive corpus census/gate (`tools/content_model.py`). The gate is intentionally strict: a frontmatter key, named MDX component, container directive or route collision not classified in the registry makes the command exit non-zero. Unknown constructs are never flattened or dropped.

The frozen source tree established in CP0 contains 6,882 MD/MDX files under `src/content/docs`, 1,365 partials, 1,180 changelog entries and 110 top-level documentation product roots. The upstream `src/components.ts` barrel currently exposes the documented content component surface; each exposed component has an explicit disposition in the registry: static HTML expansion, browser-interactive implementation, data-generated implementation, or Nift/template handling. Frontmatter fields explicitly accepted by the frozen `src/content.config.ts` are likewise classified.

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

Run from the stage repository once the frozen upstream checkout is present:

```sh
python3 tools/content_model.py /path/to/cloudflare-docs-upstream
```

It scans every docs MD/MDX file, counts frontmatter keys, named components, imports, directives, literal HTML and fenced-code languages, detects MDX exports/JSX expressions, constructs the complete route map, checks collisions, and writes `reports/CP3-CENSUS.json`. It also writes a real-usage component fixture index under `fixtures/cp3/`.

Exit `0` means every discovered named construct is classified. Exit `2` means the compatibility gate failed and includes the unknown constructs/files in the JSON report. CP4/CP5 must not weaken this failure mode.

## Verification boundary

The local runner still does not contain the frozen 1.4 GB upstream checkout, so the *dynamic occurrence counts* cannot honestly be materialized here. CP3 therefore does not fabricate occurrence counts. The complete census is deterministic and ready to run on the controlled Linode (or any machine with the pinned checkout), and its zero-unknown result is a mandatory gate before CP6 bulk import. The static registry is source-derived from the frozen component barrel and content schema already inspected in CP0–CP2.

This distinction is deliberate: “classified in the known source API” and “observed exhaustively across all 6,882 documents” are separate evidence. The latter must come from running the census over the actual bytes.

## CP4/CP5 handoff

Implement the compatibility registry by class, starting with high-frequency static primitives but retaining the zero-unknown gate. Every named component gets a real-upstream fixture once the census runs. Data-generated constructs must identify their collection and route dependencies. Interactive constructs require behaviour tests in CP7. Only after the census returns zero unknowns and implementations cover the matrix may CP6 import the complete corpus.
