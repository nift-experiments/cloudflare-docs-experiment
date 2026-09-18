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

## Mission

Rebuild the public Cloudflare developer documentation site from the frozen
`nift-experiments/cloudflare-docs-upstream` snapshot using Nift as the site
builder.

This is a **fidelity experiment**, not a redesign and not a representative
sample. The finished Nift site must reproduce the upstream website across the
entire documentation corpus (5,000+ pages) with the same content, information
architecture, URLs, typography, colours, spacing, responsive layout, assets,
syntax highlighting, navigation and user-facing functionality to the extent
that functionality belongs to the docs frontend.

The target is not “Cloudflare-like”. The target is an independently built Nift
version whose rendered pages are visually and behaviourally indistinguishable
from the frozen upstream site for practical use.

## Repositories and source-of-truth policy

- Nift implementation: this repository, `cloudflare-docs-experiment`.
- Frozen reference source: `nift-experiments/cloudflare-docs-upstream`.
- Reference production behaviour: the corresponding Cloudflare Developers site
  generated from that snapshot, where needed to establish rendered behaviour.
- Never modify the upstream snapshot to make the port easier.
- Record the exact upstream commit SHA used by the experiment before importing
  content. Once chosen, pin it in this handover (or a dedicated manifest) so all
  benchmark and fidelity results refer to one reproducible source tree.
- Do not silently substitute current production content for snapshot content.
  If production has moved on, the snapshot wins for content and the matching
  snapshot/build wins for implementation semantics.

## Non-negotiable fidelity requirements

The Nift version must preserve, rather than approximate:

1. every publishable documentation page in the selected upstream snapshot;
2. page URLs/routes and meaningful redirects;
3. page titles, descriptions, headings, prose, code, tables, callouts and other
   authored content;
4. global header, product navigation, sidebars, breadcrumbs, table of contents,
   footer and mobile navigation;
5. fonts, font weights, type scale, colours, borders, radii, shadows, spacing,
   widths, breakpoints and other visual tokens;
6. icons, logos, diagrams, screenshots and other static assets;
7. light/dark/theme behaviour if present upstream;
8. syntax highlighting and code-block affordances;
9. search UI and behaviour, using the same service/data contract where it can
   legitimately be reused, or a behaviourally equivalent implementation where
   the upstream service is coupled to the original deployment;
10. interactive documentation components, tabs, accordions/disclosures,
    copy buttons, anchors, feedback controls and other client-side behaviours
    that are part of the public docs experience;
11. canonical/SEO/social metadata, sitemap/robots behaviour and other public
    document metadata that affects the resulting site;
12. desktop, tablet and mobile responsive behaviour.

Do not “clean up”, simplify, modernise or restyle upstream behaviour during the
port. Differences should be treated as defects unless explicitly documented as
an unavoidable external-service/deployment difference.

## Architectural rule

Port the *rendered contract*, not Astro itself.

Study the upstream implementation to determine what each Astro/Nimbus
component ultimately emits and does, then reproduce that contract with the
simplest maintainable combination of:

- Nift templates, `@input`, metadata, JSON, loops/conditionals and `@path`;
- Markup++/Markdown processing where it preserves the upstream content
  semantics;
- ordinary CSS and browser JavaScript for styling and runtime interaction;
- generated intermediate data only where a deterministic conversion step is
  genuinely necessary for upstream MDX/component constructs.

Do not build a second general-purpose Astro/MDX framework inside Nift. Prefer a
small explicit compatibility layer for the finite constructs actually present
in the pinned Cloudflare corpus.

Static assets that need no build-time transformation should remain ordinary
static files in the configured output tree. Nift's tracked graph should contain
pages and genuinely generated resources, not thousands of pointless asset
copies.

## Step-by-step game plan

### CP0 — Freeze and inventory the reference

1. Record the upstream repository URL, branch and exact commit SHA.
2. Record tool/runtime versions required to build the frozen upstream site.
3. Build the upstream site unmodified if feasible and save its route/output
   manifest as reference evidence.
4. Inventory all content roots, page extensions, layouts, components, partials,
   stylesheets, fonts, images, public assets, data files and generated content.
5. Count publishable pages and routes independently of the upstream build.
6. Inventory Astro/MDX/Nimbus constructs used by content, including frequency
   and representative files for every construct.
7. Inventory runtime/client features and external services.
8. Produce a machine-readable `reference-manifest` containing at minimum the
   pinned SHA, expected routes and relevant source files/assets.
9. Commit the inventory before beginning the port.

**Gate:** we can account for the complete source corpus and know what must be
ported; no “we will discover the other 4,000 pages later” shortcut.

### CP1 — Establish reference builds and fidelity tooling

1. Obtain a clean upstream production build from the pinned snapshot.
2. Serve upstream and Nift builds locally under deterministic origins.
3. Add a route crawler that can visit every expected route and report missing,
   unexpected, redirected and failed pages.
4. Add normalized HTML comparison tooling. Ignore only explicitly documented
   nondeterminism; do not normalize away structural differences merely to make
   tests pass.
5. Add browser screenshot capture at fixed desktop/tablet/mobile viewports.
6. Add image-diff reporting with both aggregate metrics and saved diff images.
7. Add DOM/style probes for key geometry, typography and computed CSS values.
8. Add link, asset and console-error checks.
9. Establish a small but deliberately diverse golden-page set: landing page,
   product overview, deeply nested article, code-heavy article, tables,
   callouts, tabs/interactive components, images, long TOC, and mobile-heavy
   navigation cases.
10. Commit the harness separately from implementation changes.

**Gate:** fidelity is measurable automatically rather than judged from a few
hand-picked screenshots.

### CP2 — Extract the upstream design system exactly

1. Trace the actual upstream CSS/theme/font sources rather than eyeballing the
   live site.
2. Bring across legally/repository-available font files and preserve the exact
   `@font-face` declarations, weights and fallbacks.
3. Preserve upstream colour variables/tokens and theme rules.
4. Preserve reset/base typography, spacing, breakpoints, content widths,
   borders, shadows and radii.
5. Bring across icons and public visual assets without lossy recreation.
6. Reproduce the outer document shell in Nift: head metadata, header, global
   navigation, page grid, footer and client-script entry points.
7. Match golden-page shell screenshots before proceeding to thousands of pages.

**Gate:** the empty/skeleton page geometry and global chrome match upstream at
all target viewports.

### CP3 — Map the content model before bulk conversion

1. Enumerate frontmatter fields and determine their rendered/behavioural use.
2. Enumerate every MD/MDX component/tag/directive used in the corpus.
3. Classify each construct as:
   - direct Markdown/Markup++;
   - Nift template/data expression;
   - static HTML component expansion;
   - browser-side interactive component;
   - generated/data-driven page;
   - unsupported/error requiring an explicit implementation.
4. Build a compatibility matrix with occurrence counts and test fixtures.
5. Define deterministic route mapping from upstream source path/frontmatter to
   Nift tracked page name and output path.
6. Define link and asset resolution rules, including anchors and relative links.
7. Fail conversion on unknown constructs. Never silently drop or flatten an
   unrecognised component.

**Gate:** 100% of constructs in the pinned corpus are classified before claiming
bulk-content support.

### CP4 — Build the Nift page/template architecture

1. Split the shell into reusable Nift inputs/templates at sensible boundaries.
2. Define page metadata needed for title, description, product hierarchy,
   breadcrumbs, sidebar state, TOC and SEO.
3. Implement deterministic navigation data rather than hard-coding individual
   pages into templates.
4. Implement content rendering with exactly one effective `@content` insertion
   per tracked page.
5. Use `@path` for Nift-managed internal page/asset relationships wherever it
   is appropriate and preserve upstream public URLs in generated output.
6. Implement headings/anchor IDs and heading-link behaviour exactly.
7. Implement sidebar, breadcrumb and TOC generation from the same semantic
   information as upstream.
8. Verify the golden set before scaling out.

**Gate:** representative pages have the correct DOM structure and navigation,
not merely similar prose inside a generic template.

### CP5 — Implement the complete MDX/component compatibility layer

Implement and test every construct found in CP3. Work from highest-frequency
constructs downward, but finish the complete matrix. This includes ordinary
content plus Cloudflare-specific documentation components and nested/component
composition.

For each construct:

1. create minimal fixtures from real upstream usages;
2. determine exact upstream DOM and runtime behaviour;
3. implement the Nift/conversion equivalent;
4. compare rendered HTML and screenshots;
5. test nesting/edge cases found in the corpus;
6. mark it complete in the compatibility matrix only when all known usages can
   be rendered without fallback loss.

**Gate:** conversion reports zero unknown or silently degraded constructs over
the entire corpus.

### CP6 — Import all content and preserve all routes

1. Convert/generate tracked-page metadata for the full upstream corpus.
2. Preserve the upstream content hierarchy and output URLs.
3. Import reusable content/partials/data while avoiding duplicated rendered
   content.
4. Copy/reference all required static assets.
5. Implement generated/index pages and data-driven page families.
6. Implement redirects/aliases required by the frozen site.
7. Build all pages with Nift.
8. Compare expected and actual route manifests.
9. Crawl every generated route and every internal link.

**Gate:** expected publishable page/route coverage is 100%, with no unexplained
missing pages, broken internal links or missing local assets.

### CP7 — Reproduce client-side functionality

Match public user-facing behaviour feature by feature, including where present:

- desktop/mobile navigation and sidebar state;
- search dialog/input/results/navigation;
- theme controls;
- code copy and code-block controls;
- tabs and other content switches;
- disclosures/accordions;
- heading anchors and deep linking;
- responsive TOC behaviour;
- feedback widgets where their external backend can legitimately be used;
- any other interactive component discovered during the inventory.

Prefer upstream browser code/assets when they are reusable independently of
Astro; otherwise implement equivalent behaviour without changing the UI.
Document external functionality that cannot be made self-contained and test the
remaining frontend contract.

**Gate:** automated interaction tests pass for every discovered public
interaction class.

### CP8 — Full-corpus visual and structural parity campaign

1. Run HTML/DOM comparisons for every route where meaningful.
2. Screenshot every route at the primary desktop viewport.
3. Screenshot a broad/complete responsive matrix, batching it if runtime/storage
   is large.
4. Sort visual diffs by severity and fix shared/template differences before
   page-specific ones.
5. Re-run after every systemic fix.
6. Treat font loading, wrapping, code highlighting, tables, callouts, images,
   sticky positioning, sidebars and long-page TOCs as first-class parity work.
7. Manually inspect outliers and pages where automated comparison is weak.

**Gate:** no material unexplained visual differences remain. Any intentional or
unavoidable difference is individually documented rather than hidden behind a
loose global threshold.

### CP9 — Metadata, accessibility and browser verification

1. Compare `<head>` output, canonical links, social metadata and structured data.
2. Compare sitemap and robots behaviour.
3. Verify keyboard navigation, focus states and relevant ARIA semantics against
   upstream.
4. Check responsive behaviour at and around upstream breakpoints.
5. Check current Chromium, Firefox and WebKit-family rendering where practical.
6. Run HTML/link/accessibility checks and resolve port-introduced regressions.

**Gate:** the Nift port has not lost important non-visual behaviour or document
metadata.

### CP10 — Performance experiment, only after fidelity

Do **not** tune the Nift implementation by deleting functionality or reducing
fidelity. Once parity gates pass, benchmark the two frozen implementations.

Measure at minimum:

- clean/full build wall time;
- peak RSS;
- output file count and total output bytes;
- no-op rebuild;
- single-page/content edit rebuild;
- shared-template edit rebuild;
- shared-data/navigation edit rebuild;
- batches such as 10/100/1,000 changed pages where useful;
- cold and warm runs with enough repetitions to report distributions rather
  than one lucky number.

Record hardware, OS, filesystem, tool versions, commands, cache state, upstream
SHA, Nift SHA and methodology. Keep raw benchmark results in machine-readable
form. Do not publish speed ratios between sites that are not demonstrably
functionally equivalent.

### CP11 — Reproducibility and final audit

1. Start from clean clones/checkouts and follow the documented setup only.
2. Build both frozen sites successfully.
3. Re-run route/content/functionality/visual gates.
4. Re-run benchmark suite.
5. Verify no generated outputs or local caches are accidentally required from a
   developer machine.
6. Document all remaining differences explicitly.
7. Record final upstream and experiment commit SHAs.
8. Produce a concise final report separating fidelity evidence from performance
   evidence.

**Final gate:** another agent can reproduce the Nift site and the comparison
without relying on undocumented local state.

## Fidelity test strategy

A 5,000+ page port cannot rely on manual inspection alone. Use layered evidence:

- **Corpus completeness:** source/page/component inventories and route manifests.
- **Structural parity:** normalized HTML/DOM comparison and targeted selectors.
- **Visual parity:** deterministic screenshots and pixel/image diffs.
- **Behavioural parity:** browser interaction tests.
- **Navigation integrity:** crawler, internal-link and asset checks.
- **Semantic parity:** title/headings/metadata/code/table/callout/component probes.
- **Manual audit:** representative golden pages plus automated-diff outliers.

Do not declare parity from a homepage screenshot or a dozen representative
pages. Representative pages are an early-development tool; final confidence
must cover the full corpus.

## Working/commit discipline

- Commit at the end of each checkpoint and at meaningful independently verified
  sub-checkpoints when a checkpoint is large.
- Keep upstream-import/conversion changes separate from fidelity fixes when
  practical so regressions are traceable.
- Run `nift build` frequently and `nift status` before checkpoint completion.
- Do not commit benchmark conclusions until fidelity gates for the compared
  builds pass.
- Never solve a comparison failure by weakening/removing the comparison unless
  the ignored difference is proven nondeterministic and documented.
- Preserve failures and unexpected constructs as actionable errors; silent
  fallback is unacceptable for this experiment.

## Immediate next action

Begin with **CP0 only**: acquire/inspect the frozen upstream snapshot, pin its
commit, inventory the entire source/content/component/asset/runtime surface and
commit that evidence. Do not begin hand-porting the homepage before the corpus
and component model are understood.

## Campaign status — 2026-09-18

- **CP0 complete:** frozen upstream `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`; repository inventory in `reports/CP0-INVENTORY.md`; local deep scanner in `tools/inventory_upstream.py`.
- **CP1 complete:** normalized-DOM/diff/Chromium-screenshot harness in `tools/parity.py`; representative routes in `parity/golden-routes.txt`; final-gate extensions in `reports/CP1-PARITY-HARNESS.md`.
- **Next: CP2 design-system extraction.** Do not approximate Cloudflare visually: extract the actual rendered fonts, CSS tokens, dimensions, breakpoints, icons and assets against the frozen baseline.

The attached Nift source was consulted and successfully compiled in this environment using an unoptimised development build (the normal `-O2` compile exceeded the runner's per-command time limit). The current barebones project structure matches the documented Nift model: `.nift/config.json`, `.nift/tracked.json`, `content/`, reusable templates and generated `public/` output. The current Nift site itself remains intentionally barebones through CP1; CP0–CP1 establish evidence and tooling before visual implementation begins.

### CP2 completion note — 2026-09-18

CP2 source extraction and Nift shell implementation are committed. See `reports/CP2-DESIGN-SYSTEM.md` for the exact sources, tokens, font versions, geometry and remaining verification boundary. The shell is source-derived from frozen upstream `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`; do not replace its values with visually guessed equivalents. Screenshot/pixel certification is deferred until both frozen sites can be built together on the controlled Linode environment.

**Next: CP3 content-model inventory.** Enumerate every frontmatter field and every MD/MDX component/directive across the frozen corpus, classify every construct, define deterministic route/link/asset rules, and fail conversion on unknown constructs.

### CP3 completion note — 2026-09-18

CP3's strict content-model contract is committed. See `reports/CP3-CONTENT-MODEL.md`, `compatibility/content-model.json`, `compatibility/route-link-asset-rules.md`, and `tools/content_model.py`. The known component/frontmatter API from the frozen upstream source is classified, deterministic route/link/asset rules are fixed, and the exhaustive scanner fails on unknown constructs rather than degrading them. Because this runner still lacks the 1.4 GB upstream checkout, do not invent corpus occurrence counts: run the census against pinned SHA `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf` on the controlled Linode and require `unknown=0` before CP6. CP4/CP5 implementation must preserve that strict gate.

**Next: CP4 page/template architecture**, followed by CP5 implementation of the complete construct matrix. Keep static rendering, data-generated content and browser-interactive behaviour separate so later parity failures are diagnosable.
