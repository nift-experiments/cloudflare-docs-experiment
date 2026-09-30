<p>Review how the Workers Vitest integration runs your tests, how it isolates tests from each other, and how it imports modules.</p>
<h2 id="run-tests">Run tests</h2>
<p>When you run your tests with the Workers Vitest integration, Vitest will:</p>
<ol>
<li>Read and evaluate your configuration file using Node.js.</li>
<li>Run any <a href="https://vitest.dev/config/#globalsetup"><code>globalSetup</code></a> files using Node.js.</li>
<li>Collect and sequence test files.</li>
<li>For each Vitest project, depending on its configured isolation and concurrency, start one or more <a href="https://github.com/cloudflare/workerd"><code>workerd</code></a> processes, each running one or more Workers.</li>
<li>Run <a href="https://vitest.dev/config/#setupfiles"><code>setupFiles</code></a> and test files in <code>workerd</code> using the appropriate Workers.</li>
<li>Watch for changes and re-run test files using the same Workers if the configuration has not changed.</li>
</ol>
<h2 id="isolation-model">Isolation model</h2>
<p>Storage isolation is per test file. Each test file gets its own storage environment, and any writes to storage during a test file are not visible to other test files. The Workers Vitest integration reuses Workers and their module caches between test runs where possible. A copy of all auxiliary <code>workers</code> exists in each <code>workerd</code> process.</p>
<p>By default, test files run concurrently. To make test files share the same storage (for example, for integration tests that depend on shared state), use the Vitest flags <code>--max-workers=1 --no-isolate</code>.</p>
<h2 id="modules">Modules</h2>
<p>Each Worker has its own module cache. As Workers are reused between test runs, their module caches are also reused. Vitest invalidates parts of the module cache at the start of each test run based on changed files.</p>
<p>The Workers Vitest plugin runs code inside a Cloudflare Worker that Vitest would usually run inside a <a href="https://nodejs.org/api/worker_threads.html">Node.js Worker thread</a>. To make this possible, the plugin <strong>automatically injects</strong> the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag"><code>nodejs_compat</code></a>, [<code>no_nodejs_compat_v2</code>] and <a href="/workers/configuration/compatibility-flags/#commonjs-modules-do-not-export-a-module-namespace"><code>export_commonjs_default</code></a> compatibility flags. This is the minimal compatibility setup that still allows Vitest to run correctly, but without pulling in polyfills and globals that are not required. If you already have a Node.js compatibility flag defined in your configuration, the Vitest plugin does not add those flags.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17328.md")
</aside>
