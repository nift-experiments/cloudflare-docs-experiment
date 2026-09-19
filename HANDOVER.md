# HANDOVER.md
v0.0.8

This is a living handover for working effectively in a Nift project.

Canonical version:

https://nift.dev/HANDOVER.md

Check the version at the top of this file against the canonical copy when the
project is old, unfamiliar, or behaving differently from the current Nift
documentation.

To replace this file with the latest canonical version:

```sh
curl -fsSL https://nift.dev/HANDOVER.md -o HANDOVER.md
```

If this project has project-specific additions, preserve or reapply them when
updating the canonical handover.

This project uses Nift as part of its website build process.

Nift is the project's build-time templating and dependency layer. It does not determine what the website is about or what other technologies the project should use.

Keep the existing project architecture and use the project's normal HTML, CSS, JavaScript, frameworks, backend, and other tooling where appropriate.

Do not introduce Nift-specific machinery where ordinary web tooling is the clearer solution.

## Start here

Before making substantial changes:

1. Inspect `.nift/config.json` and `.nift/tracked.json`.
2. Inspect the existing `content/`, `templates/`, and output structure.
3. Read this project's `README.md` and other project-specific documentation.
4. Run:

```sh
nift status
```

During normal development, build frequently:

```sh
nift build
```

Use this throughout a task, not only at the end. Rebuild after meaningful
changes so Nift can surface template, path, dependency, configuration, and
tracking errors while the cause is still obvious.

In particular, run `nift build` immediately after editing
`.nift/config.json` or `.nift/tracked.json`.

Use:

```sh
nift status
```

when you want to inspect what Nift considers stale and why.

Successful `nift build` output may include indented `↳ ...` lines explaining
why a page was considered stale and rebuilt, such as a missing generated output
or a changed dependency. These are rebuild reasons, not errors. Actual build
failures are reported as errors and cause the build to fail.

Do not delete or recreate `.nift/`.

## Nift's core template model

Most Nift websites need very little Nift-specific syntax.

The three primitives you will use most often are:

```text
@content
@input(...)
@path(...)
```

`@content` inserts the tracked page's content into its template.

```html
<main>
    @content
</main>
```

`@content` should execute exactly once across the rendered template/input graph
for a tracked page. It is normally placed in the page's template; the tracked
content file supplies the content inserted there.

Content files may still use other Nift syntax when needed. If page text needs
to display Nift syntax literally, prefix the active sigil with `\` rather than
leaving it as template syntax:

```html
<code>\@content</code>
<code>\@path('about')</code>
<code>\$[title]</code>
```

This applies whenever `@...`, `$[...]`, or other Nift syntax is intended as
literal output rather than something Nift should execute or resolve.

`@input(...)` inserts a reusable file and automatically makes it a dependency of the output using it.

```html
@input('templates/header.html')

<main>
    @content
</main>

@input('templates/footer.html')
```

### Structured JSON and markup sources

Use name-first `@json` when a template needs immutable structured data:

```text
@json(name, path)
@json(name, schema-path, path)
@json(name, schema-name, path)
@json(name){...}
@json(name, schema-path){...}
@json(name, schema-name){...}
```

Inline bodies are evaluated as Nift templates before JSON parsing. A schema
name refers to an earlier JSON binding. Data and schema files are automatic
dependencies and paths must stay inside the project.

Use `@markup(format){...}` or `@markup(format, path)` for Markdown (`md`),
AsciiDoc (`adoc`) or reStructuredText (`rst`). Nift evaluates template syntax in
the source first, Markup++ converts it once, and the resulting HTML is appended
without being parsed as Nift syntax again. File sources and host-resolved
AsciiDoc/RST includes are automatic dependencies.

`@path(...)` creates project-aware links to tracked pages and local assets.

Nift has additional features including metadata, JSON data, loops, conditionals, pagination, contracts, and explicit dependencies. Use them when the project actually needs them; do not use advanced features merely because they exist.

When writing expressions inside constructs such as `@if(...)`, refer to values directly rather than wrapping them in `$[...]`. For example:

```html
@if(name == 'about'){...}
```

Use `$[...]` when resolving or rendering a value into output, for example `$[title]`. Consult the expressions and control-flow documentation when using more advanced expression syntax.

## Internal links: use `@path`

Use `@path(...)` for internal links.

This applies to:

- links between pages;
- stylesheets;
- JavaScript;
- images and other local assets where Nift should know the relationship.

For pages, link to the **tracked page name**, not its generated file.

```html
<nav>
    <a href="@path('/')">Home</a>
    <a href="@path('about')">About</a>
    <a href="@path('docs')">Docs</a>
    <a href="@path('contact')">Contact</a>
</nav>
```

Do this:

```html
<a href="@path('about')">About</a>
```

Do not do this:

```html
<a href="@path('about.html')">About</a>
```

and do not hard-code the generated output path:

```html
<a href="about.html">About</a>
```

The tracked page name is the stable project identity. Its output filename or location may change independently.

CSS and JavaScript includes should also use `@path(...)`:

```html
<link rel="stylesheet" href="@path('public/assets/style.css')">
<script src="@path('public/assets/app.js')"></script>
```

Do not calculate relative paths such as:

```html
<link rel="stylesheet" href="../../assets/style.css">
```

Using `@path` lets Nift resolve the correct output-relative path and check the project relationship during the build.

## Project configuration

`.nift/config.json` contains project-level Nift configuration.

`.nift/tracked.json` describes tracked pages and their metadata, including things such as their content, template, and output relationships.

By default, ordinary CSS, JavaScript, images, fonts and other static assets live
directly in the configured output tree (normally `public/`) and do not have
entries in `.nift/tracked.json`. Edit those files in place. This keeps Nift's
tracked graph focused on content that Nift actually renders and avoids duplicate
source/output copies for files that need no build-time transformation.

Track an asset only when Nift genuinely needs to generate it from content,
templates or build-time data. Template-less tracked entries remain available for
that advanced case; they are not the default asset workflow.

These files are part of the project and should evolve with its structure.

If you add, remove, or reorganise pages, templates, outputs, deployment settings, or other Nift-managed structure, inspect the relevant `.nift` configuration and update it where necessary.

Do not treat `.nift/` as disposable generated state.

Do not invent `.nift/tracked.json` fields or assume arbitrary fields become
`$[...]` metadata. When you need tracking behaviour or metadata that is not
already demonstrated by the project, consult the tracked-files and metadata
documentation rather than guessing.

## Output directory

Do not assume the generated website always lives in `public/`.

A normal Nift project may use `public/`, but deployment targets can use a different output structure appropriate to the platform.

Inspect `.nift/config.json` before making assumptions about output paths.

Edit Nift-managed page sources rather than their generated output. Edit untracked
static assets directly in the configured output tree, unless the project
documents another tool or source directory as their owner.

## Pagination

Pagination has several related pieces across `.nift/tracked.json`, page
content, pagination templates, and generated page links. Do not infer its full
behaviour from this handover.

If working with pagination, read the dedicated documentation first:

https://nift.dev/docs/pagination.html

Preserve the project's existing pagination structure unless the task actually
requires changing it, and run `nift build` frequently while doing so.

## Other stacks and tools

Nift does not need to own the whole application.

A project may use Nift alongside tools such as Vite, React, Vue, Svelte, TypeScript, Go, Node, Python, PHP, serverless functions, or other systems.

Keep responsibilities separated:

- use Nift for build-time composition, tracked relationships, and dependencies;
- use the neighbouring tool for the job it is designed to do.

Do not replace an existing stack with Nift-specific code simply to make more of the project use Nift.

## Before finishing

Run:

```sh
nift build
nift status
```

The build should succeed and `nift status` should report the project up to date.
Spot-check generated output when changes affect paths, templates, tracked
relationships, or deployment structure.

## Documentation

Nift documentation:

https://nift.dev/docs.html

When unfamiliar with the project, prioritise:

1. Getting started — https://nift.dev/docs/getting-started.html
2. the three-primitives/template-language material;
3. paths and tracked files, especially `@path`;
4. project structure;
5. `.nift/config.json` and `.nift/tracked.json`;
6. incremental builds and CLI commands.

Then read feature documentation only when the task requires it, for example:

- JSON and control flow;
- pagination;
- contracts;
- minification;
- deployment targets;
- integration with other application stacks.

Prefer documented Nift behaviour and the existing project structure over guessing based on another website generator or framework.

---

# Project-specific handover — Cloudflare Docs → Nift fidelity experiment

This section is for a **fresh agent resuming this experiment with no prior
conversation context**. Read this entire section, then the CP reports, then
verify the baseline before changing anything. The experiment is paused at a
certified CP6B baseline; the next checkpoint is CP7.

## 1. Mission and experiment design

Rebuild the public Cloudflare developer documentation site **from the frozen
upstream snapshot** using **Nift** as the site builder, preserving routes,
content, structure, visual behaviour and useful client-side functionality as
closely as practical.

- This is a **fidelity experiment**, not a redesign and not a representative
  sample: the finished Nift site must be visually and behaviourally
  indistinguishable from the frozen upstream site for practical use.
- Only benchmark performance **after** fidelity is established (CP10).
- Compare Nift against the frozen upstream Astro implementation on build time,
  memory, dependency footprint and operational/developer complexity.
- Use the experiment to discover **genuine Nift strengths and weaknesses** rather
  than modifying either side merely to manufacture a benchmark win.

## 2. Repositories and source-of-truth policy

- Nift implementation: `nift-experiments/cloudflare-docs-experiment` (this repo).
- Frozen reference source: `nift-experiments/cloudflare-docs-upstream`.
- **Pinned upstream SHA: `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf` — never rebase
  or silently substitute current production content.**
- Never modify the upstream snapshot to make the port easier. If production has
  moved on, the snapshot wins for content and semantics.
- GitHub is the persistence layer. The development VPS is disposable.

## 3. Completed checkpoint history

- **CP0 — freeze & inventory.** Pinned upstream SHA; repository inventory
  `reports/CP0-INVENTORY.md`; `tools/inventory_upstream.py`.
- **CP1 — parity/fidelity tooling.** Normalized-DOM/diff/Chromium-screenshot
  harness `tools/parity.py`; golden routes `parity/golden-routes.txt`;
  `reports/CP1-PARITY-HARNESS.md`.
- **CP2 — design-system extraction.** Cloudflare-derived shell (fonts, tokens,
  geometry) `reports/CP2-DESIGN-SYSTEM.md`; initial Nift shell assets in the
  nested `public` repo.
- **CP3 — content-model inventory.** Strict deterministic compatibility contract
  `reports/CP3-CONTENT-MODEL.md`, `compatibility/content-model.json`,
  `compatibility/route-link-asset-rules.md`, `tools/content_model.py`;
  census `reports/CP3-CENSUS.md/.json`. Real corpus: 6,882 docs → 6,882 routes,
  0 unknown constructs.
- **CP4/CP5 — Nift page/template architecture + MDX compatibility layer.**
  `templates/docs.html`; `tools/import_cloudflare.py` backed by
  `compatibility/content-model.json`; fixtures/tests. Unknown MDX constructs are
  fatal (strict gate).
- **CP6A — ordinary documentation import (CERTIFIED).** 6,882/6,882 docs import,
  0 unknown/unresolved; route verifier 0 missing; importer robustness tests.
- **CP6B — generated/data-driven surface + rendering correctness (CERTIFIED).**
  See Section 4-6 and `reports/CP6-IMPORT.md`,
  `reports/CP6B-RENDERING-ARCHITECTURE.md`.

## 4. Current certified state (exact gates)

- **6,882 / 6,882** ordinary docs import (0 failures).
- **9,134 tracked HTML pages**, all build, **0 Nift HTML-validation failures**.
- **0 missing expected routes** (route verifier `tools/verify_routes.py`).
- **31 / 31** importer regression tests pass.
- **REAL rendering leakage = 0** (`tools/leak_scan.py`).
- INTENTIONAL scanner findings (defensible, not leakage): `code-fence` 187,
  `code-import` 62, `prose-placeholder` 19, `ts-type-name` 2.
- Important static/data endpoints reproduced: robots.txt, _headers, __redirects,
  shell assets, changelog RSS index + 75 per-product feeds,
  compatibility-flags.json, Pages build-configuration.json + language-support
  JSON, llms.txt + per-product llms.txt, llms-full.txt + per-product llms-full.txt.
- Nift **v4.3.0** on the VPS.
- Final CP6B commit: **`dcc8d92`** (pushed `stage`).

### The route verifier still reports broken local references

This is **expected and documented** — **do not** treat it as Nift conversion
failures, and **do not** invent pages to make the number zero. Categories:

- `/api/...` (~1,585): sibling/external application outside this frozen docs build.
- `/logs/logpush/.../datasets/...` (~136): data-driven/live surfaces fetched at
  build (Logpush API), not present as frozen ordinary docs.
- `/workers-ai/models/...` (~21): externally/generated (proxied) model surfaces.
- Everything else: links already stale/legacy/broken **in the frozen upstream
  source** (e.g. `/workers/runtime-apis/bindings/mtls/`, `/changelog/<name>/`
  links missing the product prefix, legacy `/changelog/post/` links inside
  upstream changelog post bodies). These are reproduced faithfully.

Evidence: `reports/cp6/leak-scan-classified.json`, `reports/cp6/expected-routes.json`.

## 5. Rendering architecture (final)

The most important technical outcome of CP6B. The architecture is **not** simply
"wrap everything in Markdown".

1. **Inline `@markup("md"){...}` was abandoned** for arbitrary corpus bodies:
   Nift's `find_balanced` must find the balanced body boundary through hostile
   Markdown/code (apostrophes, stray backticks, irregular fences, braces) and
   could not do so deterministically across the corpus.
2. **File-based `@markup("md", path)`** was introduced: component/directive
   bodies are written to `content/.markup/bodies/N.md` and referenced by path.
   Importer state: `_BODY_REGISTRY` (idx→body), `_BODY_NEXT` global counter
   (reset once at import_corpus start, never per page), `_BODY_DIR`.
3. **Nested `@markup` was found to double-render**: when a `@markup` body
   contains nested `@markup` references, Nift resolves the nested HTML and then
   re-runs CommonMark on the whole result, re-parsing already-rendered `<pre>`
   HTML and splitting hostile code (Rust `r#"..."#` raw strings, JSX containing
   `</pre>`/`</code>` literals) at nesting depth ≥ 3.
4. **Final architecture distinguishes body kinds:**
   - **Markdown-bearing / leaf bodies** use file-based `@markup("md", path)`;
   - **pure composition/container bodies** (component shells + nested refs, no
     own Markdown) use `@input(path)` so nested rendered HTML is not
     Markdown-converted again;
   - **top-level imported documentation** is rendered **once by the importer**
     (cmarkgfm) and inserted by `templates/docs.html` through `@content`;
   - **generated families** that still intentionally emit Markdown use
     `templates/docs-md.html` (`@markup("md"){@content}`).
5. **Other generic fixes** (each with a regression test):
   - nested `:::` directives are converted once (recursion), never
     double-processed with stale top-level line indices;
   - fenced blocks are pre-rendered to `<pre><code class="language-...">` at
     restore time so an irregular closing fence (indented deeper than the
     opener) cannot leave a fence open and swallow following HTML;
   - multiline lowercase HTML tags (e.g. `<a\n\thref=...>`) are joined onto one
     line so CommonMark treats them as type-6 HTML blocks;
   - asset refs (`~/assets/`, `src/assets/`, `public/...`) are rewritten inside
     body files as well as page content.

**Example worth preserving:** the React `<Tabs><TabItem><Steps>` chain with a JSX
code block containing `</pre>`/`</code>` literals — nested `@markup` passes
re-rendered the JSX three times and split it; using `@input` for the pure-HTML
TabItem container removed the redundant CommonMark pass and fixed it without any
page-specific exception.

See `reports/CP6B-RENDERING-ARCHITECTURE.md` for the full write-up. The finding
that this corpus is valuable adversarial evidence for Nift's `find_balanced` /
`@markup` design is preserved for later consideration outside this experiment.

## 6. Clean reproduction procedure (read before touching the VPS)

The generated tree and the checked-in shell have an **unusual relationship**.
Blindly doing `rm -rf public` destroys the checked-out shell assets
(`assets/cf-design.css`, `assets/cf-shell.js`, `assets/cloudflare-logo.svg`,
`index.html`, `CP6.md`), which live in a **nested git repository on the remote's
`main` branch** (the experiment repo's `stage` branch gitlinks to it via commit
`c1e5add`). There is **no `.gitmodules`**; treat it as a hand-managed nested
checkout.

Safe clean-from-scratch sequence on the VPS:

```sh
cd /srv/cloudflare-docs-experiment

# 1. Restore/initialise the public tree (shell assets) if missing/wiped.
#    The public dir is a checkout of the SAME repo's `main` branch at c1e5add.
rm -rf public
git clone -q -b main https://github.com/nift-experiments/cloudflare-docs-experiment.git public
git -C public rev-parse HEAD        # expect c1e5add...

# 2. Clear generated content (dotfiles like content/.markup survive `rm -rf content/*`).
rm -rf content/*
# 3. Full-corpus import (writes content/, tracked.json, expected-routes.json,
#    and copies upstream public/ + src/assets into public/).
python3 tools/import_corpus.py /srv/cloudflare-docs-upstream
# 4. Generated families (changelog, glossary, llms.txt/full, RSS, JSON endpoints, ...).
python3 tools/generate_families.py /srv/cloudflare-docs-upstream
# 5. Restore the bespoke root landing page (it is a tracked git file; import_corpus
#    preserves its tracked entry but `rm -rf content/*` deletes the file).
git checkout content/index.html
# 6. Restore any shell assets the import may have displaced, then build.
cd public && git checkout -- . && cd ..
nift build --all        # full clean build; expect 9,134 files
# 7. Gates.
python3 -m unittest discover -s tests          # 31/31
python3 tools/verify_routes.py                 # missing = 0
python3 tools/leak_scan.py --write-classified  # REAL = 0 (or scan all public/*.html)
```

If the VPS is gone, recreate it (see Section 10 Infrastructure) and restore the
repo from GitHub before running this.

## 7. Generated surfaces (`tools/generate_families.py`)

Implemented: glossary; directory; field catalog (176); Workers AI legacy models
(65) + catalog models (161) where reproducible; changelog posts (at upstream
route `/changelog/<product>/<name>/`) + paginated index + product + product-group
pages; learning paths (20); `llms.txt` + per-product `llms.txt`; `llms-full.txt`
+ per-product `llms-full.txt`; videos (30); agent-setup (13); synthesized WARP
release changelog posts (292, under `/changelog/post/`); compatibility-flags.json
(124); Pages build-configuration.json (28) + language-support-and-tools.json (3);
changelog RSS index + per-product feeds (76); robots.txt/_headers/__redirects
(copied static).

**Deliberate exclusions (do not fabricate data for these):**
- `/api/...` — sibling/external application (fetched OpenAPI), outside the build.
- `/logs/logpush/.../datasets/...` — fetched live from the Logpush API.
- Proxied Workers AI models (e.g. `uform-*`) — live catalog data.
- Release notes, dash routes, notifications — collections feeding other routes or
  sibling apps; no standalone reproducible routes.
- Sitemap-index.xml — derived from tracked routes; low fidelity-gate value.
- WARP posts are synthesized (supplementary), not frozen-site routes.

## 8. Important lessons — things NOT to regress

- Do **not** weaken REAL leakage = 0.
- Do **not** introduce page-specific importer exceptions unless unavoidable and
  documented.
- Do **not** move back to arbitrary inline `@markup` bodies for corpus content.
- Do **not** indiscriminately Markdown-render generated HTML multiple times.
- Do **not** treat upstream broken links as missing Nift routes without checking
  the frozen source.
- Do **not** fabricate data for externally generated/live collections merely to
  raise a parity number.
- Do **not** benchmark Nift vs Astro until fidelity reaches the planned gate.
- Do **not** change Nift itself merely to make this experiment pass, unless the
  corpus exposed a genuinely general Nift defect worth fixing deliberately.
- The corpus is valuable adversarial evidence for Nift's `find_balanced` /
  `@markup` design — preserve it for later Nift work outside this experiment.

## 9. Infrastructure

- Experiment checkout: `/srv/cloudflare-docs-experiment` (branch `stage`).
- Frozen upstream checkout: `/srv/cloudflare-docs-upstream`
  (SHA `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`).
- Nift source/build: `/srv/nift-src`; installed `/usr/local/bin/nift` (v4.3.0).
- VPS: Linode `cf-nift-dev`, g6-standard-1 (1 vCPU / 2 GB / 50 GB), IP
  `45.33.120.107`. **Cost-sensitive: the VM may no longer exist when work
  resumes. This handover must not depend on ephemeral VPS state** — GitHub is the
  persistence layer. No credentials/secrets belong in the repo.
- The original 6-vCPU g6-standard-6 baseline Linode was **destroyed** after the
  Astro baseline was captured (`reports/benchmarks/`).

## 10. Pre-pause measurement snapshot

See `reports/PRE-PAUSE-DEVELOPMENT-SNAPSHOT.md` for the full record. Key facts:

- Nift clean build (`nift build --all`, 9,134 pages, g6-standard-1): median
  **15.11 s** wall, median peak RSS **60,220 KB (~58.8 MiB)**; no-op 3.15 s /
  ~11.9 MiB; Nift binary 2,729,392 bytes; **no Node / `node_modules` required**.
- Frozen Astro source checkout (this VPS): Astro 7.3.2, working tree
  611,154,889 B excl `.git`; **no Node, no `node_modules`, no `dist` here**;
  dependencies were not installed for the snapshot.
- Historical Astro baseline (destroyed g6-standard-6): clean build **433.46 s**,
  peak RSS **~8.35 GB**, 9,025 pages, `node_modules` ~1.3 GB, `dist` ~2.0 GB.

**WARNING — historical Astro and current Nift timings are NOT comparable**
(different hardware/config). Do not advertise a "Nift is Nx faster" number. CP10
must rerun both implementations on **identical hardware** with frozen dependency
state before any comparative claim.

## 11. Next checkpoints

- **CP7 — client-side functional fidelity (next).** Inventory which behaviours
  are currently static approximations vs which upstream interactions matter:
  navigation/sidebar interactions; mobile navigation; tabs; details/disclosures;
  theme behaviour; copy-code controls; search behaviour; table-of-contents
  interaction; interactive component shells that currently render only
  structurally; client-side routing/link behaviour where applicable. Goal is to
  reproduce **observable behaviour**, not recreate Astro.
- **CP8 — full-corpus visual/structural parity.** Use `tools/parity.py` +
  golden routes, then systematic corpus sampling: DOM structure, typography,
  spacing/layout, navigation/sidebar, code blocks, tables, cards/callouts,
  responsive states, screenshots/pixel diffs. Fix systemic causes before
  individual pages.
- **CP9 — metadata/accessibility/browser verification.** Titles/meta,
  canonical/OG metadata, headings/landmarks, keyboard behaviour, responsive
  behaviour, accessibility, Chromium/Vantage verification where useful.
- **CP10 — controlled same-hardware performance campaign.** Only after fidelity
  gates. Rebuild the frozen Astro reference and the Nift site on **the same
  VPS/hardware configuration** with their frozen dependency state; collect clean
  build wall time, no-op/incremental time, peak RSS, CPU, output size,
  dependency/install footprint (`node_modules` size/count for Astro; Nift
  binary/runtime footprint), setup complexity, reproducibility. Do **not** compare
  the current development-VPS Nift timings with the old g6-standard-6 Astro
  measurement.
- **CP11 — reproducibility/final audit.** Fresh-environment reproduction, final
  reports, evidence bundle, conclusions.

## 12. RESUME HERE — next session

The intended resume state is:

**CP0–CP6B complete and certified. Next work: CP7. Performance comparison remains
provisional until CP10 same-hardware benchmarking.**

1. Read this HANDOVER.md (especially Sections 4-10).
2. Read `reports/CP6-IMPORT.md`, `reports/CP6B-RENDERING-ARCHITECTURE.md`,
   `reports/PRE-PAUSE-DEVELOPMENT-SNAPSHOT.md`.
3. Verify the frozen upstream SHA is `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.
4. Verify the experiment branch/SHA (stage, latest pushed CP6B commit `dcc8d92`
   at time of pause; local SHA must equal remote `stage`).
5. Recreate the environment if the VPS is gone (Section 9, 6).
6. **Run the certified CP6B gates before changing anything:** 6,882/6,882 import;
   9,134 tracked pages build with 0 HTML-validation failures; 0 missing routes;
   31/31 tests; REAL leakage = 0. Expected baseline numbers above make any
   regression immediately obvious.
7. Investigate any regression before proceeding.
8. Begin **CP7** only after the CP6B baseline reproduces. Do not skip ahead to
   benchmarking.
