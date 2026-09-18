# CP1 — comparison and parity machinery

Status: **complete for the pre-port baseline; designed to grow into the full-corpus gate.**

`tools/parity.py` compares identical routes on two HTTP origins and records HTTP status, response bytes, normalized HTML hashes, structural equality, bounded unified diffs, and optional headless-Chromium screenshots at an explicit viewport.

```sh
python3 tools/parity.py --upstream http://127.0.0.1:1111 --nift http://127.0.0.1:8000 --screenshots
```

`parity/golden-routes.txt` spans the homepage, product landings, deep ordinary docs, Workers APIs, R2, Pages, Zero Trust, WAF, SSL, cache, learning paths, changelog and style guide. It is a fast development gate only, never final certification.

As CP2–CP7 land, generate a full route manifest from frozen upstream and add pixel/image diffing, computed-style probes, internal-link/asset crawling, console-error capture, metadata/head comparison, accessibility/keyboard checks and multiple responsive viewports.

Chromium is available and screenshots require no Node package. That is deliberate: the test harness should not create a `node_modules` footprint that contaminates the experiment's dependency-size story.

For the final comparison, follow the Omarchy experiment's breadth: clean/incremental/no-op build time, peak memory, install/dependency and `node_modules` footprint, source/build complexity, output size, cold/warm runs, one-page edit, shared-template edit, navigation/data fan-out edits, setup/deployment requirements and AI/agent developer experience. Record these only after parity is established.
