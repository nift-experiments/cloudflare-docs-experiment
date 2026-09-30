<p>Try the Dynamic Workers <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground">playground</a> to write or import code from GitHub, bundle it at runtime, execute it in a Dynamic Worker, and view real-time logs.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p><img src="/assets/upstream/images/dynamic-workers/dw-playground.png" alt="Dynamic Workers Playground UI" /></p>
<h2 id="what-this-demo-shows">What this demo shows</h2>
<ul>
<li><strong>Runtime bundling</strong> — Uses <a href="https://www.npmjs.com/package/@cloudflare/worker-bundler"><code>@cloudflare/worker-bundler</code></a> to resolve npm dependencies and compile TypeScript inside a Worker</li>
<li><strong>Dynamic execution</strong> — Loads bundled code into an isolated Dynamic Worker</li>
<li><strong>Caching</strong> — Reuses previously bundled Workers when the source has not changed</li>
<li><strong>Real-time output</strong> — Streams the response body, console logs, execution timing, and bundle metadata back to the client</li>
</ul>
<h2 id="bundling-code-at-runtime">Bundling code at runtime</h2>
<p>The playground uses <a href="https://www.npmjs.com/package/@cloudflare/worker-bundler"><code>@cloudflare/worker-bundler</code></a> to compile TypeScript, resolve npm dependencies, and produce modules the Worker Loader can execute.</p>
<p>Pass source files and a <code>package.json</code> to <code>createWorker()</code>, which resolves dependencies and returns bundled modules ready to load as a Dynamic Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8451.md")
</div>
<h2 id="caching-dynamic-workers">Caching Dynamic Workers</h2>
<p><code>env.LOADER.load()</code> creates a new Dynamic Worker on every call. To avoid re-bundling unchanged code, use <code>env.LOADER.get(id, callback)</code> instead. The runtime returns an existing Worker on a cache hit, or calls your callback to build one on a miss:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8452.md")
</div>
<p>In the playground, you can see this in action — run the same Dynamic Worker twice and the second request shows a cached result with 0ms cold start, since the build and load phases are skipped entirely.</p>
<h2 id="observability-with-tail-workers">Observability with Tail Workers</h2>
<p>When you run code in the playground, console output from the Dynamic Worker streams back to the browser in real time. Under the hood, this works through a <a href="/workers/observability/logs/tail-workers/">Tail Worker</a> pipeline:</p>
<ol>
<li>A Tail Worker (<code>DynamicWorkerTail</code>) captures <code>console.log</code> output from the Dynamic Worker.</li>
<li>Logs are forwarded to a <code>LogSession</code> Durable Object.</li>
<li>The Durable Object streams them to the client over WebSocket.</li>
</ol>
<p>To wire this up, include the Tail Worker in the <code>tails</code> array when creating the Dynamic Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8453.md")
</div>
<p>For more information on how to capture and stream logs from Dynamic Workers, refer to <a href="/dynamic-workers/usage/observability/">Observability with Dynamic Workers</a>.</p>
<h2 id="running-locally">Running locally</h2>
<p>Clone the repo and start the dev server:</p>
<pre><code class="language-sh">npm install&#10;npm run dev&#10;</code></pre>
