# CP6C — Generated-family body materialization repair

Pinned upstream: `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.
Date: 2026-09-28.
Status: **CERTIFIED — generated changelog body aliasing repaired.**

## Discovery

A fresh-environment readiness audit reproduced every CP6B headline gate but found
semantic corruption in generated changelog pages. Of the generated changelog
sources, 144 pages emitted 214 references to `content/.markup/bodies/0.md` through
`5.md`. Those paths belonged to ordinary documentation, so valid but unrelated
content was substituted during the Nift build.

The confirmed example was
`src/content/changelog/stream/2026-03-18-media-transformations-workers-binding.mdx`.
Its Wrangler TOML and TypeScript examples rendered as DNS record-type lists.

The old leakage gate stayed green because the substituted material was valid HTML;
this was semantic substitution, not literal MDX/Markdown leakage.

## Root cause

`tools/generate_families.py` loaded a fresh `import_cloudflare.py` module for every
changelog document. Each module started with `_BODY_NEXT = 0` and `_BODY_DIR =
None`. The importer still emitted file references, but did not materialize their
bodies. Those references accidentally resolved to existing ordinary-corpus body
files with the same low numeric IDs.

The generator also caught conversion exceptions and fell back to raw source,
weakening the strict importer contract.

## Architectural repair

- The importer now exposes `configure_body_output(body_dir, reset=False)`.
- Ordinary import explicitly resets the allocator in a clean body directory.
- Generated-family import uses one importer module and resumes after the highest
  existing numeric body ID.
- Resetting ordinary import removes stale numeric body files, so repeated clean
  reproductions remain deterministic rather than appending generated ranges.
- Ordinary import materializes into a temporary body directory and publishes it
  only after all 6,882 sources validate; `--dry-run`, invalid input, and failed
  conversion cannot destroy the last valid body corpus.
- Conversion refuses to emit component body references unless body output has
  been configured.
- Generated changelog conversion is strict; exceptions are no longer downgraded
  to raw-source warnings.
- `cmarkgfm` is mandatory and absence fails early with an actionable error.

After repair, ordinary bodies occupy IDs `0..14753`; generated changelog bodies
start at `14754`. The 214 top-level changelog references materialize 219 files
(including nested component bodies), for 14,973 total body files. No top-level
body ID is shared between generated changelog documents.

Only changelog posts call `convert_mdx_body()`. No other generated family used the
faulty importer path.

## New regression gates

- The confirmed Stream fixture verifies the generated body files contain
  `[media]`, `binding = "MEDIA"`, and `env.MEDIA.input(video.body)`, and do not
  contain the unrelated `AAAA` or `DNSKEY` content.
- A generic two-document test proves component body IDs and content cannot alias
  across generated MDX conversions.
- The importer fails if component bodies would be referenced without configured
  materialization output.
- Route verification now combines the 6,882 ordinary routes, all claimed
  generated routes, and 196 claimed static/data files.
- The generated manifest contains 2,251 generated-only routes. Twenty learning
  path entries overlap ordinary docs and are not falsely claimed a second time.
- `tools/leak_scan.py --write-classified` is implemented and REAL leakage returns
  non-zero; missing or empty build output also fails.
- Semantic generated-content tests remain separate from leakage scanning.

## Certified clean reproduction

- Ordinary import: **6,882 / 6,882**.
- Tracked/build output: **9,134 / 9,134**, zero Nift HTML-validation failures.
- Expected index routes: **9,134** (6,883 ordinary/root plus 2,251
  generated-only), missing **0**.
- Expected static/data files: **196**, missing **0**.
- Tests: **39 / 39**.
- REAL leakage: **0**.
- Intentional findings: code-fence **188**, code-import **63**,
  prose-placeholder **19**, ts-type-name **2**.
- Broken local references: **1,864**, reported but not route-gate failures:
  1,588 external API application, 133 live Logpush datasets, 21 live/proxied
  Workers AI models, and 122 upstream-stale or otherwise unclassified references.

The code-fence and code-import counts each increased by one because the repaired
changelog bodies now contain their intended code examples instead of unrelated DNS
list content. The additional broken references likewise come from restored source
semantics; no excluded/live routes were fabricated.

Additional lifecycle checks confirmed that a generator-only rerun preserves the
2,251-route manifest and 14,973-file body count, while ordinary-import `--dry-run`
leaves both ordinary and generated body hashes unchanged.

CP6C supersedes the semantic-certification claim attached to CP6B commit
`dcc8d92`. CP7 may begin only from the CP6C `stage` state.
