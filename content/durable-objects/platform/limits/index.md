<p>Durable Objects are a special kind of Worker, so <a href="/workers/platform/limits/">Workers Limits</a> apply according to your Workers plan. In addition, Durable Objects have specific limits as listed in this page.</p>
<h2 id="sqlite-backed-durable-objects-general-limits">SQLite-backed Durable Objects general limits</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Number of Objects</td>
<td>Unlimited (within an account or of a given class)</td>
</tr>
<tr>
<td>Maximum Durable Object classes (per account)</td>
<td>500 (Workers Paid) / 100 (Free) <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td>Storage per account</td>
<td>Unlimited (Workers Paid) / 5GB (Free) <sup><a href="#footnote-2">2</a></sup></td>
</tr>
<tr>
<td>Storage per class</td>
<td>Unlimited <sup><a href="#footnote-3">3</a></sup></td>
</tr>
<tr>
<td>Storage per Durable Object</td>
<td>10 GB <sup><a href="#footnote-3">3</a></sup></td>
</tr>
<tr>
<td>Key size</td>
<td>Key and value combined cannot exceed 2 MB</td>
</tr>
<tr>
<td>Value size</td>
<td>Key and value combined cannot exceed 2 MB</td>
</tr>
<tr>
<td>WebSocket message size</td>
<td>32 MiB (only for received messages)</td>
</tr>
<tr>
<td>CPU per request</td>
<td>30 seconds (default) / configurable to 5 minutes of <a href="/workers/platform/limits/#cpu-time">active CPU time</a> <sup><a href="#footnote-4">4</a></sup></td>
</tr>
<tr>
<td>Simultaneous outgoing connections/request</td>
<td>6 (same as <a href="/workers/platform/limits/#simultaneous-open-connections">Workers</a>)</td>
</tr>
</tbody>
</table>
<h3 id="sql-storage-limits">SQL storage limits</h3>
<p>For Durable Object classes with <a href="/durable-objects/api/sqlite-storage-api/">SQLite storage</a> these SQL limits apply:</p>
<table>
<thead>
<tr>
<th>SQL</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum number of columns per table</td>
<td>100</td>
</tr>
<tr>
<td>Maximum number of rows per table</td>
<td>Unlimited (excluding per-object storage limits)</td>
</tr>
<tr>
<td>Maximum string, <code>BLOB</code> or table row size</td>
<td>2 MB</td>
</tr>
<tr>
<td>Maximum SQL statement length</td>
<td>100 KB</td>
</tr>
<tr>
<td>Maximum bound parameters per query</td>
<td>100</td>
</tr>
<tr>
<td>Maximum arguments per SQL function</td>
<td>32</td>
</tr>
<tr>
<td>Maximum characters (bytes) in a <code>LIKE</code> or <code>GLOB</code> pattern</td>
<td>50 bytes</td>
</tr>
</tbody>
</table>
<h2 id="key-value-backed-durable-objects-general-limits">Key-value backed Durable Objects general limits</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8164.md")
</aside>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit for class with key-value storage backend</th>
</tr>
</thead>
<tbody>
<tr>
<td>Number of Objects</td>
<td>Unlimited (within an account or of a given class)</td>
</tr>
<tr>
<td>Maximum Durable Object classes (per account)</td>
<td>500 (Workers Paid) / 100 (Free) <sup><a href="#footnote-5">5</a></sup></td>
</tr>
<tr>
<td>Storage per account</td>
<td>50 GB (can be raised by contacting Cloudflare) <sup><a href="#footnote-6">6</a></sup></td>
</tr>
<tr>
<td>Storage per class</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Storage per Durable Object</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Key size</td>
<td>2 KiB (2048 bytes)</td>
</tr>
<tr>
<td>Value size</td>
<td>128 KiB (131072 bytes)</td>
</tr>
<tr>
<td>WebSocket message size</td>
<td>32 MiB (only for received messages)</td>
</tr>
<tr>
<td>CPU per request</td>
<td>30s (including WebSocket messages) <sup><a href="#footnote-7">7</a></sup></td>
</tr>
<tr>
<td>Simultaneous outgoing connections/request</td>
<td>6 (same as <a href="/workers/platform/limits/#simultaneous-open-connections">Workers</a>)</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/8163.md")
</aside>
<h2 id="frequently-asked-questions">Frequently Asked Questions</h2>
<h3 id="how-much-work-can-a-single-durable-object-do">How much work can a single Durable Object do?</h3>
<p>Durable Objects can scale horizontally across many Durable Objects. Each individual Object is inherently single-threaded.</p>
<ul>
<li>An individual Object has a soft limit of 1,000 requests per second. You can have an unlimited number of individual objects per namespace.</li>
<li>A simple <a href="/durable-objects/api/sqlite-storage-api/">storage</a> <code>get()</code> on a small value that directly returns the response may realize a higher request throughput compared to a Durable Object that (for example) serializes and/or deserializes large JSON values.</li>
<li>Similarly, a Durable Object that performs multiple <code>list()</code> operations may be more limited in terms of request throughput.</li>
</ul>
<p>A Durable Object that receives too many requests will, after attempting to queue them, return an <a href="/durable-objects/observability/troubleshooting/#durable-object-is-overloaded">overloaded</a> error to the caller.</p>
<h3 id="how-many-durable-objects-can-i-create">How many Durable Objects can I create?</h3>
<p>Durable Objects are designed such that the number of individual objects in the system do not need to be limited, and can scale horizontally.</p>
<ul>
<li>You can create and run as many separate Durable Objects as you want within a given Durable Object <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/8165.md")
</div>.
- There are no limits for storage per account when using SQLite-backed Durable Objects on a Workers Paid plan.
- Each SQLite-backed Durable Object has a storage limit of 10 GB on a Workers Paid plan.
- Refer to [Durable Object limits](/durable-objects/platform/limits/) for more information.
<h3 id="can-i-increase-durable-objects-cpu-limit">Can I increase Durable Objects' CPU limit?</h3>
<p>Durable Objects are Worker scripts, and have the same <a href="/workers/platform/limits/#account-plan-limits">per invocation CPU limits</a> as any Workers do. Note that CPU time is active processing time: not time spent waiting on network requests, storage calls, or other general I/O, which don't count towards your CPU time or Durable Objects compute consumption.</p>
<p>By default, the maximum CPU time per Durable Objects invocation (HTTP request, WebSocket message, or Alarm) is set to 30 seconds, but can be increased for all Durable Objects associated with a Durable Object definition by setting <code>limits.cpu_ms</code> in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8166.md")
</div>
<h3 id="what-happens-when-a-durable-object-exceeds-its-storage-limit">What happens when a Durable Object exceeds its storage limit?</h3>
<p>When a SQLite-backed Durable Object reaches its <a href="/durable-objects/platform/limits/">maximum storage limit</a> (10 GB on Workers Paid, or 1 GB on the Free plan), write operations (such as <code>INSERT</code>, <code>UPDATE</code>, or calls to the <code>put()</code> and <code>sql.exec()</code> storage APIs) will fail with the following error:</p>
<pre><code class="language-txt">database or disk is full: SQLITE_FULL&#10;</code></pre>
<p>Read operations (such as <code>SELECT</code> queries, <code>get()</code>, and <code>list()</code> calls) will continue to work, and <code>DELETE</code> operations will also succeed so that you can remove data to free up space.</p>
<p>To handle this error in your Durable Object, catch the exception thrown by the storage API:</p>
<pre><code class="language-ts">try {&#10;	this.ctx.storage.sql.exec(&#10;		&quot;INSERT INTO my_table (key, value) VALUES (?, ?)&quot;,&#10;		key,&#10;		value,&#10;	);&#10;} catch (e) {&#10;	if (e.message.includes(&quot;SQLITE_FULL&quot;)) {&#10;		// Storage limit reached — reads and deletes still work&#10;		// Consider deleting old data or returning a meaningful error to the caller&#10;	}&#10;	throw e;&#10;}&#10;</code></pre>
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
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Identical to the Workers [script limit](/workers/platform/limits/).</li>
<li id="footnote-2">Durable Objects both bills and measures storage based on a gigabyte <br/> (1 GB = 1,000,000,000 bytes) and not a gibibyte (GiB). <br/></li>
<li id="footnote-3">Accounts on the Workers Free plan are limited to 5 GB total Durable Objects storage.</li>
<li id="footnote-4">Each incoming HTTP request or WebSocket _message_ resets the remaining available CPU time to 30 seconds. This allows the Durable Object to consume up to 30 seconds of compute after each incoming network request, with each new network request resetting the timer. If you consume more than 30 seconds of compute between incoming network requests, there is a heightened chance that the individual Durable Object is evicted and reset. CPU time per request invocation [can be increased](/durable-objects/platform/limits/#can-i-increase-durable-objects-cpu-limit).</li>
<li id="footnote-5">Identical to the Workers [script limit](/workers/platform/limits/).</li>
<li id="footnote-6">Durable Objects both bills and measures storage based on a gigabyte <br/> (1 GB = 1,000,000,000 bytes) and not a gibibyte (GiB). <br/></li>
<li id="footnote-7">Each incoming HTTP request or WebSocket _message_ resets the remaining available CPU time to 30 seconds. This allows the Durable Object to consume up to 30 seconds of compute after each incoming network request, with each new network request resetting the timer. If you consume more than 30 seconds of compute between incoming network requests, there is a heightened chance that the individual Durable Object is evicted and reset. CPU time per request invocation [can be increased](/durable-objects/platform/limits/#can-i-increase-durable-objects-cpu-limit).</li></ol></section>
