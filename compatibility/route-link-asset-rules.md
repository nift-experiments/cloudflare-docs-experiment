# CP3 route, link and asset contract

Pinned source: `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.

## Routes

For `src/content/docs/<path>.md[x]`, strip the content root and extension, collapse a terminal `/index`, and emit a trailing-slash route. Examples: `workers/index.mdx` → `/workers/`; `dns/manage-dns-records/index.mdx` → `/dns/manage-dns-records/`. Root `index` maps to `/`. Any two sources mapping to one route are a hard error. Frontmatter `external_link` is not emitted as a normal local document route; it is navigation metadata and must preserve the upstream destination. Dynamic families under `src/pages` and data collections are inventoried separately and implemented as generated routes in CP5/CP6.

## Links

Absolute `/...` links retain their path and query/fragment. `#fragment` links remain page-local. Relative document links are resolved against the *source document directory*, normalized, then converted through the same route function; `.md`/`.mdx` and terminal `index` are removed. External `http(s)`, `mailto:`, `tel:` and protocol-relative URLs are passed through. Fragment text is not rewritten: heading-id generation must match upstream. A link whose local target cannot be resolved is a hard conversion/crawl failure.

## Assets

`~/assets/...` maps to the frozen upstream `src/assets/...` object and must be copied or deterministically emitted under the Nift public asset tree without changing bytes unless upstream itself transforms that asset. `/...` public references map to frozen `public/...`. Relative image/file references resolve against the source document first. Missing local assets are hard failures. Astro-transformed images require a manifest recording source, output URL, dimensions/format and transformation so parity can be checked rather than approximated.

## Unknown syntax policy

Unknown frontmatter keys, named JSX/MDX components, container directives, route collisions, unresolved local links and missing local assets all fail the importer. No unknown construct may be converted to plain text or discarded as a fallback.
