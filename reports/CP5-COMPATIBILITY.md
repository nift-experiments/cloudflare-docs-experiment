# CP5 — MDX/component compatibility foundation

CP5 turns the CP3 classification into executable migration machinery.

## Strict importer

`tools/import_cloudflare.py` is dependency-free and reads `compatibility/content-model.json`. It strips build-only MDX imports/exports, preserves frontmatter metadata for the tracking-generation stage, reduces known JSX constructs, and **fails on unknown uppercase MDX components**. It also fails when a known nested construct cannot be reduced safely. Silent flattening is forbidden.

## Rendering classes

Static documentation primitives (`Aside`, cards, steps, badges, details, file trees, etc.) receive semantic HTML and source-derived `nb-*` styling. Tabs/package-manager surfaces receive browser hooks. Data-generated and interactive Cloudflare-specific components retain explicit `data-cf-component` identities rather than being falsely represented as completed static equivalents.

That last distinction is important: CP5 establishes a lossless compatibility boundary. Exact implementations for calculators, diagrams, data catalogs and other complex components can be filled in and parity-tested against upstream without the importer erasing their identity.

## Tests

`tests/test_import_cloudflare.py` covers static nesting, interactive/data identities and the unknown-component fatal gate. All tests pass in the checkpoint workspace.

## Remaining proof

The runtime does not contain the full frozen Cloudflare checkout. Therefore CP5 does **not** claim a zero-unknown full-corpus result. Before CP6 can certify import completion, run the CP3 census and CP5 importer over SHA `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`; every discovered construct must be classified and implemented to the required parity level.
