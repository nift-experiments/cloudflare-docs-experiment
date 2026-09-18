# CP5 compatibility implementation registry

`compatibility/content-model.json` is the census/classification contract. `tools/import_cloudflare.py` is the strict staging converter. The converter must never silently discard an uppercase MDX component: an unknown component aborts the import.

Static primitives are emitted as semantic HTML with `nb-*` classes. Browser-interactive components retain `data-cf-component` identities so their exact upstream behaviour can be implemented/tested without contaminating Nift's build layer. Data-generated components use the same identity strategy and are resolved from frozen upstream data during the full import. This separation is intentional: Nift owns build-time composition; ordinary browser JS owns browser behaviour.

The current converter is a CP5 compatibility foundation, not the CP6 bulk import. Full-corpus execution against the pinned checkout remains the gate that proves the registry is exhaustive.
