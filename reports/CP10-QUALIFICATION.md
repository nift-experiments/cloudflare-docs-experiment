# CP10 Machine And Tool Qualification

Status: **QUALIFIED FOR FORMAL RUNS**

Date: 2026-10-01

Methodology: `reports/CP10-BENCHMARK-METHODOLOGY.md` version 5

## Machine Decision

Linode `107157732` (`g6-standard-6`, 6 shared vCPUs, 16 GB RAM, Dallas) passed
the predeclared qualification rule. Three successful Astro clean builds used
10.58-11.38 GiB aggregate peak memory, at most 72.9% of physical RAM, with no
swap or cgroup OOM event. The 32 GB fallback is not required.

Node's default heap completed all successful builds. Formal Astro runs therefore
do not set `NODE_OPTIONS`.

## Frozen Astro Inputs

Today's live OpenAPI schema no longer contained an operation referenced by the
frozen source. Two attempted builds failed at
`/rules/custom-errors/api-calls` and remain in raw evidence. They are excluded
from performance results.

The compatible OpenAPI input is now pinned to Cloudflare `api-schemas` commit
`9027404ade37d6f84ff4b17e027c2a4f842ef82e` (2026-09-18 11:17:43 UTC),
immediately before the historical successful build. Its `openapi.json` SHA-256
is `425a9164160673b5e2390672df0c786fc96693cd2ed0673aa383a9df8f00723e`.
Skills and Logpush inputs come from the frozen CP8 upstream checkout. The full
input manifest is retained in `reports/cp10/qualification/`.

## Nift Worker Sweep

Each setting used eight infrastructure-valid `nift build --all` runs. The final
output matched all 28,111 paths and file contents in the certified CP9 tree,
including 8,803 HTML routes, with no missing static files or unclassified
references.

| Setting | Workers | Median wall | Mean wall | Range | Wall SD | Median cgroup peak | Maximum cgroup peak |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `-1` | 6 | 4.585 s | 4.880 s | 4.24-7.08 s | 0.886 s | 492.8 MiB | 493.9 MiB |
| `-2` | 12 | 4.755 s | 4.868 s | 4.17-6.53 s | 0.682 s | 511.7 MiB | 533.6 MiB |

The repository/default `-1` remains the primary configuration as predeclared.
It was also 3.6% faster by median and used less memory. `-2` remains a labelled
tuned alternative only.

## Astro Qualification

Successful clean builds with default heap:

| Run | Wall | GNU peak RSS | Cgroup peak | Swap/OOM |
| --- | ---: | ---: | ---: | --- |
| 1 | 571.37 s | 7,844.4 MiB | 10.58 GiB | none |
| 2 | 570.23 s | 7,981.3 MiB | 11.38 GiB | none |
| 3 | 570.27 s | 7,741.5 MiB | 11.03 GiB | none |

The reference output contains 9,022 pages, 12,447 files, and 1,977,890,517
bytes. Clean runs expose an Astro concurrency nondeterminism affecting 580
files: an identical SVG can receive one of two source-derived names, changing
dependent references. These raw diffs are retained and require normalization or
classification before formal correctness acceptance.

Astro's documented `INCREMENTAL_BUILD=true` mode completed, but rebuilt all
9,022 pages in both qualification invocations:

| Operation | Wall | Cgroup peak |
| --- | ---: | ---: |
| Incremental baseline | 582.43 s | 12.20 GiB |
| No-change incremental | 626.52 s | 12.47 GiB |

This mode remains the legitimate Astro incremental command in formal scenarios;
the report will not claim that it provides a fast no-change path on this corpus.

## Preliminary Context

The Nift `-1` qualification median was 4.585 seconds; the first
correctness-valid Astro clean build was 571.37 seconds. Their provisional ratio
is 124.6x. This is not the final headline comparison because it is not yet the
balanced six-round formal series.
