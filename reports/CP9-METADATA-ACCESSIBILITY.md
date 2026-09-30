# CP9 Metadata, Accessibility, and Browser Verification

Status: **CERTIFIED**

Date: 2026-10-01

Certified URL: `http://172.105.161.70:8000`

## Certified Identity

- Frozen upstream commit: `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`
- Frozen upstream tree: `289e5331c2e6f257f37b40fa2910b434c906d3e9`
- Experiment implementation commit: `b83c5686c48849e9b82c3b3ac9de00e33d61a747`
- Shell implementation commit: `b6a90044d8eb4874bb03da5e11373c8b4bb9978e`
- Public file count: 18,843
- Public tree SHA-256: `afb40cd4f348479246102bc20a4eee6607fd8aec407bf3f0abbb1e8a27c484ed`

`reports/cp9/candidate-provenance.json` was generated only after all three
source worktrees were clean. `reports/cp9/deployment.json` verifies an empty
checksum rsync diff, the expected server implementation and document root, the
sole listener on port 8000, matching representative HTTP response hashes, and
HTTP 404 responses for repository metadata.

## Metadata

The fail-closed full-corpus audit in `reports/cp9/metadata.json` checked all
8,803 structural pages. It verified title, canonical, sitemap link, social
metadata uniqueness and values, description consistency, JSON-LD contracts,
Markdown alternates, robots directives, and sitemap inclusion/exclusion.

- Pages checked: 8,803
- Intentional noindex pages: 328
- Sitemap routes: 8,315
- Fatal findings: 0

An upstream custom `noindex` directive on `/ai-gateway/models/` is now honored
by generation: the page has one normalized robots directive, no JSON-LD, and no
sitemap entry.

## Accessibility

The static audit in `reports/cp9/accessibility.json` checked document language,
main landmarks, accessible control names, ARIA references, iframe titles, and
keyboard reachability contracts over the complete structural corpus.

- Pages checked: 8,803
- Controls checked: 400,826
- Fatal findings: 0
- Heading-order advisories: 1,297 routes

The generated shell also provides a working skip link, labelled controls,
focusable overflow regions, valid link-card markup, non-color link cues, and
improved control/text contrast.

## Browser Gates

`reports/cp9/browser-chromium.json` binds the hosted run to the candidate and
deployment attestations. The exact 41-route sample is digest-pinned. axe-core
4.10.3 is pinned by SHA-256 and every WCAG A/AA violation is fatal. The gate
also verifies skip-link activation, search focus restoration, tablist Home/End
and Arrow behavior, horizontal overflow, and navigation/sidebar/menu state at
eight responsive boundaries.

- Chromium: `153.0.8010.47 snap`
- Chromium payload SHA-256:
  `5d4f4ce28120d4f6ab7566306c26b9a766227ca76da70f44ed322e4ee04b5bbb`
- axe-core: `4.10.3`
- Routes: 41
- Fatal violations: 0
- Console errors: 0

`reports/cp9/browser-vantage.json` independently exercises WebKitGTK through
Vantage's stable agent API on four representative routes.

- Vantage: 0.1.11
- Native stack: GTK 4.22.4; WebKitGTK 2.52.6
- Routes: 4
- Fatal findings: 0

## Regression Closure

- Unit suite: 127 tests passed.
- Nift status: all 8,803 tracked files up to date.
- Structural audit: 8,803 pages with complete header, footer, and navigation
  coverage; zero fatal findings.
- Route closure: 8,803 routes and 7,948 static files present; zero missing,
  unexpected, or unclassified references.
- Leakage audit: 8,803 HTML pages; zero real leakage.
- CP8 corpus regression: 8,986 endpoints; 13 existing classified
  reference-side findings; zero unclassified findings.
- CP8 visual regression: 41 routes x 4 viewports = 164 comparisons; zero
  failures.
- CP8 evidence preservation: `reports/cp8/` is unchanged.

## Independent Review

The first independent review found several real fail-closed weaknesses. Those
were fixed in commits `b2f8cf80667a5aa0ee218a39b80b499d68f8f07e` and
`b83c5686c48849e9b82c3b3ac9de00e33d61a747`, covered by adversarial tests, and
then subjected to a fresh deployment and complete evidence run.

The independent re-review in `reports/cp9/independent-review.md` found no
remaining blocking or non-blocking findings and recommended certification.

## Scope Limits

This checkpoint certifies the frozen CP9 candidate identified above. It does
not claim browser execution over every page or blanket conformance to every
accessibility success criterion. Representative browser coverage is paired
with complete static corpus audits. Performance comparisons remain deferred to
CP10 on identical hardware with frozen dependency state.

## Decision

CP9 is certified. Metadata, static accessibility, keyboard and responsive
browser behavior, deployment identity, and CP8 regression closure all pass the
defined fail-closed gates for the exact candidate tree above.
