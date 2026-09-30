<h1 id="changelog">Changelog</h1>

<h2 id="use-cloudflare-containers-with-codex-via-the-openai-agents-api"><a href="/changelog/post/2026-09-10-using-openai-agents-api-with-cloudflare-containers/">Use Cloudflare Containers with Codex via the OpenAI Agents API</a></h2>
<p><em>2026-09-10</em></p>
<p>The OpenAI Agents API gives your application access to Codex through an OpenAI-managed API.</p>
<p>OpenAI manages sessions, orchestration, context compaction, and recovery while your application provides tools and uses Cloudflare Containers as the execution environment.</p>
<p>Cloudflare Containers can now provide self-hosted execution environments for the OpenAI Agents API. The open-source <a href="https://github.com/cloudflare/sandbox-sdk/tree/main/openai/agents-api">OpenAI Agents API Workers template</a> provides a reference implementation. The Worker maintains a Cloudflare Container for each Codex session, keeps active work running, reconnects on follow-up input, and shuts down automatically when idle.</p>
<p>You can configure the reference implementation to meet your needs by extending the Container to provide controlled access to data and the network or by integrating it with other Cloudflare products.</p>
<p>To get started, refer to <a href="/sandbox/tutorials/openai-agents-api/">Run Codex on Cloudflare using the OpenAI Agents API</a>.</p>


<h2 id="use-fuse-in-local-containers-development"><a href="/changelog/post/2026-08-20-fuse-local-development/">Use FUSE in local Containers development</a></h2>
<p><em>2026-08-20</em></p>
<p>Miniflare now automatically grants local Containers the Docker privileges required for Filesystem in Userspace (FUSE). This applies to <code>wrangler dev</code>, the Cloudflare Vite plugin, and direct Miniflare use.</p>
<p>Miniflare grants these privileges when the local Docker daemon runs inside a virtual machine (VM). This includes Docker engines on macOS and through Windows Subsystem for Linux (WSL). On Linux, Miniflare grants the privileges for local rootless Docker when <code>/dev/fuse</code> is available.</p>
<p>Rootful Docker on Linux does not support FUSE by default during local development. Miniflare does not grant FUSE privileges when the Docker daemon does not meet these conditions or cannot be inspected.</p>
<p>For requirements and troubleshooting, refer to <a href="/containers/guides/local-dev/#fuse-support">FUSE support during local development</a>. For a complete example, refer to <a href="/containers/examples/r2-fuse-mount/">Mount R2 buckets with FUSE</a>.</p>


<h2 id="use-google-artifact-registry-images-with-containers"><a href="/changelog/post/2026-07-01-google-artifact-registry-images/">Use Google Artifact Registry images with Containers</a></h2>
<p><em>2026-07-01</em></p>
<p>Containers now support <a href="https://cloud.google.com/artifact-registry">Google Artifact Registry</a> images. After you configure credentials, you can use a fully qualified Google Artifact Registry image reference in your <a href="/workers/wrangler/configuration/#containers">Wrangler configuration</a> instead of first pushing the image to Cloudflare Registry.</p>
<p>Provide the service account email with <code>--gar-email</code> and pipe the service account JSON key through <code>stdin</code>:</p>
<pre><code class="language-bash">cat &lt;PATH_TO_KEY&gt; | npx wrangler containers registries configure &lt;REGION&gt;-docker.pkg.dev --gar-email=&lt;SERVICE_ACCOUNT_EMAIL&gt; --secret-name=&lt;SECRET_NAME&gt;&#10;</code></pre>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17714.md")</div>
<p>Only <code>*-docker.pkg.dev</code> hosts are supported. To configure credentials, refer to <a href="/containers/guides/image-management/#use-private-google-artifact-registry-images">Use private Google Artifact Registry images</a>.</p>
<p>For more information, refer to <a href="/containers/guides/image-management/">Image management</a>.</p>


<h2 id="exec-is-now-available-for-containers"><a href="/changelog/post/2026-06-18-container-exec/">exec() is now available for Containers</a></h2>
<p><em>2026-06-18</em></p>
<p><code>exec()</code> is now available for <a href="/containers/">Containers</a>. Use <code>this.ctx.container.exec()</code> to start processes inside a running Container, stream standard input and output, inspect exit codes, and signal each process.</p>
<p>Call <code>exec()</code> from a class extending <code>Container</code>, or from another Durable Object through <code>this.ctx.container</code>. The associated Container must already be running.</p>
<p>This example starts the Container when needed, then reads its Node.js version:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17713.md")</div>
<p>The command array starts an executable directly, without an implicit shell. Invoke a shell explicitly for pipes, redirects, or variable expansion.</p>
<p>One RPC method can coordinate multiple <code>exec()</code> calls in one caller-to-Durable Object round trip. It can also pass byte-oriented <code>ReadableStream</code> input or return streamed output with flow control.</p>
<p>For options and streaming examples, refer to <a href="/containers/guides/execute-commands/">Execute commands</a>.</p>


<h2 id="billable-usage-and-budget-alerts-now-in-product-sidebars"><a href="/changelog/post/2026-06-04-billable-usage-product-sidebar/">Billable usage and budget alerts now in product sidebars</a></h2>
<p><em>2026-06-04</em></p>
<p>Pay-as-you-go customers can now view billable usage and create <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">budget alerts</a> directly from the product overview pages for <a href="/workers/">Workers &amp; Pages</a>, <a href="/d1/">D1</a>, <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/containers/">Containers</a>. A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.</p>
<p>The widget pulls from the same data as the <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Billable Usage dashboard</a> and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-06-04-billable-usage-product-sidebar.png" alt="Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service" /></p>
<p>Selecting <strong>Create budget alert</strong> opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.</p>
<p>For more information, refer to the <a href="/billing/">Usage-based billing documentation</a>.</p>


<h2 id="wrangler-supports-ssh-proxycommand-for-containers"><a href="/changelog/post/2026-05-28-ssh-proxy-command/">Wrangler supports SSH ProxyCommand for Containers</a></h2>
<p><em>2026-05-28</em></p>
<p><a href="/workers/wrangler/">Wrangler</a> supports using <code>wrangler containers ssh</code> as an OpenSSH <code>ProxyCommand</code> for <a href="/containers/">Containers</a>. This lets your local SSH client connect to a running Container through Wrangler.</p>
<pre><code class="language-sh">ssh -o ProxyCommand=&quot;wrangler containers ssh %h&quot; cloudchamber@&lt;INSTANCE_ID&gt;&#10;</code></pre>
<p>When standard input and output are piped, Wrangler forwards data to the SSH server in the Container. You can also pass <code>--stdio</code> to force this mode.</p>
<p>For more information, refer to the <a href="/containers/guides/ssh/">SSH documentation</a>.</p>


<h2 id="ssh-through-wrangler-is-now-enabled-by-default-for-containers"><a href="/changelog/post/2026-05-12-ssh-enabled-by-default/">SSH through Wrangler is now enabled by default for Containers</a></h2>
<p><em>2026-05-12</em></p>
<p>SSH through Wrangler is now enabled by default for <a href="/containers/">Containers</a>. Previously, you had to set <code>ssh.enabled</code> to <code>true</code> in your Container configuration before you could connect.</p>
<p>This change does not expose any publicly accessible ports on your Container. The SSH service is reachable only through <a href="/workers/wrangler/commands/containers/#containers-ssh"><code>wrangler containers ssh</code></a>, which authenticates against your Cloudflare account. You also need to add an <code>ssh-ed25519</code> public key to <code>authorized_keys</code> before anyone can connect, so enabling SSH alone does not grant access.</p>
<p>To connect, add a public key to your Container configuration and run <code>wrangler containers ssh &lt;INSTANCE_ID&gt;</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17711.md")</div>
<p>To disable SSH, set <code>ssh.enabled</code> to <code>false</code> in your Container configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17712.md")</div>
<p>For more information, refer to the <a href="/containers/guides/ssh/">SSH documentation</a>.</p>


<h2 id="container-logs-page-now-includes-relevant-worker-and-durable-object-logs"><a href="/changelog/post/2026-04-21-correlated-worker-durable-object-logs/">Container logs page now includes relevant Worker and Durable Object logs</a></h2>
<p><em>2026-04-21</em></p>
<p>The Container logs page now displays related <a href="/workers/">Worker</a> and <a href="/durable-objects/">Durable Object</a> logs alongside container logs. This co-locates all relevant log events for a container application in one place, making it easier to trace requests and debug issues.</p>
<p><img src="/assets/upstream/images/containers/container-worker-logs.png" alt="Container logs page showing Worker and Durable Object logs alongside container logs" /></p>
<p>You can filter to a single source when you need to isolate Container, Worker, or Durable Object output.</p>
<p>For information on configuring container logging, refer to <a href="/containers/faq/#how-do-container-logs-work">How do Container logs work?</a>.</p>


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


<h2 id="use-docker-hub-images-with-containers"><a href="/changelog/post/2026-03-24-docker-hub-images/">Use Docker Hub images with Containers</a></h2>
<p><em>2026-03-24</em></p>
<p>Containers now support <a href="https://hub.docker.com/">Docker Hub</a> images. You can use a fully qualified Docker Hub image reference in your <a href="https://developers.cloudflare.com/workers/wrangler/configuration/#containers">Wrangler configuration</a> instead of first pushing the image to Cloudflare Registry.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17710.md")</div>
<p>Containers also support private Docker Hub images. To configure credentials, refer to <a href="/containers/guides/image-management/#use-private-docker-hub-images">Use private Docker Hub images</a>.</p>
<p>For more information, refer to <a href="/containers/guides/image-management/">Image management</a>.</p>


<h2 id="ssh-into-running-container-instances"><a href="/changelog/post/2026-03-12-ssh-support/">SSH into running Container instances</a></h2>
<p><em>2026-03-12</em></p>
<p>You can now SSH into running Container instances using Wrangler. This is useful for debugging, inspecting running processes, or executing one-off commands inside a Container.</p>
<p>To connect, enable <code>wrangler_ssh</code> in your Container configuration and add your <code>ssh-ed25519</code> public key to <code>authorized_keys</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17709.md")</div>
<p>Then connect with:</p>
<pre><code class="language-sh">wrangler containers ssh &lt;INSTANCE_ID&gt;&#10;</code></pre>
<p>You can also run a single command without opening an interactive shell:</p>
<pre><code class="language-sh">wrangler containers ssh &lt;INSTANCE_ID&gt; -- ls -al&#10;</code></pre>
<p>Use <code>wrangler containers instances &lt;APPLICATION&gt;</code> to find the instance ID for a running Container.</p>
<p>For more information, refer to the <a href="/containers/guides/ssh/">SSH documentation</a>.</p>


<h2 id="list-container-instances-with-wrangler-containers-instances"><a href="/changelog/post/2026-03-12-wrangler-containers-instances/">List Container instances with `wrangler containers instances`</a></h2>
<p><em>2026-03-12</em></p>
<p>A new <a href="/workers/wrangler/commands/containers/#containers-instances"><code>wrangler containers instances</code></a> command lists all instances for a given Container application. This mirrors the instances view in the Cloudflare dashboard.</p>
<p>The command displays each instance's ID, name, state, location, version, and creation time:</p>
<pre><code class="language-sh">wrangler containers instances &lt;APPLICATION_ID&gt;&#10;</code></pre>
<p>Use the <code>--json</code> flag for machine-readable output, which is also the default format in non-interactive environments such as CI pipelines.</p>
<p>For the full list of options, refer to the <a href="/workers/wrangler/commands/containers/#containers-instances"><code>containers instances</code> command reference</a>.</p>


<h2 id="run-15x-more-containers-with-higher-resource-limits"><a href="/changelog/post/2026-02-25-higher-container-resource-limits/">Run 15x more Containers with higher resource limits</a></h2>
<p><em>2026-02-25</em></p>
<p>You can now run more <a href="/containers/">Containers</a> concurrently with significantly higher limits on memory, vCPU, and disk.</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Previous Limit</th>
<th>New Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Memory for concurrent live Container instances</td>
<td>400GiB</td>
<td>6TiB</td>
</tr>
<tr>
<td>vCPU for concurrent live Container instances</td>
<td>100</td>
<td>1,500</td>
</tr>
<tr>
<td>Disk for concurrent live Container instances</td>
<td>2TB</td>
<td>30TB</td>
</tr>
</tbody>
</table>
<p>This 15x increase enables larger-scale workloads on Containers. You can now run 15,000 instances of the <code>lite</code> instance type, 6,000 instances of <code>basic</code>, over 1,500 instances of <code>standard-1</code>, or over 1,000 instances of <code>standard-2</code> concurrently.</p>
<p>Refer to <a href="/containers/platform/limits/">Limits</a> for more details on the available instance types and limits.</p>


<h2 id="backup-and-restore-api-for-sandbox-sdk"><a href="/changelog/post/2026-02-23-sandbox-backup-restore-api/">Backup and restore API for Sandbox SDK</a></h2>
<p><em>2026-02-23</em></p>
<p><a href="/sandbox/">Sandboxes</a> now support <code>createBackup()</code> and <code>restoreBackup()</code> methods for creating and restoring point-in-time snapshots of directories.</p>
<p>This allows you to restore environments quickly. For instance, in order to develop in a sandbox, you may need to include a user's codebase and run a build step.
Unfortunately <code>git clone</code> and <code>npm install</code> can take minutes, and you don't want to run these steps every time the user starts their sandbox.</p>
<p>Now, after the initial setup, you can just call <code>createBackup()</code>, then <code>restoreBackup()</code> the next time this environment is needed. This makes it practical to pick up exactly
where a user left off, even after days of inactivity, without repeating expensive setup steps.</p>
<pre><code class="language-ts">const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;&#10;// Make non-trivial changes to the file system&#10;await sandbox.gitCheckout(endUserRepo, { targetDir: &quot;/workspace&quot; });&#10;await sandbox.exec(&quot;npm install&quot;, { cwd: &quot;/workspace&quot; });&#10;&#10;// Create a point-in-time backup of the directory&#10;const backup = await sandbox.createBackup({ dir: &quot;/workspace&quot; });&#10;&#10;// Store the handle for later use&#10;await env.KV.put(`backup:${userId}`, JSON.stringify(backup));&#10;&#10;// ... in a future session...&#10;&#10;// Restore instead of re-cloning and reinstalling&#10;await sandbox.restoreBackup(backup);&#10;</code></pre>
<p>Backups are stored in <a href="/r2">R2</a> and can take advantage of <a href="/sandbox/guides/backup-restore/#configure-r2-lifecycle-rules-for-automatic-cleanup">R2 object lifecycle rules</a> to ensure they do not persist forever.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>Persist and reuse across sandbox sessions</strong> — Easily store backup handles in KV, D1, or Durable Object storage for use in subsequent sessions</li>
<li><strong>Usable across multiple instances</strong> — Fork a backup across many sandboxes for parallel work</li>
<li><strong>Named backups</strong> — Provide optional human-readable labels for easier management</li>
<li><strong>TTLs</strong> — Set time-to-live durations so backups are automatically removed from storage once they are no longer needed</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17640.md")</aside>
<p>To get started, refer to the <a href="/sandbox/guides/backup-restore/">backup and restore guide</a> for setup instructions and usage patterns, or the <a href="/sandbox/api/backups/">Backups API reference</a> for full method documentation.</p>


<h2 id="docker-in-docker-support-added-to-containers-and-sandboxes"><a href="/changelog/post/2026-02-17-docker-in-docker/">Docker-in-Docker support added to Containers and Sandboxes</a></h2>
<p><em>2026-02-17</em></p>
<p><a href="/sandbox/">Sandboxes</a> and <a href="/containers/">Containers</a> now support running Docker for &quot;Docker-in-Docker&quot; setups. This is particularly useful when your end users or <a href="/agents">agents</a> want to run a full sandboxed development environment.</p>
<p>This allows you to:</p>
<ul>
<li>Develop containerized applications with your Sandbox</li>
<li>Run isolated test environments for images</li>
<li>Build container images as part of CI/CD workflows</li>
<li>Deploy arbitrary images supplied at runtime within a container</li>
</ul>
<p>For <a href="/sandbox/">Sandbox SDK</a> users, see the <a href="/sandbox/guides/docker-in-docker/">Docker-in-Docker guide</a> for instructions on combining Docker with the SandboxSDK. For general Containers usage, see the <a href="/containers/faq/#can-i-run-docker-inside-a-container-docker-in-docker">Containers FAQ</a>.</p>


<h2 id="custom-container-instance-types-now-available-for-all-users"><a href="/changelog/post/2026-01-05-custom-instance-types/">Custom container instance types now available for all users</a></h2>
<p><em>2026-01-05</em></p>
<p>Custom instance types are now enabled for all <a href="/containers">Cloudflare Containers</a> users. You can now specify specific vCPU, memory, and disk amounts, rather than being limited to pre-defined <a href="/containers/platform/limits/#instance-types">instance types</a>. Previously, only select Enterprise customers were able to customize their instance type.</p>
<p>To use a custom instance type, specify the <code>instance_type</code> property as an object with <code>vcpu</code>, <code>memory_mib</code>, and <code>disk_mb</code> fields in your Wrangler configuration:</p>
<pre><code class="language-toml">[[containers]]&#10;image = &quot;./Dockerfile&quot;&#10;instance_type = { vcpu = 2, memory_mib = 6144, disk_mb = 12000 }&#10;</code></pre>
<p>Individual limits for custom instance types are based on the <code>standard-4</code> instance type (4 vCPU, 12 GiB memory, 20 GB disk). You must allocate at least 1 vCPU for custom instance types. For workloads requiring less than 1 vCPU, use the predefined instance types like <code>lite</code> or <code>basic</code>.</p>
<p>See the <a href="/containers/platform/limits/#custom-instance-types">limits documentation</a> for the full list of constraints on custom instance types.
See the <a href="/containers/get-started/">getting started guide</a> to deploy your first Container,</p>


<h2 id="mount-r2-buckets-in-containers"><a href="/changelog/post/2025-11-21-fuse-support-in-containers/">Mount R2 buckets in Containers</a></h2>
<p><em>2025-11-21</em></p>
<p><a href="/containers/">Containers</a> now support mounting R2 buckets as FUSE (Filesystem in Userspace) volumes, allowing applications to interact with <a href="/r2/">R2</a> using standard filesystem operations.</p>
<p>Common use cases include:</p>
<ul>
<li>Bootstrapping containers with datasets, models, or dependencies for <a href="/sandbox/">sandboxes</a> and <a href="/agents/">agent</a> environments</li>
<li>Persisting user configuration or application state without managing downloads</li>
<li>Accessing large static files without bloating container images or downloading at startup</li>
</ul>
<p>FUSE adapters like <a href="https://github.com/tigrisdata/tigrisfs">tigrisfs</a>, <a href="https://github.com/s3fs-fuse/s3fs-fuse">s3fs</a>, and <a href="https://github.com/GoogleCloudPlatform/gcsfuse">gcsfuse</a> can be installed in your container image and configured to mount buckets at startup.</p>
<pre><code class="language-dockerfile">FROM alpine:3.20&#10;&#10;&#35; Install FUSE and dependencies&#10;RUN apk update &amp;&amp; \&#10;    apk add --no-cache ca-certificates fuse curl bash&#10;&#10;&#35; Install tigrisfs&#10;RUN ARCH=$(uname -m) &amp;&amp; \&#10;    if [ &quot;$ARCH&quot; = &quot;x86_64&quot; ]; then ARCH=&quot;amd64&quot;; fi &amp;&amp; \&#10;    if [ &quot;$ARCH&quot; = &quot;aarch64&quot; ]; then ARCH=&quot;arm64&quot;; fi &amp;&amp; \&#10;    VERSION=$(curl -s https://api.github.com/repos/tigrisdata/tigrisfs/releases/latest | grep -o &#x27;&quot;tag_name&quot;: &quot;[^&quot;]*&#x27; | cut -d&#x27;&quot;&#x27; -f4) &amp;&amp; \&#10;    curl -L &quot;https://github.com/tigrisdata/tigrisfs/releases/download/${VERSION}/tigrisfs_${VERSION#v}_linux_${ARCH}.tar.gz&quot; -o /tmp/tigrisfs.tar.gz &amp;&amp; \&#10;    tar -xzf /tmp/tigrisfs.tar.gz -C /usr/local/bin/ &amp;&amp; \&#10;    rm /tmp/tigrisfs.tar.gz &amp;&amp; \&#10;    chmod +x /usr/local/bin/tigrisfs&#10;&#10;&#35; Create startup script that mounts bucket&#10;RUN printf &#x27;#!/bin/sh\n\&#10;    set -e\n\&#10;    mkdir -p /mnt/r2\n\&#10;    R2_ENDPOINT=&quot;https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com&quot;\n\&#10;    /usr/local/bin/tigrisfs --endpoint &quot;${R2_ENDPOINT}&quot; -f &quot;${BUCKET_NAME}&quot; /mnt/r2 &amp;\n\&#10;    sleep 3\n\&#10;    ls -lah /mnt/r2\n\&#10;    &#x27; &gt; /startup.sh &amp;&amp; chmod +x /startup.sh&#10;&#10;CMD [&quot;/startup.sh&quot;]&#10;</code></pre>
<p>See the <a href="/containers/examples/r2-fuse-mount/">Mount R2 buckets with FUSE</a> example for a complete guide on mounting R2 buckets and/or other S3-compatible storage buckets within your containers.</p>


<h2 id="new-cpu-pricing-for-containers-and-sandboxes"><a href="/changelog/post/2025-11-21-new-cpu-pricing/">New CPU Pricing for Containers and Sandboxes</a></h2>
<p><em>2025-11-21</em></p>
<p><a href="/containers/">Containers</a> and <a href="/sandbox/">Sandboxes</a> pricing for CPU time is now based on active usage only, instead of provisioned resources.</p>
<p>This means that you now pay less for Containers and Sandboxes.</p>
<h4 id="2025-11-21-new-cpu-pricing-an-example-before-and-after">An Example Before and After</h4>
<p>Imagine running the <code>standard-2</code> instance type for one hour, which can use up to 1 vCPU,
but on average you use only 20% of your CPU capacity.</p>
<p>CPU-time is priced at <em>$0.00002 per vCPU-second</em>.</p>
<p>Previously, you would be charged for the CPU allocated to the instance multiplied by the time it was active, in this case 1 hour.</p>
<p>CPU cost would have been: <strong>$0.072</strong> — 1 vCPU * 3600 seconds * $0.00002</p>
<p>Now, since you are only using 20% of your CPU capacity, your CPU cost is cut to 20% of the previous amount.</p>
<p>CPU cost is now: <strong>$0.0144</strong> — 1 vCPU * 3600 seconds * $0.00002 * 20% utilization</p>
<p>This can significantly reduce costs for Containers and Sandboxes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17708.md")</aside>
<p>See the documentation to learn more about <a href="/containers/get-started/">Containers</a>, <a href="/sandbox/">Sandboxes</a>,
and <a href="/containers/platform/pricing">associated pricing</a>.</p>


<h2 id="larger-container-instance-types"><a href="/changelog/post/2025-10-01-new-container-instance-types/">Larger Container instance types</a></h2>
<p><em>2025-10-01</em></p>
<p>New instance types provide up to 4 vCPU, 12 GiB of memory, and 20 GB of disk per container instance.</p>
<table>
<thead>
<tr>
<th>Instance Type</th>
<th>vCPU</th>
<th>Memory</th>
<th>Disk</th>
</tr>
</thead>
<tbody>
<tr>
<td>lite</td>
<td>1/16</td>
<td>256 MiB</td>
<td>2 GB</td>
</tr>
<tr>
<td>basic</td>
<td>1/4</td>
<td>1 GiB</td>
<td>4 GB</td>
</tr>
<tr>
<td>standard-1</td>
<td>1/2</td>
<td>4 GiB</td>
<td>8 GB</td>
</tr>
<tr>
<td>standard-2</td>
<td>1</td>
<td>6 GiB</td>
<td>12 GB</td>
</tr>
<tr>
<td>standard-3</td>
<td>2</td>
<td>8 GiB</td>
<td>16 GB</td>
</tr>
<tr>
<td>standard-4</td>
<td>4</td>
<td>12 GiB</td>
<td>20 GB</td>
</tr>
</tbody>
</table>
<p>The <code>dev</code> and <code>standard</code> instance types are preserved for backward compatibility and are aliases for <code>lite</code> and <code>standard-1</code>, respectively. The <code>standard-1</code> instance type now provides up to 8 GB of disk instead of only 4 GB.</p>
<p>See the <a href="/containers/get-started/">getting started guide</a> to deploy your first Container,
and the <a href="/containers/platform/limits/">limits documentation</a> for more details on the available instance types and limits.</p>


<h2 id="run-more-containers-with-higher-resource-limits"><a href="/changelog/post/2025-09-24-higher-container-resource-limits/">Run more Containers with higher resource limits</a></h2>
<p><em>2025-09-25</em></p>
<p>You can now run more Containers concurrently with higher limits on CPU, memory, and disk.</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>New Limit</th>
<th>Previous Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Memory for concurrent live Container instances</td>
<td>400GiB</td>
<td>40GiB</td>
</tr>
<tr>
<td>vCPU for concurrent live Container instances</td>
<td>100</td>
<td>20</td>
</tr>
<tr>
<td>Disk for concurrent live Container instances</td>
<td>2TB</td>
<td>100GB</td>
</tr>
</tbody>
</table>
<p>You can now run 1000 instances of the <code>dev</code> instance type, 400 instances of <code>basic</code>, or 100 instances of <code>standard</code> concurrently.</p>
<p>This opens up new possibilities for running larger-scale workloads on Containers.</p>
<p>See the <a href="/containers/get-started/">getting started guide</a> to deploy your first Container,
and the <a href="/containers/platform/limits/">limits documentation</a> for more details on the available instance types and limits.</p>



