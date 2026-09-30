<h1 id="changelog">Changelog</h1>

<h2 id="r2-data-catalog-table-level-compaction"><a href="/changelog/post/2025-10-06-data-catalog-table-compaction/">R2 Data Catalog table-level compaction</a></h2>
<p><em>2025-10-06</em></p>
<p>You can now enable compaction for individual <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a>, giving you fine-grained control over different workloads.</p>
<pre><code class="language-bash">&#35; Enable compaction for a specific table (no token required)&#10;npx wrangler r2 bucket catalog compaction enable &lt;BUCKET&gt; &lt;NAMESPACE&gt; &lt;TABLE&gt; --target-size 256&#10;</code></pre>
<p>This allows you to:</p>
<ul>
<li>Apply different target file sizes per table</li>
<li>Disable compaction for specific tables</li>
<li>Optimize based on table-specific access patterns</li>
</ul>
<p>Learn more at <a href="/r2-data-catalog/manage-catalogs/">Manage catalogs</a>.</p>


<h2 id="one-click-cloudflare-access-for-workers"><a href="/changelog/post/2025-10-03-one-click-access-for-workers/">One-click Cloudflare Access for Workers</a></h2>
<p><em>2025-10-03</em></p>
<p>You can now enable <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> for your <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code></a> and <a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a> in a single click.</p>
<p><img src="/assets/upstream/images/workers/changelog/workers-access.png" alt="Screenshot of the Enable/Disable Cloudflare Access button on the workers.dev route settings page" /></p>
<p>Access allows you to limit access to your Workers to specific users or groups. You can limit access to yourself, your teammates, your organization, or anyone else you specify in your <a href="/cloudflare-one/access-controls/policies/">Access policy</a>.</p>
<p>To enable Cloudflare Access:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domains &amp; Routes</strong>.</li>
<li>For <code>workers.dev</code> or Preview URLs, click <strong>Enable Cloudflare Access</strong>.</li>
<li>Optionally, to configure the Access application, click <strong>Manage Cloudflare Access</strong>. There, you can change the email addresses you want to authorize. View <a href="/cloudflare-one/access-controls/policies/#selectors">Access policies</a> to learn about configuring alternate rules.</li>
</ol>
<p>To fully secure your application, it is important that you validate the JWT that Cloudflare Access adds to the <code>Cf-Access-Jwt-Assertion</code> header on the incoming request.</p>
<p>The following code will validate the JWT using the <a href="https://www.npmjs.com/package/jose">jose NPM package</a>:</p>
<pre><code class="language-javascript">import { jwtVerify, createRemoteJWKSet } from &quot;jose&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		// Verify the POLICY_AUD environment variable is set&#10;		if (!env.POLICY_AUD) {&#10;			return new Response(&quot;Missing required audience&quot;, {&#10;				status: 403,&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		}&#10;&#10;		// Get the JWT from the request headers&#10;		const token = request.headers.get(&quot;cf-access-jwt-assertion&quot;);&#10;&#10;		// Check if token exists&#10;		if (!token) {&#10;			return new Response(&quot;Missing required CF Access JWT&quot;, {&#10;				status: 403,&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		}&#10;&#10;		try {&#10;			// Create JWKS from your team domain&#10;			const JWKS = createRemoteJWKSet(&#10;				new URL(`${env.TEAM_DOMAIN}/cdn-cgi/access/certs`),&#10;			);&#10;&#10;			// Verify the JWT&#10;			const { payload } = await jwtVerify(token, JWKS, {&#10;				issuer: env.TEAM_DOMAIN,&#10;				audience: env.POLICY_AUD,&#10;			});&#10;&#10;			// Token is valid, proceed with your application logic&#10;			return new Response(`Hello ${payload.email || &quot;authenticated user&quot;}!`, {&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		} catch (error) {&#10;			// Token verification failed&#10;			return new Response(`Invalid token: ${error.message}`, {&#10;				status: 403,&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-10-03-one-click-access-for-workers-required-environment-variables">Required environment variables</h4>
<p>Add these <a href="/workers/configuration/environment-variables/">environment variables</a> to your Worker:</p>
<ul>
<li><code>POLICY_AUD</code>: Your application's AUD tag</li>
<li><code>TEAM_DOMAIN</code>: <code>https://&lt;your-team-name&gt;.cloudflareaccess.com</code></li>
</ul>
<p>Both of these appear in the modal that appears when you enable Cloudflare Access.</p>
<p>You can set these variables by adding them to your Worker's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, or via the Cloudflare dashboard under <strong>Workers &amp; Pages</strong> &gt; <strong>your-worker</strong> &gt; <strong>Settings</strong> &gt; <strong>Environment Variables</strong>.</p>


<h2 id="workers-analytics-engine-adds-supports-for-new-sql-functions"><a href="/changelog/post/2025-09-26-analytics-engine-sql-enhancements/">Workers Analytics Engine adds supports for new SQL functions</a></h2>
<p><em>2025-10-02</em></p>
<p>You can now perform more powerful queries directly in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a> with a major expansion of our SQL function library.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.</p>
<p>Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:</p>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/"><strong>New aggregate functions:</strong></a></p>
<ul>
<li><code>argMin()</code> - Returns the value associated with the minimum in a group</li>
<li><code>argMax()</code> - Returns the value associated with the maximum in a group</li>
<li><code>topK()</code> - Returns an array of the most frequent values in a group</li>
<li><code>topKWeighted()</code> - Returns an array of the most frequent values in a group using weights</li>
<li><code>first_value()</code> - Returns the first value in an ordered set of values within a partition</li>
<li><code>last_value()</code> - Returns the last value in an ordered set of values within a partition</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/"><strong>New bit functions:</strong></a></p>
<ul>
<li><code>bitAnd()</code> - Returns the bitwise AND of two expressions</li>
<li><code>bitCount()</code> - Returns the number of bits set to one in the binary representation of a number</li>
<li><code>bitHammingDistance()</code> - Returns the number of bits that differ between two numbers</li>
<li><code>bitNot()</code> - Returns a number with all bits flipped</li>
<li><code>bitOr()</code> - Returns the inclusive bitwise OR of two expressions</li>
<li><code>bitRotateLeft()</code> - Rotates all bits in a number left by specified positions</li>
<li><code>bitRotateRight()</code> - Rotates all bits in a number right by specified positions</li>
<li><code>bitShiftLeft()</code> - Shifts all bits in a number left by specified positions</li>
<li><code>bitShiftRight()</code> - Shifts all bits in a number right by specified positions</li>
<li><code>bitTest()</code> - Returns the value of a specific bit in a number</li>
<li><code>bitXor()</code> - Returns the bitwise exclusive-or of two expressions</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/"><strong>New mathematical functions:</strong></a></p>
<ul>
<li><code>abs()</code> - Returns the absolute value of a number</li>
<li><code>log()</code> - Computes the natural logarithm of a number</li>
<li><code>round()</code> - Rounds a number to a specified number of decimal places</li>
<li><code>ceil()</code> - Rounds a number up to the nearest integer</li>
<li><code>floor()</code> - Rounds a number down to the nearest integer</li>
<li><code>pow()</code> - Returns a number raised to the power of another number</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/string-functions/"><strong>New string functions:</strong></a></p>
<ul>
<li><code>lowerUTF8()</code> - Converts a string to lowercase using UTF-8 encoding</li>
<li><code>upperUTF8()</code> - Converts a string to uppercase using UTF-8 encoding</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/"><strong>New encoding functions:</strong></a></p>
<ul>
<li><code>hex()</code> - Converts a number to its hexadecimal representation</li>
<li><code>bin()</code> - Converts a string to its binary representation</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/"><strong>New type conversion functions:</strong></a></p>
<ul>
<li><code>toUInt8()</code> - Converts any numeric expression, or expression resulting in a string representation of a decimal, into an unsigned 8 bit integer</li>
</ul>
<h4 id="2025-09-26-analytics-engine-sql-enhancements-ready-to-get-started">Ready to get started?</h4>
Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started ](/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](/analytics/analytics-engine/sql-reference/).


<h2 id="new-deepgram-flux-model-available-on-workers-ai"><a href="/changelog/post/2025-10-02-deepgram-flux/">New Deepgram Flux model available on Workers AI</a></h2>
<p><em>2025-10-02</em></p>
<p>Deepgram's newest Flux model <a href="/workers-ai/models/flux/"><code>@cf/deepgram/flux</code></a> is now available on Workers AI, hosted directly on Cloudflare's infrastructure. We're excited to be a launch partner with Deepgram and offer their new Speech Recognition model built specifically for enabling voice agents. Check out <a href="https://deepgram.com/flux">Deepgram's blog</a> for more details on the release.</p>
<p>The Flux model can be used in conjunction with Deepgram's speech-to-text model <a href="/workers-ai/models/nova-3/"><code>@cf/deepgram/nova-3</code></a> and text-to-speech model <a href="/workers-ai/models/aura-1/"><code>@cf/deepgram/aura-1</code></a> to build end-to-end voice agents. Having Deepgram on Workers AI takes advantage of our edge GPU infrastructure, for ultra low latency voice AI applications.</p>
<h4 id="2025-10-02-deepgram-flux-promotional-pricing">Promotional Pricing</h4>
For the month of October 2025, Deepgram's Flux model will be free to use on Workers AI. Official pricing will be announced soon and charged after the promotional pricing period ends on October 31, 2025. Check out the [model page](/workers-ai/models/flux/) for pricing details in the future.
<h4 id="2025-10-02-deepgram-flux-example-usage">Example Usage</h4>
<p>The new Flux model is WebSocket only as it requires live bi-directional streaming in order to recognize speech activity.</p>
<ol>
<li>Create a worker that establishes a websocket connection with <code>@cf/deepgram/flux</code></li>
</ol>
<pre><code class="language-js">export default {&#10;  async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;    const resp = await env.AI.run(&quot;@cf/deepgram/flux&quot;, {&#10;      encoding: &quot;linear16&quot;,&#10;      sample_rate: &quot;16000&quot;&#10;    }, {&#10;      websocket: true&#10;    });&#10;    return resp;&#10;  },&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<ol start="2">
<li>Deploy your worker</li>
</ol>
<pre><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<ol start="3">
<li>Write a client script to connect to your worker and start sending random audio bytes to it</li>
</ol>
<pre><code class="language-js">const ws = new WebSocket(&#x27;wss://&lt;your-worker-url.com&gt;&#x27;);&#10;&#10;ws.onopen = () =&gt; {&#10;  console.log(&#x27;Connected to WebSocket&#x27;);&#10;&#10;  // Generate and send random audio bytes&#10;  // You can replace this part with a function&#10;  // that reads from your mic or other audio source&#10;  const audioData = generateRandomAudio();&#10;  ws.send(audioData);&#10;  console.log(&#x27;Audio data sent&#x27;);&#10;};&#10;&#10;ws.onmessage = (event) =&gt; {&#10;  // Transcription will be received here&#10;  // Add your custom logic to parse the data&#10;  console.log(&#x27;Received:&#x27;, event.data);&#10;};&#10;&#10;ws.onerror = (error) =&gt; {&#10;  console.error(&#x27;WebSocket error:&#x27;, error);&#10;};&#10;&#10;ws.onclose = () =&gt; {&#10;  console.log(&#x27;WebSocket closed&#x27;);&#10;};&#10;&#10;// Generate random audio data (1 second of noise at 44.1kHz, mono)&#10;function generateRandomAudio() {&#10;  const sampleRate = 44100;&#10;  const duration = 1;&#10;  const numSamples = sampleRate * duration;&#10;  const buffer = new ArrayBuffer(numSamples * 2);&#10;  const view = new Int16Array(buffer);&#10;&#10;  for (let i = 0; i &lt; numSamples; i++) {&#10;    view[i] = Math.floor(Math.random() * 65536 - 32768);&#10;  }&#10;&#10;  return buffer;&#10;}&#10;</code></pre>


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


<h2 id="automatic-loopback-bindings-via-ctx-exports"><a href="/changelog/post/2025-09-26-ctx-exports/">Automatic loopback bindings via ctx.exports</a></h2>
<p><em>2025-09-26</em></p>
<p>The <a href="/workers/runtime-apis/context/#exports"><code>ctx.exports</code> API</a> contains automatically-configured bindings corresponding to your Worker's top-level exports. For each top-level export extending <code>WorkerEntrypoint</code>, <code>ctx.exports</code> will contain a <a href="/workers/runtime-apis/bindings/service-bindings">Service Binding</a> by the same name, and for each export extending <code>DurableObject</code> (and for which storage has been configured via a <a href="/durable-objects/reference/durable-objects-migrations/">migration</a>), <code>ctx.exports</code> will contain a <a href="/durable-objects/api/namespace/">Durable Object namespace binding</a>. This means you no longer have to configure these bindings explicitly in <code>wrangler.jsonc</code>/<code>wrangler.toml</code>.</p>
<p>Example:</p>
<pre><code class="language-js">import { WorkerEntrypoint } from &quot;cloudflare:workers&quot;;&#10;&#10;export class Greeter extends WorkerEntrypoint {&#10;  greet(name) {&#10;    return `Hello, ${name}!`;&#10;  }&#10;}&#10;&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    let greeting = await ctx.exports.Greeter.greet(&quot;World&quot;)&#10;    return new Response(greeting);&#10;  }&#10;}&#10;</code></pre>
<p>At present, you must use <a href="/workers/configuration/compatibility-flags#enable-ctxexports">the <code>enable_ctx_exports</code> compatibility flag</a> to enable this API, though it will be on by default in the future.</p>
<p><a href="/workers/runtime-apis/context/#exports">See the API reference for more information.</a></p>


<h2 id="pipelines-now-supports-sql-transformations-and-apache-iceberg"><a href="/changelog/post/2025-09-25-pipelines-sql/">Pipelines now supports SQL transformations and Apache Iceberg</a></h2>
<p><em>2025-09-25T13:00:00</em></p>
<p>Today, we're launching the new <a href="/pipelines/">Cloudflare Pipelines</a>: a streaming data platform that ingests events, transforms them with <a href="/pipelines/sql-reference/select-statements/">SQL</a>, and writes to <a href="/r2/">R2</a> as <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables or Parquet files.</p>
<p>Pipelines can receive events via <a href="/pipelines/streams/writing-to-streams/#send-via-http">HTTP endpoints</a> or <a href="/pipelines/streams/writing-to-streams/#send-via-workers">Worker bindings</a>, transform them with SQL, and deliver to R2 with exactly-once guarantees. This makes it easy to build analytics-ready warehouses for server logs, mobile application events, IoT telemetry, or clickstream data without managing streaming infrastructure.</p>
<p>For example, here's a pipeline that ingests clickstream events and filters out bot traffic while extracting domain information:</p>
<pre><code class="language-sql">INSERT into events_table&#10;SELECT&#10;  user_id,&#10;  lower(event) AS event_type,&#10;  to_timestamp_micros(ts_us) AS event_time,&#10;  regexp_match(url, &#x27;^https?://([^/]+)&#x27;)[1]  AS domain,&#10;  url,&#10;  referrer,&#10;  user_agent&#10;FROM events_json&#10;WHERE event = &#x27;page_view&#x27;&#10;  AND NOT regexp_like(user_agent, &#x27;(?i)bot|spider&#x27;);&#10;</code></pre>
<p>Get started by creating a pipeline in the dashboard or running a single command in <a href="/workers/wrangler/">Wrangler</a>:</p>
<pre><code class="language-bash">npx wrangler pipelines setup&#10;</code></pre>
<p>Check out our <a href="/pipelines/getting-started/">getting started guide</a> to learn how to create a pipeline that delivers events to an <a href="/r2-data-catalog/">Iceberg table</a> you can query with R2 SQL. Read more about today's announcement in our <a href="https://blog.cloudflare.com/cloudflare-data-platform">blog post</a>.</p>


<h2 id="announcing-r2-sql"><a href="/changelog/post/2025-09-25-announcing-r2-sql-open-beta/">Announcing R2 SQL</a></h2>
<p><em>2025-09-25T13:00:00</em></p>
<p>Today, we're launching the <strong>open beta</strong> for <a href="/r2-sql/">R2 SQL</a>: A serverless, distributed query engine that can efficiently analyze petabytes of data in <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables managed by <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<p>R2 SQL is ideal for exploring analytical and time-series data stored in R2, such as logs, events from <a href="/pipelines/">Pipelines</a>, or clickstream and user behavior data.</p>
<p>If you already have a table in R2 Data Catalog, running queries is as simple as:</p>
<pre><code class="language-bash">npx wrangler r2 sql query YOUR_WAREHOUSE &quot;&#10;SELECT&#10;    user_id,&#10;    event_type,&#10;    value&#10;FROM events.user_events&#10;WHERE event_type = &#x27;CHANGELOG&#x27; or event_type = &#x27;BLOG&#x27;&#10;  AND __ingest_ts &gt; &#x27;2025-09-24T00:00:00Z&#x27;&#10;ORDER BY __ingest_ts DESC&#10;LIMIT 100&quot;&#10;</code></pre>
<p>To get started with R2 SQL, check out our <a href="/r2-sql/get-started/">getting started guide</a> or learn more about supported features in the <a href="/r2-sql/sql-reference/">SQL reference</a>. For a technical deep dive into how we built R2 SQL, read our <a href="https://blog.cloudflare.com/r2-sql-deep-dive/">blog post</a>.</p>


<h2 id="browser-rendering-playwright-ga-stagehand-support-beta-and-higher-limits"><a href="/changelog/post/2025-09-25-br-playwright-ga-stagehand-limits/">Browser Rendering Playwright GA, Stagehand support (Beta), and higher limits</a></h2>
<p><em>2025-09-25T12:00:00+00:00</em></p>
<p>We’re shipping three updates to Browser Rendering:</p>
<ul>
<li>Playwright support is now Generally Available and synced with <a href="https://playwright.dev/docs/release-notes#version-155">Playwright v1.55</a>, giving you a stable foundation for critical automation and AI-agent workflows.</li>
<li>We’re also adding <a href="/browser-run/stagehand/">Stagehand support (Beta)</a> so you can combine code with natural language instructions to build more resilient automations.</li>
<li>Finally, we’ve tripled <a href="/browser-run/limits/#workers-paid">limits</a> for paid plans across both the <a href="/browser-run/quick-actions/">REST API</a> and <a href="/browser-run/#integration-methods">Browser Sessions</a> to help you scale.</li>
</ul>
<p>To get started with Stagehand, refer to the <a href="/browser-run/stagehand/">Stagehand</a> example that uses Stagehand and <a href="/workers-ai/">Workers AI</a> to search for a movie on this <a href="https://demo.playwright.dev/movies">example movie directory</a>, extract its details using natural language (title, year, rating, duration, and genre), and return the information along with a screenshot of the webpage.</p>
<pre><code class="language-ts">const stagehand = new Stagehand({&#10;	env: &quot;LOCAL&quot;,&#10;	localBrowserLaunchOptions: { cdpUrl: endpointURLString(env.BROWSER) },&#10;	llmClient: new WorkersAIClient(env.AI),&#10;	verbose: 1,&#10;});&#10;&#10;await stagehand.init();&#10;const page = stagehand.page;&#10;&#10;await page.goto(&quot;https://demo.playwright.dev/movies&quot;);&#10;&#10;// if search is a multi-step action, stagehand will return an array of actions it needs to act on&#10;const actions = await page.observe(&#x27;Search for &quot;Furiosa&quot;&#x27;);&#10;for (const action of actions) await page.act(action);&#10;&#10;await page.act(&quot;Click the search result&quot;);&#10;&#10;// normal playwright functions work as expected&#10;await page.waitForSelector(&quot;.info-wrapper .cast&quot;);&#10;&#10;let movieInfo = await page.extract({&#10;	instruction: &quot;Extract movie information&quot;,&#10;	schema: z.object({&#10;		title: z.string(),&#10;		year: z.number(),&#10;		rating: z.number(),&#10;		genres: z.array(z.string()),&#10;		duration: z.number().describe(&quot;Duration in minutes&quot;),&#10;	}),&#10;});&#10;&#10;await stagehand.close();&#10;</code></pre>
<p><img src="/images/browser-run/speedystagehand.gif" alt="Stagehand video" /></p>


<h2 id="ai-search-formerly-autorag-now-with-more-models-to-choose-from"><a href="/changelog/post/2025-09-25-ai-search-more-models/">AI Search (formerly AutoRAG) now with More Models To Choose From</a></h2>
<p><em>2025-09-25</em></p>
<p>AutoRAG is now AI Search! The new name marks a new and bigger mission: to make world-class search infrastructure available to every developer and business.</p>
<p>With AI Search you can now use models from different providers like OpenAI and Anthropic. By attaching your provider keys to the AI Gateway linked to your AI Search instance, you can use many more models for both embedding and inference.</p>
<p>To use AI Search with other <a href="/ai-search/configuration/models/">model providers</a>:</p>
<ol>
<li><strong>Add provider keys to AI Gateway</strong>
<ol>
<li>Go to AI &gt; AI Gateway in the dashboard.</li>
<li>Select or create an AI gateway.</li>
<li>In Provider Keys, choose your provider, click Add, and enter the key.</li>
</ol>
</li>
<li><strong>Connect a gateway to AI Search</strong>: When creating a new AI Search, select the AI Gateway with your provider keys. For an existing AI Search, go to Settings and switch to a gateway that has your keys under Resources.</li>
<li><strong>Select models</strong>: Embedding models are only available to be changed when creating a new AI Search. Generation model can be selected when creating a new AI Search and can be changed at any time in Settings.</li>
</ol>
<p>Once configured, your AI Search instance will be able to reference models available through your AI Gateway when making a <code>/ai-search</code> request:</p>
<pre><code class="language-javascript">export default {&#10;  async fetch(request, env) {&#10;    &#10;    // Query your AI Search instance with a natural language question to an OpenAI model&#10;    const result = await env.AI.autorag(&quot;my-ai-search&quot;).aiSearch({&#10;      query: &quot;What&#x27;s new for Cloudflare Birthday Week?&quot;,&#10;      model: &quot;openai/gpt-5&quot;&#10;    });&#10;&#10;    // Return only the generated answer as plain text&#10;    return new Response(result.response, {&#10;      headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;    });&#10;  },&#10;};&#10;</code></pre>
<p>In the coming weeks we will also roll out updates to align the APIs with the new name. The existing APIs will continue to be supported for the time being. Stay tuned to the <a href="/changelog/product/ai-search/">AI Search Changelog</a> and <a href="https://discord.cloudflare.com/">Discord</a> for more updates!</p>


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


<h2 id="r2-data-catalog-now-supports-compaction"><a href="/changelog/post/2025-09-25-data-catalog-compaction/">R2 Data Catalog now supports compaction</a></h2>
<p><em>2025-09-25</em></p>
<p>You can now enable automatic compaction for <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a> to improve query performance.</p>
<p>Compaction is the process of taking a group of small files and combining them into fewer larger files. This is an important maintenance operation as it helps ensure that query performance remains consistent by reducing the number of files that needs to be scanned.</p>
<p>To enable automatic compaction in R2 Data Catalog, find it under <strong>R2 Data Catalog</strong> in your R2 bucket settings in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/r2/compaction.png" alt="compaction-dash" /></p>
<p>Or with <a href="/workers/wrangler/">Wrangler</a>, run:</p>
<pre><code class="language-bash">npx wrangler r2 bucket catalog compaction enable &lt;BUCKET_NAME&gt;  --target-size 128 --token &lt;API_TOKEN&gt;&#10;</code></pre>
<p>To get started with compaction, check out <a href="/r2-data-catalog/manage-catalogs/">manage catalogs</a>. For best practices and limitations, refer to <a href="/r2-data-catalog/table-maintenance/">about compaction</a>.</p>


<h2 id="improved-support-for-running-multiple-workers-with-wrangler-dev"><a href="/changelog/post/2025-09-23-wrangler-dev-multi-config-cross-command-support/">Improved support for running multiple Workers with `wrangler dev`</a></h2>
<p><em>2025-09-23</em></p>
<p>You can run multiple Workers in a single dev command by passing multiple config files to <code>wrangler dev</code>:</p>
<pre><code class="language-sh">wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc&#10;</code></pre>
<p>Previously, if you ran the command above and then also ran wrangler dev for a different Worker, the Workers running in separate wrangler dev sessions could not communicate with each other. This prevented you from being able to use <a href="https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/">Service Bindings</a> and <a href="https://developers.cloudflare.com/workers/observability/logs/tail-workers/">Tail Workers</a> in local development, when running separate wrangler dev sessions.</p>
<p>Now, the following works as expected:</p>
<pre><code class="language-sh">&#35; Terminal 1: Run your application that includes both Web and API workers&#10;wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc&#10;&#10;&#35; Terminal 2: Run your auth worker separately&#10;wrangler dev --config ./auth/wrangler.jsonc&#10;</code></pre>
<p>These Workers can now communicate with each other across separate dev commands, regardless of your development setup.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		// This service binding call now works across dev commands&#10;		const authorized = await env.AUTH.isAuthorized(request);&#10;&#10;		if (!authorized) {&#10;			return new Response(&quot;Unauthorized&quot;, { status: 401 });&#10;		}&#10;&#10;		return new Response(&quot;Hello from API Worker!&quot;, { status: 200 });&#10;	},&#10;};&#10;</code></pre>
<p>Check out the <a href="/workers/local-development/multi-workers">Developing with multiple Workers</a> guide to learn more about the different approaches and when to use each one.</p>


<h2 id="new-metrics-view-in-autorag"><a href="/changelog/post/2025-09-19-autorag-metrics/">New Metrics View in AutoRAG</a></h2>
<p><em>2025-09-19</em></p>
<p><a href="/ai-search/">AutoRAG</a> now includes a <strong>Metrics</strong> tab that shows how your data is indexed and searched. Get a clear view of the health of your indexing pipeline, compare usage between <code>ai-search</code> and <code>search</code>, and see which files are retrieved most often.</p>
<p><img src="/assets/upstream/images/ai-search/metrics.png" alt="Metrics" /></p>
<p>You can find these metrics within each AutoRAG instance:</p>
<ul>
<li>Indexing: Track how files are ingested and see status changes over time.</li>
<li>Search breakdown: Compare usage between <code>ai-search</code> and <code>search</code> endpoints.</li>
<li>Top file retrievals: Identify which files are most frequently retrieved in a given period.</li>
</ul>
<p>Try it today in <a href="/ai-search/get-started/">AutoRAG</a>.</p>


<h2 id="rate-limiting-in-workers-is-now-ga"><a href="/changelog/post/2025-09-19-ratelimit-workers-ga/">Rate Limiting in Workers is now GA</a></h2>
<p><em>2025-09-19</em></p>
<p><a href="/workers/runtime-apis/bindings/rate-limit/">Rate Limiting within Cloudflare Workers</a> is now Generally Available (GA).</p>
<p>The <code>ratelimit</code> binding is now stable and recommended for all production workloads. Existing deployments using the unsafe binding will continue to function to allow for a smooth transition.</p>
<p>For more details, refer to <a href="/workers/runtime-apis/bindings/rate-limit/">Workers Rate Limiting</a> documentation.</p>


<h2 id="panic-recovery-for-rust-workers"><a href="/changelog/post/2025-09-19-workers-rs-panic-recovery/">Panic Recovery for Rust Workers</a></h2>
<p><em>2025-09-19</em></p>
<p>In <a href="https://github.com/cloudflare/workers-rs">workers-rs</a>, Rust panics were previously non-recoverable. A panic would put the Worker into an invalid state, and further function calls could result in memory overflows or exceptions.</p>
<p>Now, when a panic occurs, in-flight requests will throw 500 errors, but the Worker will automatically and instantly recover for future requests.</p>
<p>This ensures more reliable deployments. Automatic panic recovery is enabled for all new workers-rs deployments as of version 0.6.5, with no configuration required.</p>
<h4 id="2025-09-19-workers-rs-panic-recovery-fixing-rust-panics-with-wasm-bindgen">Fixing Rust Panics with Wasm Bindgen</h4>
<p>Rust Workers are built with Wasm Bindgen, which treats panics as non-recoverable. After a panic, the entire Wasm application is considered to be in an invalid state.</p>
<p>We now attach a default panic handler in Rust:</p>
<pre><code class="language-rust">std::panic::set_hook(Box::new(move |panic_info| {&#10;  hook_impl(panic_info);&#10;}));&#10;</code></pre>
<p>Which is registered by default in the JS initialization:</p>
<pre><code class="language-js">import { setPanicHook } from &quot;./index.js&quot;;&#10;setPanicHook(function (err) {&#10;	console.error(&quot;Panic handler!&quot;, err);&#10;});&#10;</code></pre>
<p>When a panic occurs, we reset the Wasm state to revert the Wasm application to how it was when the application started.</p>
<h4 id="2025-09-19-workers-rs-panic-recovery-resetting-vm-state-in-wasm-bindgen">Resetting VM State in Wasm Bindgen</h4>
<p>We worked upstream on the Wasm Bindgen project to implement a new <a href="https://github.com/wasm-bindgen/wasm-bindgen/pull/4644"><code>--experimental-reset-state-function</code> compilation option</a> which outputs a new <code>__wbg_reset_state</code> function.</p>
<p>This function clears all internal state related to the Wasm VM, and updates all function bindings in place to reference the new WebAssembly instance.</p>
<p>One other necessary change here was associating Wasm-created JS objects with an instance identity. If a JS object created by an earlier instance is then passed into a new instance later on, a new &quot;stale object&quot; error is specially thrown when using this feature.</p>
<h4 id="2025-09-19-workers-rs-panic-recovery-layered-solution">Layered Solution</h4>
<p>Building on this new Wasm Bindgen feature, layered with our new default panic handler, we also added a proxy wrapper to ensure all top-level exported class instantiations (such as for Rust Durable Objects) are tracked and fully reinitialized when resetting the Wasm instance. This was necessary because
the workerd runtime will instantiate exported classes, which would then be associated with the Wasm instance.</p>
<p>This approach now provides full panic recovery for Rust Workers on subsequent requests.</p>
<p>Of course, we never want panics, but when they do happen they are isolated and can be investigated further from the error logs - avoiding broader service disruption.</p>
<h4 id="2025-09-19-workers-rs-panic-recovery-webassembly-exception-handling">WebAssembly Exception Handling</h4>
<p>In the future, full support for recoverable panics could be implemented without needing reinitialization at all, utilizing the <a href="https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/Exceptions.md">WebAssembly Exception Handling</a>
proposal, part of the newly announced <a href="https://webassembly.org/news/2025-09-17-wasm-3.0/">WebAssembly 3.0</a> specification. This would allow unwinding panics as normal JS errors, and concurrent requests would no longer fail.</p>
<p><strong>We're making significant improvements to the reliability of <a href="https://github.com/cloudflare/workers-rs">Rust Workers</a>. Join us in <code>#rust-on-workers</code> on the <a href="https://discord.gg/cloudflaredev">Cloudflare Developers Discord</a> to stay updated.</strong></p>


<h2 id="connect-and-secure-any-private-or-public-app-by-hostname-not-ip-with-hostname-routing-for-cloudflare-tunnel"><a href="/changelog/post/2025-09-18-tunnel-hostname-routing/">Connect and secure any private or public app by hostname, not IP — with hostname routing for Cloudflare Tunnel</a></h2>
<p><em>2025-09-18</em></p>
<p>You can now route private traffic to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> based on a hostname or domain, moving beyond the limitations of IP-based routing. This new capability is <strong>free for all Cloudflare One customers</strong>.</p>
<p>Previously, Tunnel routes could only be defined by IP address or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">CIDR range</a>. This created a challenge for modern applications with dynamic or ephemeral IP addresses, often forcing administrators to maintain complex and brittle IP lists.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/tunnel-hostname-routing.webp" alt="Hostname-based routing in Cloudflare Tunnel" /></p>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>Hostname &amp; Domain Routing</strong>: Create routes for individual hostnames (e.g., <code>payroll.acme.local</code>) or entire domains (e.g., <code>*.acme.local</code>) and direct their traffic to a specific Tunnel.</li>
<li><strong>Simplified Zero Trust Policies</strong>: Build resilient policies in Cloudflare Access and Gateway using stable hostnames, making it dramatically easier to apply per-resource authorization for your private applications.</li>
<li><strong>Precise Egress Control</strong>: Route traffic for public hostnames (e.g., <code>bank.example.com</code>) through a specific Tunnel to enforce a dedicated source IP, solving the IP allowlist problem for third-party services.</li>
<li><strong>No More IP Lists</strong>: This feature makes the workaround of maintaining dynamic IP Lists for Tunnel connections obsolete.</li>
</ul>
<p>Get started in the Tunnels section of the Zero Trust dashboard with your first <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostname</a> or <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public hostname</a> route.</p>
<p>Learn more in our <a href="https://blog.cloudflare.com/tunnel-hostname-routing/">blog post</a>.</p>


<h2 id="increased-vcpu-for-workers-builds-on-paid-plans"><a href="/changelog/post/2025-09-07-builds-increased-cpu-paid/">Increased vCPU for Workers Builds on paid plans</a></h2>
<p><em>2025-09-18</em></p>
<p>We recently <a href="/changelog/2025-08-04-builds-increased-disk-size/">increased the available disk space</a> from 8 GB to 20 GB for <strong>all</strong> plans. Building on that improvement, we’re now doubling the CPU power available for paid plans — from 2 vCPU to <strong>4 vCPU</strong>.</p>
<p>These changes continue our focus on making <a href="/workers/ci-cd/builds/">Workers Builds</a> faster and more reliable.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Free Plan</th>
<th>Paid Plans</th>
</tr>
</thead>
<tbody>
<tr>
<td>CPU</td>
<td>2 vCPU</td>
<td><strong>4 vCPU</strong></td>
</tr>
</tbody>
</table>
<h4 id="2025-09-07-builds-increased-cpu-paid-performance-improvements">Performance Improvements</h4>
- **Fast build times**: Even single-threaded workloads benefit from having more vCPUs 
- **2x faster multi-threaded builds**: Tools like [esbuild](https://esbuild.github.io/) and [webpack](https://webpack.js.org/) can now utilize additional cores, delivering near-linear performance scaling
<p>All other <a href="/workers/ci-cd/builds/limits-and-pricing/">build limits</a> — including memory, build minutes, and timeout remain unchanged.</p>


<h2 id="preview-urls-now-default-to-opt-in"><a href="/changelog/post/2025-09-17-update-preview-url-setting/">Preview URLs now default to opt-in</a></h2>
<p><em>2025-09-17</em></p>
<p>To prevent the accidental exposure of applications, we've updated how <a href="/workers/versions-and-deployments/preview-urls/">Worker preview URLs</a> (<code>&lt;PREVIEW&gt;-&lt;WORKER_NAME&gt;.&lt;SUBDOMAIN&gt;.workers.dev</code>) are handled. We made this change to ensure preview URLs are only active when intentionally configured, improving the default security posture of your Workers.</p>
<h4 id="2025-09-17-update-preview-url-setting-one-time-update-for-workers-with-workers-dev-disabled">One-Time Update for Workers with workers.dev Disabled</h4>
We performed a one-time update to disable preview URLs for existing Workers where the [workers.dev subdomain](/workers/configuration/routing/workers-dev/) was also disabled.
<p>Because preview URLs were historically enabled by default, users who had intentionally disabled their workers.dev route may not have realized their Worker was still accessible at a separate preview URL. This update was performed to ensure that using a preview URL is always an intentional, opt-in choice.</p>
<p>If your Worker was affected, its preview URL (<code>&lt;PREVIEW&gt;-&lt;WORKER_NAME&gt;.&lt;SUBDOMAIN&gt;.workers.dev</code>) will now direct to an informational page explaining this change.</p>
<p><strong>How to Re-enable Your Preview URL</strong></p>
<p>If your preview URL was disabled, you can re-enable it <a href="/workers/versions-and-deployments/preview-urls/#toggle-preview-urls-enable-or-disable">via the Cloudflare dashboard</a> by navigating to your Worker's Settings page and toggling on the Preview URL.</p>
<p>Alternatively, you can use Wrangler by adding the <code>preview_urls = true</code> setting to your Wrangler file and redeploying the Worker.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17788.md")</div>
<p><strong>Note:</strong> You can set <code>preview_urls = true</code> with any Wrangler version that supports the preview URL flag (v3.91.0+). However, we recommend updating to v4.34.0 or newer, as this version defaults <code>preview_urls</code> to false, ensuring preview URLs are always enabled by explicit choice.</p>


<h2 id="remote-bindings-ga-connect-to-remote-resources-d1-kv-r2-etc-during-local-development"><a href="/changelog/post/2025-09-16-remote-bindings-ga/">Remote bindings GA - Connect to remote resources (D1, KV, R2, etc.) during local development</a></h2>
<p><em>2025-09-16</em></p>
<p>Three months ago <a href="/changelog/2025-06-18-remote-bindings-beta/">we announced the public beta</a> of <a href="/workers/local-development/#remote-bindings">remote bindings</a> for local development. Now, we're excited to say that it's available for everyone in Wrangler, Vite, and Vitest without using an experimental flag!</p>
<p>With remote bindings, you can now connect to deployed resources like <a href="/r2/">R2 buckets</a> and <a href="/d1/">D1 databases</a> while running Worker code on your local machine. This means you can test your local code changes against real data and services, without the overhead of deploying for each iteration.</p>
<h4 id="2025-09-16-remote-bindings-ga-example-configuration">Example configuration</h4>
<p>To enable remote bindings, add <code>&quot;remote&quot; : true</code> to each binding that you want to rely on a remote resource running on Cloudflare:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17787.md")</div>
<p>When remote bindings are configured, your Worker <strong>still executes locally</strong>, but all binding calls are proxied to the deployed resource that runs on Cloudflare's network.</p>
<p><strong>You can <a href="/workers/local-development/#remote-bindings">try out remote bindings</a> for local development today with:</strong></p>
<ul>
<li><a href="/workers/wrangler/">Wrangler v4.37.0</a></li>
<li>The <a href="/workers/vite-plugin/">Cloudflare Vite Plugin</a></li>
<li>The <a href="/workers/testing/vitest-integration/">Cloudflare Vitest Plugin</a></li>
</ul>


<h2 id="d1-automatically-retries-read-only-queries"><a href="/changelog/post/2025-09-11-d1-automatic-read-retries/">D1 automatically retries read-only queries</a></h2>
<p><em>2025-09-11</em></p>
<p>D1 now detects read-only queries and automatically attempts up to two retries to execute those queries in the event of failures with retryable errors. You can access the number of execution attempts in the returned <a href="/d1/worker-api/return-object/#d1result">response metadata</a> property <code>total_attempts</code>.</p>
<p>At the moment, only read-only queries are retried, that is, queries containing only the following SQLite keywords: <code>SELECT</code>, <code>EXPLAIN</code>, <code>WITH</code>. Queries containing any <a href="https://sqlite.org/lang_keywords.html">SQLite keyword</a> that leads to database writes are not retried.</p>
<p>The retry success ratio among read-only retryable errors varies from 5% all the way up to 95%, depending on the underlying error and its duration (like network errors or other internal errors).</p>
<p>The retry success ratio among all retryable errors is lower, indicating that there are write-queries that could be retried. Therefore, we recommend D1 users to continue applying <a href="/d1/best-practices/retry-queries/">retries in their own code</a> for queries that are not read-only but are idempotent according to the business logic of the application.</p>
<p><img src="/assets/upstream/images/changelog/d1/d1-auto-retry-success-ratio.png" alt="D1 automatically query retries success ratio" /></p>
<p>D1 ensures that any retry attempt does not cause database writes, making the automatic retries safe from side-effects, even if a query causing changes slips through the read-only detection. D1 achieves this by checking for modifications after every query execution, and if any write occurred due to a retry attempt, the query is rolled back.</p>
<p>The read-only query detection heuristics are simple for now, and there is room for improvement to capture more cases of queries that can be retried, so this is just the beginning.</p>


<h2 id="worker-version-rollback-limit-increased-from-10-to-100"><a href="/changelog/post/2025-09-11-increased-version-rollback-limit/">Worker version rollback limit increased from 10 to 100</a></h2>
<p><em>2025-09-11</em></p>
<p>The number of recent versions available for a Worker rollback has been increased from 10 to 100.</p>
<p>This allows you to:</p>
<ul>
<li>
<p>Promote any of the 100 most recent versions to be the active deployment.</p>
</li>
<li>
<p>Split traffic using <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployments</a> between your latest code and any of the 100 most recent versions.</p>
</li>
</ul>
<p>You can do this through the Cloudflare dashboard or with <a href="/workers/wrangler/commands/general/#rollback">Wrangler's rollback command</a></p>
<p>Learn more about <a href="/workers/versions-and-deployments/">versioned deployments</a> and <a href="/workers/versions-and-deployments/rollbacks/">rollbacks</a>.</p>


<h2 id="agents-sdk-v0-1-0-and-workers-ai-provider-v2-0-0-with-ai-sdk-v5-support"><a href="/changelog/post/2025-09-03-agents-sdk-beta-v5/">Agents SDK v0.1.0 and workers-ai-provider v2.0.0 with AI SDK v5 support</a></h2>
<p><em>2025-09-10</em></p>
<p>We've shipped a new release for the <a href="https://github.com/cloudflare/agents">Agents SDK</a> bringing full compatibility with <a href="https://ai-sdk.dev/docs/introduction">AI SDK v5</a> and introducing automatic message migration that handles all legacy formats transparently.</p>
<p>This release includes improved streaming and tool support, tool confirmation detection (for &quot;human in the loop&quot; systems), enhanced React hooks with automatic tool resolution, improved error handling for streaming responses, and seamless migration utilities that work behind the scenes.</p>
<p>This makes it ideal for building production AI chat interfaces with Cloudflare Workers AI models, agent workflows, human-in-the-loop systems, or any application requiring reliable message handling across SDK versions — all while maintaining backward compatibility.</p>
<p>Additionally, we've updated workers-ai-provider v2.0.0, the official provider for Cloudflare Workers AI models, to be compatible with AI SDK v5.</p>
<h4 id="2025-09-03-agents-sdk-beta-v5-useagentchat-options">useAgentChat(options)</h4>
<p>Creates a new chat interface with enhanced v5 capabilities.</p>
<pre><code class="language-ts">// Basic chat setup&#10;const { messages, sendMessage, addToolResult } = useAgentChat({&#10;	agent,&#10;	experimental_automaticToolResolution: true,&#10;	tools,&#10;});&#10;&#10;// With custom tool confirmation&#10;const chat = useAgentChat({&#10;	agent,&#10;	experimental_automaticToolResolution: true,&#10;	toolsRequiringConfirmation: [&quot;dangerousOperation&quot;],&#10;});&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-automatic-tool-resolution">Automatic Tool Resolution</h4>
<p>Tools are automatically categorized based on their configuration:</p>
<pre><code class="language-ts">const tools = {&#10;	// Auto-executes (has execute function)&#10;	getLocalTime: {&#10;		description: &quot;Get current local time&quot;,&#10;		inputSchema: z.object({}),&#10;		execute: async () =&gt; new Date().toLocaleString(),&#10;	},&#10;&#10;	// Requires confirmation (no execute function)&#10;	deleteFile: {&#10;		description: &quot;Delete a file from the system&quot;,&#10;		inputSchema: z.object({&#10;			filename: z.string(),&#10;		}),&#10;	},&#10;&#10;	// Server-executed (no client confirmation)&#10;	analyzeData: {&#10;		description: &quot;Analyze dataset on server&quot;,&#10;		inputSchema: z.object({ data: z.array(z.number()) }),&#10;		serverExecuted: true,&#10;	},&#10;} satisfies Record&lt;string, AITool&gt;;&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-message-handling">Message Handling</h4>
<p>Send messages using the new v5 format with parts array:</p>
<pre><code class="language-ts">// Text message&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [{ type: &quot;text&quot;, text: &quot;Hello, assistant!&quot; }],&#10;});&#10;&#10;// Multi-part message with file&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{ type: &quot;image&quot;, image: imageData },&#10;	],&#10;});&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-tool-confirmation-detection">Tool Confirmation Detection</h4>
<p>Simplified logic for detecting pending tool confirmations:</p>
<pre><code class="language-ts">const pendingToolCallConfirmation = messages.some((m) =&gt;&#10;	m.parts?.some(&#10;		(part) =&gt; isToolUIPart(part) &amp;&amp; part.state === &quot;input-available&quot;,&#10;	),&#10;);&#10;&#10;// Handle tool confirmation&#10;if (pendingToolCallConfirmation) {&#10;	await addToolResult({&#10;		toolCallId: part.toolCallId,&#10;		tool: getToolName(part),&#10;		output: &quot;User approved the action&quot;,&#10;	});&#10;}&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-automatic-message-migration">Automatic Message Migration</h4>
<p>Seamlessly handle legacy message formats without code changes.</p>
<pre><code class="language-ts">// All these formats are automatically converted:&#10;&#10;// Legacy v4 string content&#10;const legacyMessage = {&#10;	role: &quot;user&quot;,&#10;	content: &quot;Hello world&quot;,&#10;};&#10;&#10;// Legacy v4 with tool calls&#10;const legacyWithTools = {&#10;	role: &quot;assistant&quot;,&#10;	content: &quot;&quot;,&#10;	toolInvocations: [&#10;		{&#10;			toolCallId: &quot;123&quot;,&#10;			toolName: &quot;weather&quot;,&#10;			args: { city: &quot;SF&quot; },&#10;			state: &quot;result&quot;,&#10;			result: &quot;Sunny, 72°F&quot;,&#10;		},&#10;	],&#10;};&#10;&#10;// Automatically becomes v5 format:&#10;// {&#10;//   role: &quot;assistant&quot;,&#10;//   parts: [{&#10;//     type: &quot;tool-call&quot;,&#10;//     toolCallId: &quot;123&quot;,&#10;//     toolName: &quot;weather&quot;,&#10;//     args: { city: &quot;SF&quot; },&#10;//     state: &quot;result&quot;,&#10;//     result: &quot;Sunny, 72°F&quot;&#10;//   }]&#10;// }&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-tool-definition-updates">Tool Definition Updates</h4>
<p>Migrate tool definitions to use the new <code>inputSchema</code> property.</p>
<pre><code class="language-ts">// Before (AI SDK v4)&#10;const tools = {&#10;	weather: {&#10;		description: &quot;Get weather information&quot;,&#10;		parameters: z.object({&#10;			city: z.string(),&#10;		}),&#10;		execute: async (args) =&gt; {&#10;			return await getWeather(args.city);&#10;		},&#10;	},&#10;};&#10;&#10;// After (AI SDK v5)&#10;const tools = {&#10;	weather: {&#10;		description: &quot;Get weather information&quot;,&#10;		inputSchema: z.object({&#10;			city: z.string(),&#10;		}),&#10;		execute: async (args) =&gt; {&#10;			return await getWeather(args.city);&#10;		},&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-cloudflare-workers-ai-integration">Cloudflare Workers AI Integration</h4>
<p>Seamless integration with Cloudflare Workers AI models through the updated workers-ai-provider v2.0.0.</p>
<h4 id="2025-09-03-agents-sdk-beta-v5-model-setup-with-workers-ai">Model Setup with Workers AI</h4>
<p>Use Cloudflare Workers AI models directly in your agent workflows:</p>
<pre><code class="language-ts">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import { useAgentChat } from &quot;agents/ai-react&quot;;&#10;&#10;// Create Workers AI model (v2.0.0 - same API, enhanced v5 internals)&#10;const model = createWorkersAI({&#10;	binding: env.AI,&#10;})(&quot;@cf/meta/llama-3.2-3b-instruct&quot;);&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-enhanced-file-and-image-support">Enhanced File and Image Support</h4>
<p>Workers AI models now support v5 file handling with automatic conversion:</p>
<pre><code class="language-ts">// Send images and files to Workers AI models&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{&#10;			type: &quot;file&quot;,&#10;			data: imageBuffer,&#10;			mediaType: &quot;image/jpeg&quot;,&#10;		},&#10;	],&#10;});&#10;&#10;// Workers AI provider automatically converts to proper format&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-streaming-with-workers-ai">Streaming with Workers AI</h4>
<p>Enhanced streaming support with automatic warning detection:</p>
<pre><code class="language-ts">// Streaming with Workers AI models&#10;const result = await streamText({&#10;	model: createWorkersAI({ binding: env.AI })(&quot;@cf/meta/llama-3.2-3b-instruct&quot;),&#10;	messages,&#10;	onChunk: (chunk) =&gt; {&#10;		// Enhanced streaming with warning handling&#10;		console.log(chunk);&#10;	},&#10;});&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-import-updates">Import Updates</h4>
<p>Update your imports to use the new v5 types:</p>
<pre><code class="language-ts">// Before (AI SDK v4)&#10;import type { Message } from &quot;ai&quot;;&#10;import { useChat } from &quot;ai/react&quot;;&#10;&#10;// After (AI SDK v5)&#10;import type { UIMessage } from &quot;ai&quot;;&#10;// or alias for compatibility&#10;import type { UIMessage as Message } from &quot;ai&quot;;&#10;import { useChat } from &quot;@ai-sdk/react&quot;;&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-resources">Resources</h4>
<ul>
<li><a href="https://github.com/cloudflare/agents/blob/main/docs/migration-to-ai-sdk-v5.md">Migration Guide</a> - Comprehensive migration documentation</li>
<li><a href="https://ai-sdk.dev/docs/migration-guides/migration-guide-5-0">AI SDK v5 Documentation</a> - Official AI SDK migration guide</li>
<li><a href="https://github.com/cloudflare/agents-starter/pull/105">An Example PR showing the migration from AI SDK v4 to v5</a></li>
<li><a href="https://github.com/cloudflare/agents/issues">GitHub Issues</a> - Report bugs or request features</li>
</ul>
<h4 id="2025-09-03-agents-sdk-beta-v5-feedback-welcome">Feedback Welcome</h4>
<p>We'd love your feedback! We're particularly interested in feedback on:</p>
<ul>
<li><strong>Migration experience</strong> - How smooth was the upgrade process?</li>
<li><strong>Tool confirmation workflow</strong> - Does the new automatic detection work as expected?</li>
<li><strong>Message format handling</strong> - Any edge cases with legacy message conversion?</li>
</ul>


<h2 id="built-with-cloudflare-button"><a href="/changelog/post/2025-09-10-built-with-cloudflare-button/">Built with Cloudflare button</a></h2>
<p><em>2025-09-10</em></p>
<p>We've updated our &quot;Built with Cloudflare&quot; button to make it easier to share that you're building on Cloudflare with the world. Embed it in your project's README, blog post, or wherever you want to let people know.</p>
<p><img src="https://workers.cloudflare.com/built-with-cloudflare.svg" alt="Built with Cloudflare" /></p>
<p>Check out the <a href="/workers/platform/built-with-cloudflare">documentation</a> for usage information.</p>


<h2 id="deploy-static-sites-to-workers-without-a-configuration-file"><a href="/changelog/post/2025-09-09-interactive-wrangler-assets/">Deploy static sites to Workers without a configuration file</a></h2>
<p><em>2025-09-09</em></p>
<p>Deploying static site to Workers is now easier. When you run <code>wrangler deploy [directory]</code> or <code>wrangler deploy --assets [directory]</code> without an existing <a href="/workers/wrangler/configuration/">configuration file</a>, <a href="/workers/wrangler/">Wrangler CLI</a> now guides you through the deployment process with interactive prompts.</p>
<h4 id="2025-09-09-interactive-wrangler-assets-before-and-after">Before and after</h4>
<p><strong>Before:</strong> Required remembering multiple flags and parameters</p>
<pre><code class="language-bash">wrangler deploy --assets ./dist --compatibility-date 2025-09-09 --name my-project&#10;</code></pre>
<p><strong>After:</strong> Simple directory deployment with guided setup</p>
<pre><code class="language-bash">wrangler deploy dist&#10;&#35; Interactive prompts handle the rest as shown in the example flow below&#10;</code></pre>
<h4 id="2025-09-09-interactive-wrangler-assets-what-s-new">What's new</h4>
<p><strong>Interactive prompts for missing configuration:</strong></p>
<ul>
<li>Wrangler detects when you're trying to deploy a directory of static assets</li>
<li>Prompts you to confirm the deployment type</li>
<li>Asks for a project name (with smart defaults)</li>
<li>Automatically sets the compatibility date to today</li>
</ul>
<p><strong>Automatic configuration generation:</strong></p>
<ul>
<li>Creates a <code>wrangler.jsonc</code> file with your deployment settings</li>
<li>Stores your choices for future deployments</li>
<li>Eliminates the need to remember complex command-line flags</li>
</ul>
<h4 id="2025-09-09-interactive-wrangler-assets-example-workflow">Example workflow</h4>
<pre><code class="language-bash">&#35; Deploy your built static site&#10;wrangler deploy dist&#10;&#10;&#35; Wrangler will prompt:&#10;✔ It looks like you are trying to deploy a directory of static assets only. Is this correct? … yes&#10;✔ What do you want to name your project? … my-astro-site&#10;&#10;&#35; Automatically generates a wrangler.jsonc file and adds it to your project:&#10;{&#10;  &quot;name&quot;: &quot;my-astro-site&quot;,&#10;  &quot;compatibility_date&quot;: &quot;2025-09-09&quot;,&#10;  &quot;assets&quot;: {&#10;    &quot;directory&quot;: &quot;dist&quot;&#10;  }&#10;}&#10;&#10;&#35; Next time you run wrangler deploy, this will use the configuration in your newly generated wrangler.jsonc file&#10;wrangler deploy&#10;</code></pre>
<h4 id="2025-09-09-interactive-wrangler-assets-requirements">Requirements</h4>
<ul>
<li>You must use Wrangler version 4.24.4 or later in order to use this feature</li>
</ul>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/15/">Previous</a><span>Page 16 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/17/">Next</a></nav>
