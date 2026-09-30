# CP10 Controlled Benchmark Methodology

Status: **FROZEN BEFORE FORMAL RESULTS**

Methodology version: 4

Frozen: 2026-10-01

## Purpose

Measure Nift and Astro on the same frozen Cloudflare Docs corpus and machine,
after CP9 certified the reproduced Nift output. Results apply only to the
commands, corpus, machine, and versions recorded here. They are not blanket
claims about either tool.

## Immutable Source Anchors

- Cloudflare upstream commit:
  `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`
- Cloudflare upstream tree:
  `289e5331c2e6f257f37b40fa2910b434c906d3e9`
- CP9 Nift implementation commit:
  `b83c5686c48849e9b82c3b3ac9de00e33d61a747`
- CP9 shell commit: `b6a90044d8eb4874bb03da5e11373c8b4bb9978e`
- CP9 shell tree: `5f43acda3212cdd10351af0e021365cfdfd0acd1`
- CP9 shell repository:
  `https://github.com/nift-experiments/cloudflare-docs-experiment.git`
- CP9 certification commit:
  `9df944a87c365220967cae4679f209b8ecc5544c`
- CP9 public-tree SHA-256:
  `afb40cd4f348479246102bc20a4eee6607fd8aec407bf3f0abbb1e8a27c484ed`

Benchmark work uses disposable clones or worktrees at these commits. The shell
is an independently verified checkout outside the Nift project's `public/`
directory; the parent repository's historical gitlink alone is not accepted as
proof of shell state. Only files in the shell commit's `git ls-files` manifest
are copied into `public/`, with path/type/mode/size/SHA-256 verified after the
copy. Both repositories' HEAD, tree, tracked-file diff, and tracked-file
manifest are checked before and after phases. Generated Nift output is governed
by complete output manifests. CP8/CP9 sources and evidence are not modified to
prepare a run.

## Primary Machine

Provision one fresh Linode solely for CP10:

- Planned type: `g6-standard-6` (Linode 16 GB)
- Advertised resources: 6 shared vCPUs, 16 GB RAM, 320 GB storage
- Region: `us-central` (Dallas)
- Image: Ubuntu 24.04 LTS
- Backups: disabled
- Swap: disabled for qualification and every formal run
- Filesystem: the image default ext4 filesystem

The historical frozen-Astro observation peaked at 8,354,548 KiB process RSS.
The 8 GB tier is therefore disqualified before testing. The 16 GB tier is the
smallest standard tier with material headroom and is the same plan class on
which the historical build completed. Qualification requires three successful
clean Astro builds, no cgroup OOM events, zero swap, and aggregate cgroup
`memory.peak` below 90% of physical RAM. If it fails, the exact replacement is
`g6-standard-8` (32 GB, 8 shared vCPUs), and qualification restarts. Nift and
Astro must use the same final machine.

Before formal runs, `reports/cp10/machine.json` will freeze the Linode ID/type,
region, CPU model/topology, RAM, disk, filesystem, kernel, OS, swap state, CPU
governor, tool versions, binary hashes, and source heads. Recording that actual
identity completes this pre-result methodology; it is not a result-driven rule
change.

## Toolchains

- Nift: Nift 4.5.0 Linux x86-64 release archive from
  `https://github.com/nift-dev/nift/releases/download/v4.5.0/nift-4.5.0-linux-x86_64.tar.gz`,
  archive SHA-256
  `856fcc401333aced5c492b92050caf6252cfec3fb9d15a51b2676af363599694`.
  The extracted binary's SHA-256 is recorded before testing.
- Node: Node 24.x, with the exact patch version recorded before testing.
- pnpm: 12.4.2, matching the prior frozen-source setup; its exact version and
  executable hash are recorded.
- Astro: repository-pinned 7.3.2 from the frozen lockfile install.
- GNU `/usr/bin/time` with `LC_ALL=C` and an explicit `-f` field format supplies
  process wall, user, system, CPU percentage, and peak RSS measurements without
  locale-dependent parsing.

Qualification first attempts one clean Astro build with Node's default heap. If
it succeeds, all formal runs use the default. If it fails specifically from
JavaScript heap exhaustion, the failure evidence is retained and
`NODE_OPTIONS=--max-old-space-size=8192` is used for qualification and every
formal Astro run. The value is never changed between scenarios.

## Preparation And Footprint

Preparation is reported separately from site builds:

1. Clone/fetch and checkout each immutable source.
2. Astro dependency install from the upstream root:
   `pnpm install --frozen-lockfile`.
3. Astro remote-data preparation from the upstream root:
   `pnpm run fetch:assets`. The frozen archive contains `skills/`, `.tmp/`, and
   generated `src/content/docs/logs/logpush/logpush-job/datasets/*/*.md` files.
   Its canonical manifest records each relative path, type, mode, byte size,
   nanosecond mtime, and file SHA-256. Before each build, those paths are
   cleared, restored with archived modes/mtimes, and verified against the
   manifest. Network fetching is not included in site-build timing.
4. Nift corpus conversion in a disposable experiment checkout, with tracked
   files from the separately verified shell checkout copied into `public/`
   first: `python3 tools/import_corpus.py
   /srv/cp10/upstream`, then `python3 tools/generate_families.py
   /srv/cp10/upstream`, then `git restore --source=HEAD --
   content/index.html`, then repeat the manifest-driven shell-file copy into
   `public/` and verify it. Import and family generation are timed separately.
   The machine manifest pins Python, PyYAML, and cmarkgfm versions and records
   all cleanup commands. This is a setup cost, not an ordinary Nift rebuild
   cost.

Each of the three install repetitions starts from a fresh upstream clone with
no `node_modules` and a new empty dedicated pnpm store; registry network access
is allowed and reported as a network-dependent setup measurement, never a build
headline. Each conversion repetition starts from a fresh experiment clone at
the certification commit and a fresh independently verified shell checkout;
`content/` is removed only there, `.nift/tracked.json` and
`content/index.html` are restored from HEAD, and the exact sequence above runs.
An environment lock recording Python and package versions is committed before
qualification or any measured setup run.

Footprint evidence records checkout size separately from toolchain size. It
includes Astro `node_modules` bytes/files, accurately derivable package count,
Astro output bytes/files, Nift binary bytes/SHA-256 and runtime dependencies,
Nift output bytes/files, and each source checkout's bytes/files.

## Exact Run States

The harness creates fresh disposable benchmark clones, never cleans a certified
working repository, and executes these states:

- Nift clean: verify both repositories; delete exactly the generated output
  paths named by `.nift/tracked.json`; delete `.nift/public/`; preserve and
  re-verify copied shell/static assets against the external shell checkout's
  tracked-file manifest; then run `nift build --all`.
- Nift incremental baseline: complete a clean build, retain output and
  `.nift/public/` metadata, and verify no source change before an edit/no-change
  run.
- Astro clean: verify the upstream repository and frozen remote-input manifest;
  delete `dist/`, repository-root `.astro/`, and `node_modules/.astro/`; preserve
  the remaining frozen `node_modules`.
- Astro incremental baseline: start Astro clean, run
  `INCREMENTAL_BUILD=true pnpm exec astro build` untimed, and retain `dist/` and
  `node_modules/.astro/` before an edit/no-change run.

Every edit repetition creates its own verified baseline, applies the declared
edit, times one command, verifies output, restores the exact source bytes, and
re-establishes baseline output outside timing. Source and output path/SHA-256
manifests are retained. Source mtimes and tool metadata state are recorded; an
edit is always made after baseline creation.

Every no-change repetition restores and verifies the same archived baseline
output and complete tool metadata (`.nift/public/` for Nift; `dist/` and
`node_modules/.astro/` for Astro), then times exactly one invocation. Recorded
runs are not chained on state mutated by earlier recorded runs.

## Run Discipline

- Record HEAD, tree, and tracked-file status before and after every phase. Use
  normal `git status --porcelain` for ordinary checkouts and verify the external
  shell checkout independently.
- Reject a phase if tracked benchmark source changed unexpectedly.
- Disable unattended package activity and avoid concurrent benchmark jobs.
- Run each timed command in its own cgroup v2. Record aggregate
  `memory.current`, `memory.peak`, `memory.events`, `memory.swap.current`, and
  cgroup/system pressure-stall counters in addition to GNU `time -v`. Sample
  load, memory, swap I/O, disk, and guest-visible CPU frequency every second.
- A run is invalid only for a nonzero command exit, correctness failure,
  cgroup `oom`/`oom_kill`, nonzero swap, machine reboot, ENOSPC, monitoring
  failure, or overlapping CP10 benchmark process. No load or timing threshold
  invalidates a slow run. If a machine-level condition affects a paired round,
  rerun the whole pair. Original invalid and replacement runs remain published.
- Paired series use six rounds in fixed `ABBAAB` first-tool order, where A is
  Nift and B is Astro. Scenario order is fixed as A through F below.
- Each ordinary series gets one unrecorded warmup per tool after setup.
- Primary series use warm filesystem caches and six recorded runs.
- Clean full builds also get four recorded guest-page-cache-dropped runs per
  tool, ordered `ABBA`. Root runs `sync` and writes `3` to
  `/proc/sys/vm/drop_caches` immediately before each run. This does not claim to
  clear provider, disk-controller, CPU, or tool-internal caches. These results
  are supplementary and are not mixed with warm medians.
- Nift targeted single-page gets three warmups and 30 recorded runs, each from
  the same reconstructed baseline. Small-batch Nift explicit-target gets two
  warmups and 20 similarly reconstructed unpaired runs so launch/timer noise
  does not dominate. Small-batch Nift-normal versus Astro-automatic is a
  separate six-round `ABBAAB` paired series.
- Setup/install and corpus-conversion series use three recorded runs because
  they are expensive preparation measurements rather than headline rebuilds.

## Statistics

Machine-readable raw JSON and CSV retain every run. Each series reports count,
median, arithmetic mean, minimum, maximum, population standard deviation, user
CPU, system CPU, CPU percentage where available, GNU peak RSS, and cgroup
aggregate peak memory. Paired comparisons report per-round wall-time ratios and
a deterministic 10,000-resample paired bootstrap 95% confidence interval
(seed `20261001`). If that interval crosses parity, the difference is labelled
inconclusive. Median wall time is primary. No best-run cherry-picking and no
post-result trimming are permitted.

## Scenarios And Commands

### A. Tool-native Clean Full Production Build

- Nift: `nift build --all`
- Astro: `pnpm exec astro build`

Astro's documented `pnpm build` consists of network-backed preparation followed
by `astro build`. Preparation is frozen and measured separately, so the timed
site builder is invoked directly.

This is a tool-native generated-page comparison, not an equal empty-output
assembly boundary. Nift's architecture keeps static shell/assets in its final
`public/` tree, so those files are present before timing; Astro copies its
`public/` static inputs into an initially empty `dist/` during timing. Reports
must disclose Nift's pre-staged static file/byte count next to this result and
must not describe the series as complete-site assembly speed. An additive setup
estimate is separately reported from clone/tool acquisition, measured native
preparation phases, and first build, with components and aggregation stated; it
is not folded into the generated-page headline or called a directly timed
end-to-end series.

### B. No-change Rebuild

After an untimed successful incremental baseline with no source changes:

- Nift: `nift build`
- Astro: `INCREMENTAL_BUILD=true pnpm exec astro build`

The Astro command is the implementation behind the repository's documented
`build:incremental` script; direct invocation omits only the frozen, separately
measured `prebuild:incremental` network preparation. This is production
incremental build, not dev-server HMR.

### C. One-page Edit, Normal Incremental Workflow

Representative route: `/workers/get-started/guide/`.

- Astro source: `src/content/docs/workers/get-started/guide.mdx`
- Nift source: `content/workers/get-started/guide/index.md`
- Edit: append the same visible sentence, `CP10 benchmark edit.`, as an ordinary
  paragraph at the end of each source body.
- Nift command: `nift build`
- Astro command: `INCREMENTAL_BUILD=true pnpm exec astro build`

### D. One-page Edit, Explicit Target

- Nift: `nift build workers/get-started/guide/`
- Nift tracked page name is verified from `.nift/tracked.json` before runs.

Astro's supported incremental command automatically chooses invalidated pages
but does not accept a selected production route. Therefore the result states:
**Astro: no equivalent explicit targeted production build command in this
project/toolchain.** Scenario C is the separately labelled supported incremental
counterpart; it is not presented as an explicit route-targeting command. Dev
HMR, SSR, on-demand rendering, custom plugins, and output copying are excluded.

### E. Small-batch Edit

The five frozen routes are `/workers/get-started/`,
`/workers/get-started/guide/`, `/workers/get-started/dashboard/`,
`/workers/get-started/prompting/`, and
`/workers/get-started/quickstarts/`. Their Astro sources are the five matching
MDX files under `src/content/docs/workers/get-started/`; their Nift sources are
the five matching `index.md` files under `content/workers/get-started/`. The
same visible sentence is added to all five.

- Nift explicit-target command: one `nift build` invocation followed by the
  five exact tracked names.
- Nift normal command: `nift build` is also measured for this edit.
- Astro: `INCREMENTAL_BUILD=true pnpm exec astro build`, reported as automatic
  incremental rather than explicit target selection.

Nift normal and Astro automatic use the balanced six-round paired schedule.
Nift explicit-target is a separately labelled 20-run series and is not used to
compute a paired speedup against Astro.

### F. Shared Dependency/Template Edit

- Nift source: append `<!-- CP10 shared-template edit -->` to
  `templates/head.html`, a declared dependency of all page templates.
- Astro source: append the same inert HTML comment after `</html>` in
  `src/layouts/BaseLayout.astro`.
- Commands: each tool's normal incremental workflow.

Before timing, the harness creates each edited correctness reference with an
independent clean full build: clean state, declared edit, then `nift build
--all` or non-incremental `pnpm exec astro build`. Complete output path/type/
mode/size/SHA-256 manifests from those builds and their diff from clean baseline
become the frozen expected trees and changed-path sets. Every timed incremental
or explicit-target output must equal its independently clean-built edited tree
byte-for-byte, prove markers are present, and restore exact baselines.

## Nift Worker Qualification

Before comparison series, run a declared Nift-only sweep for `build-threads`
values `-1` and `-2`. These request the final machine's vCPU count and twice
that count respectively; actual counts are recorded. Each gets one warmup and
eight `nift build --all` runs in `ABBAABBA` order.

The repository/default `-1` setting remains the primary formal configuration
regardless of the sweep outcome. `-2` is reported as a clearly labelled tuned
alternative and is never substituted into headline comparisons. This preserves
worker qualification without selecting a favorable result.

## Correctness Gates

Performance is invalid unless correctness passes:

- Source heads, trees, tracked-file manifests, and worktree cleanliness match
  the immutable anchors, including the independent shell checkout.
- Nift reports all 8,803 tracked pages up to date after complete builds.
- A complete path/type/mode/size/SHA-256 manifest is frozen for each clean
  baseline tree. Every full/no-change output must match its tool's manifest;
  Nift certified-tree scenarios also require 8,803 HTML routes and 18,843
  certified public files.
- Astro and Nift use separate frozen references; their output byte counts are
  not assumed to be identical.
- Edit scenarios must exactly match their pre-formal changed-path manifest,
  prove all expected dependents changed, prove no unclassified output changed,
  and contain the marker in designated representative pages.
- Restore steps prove source hashes return exactly to baseline.
- Targeted scenarios gate on content hashes and separately record mtimes;
  mtimes are never treated as correctness proof.
- Final worktrees must be clean and at their original heads. The external shell
  must have its original HEAD/tree and no tracked changes; copied shell files
  and expected Nift output must match their complete manifests.

## Independent Review And Publication

An independent reviewer must challenge command equivalence, preparation
accounting, cache state, machine state, worker selection, edit semantics,
memory measurement, regenerated-file counting, statistics, dependency
footprint, correctness, and wording. Any methodological defect is documented
and affected series are rerun for both tools. No benchmark website is pushed or
published until that review passes.
