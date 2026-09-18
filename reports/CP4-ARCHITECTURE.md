# CP4 — Nift page architecture

CP4 establishes reusable Nift composition for Cloudflare's docs layout rather than page-specific output.

## Layers

- `templates/docs.html`: canonical documentation-page shell.
- `head.html`, `header.html`, `footer.html`: global chrome.
- `sidebar.html` and `mobile-sidebar.html`: desktop/mobile navigation surfaces.
- `breadcrumbs.html`, `article-header.html`, `toc.html`: route/page context.
- `pagination.html`, `page-actions.html`: lower-page navigation and actions.
- `@content` remains the single article-body insertion point.

The architecture preserves the CP2 design tokens and three-column geometry. Content pages will be tracked independently in CP6 and can share this shell, allowing a template change to fan out through Nift's dependency graph rather than duplicating chrome into source files.

## Route/data policy

CP3's route contract remains authoritative. CP4 does not invent alternate URL schemes. Product sidebar trees, breadcrumbs, TOC entries, prev/next relationships and page metadata are generated from the frozen upstream corpus during CP6 and supplied to the shared layers rather than hard-coded per page.

## Gate

The existing landing page is intentionally retained. CP4 supplies the docs architecture needed by imported pages; it does not claim full-site import or visual parity before CP6.
