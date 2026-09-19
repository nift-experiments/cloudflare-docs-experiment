# Pre-pause Development Snapshot — Nift vs Astro footprint/build (2026-09-19)

This is a **development-environment snapshot**, not the controlled CP10 benchmark.
The two implementations were **not** measured under equivalent conditions (the
frozen Astro install cannot run on this VPS). It preserves evidence before the VPS
is torn down and records the number that matters most: the Nift reproduction needs
**no Node runtime and no `node_modules`**.

---

## 1. Environment

- Host: Linode **g6-standard-1** (1 vCPU / 2 GB / 50 GB), Ubuntu 24.04, `$12/mo`.
- Nift: **v4.3.0**, binary `/usr/local/bin/nift` = **2,729,392 bytes (~2.7 MB)**.
- Experiment checkout: `/srv/cloudflare-docs-experiment` (working tree md5-identical
  to pushed `stage` commit `dcc8d92`).
- Frozen upstream: `/srv/cloudflare-docs-upstream` at SHA
  `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.
- Certified state: **9,134 tracked pages**.
- No unrelated CPU/RAM-heavy processes running during measurement.

## 2. Nift clean build — `nift build --all`

Command (exact): `/usr/bin/time -v nift build --all`

| Run | Wall | User | Sys | Peak RSS | Pages | Exit |
|---|---|---|---|---|---|---|
| 1 | 15.11 s | 9.44 s | 5.23 s | 60,220 KB | 9,134 | 0 |
| 2 | 14.57 s | 9.42 s | 4.70 s | 60,240 KB | 9,134 | 0 |
| 3 | 15.85 s | 10.28 s | 4.98 s | 60,220 KB | 9,134 | 0 |
| **Median** | **15.11 s** | | | **60,220 KB (~58.8 MiB)** | | |

An earlier batch (same certified tree, clean via `rm -rf .nift/public` +
`nift build --repair`) gave 17.22 / 15.58 / 16.29 s at ~70.9 MiB RSS; the
`--all` flag is the canonical clean build and the numbers above are preferred.

## 3. Nift no-op build — `nift build`

Wall **3.15 s**; peak RSS **12,232 KB (~11.9 MiB)**; exit 0; all 9,134 up to date.

## 4. Nift project footprint

`du -sh` (1024-based blocks) vs `du -sb` (logical bytes) differ substantially
because the tree contains many small files (14,755 body files); both are given.

| Path | `du -sh` | `du -sb` (bytes) |
|---|---|---|
| Checkout incl `.git` | 940M | 738,628,598 |
| `.git` | 2.0M | 893,195 |
| Working tree excl `.git` | 938M | 737,297,985 |
| Generated `public/` | 712M | 683,270,997 |
| — `public/assets` (staged upstream `src/assets` copy) | 451M | — |
| `content/` | 149M | 38,658,534 |
| — `content/.markup/bodies/` | 59M | 5,821,562 (14,755 files) |
| `.nift/` build metadata | 74M | 13,114,871 |
| Nift binary | 2.6M | 2,729,392 |

**Interpretation warning:** the ~938M working tree is **inflated** by the generated
`public/` output (712M, of which ~451M is the copied upstream asset corpus staged
for link fidelity). It is **not** a runtime/build dependency footprint. Nift itself
requires **no Node runtime and no `node_modules`** (0 files).

## 5. Frozen Astro source checkout

`/srv/cloudflare-docs-upstream`, SHA verified `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`.

- Astro **7.3.2** (devDependency), **pnpm** project (`pnpm-lock.yaml`), build = `astro build`.
- Current frozen source checkout (no build run):
  - working tree excl `.git`: **611,154,889 bytes**;
  - `.git`: **1,487,826,626 bytes**;
  - total incl `.git`: **2,098,981,515 bytes**;
  - `src`: ~549M (`src/assets` ~451M, `src/content` ~95M);
  - `public`: ~71M;
  - files excl `.git`: 13,333.
- **Node is not installed on this VPS; `node_modules` is absent; `dist` is absent.**
  Dependencies were **not** installed for this snapshot (frozen-state policy).

## 6. Historical Astro baseline (different hardware — do NOT compare directly)

From `reports/benchmarks/astro-baseline.json` and `reports/benchmarks/` raw files,
measured on the now-destroyed Linode **g6-standard-6** (6 vCPU / 16 GB), Node
v24.21.0, pnpm 12.4.2, upstream SHA `bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf`:

- **9,025** pages generated;
- clean build: **433.46 s** wall, peak RSS **~8.35 GB**;
- no-op rebuild: 411.08 s, peak RSS ~8.13 GB;
- `node_modules`: **~1.3 GB**;
- `dist`: ~2.0 GB / 12,450 files.

**Historical Astro baseline from different hardware — NOT directly comparable to
the current Nift development snapshot.** Do not compute or advertise a
"Nift is Nx faster" ratio from these numbers.

## 7. Comparison table (development snapshot)

| Metric | Nift reproduction | Frozen Astro site |
|---|---:|---:|
| Pages/output routes | 9,134 | 9,025 (historical) |
| Clean build wall | 15.11 s (median, 1 vCPU) | 433.46 s (historical, 6 vCPU) |
| Peak RSS | ~58.8 MiB | ~8.35 GB (historical) |
| No-op build | 3.15 s | 411.08 s (historical) |
| `node_modules` | **0 / not required** | ~1.3 GB (historical); absent on this VPS |
| Working size excl `.git` | 737,297,985 B (incl generated `public/`) | 611,154,889 B (source only) |
| `.git` | 893,195 B | 1,487,826,626 B |
| Complete checkout | 738,628,598 B | 2,098,981,515 B |
| Generated output | 683,270,997 B | ~2.0 GB (historical `dist`) |
| Version / runtime | Nift v4.3.0, 2.7 MB binary | Astro 7.3.2, Node v24.21.0 |

## 8. Observable facts worth recording (not a benchmark claim)

- Nift rebuilt **9,134 pages** on a 1-vCPU/2-GB machine in a median **15.11 s**
  peaking at ~58.8 MiB.
- The Nift reproduction has **no Node / `node_modules`** runtime or build dependency.
- The historical frozen Astro install had ~1.3 GB `node_modules` and its build
  peaked above 8 GB RSS.
- **CP10 must rerun both implementations on identical hardware** with their frozen
  dependency state before any comparative performance conclusions.

## 9. Raw evidence

- `/tmp/nift_all_1.log`, `/tmp/nift_all_2.log`, `/tmp/nift_all_3.log` (on VPS;
  VPS is disposable).
- Machine-readable Astro baseline: `reports/benchmarks/astro-baseline.json`,
  `reports/benchmarks/astro-build-run1-summary.txt`,
  `reports/benchmarks/astro-build-run2-summary.txt`,
  `reports/benchmarks/linode-machine-spec.md`.