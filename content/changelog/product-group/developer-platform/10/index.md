<h1 id="changelog">Changelog</h1>

<h2 id="vpc-networks-and-cloudflare-mesh-support-now-in-public-beta"><a href="/changelog/post/2026-04-14-vpc-networks/">VPC Networks and Cloudflare Mesh support now in public beta</a></h2>
<p><em>2026-04-14</em></p>
<p><a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> bindings now give your Workers access to any service in your private network without pre-registering individual hosts or ports. This complements existing <a href="/workers-vpc/configuration/vpc-services/">VPC Service</a> bindings, which scope each binding to a specific host and port.</p>
<p>You can bind to a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> by <code>tunnel_id</code> to reach any service on the network where that tunnel is running, or bind to your <a href="/mesh/">Cloudflare Mesh</a> network using <code>cf1:network</code> to reach any Mesh node, client device, or subnet route in your account:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17822.md")</div>
<p>At runtime, <code>fetch()</code> routes through the network to reach the service at the IP and port you specify:</p>
<pre><code class="language-js">const response = await env.MESH.fetch(&quot;http://10.0.1.50:8080/api/data&quot;);&#10;</code></pre>
<p>For configuration options and examples, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a> and <a href="/workers-vpc/examples/connect-to-cloudflare-mesh/">Connect Workers to Cloudflare Mesh</a>.</p>


<h2 id="containers-and-sandboxes-are-now-generally-available"><a href="/changelog/post/2026-04-13-containers-sandbox-ga/">Containers and Sandboxes are now generally available</a></h2>
<p><em>2026-04-13</em></p>
<p>Cloudflare <a href="/containers/">Containers</a> and <a href="/sandbox/">Sandboxes</a> are now generally available.</p>
<p>Containers let you run more workloads on the Workers platform, including resource-intensive applications, different languages, and CLI tools that need full Linux environments.</p>
<p>Since the initial launch of Containers, there have been significant improvements to Containers' performance, stability, and feature set. Some highlights include:</p>
<ul>
<li><a href="/changelog/post/2026-02-25-higher-container-resource-limits/">Higher limits</a> allow you to run thousands of containers concurrently.</li>
<li><a href="/changelog/post/2025-11-21-new-cpu-pricing/">Active-CPU pricing</a> means that you only pay for used CPU cycles.</li>
<li><a href="/changelog/post/2026-03-26-outbound-workers/">Easy connections to Workers and other bindings</a> via hostnames help you extend your Containers with additional functionality.</li>
<li><a href="/changelog/post/2026-03-24-docker-hub-images/">Docker Hub support</a> makes it easy to use your existing images and registries.</li>
<li><a href="/changelog/post/2026-03-12-ssh-support/">SSH support</a> helps you access and debug issues in live containers.</li>
</ul>
<p>The <a href="/sandbox/">Sandbox SDK</a> provides isolated environments for running untrusted code securely, with a simple TypeScript API for executing commands, managing files, and exposing services. This makes it easier to secure and manage your agents at scale. Some additions since launch include:</p>
<ul>
<li><a href="/changelog/post/2025-08-05-sandbox-sdk-major-update/">Live preview URLs</a> so agents can run long-lived services and verify in-flight changes.</li>
<li><a href="/changelog/post/2025-08-05-sandbox-sdk-major-update/">Persistent code interpreters</a> for Python, JavaScript, and TypeScript, with rich structured outputs.</li>
<li><a href="/changelog/post/2026-02-09-pty-terminal-support/">Interactive PTY terminals</a> for real browser-based terminal access with multiple isolated shells per sandbox.</li>
<li><a href="/changelog/post/2026-02-23-sandbox-backup-restore-api/">Backup and restore APIs</a> to snapshot a workspace and quickly restore an agent's coding session without repeating expensive setup steps.</li>
<li><a href="/changelog/post/2026-03-03-sandbox-watch-file-events/">Real-time filesystem watching</a> so apps and agents can react immediately to file changes inside a sandbox.</li>
</ul>
<p>For more information, refer to <a href="/containers/">Containers</a> and <a href="/sandbox/">Sandbox SDK</a> documentation.</p>


<h2 id="secure-credential-injection-and-dynamic-egress-policies-for-sandboxes"><a href="/changelog/post/2026-04-13-sandbox-outbound-workers-tls-auth/">Secure credential injection and dynamic egress policies for Sandboxes</a></h2>
<p><em>2026-04-13</em></p>
<p>Outbound Workers for <a href="/sandbox/">Sandboxes</a> and <a href="/containers/">Containers</a> now support zero-trust credential injection, TLS interception, allow/deny lists, and dynamic per-instance egress policies. These features give platforms running agentic workloads full control over what leaves the sandbox, without exposing secrets to untrusted workloads, like user-generated code or coding agents.</p>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-credential-injection">Credential injection</h4>
<p>Because outbound handlers run in the Workers runtime, outside the sandbox, they can hold secrets the sandbox never sees. A sandboxed workload can make a plain request, and credentials are transparently attached before a request is forwarded upstream.</p>
<p>For instance, you could run an agent in a sandbox and ensure that any requests it makes to Github are authenticated.
But it will never be able to access the credentials:</p>
<pre><code class="language-ts">export class MySandbox extends Sandbox {}&#10;&#10;MySandbox.outboundByHost = {&#10;	&quot;github.com&quot;: (request: Request, env: Env, ctx: OutboundHandlerContext) =&gt; {&#10;		const requestWithAuth = new Request(request);&#10;		requestWithAuth.headers.set(&quot;x-auth-token&quot;, env.SECRET);&#10;		return fetch(requestWithAuth);&#10;	},&#10;};&#10;</code></pre>
<p>You can easily inject unique credentials for different instances
by using <code>ctx.containerId</code>:</p>
<pre><code class="language-ts">MySandbox.outboundByHost = {&#10;	&quot;my-internal-vcs.dev&quot;: async (&#10;		request: Request,&#10;		env: Env,&#10;		ctx: OutboundHandlerContext,&#10;	) =&gt; {&#10;		const authKey = await env.KEYS.get(ctx.containerId);&#10;&#10;		const requestWithAuth = new Request(request);&#10;		requestWithAuth.headers.set(&quot;x-auth-token&quot;, authKey);&#10;		return fetch(requestWithAuth);&#10;	},&#10;};&#10;</code></pre>
<p>No token is ever passed into the sandbox. You can rotate secrets in the Worker environment
and every request will pick them up immediately.</p>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-tls-interception">TLS interception</h4>
<p>Outbound Workers now intercept HTTPS traffic. A unique ephemeral certificate authority (CA) and private key are created for each sandbox instance. The CA is placed into the sandbox and trusted by default. The ephemeral private key never leaves the container runtime sidecar process and is never shared across instances.</p>
<p>With TLS interception active, outbound Workers can act as a transparent proxy for both HTTP and HTTPS traffic.</p>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-allow-and-deny-hosts">Allow and deny hosts</h4>
<p>Easily filter outbound traffic with <code>allowedHosts</code> and <code>deniedHosts</code>. When <code>allowedHosts</code> is set, it becomes a deny-by-default allowlist. Both properties support glob patterns.</p>
<pre><code class="language-ts">export class MySandbox extends Sandbox {&#10;	allowedHosts = [&quot;github.com&quot;, &quot;npmjs.org&quot;];&#10;}&#10;</code></pre>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-dynamic-outbound-handlers">Dynamic outbound handlers</h4>
<p>Define named outbound handlers then apply or remove them at runtime using <code>setOutboundHandler()</code> or <code>setOutboundByHost()</code>. This lets you change egress policy for a running sandbox without restarting it.</p>
<pre><code class="language-ts">export class MySandbox extends Sandbox {}&#10;&#10;MySandbox.outboundHandlers = {&#10;	allowHosts: async (req: Request, env: Env, ctx: OutboundHandlerContext ) =&gt; {&#10;		const url = new URL(req.url);&#10;		if (ctx.params.allowedHostnames.includes(url.hostname)) {&#10;			return fetch(req);&#10;		}&#10;		return new Response(null, { status: 403 });&#10;	},&#10;&#10;	noHttp: async () =&gt; {&#10;		return new Response(null, { status: 403 });&#10;	},&#10;};&#10;</code></pre>
<p>Apply handlers programmatically from your Worker:</p>
<pre><code class="language-ts">const sandbox = getSandbox(env.Sandbox, userId);&#10;&#10;// Open network for setup&#10;await sandbox.setOutboundHandler(&quot;allowHosts&quot;, {&#10;	allowedHostnames: [&quot;github.com&quot;, &quot;npmjs.org&quot;],&#10;});&#10;await sandbox.exec(&quot;npm install&quot;);&#10;&#10;// Lock down after setup&#10;await sandbox.setOutboundHandler(&quot;noHttp&quot;);&#10;</code></pre>
<p>Handlers accept <code>params</code>, so you can customize behavior per instance without defining separate handler functions.</p>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-get-started">Get started</h4>
<p>Upgrade to <code>@cloudflare/containers@0.3.0</code> or <code>@cloudflare/sandbox@0.8.9</code> to use these features.</p>
<p>For more details, refer to <a href="/sandbox/guides/outbound-traffic/">Sandbox outbound traffic</a> and <a href="/containers/guides/outbound-traffic/">Container outbound traffic</a>.</p>


<h2 id="local-explorer-for-local-resource-data"><a href="/changelog/post/2026-04-13-local-explorer/">Local Explorer for local resource data</a></h2>
<p><em>2026-04-13</em></p>
<p>Local Explorer is a browser-based interface and REST API for viewing and editing local resource data during development. It removes the need to write throwaway scripts or dig through <code>.wrangler/state</code> to understand what data your Worker has stored locally.</p>
<p>Local Explorer is available in Wrangler 4.82.1+ and the Cloudflare Vite plugin 1.32.0+. Start a local development session and press <code>e</code> in your terminal, or navigate to <code>/cdn-cgi/local/explorer</code> on your local dev server.</p>
<h4 id="2026-04-13-local-explorer-supported-resources">Supported resources</h4>
<p>Local Explorer supports five resource types and works across multiple workers running locally:</p>
<ul>
<li><strong><a href="/kv/">KV</a></strong> — Browse keys, view values and metadata, create, update, and delete key-value pairs.</li>
<li><strong><a href="/r2/">R2</a></strong> — List objects, view metadata, upload files, and delete objects. Supports directory views and multi-select.</li>
<li><strong><a href="/d1/">D1</a></strong> — Browse tables and rows, run arbitrary SQL queries, and edit schemas in a full data studio.</li>
<li><strong><a href="/durable-objects/">Durable Objects</a></strong> (SQLite storage) — Browse individual object SQLite tables, run SQL queries, and edit schemas.</li>
<li><strong><a href="/workflows/">Workflows</a></strong> — List instances, view status and step history, trigger new runs, and pause, resume, restart, or terminate instances.</li>
</ul>
<h4 id="2026-04-13-local-explorer-openapi-powered-rest-api">OpenAPI-powered REST API</h4>
<p>Local Explorer exposes a REST API at <code>/cdn-cgi/local/explorer/api</code> that provides programmatic access to the same operations available in the browser. The root endpoint returns an <a href="https://www.openapis.org/">OpenAPI specification</a> describing all available endpoints, parameters, and response formats.</p>
<pre><code class="language-sh">curl http://localhost:8787/cdn-cgi/local/explorer/api&#10;</code></pre>
<p>Point an AI coding agent at <code>/cdn-cgi/local/explorer/api</code> and it can discover and interact with your local resources without manual setup. This enables iterative development loops where an agent can populate test data in KV or D1, inspect Durable Object state, trigger Workflow runs, or upload files to R2.</p>
<p>For more details, refer to the <a href="/workers/local-development/local-explorer/">Local Explorer documentation</a>.</p>


<h2 id="browser-rendering-adds-chrome-devtools-protocol-cdp-and-mcp-client-support"><a href="/changelog/post/2026-04-10-browser-rendering-cdp-endpoint/">Browser Rendering adds Chrome DevTools Protocol (CDP) and MCP client support</a></h2>
<p><em>2026-04-10</em></p>
<p><a href="/browser-run/">Browser Rendering</a> now exposes the <a href="/browser-run/cdp/">Chrome DevTools Protocol (CDP)</a>, the low-level protocol that powers browser automation. The growing ecosystem of CDP-based agent tools, along with existing CDP automation scripts, can now use Browser Rendering directly.</p>
<p>Any CDP-compatible client, including <a href="/browser-run/cdp/puppeteer/">Puppeteer</a> and <a href="/browser-run/cdp/playwright/">Playwright</a>, can connect from any environment, whether that is <a href="/workers/">Cloudflare Workers</a>, your local machine, or a cloud environment. All you need is your Cloudflare API key.</p>
<p>For any existing CDP script, switching to Browser Rendering is a one-line change:</p>
<pre><code class="language-js">const puppeteer = require(&quot;puppeteer-core&quot;);&#10;&#10;const browser = await puppeteer.connect({&#10;	browserWSEndpoint: `wss://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/browser-rendering/devtools/browser?keep_alive=600000`,&#10;	headers: { Authorization: `Bearer ${API_TOKEN}` },&#10;});&#10;&#10;const page = await browser.newPage();&#10;await page.goto(&quot;https://example.com&quot;);&#10;console.log(await page.title());&#10;await browser.close();&#10;</code></pre>
<p>Additionally, MCP clients like Claude Desktop, Claude Code, Cursor, and OpenCode can now use Browser Rendering as their remote browser via the <a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">chrome-devtools-mcp</a> package.</p>
<p>Here is an example of how to configure Browser Rendering for Claude Desktop:</p>
<pre><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;browser-rendering&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&#10;				&quot;-y&quot;,&#10;				&quot;chrome-devtools-mcp@latest&quot;,&#10;				&quot;--wsEndpoint=wss://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-rendering/devtools/browser?keep_alive=600000&quot;,&#10;				&quot;--wsHeaders={\&quot;Authorization\&quot;:\&quot;Bearer &lt;API_TOKEN&gt;\&quot;}&quot;&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To get started, refer to the <a href="/browser-run/cdp/">CDP documentation</a>.</p>


<h2 id="relaxed-simultaneous-connection-limiting-for-workers"><a href="/changelog/post/2026-04-09-relaxed-connection-limiting/">Relaxed simultaneous connection limiting for Workers</a></h2>
<p><em>2026-04-09</em></p>
<p>The <a href="/workers/platform/limits/#simultaneous-open-connections">simultaneous open connections limit</a> has been relaxed. Previously, each Worker invocation was limited to six open connections at a time for the entire lifetime of each connection, including while reading the response body. Now, a connection is freed as soon as response headers arrive, so the six-connection limit only constrains how many connections can be in the initial &quot;waiting for headers&quot; phase simultaneously.</p>
<h4 id="2026-04-09-relaxed-connection-limiting-before-new-connections-are-blocked-until-an-earlier-connection-fully-completes">Before: New connections are blocked until an earlier connection fully completes</h4>
<p><img src="/assets/upstream/images/workers/platform/limits/connection-limit-before.svg" alt="A 7th fetch is queued until an earlier connection fully completes, including reading its entire response body" /></p>
<h4 id="2026-04-09-relaxed-connection-limiting-after-new-connections-can-start-as-soon-as-response-headers-arrive">After: New connections can start as soon as response headers arrive</h4>
<p><img src="/assets/upstream/images/workers/platform/limits/connection-limit-after.svg" alt="A 7th fetch starts as soon as any earlier connection receives its response headers" /></p>
<p>This means Workers can now have many more connections open at the same time without queueing, as long as no more than six are waiting for their initial response. This eliminates the <code>Response closed due to connection limit</code> exception that could previously occur when the runtime canceled stalled connections to prevent deadlocks.</p>
<p>Previously, the runtime used a deadlock avoidance algorithm that watched each open connection for I/O activity. If all six connections appeared idle — even momentarily — the runtime would cancel the least-recently-used connection to make room for new requests. In practice, this heuristic was fragile. For example, when a response used <code>Content-Encoding: gzip</code>, the runtime's internal decompression created brief gaps between read and write operations. During these gaps, the connection appeared stalled despite being actively read by the Worker. If multiple connections hit these gaps at the same time, the runtime could spuriously cancel a connection that was working correctly. By only counting connections during the waiting-for-headers phase — where the runtime is fully in control and there is no ambiguity about whether the connection is active — this class of bug is eliminated entirely.</p>
<h4 id="2026-04-09-relaxed-connection-limiting-before-connections-could-be-canceled-during-brief-internal-pauses">Before: Connections could be canceled during brief internal pauses</h4>
<p><img src="/assets/upstream/images/workers/platform/limits/connection-cancel-before.svg" alt="A connection with gaps from gzip decompression appears idle and is canceled by the runtime" /></p>
<h4 id="2026-04-09-relaxed-connection-limiting-after-connections-complete-normally-regardless-of-internal-pauses">After: Connections complete normally regardless of internal pauses</h4>
<p><img src="/assets/upstream/images/workers/platform/limits/connection-cancel-after.svg" alt="The same connection completes normally because the body phase is no longer counted against the limit" /></p>


<h2 id="website-source-css-content-selectors-for-precise-content-extraction-in-ai-search"><a href="/changelog/post/2026-04-09-ai-search-content-selectors/">Website Source CSS content selectors for precise content extraction in AI Search</a></h2>
<p><em>2026-04-08</em></p>
<p><a href="/ai-search/">AI Search</a> now supports <a href="/ai-search/configuration/data-source/website/content-selectors/">CSS content selectors</a> for website data sources. You can now define which parts of a crawled page are extracted and indexed by specifying CSS selectors paired with URL glob patterns.</p>
<p>Content selectors solve the problem of indexing only relevant content while ignoring navigation, sidebars, footers, and other boilerplate. When a page URL matches a glob pattern, only elements matching the corresponding CSS selector are extracted and converted to Markdown for indexing.</p>
<p>Configure content selectors via the dashboard or API:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-search/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-ai-search&quot;,&#10;    &quot;source&quot;: &quot;https://example.com&quot;,&#10;    &quot;type&quot;: &quot;web-crawler&quot;,&#10;    &quot;source_params&quot;: {&#10;      &quot;web_crawler&quot;: {&#10;        &quot;parse_options&quot;: {&#10;          &quot;content_selector&quot;: [&#10;            {&#10;              &quot;path&quot;: &quot;**/blog/**&quot;,&#10;              &quot;selector&quot;: &quot;article .post-body&quot;&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Selectors are evaluated in order, and the first matching pattern wins. You can define up to 10 content selector entries per instance.</p>
<p>For configuration details and examples, refer to the <a href="/ai-search/configuration/data-source/website/content-selectors/">content selectors documentation</a>.</p>


<h2 id="new-workers-ai-models-for-text-generation-and-embedding-in-ai-search"><a href="/changelog/post/2026-04-09-new-workers-ai-models/">New Workers AI models for text generation and embedding in AI Search</a></h2>
<p><em>2026-04-08</em></p>
<p><a href="/ai-search/">AI Search</a> now supports four additional <a href="/workers-ai/">Workers AI</a> models across text generation and embedding.</p>
<h4 id="2026-04-09-new-workers-ai-models-text-generation">Text generation</h4>
<table>
<thead>
<tr>
<th>Model</th>
<th>Context window (tokens)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/zai-org/glm-4.7-flash</code></td>
<td>131,072</td>
</tr>
<tr>
<td><code>@cf/qwen/qwen3-30b-a3b-fp8</code></td>
<td>32,000</td>
</tr>
</tbody>
</table>
<p>GLM-4.7-Flash is a lightweight model from Zhipu AI with a 131,072 token context window, suitable for long-document summarization and retrieval tasks. Qwen3-30B-A3B is a mixture-of-experts model from Alibaba that activates only 3 billion parameters per forward pass, keeping inference fast while maintaining strong response quality.</p>
<h4 id="2026-04-09-new-workers-ai-models-embedding">Embedding</h4>
<table>
<thead>
<tr>
<th>Model</th>
<th>Vector dims</th>
<th>Input tokens</th>
<th>Metric</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/qwen/qwen3-embedding-0.6b</code></td>
<td>1,024</td>
<td>4,096</td>
<td>cosine</td>
</tr>
<tr>
<td><code>@cf/google/embeddinggemma-300m</code></td>
<td>768</td>
<td>512</td>
<td>cosine</td>
</tr>
</tbody>
</table>
<p>Qwen3-Embedding-0.6B supports up to 4,096 input tokens, making it a good fit for indexing longer text chunks. EmbeddingGemma-300M from Google produces 768-dimension vectors and is optimized for low-latency embedding workloads.</p>
<p>All four models are available without additional provider keys since they run on Workers AI. Select them when creating or updating an AI Search instance in the dashboard or through the API.</p>
<p>For the full list of supported models, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>


<h2 id="websockets-now-automatically-reply-to-close-frames"><a href="/changelog/post/2026-04-07-websocket-auto-reply-to-close/">WebSockets now automatically reply to Close frames</a></h2>
<p><em>2026-04-07</em></p>
<p>The Workers runtime now automatically sends a reciprocal Close frame when it receives a Close frame from the peer. The <code>readyState</code> transitions to <code>CLOSED</code> before the <code>close</code> event fires. This matches the <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close_event">WebSocket specification</a> and standard browser behavior.</p>
<p>This change is enabled by default for Workers using compatibility dates on or after <code>2026-04-07</code> (via the <a href="/workers/configuration/compatibility-flags/#websocket-auto-reply-to-close"><code>web_socket_auto_reply_to_close</code></a> compatibility flag). Existing code that manually calls <code>close()</code> inside the <code>close</code> event handler will continue to work — the call is silently ignored when the WebSocket is already closed.</p>
<pre><code class="language-js">const [client, server] = Object.values(new WebSocketPair());&#10;server.accept();&#10;&#10;server.addEventListener(&quot;close&quot;, (event) =&gt; {&#10;	// readyState is already CLOSED — no need to call server.close().&#10;	console.log(server.readyState); // WebSocket.CLOSED&#10;	console.log(event.code); // 1000&#10;	console.log(event.wasClean); // true&#10;});&#10;</code></pre>
<h4 id="2026-04-07-websocket-auto-reply-to-close-half-open-mode-for-websocket-proxying">Half-open mode for WebSocket proxying</h4>
<p>The automatic close behavior can interfere with WebSocket proxying, where a Worker sits between a client and a backend and needs to coordinate the close on both sides independently. To support this use case, pass <code>{ allowHalfOpen: true }</code> to <code>accept()</code>:</p>
<pre><code class="language-js">const [client, server] = Object.values(new WebSocketPair());&#10;&#10;server.accept({ allowHalfOpen: true });&#10;&#10;server.addEventListener(&quot;close&quot;, (event) =&gt; {&#10;	// readyState is still CLOSING here, giving you time&#10;	// to coordinate the close on the other side.&#10;	console.log(server.readyState); // WebSocket.CLOSING&#10;&#10;	// Manually close when ready.&#10;	server.close(event.code, &quot;done&quot;);&#10;});&#10;</code></pre>
<p>For more information, refer to <a href="/workers/runtime-apis/websockets/#close-behavior">WebSockets Close behavior</a>.</p>


<h2 id="control-where-your-containers-run-with-regional-and-jurisdictional-placement"><a href="/changelog/post/2026-04-05-regional-placement/">Control where your Containers run with regional and jurisdictional placement</a></h2>
<p><em>2026-04-05</em></p>
<p>You can now specify placement constraints to control where your <a href="/containers/">Containers</a> run.</p>
<table>
<thead>
<tr>
<th>Constraint</th>
<th>Values</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>regions</code></td>
<td><code>ENAM</code>, <code>WNAM</code>, <code>EEUR</code>, <code>WEUR</code></td>
<td>Geographic placement</td>
</tr>
<tr>
<td><code>jurisdiction</code></td>
<td><code>eu</code>, <code>fedramp</code></td>
<td>Compliance boundaries</td>
</tr>
</tbody>
</table>
<p>Use <code>regions</code> to limit placement to specific geographic areas. Use <code>jurisdiction</code> to restrict containers to compliance boundaries — <code>eu</code> maps to European regions (EEUR, WEUR) and <code>fedramp</code> maps to North American regions (ENAM, WNAM).</p>
<p>Refer to <a href="/containers/concepts/placement/">Containers placement</a> for more details.</p>


<h2 id="google-gemma-4-26b-a4b-now-available-on-workers-ai"><a href="/changelog/post/2026-04-04-gemma-4-26b-a4b-workers-ai/">Google Gemma 4 26B A4B now available on Workers AI</a></h2>
<p><em>2026-04-04</em></p>
<p>We are partnering with Google to bring <a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a> to Workers AI. Gemma 4 26B A4B is a Mixture-of-Experts (MoE) model built from Gemini 3 research, with 26B total parameters and only 4B active per forward pass. By activating a small subset of parameters during inference, the model runs almost as fast as a 4B-parameter model while delivering the quality of a much larger one.</p>
<p>Gemma 4 is Google's most capable family of open models, designed to maximize intelligence-per-parameter.</p>
<h4 id="2026-04-04-gemma-4-26b-a4b-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Mixture-of-Experts architecture</strong> with 8 active experts out of 128 total (plus 1 shared expert), delivering frontier-level performance at a fraction of the compute cost of dense models</li>
<li><strong>256,000 token context window</strong> for retaining full conversation history, tool definitions, and long documents across extended sessions</li>
<li><strong>Built-in thinking mode</strong> that lets the model reason step-by-step before answering, improving accuracy on complex tasks</li>
<li><strong>Vision understanding</strong> for object detection, document and PDF parsing, screen and UI understanding, chart comprehension, OCR (including multilingual), and handwriting recognition, with support for variable aspect ratios and resolutions</li>
<li><strong>Function calling</strong> with native support for structured tool use, enabling agentic workflows and multi-step planning</li>
<li><strong>Multilingual</strong> with out-of-the-box support for 35+ languages, pre-trained on 140+ languages</li>
<li><strong>Coding</strong> for code generation, completion, and correction</li>
</ul>
<p>Use Gemma 4 26B A4B through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, or the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/gemma-4-26b-a4b-it/">Gemma 4 26B A4B model page</a>.</p>


<h2 id="automatically-retry-on-upstream-provider-failures-on-ai-gateway"><a href="/changelog/post/2026-04-02-auto-retry-upstream-failures/">Automatically retry on upstream provider failures on AI Gateway</a></h2>
<p><em>2026-04-02</em></p>
<p>AI Gateway now supports automatic retries at the gateway level. When an upstream provider returns an error, your gateway retries the request based on the retry policy you configure, without requiring any client-side changes.</p>
<p>You can configure the retry count (up to 5 attempts), the delay between retries (from 100ms to 5 seconds), and the backoff strategy (Constant, Linear, or Exponential). These defaults apply to all requests through the gateway, and per-request headers can override them.</p>
<p><img src="/assets/upstream/images/ai-gateway/auto-retry-changelog.png" alt="Retry Requests settings in the AI Gateway dashboard" /></p>
<p>This is particularly useful when you do not control the client making the request and cannot implement retry logic on the caller side. For more complex failover scenarios — such as failing across different providers — use <a href="/ai-gateway/features/dynamic-routing/">Dynamic Routing</a>.</p>
<p>For more information, refer to <a href="/ai-gateway/configuration/manage-gateway/#retry-requests">Manage gateways</a>.</p>


<h2 id="all-wrangler-commands-for-workflows-now-support-local-development"><a href="/changelog/post/2026-04-01-wrangler-workflows-local/">All Wrangler commands for Workflows now support local development</a></h2>
<p><em>2026-04-01 12:00:00 UTC</em></p>
<p>All <code>wrangler workflows</code> commands now accept a <code>--local</code> flag to target a Workflow running in a local <code>wrangler dev</code> session instead of the production API.</p>
<p>You can now manage the full Workflow lifecycle locally, including triggering Workflows, listing instances, pausing, resuming, restarting, terminating, and sending events:</p>
<pre><code class="language-sh">npx wrangler workflows list --local&#10;npx wrangler workflows trigger my-workflow --local&#10;npx wrangler workflows instances list my-workflow --local&#10;npx wrangler workflows instances pause my-workflow &lt;INSTANCE_ID&gt; --local&#10;npx wrangler workflows instances send-event my-workflow &lt;INSTANCE_ID&gt; --type my-event --local&#10;</code></pre>
<p>All commands also accept <code>--port</code> to target a specific <code>wrangler dev</code> session (defaults to <code>8787</code>).</p>
<p>For more information, refer to <a href="/workflows/build/local-development/">Workflows local development</a>.</p>


<h2 id="create-manage-search-ai-search-instances-with-wrangler-cli"><a href="/changelog/post/2026-04-01-ai-search-wrangler-commands/">Create, manage, search AI Search instances with Wrangler CLI</a></h2>
<p><em>2026-04-01</em></p>
<p><a href="/ai-search/">AI Search</a> supports a <code>wrangler ai-search</code> command namespace. Use it to manage instances from the command line.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler ai-search create</code></td>
<td>Create a new instance with an interactive wizard</td>
</tr>
<tr>
<td><code>wrangler ai-search list</code></td>
<td>List all instances in your account</td>
</tr>
<tr>
<td><code>wrangler ai-search get</code></td>
<td>Get details of a specific instance</td>
</tr>
<tr>
<td><code>wrangler ai-search update</code></td>
<td>Update the configuration of an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search delete</code></td>
<td>Delete an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search search</code></td>
<td>Run a search query against an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search stats</code></td>
<td>Get usage statistics for an instance</td>
</tr>
</tbody>
</table>
<p>The <code>create</code> command guides you through setup, choosing a name, source type (<code>r2</code> or <code>web</code>), and data source. You can also pass all options as flags for non-interactive use:</p>
<pre><code class="language-sh">wrangler ai-search create my-instance --type r2 --source my-bucket&#10;</code></pre>
<p>Use <code>wrangler ai-search search</code> to query an instance directly from the CLI:</p>
<pre><code class="language-sh">wrangler ai-search search my-instance --query &quot;how do I configure caching?&quot;&#10;</code></pre>
<p>All commands support <code>--json</code> for structured output that scripts and AI agents can parse directly.</p>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">Wrangler commands documentation</a>.</p>


<h2 id="deploy-hooks-are-now-available-for-workers-builds"><a href="/changelog/post/2026-04-01-deploy-hooks/">Deploy Hooks are now available for Workers Builds</a></h2>
<p><em>2026-04-01</em></p>
<p><a href="/workers/ci-cd/builds/">Workers Builds</a> now supports Deploy Hooks — trigger builds from your headless CMS, a Cron Trigger, a Slack bot, or any system that can send an HTTP request.</p>
<p>Each Deploy Hook is a unique URL tied to a specific branch. Send it a <code>POST</code> and your Worker builds and deploys.</p>
<pre><code class="language-sh">curl -X POST &quot;https://api.cloudflare.com/client/v4/workers/builds/deploy_hooks/&lt;DEPLOY_HOOK_ID&gt;&quot;&#10;</code></pre>
<p>To create one, go to <strong>Workers &amp; Pages</strong> &gt; your Worker &gt; <strong>Settings</strong> &gt; <strong>Builds</strong> &gt; <strong>Deploy Hooks</strong>.</p>
<p>Since a Deploy Hook is a URL, you can also call it from another Worker. For example, a Worker with a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> can rebuild your project on a schedule:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17803.md")</div>
<p>You can also use Deploy Hooks to <a href="/workers/ci-cd/builds/deploy-hooks/#cms-integration">rebuild when your CMS publishes new content</a> or <a href="/workers/ci-cd/builds/deploy-hooks/#deploy-from-a-slack-slash-command">deploy from a Slack slash command</a>.</p>
<h4 id="2026-04-01-deploy-hooks-built-in-optimizations">Built-in optimizations</h4>
<ul>
<li><strong>Automatic deduplication</strong>: If a Deploy Hook fires multiple times before the first build starts running, redundant builds are automatically skipped. This keeps your build queue clean when webhooks retry or CMS events arrive in bursts.</li>
<li><strong>Last triggered</strong>: The dashboard shows when each hook was last triggered.</li>
<li><strong>Build source</strong>: Your Worker's build history shows which Deploy Hook started each build by name.</li>
</ul>
<p>Deploy Hooks are rate limited to 10 builds per minute per Worker and 100 builds per minute per account. For all limits, see <a href="/workers/ci-cd/builds/limits-and-pricing/">Limits &amp; pricing</a>.</p>
<p>To get started, read the <a href="/workers/ci-cd/builds/deploy-hooks/">Deploy Hooks documentation</a>.</p>


<h2 id="new-l4-transport-telemetry-fields-in-workers"><a href="/changelog/post/2026-04-01-l4-transport-telemetry-fields/">New L4 transport telemetry fields in Workers</a></h2>
<p><em>2026-04-01</em></p>
<p>Three new properties are now available on <code>request.cf</code> in Workers that expose Layer 4 transport telemetry from the client connection. These properties let your Worker make decisions based on real-time connection quality signals — such as round-trip time and data delivery rate — without requiring any client-side changes.</p>
<p>Previously, this telemetry was only available via the <code>Server-Timing: cfL4</code> response header. These new properties surface the same data directly in the Workers runtime, so you can use it for routing, logging, or response customization.</p>
<h4 id="2026-04-01-l4-transport-telemetry-fields-new-properties">New properties</h4>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>clientTcpRtt</code></td>
<td>number | undefined</td>
<td>The smoothed TCP round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for TCP connections (HTTP/1, HTTP/2). For example, <code>22</code>.</td>
</tr>
<tr>
<td><code>clientQuicRtt</code></td>
<td>number | undefined</td>
<td>The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for QUIC connections (HTTP/3). For example, <code>42</code>.</td>
</tr>
<tr>
<td><code>edgeL4</code></td>
<td>Object | undefined</td>
<td>Layer 4 transport statistics. Contains <code>deliveryRate</code> (number) — the most recent data delivery rate estimate for the connection, in bytes per second. For example, <code>123456</code>.</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-01-l4-transport-telemetry-fields-example-log-connection-quality-metrics">Example: Log connection quality metrics</h4>
<pre><code class="language-js">export default {&#10;  async fetch(request) {&#10;    const cf = request.cf;&#10;&#10;    const rtt = cf.clientTcpRtt ?? cf.clientQuicRtt ?? 0;&#10;    const deliveryRate = cf.edgeL4?.deliveryRate ?? 0;&#10;    const transport = cf.clientTcpRtt ? &quot;TCP&quot; : &quot;QUIC&quot;;&#10;&#10;    console.log(`Transport: ${transport}, RTT: ${rtt}ms, Delivery rate: ${deliveryRate} B/s`);&#10;&#10;    const headers = new Headers(request.headers);&#10;    headers.set(&quot;X-Client-RTT&quot;, String(rtt));&#10;    headers.set(&quot;X-Delivery-Rate&quot;, String(deliveryRate));&#10;&#10;    return fetch(new Request(request, { headers }));&#10;  },&#10;};&#10;</code></pre>
<p>For more information, refer to <a href="/workers/runtime-apis/request/">Workers Runtime APIs: Request</a>.</p>


<h2 id="new-rfc-9440-mtls-certificate-fields-in-workers"><a href="/changelog/post/2026-03-27-rfc9440-mtls-fields/">New RFC 9440 mTLS certificate fields in Workers</a></h2>
<p><em>2026-03-27</em></p>
<p>Four new fields are now available on <code>request.cf.tlsClientAuth</code> in Workers for requests that include a mutual TLS (mTLS) client certificate. These fields encode the client certificate and its intermediate chain in <a href="https://www.rfc-editor.org/rfc/rfc9440">RFC 9440</a> format — the same standard format used by the <code>Client-Cert</code> and <code>Client-Cert-Chain</code> HTTP headers — so your Worker can forward them directly to your origin without any custom parsing or encoding logic.</p>
<h4 id="2026-03-27-rfc9440-mtls-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>certRFC9440</code></td>
<td>String</td>
<td>The client leaf certificate in RFC 9440 format (<code>:base64-DER:</code>). Empty if no client certificate was presented.</td>
</tr>
<tr>
<td><code>certRFC9440TooLarge</code></td>
<td>Boolean</td>
<td><code>true</code> if the leaf certificate exceeded 10 KB and was omitted from <code>certRFC9440</code>.</td>
</tr>
<tr>
<td><code>certChainRFC9440</code></td>
<td>String</td>
<td>The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediates were sent or if the chain exceeded 16 KB.</td>
</tr>
<tr>
<td><code>certChainRFC9440TooLarge</code></td>
<td>Boolean</td>
<td><code>true</code> if the intermediate chain exceeded 16 KB and was omitted from <code>certChainRFC9440</code>.</td>
</tr>
</tbody>
</table>
<h4 id="2026-03-27-rfc9440-mtls-fields-example-forwarding-client-certificate-headers-to-your-origin">Example: forwarding client certificate headers to your origin</h4>
<pre><code class="language-js">export default {&#10;  async fetch(request) {&#10;    const tls = request.cf.tlsClientAuth;&#10;&#10;    // Only forward if cert was verified and chain is complete&#10;    if (!tls || !tls.certVerified || tls.certRevoked || tls.certChainRFC9440TooLarge) {&#10;      return new Response(&quot;Unauthorized&quot;, { status: 401 });&#10;    }&#10;&#10;    const headers = new Headers(request.headers);&#10;    headers.set(&quot;Client-Cert&quot;, tls.certRFC9440);&#10;    headers.set(&quot;Client-Cert-Chain&quot;, tls.certChainRFC9440);&#10;&#10;    return fetch(new Request(request, { headers }));&#10;  },&#10;};&#10;</code></pre>
<p>For more information, refer to <a href="/ssl/client-certificates/client-certificate-variables/#workers-variables">Client certificate variables</a> and <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">Mutual TLS authentication</a>.</p>


<h2 id="easily-connect-containers-and-sandboxes-to-workers"><a href="/changelog/post/2026-03-26-outbound-workers/">Easily connect Containers and Sandboxes to Workers</a></h2>
<p><em>2026-03-26</em></p>
<p><a href="/containers/">Containers</a> and <a href="/sandbox/">Sandboxes</a> now support connecting directly to Workers over HTTP. This allows you to call Workers
functions and <a href="/workers/runtime-apis/bindings/">bindings</a>, like <a href="/kv">KV</a> or <a href="/r2/">R2</a>, from within the container at specific hostnames.</p>
<h4 id="2026-03-26-outbound-workers-run-worker-code">Run Worker code</h4>
<p>Define an <code>outbound</code> handler to capture any HTTP request or use <code>outboundByHost</code> to capture requests to individual hostnames and IPs.</p>
<pre><code class="language-js">export class MyApp extends Sandbox {}&#10;&#10;MyApp.outbound = async (request, env, ctx) =&gt; {&#10;	// you can run arbitrary functions defined in your Worker on any HTTP request&#10;	return await someWorkersFunction(request.body);&#10;};&#10;&#10;MyApp.outboundByHost = {&#10;	&quot;my.worker&quot;: async (request, env, ctx) =&gt; {&#10;		return await anotherFunction(request.body);&#10;	},&#10;};&#10;</code></pre>
<p>In this example, requests from the container to <code>http://my.worker</code> will run the function defined within <code>outboundByHost</code>,
and any other HTTP requests will run the <code>outbound</code> handler. These handlers run entirely inside the Workers runtime,
outside of the container sandbox.</p>
<h4 id="2026-03-26-outbound-workers-access-workers-bindings">Access Workers bindings</h4>
<p>Each handler has access to <code>env</code>, so it can call any binding set in <a href="/workers/wrangler/configuration/#bindings">Wrangler config</a>.
Code inside the container makes a standard HTTP request to that hostname and the outbound Worker translates it into a binding call.</p>
<pre><code class="language-js">export class MyApp extends Sandbox {}&#10;&#10;MyApp.outboundByHost = {&#10;	&quot;my.kv&quot;: async (request, env, ctx) =&gt; {&#10;		const key = new URL(request.url).pathname.slice(1);&#10;		const value = await env.KV.get(key);&#10;		return new Response(value ?? &quot;&quot;, { status: value ? 200 : 404 });&#10;	},&#10;	&quot;my.r2&quot;: async (request, env, ctx) =&gt; {&#10;		const key = new URL(request.url).pathname.slice(1);&#10;		const object = await env.BUCKET.get(key);&#10;		return new Response(object?.body ?? &quot;&quot;, { status: object ? 200 : 404 });&#10;	},&#10;};&#10;</code></pre>
<p>Now, from inside the container sandbox, <code>curl http://my.kv/some-key</code> will access <a href="/kv">Workers KV</a> and <code>curl http://my.r2/some-object</code> will access <a href="/r2/">R2</a>.</p>
<h4 id="2026-03-26-outbound-workers-access-durable-object-state">Access Durable Object state</h4>
<p>Use <code>ctx.containerId</code> to reference the container's automatically provisioned <a href="/durable-objects">Durable Object</a>.</p>
<pre><code class="language-js">export class MyContainer extends Container {}&#10;&#10;MyContainer.outboundByHost = {&#10;	&quot;get-state.do&quot;: async (request, env, ctx) =&gt; {&#10;		const id = env.MY_CONTAINER.idFromString(ctx.containerId);&#10;		const stub = env.MY_CONTAINER.get(id);&#10;		return stub.getStateForKey(request.body);&#10;	},&#10;};&#10;</code></pre>
<p>This provides an easy way to associate state with any container instance, and includes a <a href="/durable-objects/get-started/#2-write-a-durable-object-class-using-sql-api">built-in SQLite database</a>.</p>
<h4 id="2026-03-26-outbound-workers-get-started-today">Get Started Today</h4>
<p>Upgrade to <code>@cloudflare/containers</code> version 0.2.0 or later, or <code>@cloudflare/sandbox</code> version 0.8.0 or later to use outbound Workers.</p>
<p>Refer to <a href="/containers/guides/outbound-traffic/">Containers outbound traffic</a> and <a href="/sandbox/guides/outbound-traffic/">Sandboxes outbound traffic</a> for more details and examples.</p>


<h2 id="access-durable-object-jurisdiction-via-ctx-id-jurisdiction"><a href="/changelog/post/2026-03-26-durable-object-id-jurisdiction/">Access Durable Object jurisdiction via `ctx.id.jurisdiction`</a></h2>
<p><em>2026-03-26</em></p>
<p><code>ctx.id.jurisdiction</code> inside a Durable Object now reports the <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a> the object was created in — for example <code>&quot;eu&quot;</code> when accessed through <code>env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;)</code> — so you can make region-aware decisions without passing the jurisdiction through method arguments or persisting it in storage. For the full list of ID-construction paths that preserve <code>jurisdiction</code>, refer to the <a href="/durable-objects/api/id/#jurisdiction">Durable Object ID documentation</a>.</p>
<pre><code class="language-js">export class RegionalRoom extends DurableObject {&#10;	async fetch(request) {&#10;		// &quot;eu&quot; when accessed through env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;)&#10;		const region = this.ctx.id.jurisdiction;&#10;		return new Response(`Hello from ${region ?? &quot;the default region&quot;}!`);&#10;	}&#10;}&#10;&#10;// Worker&#10;export default {&#10;	async fetch(request, env) {&#10;		const stub = env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;).getByName(&quot;general&quot;);&#10;		return stub.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p><code>ctx.id.jurisdiction</code> is <code>undefined</code> for Durable Objects that were not created in a jurisdiction-restricted namespace. Alarms scheduled before 2026-03-15 also do not have <code>jurisdiction</code> stored; to backfill the value, reschedule the alarm from a <code>fetch()</code> or RPC handler.</p>


<h2 id="declare-required-secrets-in-your-wrangler-configuration"><a href="/changelog/post/2026-03-24-secrets-config-property/">Declare required secrets in your Wrangler configuration</a></h2>
<p><em>2026-03-25</em></p>
<p>The new <code>secrets</code> configuration property lets you declare the secret names your Worker requires in your Wrangler configuration file. Required secrets are validated during local development and deploy, and used as the source of truth for type generation.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17802.md")</div>
<h4 id="2026-03-24-secrets-config-property-local-development">Local development</h4>
<p>When <code>secrets</code> is defined, <code>wrangler dev</code> and <code>vite dev</code> load only the keys listed in <code>secrets.required</code> from <code>.dev.vars</code> or <code>.env</code>/<code>process.env</code>. Additional keys in those files are excluded. If any required secrets are missing, a warning is logged listing the missing names.</p>
<h4 id="2026-03-24-secrets-config-property-type-generation">Type generation</h4>
<p><code>wrangler types</code> generates typed bindings from <code>secrets.required</code> instead of inferring names from <code>.dev.vars</code> or <code>.env</code>. This lets you run type generation in CI or other environments where those files are not present. Per-environment secrets are supported — the aggregated <code>Env</code> type marks secrets that only appear in some environments as optional.</p>
<h4 id="2026-03-24-secrets-config-property-deploy">Deploy</h4>
<p><code>wrangler deploy</code> and <code>wrangler versions upload</code> validate that all secrets in <code>secrets.required</code> are configured on the Worker before the operation succeeds. If any required secrets are missing, the command fails with an error listing which secrets need to be set.</p>
<p>For more information, refer to the <a href="/workers/wrangler/configuration/#secrets-configuration-property"><code>secrets</code> configuration property</a> reference.</p>


<h2 id="use-docker-hub-images-with-containers"><a href="/changelog/post/2026-03-24-docker-hub-images/">Use Docker Hub images with Containers</a></h2>
<p><em>2026-03-24</em></p>
<p>Containers now support <a href="https://hub.docker.com/">Docker Hub</a> images. You can use a fully qualified Docker Hub image reference in your <a href="https://developers.cloudflare.com/workers/wrangler/configuration/#containers">Wrangler configuration</a> instead of first pushing the image to Cloudflare Registry.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17710.md")</div>
<p>Containers also support private Docker Hub images. To configure credentials, refer to <a href="/containers/guides/image-management/#use-private-docker-hub-images">Use private Docker Hub images</a>.</p>
<p>For more information, refer to <a href="/containers/guides/image-management/">Image management</a>.</p>


<h2 id="dynamic-workers-now-in-open-beta"><a href="/changelog/post/2026-03-24-dynamic-workers-open-beta/">Dynamic Workers, now in open beta</a></h2>
<p><em>2026-03-24</em></p>
<p><a href="/dynamic-workers/">Dynamic Workers</a> are now in <a href="https://blog.cloudflare.com/dynamic-workers/">open beta</a> for all paid Workers users. You can now have a Worker spin up other Workers, called Dynamic Workers, at runtime to execute code on-demand in a secure, sandboxed environment. Dynamic Workers start in milliseconds, making them well suited for fast, secure code execution at scale.</p>
<h4 id="2026-03-24-dynamic-workers-open-beta-use-dynamic-workers-for">Use Dynamic Workers for</h4>
<ul>
<li><strong><a href="/agents/tools/codemode/">Code Mode</a></strong>: LLMs are trained to write code. Run tool-calling logic written in code instead of stepping through many tool calls, which can save up to 80% in inference tokens and cost.</li>
<li><strong>AI agents executing code</strong>: Run code for tasks like data analysis, file transformation, API calls, and chained actions.</li>
<li><strong>Running AI-generated code</strong>: Run generated code for prototypes, projects, and automations in a secure, isolated sandboxed environment.</li>
<li><strong>Fast development and previews</strong>: Load prototypes, previews, and playgrounds in milliseconds.</li>
<li><strong>Custom automations</strong>: Create custom tools on the fly that execute a task, call an integration, or automate a workflow.</li>
</ul>
<h4 id="2026-03-24-dynamic-workers-open-beta-executing-dynamic-workers">Executing Dynamic Workers</h4>
<p>Dynamic Workers support two loading modes:</p>
<ul>
<li><code>load(code)</code> — for one-time code execution (equivalent to calling <code>get()</code> with a null ID).</li>
<li><code>get(id, callback)</code> — caches a Dynamic Worker by ID so it can stay warm across requests. Use this when the same code will receive subsequent requests.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17801.md")</div>
<h4 id="2026-03-24-dynamic-workers-open-beta-helper-libraries-for-dynamic-workers">Helper libraries for Dynamic Workers</h4>
<p>Here are 3 new libraries to help you build with Dynamic Workers:</p>
<ul>
<li>
<p><strong><a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a></strong>: Replace individual tool calls with a single <code>code()</code> tool, so LLMs write and execute TypeScript that orchestrates multiple API calls in one pass.</p>
</li>
<li>
<p><strong><a href="https://www.npmjs.com/package/@cloudflare/worker-bundler"><code>@cloudflare/worker-bundler</code></a></strong>: Resolve npm dependencies and bundle source files into ready-to-load modules for Dynamic Workers, all at runtime.</p>
</li>
<li>
<p><strong><a href="https://www.npmjs.com/package/@cloudflare/shell"><code>@cloudflare/shell</code></a></strong>: Give your agent a virtual filesystem inside a Dynamic Worker with persistent storage backed by SQLite and R2.</p>
</li>
</ul>
<h4 id="2026-03-24-dynamic-workers-open-beta-try-it-out">Try it out</h4>
<p><strong>Dynamic Workers Starter</strong></p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>Use this <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers">starter</a> to deploy a Worker that can load and execute Dynamic Workers.</p>
<p><strong>Dynamic Workers Playground</strong></p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>Deploy the <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground">Dynamic Workers Playground</a> to write or import code, bundle it at runtime with <code>@cloudflare/worker-bundler</code>, execute it through a Dynamic Worker, and see real-time responses and execution logs.</p>
<p>For the full API reference and configuration options, refer to the <a href="/dynamic-workers/">Dynamic Workers documentation</a>.</p>
<h4 id="2026-03-24-dynamic-workers-open-beta-pricing">Pricing</h4>
<p>Dynamic Workers <a href="/dynamic-workers/pricing/">pricing</a> is based on three dimensions: Dynamic Workers created daily, requests, and CPU time.</p>
<table>
<thead>
<tr>
<th></th>
<th>Included</th>
<th>Additional usage</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Dynamic Workers created daily</strong></td>
<td>1,000 unique Dynamic Workers per month</td>
<td>+$0.002 per Dynamic Worker per day</td>
</tr>
<tr>
<td><strong>Requests</strong> ¹</td>
<td>10 million per month</td>
<td>+$0.30 per million requests</td>
</tr>
<tr>
<td><strong>CPU time</strong> ¹</td>
<td>30 million CPU milliseconds per month</td>
<td>+$0.02 per million CPU milliseconds</td>
</tr>
</tbody>
</table>
<p>¹ Uses <a href="/workers/platform/pricing/#workers">Workers Standard rates</a> and will appear as part of your existing Workers bill, not as separate Dynamic Workers charges.</p>
<p>Note: Dynamic Workers requests and CPU time are already billed as part of your Workers plan and will count toward your Workers requests and CPU usage. The Dynamic Workers created daily charge is not yet active — you will not be billed for the number of Dynamic Workers created at this time. Pricing information is shared in advance so you can estimate future costs.</p>


<h2 id="workflow-instances-now-support-pause-resume-restart-and-terminate-methods-in-local-development"><a href="/changelog/post/2026-03-23-local-dev-instance-methods/">Workflow instances now support pause(), resume(), restart(), and terminate() methods in local development</a></h2>
<p><em>2026-03-23 12:00:00 UTC</em></p>
<p>Workflow instance methods <code>pause()</code>, <code>resume()</code>, <code>restart()</code>, and <code>terminate()</code> are now available in local development when using <code>wrangler dev</code>.</p>
<p>You can now test the full Workflow instance lifecycle locally:</p>
<pre><code class="language-ts">const instance = await env.MY_WORKFLOW.create({&#10;	id: &quot;my-instance-id&quot;,&#10;});&#10;&#10;await instance.pause(); // pauses a running workflow instance&#10;await instance.resume(); // resumes a paused instance&#10;await instance.restart(); // restarts the instance from the beginning&#10;await instance.terminate(); // terminates the instance immediately&#10;</code></pre>


<h2 id="agents-sdk-v0-8-0-readable-state-idempotent-schedules-typed-agentclient-and-zod-4"><a href="/changelog/post/2026-03-23-agents-sdk-v0.8.0/">Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4</a></h2>
<p><em>2026-03-23</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> exposes agent state as a readable property, prevents duplicate schedule rows across Durable Object restarts, brings full TypeScript inference to <code>AgentClient</code>, and migrates to Zod 4.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-readable-state-on-useagent-and-agentclient">Readable <code>state</code> on <code>useAgent</code> and <code>AgentClient</code></h4>
<p>Both <code>useAgent</code> (React) and <code>AgentClient</code> (vanilla JS) now expose a <code>state</code> property that reflects the current agent state. Previously, reading state required manually tracking it through the <code>onStateUpdate</code> callback.</p>
<p><strong>React (<code>useAgent</code>)</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17655.md")</div>
<p><code>agent.state</code> is reactive — the component re-renders when state changes from either the server or a client-side <code>setState()</code> call.</p>
<p><strong>Vanilla JS (<code>AgentClient</code>)</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17656.md")</div>
<p>State starts as <code>undefined</code> and is populated when the server sends the initial state on connect (from <code>initialState</code>) or when <code>setState()</code> is called. Use optional chaining (<code>agent.state?.field</code>) for safe access. The <code>onStateUpdate</code> callback continues to work as before — the new <code>state</code> property is additive.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-idempotent-schedule">Idempotent <code>schedule()</code></h4>
<p><code>schedule()</code> now supports an <code>idempotent</code> option that deduplicates by <code>(type, callback, payload)</code>, preventing duplicate rows from accumulating when called in places that run on every Durable Object restart such as <code>onStart()</code>.</p>
<p><strong>Cron schedules are idempotent by default.</strong> Calling <code>schedule(&quot;0 * * * *&quot;, &quot;tick&quot;)</code> multiple times with the same callback, expression, and payload returns the existing schedule row instead of creating a new one. Pass <code>{ idempotent: false }</code> to override.</p>
<p>Delayed and date-scheduled types support opt-in idempotency:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17657.md")</div>
<p>Two new warnings help catch common foot-guns:</p>
<ul>
<li>Calling <code>schedule()</code> inside <code>onStart()</code> without <code>{ idempotent: true }</code> emits a <code>console.warn</code> with actionable guidance (once per callback; skipped for cron and when <code>idempotent</code> is set explicitly).</li>
<li>If an alarm cycle processes 10 or more stale one-shot rows for the same callback, the SDK emits a <code>console.warn</code> and a <code>schedule:duplicate_warning</code> diagnostics channel event.</li>
</ul>
<h4 id="2026-03-23-agents-sdk-v0.8.0-typed-agentclient-with-call-inference-and-stub-proxy">Typed <code>AgentClient</code> with <code>call</code> inference and <code>stub</code> proxy</h4>
<p><code>AgentClient</code> now accepts an optional agent type parameter for full type inference on RPC calls, matching the typed experience already available with <code>useAgent</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17658.md")</div>
<p>State is automatically inferred from the agent type, so <code>onStateUpdate</code> is also typed:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17659.md")</div>
<p>Existing untyped usage continues to work without changes. The RPC type utilities (<code>AgentMethods</code>, <code>AgentStub</code>, <code>RPCMethods</code>) are now exported from <code>agents/client</code> for advanced typing scenarios.
<code>agents</code>, <code>@cloudflare/ai-chat</code>, and <code>@cloudflare/codemode</code> now require <code>zod ^4.0.0</code>. Zod v3 is no longer supported.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-cloudflare-ai-chat-fixes"><code>@cloudflare/ai-chat</code> fixes</h4>
<ul>
<li><strong>Turn serialization</strong> — <code>onChatMessage()</code> and <code>_reply()</code> work is now queued so user requests, tool continuations, and <code>saveMessages()</code> never stream concurrently.</li>
<li><strong>Duplicate messages on stop</strong> — Clicking stop during an active stream no longer splits the assistant message into two entries.</li>
<li><strong>Duplicate messages after tool calls</strong> — Orphaned client IDs no longer leak into persistent storage.</li>
</ul>
<h4 id="2026-03-23-agents-sdk-v0.8.0-keepalive-and-keepalivewhile-are-no-longer-experimental"><code>keepAlive()</code> and <code>keepAliveWhile()</code> are no longer experimental</h4>
<p><code>keepAlive()</code> now uses a lightweight in-memory ref count instead of schedule rows. Multiple concurrent callers share a single alarm cycle. The <code>@experimental</code> tag has been removed from both <code>keepAlive()</code> and <code>keepAliveWhile()</code>.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-cloudflare-codemode-tanstack-ai-integration"><code>@cloudflare/codemode</code>: TanStack AI integration</h4>
<p>A new entry point <code>@cloudflare/codemode/tanstack-ai</code> adds support for <a href="https://tanstack.com/ai">TanStack AI's</a> <code>chat()</code> as an alternative to the Vercel AI SDK's <code>streamText()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17660.md")</div>
<h4 id="2026-03-23-agents-sdk-v0.8.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="new-ai-search-rest-api-endpoints-for-search-and-chat-completions"><a href="/changelog/post/2026-03-23-ai-search-new-rest-api/">New AI Search REST API endpoints for /search and /chat/completions</a></h2>
<p><em>2026-03-23</em></p>
<p><a href="/ai-search/">AI Search</a> now offers new <a href="/ai-search/api/search/rest-api/">REST API</a> endpoints for search and chat that use an OpenAI compatible format. This means you can use the familiar <code>messages</code> array structure that works with existing OpenAI SDKs and tools. The messages array also lets you pass previous messages within a session, so the model can maintain context across multiple turns.</p>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Path</th>
</tr>
</thead>
<tbody>
<tr>
<td>Chat Completions</td>
<td><code>POST /accounts/{account_id}/ai-search/instances/{name}/chat/completions</code></td>
</tr>
<tr>
<td>Search</td>
<td><code>POST /accounts/{account_id}/ai-search/instances/{name}/search</code></td>
</tr>
</tbody>
</table>
<p>Here is an example request to the Chat Completions endpoint using the new <code>messages</code> array format:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/chat/completions \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer {API_TOKEN}&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;system&quot;,&#10;        &quot;content&quot;: &quot;You are a helpful documentation assistant.&quot;&#10;      },&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;How do I get started?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/api/search/rest-api/">AI Search REST API guide</a>.</p>
<h4 id="2026-03-23-ai-search-new-rest-api-migration-from-existing-autorag-api-recommended">Migration from existing AutoRAG API (recommended)</h4>
<p>If you are using the previous AutoRAG API endpoints (<code>/autorag/rags/</code>), we recommend migrating to the new endpoints. The previous AutoRAG API endpoints will continue to be fully supported.</p>
<p>Refer to the <a href="/ai-search/api/migration/rest-api/">migration guide</a> for step-by-step instructions.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/9/">Previous</a><span>Page 10 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/11/">Next</a></nav>
