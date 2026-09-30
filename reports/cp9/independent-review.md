# CP9 Independent Re-review

Date: 2026-10-01

## Scope

The reviewer independently inspected experiment commit
`b83c5686c48849e9b82c3b3ac9de00e33d61a747`, shell commit
`b6a90044d8eb4874bb03da5e11373c8b4bb9978e`, frozen upstream commit
`bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`, and the final evidence under
`reports/cp9/`. The review covered metadata generation and auditing, static
accessibility auditing, Chromium and Vantage gates, deployment/provenance
binding, CP8 regression evidence, and preservation of `reports/cp8/`.

## Findings

- Blocking findings: none.
- Non-blocking findings: none.
- Recommendation: commit the evidence bundle separately and certify CP9.

The initial review found fail-closed gaps involving contradictory `noindex`
metadata, input values used as accessible names, optional tablist execution,
unasserted responsive menu state, sample mutability, and identification of the
Chromium Snap launcher rather than its payload. The reviewer adversarially
retested each fix and confirmed that all were closed.

## Independent Validation

- Recomputed public tree: 18,843 files, SHA-256
  `afb40cd4f348479246102bc20a4eee6607fd8aec407bf3f0abbb1e8a27c484ed`.
- All provenance-bearing reports contain the same candidate identity.
- All deployment-bound reports contain the exact verified deployment
  attestation.
- Metadata: 8,803 pages, 328 noindex pages, zero fatal findings.
- Accessibility: 8,803 pages, 400,826 controls, zero fatal findings.
- Structure: 8,803 pages, complete shell coverage, zero fatal findings.
- Route closure: 8,803 routes and 7,948 static files present, with zero
  missing, unexpected, or unclassified references.
- Chromium: 41 routes and eight responsive widths, zero violations or console
  errors.
- Vantage/WebKitGTK: four routes, zero fatal findings.
- CP8 corpus regression: 8,986 routes, 13 classified findings, zero
  unclassified findings.
- CP8 visual regression: 41 routes at four viewports, 164 comparisons and zero
  failures; all 328 source/candidate screenshots are present.
- The CP8 evidence tree is unchanged from the certified CP8 baseline.

## Residual Risks

- Dynamic browser coverage is representative: 41 Chromium routes and four
  Vantage routes, not all 8,803 pages.
- Static accessibility records 1,297 heading-order advisory routes.
- Corpus parity retains 13 documented reference-side nondeterministic or live
  input classifications.
- Route closure retains 12,331 classified external or upstream-stale
  references and zero unclassified references.

These are disclosed coverage limits or inherited reference conditions, not
CP9 certification blockers.
