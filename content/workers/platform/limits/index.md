<h2 id="account-plan-limits">Account plan limits</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#daily-requests">Requests</a></td>
<td>100,000/day</td>
<td>No limit</td>
</tr>
<tr>
<td><a href="#cpu-time">CPU time</a></td>
<td>10 ms</td>
<td>5 min</td>
</tr>
<tr>
<td><a href="#memory">Memory</a></td>
<td>128 MB</td>
<td>128 MB</td>
</tr>
<tr>
<td><a href="#subrequests">Subrequests</a></td>
<td>50/request</td>
<td>10,000/request</td>
</tr>
<tr>
<td><a href="#simultaneous-open-connections">Simultaneous outgoing<br/>connections/request</a></td>
<td>6</td>
<td>6</td>
</tr>
<tr>
<td><a href="#environment-variables">Environment variables</a></td>
<td>64/Worker</td>
<td>128/Worker</td>
</tr>
<tr>
<td><a href="#environment-variables">Environment variable<br/>size</a></td>
<td>5 KB</td>
<td>5 KB</td>
</tr>
<tr>
<td><a href="#worker-size">Worker size</a></td>
<td>64 MiB</td>
<td>64 MiB</td>
</tr>
<tr>
<td><a href="#worker-startup-time">Worker startup time</a></td>
<td>1 second</td>
<td>1 second</td>
</tr>
<tr>
<td><a href="#number-of-workers">Number of Workers</a></td>
<td>100</td>
<td>500<sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td>Number of <a href="/workers/configuration/cron-triggers/">Cron Triggers</a><br/>per account</td>
<td>5</td>
<td>250</td>
</tr>
<tr>
<td>Number of <a href="#static-assets">Static Asset</a> files per Worker version</td>
<td>20,000</td>
<td>100,000</td>
</tr>
<tr>
<td>Individual <a href="#static-assets">Static Asset</a> file size</td>
<td>25 MiB</td>
<td>25 MiB</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/16214.md")
</aside>
<hr />
<h2 id="request-and-response-limits">Request and response limits</h2>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>URL size</td>
<td>16 KB</td>
</tr>
<tr>
<td>Request header size</td>
<td>128 KB (total)</td>
</tr>
<tr>
<td>Response header size</td>
<td>128 KB (total)</td>
</tr>
<tr>
<td>Response body size</td>
<td>No enforced limit</td>
</tr>
</tbody>
</table>
<p>Request body size limits depend on your Cloudflare account plan, not your Workers plan. Requests exceeding these limits return a <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-413/#cloudflare-specific-information"><code>413 Request entity too large</code></a> error.</p>
<table>
<thead>
<tr>
<th>Cloudflare Plan</th>
<th>Maximum request body size</th>
</tr>
</thead>
<tbody>
<tr>
<td>Free</td>
<td>100 MB</td>
</tr>
<tr>
<td>Pro</td>
<td>100 MB</td>
</tr>
<tr>
<td>Business</td>
<td>200 MB</td>
</tr>
<tr>
<td>Enterprise</td>
<td>Up to 5 GB (self-serve)</td>
</tr>
</tbody>
</table>
<p>Enterprise customers can adjust the maximum request body size up to 5 GB themselves from the zone's <strong>Network</strong> page (<strong>Maximum Upload Size</strong>). For limits above 5 GB, contact your account team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</p>
<p>Cloudflare does not enforce response body size limits. <a href="/cache/concepts/default-cache-behavior/">CDN cache limits</a> apply: 512 MB for Free, Pro, and Business plans, and 5 GB for Enterprise.</p>
<hr />
<h2 id="cpu-time">CPU time</h2>
<p>CPU time measures how long the CPU spends executing your Worker code. Waiting on network requests (such as <code>fetch()</code> calls, KV reads, or database queries) does <strong>not</strong> count toward CPU time.</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>CPU time per HTTP request</td>
<td>10 ms</td>
<td>5 min (default: 30 seconds)</td>
</tr>
<tr>
<td>CPU time per Cron Trigger</td>
<td>10 ms</td>
<td>30 seconds (&lt; 1 hour interval) <br/> 15 min (&gt;= 1 hour interval)</td>
</tr>
</tbody>
</table>
<p>Most Workers consume very little CPU time. The average Worker uses approximately 2.2 ms per request. Heavier workloads that handle authentication, server-side rendering, or parse large payloads typically use 10-20 ms.</p>
<p>Each <a href="/workers/reference/how-workers-works/#isolates">isolate</a> has some built-in flexibility to allow for cases where your Worker infrequently runs over the configured limit. If your Worker starts hitting the limit consistently, its execution will be terminated according to the limit configured.</p>
<h4 id="error-exceeded-cpu-time-limit-exceeded-cpu">Error: exceeded CPU time limit </h4>
<p>When a Worker exceeds its CPU time limit, Cloudflare returns <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1102/#error-1102-worker-exceeded-resource-limits">Error 1102</a> to the client with the message <code>Worker exceeded resource limits</code>. In the dashboard, this appears as <code>Exceeded CPU Time Limits</code> under <strong>Metrics</strong> &gt; <strong>Errors</strong> &gt; <strong>Invocation Statuses</strong>. In analytics and Logpush, the invocation outcome is <code>exceededCpu</code>.</p>
<p>To resolve a CPU time limit error:</p>
<ol>
<li><strong>Increase the CPU time limit</strong> — On the Workers Paid plan, you can raise the limit from the default 30 seconds up to 5 minutes (300,000 ms). Set this in your Wrangler configuration or in the dashboard.</li>
<li><strong>Optimize your code</strong> — Use <a href="/workers/observability/dev-tools/cpu-usage/">CPU profiling with DevTools</a> to identify CPU-intensive sections of your code.</li>
<li><strong>Offload work</strong> — Move expensive computation to <a href="/durable-objects/">Durable Objects</a> or process data in smaller chunks across multiple requests.</li>
</ol>
<h4 id="increasing-the-cpu-time-limit">Increasing the CPU time limit</h4>
<p>On the Workers Paid plan, you can increase the maximum CPU time from the default 30 seconds to 5 minutes (300,000 ms).</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16215.md")
</div>
<p>You can also change this in the dashboard: go to <strong>Workers &amp; Pages</strong> &gt; select your Worker &gt; <strong>Settings</strong> &gt; adjust the CPU time limit.</p>
<h4 id="monitoring-cpu-usage">Monitoring CPU usage</h4>
<ul>
<li><strong>Workers Logs</strong> — CPU time and wall time appear in the <a href="/workers/observability/logs/workers-logs/#invocation-logs">invocation log</a>.</li>
<li><strong>Tail Workers / Logpush</strong> — CPU time and wall time appear at the top level of the <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events/">Workers Trace Events object</a>.</li>
<li><strong>DevTools</strong> — Use <a href="/workers/observability/dev-tools/cpu-usage/">CPU profiling with DevTools</a> locally to identify CPU-intensive sections of your code.</li>
</ul>
<hr />
<h2 id="memory">Memory</h2>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Memory per isolate</td>
<td>128 MB</td>
</tr>
</tbody>
</table>
<p>Each <a href="/workers/reference/how-workers-works/#isolates">isolate</a> can consume up to 128 MB of memory, including the JavaScript heap and <a href="/workers/runtime-apis/webassembly/">WebAssembly</a> allocations. This limit is per-isolate, not per-invocation. A single isolate can handle many concurrent requests.</p>
<p>When an isolate exceeds 128 MB, the Workers runtime lets in-flight requests complete and creates a new isolate for subsequent requests. During extremely high load, the runtime may cancel some incoming requests to maintain stability.</p>
<h4 id="error-exceeded-memory-limit-exceeded-memory">Error: exceeded memory limit </h4>
<p>When a Worker exceeds its memory limit, Cloudflare returns <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1102/#error-1102-worker-exceeded-resource-limits">Error 1102</a> to the client with the message <code>Worker exceeded resource limits</code>. In the dashboard, this appears as <code>Exceeded Memory</code> under <strong>Metrics</strong> &gt; <strong>Errors</strong> &gt; <strong>Invocation Statuses</strong>. In analytics and Logpush, the invocation outcome is <code>exceededMemory</code>.</p>
<p>You may also see the runtime error <code>Memory limit would be exceeded before EOF</code> when attempting to buffer a response body that exceeds the limit.</p>
<p>To resolve a memory limit error:</p>
<ol>
<li><strong>Stream request and response bodies</strong> — Use <a href="/workers/runtime-apis/streams/transformstream/"><code>TransformStream</code></a> or <a href="/workers/runtime-apis/nodejs/streams/"><code>node:stream</code></a> instead of buffering entire payloads in memory.</li>
<li><strong>Avoid large in-memory objects</strong> — Store large data in <a href="/kv/">KV</a>, <a href="/r2/">R2</a>, or <a href="/d1/">D1</a> instead of holding it in Worker memory.</li>
<li><strong>Update Zod</strong> — If your Worker uses Zod, use <a href="https://github.com/colinhacks/zod/releases/tag/v4.5.0">version 4.5.0 or later</a>. Earlier versions use substantially more memory per schema.</li>
<li><strong>Profile memory usage</strong> — Use <a href="/workers/observability/dev-tools/memory-usage/">memory profiling with DevTools</a> locally to identify leaks and high-memory allocations.</li>
</ol>
<p>To view memory errors in the dashboard:</p>
<ol>
<li>Go to <strong>Workers &amp; Pages</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the Worker you want to investigate.</li>
<li>Under <strong>Metrics</strong>, select <strong>Errors</strong> &gt; <strong>Invocation Statuses</strong> and examine <strong>Exceeded Memory</strong>.</li>
</ol>
<hr />
<h2 id="duration">Duration</h2>
<p>Duration measures wall-clock time from start to end of a Worker invocation.</p>
<table>
<thead>
<tr>
<th>Trigger type</th>
<th>Duration limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>HTTP request</td>
<td>No limit</td>
</tr>
<tr>
<td><a href="/workers/configuration/cron-triggers/">Cron Trigger</a></td>
<td>15 min</td>
</tr>
<tr>
<td><a href="/durable-objects/api/alarms/">Durable Object Alarm</a></td>
<td>15 min</td>
</tr>
<tr>
<td><a href="/queues/configuration/javascript-apis/#consumer">Queue Consumer</a></td>
<td>15 min</td>
</tr>
</tbody>
</table>
<p>There is no hard limit on duration for HTTP-triggered Workers. As long as the client remains connected, the Worker can continue processing, making subrequests, and streaming a response body. When the client disconnects or the response is complete, tasks associated with that request may be canceled. Use <a href="/workers/runtime-apis/context/#waituntil"><code>ctx.waitUntil()</code></a> to perform work after returning a response. <code>waitUntil()</code> can extend execution for up to 30 seconds after the response is sent or the client disconnects.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16213.md")
</aside>
<hr />
<h2 id="daily-requests">Daily requests</h2>
<p>Workers scale automatically across the Cloudflare global network. There is no general limit on requests per second.</p>
<p>Accounts on the Workers Free plan have a daily request limit of 100,000 requests, resetting at midnight UTC. When a Worker exceeds this limit, Cloudflare returns <strong>Error 1027</strong>.</p>
<table>
<thead>
<tr>
<th>Route mode</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Fail open</td>
<td>Bypasses the Worker. Requests behave as if no Worker is configured.</td>
</tr>
<tr>
<td>Fail closed</td>
<td>Returns a Cloudflare <code>1027</code> error page. Use this for security-critical Workers.</td>
</tr>
</tbody>
</table>
<p>You can configure the fail mode by toggling the corresponding <a href="/workers/configuration/routing/routes/">route</a>.</p>
<hr />
<h2 id="subrequests">Subrequests</h2>
<p>A subrequest is any request a Worker makes using the <a href="/workers/runtime-apis/fetch/">Fetch API</a> or to Cloudflare services like <a href="/r2/">R2</a>, <a href="/kv/">KV</a>, or <a href="/d1/">D1</a>.</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Subrequests per invocation</td>
<td>50</td>
<td>10,000 (up to 10M)</td>
</tr>
<tr>
<td>Subrequests to internal services</td>
<td>1,000</td>
<td>Matches configured limit (default 10,000)</td>
</tr>
</tbody>
</table>
<p>Each subrequest in a redirect chain counts against this limit. The total number of subrequests may exceed the number of <code>fetch()</code> calls in your code. You can change the subrequest limit per Worker using the <a href="/workers/wrangler/configuration/#limits"><code>limits</code> configuration</a> in your Wrangler configuration file.</p>
<p>There is no set time limit on individual subrequests. As long as the client remains connected, the Worker can continue making subrequests. When the client disconnects or the response is complete, outstanding work may be canceled unless it is passed to <a href="/workers/runtime-apis/context/#waituntil"><code>ctx.waitUntil()</code></a>, which can extend execution for up to 30 seconds.</p>
<h3 id="worker-to-worker-subrequests">Worker-to-Worker subrequests</h3>
<p>Use <a href="/workers/runtime-apis/bindings/service-bindings/">Service Bindings</a> to send requests from one Worker to another on your account without going over the Internet.</p>
<p>Using global <a href="/workers/runtime-apis/fetch/"><code>fetch()</code></a> to call another Worker on the same <a href="/fundamentals/concepts/accounts-and-zones/#zones">zone</a> without service bindings fails. Workers accept requests sent to a <a href="/workers/configuration/routing/custom-domains/#worker-to-worker-communication">Custom Domain</a>.</p>
<hr />
<h2 id="simultaneous-open-connections">Simultaneous open connections</h2>
<p>Each Worker invocation can have up to six connections simultaneously waiting for response headers. The following API calls count toward this limit while the initial connection is being established and the server has not yet responded:</p>
<ul>
<li><code>fetch()</code> method of the <a href="/workers/runtime-apis/fetch/">Fetch API</a></li>
<li><code>get()</code>, <code>put()</code>, <code>list()</code>, and <code>delete()</code> methods of <a href="/kv/api/">Workers KV namespace objects</a></li>
<li><code>put()</code>, <code>match()</code>, and <code>delete()</code> methods of <a href="/workers/runtime-apis/cache/">Cache objects</a></li>
<li><code>list()</code>, <code>get()</code>, <code>put()</code>, <code>delete()</code>, and <code>head()</code> methods of <a href="/r2/">R2</a></li>
<li><code>send()</code> and <code>sendBatch()</code> methods of <a href="/queues/">Queues</a></li>
<li>Opening a TCP socket using the <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code></a> API</li>
</ul>
<p>Outbound WebSocket connections also count toward this limit.</p>
<p>Once response headers arrive for a connection, it no longer counts toward the six-connection limit. This means a Worker can have many connections open simultaneously, as long as no more than six are in the initial &quot;waiting for headers&quot; phase at the same time. If a seventh connection is attempted while six are already waiting for headers, it is queued until one of the existing connections receives its response headers.</p>
<p>If you use <code>fetch()</code> but do not need the response body, calling <code>response.body.cancel()</code> is still good practice to free memory:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16216.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16212.md")
</aside>
<hr />
<h2 id="environment-variables">Environment variables</h2>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Variables per Worker (secrets + text)</td>
<td>64</td>
<td>128</td>
</tr>
<tr>
<td>Variable size</td>
<td>5 KB</td>
<td>5 KB</td>
</tr>
<tr>
<td>Variables per account</td>
<td>No limit</td>
<td>No limit</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="worker-size">Worker size</h2>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Worker size (uncompressed)</td>
<td>64 MiB</td>
<td>64 MiB</td>
</tr>
</tbody>
</table>
<p>There is no compressed size limit. Only the uncompressed bundle size counts.</p>
<p>Larger Worker bundles can impact startup time. To check your Worker bundle size:</p>
<pre><code class="language-sh">wrangler deploy --outdir bundled/ --dry-run&#10;</code></pre>
<pre><code class="language-sh">Total Upload: 259.61 KiB / gzip: 47.23 KiB&#10;</code></pre>
<p>The <code>Total Upload</code> value is your uncompressed bundle size. The <code>gzip</code> value is shown for reference but is not a limit.</p>
<p>To reduce Worker size:</p>
<ul>
<li>Remove unnecessary dependencies and packages.</li>
<li>Store configuration files, static assets, and binary data in <a href="/kv/">KV</a>, <a href="/r2/">R2</a>, <a href="/d1/">D1</a>, or <a href="/workers/static-assets/">Workers Static Assets</a> instead of bundling them.</li>
<li>Split functionality across multiple Workers using <a href="/workers/runtime-apis/bindings/service-bindings/">Service bindings</a>.</li>
</ul>
<hr />
<h2 id="worker-startup-time">Worker startup time</h2>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Startup time</td>
<td>1 second</td>
</tr>
</tbody>
</table>
<p>A Worker must parse and execute its global scope (top-level code outside of handlers) within 1 second. Larger bundles and expensive initialization code in global scope increase startup time.</p>
<p>When the platform rejects a deployment because the Worker exceeds the startup time limit, the validation returns the error <code>Script startup exceeded CPU time limit</code> (error code <code>10021</code>). Wrangler automatically generates a CPU profile that you can import into Chrome DevTools or open in VS Code. Refer to <a href="/workers/wrangler/commands/workers/#startup"><code>wrangler check startup</code></a> for more details.</p>
<p>To measure startup time, run <code>npx wrangler@latest deploy</code> or <code>npx wrangler@latest versions upload</code>. Wrangler reports <code>startup_time_ms</code> in the output.</p>
<p>To reduce startup time, avoid expensive work in global scope. Move initialization logic into your handler or to build time. For example, generating or consuming a large schema at the top level is a common cause of exceeding this limit.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit-1">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/16211.md")
</aside>
<hr />
<h2 id="number-of-workers">Number of Workers</h2>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers per account</td>
<td>100</td>
<td>500<sup><a href="#footnote-1">1</a></sup></td>
</tr>
</tbody>
</table>
<hr />
<h2 id="routes-and-domains">Routes and domains</h2>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/configuration/routing/routes/">Routes</a> per zone</td>
<td>1,000</td>
</tr>
<tr>
<td>Routes per zone (<a href="#routes-remote-dev"><code>wrangler dev --remote</code></a>)</td>
<td>50</td>
</tr>
<tr>
<td><a href="/workers/configuration/routing/custom-domains/">Custom domains</a> per zone</td>
<td>100</td>
</tr>
<tr>
<td>Routed zones per Worker</td>
<td>1,000</td>
</tr>
</tbody>
</table>
<h3 id="routes-with-wrangler-dev-remote-routes-remote-dev">Routes with <code>wrangler dev --remote</code> </h3>
<p>When you run a <a href="/workers/local-development/#remote-bindings">remote development</a> session using the <code>--remote</code> flag, Cloudflare enforces a limit of 50 routes per zone. The Quick Editor in the Cloudflare dashboard also uses <code>wrangler dev --remote</code>, so the same limit applies.</p>
<p>If your zone has more than 50 routes, you cannot run a remote session until you remove routes to get under the limit.</p>
<p>If you require more than 1,000 routes or 1,000 routed zones per Worker, consider using <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a>. If you require more than 100 custom domains per zone, consider using a wildcard <a href="/workers/configuration/routing/routes/">route</a>.</p>
<hr />
<h2 id="cache-api-limits">Cache API limits</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum object size</td>
<td>512 MB</td>
<td>512 MB</td>
</tr>
<tr>
<td>Calls per request</td>
<td>50</td>
<td>1,000</td>
</tr>
</tbody>
</table>
<p>Calls per request is the number of <code>put()</code>, <code>match()</code>, or <code>delete()</code> Cache API calls per request. This shares the same quota as subrequests (<code>fetch()</code>).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16210.md")
</aside>
<hr />
<h2 id="log-size">Log size</h2>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Log data per request</td>
<td>256 KB</td>
</tr>
</tbody>
</table>
<p>This limit covers all data emitted via <code>console.log()</code> statements, exceptions, request metadata, and headers for a single request. After exceeding this limit, the system does not record additional context for that request in logs, tail logs, or <a href="/workers/observability/logs/tail-workers/">Tail Workers</a>.</p>
<p>Refer to the <a href="/workers/observability/logs/logpush/#limits">Workers Trace Event Logpush documentation</a> for limits on fields sent to Logpush destinations.</p>
<hr />
<h2 id="image-resizing-with-workers">Image Resizing with Workers</h2>
<p>Refer to the <a href="/images/optimization/transformations/overview/">Image Resizing documentation</a> for limits that apply when using Image Resizing with Workers.</p>
<hr />
<h2 id="static-assets">Static Assets</h2>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Files per Worker version</td>
<td>20,000</td>
<td>100,000</td>
</tr>
<tr>
<td>Individual file size</td>
<td>25 MiB</td>
<td>25 MiB</td>
</tr>
<tr>
<td><code>_headers</code> rules</td>
<td>100</td>
<td>100</td>
</tr>
<tr>
<td><code>_headers</code> characters per line</td>
<td>2,000</td>
<td>2,000</td>
</tr>
<tr>
<td><code>_redirects</code> static redirects</td>
<td>2,000</td>
<td>2,000</td>
</tr>
<tr>
<td><code>_redirects</code> dynamic redirects</td>
<td>100</td>
<td>100</td>
</tr>
<tr>
<td><code>_redirects</code> total</td>
<td>2,100</td>
<td>2,100</td>
</tr>
<tr>
<td><code>_redirects</code> characters per rule</td>
<td>1,000</td>
<td>1,000</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16209.md")
</aside>
<hr />
<h2 id="unbound-and-bundled-plan-limits">Unbound and Bundled plan limits</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16208.md")
</aside>
<p>If your Worker is on an Unbound plan, limits match the Workers Paid plan.</p>
<p>If your Worker is on a Bundled plan, limits match the Workers Paid plan with these exceptions:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Bundled plan limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Subrequests</td>
<td>50/request</td>
</tr>
<tr>
<td>CPU time (HTTP requests)</td>
<td>50 ms</td>
</tr>
<tr>
<td>CPU time (Cron Triggers)</td>
<td>50 ms</td>
</tr>
<tr>
<td>Cache API calls/request</td>
<td>50</td>
</tr>
</tbody>
</table>
<p>Bundled plan Workers have no duration limits for <a href="/workers/configuration/cron-triggers/">Cron Triggers</a>, <a href="/durable-objects/api/alarms/">Durable Object Alarms</a>, or <a href="/queues/configuration/javascript-apis/#consumer">Queue Consumers</a>.</p>
<hr />
<h2 id="wall-time-limits-by-invocation-type">Wall time limits by invocation type</h2>
<p>Wall time (also called wall-clock time) is the total elapsed time from the start to end of an invocation, including time spent waiting on network requests, I/O, and other asynchronous operations. This is distinct from <a href="/workers/platform/limits/#cpu-time">CPU time</a>, which only measures time the CPU spends actively executing your code.</p>
<p>The following table summarizes the wall time limits for different types of Worker invocations across the developer platform:</p>
<table>
<thead>
<tr>
<th>Invocation type</th>
<th>Wall time limit</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td>Incoming HTTP request</td>
<td>Unlimited</td>
<td>No hard limit while the client remains connected. A Worker that is still streaming a response body remains active. <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil()</code></a> extends execution for up to 30 seconds after the response or disconnect.</td>
</tr>
<tr>
<td><a href="/workers/configuration/cron-triggers/">Cron Triggers</a></td>
<td>15 minutes</td>
<td>Scheduled Workers have a maximum wall time of 15 minutes per invocation.</td>
</tr>
<tr>
<td><a href="/queues/configuration/javascript-apis/#consumer">Queue consumers</a></td>
<td>15 minutes</td>
<td>Each consumer invocation has a maximum wall time of 15 minutes.</td>
</tr>
<tr>
<td><a href="/durable-objects/api/alarms/">Durable Object alarm handlers</a></td>
<td>15 minutes</td>
<td>Alarm handler invocations have a maximum wall time of 15 minutes.</td>
</tr>
<tr>
<td><a href="/durable-objects/">Durable Objects</a> (RPC / HTTP)</td>
<td>Unlimited</td>
<td>No hard limit while the caller stays connected to the Durable Object. Durable Objects remain active while a request, RPC call, response stream, WebSocket, or pending I/O is in flight.</td>
</tr>
<tr>
<td><a href="/workflows/">Workflows</a> (per step)</td>
<td>Unlimited</td>
<td>Each step can run for an unlimited wall time. Individual steps are subject to the configured <a href="/workers/platform/limits/#cpu-time">CPU time limit</a>.</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/kv/platform/limits/">KV limits</a></li>
<li><a href="/durable-objects/platform/limits/">Durable Object limits</a></li>
<li><a href="/queues/platform/limits/">Queues limits</a></li>
<li><a href="/workers/observability/errors/">Workers errors reference</a></li>
</ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">If you need a higher Worker limit, use [Workers for Platforms](/cloudflare-for-platforms/workers-for-platforms/).</li></ol></section>
