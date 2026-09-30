<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h3>
@markup("md", "content/.markup/bodies/13587.md")
</aside>
<p>This page documents every route exposed by the <a href="/sandbox/bridge/">sandbox bridge</a> on the stable template.</p>
<h2 id="authentication">Authentication</h2>
<p>All routes under <code>/v1/sandbox/*</code> and <code>/v1/openapi.*</code> require a Bearer token:</p>
<pre><code class="language-txt">Authorization: Bearer &lt;SANDBOX_API_KEY&gt;&#10;</code></pre>
<p>When <code>SANDBOX_API_KEY</code> is not configured, authentication is skipped for local development convenience. Always set the secret before deploying to production.</p>
<h2 id="openapi-schema">OpenAPI schema</h2>
<p>The bridge serves its own API documentation:</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Route</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>GET</code></td>
<td><code>/v1/openapi.json</code></td>
<td>Machine-readable OpenAPI 3.1 schema.</td>
</tr>
<tr>
<td><code>GET</code></td>
<td><code>/v1/openapi</code></td>
<td>Interactive HTML documentation.</td>
</tr>
</tbody>
</table>
<p>Both routes accept authentication via Bearer header or <code>?token=</code> query parameter.</p>
<p>When running locally with <code>npm run dev</code>, open <code>http://localhost:8787/v1/openapi</code> in your browser to explore every endpoint interactively.</p>
<h2 id="sandbox-lifecycle">Sandbox lifecycle</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Route</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>POST</code></td>
<td><code>/v1/sandbox</code></td>
<td>Create a new sandbox. Returns <code>{&quot;id&quot;: &quot;&lt;sandbox-id&gt;&quot;}</code>.</td>
</tr>
<tr>
<td><code>DELETE</code></td>
<td><code>/v1/sandbox/:id</code></td>
<td>Destroy the sandbox container. Returns <code>204</code>.</td>
</tr>
<tr>
<td><code>GET</code></td>
<td><code>/v1/sandbox/:id/running</code></td>
<td>Check container liveness. Returns <code>{&quot;running&quot;: true|false}</code>.</td>
</tr>
</tbody>
</table>
<h2 id="command-execution">Command execution</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Route</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>POST</code></td>
<td><code>/v1/sandbox/:id/exec</code></td>
<td>Run a command. Response is an SSE stream (see below).</td>
</tr>
</tbody>
</table>
<p>The <code>/exec</code> endpoint accepts a JSON body:</p>
<pre><code class="language-json">{&#10;  &quot;argv&quot;: [&quot;sh&quot;, &quot;-lc&quot;, &quot;echo hello&quot;],&#10;  &quot;timeout_ms&quot;: 10000,&#10;  &quot;cwd&quot;: &quot;/workspace&quot;&#10;}&#10;</code></pre>
<h3 id="argv-escaping">Argv escaping</h3>
<p>Each element of the <code>argv</code> array is escaped using ANSI-C <code>$'...'</code> quoting before being joined into a shell command. Tokens that contain only safe characters (<code>A-Za-z0-9@%+=:,./-</code>) are passed through unchanged. All other tokens are wrapped in <code>$'...'</code> with backslashes, single quotes, newlines, carriage returns, and tabs escaped. This prevents shell injection while preserving arguments that contain spaces, quotes, or special characters.</p>
<h3 id="sse-response-format">SSE response format</h3>
<p>The response is a <code>text/event-stream</code> with the following event types:</p>
<table>
<thead>
<tr>
<th>Event</th>
<th>Data</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>stdout</code></td>
<td>Base64-encoded chunk</td>
<td>Standard output from the command.</td>
</tr>
<tr>
<td><code>stderr</code></td>
<td>Base64-encoded chunk</td>
<td>Standard error from the command.</td>
</tr>
<tr>
<td><code>exit</code></td>
<td><code>{&quot;exit_code&quot;: N}</code></td>
<td>Command completed. Terminal event.</td>
</tr>
<tr>
<td><code>error</code></td>
<td><code>{&quot;error&quot;: &quot;…&quot;, &quot;code&quot;: &quot;…&quot;}</code></td>
<td>Command failed. Terminal event.</td>
</tr>
</tbody>
</table>
<h2 id="file-operations">File operations</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Route</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>GET</code></td>
<td><code>/v1/sandbox/:id/file/*</code></td>
<td>Read a file. Returns raw bytes (<code>application/octet-stream</code>).</td>
</tr>
<tr>
<td><code>PUT</code></td>
<td><code>/v1/sandbox/:id/file/*</code></td>
<td>Write a file. Request body is raw bytes. Returns <code>{&quot;ok&quot;: true}</code>. Max 32 MiB.</td>
</tr>
</tbody>
</table>
<p>The file path is encoded in the URL after <code>/file/</code>. All paths must resolve within <code>/workspace</code>. Path traversal attempts (for example, <code>../../etc/passwd</code>) are rejected.</p>
<h2 id="workspace-persistence">Workspace persistence</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Route</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>POST</code></td>
<td><code>/v1/sandbox/:id/persist</code></td>
<td>Serialize <code>/workspace</code> to a tar archive. Returns raw tar bytes.</td>
</tr>
<tr>
<td><code>POST</code></td>
<td><code>/v1/sandbox/:id/hydrate</code></td>
<td>Populate <code>/workspace</code> from a tar archive sent as the request body.</td>
</tr>
</tbody>
</table>
<p>The <code>/persist</code> endpoint accepts an optional <code>excludes</code> query parameter — a comma-separated list of relative paths to exclude from the archive.</p>
<p>The <code>/hydrate</code> endpoint accepts a raw tar payload up to 32 MiB.</p>
<h2 id="bucket-mounts">Bucket mounts</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Route</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>POST</code></td>
<td><code>/v1/sandbox/:id/mount</code></td>
<td>Mount an S3-compatible bucket as a local directory.</td>
</tr>
<tr>
<td><code>POST</code></td>
<td><code>/v1/sandbox/:id/unmount</code></td>
<td>Unmount a previously mounted bucket.</td>
</tr>
</tbody>
</table>
<p>The <code>/mount</code> endpoint accepts a JSON body. Two flows are supported:</p>
<h3 id="r2-binding-mounts">R2 binding mounts</h3>
<p>Omit <code>endpoint</code> and pass the Worker R2 binding name in <code>bucket</code>:</p>
<pre><code class="language-json">{&#10;  &quot;bucket&quot;: &quot;MY_BUCKET&quot;,&#10;  &quot;mountPath&quot;: &quot;/mnt/data&quot;,&#10;  &quot;options&quot;: {&#10;    &quot;readOnly&quot;: false,&#10;    &quot;prefix&quot;: &quot;/subdir&quot;&#10;  }&#10;}&#10;</code></pre>
<p>When <code>options.endpoint</code> is omitted, <code>bucket</code> means the Worker R2 binding name.</p>
<p>For an explicit S3-compatible endpoint mount, include <code>endpoint</code> and optionally <code>credentials</code>:</p>
<pre><code class="language-json">{&#10;  &quot;bucket&quot;: &quot;my-r2-bucket&quot;,&#10;  &quot;mountPath&quot;: &quot;/mnt/data&quot;,&#10;  &quot;options&quot;: {&#10;    &quot;endpoint&quot;: &quot;https://ACCOUNT_ID.r2.cloudflarestorage.com&quot;,&#10;    &quot;readOnly&quot;: false,&#10;    &quot;prefix&quot;: &quot;/subdir&quot;,&#10;    &quot;credentials&quot;: {&#10;      &quot;accessKeyId&quot;: &quot;...&quot;,&#10;      &quot;secretAccessKey&quot;: &quot;...&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>When <code>endpoint</code> is provided, <code>bucket</code> means the remote bucket name. Credentials are optional in this mode only — the bridge auto-detects from Worker secrets (<code>R2_ACCESS_KEY_ID</code> / <code>R2_SECRET_ACCESS_KEY</code> or <code>AWS_ACCESS_KEY_ID</code> / <code>AWS_SECRET_ACCESS_KEY</code>) when omitted.</p>
<h2 id="sessions">Sessions</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Route</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>POST</code></td>
<td><code>/v1/sandbox/:id/session</code></td>
<td>Create a session. Returns <code>{&quot;id&quot;: &quot;&lt;session-id&gt;&quot;}</code>.</td>
</tr>
<tr>
<td><code>DELETE</code></td>
<td><code>/v1/sandbox/:id/session/:sid</code></td>
<td>Delete a session. Returns <code>204</code>.</td>
</tr>
</tbody>
</table>
<p>Sessions isolate working directory, environment variables, and command execution state within a sandbox. Pass the <code>Session-Id</code> header on <code>/exec</code>, <code>/file/*</code>, and <code>/pty</code> requests to scope them to a session.</p>
<p>When no <code>Session-Id</code> header is provided, requests use the sandbox's implicit execution mode. By default this is the default session, but SDKs configured with <code>enableDefaultSession: false</code> run those implicit operations sessionless instead.</p>
<h2 id="terminal-pty">Terminal (PTY)</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Route</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>GET</code></td>
<td><code>/v1/sandbox/:id/pty</code></td>
<td>Upgrade to a WebSocket PTY session.</td>
</tr>
</tbody>
</table>
<p>Query parameters:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cols</code></td>
<td>number</td>
<td><code>80</code></td>
<td>Terminal width in columns.</td>
</tr>
<tr>
<td><code>rows</code></td>
<td>number</td>
<td><code>24</code></td>
<td>Terminal height in rows.</td>
</tr>
<tr>
<td><code>shell</code></td>
<td>string</td>
<td>—</td>
<td>Shell binary (for example, <code>/bin/bash</code>).</td>
</tr>
<tr>
<td><code>session</code></td>
<td>string</td>
<td>—</td>
<td>Session ID for session-scoped PTY.</td>
</tr>
</tbody>
</table>
<p>The WebSocket carries binary frames for terminal I/O and JSON text frames for control messages:</p>
<table>
<thead>
<tr>
<th>Direction</th>
<th>Frame type</th>
<th>Content</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client to server</td>
<td>Binary</td>
<td>UTF-8 encoded keystrokes.</td>
</tr>
<tr>
<td>Server to client</td>
<td>Binary</td>
<td>Terminal output including ANSI escape sequences.</td>
</tr>
<tr>
<td>Client to server</td>
<td>Text (JSON)</td>
<td>Control messages (for example, <code>{&quot;type&quot;: &quot;resize&quot;, &quot;cols&quot;: 120, &quot;rows&quot;: 30}</code>).</td>
</tr>
<tr>
<td>Server to client</td>
<td>Text (JSON)</td>
<td>Status messages (<code>ready</code>, <code>exit</code>, <code>error</code>).</td>
</tr>
</tbody>
</table>
<h2 id="warm-pool">Warm pool</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Route</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>GET</code></td>
<td><code>/v1/pool/stats</code></td>
<td>Current pool statistics.</td>
</tr>
<tr>
<td><code>POST</code></td>
<td><code>/v1/pool/prime</code></td>
<td>Start the warm pool alarm loop.</td>
</tr>
<tr>
<td><code>POST</code></td>
<td><code>/v1/pool/shutdown-prewarmed</code></td>
<td>Stop all idle warm containers.</td>
</tr>
</tbody>
</table>
<p>The warm pool pre-starts sandbox containers so new sessions boot instantly. Configure it with environment variables in <code>wrangler.jsonc</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13588.md")
</div>
<p>A cron trigger (<code>* * * * *</code>) primes the pool automatically after deployment. Set <code>WARM_POOL_TARGET</code> to <code>&quot;0&quot;</code> (the default) to disable the pool and avoid unexpected costs.</p>
<h2 id="health-check">Health check</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Route</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>GET</code></td>
<td><code>/health</code></td>
<td>Unauthenticated liveness probe. Returns <code>{&quot;ok&quot;: true}</code>.</td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/bridge/">Bridge overview</a> — What the bridge is, deployment, and usage examples.</li>
<li><a href="/sandbox/api/">Sandbox API reference</a> — Complete Sandbox SDK method reference.</li>
<li><a href="https://github.com/cloudflare/sandbox-sdk/tree/main/bridge">Bridge source on GitHub</a> — Worker, Dockerfile, and OpenAPI schema.</li>
</ul>
