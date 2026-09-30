<p>A Tail Worker receives information about the execution of other Workers (known as producer Workers), such as HTTP statuses, data passed to <code>console.log()</code> or uncaught exceptions. Tail Workers can process logs for alerts, debugging, or analytics.</p>
<p>Tail Workers are available to all customers on the Workers Paid and Enterprise tiers. Tail Workers are billed by <a href="/workers/platform/pricing/#workers">CPU time</a>, not by the number of requests.</p>
<p><img src="/assets/upstream/images/workers/platform/tail-workers.png" alt="Tail Worker diagram" /></p>
<p>A Tail Worker is automatically invoked after the invocation of a producer Worker (the Worker the Tail Worker will track) that contains the application logic. It captures events after the producer has finished executing. Events throughout the request lifecycle, including potential sub-requests via <a href="/workers/runtime-apis/bindings/service-bindings/">Service Bindings</a> and <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">Dynamic Dispatch</a>, will be included. You can filter, change the format of the data, and send events to any HTTP endpoint. For quick debugging, Tail Workers can be used to send logs to <a href="/kv/api/">KV</a> or any database.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="export-batches-of-logs-and-traces-to-sentry-grafana-honeycomb-and-more">Export batches of logs and traces to Sentry, Grafana, Honeycomb and more</h3>
@markup("md", "content/.markup/bodies/17037.md")
</aside>
<h2 id="configure-tail-workers">Configure Tail Workers</h2>
<p>To configure a Tail Worker:</p>
<ol>
<li><a href="/workers/get-started/guide">Create a Worker</a> to serve as the Tail Worker.</li>
<li>Add a <a href="/workers/runtime-apis/handlers/tail/"><code>tail()</code></a> handler to your Worker. The <code>tail()</code> handler is invoked every time the producer Worker to which a Tail Worker is connected is invoked. The following Worker code is a Tail Worker that sends its data to an HTTP endpoint:</li>
</ol>
<pre><code class="language-js">export default {&#10;	async tail(events) {&#10;		fetch(&quot;https://example.com/endpoint&quot;, {&#10;			method: &quot;POST&quot;,&#10;			body: JSON.stringify(events),&#10;		});&#10;	},&#10;};&#10;</code></pre>
<p>The following Worker code is an example of what the <code>events</code> object may look like:</p>
<pre><code class="language-json">[&#10;	{&#10;		&quot;scriptName&quot;: &quot;Example script&quot;,&#10;		&quot;outcome&quot;: &quot;exception&quot;,&#10;		&quot;eventTimestamp&quot;: 1587058642005,&#10;		&quot;event&quot;: {&#10;			&quot;request&quot;: {&#10;				&quot;url&quot;: &quot;https://example.com/some/requested/url&quot;,&#10;				&quot;method&quot;: &quot;GET&quot;,&#10;				&quot;headers&quot;: {&#10;					&quot;cf-ray&quot;: &quot;57d55f210d7b95f3&quot;,&#10;					&quot;x-custom-header-name&quot;: &quot;my-header-value&quot;&#10;				},&#10;				&quot;cf&quot;: {&#10;					&quot;colo&quot;: &quot;SJC&quot;&#10;				}&#10;			}&#10;		},&#10;		&quot;logs&quot;: [&#10;			{&#10;				&quot;message&quot;: [&quot;string passed to console.log()&quot;],&#10;				&quot;level&quot;: &quot;log&quot;,&#10;				&quot;timestamp&quot;: 1587058642005&#10;			}&#10;		],&#10;		&quot;exceptions&quot;: [&#10;			{&#10;				&quot;name&quot;: &quot;Error&quot;,&#10;				&quot;message&quot;: &quot;Threw a sample exception&quot;,&#10;				&quot;timestamp&quot;: 1587058642005&#10;			}&#10;		],&#10;		&quot;diagnosticsChannelEvents&quot;: [&#10;			{&#10;				&quot;channel&quot;: &quot;foo&quot;,&#10;				&quot;message&quot;: &quot;The diagnostic channel message&quot;,&#10;				&quot;timestamp&quot;: 1587058642005&#10;			}&#10;		]&#10;	}&#10;]&#10;</code></pre>
<ol start="3">
<li>Add the following to the Wrangler file of the producer Worker:</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17038.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17036.md")
</aside>
<h2 id="use-analytics-engine-for-aggregated-metrics">Use Analytics Engine for aggregated metrics</h2>
<p>If you need aggregated analytics rather than individual log events, consider writing to <a href="/analytics/analytics-engine/">Workers Analytics Engine</a> from your Tail Worker. Analytics Engine is optimized for high-cardinality, time-series data that you can query with SQL.</p>
<p>For example, you can use a Tail Worker to count errors by endpoint, track response times by customer, or build usage metrics, then write those aggregates to Analytics Engine for querying and visualization.</p>
<pre><code class="language-js">export default {&#10;	async tail(events, env) {&#10;		for (const event of events) {&#10;			env.ANALYTICS.writeDataPoint({&#10;				blobs: [event.scriptName, event.outcome],&#10;				doubles: [1],&#10;				indexes: [event.event?.request?.cf?.colo ?? &quot;unknown&quot;],&#10;			});&#10;		}&#10;	},&#10;};&#10;</code></pre>
<p>Refer to the <a href="/analytics/analytics-engine/">Analytics Engine documentation</a> for more details on writing and querying data.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/handlers/tail/"><code>tail()</code></a> Handler API docs - Learn how to set up a <code>tail()</code> handler in your Worker.</li>
<li><a href="/analytics/analytics-engine/">Analytics Engine</a> - Write custom analytics from your Worker for high-cardinality, time-series queries.</li>
<li><a href="/workers/observability/errors/">Errors and exceptions</a> - Review common Workers errors.</li>
<li><a href="/workers/local-development/">Local development</a> - Develop and test your Workers locally.</li>
<li><a href="/workers/observability/source-maps">Source maps and stack traces</a> - Learn how to enable source maps and generate stack traces for Workers.</li>
</ul>
