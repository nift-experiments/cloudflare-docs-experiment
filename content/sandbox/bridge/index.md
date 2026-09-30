<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h3>
@markup("md", "content/.markup/bodies/13577.md")
</aside>
<p>The sandbox bridge is a reference-implementation Cloudflare Worker that exposes the <a href="/sandbox/api/">Sandbox SDK</a> as an HTTP API. Any HTTP client — Python script, Node.js service, CI pipeline — can create and control sandboxes without writing a Worker. You deploy the Worker in <strong>your</strong> account; it is not a Cloudflare-hosted shared API.</p>
<h2 id="why-use-the-bridge">Why use the bridge</h2>
<p>The Sandbox SDK is designed for use within Cloudflare Workers. If your application runs outside of the Workers ecosystem, it cannot interact with sandboxes directly.</p>
<p>The bridge exposes the Sandbox SDK as a standard HTTP API so you can create and control sandboxes from any language or platform.</p>
<p>Key <a href="/sandbox/api/">Sandbox SDK methods</a> map to individual HTTP endpoints. The bridge adds authentication, input validation, workspace path containment, and an optional <a href="/sandbox/bridge/http-api/#warm-pool">warm pool</a> for instant container boot.</p>
<h2 id="deploy">Deploy</h2>
<p>Deploy the bridge Worker to your Cloudflare account:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/sandbox-sdk/tree/main/bridge/worker"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>The button deploys the Worker and generates a <code>SANDBOX_API_KEY</code> secret for authentication. When deployment finishes, note your Worker URL and API key — every example on this page uses them.</p>
<details class="nb-details"><summary>Manual deployment</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13578.md")
</div></details>
<h3 id="container-image">Container image</h3>
<p>The bridge <code>Dockerfile</code> extends the <a href="https://hub.docker.com/r/cloudflare/sandbox"><code>cloudflare/sandbox</code></a> base image and pre-installs common agent tooling:</p>
<ul>
<li><strong>Languages</strong>: Python 3.13, Node.js, Bun</li>
<li><strong>Tools</strong>: git, ripgrep, curl, wget, jq, tar, sed, gawk, procps</li>
</ul>
<p>Customize the <code>Dockerfile</code> to add languages, system packages, or tools your workloads need.</p>
<h2 id="usage">Usage</h2>
<p>All examples assume the following environment variables are set:</p>
<pre><code class="language-sh">export SANDBOX_API_URL=https://cloudflare-sandbox-bridge.&lt;your-subdomain&gt;.workers.dev&#10;export SANDBOX_API_KEY=&lt;your-token&gt;&#10;</code></pre>
<h3 id="create-a-sandbox-and-run-a-command">Create a sandbox and run a command</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13582.md")
</div></div>
<h3 id="write-and-read-files">Write and read files</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13586.md")
</div></div>
<h2 id="keep-the-bridge-updated">Keep the bridge updated</h2>
<p>The bulk of the bridge logic is in the <code>@cloudflare/sandbox</code> package. To pull in the latest improvements:</p>
<ol>
<li>Update the SDK dependency:</li>
</ol>
<pre><code class="language-sh">npm update @cloudflare/sandbox&#10;</code></pre>
<ol start="2">
<li>Redeploy:</li>
</ol>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Check the <a href="https://github.com/cloudflare/sandbox-sdk/releases">sandbox-sdk releases</a> for changes to the <code>Dockerfile</code> or bridge configuration that may require manual updates.</p>
<h2 id="source-code-and-examples">Source code and examples</h2>
<p>The bridge source code and examples are available on GitHub:</p>
<ul>
<li><a href="https://github.com/cloudflare/sandbox-sdk/tree/main/bridge">Bridge source</a> — Worker, Dockerfile, deploy script, and OpenAPI schema.</li>
<li><a href="https://github.com/cloudflare/sandbox-sdk/tree/main/bridge/examples/workspace-chat">Workspace chat example</a> — Full-stack chat application with a file browser sidebar.</li>
<li><a href="https://github.com/cloudflare/sandbox-sdk/tree/main/bridge/examples/basic">Basic example</a> — One-shot Python coding agent using the OpenAI Agents SDK.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/bridge/http-api/">HTTP API reference</a> — Complete route reference for the bridge API.</li>
<li><a href="/sandbox/get-started/">Getting started</a> — Build your first sandbox application directly on Workers.</li>
<li><a href="/sandbox/concepts/architecture/">Architecture</a> — How the Sandbox SDK layers Workers, Durable Objects, and Containers.</li>
<li><a href="/sandbox/api/">API reference</a> — Complete Sandbox SDK method reference.</li>
<li><a href="/sandbox/tutorials/openai-agents/">OpenAI Agents SDK tutorial</a> — Build a Python coding agent with the bridge.</li>
</ul>
