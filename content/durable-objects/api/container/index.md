<h2 id="description">Description</h2>
<p>Each <a href="/containers/">container</a> is managed by a Durable Object. The <a href="/containers/reference/container-class/"><code>Container</code> class</a> from <code>@cloudflare/containers</code> extends <code>DurableObject</code> and handles lifecycle management, port readiness, and sleep timeouts for you. The Durable Object manages routing, persistent state, and lifecycle hooks, while the container process runs your image inside a Linux VM.</p>
<p>The low-level API documented on this page is available on <code>this.ctx.container</code> inside any Durable Object class that has a container binding. Use it when you need direct control over the container process or cannot use the <code>Container</code> class.</p>
<p>Because the <code>Container</code> class extends <code>DurableObject</code>, you also have access to <a href="/durable-objects/api/sqlite-storage-api/">SQLite storage</a> via <code>this.ctx.storage</code>, <a href="/durable-objects/api/alarms/">alarms</a>, and all other Durable Object APIs.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8403.md")
</div>
<h2 id="attributes">Attributes</h2>
<h3 id="running"><code>running</code></h3>
<p><code>running</code> returns <code>true</code> if the container is currently running. It does not ensure that the container has fully started and ready to accept requests.</p>
<pre><code class="language-js">	this.ctx.container.running;&#10;</code></pre>
<h2 id="methods">Methods</h2>
<h3 id="start"><code>start</code></h3>
<p><code>start</code> boots a container. This method does not block until the container is fully started.
You may want to confirm the container is ready to accept requests before using it.</p>
<pre><code class="language-js">this.ctx.container.start({&#10;	env: {&#10;		FOO: &quot;bar&quot;,&#10;	},&#10;	enableInternet: false,&#10;	entrypoint: [&quot;node&quot;, &quot;server.js&quot;],&#10;});&#10;</code></pre>
<h4 id="parameters">Parameters</h4>
<ul>
<li><code>options</code> (optional): An object with the following properties:
<ul>
<li><code>env</code>: An object containing environment variables to pass to the container. This is useful for passing configuration values or secrets to the container.</li>
<li><code>entrypoint</code>: An array of strings representing the command to run in the container.</li>
<li><code>enableInternet</code>: A boolean indicating whether to enable internet access for the container.</li>
</ul>
</li>
</ul>
<h4 id="return-values">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h3 id="exec"><code>exec</code></h3>
<p><code>exec</code> starts another process inside an already-running Container. It does not start a stopped Container.</p>
<p>The following example calls <code>this.ctx.container.exec()</code> inside a class extending <code>Container</code> from <code>@cloudflare/containers</code>. In RPC methods, check <code>this.ctx.container.running</code> and call <code>await this.start()</code> when needed. You can also use the <code>onStart()</code> hook to run any series of commands whenever the Container starts.</p>
<pre><code class="language-ts">exec(&#10;  cmd: string[],&#10;  options?: ContainerExecOptions,&#10;): Promise&lt;ExecProcess&gt;&#10;</code></pre>
<p>The <code>exec</code> operation starts the executable directly with the provided arguments. It does not start a shell or interpret pipes, redirects, expansion, or other shell syntax. Invoke Bash explicitly with <code>[&quot;bash&quot;, &quot;-lc&quot;, &quot;&lt;COMMAND&gt;&quot;]</code> when Bash exists in the image. Use <code>[&quot;sh&quot;, &quot;-c&quot;, &quot;&lt;COMMAND&gt;&quot;]</code> for images with only a Portable Operating System Interface (POSIX) shell.</p>
<p>The following RPC method starts the Container before executing a command:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8404.md")
</div>
<h4 id="parameters-1">Parameters</h4>
<ul>
<li><code>cmd</code> (<code>string[]</code>) — executable followed by its arguments.</li>
<li><code>options</code> (<code>ContainerExecOptions</code>, optional) — process configuration:
<ul>
<li><code>stdin</code> (<code>ReadableStream | &quot;pipe&quot;</code>) — source for standard input. Use <code>&quot;pipe&quot;</code> to write through the returned <code>stdin</code> stream. When omitted, standard input closes and sends end-of-file (EOF).</li>
<li><code>stdout</code> (<code>&quot;pipe&quot; | &quot;ignore&quot;</code>, default <code>&quot;pipe&quot;</code>) — captures or discards standard output.</li>
<li><code>stderr</code> (<code>&quot;pipe&quot; | &quot;ignore&quot; | &quot;combined&quot;</code>, default <code>&quot;pipe&quot;</code>) — captures, discards, or merges standard error into standard output. The <code>&quot;combined&quot;</code> value requires <code>stdout: &quot;pipe&quot;</code>. Combined output does not guarantee ordering between its source streams.</li>
<li><code>cwd</code> (<code>string</code>) — working directory for the process.</li>
<li><code>env</code> (<code>Record&lt;string, string&gt;</code>) — environment additions and overrides. The process inherits existing Container variables. Matching keys use the per-execution value.</li>
<li><code>user</code> (<code>string</code>) — image user for the process.</li>
</ul>
</li>
</ul>
<h4 id="return-values-1">Return values</h4>
<p>Returns <code>Promise&lt;ExecProcess&gt;</code>.</p>
<p>An <code>ExecProcess</code> has these fields and methods:</p>
<ul>
<li><code>stdin</code> (<code>WritableStream | null</code>) — writable standard input when <code>stdin</code> is <code>&quot;pipe&quot;</code>.</li>
<li><code>stdout</code> (<code>ReadableStream | null</code>) — readable standard output when piped.</li>
<li><code>stderr</code> (<code>ReadableStream | null</code>) — readable standard error when piped separately.</li>
<li><code>pid</code> (<code>number</code>) — process identifier.</li>
<li><code>exitCode</code> (<code>Promise&lt;number&gt;</code>) — resolves when the process exits. Nonzero codes resolve normally instead of rejecting.</li>
<li><code>output()</code> (<code>Promise&lt;ExecOutput&gt;</code>) — reads buffered output once. <code>ExecOutput</code> contains <code>stdout</code> (<code>ArrayBuffer</code>), <code>stderr</code> (<code>ArrayBuffer</code>), and <code>exitCode</code> (<code>number</code>). Ignored streams produce empty buffers. Use <code>TextDecoder</code> to decode text.</li>
<li><code>kill(signal?: number)</code> (<code>void</code>) — queues a signal for the process. The default is <code>SIGTERM</code>, signal <code>15</code>. The signal must be from <code>1</code> through <code>64</code>.</li>
</ul>
<p>With <code>stderr: &quot;combined&quot;</code>, <code>stderr</code> is <code>null</code> on <code>ExecProcess</code> and an empty <code>ArrayBuffer</code> on <code>ExecOutput</code>. Read both output channels from <code>stdout</code>.</p>
<p><code>output()</code> throws a <code>TypeError</code> when called more than once or after either readable stream starts being consumed. For large output, consume both readable streams concurrently instead of buffering them with <code>output()</code>.</p>
<p><code>exec</code> has no built-in timeout. Use <code>kill()</code> to request termination, then observe completion through <code>exitCode</code>. A process can handle or ignore a signal, so this does not enforce a hard deadline. Do not infer a specific exit code from the signal.</p>
<h4 id="exceptions">Exceptions</h4>
<ul>
<li><code>exec()</code> throws when the Container is not running.</li>
<li><code>exec()</code> throws a <code>TypeError</code> when <code>cmd</code> is empty, an option mode is invalid, or <code>stderr: &quot;combined&quot;</code> is used with <code>stdout: &quot;ignore&quot;</code>.</li>
<li><code>exec()</code> rejects if the runtime cannot create or start the process.</li>
<li>Environment variable names cannot contain <code>=</code> or null characters. Environment values, <code>cwd</code>, and <code>user</code> cannot contain null characters.</li>
<li><code>kill()</code> throws a <code>RangeError</code> when the signal is outside the supported range.</li>
</ul>
<p>For task-oriented examples, refer to <a href="/containers/guides/execute-commands/">Execute commands</a>.</p>
<h3 id="destroy"><code>destroy</code></h3>
<p><code>destroy</code> stops the container and optionally returns a custom error message to the <code>monitor()</code> error callback.</p>
<pre><code class="language-js">this.ctx.container.destroy(&quot;Manually Destroyed&quot;);&#10;</code></pre>
<h4 id="parameters-2">Parameters</h4>
<ul>
<li><code>error</code> (optional): A string that will be sent to the error handler of the <code>monitor</code> method. This is useful for logging or debugging purposes.</li>
</ul>
<h4 id="return-values-2">Return values</h4>
<ul>
<li>A promise that returns once the container is destroyed.</li>
</ul>
<h3 id="signal"><code>signal</code></h3>
<p><code>signal</code> sends an IPC signal to the container, such as SIGKILL or SIGTERM. This is useful for stopping the container gracefully or forcefully.</p>
<pre><code class="language-js">const SIGTERM = 15;&#10;this.ctx.container.signal(SIGTERM);&#10;</code></pre>
<h4 id="parameters-3">Parameters</h4>
<ul>
<li><code>signal</code>: a number representing the signal to send to the container. This is typically a POSIX signal number, such as SIGTERM (15) or SIGKILL (9).</li>
</ul>
<h4 id="return-values-3">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h3 id="gettcpport"><code>getTcpPort</code></h3>
<p><code>getTcpPort</code> returns a TCP port from the container. This can be used to communicate with the container over TCP and HTTP.</p>
<pre><code class="language-js">const port = this.ctx.container.getTcpPort(8080);&#10;const res = await port.fetch(&quot;http://container/set-state&quot;, {&#10;	body: initialState,&#10;	method: &quot;POST&quot;,&#10;});&#10;</code></pre>
<pre><code class="language-js">const conn = this.ctx.container.getTcpPort(8080).connect(&quot;10.0.0.1:8080&quot;);&#10;await conn.opened;&#10;&#10;try {&#10;	if (request.body) {&#10;		await request.body.pipeTo(conn.writable);&#10;	}&#10;	return new Response(conn.readable);&#10;} catch (err) {&#10;	console.error(&quot;Request body piping failed:&quot;, err);&#10;	return new Response(&quot;Failed to proxy request body&quot;, { status: 502 });&#10;}&#10;</code></pre>
<h4 id="parameters-4">Parameters</h4>
<ul>
<li><code>port</code> (number): a TCP port number to use for communication with the container.</li>
</ul>
<h4 id="return-values-4">Return values</h4>
<ul>
<li><code>TcpPort</code>: a <code>TcpPort</code> object representing the TCP port. This object can be used to send requests to the container over TCP and HTTP.</li>
</ul>
<h3 id="monitor"><code>monitor</code></h3>
<p><code>monitor</code> returns a promise that resolves when a container exits and errors if a container errors. This is useful for setting up
callbacks to handle container status changes in your Workers code.</p>
<pre><code class="language-js">class MyContainer extends DurableObject {&#10;	constructor(ctx, env) {&#10;		super(ctx, env);&#10;		function onContainerExit() {&#10;			console.log(&quot;Container exited&quot;);&#10;		}&#10;&#10;		// the &quot;err&quot; value can be customized by the destroy() method&#10;		async function onContainerError(err) {&#10;			console.log(&quot;Container errored&quot;, err);&#10;		}&#10;&#10;		this.ctx.container.start();&#10;		this.ctx.container.monitor().then(onContainerExit).catch(onContainerError);&#10;	}&#10;}&#10;</code></pre>
<h4 id="parameters-5">Parameters</h4>
<ul>
<li>None</li>
</ul>
<h4 id="return-values-5">Return values</h4>
<ul>
<li>A promise that resolves when the container exits.</li>
</ul>
<h3 id="interceptoutboundhttp"><code>interceptOutboundHttp</code></h3>
<p><code>interceptOutboundHttp</code> routes outbound HTTP requests matching a hostname, hostname glob, IP address, IP:port, or CIDR range through a <code>WorkerEntrypoint</code>. Can be called before or after starting the container. Open connections pick up the new handler without being dropped.</p>
<pre><code class="language-js">const worker = this.ctx.exports.MyWorker({ props: { message: &quot;hello&quot; } });&#10;&#10;// Match a specific hostname&#10;this.ctx.container.interceptOutboundHttp(&quot;api.example.com&quot;, worker);&#10;&#10;// Match a hostname glob pattern&#10;this.ctx.container.interceptOutboundHttp(&quot;*.example.com&quot;, worker);&#10;&#10;// Match an IP:port&#10;await this.ctx.container.interceptOutboundHttp(&quot;15.0.0.1:80&quot;, worker);&#10;&#10;// Match a CIDR range (IPv4 and IPv6)&#10;await this.ctx.container.interceptOutboundHttp(&quot;123.123.123.123/23&quot;, worker);&#10;</code></pre>
<h4 id="parameters-6">Parameters</h4>
<ul>
<li><code>target</code> (string): A hostname, hostname glob (for example, <code>*.example.com</code>), IP address, IP:port, or CIDR range to match.</li>
<li><code>worker</code> (WorkerEntrypoint): A <code>WorkerEntrypoint</code> instance to handle matching requests.</li>
</ul>
<h4 id="return-values-6">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h3 id="interceptalloutboundhttp"><code>interceptAllOutboundHttp</code></h3>
<p><code>interceptAllOutboundHttp</code> routes all outbound HTTP requests from the container through a <code>WorkerEntrypoint</code>, regardless of destination.</p>
<pre><code class="language-js">await this.ctx.container.interceptAllOutboundHttp(worker);&#10;</code></pre>
<h4 id="parameters-7">Parameters</h4>
<ul>
<li><code>worker</code> (WorkerEntrypoint): A <code>WorkerEntrypoint</code> instance to handle all outbound HTTP requests.</li>
</ul>
<h4 id="return-values-7">Return values</h4>
<ul>
<li>A promise that resolves once the intercept rule is installed.</li>
</ul>
<h3 id="interceptoutboundhttps"><code>interceptOutboundHttps</code></h3>
<p><code>interceptOutboundHttps</code> routes outbound HTTPS requests matching a hostname or hostname glob through a <code>WorkerEntrypoint</code>. Works the same way as <code>interceptOutboundHttp</code> but for HTTPS traffic. The container must trust the CA certificate at <code>/etc/cloudflare/certs/cloudflare-containers-ca.crt</code> for HTTPS interception to work.</p>
<p>Supports glob patterns where <code>*</code> matches any sequence of characters.</p>
<pre><code class="language-js">const worker = this.ctx.exports.MyWorker({ props: {} });&#10;&#10;// Match a specific hostname&#10;this.ctx.container.interceptOutboundHttps(&quot;api.example.com&quot;, worker);&#10;&#10;// Match a hostname glob pattern&#10;this.ctx.container.interceptOutboundHttps(&quot;*.example.com&quot;, worker);&#10;&#10;// Intercept all HTTPS traffic&#10;this.ctx.container.interceptOutboundHttps(&quot;*&quot;, worker);&#10;</code></pre>
<h4 id="parameters-8">Parameters</h4>
<ul>
<li><code>target</code> (string): A hostname or hostname glob pattern to match. Use <code>*</code> to intercept all HTTPS traffic.</li>
<li><code>worker</code> (WorkerEntrypoint): A <code>WorkerEntrypoint</code> instance to handle matching requests.</li>
</ul>
<h4 id="return-values-8">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/containers/reference/container-class/">Container class reference</a> — the recommended high-level API built on top of this interface</li>
<li><a href="/containers/">Containers overview</a></li>
<li><a href="/containers/get-started/">Get started with Containers</a></li>
<li><a href="/durable-objects/api/sqlite-storage-api/">SQLite storage API</a> — persist state across container restarts</li>
<li><a href="/durable-objects/">Durable Objects</a> — the underlying platform that powers Containers</li>
</ul>
