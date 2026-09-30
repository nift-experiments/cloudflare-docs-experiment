<p>A <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers">starter template</a> for deploying a Worker that loads and runs <a href="/dynamic-workers/">Dynamic Workers</a>.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<h2 id="what-it-does">What it does</h2>
<p>This template demonstrates how to use the <a href="/workers/runtime-apis/bindings/worker-loader/">Worker Loader API</a> to execute code at runtime. The host Worker exposes an <code>/api/run</code> endpoint that accepts code from the frontend, loads it into a sandboxed Dynamic Worker, and returns the result.</p>
<p>Use this pattern for AI agents that need to execute a snippet of code to complete an action.</p>
<h2 id="configuration">Configuration</h2>
<p>Add a <code>worker_loaders</code> binding to your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8449.md")
</div>
<h2 id="loading-and-executing-a-dynamic-worker">Loading and executing a Dynamic Worker</h2>
<p>In this example:</p>
<ul>
<li><code>env.LOADER.load()</code> creates a one-off dynamic isolate</li>
<li><code>globalOutbound: null</code> blocks all outbound network access from the Dynamic Worker</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8450.md")
</div>
<h2 id="running-locally">Running locally</h2>
<pre><code class="language-sh">npm install&#10;npm run dev&#10;</code></pre>
