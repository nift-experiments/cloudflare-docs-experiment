---
cp9:
  canonical: https://developers.cloudflare.com/containers/reference/container-class/
  description: API reference for the Container interface and utility functions
  full_title: Container Interface · Cloudflare Containers docs
  head_html: <title>Container Interface · Cloudflare Containers docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for the Container interface and utility functions"><link rel="canonical" href="https://developers.cloudflare.com/containers/reference/container-class/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/containers/reference/container-class/index.md"><meta property="og:title" content="Container Interface · Cloudflare Containers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for the Container interface and utility functions"><meta property="og:url" content="https://developers.cloudflare.com/containers/reference/container-class/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Containers"><meta name="algolia_product_filter" content="Containers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Containers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/containers/reference/container-class/#page","headline":"Container Interface \u00b7 Cloudflare Containers docs","description":"API reference for the Container interface and utility functions","url":"https://developers.cloudflare.com/containers/reference/container-class/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /containers/reference/container-class/
  schema: 1
---
<p>The <a href="https://github.com/cloudflare/containers"><code>Container</code> class</a> from <a href="https://www.npmjs.com/package/@cloudflare/containers"><code>@cloudflare/containers</code></a> is the most common way to interact with container instances from a Worker.</p>
<p><strong><code>Container</code> extends <a href="/durable-objects/api/base/"><code>DurableObject</code></a>.</strong> The Durable Object manages routing, persistent state, and lifecycle hooks, while the container process runs your image inside a Linux VM. Because your subclass is a Durable Object, you have access to the full Durable Object API — including <a href="/durable-objects/api/sqlite-storage-api/"><code>this.ctx.storage</code></a> for persistent SQLite-backed storage and <a href="/durable-objects/api/id/"><code>this.ctx.id</code></a> for the unique instance identifier. Use Durable Object storage to persist state that should survive container restarts, such as configuration, user data, or task results.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/containers</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/containers" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/containers</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/containers" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/containers</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/containers" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/containers</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/containers" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Then, define a class that extends <code>Container</code> and set the shared properties on the class:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7070.md")
</div>
<p>The <code>Container</code> class extends <code>DurableObject</code>, so all <a href="/durable-objects/">Durable Object</a> functionality is available — including <a href="/durable-objects/api/sqlite-storage-api/">SQLite storage</a>, <a href="/durable-objects/api/alarms/">alarms</a>, and <a href="/durable-objects/api/base/#rpc-methods">RPC methods</a>. Container disk is ephemeral by default, but Durable Object storage persists across container restarts.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7071.md")
</div>
<h2 id="execute-commands">Execute commands</h2>
<p>Use <code>this.ctx.container.exec()</code> to start another process inside a running Container. Refer to <a href="/containers/guides/execute-commands/">Execute commands</a> for startup, streaming, output, and process-control examples.</p>
<h2 id="properties">Properties</h2>
<p>Configure these as class fields on your subclass. They apply to every instance of the container.</p>
<ul>
<li>
<p><span id="defaultport"></span><strong><code>defaultPort</code></strong> (<code>number</code>, optional) — the
port your container process listens on. <a href="#fetch"><code>fetch()</code></a> and
<a href="#containerfetch"><code>containerFetch()</code></a> forward requests here unless you specify
a different port via <a href="#switchport"><code>switchPort()</code></a> or the <code>port</code> argument to
<a href="#containerfetch"><code>containerFetch()</code></a>. Most subclasses set this.</p>
</li>
<li>
<p><span id="requiredports"></span><strong><code>requiredPorts</code></strong> (<code>number[]</code>, optional) —
ports that must be accepting connections before the container is considered
ready. Used by <a href="#startandwaitforports"><code>startAndWaitForPorts()</code></a> when no
<code>ports</code> argument is passed. Set this when your container runs multiple
services that all need to be healthy before serving traffic.</p>
</li>
<li>
<p><span id="sleepafter"></span><strong><code>sleepAfter</code></strong> (<code>string | number</code>, default:
<code>&quot;10m&quot;</code>) — how long to keep the container alive without activity before
shutting it down. Accepts a number of seconds or a duration string such as
<code>&quot;30s&quot;</code>, <code>&quot;5m&quot;</code>, or <code>&quot;1h&quot;</code>. Activity resets the timer — see
<a href="#renewactivitytimeout"><code>renewActivityTimeout()</code></a> for manual resets.</p>
</li>
<li>
<p><span id="envvars"></span><strong><code>envVars</code></strong> (<code>Record&lt;string, string&gt;</code>, default: <code>{}</code>) — environment variables passed to the container on every start. For per-instance variables, pass <code>envVars</code> through <a href="#startandwaitforports"><code>startAndWaitForPorts()</code></a> instead.</p>
</li>
<li>
<p><span id="entrypoint"></span><strong><code>entrypoint</code></strong> (<code>string[]</code>, optional) —
overrides the image's default entrypoint. Useful when you want to run a
different command without rebuilding the image, such as a dev server or a
one-off task.</p>
</li>
<li>
<p><span id="enableinternet"></span><strong><code>enableInternet</code></strong> (<code>boolean</code>, default:
<code>true</code>) — controls whether the container can make outbound HTTP requests. Set
to <code>false</code> for sandboxed environments where you want to intercept or block all
outbound traffic. For more information, refer to <a href="/containers/guides/outbound-traffic/">Handle outbound
traffic</a>.</p>
</li>
<li>
<p><span id="pingendpoint"></span><strong><code>pingEndpoint</code></strong> (<code>string</code>, default:
<code>&quot;ping&quot;</code>) — the host and path the class uses to health-check the container
during startup. Most users do not need to change this.</p>
</li>
</ul>
<h2 id="lifecycle-hooks">Lifecycle hooks</h2>
<p>Override these methods to run Worker code when the container changes state. Refer to the <a href="/containers/examples/status-hooks/">status hooks example</a> for a full example.</p>
<h3 id="onstart"><code>onStart</code></h3>
<p>Run Worker code after the container has started.</p>
<pre tabindex="0"><code class="language-ts">onStart(): void | Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Returns</strong>: <code>void | Promise&lt;void&gt;</code>. Resolve after any startup logic finishes.</p>
<p>Use this to log startup, seed data, or schedule recurring tasks with <a href="#schedule"><code>schedule()</code></a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7072.md")
</div>
<h3 id="onstop"><code>onStop</code></h3>
<p>Run Worker code after the container process exits.</p>
<pre tabindex="0"><code class="language-ts">onStop(params: StopParams): void | Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>params.exitCode</code> - Container process exit code.</li>
<li><code>params.reason</code> - Why the container stopped: <code>'exit'</code> when the process exited on its own, or <code>'runtime_signal'</code> when the runtime signalled it.</li>
</ul>
<p><strong>Returns</strong>: <code>void | Promise&lt;void&gt;</code>. Resolve after your shutdown logic finishes.</p>
<p>Use this to log, alert, or restart the container.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7073.md")
</div>
<h3 id="onerror"><code>onError</code></h3>
<p>Handle startup and port-checking errors.</p>
<pre tabindex="0"><code class="language-ts">onError(error: unknown): any&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>error</code> - The error thrown during startup or port checks.</li>
</ul>
<p><strong>Returns</strong>: <code>any</code>. The default implementation logs the error and re-throws it.</p>
<p>Override this to suppress errors, notify an external service, or attempt a restart.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7074.md")
</div>
<h3 id="onactivityexpired"><code>onActivityExpired</code></h3>
<p>Run Worker code when the <a href="#sleepafter"><code>sleepAfter</code></a> timer expires.</p>
<pre tabindex="0"><code class="language-ts">onActivityExpired(): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Returns</strong>: <code>Promise&lt;void&gt;</code>. Resolve after your idle-time logic finishes.</p>
<p>Called when the <a href="#sleepafter"><code>sleepAfter</code></a> timeout expires with no incoming requests. The default implementation calls <a href="#stop"><code>stop()</code></a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7069.md")
</aside>
<p>If you override this method without stopping the container, the timer renews and the hook fires again on the next expiry.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7075.md")
</div>
<h2 id="request-methods">Request methods</h2>
<h3 id="fetch"><code>fetch</code></h3>
<p>Handle incoming HTTP or WebSocket requests.</p>
<pre tabindex="0"><code class="language-ts">fetch(request: Request): Promise&lt;Response&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>request</code> - The incoming request to proxy to the container.</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;Response&gt;</code> from the container or from your custom routing logic.</p>
<p>By default, <code>fetch</code> forwards the request to the container process at <a href="#defaultport"><code>defaultPort</code></a>. The container is started automatically if it is not already running.</p>
<p>Override <code>fetch</code> when you need routing logic, authentication, or other middleware before forwarding to the container. Inside the override, call <a href="#containerfetch"><code>this.containerFetch()</code></a> rather than <code>this.fetch()</code> to avoid infinite recursion:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7076.md")
</div>
<p><code>fetch</code> is the only method that supports WebSocket proxying. Refer to the <a href="/containers/examples/websocket/">WebSocket example</a> for a full example.</p>
<h3 id="containerfetch"><code>containerFetch</code></h3>
<p>Send an HTTP request directly to the container process. Generally, users should prefer
to use <a href="#fetch"><code>fetch</code></a> unless it has been overridden.</p>
<pre tabindex="0"><code class="language-ts">containerFetch(request: Request, port?: number): Promise&lt;Response&gt;&#10;containerFetch(url: string | URL, init?: RequestInit, port?: number): Promise&lt;Response&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>request</code> - Existing <code>Request</code> object to forward.</li>
<li><code>url</code> - URL to request when you are constructing a new request.</li>
<li><code>init</code> - Standard <code>RequestInit</code> options for the URL-based overload.</li>
<li><code>port</code> - Optional target port. If omitted, the class uses <a href="#defaultport"><code>defaultPort</code></a>.</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;Response&gt;</code> from the container.</p>
<p>This is what the default <a href="#fetch"><code>fetch()</code></a> implementation calls internally, and it is what you should call from within an overridden <a href="#fetch"><code>fetch()</code></a> method to avoid infinite recursion. It also accepts a standard fetch-style signature with a URL string and <code>RequestInit</code>, which is useful when you are constructing a new request rather than forwarding an existing one.</p>
<p>Does not support WebSockets. Use <a href="#fetch"><code>fetch()</code></a> with <a href="#switchport"><code>switchPort()</code></a> for those.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7077.md")
</div>
<h2 id="start-and-stop">Start and stop</h2>
<p>In most cases you do not need to call these methods directly. <a href="#fetch"><code>fetch()</code></a> and <a href="#containerfetch"><code>containerFetch()</code></a> start the container automatically. Call these explicitly when you need to pre-warm a container, run a task on a schedule, or control the lifecycle from within a lifecycle hook.</p>
<h3 id="startandwaitforports"><code>startAndWaitForPorts</code></h3>
<p>Start the container and wait until the target ports are accepting connections.</p>
<pre tabindex="0"><code class="language-ts">startAndWaitForPorts(args?: StartAndWaitForPortsOptions): Promise&lt;void&gt;&#10;startAndWaitForPorts(&#10;  ports?: number | number[],&#10;  cancellationOptions?: CancellationOptions,&#10;  startOptions?: ContainerStartConfigOptions,&#10;): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>args.ports</code> - Port or ports to wait for. Port resolution order is explicit <code>ports</code>, then <a href="#requiredports"><code>requiredPorts</code></a>, then <a href="#defaultport"><code>defaultPort</code></a>.</li>
<li><code>args.startOptions</code> - Per-instance startup overrides.</li>
<li><code>args.startOptions.envVars</code> - Per-instance environment variables.</li>
<li><code>args.startOptions.entrypoint</code> - Entrypoint override for this start only.</li>
<li><code>args.startOptions.enableInternet</code> - Whether outbound internet access is allowed for this start.</li>
<li><code>args.cancellationOptions.abort</code> - Abort signal to cancel startup.</li>
<li><code>args.cancellationOptions.instanceGetTimeoutMS</code> - Maximum time to get a container instance and issue the start command. Default: <code>8000</code>.</li>
<li><code>args.cancellationOptions.portReadyTimeoutMS</code> - Maximum time to wait for all ports to become ready. Default: <code>20000</code>.</li>
<li><code>args.cancellationOptions.waitInterval</code> - Polling interval in milliseconds. Default: <code>300</code>.</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;void&gt;</code>. Resolves after the target ports are ready and <a href="#onstart"><code>onStart()</code></a> has run.</p>
<p>This is the safest way to explicitly start a container when you need to be certain it is ready before sending traffic.</p>
<p>This method also supports positional <code>ports</code>, <code>cancellationOptions</code>, and <code>startOptions</code> arguments, but the object form is easier to read.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7078.md")
</div>
<p>Refer to the <a href="/containers/examples/env-vars-and-secrets/">env vars and secrets example</a> for a full example.</p>
<h3 id="start"><code>start</code></h3>
<p>Start the container without waiting for all ports to become ready.</p>
<pre tabindex="0"><code class="language-ts">start(startOptions?: ContainerStartConfigOptions, waitOptions?: WaitOptions): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>startOptions</code> - Per-instance startup overrides.</li>
<li><code>startOptions.envVars</code> - Per-instance environment variables.</li>
<li><code>startOptions.entrypoint</code> - Entrypoint override for this start only.</li>
<li><code>startOptions.enableInternet</code> - Whether outbound internet access is allowed for this start.</li>
<li><code>waitOptions.portToCheck</code> - Port to probe while starting. If omitted, the class uses <a href="#defaultport"><code>defaultPort</code></a>, the first <a href="#requiredports"><code>requiredPorts</code></a> entry, or a fallback port.</li>
<li><code>waitOptions.signal</code> - Abort signal to cancel startup.</li>
<li><code>waitOptions.retries</code> - Maximum number of start attempts before the method throws.</li>
<li><code>waitOptions.waitInterval</code> - Polling interval in milliseconds between retries.</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;void&gt;</code>. Resolves after the start attempt succeeds and <a href="#onstart"><code>onStart()</code></a> has run.</p>
<p>Use this when the container does not expose ports, such as a batch job or a cron task, or when you want to manage readiness yourself with <a href="#waitforport"><code>waitForPort()</code></a>. If you need to wait for all ports to be ready, use <a href="#startandwaitforports"><code>startAndWaitForPorts()</code></a> instead.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7079.md")
</div>
<p>Refer to the <a href="/containers/examples/cron/">cron example</a> for a full example.</p>
<h3 id="waitforport"><code>waitForPort</code></h3>
<p>Poll a single port until it accepts connections.</p>
<pre tabindex="0"><code class="language-ts">waitForPort(waitOptions: WaitOptions): Promise&lt;number&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>waitOptions.portToCheck</code> - Port number to check.</li>
<li><code>waitOptions.signal</code> - Abort signal to cancel waiting.</li>
<li><code>waitOptions.retries</code> - Maximum number of retries before the method throws.</li>
<li><code>waitOptions.waitInterval</code> - Polling interval in milliseconds.</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;number&gt;</code>. The numeric return value is mainly useful when you are coordinating custom readiness logic across multiple waits.</p>
<p>Throws if the port does not become available within the retry limit. Use this after <a href="#start"><code>start()</code></a> when you need to check multiple ports independently or in a specific sequence.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7080.md")
</div>
<h3 id="stop"><code>stop</code></h3>
<p>Send a signal to the container process.</p>
<pre tabindex="0"><code class="language-ts">stop(signal?: &#x27;SIGTERM&#x27; | &#x27;SIGINT&#x27; | &#x27;SIGKILL&#x27; | number): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>signal</code> - Signal to send. Defaults to <code>'SIGTERM'</code>.</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;void&gt;</code>. Resolves after the signal is sent and pending stop handling has completed.</p>
<p>Defaults to <code>SIGTERM</code>, which gives the process a chance to shut down gracefully. Triggers <a href="#onstop"><code>onStop()</code></a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7081.md")
</div>
<h3 id="destroy"><code>destroy</code></h3>
<p>Immediately kill the container process.</p>
<pre tabindex="0"><code class="language-ts">destroy(): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Returns</strong>: <code>Promise&lt;void&gt;</code>. Resolves after the runtime has destroyed the container.</p>
<p>This sends <code>SIGKILL</code>. Use it when you need the container gone immediately and cannot wait for a graceful shutdown. Triggers <a href="#onstop"><code>onStop()</code></a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7082.md")
</div>
<h2 id="state-and-monitoring">State and monitoring</h2>
<h3 id="getstate"><code>getState</code></h3>
<p>Read the current container state.</p>
<pre tabindex="0"><code class="language-ts">getState(): Promise&lt;State&gt;&#10;</code></pre>
<p><strong>Returns</strong>: <code>Promise&lt;State&gt;</code> with:</p>
<ul>
<li><code>status</code> - One of <code>'running'</code>, <code>'healthy'</code>, <code>'stopping'</code>, <code>'stopped'</code>, or <code>'stopped_with_code'</code>.</li>
<li><code>lastChange</code> - Unix timestamp in milliseconds for the last state change.</li>
<li><code>exitCode</code> - Optional exit code when <code>status</code> is <code>'stopped_with_code'</code>.</li>
</ul>
<p><code>running</code> means the container is starting and has not yet passed its health check. <code>healthy</code> means it is up and accepting requests.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7083.md")
</div>
<h3 id="renewactivitytimeout"><code>renewActivityTimeout</code></h3>
<p>Reset the <a href="#sleepafter"><code>sleepAfter</code></a> timer.</p>
<pre tabindex="0"><code class="language-ts">renewActivityTimeout(): void&#10;</code></pre>
<p><strong>Returns</strong>: <code>void</code>.</p>
<p>Incoming requests reset the timer automatically. Call this manually from background work, such as a scheduled task or a long-running operation, that should count as activity and prevent the container from sleeping.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7084.md")
</div>
<h2 id="scheduling">Scheduling</h2>
<h3 id="schedule"><code>schedule</code></h3>
<p>Schedule a method on the class to run later.</p>
<pre tabindex="0"><code class="language-ts">schedule&lt;T&gt;(when: Date | number, callback: string, payload?: T): Promise&lt;Schedule&lt;T&gt;&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>when</code> - Either a <code>Date</code> for a specific time or a number of seconds to delay.</li>
<li><code>callback</code> - Name of the class method to call.</li>
<li><code>payload</code> - Optional data passed to the callback method.</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;Schedule&lt;T&gt;&gt;</code> with:</p>
<ul>
<li><code>taskId</code> - Unique schedule ID.</li>
<li><code>callback</code> - Method name that will be called.</li>
<li><code>payload</code> - Payload that will be passed to the callback.</li>
<li><code>type</code> - <code>'scheduled'</code> for an absolute time or <code>'delayed'</code> for a relative delay.</li>
<li><code>time</code> - Unix timestamp in seconds when the task will run.</li>
<li><code>delayInSeconds</code> - Delay in seconds when <code>type</code> is <code>'delayed'</code>.</li>
</ul>
<p>Do not override <a href="https://developers.cloudflare.com/durable-objects/api/alarms/"><code>alarm()</code></a> directly. The <code>Container</code> class uses the alarm handler to manage the container lifecycle, so use <a href="#schedule"><code>schedule()</code></a> instead.</p>
<p>The following example schedules a recurring health report starting at container startup:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7085.md")
</div>
<h2 id="outbound-interception">Outbound interception</h2>
<p>Outbound interception lets you intercept, mock, or block HTTP requests that the container makes to external hosts. This is useful for sandboxing, testing, or proxying outbound traffic through Worker code.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7086.md")
</div>
<p>For more information, refer to <a href="/containers/guides/outbound-traffic/">Handle outbound traffic</a>.</p>
<h2 id="utility-functions">Utility functions</h2>
<p>These functions are exported alongside the <code>Container</code> class from <code>@cloudflare/containers</code>.</p>
<h3 id="getcontainer"><code>getContainer</code></h3>
<p>Get a stub for a named container instance.</p>
<pre tabindex="0"><code class="language-ts">getContainer&lt;T&gt;(binding: DurableObjectNamespace&lt;T&gt;, name?: string): DurableObjectStub&lt;T&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>binding</code> - Durable Object namespace binding for your container class.</li>
<li><code>name</code> - Stable instance name. Defaults to <code>cf-singleton-container</code>.</li>
</ul>
<p><strong>Returns</strong>: <code>DurableObjectStub&lt;T&gt;</code> for the named container instance.</p>
<p>Use this when you want one container per logical entity, such as a user session, a document, or a game room, identified by a stable name.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7087.md")
</div>
<h3 id="getrandom"><code>getRandom</code></h3>
<p>Get a stub for a randomly selected container instance.</p>
<pre tabindex="0"><code class="language-ts">getRandom&lt;T&gt;(binding: DurableObjectNamespace&lt;T&gt;, instances?: number): Promise&lt;DurableObjectStub&lt;T&gt;&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>binding</code> - Durable Object namespace binding for your container class.</li>
<li><code>instances</code> - Total number of instances to choose from. Defaults to <code>3</code>.</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;DurableObjectStub&lt;T&gt;&gt;</code> for the randomly selected instance.</p>
<p>Use this for stateless workloads where any container can handle any request and you want to spread load across multiple instances.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7088.md")
</div>
<p>Refer to the <a href="/containers/examples/stateless/">stateless instances example</a> for a full example.</p>
<h3 id="switchport"><code>switchPort</code></h3>
<p>Target a different container port while still using <code>fetch()</code>.</p>
<pre tabindex="0"><code class="language-ts">switchPort(request: Request, port: number): Request&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>request</code> - Request to copy.</li>
<li><code>port</code> - Port to encode into the request headers.</li>
</ul>
<p><strong>Returns</strong>: <code>Request</code> copy with the target port set.</p>
<p>Use this when you need to target a specific port and also need WebSocket support. If you do not need WebSockets, pass the port directly to <a href="#containerfetch"><code>containerFetch()</code></a> instead.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7089.md")
</div>
