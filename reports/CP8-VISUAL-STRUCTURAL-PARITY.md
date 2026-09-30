# CP8 Visual and Structural Parity

Status: **CERTIFIED**

CP8 certifies the Nift candidate against frozen Cloudflare Docs revision
`bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.

## Candidate Identity

- Upstream tree: `289e5331c2e6f257f37b40fa2910b434c906d3e9`
- Experiment source: `b2c1fc57165947872a72e3f08a8dcf254642f4db`
- Shell source: `b6dd64dbb39cf3ae6cb96bf03172d7cf6d328235`
- Public tree SHA-256: `e5489e215549de0a0a5d13c9765526f7d59c6bfe4ee36c3aacb91c7f2436c4f5`
- Public files: 18,841
- Certified URL: `http://172.105.161.70:8000`

The candidate was generated from a tracked-only `git archive` snapshot of the
pinned upstream revision. Deployment evidence verifies the complete candidate
tree with rsync checksums, the exact server implementation and document root,
exclusive listener ownership, representative HTTP byte hashes, and denial of
preserved deployment metadata.

## Gate Results

| Gate | Result |
| --- | --- |
| Corpus parity | 8,986/8,986 endpoints; 12 exact classified findings; 0 unclassified; 0 stale required classifications |
| Structural audit | 8,803 pages; 0 fatal findings; header/footer/navigation on every page |
| Route closure | 8,803 expected and actual HTML routes; 0 missing, unexpected, or missing static files; 0 unclassified references |
| Navigation closure | Root and per-product navigation JSON references included in route verification |
| Leakage | 8,803 HTML pages; 0 real conversion-leakage findings |
| Browser interactions | 11 checks; 0 console errors |
| Visual matrix | 41 routes x 4 viewports = 164 comparisons; 0 failures |
| Tests | 113 tests plus 57 subtests passed |

The visual gate independently fails at a significant-pixel ratio of 20% or
greater. The certified matrix's maximum ratio was `0.18845`.

## Classified Differences

The 12 corpus findings are exact route-and-reason classifications tied to the
frozen upstream SHA. They cover non-frozen middlecache/build-time agent data,
ignored live Logpush data, a mutable OpenAPI mismatch that causes an upstream
500, valid body-H1 normalization, and process-local ComponentsUsage inventory
nondeterminism. Any additional or changed reason remains unclassified and
audit-fatal. Only demonstrably intermittent reference-runtime entries may be
absent without becoming stale; deterministic classifications remain stale-fatal.

## Evidence

- `reports/cp8/candidate-provenance-certified.json`
- `reports/cp8/deployment-certified.json`
- `reports/cp8/corpus-parity-certified-final.json`
- `reports/cp8/structural-certified-final.json`
- `reports/cp8/route-closure-certified-final.json`
- `reports/cp8/leakage-certified-final.json`
- `reports/cp8/browser-certified-final.json`
- `reports/cp8/parity-certified-final/summary.json`
- `reports/cp8/parity-certified-final/*.png`

## Independent Review

The final independent review recomputed the candidate digest, checked all
evidence bindings and gate implementations, reran the test suite, and found no
blockers, inconsistencies, false-green paths, or missing proof. Verdict:
`CERTIFY CP8`.

CP9 remains a separate metadata, accessibility, and browser-verification phase.
CP10 performance work must not begin before CP9 is independently certified.
