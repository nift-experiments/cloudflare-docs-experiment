<p>Configure how the Sandbox SDK communicates with containers using transport modes.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13534.md")
</aside>
<h2 id="overview">Overview</h2>
<p>The Sandbox SDK supports three transport modes for communication between the Durable Object and the container:</p>
<ul>
<li><strong>HTTP transport</strong> (default) - Each SDK operation makes a separate HTTP request to the container.</li>
<li><strong>NEW: RPC transport</strong> - All SDK operations are multiplexed over a single persistent WebSocket connection. Will replace HTTP as the default transport in future. Available since 0.9.1.</li>
<li><strong>Deprecated: WebSocket transport</strong> - All SDK operations are multiplexed over a single persistent WebSocket. Superseded by RPC transport which uses an improved protocol.</li>
</ul>
<h2 id="when-to-use-rpc-transport">When to use RPC transport</h2>
<p>Use the RPC transport when your Worker or Durable Object makes many SDK operations per request. This avoids hitting <a href="/workers/platform/limits/#subrequests">subrequest limits</a>.</p>
<h3 id="subrequest-limits">Subrequest limits</h3>
<p>Cloudflare Workers have subrequest limits that apply when making requests to external services, including container API calls:</p>
<ul>
<li><strong>Workers Free</strong>: 50 subrequests per request</li>
<li><strong>Workers Paid</strong>: 1,000 subrequests per request</li>
</ul>
<p>With HTTP transport (default), each SDK operation (<code>exec()</code>, <code>readFile()</code>, <code>writeFile()</code>, etc.) consumes one subrequest. Applications that perform many sandbox operations in a single request can hit these limits.</p>
<h3 id="how-rpc-transport-helps">How RPC transport helps</h3>
<p>RPC transport establishes a single persistent connection to the container and multiplexes all SDK operations over it. The WebSocket upgrade counts as <strong>one subrequest</strong> regardless of how many operations you perform afterwards.</p>
<p><strong>Example with HTTP transport (4 subrequests):</strong></p>
<pre><code class="language-typescript">await sandbox.exec(&quot;python setup.py&quot;);&#10;await sandbox.writeFile(&quot;/app/config.json&quot;, config);&#10;await sandbox.exec(&quot;python process.py&quot;);&#10;const result = await sandbox.readFile(&quot;/app/output.txt&quot;);&#10;</code></pre>
<p><strong>Same code with RPC transport (1 subrequest):</strong></p>
<pre><code class="language-typescript">// Identical code - transport is configured via environment variable&#10;await sandbox.exec(&quot;python setup.py&quot;);&#10;await sandbox.writeFile(&quot;/app/config.json&quot;, config);&#10;await sandbox.exec(&quot;python process.py&quot;);&#10;const result = await sandbox.readFile(&quot;/app/output.txt&quot;);&#10;</code></pre>
<p>RPC transport also removes the <a href="/workers/runtime-apis/rpc/#limitations">32 MiB limitation</a> that the HTTP transport has. Pass a <code>ReadableStream</code> instance to the <code>writeFile()</code> method.</p>
<pre><code class="language-js">const req = await fetch(&quot;https://example.com/archive.tar.gz&quot;);&#10;await sandbox.writeFile(&quot;/archive.tar.gz&quot;, req.body);&#10;</code></pre>
<h2 id="configuration">Configuration</h2>
<p>Set the <code>SANDBOX_TRANSPORT</code> environment variable in your Worker's configuration. The SDK reads this from the Worker environment bindings (not from inside the container).</p>
<h3 id="http-transport-default">HTTP transport (default)</h3>
<p>HTTP transport is the default and requires no additional configuration.</p>
<h3 id="rpc-transport">RPC transport</h3>
<p>Enable RPC transport by adding <code>SANDBOX_TRANSPORT</code> to your Worker's <code>vars</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13535.md")
</div>
<p>No application code changes are needed. The SDK automatically uses the configured transport for all operations.</p>
<h2 id="transport-behavior">Transport behavior</h2>
<h3 id="connection-lifecycle">Connection lifecycle</h3>
<p><strong>HTTP transport:</strong></p>
<ul>
<li>Creates a new HTTP request for each SDK operation</li>
<li>No persistent connection</li>
<li>Each request is independent and stateless</li>
</ul>
<p><strong>RPC transport:</strong></p>
<ul>
<li>Establishes a WebSocket connection on the first SDK operation</li>
<li>Maintains the persistent connection for all subsequent operations</li>
<li>Connection is closed when the sandbox sleeps or is evicted</li>
<li>Automatically reconnects if the connection drops</li>
</ul>
<h3 id="streaming-support">Streaming support</h3>
<p>All transports support streaming operations (like <code>exec()</code> with real-time output):</p>
<ul>
<li><strong>HTTP transport</strong> - Uses Server-Sent Events (SSE)</li>
<li><strong>RPC transport</strong> - Uses WebSocket streaming messages</li>
</ul>
<p>Your code remains identical regardless of transport mode.</p>
<h3 id="error-handling">Error handling</h3>
<p>All transports provide identical error handling behavior. The SDK automatically retries on transient errors (like 503 responses) with exponential backoff.</p>
<p>WebSocket-specific behavior:</p>
<ul>
<li>Connection failures trigger automatic reconnection</li>
<li>The SDK transparently handles WebSocket disconnections</li>
<li>In-flight operations are not lost during reconnection</li>
</ul>
<h2 id="choosing-a-transport">Choosing a transport</h2>
<p>We expect the RPC transport to replace the default HTTP transport in a future release. New functionality may support only the RPC transport. Switching to use it now will avoid migrations in the future.</p>
<h2 id="migration-guide">Migration guide</h2>
<p>Switching between transports requires no code changes.</p>
<h3 id="switch-from-http-to-rpc">Switch from HTTP to RPC</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="requires-staged-deployment">Requires staged deployment</h3>
@markup("md", "content/.markup/bodies/13533.md")
</aside>
<p>Add <code>SANDBOX_TRANSPORT</code> to your <code>wrangler.jsonc</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13536.md")
</div>
<p>Then deploy:</p>
<pre><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<h3 id="switch-from-rpc-to-http">Switch from RPC to HTTP</h3>
<p>Remove the <code>SANDBOX_TRANSPORT</code> variable (or set it to <code>&quot;http&quot;</code>):</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13537.md")
</div>
<h3 id="switch-from-deprecated-websocket-to-rpc">Switch from deprecated WebSocket to RPC</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="requires-staged-deployment-1">Requires staged deployment</h3>
@markup("md", "content/.markup/bodies/13532.md")
</aside>
<p>Set the <code>SANDBOX_TRANSPORT</code> variable to <code>&quot;rpc&quot;</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13538.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/configuration/wrangler/">Wrangler configuration</a> - Complete Worker configuration</li>
<li><a href="/sandbox/configuration/environment-variables/">Environment variables</a> - Passing configuration to sandboxes</li>
<li><a href="/workers/platform/limits/#subrequests">Workers subrequest limits</a> - Understanding subrequest limits</li>
<li><a href="/sandbox/concepts/architecture/">Architecture</a> - How Sandbox SDK components communicate</li>
</ul>
