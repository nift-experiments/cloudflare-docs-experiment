# CP10 Controlled Benchmark Results

Status: **THREE-RUN ASTRO INCREMENTAL CAMPAIGN COMPLETE; TWO FORMAL-VALID RUNS**

Date: 2026-10-01

This report uses only retained CP10 evidence. It reports the completed warm
clean comparison, completed Nift-only series, and exactly three final Astro
incremental invocations. It makes no claim for other corpora, machines,
versions, or commands.

## Immutable Basis

- Method: `reports/CP10-BENCHMARK-METHODOLOGY.md`, frozen version 6
  (2026-10-01). Formal setup records version 6 in
  `reports/cp10/formal-targeted-edit/setup/targeted-setup.json`.
- Upstream source: commit
  `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`, tree
  `289e5331c2e6f257f37b40fa2910b434c906d3e9`.
- Nift project/certification: commit
  `9df944a87c365220967cae4679f209b8ecc5544c`, tree
  `242396895a6458512b7acd38fed8f26530f172e4`; implementation commit
  `b83c5686c48849e9b82c3b3ac9de00e33d61a747`; shell commit/tree
  `b6a90044d8eb4874bb03da5e11373c8b4bb9978e` /
  `5f43acda3212cdd10351af0e021365cfdfd0acd1`.
- Toolchain: Nift 4.5.0 executable SHA-256
  `4aca09ccf7244f30e99349e6043281cde694183ee436d55b7ac84e0a0b84240d`;
  Node 24.21.0 executable SHA-256
  `7fde7b8afa198da66257f42ee2001d874c7355631e6d1579a5fb5ef1f246df4c`;
  pnpm 12.4.2 native executable SHA-256
  `df602b81c2e2f75c72904664cf2ee2ce50e1394bef1cb2a153ed4c08d99bc6e4`;
  Astro 7.3.2 from the frozen lockfile. See
  `reports/cp10/environment-lock.json`.
- Machine: Linode `107157732`, `g6-standard-6`, Dallas `us-central`, six shared
  AMD EPYC 7642 vCPUs, 16,769,368,064 bytes RAM, no swap, ext4, Ubuntu 24.04.4
  LTS, kernel `6.8.0-134-generic`, cgroup v2. See
  `reports/cp10/machine.json`.
- Astro remote OpenAPI input: `api-schemas` commit
  `9027404ade37d6f84ff4b17e027c2a4f842ef82e`, `openapi.json` SHA-256
  `425a9164160673b5e2390672df0c786fc96693cd2ed0673aa383a9df8f00723e`.

GNU `/usr/bin/time` with `LC_ALL=C` measured the command process tree. Cgroup v2
recorded aggregate peak memory. Timings include only the declared build command;
clone/install, remote-input restoration, corpus conversion, cache-state setup,
source editing, output manifesting, correctness checks, and restoration are
outside the boundary. These are warm guest-page-cache results. Nift clean timed
`nift build --all` after deleting its 8,803 tracked outputs and metadata, while
10,040 non-tracked files totalling 643,073,411 bytes were already staged in
`public/`; those counts are derived from `.nift/tracked.json` and
`reports/cp10/formal-clean/nift-r01-manifest.json`. Astro clean timed
`pnpm exec astro build` after deleting `dist/` and Astro caches, so Astro copied
its static inputs during timing. This is therefore a tool-native generated-page
comparison, not an equal empty-output complete-site assembly comparison.

## Formal Clean Full Build

Evidence: `reports/cp10/formal-clean/`. Fixed paired round order was Nift/Astro,
Astro/Nift, Nift/Astro. No valid run was discarded. Raw values below are copied
from each committed `*-rNN.json`; RSS is the GNU-time maximum and cgroup peak is
aggregate memory.

| Tool | Wall seconds, rounds 1-3 | GNU peak RSS KiB, rounds 1-3 | Cgroup peak bytes, rounds 1-3 |
| --- | --- | --- | --- |
| Nift | 5.29, 5.18, 5.03 | 187832, 188232, 183240 | 713728000, 708198400, 700067840 |
| Astro | 567.49, 571.48, 570.96 | 8073748, 7658732, 8065812 | 11845435392, 12016066560, 11753394176 |

| Tool / metric | Median | Mean | Min | Max | Population SD | CV |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Nift wall (s) | 5.180 | 5.167 | 5.030 | 5.290 | 0.107 | 2.06% |
| Astro wall (s) | 570.960 | 569.977 | 567.490 | 571.480 | 1.771 | 0.31% |
| Nift GNU peak RSS (MiB) | 183.430 | 182.065 | 178.945 | 183.820 | 2.212 | 1.21% |
| Astro GNU peak RSS (MiB) | 7,876.770 | 7,746.840 | 7,479.230 | 7,884.520 | 189.255 | 2.44% |
| Nift cgroup peak (MiB) | 675.391 | 674.564 | 667.637 | 680.664 | 5.350 | 0.79% |
| Astro cgroup peak (MiB) | 11,296.688 | 11,321.671 | 11,208.910 | 11,459.414 | 103.782 | 0.92% |

Astro/Nift wall ratios by paired round were 107.276x, 110.324x, and 113.511x.
Their median/mean/min/max/population-SD were respectively 110.324x, 110.370x,
107.276x, 113.511x, and 2.546x. The primary ratio of tool medians was 110.224x;
the predeclared 10,000-resample paired bootstrap (seed `20261001`) gave a 95%
interval of 107.276x to 113.511x, which does not cross parity. Ratios of medians
were 42.942x for GNU peak RSS and 16.726x for aggregate cgroup peak. Both
first-three wall CVs were below the 15% extension threshold, with no committed
invalidity or noisy-neighbour finding, so the series correctly stopped at n=3
rather than extending to n=6. The small sample remains a limitation.

### Correctness

Nift was exact: all three manifests matched the certified content manifest with
zero added, removed, or content-changed paths. Each comparison records 15,685
mtime-only entries, which are non-content metadata. The output had 28,111
entries, 18,843 files, 8,803 HTML routes, and 832,646,534 bytes. See
`nift-rNN-manifest.json` and `nift-rNN-comparison.json` in the clean evidence
directory.

Astro's raw trees differed, but the committed clean normalization report found
all three pairwise comparisons equivalent after narrow normalization: r1/r2 raw
counts were 1 added, 580 changed, 1 removed; r1/r3 were 2/590/2; and r2/r3 were
1/588/1. Every normalized comparison was 0/0/0 and equal. The observed classes
and union path counts were package-manager UUID (349), combobox random ID (253),
checkbox random ID (1), sampled agent prompts (9), playground multipart boundary
(1), Shiki rule order (1), sitemap build-time fallback (1), and content-identical
SVG aliases (16). Source provenance and paths are in
`reports/cp10/formal-clean/astro-normalization-report.json`.

The current committed normalizer, `tools/cp10_astro_normalize.py`, also contains
a fail-closed ninth proven class, `svg-dot-pattern-id`, for paired Nimbus
`nb-dots-*` SVG pattern definitions and references. That class was added in
commit `1de652ab8fb4a44896421eb0e3663ed8214d4d3f`, after the clean normalization
report was committed in `1b0e2a38f85f0a581c07470b819463ad32044d77`.
Consequently, this report does **not** claim that the committed clean trees were
rescanned with the later class or that the class occurred in them; the clean
equivalence claim rests on the eight classes actually recorded in the committed
normalization report.

## Formal Explicit One-Page Target: Nift Only

Evidence: `reports/cp10/formal-targeted-edit/`. After three warmups, each of 30
reconstructed baselines appended `CP10 benchmark edit.` to
`content/workers/get-started/guide/index.md` and timed
`nift build workers/get-started/guide/`.

- Raw wall seconds: `0.15, 0.14, 0.15, 0.14, 0.14, 0.14, 0.16, 0.14, 0.15, 0.15, 0.16, 0.16, 0.15, 0.14, 0.15, 0.14, 0.15, 0.14, 0.14, 0.15, 0.25, 0.15, 0.25, 0.15, 0.14, 0.15, 0.14, 0.15, 0.16, 0.15`.
- Raw GNU peak RSS KiB: `12000, 11996, 11996, 11868, 11996, 11996, 11864, 12000, 11740, 12000, 11868, 11740, 11868, 11872, 11872, 11996, 11992, 11996, 12000, 11872, 11996, 11868, 11868, 11996, 11868, 11736, 11872, 11872, 11868, 11996`.
- Raw cgroup peak bytes: `7282688, 7278592, 7286784, 7274496, 7278592, 7278592, 7282688, 7282688, 7282688, 7278592, 7278592, 7282688, 7282688, 7278592, 7282688, 7278592, 7278592, 7282688, 7282688, 7278592, 7290880, 7282688, 7278592, 7278592, 7282688, 7282688, 7282688, 7274496, 7278592, 7274496`.

| Metric | Median | Mean | Min | Max | Population SD | CV |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Wall (s) | 0.150 | 0.154 | 0.140 | 0.250 | 0.026 | 17.12% |
| GNU peak RSS (MiB) | 11.594 | 11.636 | 11.461 | 11.719 | 0.083 | 0.71% |
| Cgroup peak (MiB) | 6.943 | 6.943 | 6.938 | 6.953 | 0.003 | 0.05% |

All 30 validations were formal-valid and exactly matched the independently
clean-built edited reference. In every run exactly one output was touched and
content-changed, `workers/get-started/guide/index.html`, with no added or removed
path. Astro has no equivalent explicit targeted production-build command in
this project/toolchain. Its supported automatic incremental command belongs to
the separate normal-workflow scenario; therefore no Astro value and no paired
ratio are reported here.

## No-Change Incremental Builds

Evidence: `reports/cp10/formal-no-change-nift-only/`. Each reconstructed
baseline timed `nift build` without a source change.

| Metric | Raw rounds 1-3 | Median | Mean | Min | Max | Population SD | CV |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Wall (s) | 0.98, 0.90, 0.87 | 0.900 | 0.917 | 0.870 | 0.980 | 0.046 | 5.06% |
| GNU peak RSS (KiB) | 12380, 12512, 12636 | 12512 | 12509.333 | 12380 | 12636 | 104.529 | 0.84% |
| Cgroup peak (bytes) | 9650176, 9908224, 9691136 | 9691136 | 9749845.333 | 9650176 | 9908224 | 113232.157 | 1.16% |

All three companion validations were formal-valid and record zero added,
removed, content-changed, mtime-only, regenerated, or touched output files.

The final Astro campaign is retained at
`reports/cp10/astro-final-incremental/`. It ran exactly three production
incremental commands, each from the same restored archive, with no additional
clean build or warmup. All three commands exited successfully, were
infrastructure-valid, and reported 9,022 pages built.

| Astro round | Wall | Aggregate cgroup peak | Correctness status |
| --- | ---: | ---: | --- |
| 1 | 680.27 s | 13,067,665,408 B | normalized-equivalent |
| 2 | 688.26 s | 11,542,552,576 B | normalized-equivalent |
| 3 | 688.10 s | 13,632,647,168 B | failed closed |

Across all three completed invocations, the observed wall median was 688.10 s
and the observed aggregate-peak median was 13,067,665,408 bytes. These are
descriptive campaign observations, not a formal paired speedup. Round 3 changed
`_nimbus/shiki.css` and one corresponding HTML page with different Shiki
declaration bodies and token classes. Because that is a real rendered-style
difference rather than an approved random identifier or ordering class, the
normalizer correctly rejected it. No replacement build was run. The strict
formal result is therefore two valid runs out of three, and no Astro/Nift
no-change ratio is reported.

## Nift Normal And Batch Incremental Workflows

Evidence: `reports/cp10/nift-one-normal/`,
`reports/cp10/nift-batch-normal/`, and
`reports/cp10/nift-batch-targeted/`. These Nift-only runs use the declared lean
validation contract: marker presence, designated output hashes, reported build
counts, exact source restoration, and infrastructure validity. They do not walk
or serialize the complete output tree for each run.

| Workflow | n | Wall median | Wall range | Aggregate peak median | Rebuilt/validated outputs |
| --- | ---: | ---: | ---: | ---: | ---: |
| One-page normal `nift build` | 3 | 0.94 s | 0.89-0.95 s | 10,129,408 B | 1 |
| Five-page normal `nift build` | 3 | 0.98 s | 0.94-0.99 s | 10,563,584 B | 5 |
| Five-page explicit target | 20 | 0.16 s | 0.15-0.21 s | 8,681,472 B | 5 |

Every run was valid. The explicit five-page series named all five tracked routes
in one invocation and changed exactly five outputs in every run. Astro has no
equivalent explicit named-route production command, so no cross-tool ratio is
reported for either targeted series.

## Nift Shared-Template Fan-Out

Evidence: `reports/cp10/nift-shared-normal/`. Each of three reconstructed
baselines appended the inert marker
`<meta name="cp10-benchmark" content="shared-template-edit">` to
`templates/head.html` and timed `nift build`.

| Metric | Raw rounds 1-3 | Median | Mean | Min | Max | Population SD |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Wall (s) | 4.73, 4.96, 4.89 | 4.89 | 4.86 | 4.73 | 4.96 | 0.0963 |
| Aggregate peak (bytes) | 444665856, 445517824, 444751872 | 444751872 | 444978517.333 | 444665856 | 445517824 | 382960.789 |

All three runs reported 8,803 files rebuilt successfully. Correctness checks
proved marker presence and changed hashes for five frozen representative outputs.
Regeneration outside that representative set is supported by Nift's reported
count rather than individual output hashes; no full-tree scan was performed.

## Dependency And Filesystem Footprint

Evidence: `reports/cp10/footprint/cp10-footprint.json`. Logical byte totals use
sorted recursive `lstat`, count each hard-linked object identity once, and do not
follow symlinks.

| Item | Logical bytes / count |
| --- | ---: |
| Nift executable | 3,497,360 B |
| Nift project `node_modules` | absent |
| Nift source checkout, excluding Git/metadata/output | 255,100,730 B |
| Nift `.nift` metadata | 49,979,498 B |
| Nift generated output | 870,706,566 B |
| Astro direct dependencies / dev dependencies | 0 / 105 |
| Astro pnpm resolved store entries | 1,120 |
| Astro lockfile snapshots | 1,327 |
| Astro `node_modules`, excluding `.astro` | 1,194,890,090 B |
| Astro installed regular files, excluding `.astro` | 55,232 |
| Astro generated `node_modules/.astro` cache | 1,528,202,322 B |

The Astro `node_modules` total occupies 1,366,536,192 allocated bytes before its
separately reported generated `.astro` cache. Generated output and metadata are
not dependency size and remain separate categories.

## Qualification Context, Not Formal Results

Qualification evidence is in `reports/cp10/qualification/` and summarized by
`reports/cp10/qualification-summary.json` and `reports/CP10-QUALIFICATION.md`.
These values selected the machine and Nift's predeclared default; they are not
substitutes for formal paired scenarios.

| Qualification series | n | Wall median | Wall mean | Min-max | Population SD | Cgroup peak median / max |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Nift `build-threads=-1` (6 workers) | 8 | 4.585 s | 4.880 s | 4.24-7.08 s | 0.886 s | 492.8 / 493.9 MiB |
| Nift `build-threads=-2` (12 workers) | 8 | 4.755 s | 4.868 s | 4.17-6.53 s | 0.682 s | 511.7 / 533.6 MiB |

The predeclared `-1` configuration remained formal primary. The three successful
default-heap Astro qualification clean runs were 571.37, 570.23, and 570.27 s;
GNU peak RSS was 8,032,684, 8,172,860, and 7,927,272 KiB; cgroup peak was
11,359,162,368, 12,224,098,304, and 11,836,850,176 bytes. No swap or OOM event
occurred. Two earlier failed attempts using incompatible OpenAPI inputs remain
excluded with evidence. Qualification-only Astro incremental baseline and
no-change observations were 582.43 s and 626.52 s and each reported 9,022 pages;
they are not formal no-change results and are not paired above. The qualification
document names methodology version 5, whereas the frozen current method and
formal setup name version 6; this report follows the formal v6 binding and leaves
the historical label visible rather than silently rewriting it.

## Interpretation

The evidence supports a narrow workload-fit conclusion. For this frozen corpus,
machine, and tool-native warm clean boundary, Nift completed generated-page work
with substantially lower wall time and measured memory than Astro. For agent
iteration that can identify one route, Nift's explicit target rebuilt and
validated one output at a 0.150 s median; its normal one-page workflow took
0.940 s, its five-page normal workflow took 0.980 s, and its normal no-change
command took 0.900 s while touching nothing. A shared-template edit regenerated
all 8,803 pages in 4.890 s median. This indicates that explicit targeting can be
operationally useful for route-aware agents, while also showing that command
selection and fan-out matter. It does not establish a general Astro iteration
claim: Astro has no equivalent explicit-route command here, and its supported
incremental workflow rebuilt all 9,022 pages in each final invocation. Because
only two of three outputs passed normalized correctness, that campaign is not
promoted to a formal cross-tool ratio.

## Completion Boundary

The requested final Astro campaign stopped after exactly three invocations. No
replacement was run for the correctness-invalid third result. Supplementary
methodology-v6 scenarios that do not have retained formal evidence remain
unreported rather than inferred.

All statistics above were recomputed from committed JSON using arithmetic mean,
ordinary median, and population SD (`sqrt(sum((x-mean)^2)/n)`). The paired
bootstrap follows `tools/cp10_benchmark.py:741-793`. Benchmark state and command
construction are in `tools/cp10_formal_clean.py`,
`tools/cp10_formal_edit.py`, `tools/cp10_formal_no_change.py`, and
`tools/cp10_astro_final_incremental.py`.
