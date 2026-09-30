<p>Workers for Platforms provides you with logs and analytics that can be used to share data with end users.</p>
<h2 id="logs">Logs</h2>
<p>There are a few ways to access logs with Workers for Platforms. They differ in how much of the logging stack Cloudflare runs for you:</p>
<ul>
<li><a href="#workers-logs">Workers Logs</a> — Cloudflare stores and indexes your logs, and you query them through the API. Nothing else to run. This is the best starting point for most platforms.</li>
<li><a href="#workers-trace-events-logpush">Logpush</a> — Cloudflare delivers your logs to a storage destination that you own and manage.</li>
<li><a href="#tail-workers">Tail Workers</a> — Cloudflare streams your logs to a Worker in real time, and you decide what to do with them.</li>
</ul>
<h3 id="workers-logs">Workers Logs</h3>
<p><a href="/workers/observability/logs/workers-logs/">Workers Logs</a> automatically stores logs from your user Workers in your Cloudflare account, where you can query them with the <a href="/workers/observability/query-builder/">Query Builder</a> or the <a href="/api/resources/workers/subresources/observability/">Workers Observability API</a>. Because it is fully managed, you can surface a per-user view of logs in your own dashboard without standing up a database, setting up Logpush, or deploying a Tail Worker.</p>
<p>Enable Workers Logs on a user Worker by including the <code>observability</code> setting in the <a href="/cloudflare-for-platforms/workers-for-platforms/reference/metadata/">metadata</a> when you <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/update/">upload the script</a> to your dispatch namespace:</p>
<pre><code class="language-json">{&#10;	&quot;main_module&quot;: &quot;index.js&quot;,&#10;	&quot;observability&quot;: {&#10;		&quot;enabled&quot;: true,&#10;		&quot;logs&quot;: {&#10;			&quot;enabled&quot;: true,&#10;			&quot;invocation_logs&quot;: true,&#10;			&quot;head_sampling_rate&quot;: 1&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Because you control the upload metadata, you decide whether logging is enabled for each user Worker. Set <code>head_sampling_rate</code> to a value between 0 and 1 to log a percentage of requests, or set <code>observability.enabled</code> to <code>false</code> to turn off collection.</p>
<h4 id="query-logs-for-a-single-user-worker">Query logs for a single user Worker</h4>
<p>Workers Logs are stored in the <code>cloudflare-workers</code> dataset. When you query the <a href="/api/resources/workers/subresources/observability/">Workers Observability API</a> on behalf of an end user, scope every query to the specific user Worker so that one tenant cannot read another tenant's telemetry. Filter on <code>dataset</code> (set to <code>cloudflare-workers</code>) and <code>$metadata.service</code> (the user Worker's script name).</p>
<p>Apply these filters on the server using the script name you control, rather than accepting a script name, dataset, or raw filter from the browser. This keeps each user's logs isolated even when the query is triggered by end-user input such as a search term or time range.</p>
<h3 id="workers-trace-events-logpush">Workers Trace Events Logpush</h3>
<p>Workers Trace Events logpush is used to get raw Workers execution logs. Refer to <a href="/workers/observability/logs/logpush/">Logpush</a> for more information.</p>
<p>Logpush can be enabled for an entire dispatch namespace or a single user Worker. To capture logs for all of the user Workers in a dispatch namespace:</p>
<ol>
<li>Create a <a href="/workers/observability/logs/logpush/#create-a-logpush-job">Logpush job</a>.</li>
<li>Enable <a href="/workers/observability/logs/logpush/#enable-logging-on-your-worker">logging</a> on your dispatch Worker.</li>
</ol>
<p>Enabling logging on your dispatch Worker collects logs for both the dispatch Worker and for any user Workers in the dispatch namespace. Logs are automatically collected for all new Workers added to a dispatch namespace. To enable logging for an individual user Worker rather than an entire dispatch namespace, skip step 1 and complete step 2 on your user Worker.</p>
<p>All logs are forwarded to the Logpush job that you have setup for your account. Logpush filters can be used on the <code>Outcome</code> or <code>Script Name</code> field to include or exclude specific values or send logs to different destinations.</p>
<h3 id="tail-workers">Tail Workers</h3>
<p>A <a href="/workers/observability/logs/tail-workers/">Tail Worker</a> receives information about the execution of other Workers (known as producer Workers), such as HTTP statuses, data passed to <code>console.log()</code> or uncaught exceptions.</p>
<p>Use <a href="/workers/observability/logs/tail-workers/">Tail Workers</a> instead of Logpush if you want to format logs before they leave Cloudflare, receive <a href="/workers/runtime-apis/nodejs/diagnostics-channel">diagnostics channel events</a>, or get logs in real time.</p>
<p>To collect logs from a user Worker, add the <a href="/workers/observability/logs/tail-workers/#configure-tail-workers">Tail Worker configuration</a> directly to that user Worker.</p>
<h2 id="analytics">Analytics</h2>
<p>There are two ways for you to review your Workers for Platforms analytics.</p>
<h3 id="workers-analytics-engine">Workers Analytics Engine</h3>
<p><a href="/analytics/analytics-engine/">Workers Analytics Engine</a> can be used with Workers for Platforms to provide analytics to end users. It can be used to expose events relating to a Workers invocation or custom user-defined events. Platforms can write/query events by script tag to get aggregates over a user’s usage.</p>
<h3 id="graphql-analytics-api">GraphQL Analytics API</h3>
<p>Use Cloudflare’s <a href="/analytics/graphql-api">GraphQL Analytics API</a> to get metrics relating to your Dispatch Namespaces. Use the <code>dispatchNamespaceName</code> dimension in the <code>workersInvocationsAdaptive</code> node to query usage by namespace.</p>
<p>To show metrics for a single user Worker, filter <code>workersInvocationsAdaptive</code> by the <code>scriptName</code> of that user Worker. This returns request counts, error counts, and CPU time quantiles without requiring Workers Logs to be enabled, so you can display per-user metrics even when log collection is turned off.</p>
<pre><code class="language-graphql">query UserWorkerMetrics($accountTag: string!, $scriptName: string!, $start: Time!, $end: Time!) {&#10;  viewer {&#10;    accounts(filter: { accountTag: $accountTag }) {&#10;      workersInvocationsAdaptive(&#10;        limit: 1&#10;        filter: { scriptName: $scriptName, datetime_geq: $start, datetime_leq: $end }&#10;      ) {&#10;        sum {&#10;          requests&#10;          errors&#10;        }&#10;        quantiles {&#10;          cpuTimeP50&#10;          cpuTimeP99&#10;        }&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
