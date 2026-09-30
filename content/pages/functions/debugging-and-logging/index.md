<p>Access your Functions logs by using the Cloudflare dashboard or the <a href="/workers/wrangler/commands/pages/#pages-deployment-tail">Wrangler CLI</a>.</p>
<p>Logs are a powerful debugging tool that can help you test and monitor the behavior of your Pages Functions once they have been deployed. Logs are available for every deployment of your Pages project.</p>
<p>Logs provide detailed information about events and can give insight into:</p>
<ul>
<li>Successful or failed requests to your Functions.</li>
<li>Uncaught exceptions thrown by your Functions.</li>
<li>Custom <code>console.log</code>s declared within your Functions.</li>
<li>Production issues that cannot be easily reproduced.</li>
<li>Real-time view of incoming requests to your application.</li>
</ul>
<p>There are two ways to start a logging session:</p>
<ol>
<li>Run <code>wrangler pages deployment tail</code> <a href="/pages/functions/debugging-and-logging/#view-logs-with-wrangler">in your terminal</a>.</li>
<li>Use the <a href="/pages/functions/debugging-and-logging/#view-logs-in-the-cloudflare-dashboard">Cloudflare dashboard</a>.</li>
</ol>
<h2 id="add-custom-logs">Add custom logs</h2>
<p>Custom logs are <code>console.log()</code> statements that you can add yourself inside your Functions. When streaming logs for deployments that contain these Functions, the statements will appear in both <code>wrangler pages deployment tail</code> and dashboard outputs.</p>
<p>Below is an example of a custom <code>console.log</code> statement inside a Pages Function:</p>
<pre><code class="language-js">export async function onRequest(context) {&#10;	console.log(&#10;		`[LOGGING FROM /hello]: Request came from ${context.request.url}`,&#10;	);&#10;&#10;	return new Response(&quot;Hello, world!&quot;);&#10;}&#10;</code></pre>
<p>After you deploy the code above, run <code>wrangler pages deployment tail</code> in your terminal. Then access the route at which your Function lives. Your terminal will display:</p>
<p><img src="/assets/upstream/images/pages/platform/functions/wrangler-custom-logs.png" alt="Run wrangler pages deployment tail" /></p>
<p>Your dashboard will display:</p>
<p><img src="/assets/upstream/images/pages/platform/functions/dash-custom-logs.png" alt="Follow the above steps to access custom logs in the dashboard" /></p>
<h2 id="view-logs-with-wrangler">View logs with Wrangler</h2>
<p><code>wrangler pages deployment tail</code> enables developers to livestream logs for a specific project and deployment.</p>
<p>To get started, run <code>wrangler pages deployment tail</code> in your Pages project directory. This will log any incoming requests to your application in your local terminal.</p>
<p>The output of each <code>wrangler pages deployment tail</code> log is a structured JSON object:</p>
<pre><code class="language-js">{&#10;  &quot;outcome&quot;: &quot;ok&quot;,&#10;  &quot;scriptName&quot;: null,&#10;  &quot;exceptions&quot;: [&#10;    {&#10;      &quot;stack&quot;: &quot;    at src/routes/index.tsx17:4\n    at new Promise (&lt;anonymous&gt;)\n&quot;,&#10;      &quot;name&quot;: &quot;Error&quot;,&#10;      &quot;message&quot;: &quot;An error has occurred&quot;,&#10;      &quot;timestamp&quot;: 1668542036110&#10;    }&#10;  ],&#10;  &quot;logs&quot;: [],&#10;  &quot;eventTimestamp&quot;: 1668542036104,&#10;  &quot;event&quot;: {&#10;    &quot;request&quot;: {&#10;      &quot;url&quot;: &quot;https://pages-fns.pages.dev&quot;,&#10;      &quot;method&quot;: &quot;GET&quot;,&#10;      &quot;headers&quot;: {},&#10;      &quot;cf&quot;: {}&#10;    },&#10;    &quot;response&quot;: {&#10;      &quot;status&quot;: 200&#10;    }&#10;  },&#10;  &quot;id&quot;: 0&#10;}&#10;</code></pre>
<p><code>wrangler pages deployment tail</code> allows you to customize a logging session to better suit your needs. Refer to the <a href="/workers/wrangler/commands/pages/#pages-deployment-tail"><code>wrangler pages deployment tail</code> documentation</a> for available configuration options.</p>
<h2 id="view-logs-in-the-cloudflare-dashboard">View logs in the Cloudflare Dashboard</h2>
<p>To view logs for your <code>production</code> or <code>preview</code> environments associated with any deployment:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project, go to the deployment you want to view logs for and select **View details** > **Functions**.
<p>Logging is available for all customers (Free, Paid, Enterprise).</p>
<h2 id="limits">Limits</h2>
<p>The following limits apply to Functions logs:</p>
<ul>
<li>Logs are not stored. You can start and stop the stream at any time to view them, but they do not persist.</li>
<li>Logs will not display if the Function’s requests per second are over 100 for the last five minutes.</li>
<li>Logs from any <a href="/pages/functions/bindings/#durable-objects">Durable Objects</a> your Functions bind to will show up in the Cloudflare dashboard.</li>
<li>A maximum of 10 clients can view a deployment’s logs at one time. This can be a combination of either dashboard sessions or <code>wrangler pages deployment tail</code> calls.</li>
</ul>
<h2 id="sourcemaps">Sourcemaps</h2>
<p>If you're debugging an uncaught exception, you might find that the <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack">stack traces</a> in your logs contain line numbers to generated JavaScript files. Using Pages' support for <a href="https://web.dev/articles/source-maps">source maps</a> you can get stack traces that match with the line numbers and symbols of your original source code.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10953.md")
</aside>
<p>Refer to <a href="/pages/functions/source-maps/">Source maps and stack traces</a> for an in-depth explanation.</p>
