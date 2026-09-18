# CP6 — Full-corpus import and route preservation

## Status

**Implementation complete; full-corpus execution gate pending the pinned upstream checkout.**

CP6 is intentionally not marked fidelity-complete in this runner. The frozen Cloudflare repository is not physically available here, so claiming 100% route/link/asset coverage would be fabricated. The controlled Linode run must execute the commands below against SHA `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf` before CP6's gate can turn green.

## What CP6 now provides

`tools/import_corpus.py` is the deterministic corpus orchestrator. It verifies the upstream Git SHA, walks every `src/content/docs/**/*.{md,mdx}` file, invokes the strict CP5 converter, aborts on any unknown/unresolved construct, detects route collisions, emits Nift content and tracked entries, preserves trailing-slash/index route semantics, copies upstream `public/`, stages `src/assets/`, and writes `reports/cp6/expected-routes.json`.

`tools/verify_routes.py` compares that expected manifest with generated `public/**/index.html` routes and crawls local `href`/`src` references. Missing routes or local references are fatal.

The importer deliberately does not declare data-driven/dynamic page families complete merely because their source data exists. Changelog, directory, API/SDK, learning-path, RSS/llms/sitemap/redirect and other generated families identified in CP0/CP3 remain explicit CP6 execution findings to reconcile on the full checkout.

## Controlled execution

```sh
python3 tools/content_model.py /srv/cloudflare-docs-upstream
python3 tools/import_corpus.py /srv/cloudflare-docs-upstream
nift build-all
python3 tools/verify_routes.py
```

The first command must report zero unknown constructs. The import must use the pinned SHA unless the experiment is intentionally rebased. After the Nift build, route and local-reference verification must return zero missing/broken items.

## Gate

CP6 is green only when the frozen checkout produces all of the following evidence:

- zero unknown/silently degraded MDX constructs;
- every publishable upstream docs route represented;
- generated/index/data-driven route families reconciled;
- required redirects/aliases represented;
- all required static assets present;
- Nift full build succeeds;
- expected vs actual route manifest has no unexplained difference;
- complete local link/asset crawl has zero unexplained failures.

Until that run exists, later work must describe CP6 as **implemented, execution pending**, not as certified 100% complete.
