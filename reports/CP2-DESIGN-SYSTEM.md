# CP2 — Upstream design-system extraction

Reference snapshot: `cloudflare/cloudflare-docs` production tree `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.

## Sources traced

CP2 was derived from the frozen upstream implementation, not by visually approximating the live site. The primary sources inspected were `src/styles/globals.css`, `src/styles/prose.css`, `src/layouts/BaseLayout.astro`, `src/layouts/DocsLayout.astro`, `src/components/Header.astro`, `src/components/Footer.astro`, `src/pages/index.astro`, `src/assets/logo.svg`, and the package manifest.

The upstream stack imports `@fontsource-variable/inter` and `@fontsource-variable/jetbrains-mono`; the pinned package manifest uses version 5.3.0 for both. The experiment references those exact package versions through jsDelivr for now. A controlled benchmark/final reproducibility run should vendor the package font assets from the frozen install so the Nift site has no CDN dependency.

## Exact tokens captured

The Nift shell carries the upstream Nimbus token values for light/dark background, foreground, card, muted, accent, sunken surfaces, Cloudflare orange primary/hover, borders and focus ring. It also preserves the upstream font stacks, Inter feature settings, grayscale font smoothing, selection treatment, reduced-motion rule, and these layout constants:

- sticky header: `3.5rem` / 56px
- sidebar: `18.75rem` / 300px
- TOC: `18rem` / 288px
- normal content max: `43.5rem` / 696px
- wide-screen content max at 1536px+: `52rem` / 832px
- H1: `2.1875rem`, weight 600, tracking `-0.025em`
- H2: `1.3rem`, weight 600, tracking `-0.015em`
- H3: `1.1rem`, weight 600, tracking `-0.01em`

The exact upstream Cloudflare mark SVG has been carried into `public/assets/cloudflare-logo.svg` rather than redrawn.

## Shell implemented

The Nift page is now split into reusable `head`, `header`, `sidebar`, `toc`, and `footer` inputs. The page geometry follows the upstream DocsLayout: sticky 56px global header, fixed-width desktop sidebar, centered content column, right TOC at XL widths, responsive sidebar removal, mobile dialog navigation, and full-width footer beneath the content row.

The pre-paint theme contract follows upstream `BaseLayout.astro`: preference key `ui-mode`, values `light|dark|auto`, `data-mode`, `data-theme`, `data-nb-pref`, `data-nb-state`, OS-theme following for auto mode, and cross-tab synchronization. The temporary theme button cycles the same preference states; its final icon/UI is deferred to the component/functionality checkpoints.

## Fidelity boundary

CP2 establishes the design-system primitives and documentation shell; it does **not** claim final pixel parity yet. Nimbus/Tailwind emits a large amount of component-specific CSS and the actual 6,882-page content/component surface has not been imported. Homepage-specific structural-grid/landing components, exact footer content/wordmark treatment, final SVG control icons, code-block styling, and individual MDX components belong to CP3–CP7.

The CP1 screenshot harness cannot yet execute a local upstream build in this sandbox because the full upstream checkout/npm dependency tree is unavailable. Consequently the CP2 shell has been source-derived but the screenshot gate remains a deferred verification item. It must be run against the frozen upstream build on the planned Linode before final parity can be certified; differences found there are defects, not accepted approximations.

## Build verification

The attached Nift v4.3.0 development binary successfully builds the CP2 project. After the shell changes the build completed successfully in roughly seven milliseconds in this environment. This is a development sanity check only, not a benchmark result.

## CP2 result

The exact upstream design tokens, font identities/versions, primary visual asset, responsive layout constants, theme contract, and reusable Nift shell architecture are now recorded and implemented. CP3 can inventory the content model without having to invent styling or page geometry. Final visual certification remains intentionally tied to the controlled upstream-vs-Nift comparison environment.
