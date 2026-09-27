# CP7 - Client-Side Functional Fidelity

Pinned upstream: `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.
Date: 2026-09-28.
Status: **CERTIFIED**.

## Scope

CP7 replaces the static shell approximations with progressively enhanced,
framework-free browser behavior. Nift still owns generation and composition;
`public/assets/cf-shell.js` owns browser interaction.

Implemented behavior:

- deterministic product navigation from frozen frontmatter and directory YAML;
- active/ancestor state, persisted disclosure state, filtering, pagination,
  breadcrumbs, learning-path isolation, and a mobile navigation dialog;
- light/dark/automatic theme selection with local persistence and OS changes;
- accessible content tabs and synchronized package-manager tabs, including
  arrow/Home/End keyboard behavior and persisted selection;
- semantic `details` output preserving labels, IDs, and default-open state;
- generated heading IDs and desktop/mobile tables of contents;
- per-code-block, package-command, and raw-page Markdown copy actions;
- source Markdown endpoints for all 6,882 ordinary documentation routes;
- a keyboard-accessible search dialog. The frozen checkout contains no search
  index or query protocol, so submission transparently links to Cloudflare's
  hosted search instead of fabricating local results.

## Navigation artifacts

The first implementation produced one 4.99 MB payload. Certification rejected
that design. The final generator emits a 23,719-byte manifest and 110 lazy,
route-derived product files. Median product payload is 18,338 bytes; the largest
(`cloudflare-one`) is 718,669 bytes. Every artifact is generated only from the
pinned checkout and is claimed by route verification.

## Browser verification

`tests/browser_cp7.py` starts a local HTTP server over the built output and runs
headless Chromium through Playwright. It verifies:

1. navigation filtering and active state;
2. theme cycling and reload persistence;
3. generated TOC and page-Markdown copy;
4. search dialog keyboard opening and hosted-search fallback;
5. keyboard-operated content tabs;
6. keyboard-operated package-manager tabs and command copy;
7. native disclosure toggling;
8. mobile navigation open, Escape close, and DOM restoration.

The certified run completed all eight groups with no page or console errors.
Playwright is test-only infrastructure on the Linode and is not required to
build or serve the Nift output.

## Certified reproduction

- Ordinary import: **6,882 / 6,882**.
- Tracked/build output: **9,134 / 9,134**.
- Expected index routes: **9,134**, missing **0**.
- Expected static/data/source endpoints: **7,189**, missing **0**:
  - 6,882 raw Markdown endpoints;
  - 307 shell, generated-data, and navigation artifacts.
- Python tests: **44 / 44**.
- Browser interaction groups: **8 / 8**, console errors **0**.
- REAL rendering leakage: **0**.
- Intentional findings remain: code-fence **188**, code-import **63**,
  prose-placeholder **19**, ts-type-name **2**.

Broken local references are reported but are not route-gate failures: 10,722
are links to the external same-origin `/api/` sibling application (now present
in the functional global header), 133 are live Logpush datasets, 21 are
live/proxied Workers AI models, and 121 are upstream-stale or otherwise
unclassified references.

## Gate decision

**CP7 is certified.** CP8 visual/structural parity may begin. CP10 performance
comparison remains prohibited until the planned same-hardware campaign.
