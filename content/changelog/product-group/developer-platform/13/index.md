---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/developer-platform/13/
  description: '2026-02-09'
  full_title: Developer platform changelog - page 13 | Cloudflare Docs
  head_html: <title>Developer platform changelog - page 13 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-02-09"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/developer-platform/13/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Developer platform changelog - page 13"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-02-09"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/developer-platform/13/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/developer-platform/13/#page","headline":"Developer platform changelog - page 13 | Cloudflare Docs","description":"2026-02-09","url":"https://developers.cloudflare.com/changelog/product-group/developer-platform/13/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/developer-platform/13/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="ai-search-now-with-more-granular-controls-over-indexing"><a href="/changelog/post/2026-02-09-indexing-improvements/">AI Search now with more granular controls over indexing</a></h2>
<p><em>2026-02-09</em></p>
<p>Get your content updates into <a href="/ai-search/">AI Search</a> faster and avoid a full rescan when you do not need it.</p>
<h4 id="2026-02-09-indexing-improvements-reindex-individual-files-without-a-full-sync">Reindex individual files without a full sync</h4>
<p>Updated a file or need to retry one that errored? When you know exactly which file changed, you can now <a href="/ai-search/configuration/indexing/syncing/#controls">reindex it directly</a> instead of rescanning your entire data source.</p>
<p>Go to <strong>Overview</strong> &gt; <strong>Indexed Items</strong> and select the sync icon next to any file to reindex it immediately.</p>
<p><img src="/assets/upstream/images/ai-search/individual-file-indexing.png" alt="Sync individual files from Indexed Items" /></p>
<h4 id="2026-02-09-indexing-improvements-crawl-only-the-sitemap-you-need">Crawl only the sitemap you need</h4>
<p>By default, AI Search crawls all sitemaps listed in your <code>robots.txt</code>, up to the <a href="/ai-search/platform/limits-pricing/#limits">maximum files per index limit</a>. If your site has multiple sitemaps but you only want to index a specific set, you can now <a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">specify a single sitemap URL</a> to limit what the crawler visits.</p>
<p>For example, if your <code>robots.txt</code> lists both <code>blog-sitemap.xml</code> and <code>docs-sitemap.xml</code>, you can specify just <code>https://example.com/docs-sitemap.xml</code> to index only your documentation.</p>
<p>Configure your selection anytime in <strong>Settings</strong> &gt; <strong>Parsing options</strong> &gt; <strong>Specific sitemaps</strong>, then trigger a sync to apply the changes.</p>
<p><img src="/assets/upstream/images/ai-search/specify-sitemap.png" alt="Specify a sitemap in Parsinh options" /></p>
<p>Learn more about <a href="/ai-search/configuration/indexing/syncing/#controls">indexing controls</a> and <a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">website crawling configuration</a>.</p>


<h2 id="r2-sql-now-supports-approximate-aggregation-functions"><a href="/changelog/post/2026-02-09-approximate-aggregation-functions/">R2 SQL now supports approximate aggregation functions</a></h2>
<p><em>2026-02-09</em></p>
<p>R2 SQL now supports five approximate aggregation functions for fast analysis of large datasets. These functions trade minor precision for improved performance on high-cardinality data.</p>
<h4 id="2026-02-09-approximate-aggregation-functions-new-functions">New functions</h4>
<ul>
<li><code>APPROX_PERCENTILE_CONT(column, percentile)</code> — Returns the approximate value at a given percentile (0.0 to 1.0). Works on integer and decimal columns.</li>
<li><code>APPROX_PERCENTILE_CONT_WITH_WEIGHT(column, weight, percentile)</code> — Weighted percentile calculation where each row contributes proportionally to its weight column value.</li>
<li><code>APPROX_MEDIAN(column)</code> — Returns the approximate median. Equivalent to <code>APPROX_PERCENTILE_CONT(column, 0.5)</code>.</li>
<li><code>APPROX_DISTINCT(column)</code> — Returns the approximate number of distinct values. Works on any column type.</li>
<li><code>APPROX_TOP_K(column, k)</code> — Returns the <code>k</code> most frequent values with their counts as a JSON array.</li>
</ul>
<p>All functions support <code>WHERE</code> filters. All except <code>APPROX_TOP_K</code> support <code>GROUP BY</code>.</p>
<h4 id="2026-02-09-approximate-aggregation-functions-examples">Examples</h4>
<pre tabindex="0"><code class="language-sql">&#45;- Percentile analysis on revenue data&#10;SELECT approx_percentile_cont(total_amount, 0.25),&#10;       approx_percentile_cont(total_amount, 0.5),&#10;       approx_percentile_cont(total_amount, 0.75)&#10;FROM my_namespace.sales_data&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Median per department&#10;SELECT department, approx_median(total_amount)&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Approximate distinct customers by region&#10;SELECT region, approx_distinct(customer_id)&#10;FROM my_namespace.sales_data&#10;GROUP BY region&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Top 5 most frequent departments&#10;SELECT approx_top_k(department, 5)&#10;FROM my_namespace.sales_data&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Combine approximate and standard aggregations&#10;SELECT COUNT(*),&#10;       AVG(total_amount),&#10;       approx_percentile_cont(total_amount, 0.5),&#10;       approx_distinct(customer_id)&#10;FROM my_namespace.sales_data&#10;WHERE region = &#x27;North&#x27;&#10;</code></pre>
<p>For the full syntax and additional examples, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>.</p>


<h2 id="visualize-data-share-links-and-create-exports-with-the-new-workers-observability-dashboard"><a href="/changelog/post/2026-02-06-observability-ui-refresh/">Visualize data, share links, and create exports with the new Workers Observability dashboard</a></h2>
<p><em>2026-02-06</em></p>
<p>The <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/">Workers Observability dashboard</a> has some major updates to make it easier to debug your application's issues and share findings with your team.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-01-22-events_share_obs_wobs.png" alt="Workers Observability dashboard showing events view with event details and share options" /></p>
<p>You can now:</p>
<ul>
<li><strong>Create visualizations</strong> — Build charts from your Worker data directly in a Worker's Observability tab</li>
<li><strong>Export data as JSON or CSV</strong> — Download logs and traces for offline analysis or to share with teammates</li>
<li><strong>Share events and traces</strong> — Generate direct URLs to specific events, invocations, and traces that open standalone pages with full context</li>
<li><strong>Customize table columns</strong> — Improved field picker to add, remove, and reorder columns in the events table</li>
<li><strong>Expandable event details</strong> — Expand events inline to view full details without leaving the table</li>
<li><strong>Keyboard shortcuts</strong> — Navigate the dashboard with hotkey support</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-01-22-vis_qb_wobs.png" alt="Workers Observability dashboard showing a P99 CPU time visualization grouped by outcome" /></p>
<p>These updates are now live in the Cloudflare dashboard, both in a Worker's Observability tab and in the account-level Observability dashboard for a unified experience. To get started, go to <strong>Workers &amp; Pages</strong> &gt; select your Worker &gt; <strong>Observability</strong>.</p>


<h2 id="cloudflare-queues-now-available-on-workers-free-plan"><a href="/changelog/post/2026-02-04-queues-free-plan/">Cloudflare Queues now available on Workers Free plan</a></h2>
<p><em>2026-02-04</em></p>
<p><a href="/queues">Cloudflare Queues</a> is now part of the Workers free plan, offering guaranteed message delivery across up to <strong>10,000 queues</strong> to either <a href="/workers">Cloudflare Workers</a> or <a href="/queues/configuration/pull-consumers">HTTP pull consumers</a>. Every Cloudflare account now includes <strong>10,000 operations per day</strong> across reads, writes, and deletes. For more details on how each operation is defined, refer to <a href="https://developers.cloudflare.com/workers/platform/pricing/#queues">Queues pricing</a>.</p>
<p>All features of the existing Queues functionality are available on the free plan, including unlimited <a href="/queues/event-subscriptions/">event subscriptions</a>. Note that the maximum retention period on the free tier, however, is 24 hours rather than 14 days.</p>
<p>If you are new to Cloudflare Queues, follow <a href="https://developers.cloudflare.com/queues/get-started/">this guide</a> or try one of our <a href="/queues/tutorials/">tutorials</a> to get started.</p>


<h2 id="visualize-your-workflows-in-the-cloudflare-dashboard"><a href="/changelog/post/2026-02-03-workflows-visualizer/">Visualize your Workflows in the Cloudflare dashboard</a></h2>
<p><em>2026-02-04</em></p>
<p>Cloudflare Workflows now automatically generates visual diagrams from your code</p>
<p>Your Workflow is parsed to provide a visual map of the Workflow structure, allowing you to:</p>
<ul>
<li>Understand how steps connect and execute</li>
<li>Visualize loops and nested logic</li>
<li>Follow branching paths for conditional logic</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workflows/2026-02-03-workflows-diagram.png" alt="Example diagram" /></p>
<p>You can collapse loops and nested logic to see the high-level flow, or expand them to see every step.</p>
<p>Workflow diagrams are available in beta for all JavaScript and TypeScript Workflows. Find your Workflows in the <a href="https://dash.cloudflare.com/?to=/:account/workers/workflows">Cloudflare dashboard</a> to see their diagrams.</p>


<h2 id="agents-sdk-v0-3-7-workflows-integration-synchronous-state-and-scheduleevery"><a href="/changelog/post/2026-02-03-agents-workflows-integration/">Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery()</a></h2>
<p><em>2026-02-03</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings first-class support for <a href="/workflows/">Cloudflare Workflows</a>, synchronous state management, and new scheduling capabilities.</p>
<h4 id="2026-02-03-agents-workflows-integration-cloudflare-workflows-integration">Cloudflare Workflows integration</h4>
<p>Agents excel at real-time communication and state management. Workflows excel at durable execution. Together, they enable powerful patterns where Agents handle WebSocket connections while Workflows handle long-running tasks, retries, and human-in-the-loop flows.</p>
<p>Use the new <code>AgentWorkflow</code> class to define workflows with typed access to your Agent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17624.md")</div>
<p>Start workflows from your Agent with <code>runWorkflow()</code> and handle lifecycle events:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17625.md")</div>
<p>Key workflow methods on your Agent:</p>
<ul>
<li><code>runWorkflow(workflowName, params, options?)</code> — Start a workflow with optional metadata</li>
<li><code>getWorkflow(workflowId)</code> / <code>getWorkflows(criteria?)</code> — Query workflows with cursor-based pagination</li>
<li><code>approveWorkflow(workflowId)</code> / <code>rejectWorkflow(workflowId)</code> — Human-in-the-loop approval flows</li>
<li><code>pauseWorkflow()</code>, <code>resumeWorkflow()</code>, <code>terminateWorkflow()</code> — Workflow control</li>
</ul>
<h4 id="2026-02-03-agents-workflows-integration-synchronous-setstate">Synchronous setState()</h4>
<p>State updates are now synchronous with a new <code>validateStateChange()</code> validation hook:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17626.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-scheduleevery-for-recurring-tasks">scheduleEvery() for recurring tasks</h4>
<p>The new <code>scheduleEvery()</code> method enables fixed-interval recurring tasks with built-in overlap prevention:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17627.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-callable-system-improvements">Callable system improvements</h4>
<ul>
<li><strong>Client-side RPC timeout</strong> — Set timeouts on callable method invocations</li>
<li><strong><code>StreamingResponse.error(message)</code></strong> — Graceful stream error signaling</li>
<li><strong><code>getCallableMethods()</code></strong> — Introspection API for discovering callable methods</li>
<li><strong>Connection close handling</strong> — Pending calls are automatically rejected on disconnect</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17628.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-email-and-routing-enhancements">Email and routing enhancements</h4>
<p><strong>Secure email reply routing</strong> — Email replies are now secured with HMAC-SHA256 signed headers, preventing unauthorized routing of emails to agent instances.</p>
<p><strong>Routing improvements:</strong></p>
<ul>
<li><code>basePath</code> option to bypass default URL construction for custom routing</li>
<li>Server-sent identity — Agents send <code>name</code> and <code>agent</code> type on connect</li>
<li>New <code>onIdentity</code> and <code>onIdentityChange</code> callbacks on the client</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17629.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest&#10;</code></pre>
<p>For the complete Workflows API reference and patterns, see <a href="/agents/runtime/execution/run-workflows/">Run Workflows</a>.</p>


<h2 id="improve-global-upload-performance-with-r2-local-uploads-now-in-open-beta"><a href="/changelog/post/2026-02-03-r2-local-uploads/">Improve Global Upload Performance with R2 Local Uploads - Now in Open Beta</a></h2>
<p><em>2026-02-03</em></p>
<p><a href="/r2/buckets/local-uploads/">Local Uploads</a> is now available in open beta. Enable it on your <a href="/r2/">R2</a> bucket to improve upload performance when clients upload data from a different region than your bucket. With Local Uploads enabled, object data is written to storage infrastructure near the client, then asynchronously replicated to your bucket. The object is immediately accessible and remains strongly consistent throughout. Refer to <a href="/r2/how-r2-works/">How R2 works</a> for details on how data is written to your bucket.</p>
<p>In our tests, we observed <strong>up to 75% reduction in Time to Last Byte (TTLB)</strong> for upload requests when Local Uploads is enabled.</p>
<p><img src="/assets/upstream/images/r2/local-uploads-latency.png" alt="Local Uploads latency comparison showing p50 TTLB dropping from around 2 seconds to 500ms after enabling Local Uploads" /></p>
<p>This feature is ideal when:</p>
<ul>
<li>Your users are globally distributed</li>
<li>Upload performance and reliability is critical to your application</li>
<li>You want to optimize write performance without changing your bucket's primary location</li>
</ul>
<p>To enable Local Uploads on your bucket, find <strong>Local Uploads</strong> in your bucket settings in the <a href="https://dash.cloudflare.com/?to=/:account/r2/overview">Cloudflare Dashboard</a>, or run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket local-uploads enable &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>Enabling Local Uploads on a bucket is seamless: existing uploads will complete as expected and there’s no interruption to traffic. There is no additional cost to enable Local Uploads. Upload requests incur the standard <a href="/r2/pricing/">Class A operation costs</a> same as upload requests made without Local Uploads.</p>
<p>For more information, refer to <a href="/r2/buckets/local-uploads/">Local Uploads</a>.</p>


<h2 id="reduced-minimum-cache-ttl-for-workers-kv-to-30-seconds"><a href="/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/">Reduced minimum cache TTL for Workers KV to 30 seconds</a></h2>
<p><em>2026-01-30T12:00:00+00:00</em></p>
<p>The minimum <code>cacheTtl</code> parameter for Workers KV has been reduced from 60 seconds to 30 seconds. This change applies to both <code>get()</code> and <code>getWithMetadata()</code> methods.</p>
<p>This reduction allows you to maintain more up-to-date cached data and have finer-grained control over cache behavior. Applications requiring faster data refresh rates can now configure cache durations as low as 30 seconds instead of the previous 60-second minimum.</p>
<p>The <code>cacheTtl</code> parameter defines how long a KV result is cached at the global network location it is accessed from:</p>
<pre tabindex="0"><code class="language-js">// Read with custom cache TTL&#10;const value = await env.NAMESPACE.get(&quot;my-key&quot;, {&#10;	cacheTtl: 30, // Cache for minimum 30 seconds (previously 60)&#10;});&#10;&#10;// getWithMetadata also supports the reduced cache TTL&#10;const valueWithMetadata = await env.NAMESPACE.getWithMetadata(&quot;my-key&quot;, {&#10;	cacheTtl: 30, // Cache for minimum 30 seconds&#10;});&#10;</code></pre>
<p>The default cache TTL remains unchanged at 60 seconds. Upgrade to the latest version of Wrangler to be able to use 30 seconds <code>cacheTtl</code>.</p>
<p>This change affects all KV read operations using the binding API. For more information, consult the <a href="/kv/api/read-key-value-pairs/#cachettl-parameter">Workers KV cache TTL documentation</a>.</p>


<h2 id="launching-flux-2-klein-9b-on-workers-ai"><a href="/changelog/post/2026-01-28-flux-2-klein-9b-workers-ai/">Launching FLUX.2 [klein] 9B on Workers AI</a></h2>
<p><em>2026-01-28</em></p>
<p>We have partnered with Black Forest Labs (BFL) again to bring their optimized FLUX.2 [klein] 9B model to Workers AI. This distilled model offers enhanced quality compared to the 4B variant, while maintaining cost-effective pricing. With a fixed 4-step inference process, Klein 9B is ideal for rapid prototyping and real-time applications where both speed and quality matter.</p>
<p>Read the <a href="https://bfl.ai/blog">BFL blog</a> to learn more about the model itself, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-klein-9b/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="2026-01-28-flux-2-klein-9b-workers-ai-workers-ai-platform-specifics">Workers AI platform specifics</h4>
<p>The model hosted on Workers AI is optimized for speed with a <strong>fixed 4-step inference process</strong> and supports up to 4 image inputs. Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted. Like FLUX.2 [dev] and FLUX.2 [klein] 4B, this image model uses multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-9b&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form width=1024 \&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre tabindex="0"><code class="language-javascript">const form = new FormData();&#10;form.append(&quot;prompt&quot;, &quot;a sunset with a dog&quot;);&#10;form.append(&quot;width&quot;, &quot;1024&quot;);&#10;form.append(&quot;height&quot;, &quot;1024&quot;);&#10;&#10;// FormData doesn&#x27;t expose its serialized body or boundary. Passing it to a&#10;// Request (or Response) constructor serializes it and generates the Content-Type&#10;// header with the boundary, which is required for the server to parse the multipart fields.&#10;const formResponse = new Response(form);&#10;const formStream = formResponse.body;&#10;const formContentType = formResponse.headers.get(&#x27;content-type&#x27;);&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-9b&quot;, {&#10;	multipart: {&#10;		body: formStream,&#10;		contentType: formContentType,&#10;	},&#10;});&#10;</code></pre>
<p>The parameters you can send to the model are detailed here:</p>
<details>
  <summary>JSON Schema for Model</summary>
**Required Parameters**
<ul>
<li><code>prompt</code> (string) - Text description of the image to generate</li>
</ul>
<p><strong>Optional Parameters</strong></p>
<ul>
<li><code>input_image_0</code> (string) - Binary image</li>
<li><code>input_image_1</code> (string) - Binary image</li>
<li><code>input_image_2</code> (string) - Binary image</li>
<li><code>input_image_3</code> (string) - Binary image</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
<p><strong>Note:</strong> Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted.</p>
</details>
<h4 id="2026-01-28-flux-2-klein-9b-workers-ai-multi-reference-images">Multi-reference images</h4>
<p>The FLUX.2 klein-9b model supports generating images based on reference images, just like FLUX.2 [dev] and FLUX.2 [klein] 4B. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generated images. You would use it with the same multipart form data structure, with the input images in binary. The model supports up to 4 input images.</p>
<p>For the prompt, you can reference the images based on the index, like <code>take the subject of image 1 and style it like image 0</code> or even use natural language like <code>place the dog beside the woman</code>.</p>
<p>You must name the input parameter as <code>input_image_0</code>, <code>input_image_1</code>, <code>input_image_2</code>, <code>input_image_3</code> for it to work correctly. All input images must be smaller than 512x512.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-9b&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=take the subject of image 1 and style it like image 0&#x27; \&#10;  &#45;-form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png \&#10;  &#45;-form input_image_1=@/Users/johndoe/Desktop/me.png \&#10;  &#45;-form width=1024 \&#10;  &#45;-form height=1024&#10;</code></pre>
<p>Through Workers AI Binding:</p>
<pre tabindex="0"><code class="language-javascript">//helper function to convert ReadableStream to Blob&#10;async function streamToBlob(stream: ReadableStream, contentType: string): Promise&lt;Blob&gt; {&#10;  const reader = stream.getReader();&#10;  const chunks = [];&#10;&#10;  while (true) {&#10;    const { done, value } = await reader.read();&#10;    if (done) break;&#10;    chunks.push(value);&#10;  }&#10;&#10;  return new Blob(chunks, { type: contentType });&#10;}&#10;&#10;const image0 = await fetch(&quot;http://image-url&quot;);&#10;const image1 = await fetch(&quot;http://image-url&quot;);&#10;const form = new FormData();&#10;&#10;const image_blob0 = await streamToBlob(image0.body, &quot;image/png&quot;);&#10;const image_blob1 = await streamToBlob(image1.body, &quot;image/png&quot;);&#10;form.append(&#x27;input_image_0&#x27;, image_blob0)&#10;form.append(&#x27;input_image_1&#x27;, image_blob1)&#10;form.append(&#x27;prompt&#x27;, &#x27;take the subject of image 1 and style it like image 0&#x27;)&#10;&#10;// FormData doesn&#x27;t expose its serialized body or boundary. Passing it to a&#10;// Request (or Response) constructor serializes it and generates the Content-Type&#10;// header with the boundary, which is required for the server to parse the multipart fields.&#10;const formResponse = new Response(form);&#10;const formStream = formResponse.body;&#10;const formContentType = formResponse.headers.get(&#x27;content-type&#x27;);&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-9b&quot;, {&#10;    multipart: {&#10;        body: formStream,&#10;        contentType: formContentType&#10;    }&#10;})&#10;</code></pre>


<h2 id="increased-pages-file-limit-to-100-000-for-paid-plans"><a href="/changelog/post/2026-01-23-pages-file-limit-increase/">Increased Pages file limit to 100,000 for paid plans</a></h2>
<p><em>2026-01-23</em></p>
<p>Paid plans can now have up to 100,000 files per Pages site, increased from the previous limit of 20,000 files.</p>
<p>To enable this increased limit, set the environment variable <code>PAGES_WRANGLER_MAJOR_VERSION=4</code> in your Pages project settings.</p>
<p>The Free plan remains at 20,000 files per site.</p>
<p>For more details, refer to the <a href="/pages/platform/limits/#files">Pages limits documentation</a>.</p>


<h2 id="vectorize-indexes-now-support-up-to-10-million-vectors"><a href="/changelog/post/2026-01-23-increased-index-capacity/">Vectorize indexes now support up to 10 million vectors</a></h2>
<p><em>2026-01-23</em></p>
<p>You can now store up to 10 million vectors in a single Vectorize index, doubling the previous limit of 5 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.</p>
<p>Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the <a href="/vectorize/platform/limits/">Vectorize limits documentation</a> for complete details.</p>


<h2 id="new-placement-hints-for-workers"><a href="/changelog/post/2026-01-22-explicit-placement-hints/">New Placement Hints for Workers</a></h2>
<p><em>2026-01-22</em></p>
<p>You can now configure Workers to run close to infrastructure in legacy cloud regions to minimize latency to existing services and databases. This is most useful when your Worker makes multiple round trips.</p>
<p>To <a href="/workers/configuration/placement/#configure-explicit-placement-hints">set a placement hint</a>, set the <code>placement.region</code> property in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17793.md")</div>
<p>Placement hints support Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure region identifiers. Workers run in the <a href="https://www.cloudflare.com/network/">Cloudflare data center</a> with the lowest latency to the specified cloud region.</p>
<p>If your existing infrastructure is not in these cloud providers, expose it to placement probes with <code>placement.host</code> for layer 4 checks or <code>placement.hostname</code> for layer 7 checks. These probes are designed to locate single-homed infrastructure and are not suitable for anycasted or multicasted resources.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17794.md")</div>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17795.md")</div>
<p>This is an extension of <a href="/workers/configuration/placement/#enable-smart-placement">Smart Placement</a>, which automatically places your Workers closer to back-end APIs based on measured latency. When you do not know the location of your back-end APIs or have multiple back-end APIs, set <code>mode: &quot;smart&quot;</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17796.md")</div>


<h2 id="ai-search-path-filtering-for-website-and-r2-data-sources"><a href="/changelog/post/2026-01-20-ai-search-path-filtering/">AI Search path filtering for website and R2 data sources</a></h2>
<p><em>2026-01-20</em></p>
<p><a href="/ai-search/">AI Search</a> now includes <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a> for both <a href="/ai-search/configuration/data-source/website/#path-filtering">website</a> and <a href="/ai-search/configuration/data-source/r2/#path-filtering">R2</a> data sources. You can now control which content gets indexed by defining include and exclude rules for paths.</p>
<p>By controlling what gets indexed, you can improve the relevance and quality of your search results. You can also use path filtering to split a single data source across multiple AI Search instances for specialized search experiences.</p>
<p><img src="/assets/upstream/images/ai-search/path-filtering.png" alt="Path filtering configuration in AI Search" /></p>
<p>Path filtering uses <a href="https://github.com/micromatch/micromatch">micromatch</a> patterns, so you can use <code>*</code> to match within a directory and <code>**</code> to match across directories.</p>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Include</th>
<th>Exclude</th>
</tr>
</thead>
<tbody>
<tr>
<td>Index docs but skip drafts</td>
<td><code>**/docs/**</code></td>
<td><code>**/docs/drafts/**</code></td>
</tr>
<tr>
<td>Keep admin pages out of results</td>
<td>—</td>
<td><code>**/admin/**</code></td>
</tr>
<tr>
<td>Index only English content</td>
<td><code>**/en/**</code></td>
<td>—</td>
</tr>
</tbody>
</table>
<p>Configure path filters when creating a new instance or update them anytime from <strong>Settings</strong>. Check out <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a> to learn more.</p>


<h2 id="create-ai-search-instances-programmatically-via-rest-api"><a href="/changelog/post/2026-01-20-ai-search-simplified-api/">Create AI Search instances programmatically via REST API</a></h2>
<p><em>2026-01-20</em></p>
<p>You can now create <a href="/ai-search/">AI Search</a> instances programmatically using the <a href="/ai-search/get-started/api/">API</a>. For example, use the API to create instances for each customer in a multi-tenant application or manage AI Search alongside your other infrastructure.</p>
<p>If you have created an AI Search instance via the <a href="/ai-search/get-started/dashboard/">dashboard</a> before, you already have a <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a> registered and can start creating instances programmatically right away. If not, follow the <a href="/ai-search/get-started/api/">API guide</a> to set up your first instance.</p>
<p>For example, you can now create separate search instances for each language on your website:</p>
<pre tabindex="0"><code class="language-bash">for lang in en fr es de; do&#10;  curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/instances&quot; \&#10;    &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;    &#45;H &quot;Content-Type: application/json&quot; \&#10;    &#45;-data &#x27;{&#10;      &quot;id&quot;: &quot;docs-&#x27;&quot;$lang&quot;&#x27;&quot;,&#10;      &quot;type&quot;: &quot;web-crawler&quot;,&#10;      &quot;source&quot;: &quot;example.com&quot;,&#10;      &quot;source_params&quot;: {&#10;        &quot;path_include&quot;: [&quot;**/&#x27;&quot;$lang&quot;&#x27;/**&quot;]&#10;      }&#10;    }&#x27;&#10;done&#10;</code></pre>
<p>Refer to the <a href="/api/resources/ai_search/subresources/instances/methods/create/">REST API reference</a> for additional configuration options.</p>


<h2 id="new-workers-kv-dashboard-ui"><a href="/changelog/post/2026-01-20-kv-dash-ui-homepage/">New Workers KV Dashboard UI</a></h2>
<p><em>2026-01-20</em></p>
<p><a href="/kv/">Workers KV</a> has an updated dashboard UI with new dashboard styling that makes it easier to navigate and see analytics and settings for a KV namespace.</p>
<p>The new dashboard features a <strong>streamlined homepage</strong> for easy access to your namespaces and key operations, with consistent design with the rest of the dashboard UI updates. It also provides an <strong>improved analytics view</strong>.</p>
<p><img src="/assets/upstream/images/changelog/kv/kv-dash-ui-homepage.png" alt="New KV Dashboard Homepage" /></p>
<p>The updated dashboard is now available for all Workers KV users. Log in to the <a href="https://dash.cloudflare.com/">Cloudflare Dashboard</a> to start exploring the new interface.</p>


<h2 id="cloudflare-typescript-sdk-v6-0-0-beta-1-now-available"><a href="/changelog/post/2026-01-20-cloudflare-typescript-v6.0.0-beta.1/">Cloudflare Typescript SDK v6.0.0-beta.1 now available</a></h2>
<p><em>2026-01-20</em></p>
<blockquote>
<p><strong>Disclaimer:</strong> Please note that v6.0.0-beta.1 is in Beta and we are still testing it for stability.</p>
</blockquote>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-typescript/compare/v5.2.0...v6.0.0-beta.1">v5.2.0...v6.0.0-beta.1</a></p>
<p>In this release, you'll see a large number of breaking changes. This is primarily due to a change in OpenAPI definitions, which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce our SDK libraries. As the codegen is always evolving and improving, so are our code bases.</p>
<p>Some breaking changes were introduced due to bug fixes, also listed below.</p>
<p>Please ensure you read through the list of changes below before moving to this version - this will help you understand any down or upstream issues it may cause to your environments.</p>
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-breaking-changes">Breaking Changes</h4>
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-addressing-parameter-requirements-changed">Addressing - Parameter Requirements Changed</h4>
- `BGPPrefixCreateParams.cidr`: optional → **required**
- `PrefixCreateParams.asn`: `number | null` → `number`
- `PrefixCreateParams.loa_document_id`: required → **optional**
- `ServiceBindingCreateParams.cidr`: optional → **required**
- `ServiceBindingCreateParams.service_id`: optional → **required**
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-api-gateway">API Gateway</h4>
- `ConfigurationUpdateResponse` removed
- `PublicSchema` → `OldPublicSchema`
- `SchemaUpload` → `UserSchemaCreateResponse`
- `ConfigurationUpdateParams.properties` removed; use `normalize`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-cloudforceone-response-type-changes">CloudforceOne - Response Type Changes</h4>
- `ThreatEventBulkCreateResponse`: `number` → complex object with counts and errors
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-d1-database-query-parameters">D1 Database - Query Parameters</h4>
- `DatabaseQueryParams`: simple interface → union type (`D1SingleQuery | MultipleQueries`)
- `DatabaseRawParams`: same change
- Supports batch queries via `batch` array
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-dns-records-type-renames-21-types">DNS Records - Type Renames (21 types)</h4>
All record type interfaces renamed from `*Record` to short names:
- `RecordResponse.ARecord` → `RecordResponse.A`
- `RecordResponse.AAAARecord` → `RecordResponse.AAAA`
- `RecordResponse.CNAMERecord` → `RecordResponse.CNAME`
- `RecordResponse.MXRecord` → `RecordResponse.MX`
- `RecordResponse.NSRecord` → `RecordResponse.NS`
- `RecordResponse.PTRRecord` → `RecordResponse.PTR`
- `RecordResponse.TXTRecord` → `RecordResponse.TXT`
- `RecordResponse.CAARecord` → `RecordResponse.CAA`
- `RecordResponse.CERTRecord` → `RecordResponse.CERT`
- `RecordResponse.DNSKEYRecord` → `RecordResponse.DNSKEY`
- `RecordResponse.DSRecord` → `RecordResponse.DS`
- `RecordResponse.HTTPSRecord` → `RecordResponse.HTTPS`
- `RecordResponse.LOCRecord` → `RecordResponse.LOC`
- `RecordResponse.NAPTRRecord` → `RecordResponse.NAPTR`
- `RecordResponse.SMIMEARecord` → `RecordResponse.SMIMEA`
- `RecordResponse.SRVRecord` → `RecordResponse.SRV`
- `RecordResponse.SSHFPRecord` → `RecordResponse.SSHFP`
- `RecordResponse.SVCBRecord` → `RecordResponse.SVCB`
- `RecordResponse.TLSARecord` → `RecordResponse.TLSA`
- `RecordResponse.URIRecord` → `RecordResponse.URI`
- `RecordResponse.OpenpgpkeyRecord` → `RecordResponse.Openpgpkey`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-iam-resource-groups">IAM Resource Groups</h4>
- `ResourceGroupCreateResponse.scope`: optional single → **required array**
- `ResourceGroupCreateResponse.id`: optional → **required**
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-origin-ca-certificates-parameter-requirements-changed">Origin CA Certificates - Parameter Requirements Changed</h4>
- `OriginCACertificateCreateParams.csr`: optional → **required**
- `OriginCACertificateCreateParams.hostnames`: optional → **required**
- `OriginCACertificateCreateParams.request_type`: optional → **required**
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-pages">Pages</h4>
- Renamed: `DeploymentsSinglePage` → `DeploymentListResponsesV4PagePaginationArray`
- Domain response fields: many optional → **required**
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-pipelines-v0-to-v1-migration">Pipelines - v0 to v1 Migration</h4>
- Entire v0 API deprecated; use v1 methods (`createV1`, `listV1`, etc.)
- New sub-resources: `Sinks`, `Streams`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-r2">R2</h4>
- `EventNotificationUpdateParams.rules`: optional → **required**
- Super Slurper: `bucket`, `secret` now required in source params
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-radar">Radar</h4>
- `dataSource`: `string` → typed enum (23 values)
- `eventType`: `string` → typed enum (6 values)
- V2 methods require `dimension` parameter (breaking signature change)
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-resource-sharing">Resource Sharing</h4>
- Removed: `status_message` field from all recipient response types
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-schema-validation">Schema Validation</h4>
- Consolidated `SchemaCreateResponse`, `SchemaListResponse`, `SchemaEditResponse`, `SchemaGetResponse` → `PublicSchema`
- Renamed: `SchemaListResponsesV4PagePaginationArray` → `PublicSchemasV4PagePaginationArray`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-spectrum">Spectrum</h4>
- Renamed union members: `AppListResponse.UnionMember0` → `SpectrumConfigAppConfig`
- Renamed union members: `AppListResponse.UnionMember1` → `SpectrumConfigPaygoAppConfig`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-workers">Workers</h4>
- Removed: `WorkersBindingKindTailConsumer` type (all occurrences)
- Renamed: `ScriptsSinglePage` → `ScriptListResponsesSinglePage`
- Removed: `DeploymentsSinglePage`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-dlp">Zero-Trust DLP</h4>
- `datasets.create()`, `update()`, `get()` return types changed
- `PredefinedGetResponse` union members renamed to `UnionMember0-5`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-tunnels">Zero-Trust Tunnels</h4>
- Removed: `CloudflaredCreateResponse`, `CloudflaredListResponse`, `CloudflaredDeleteResponse`, `CloudflaredEditResponse`, `CloudflaredGetResponse`
- Removed: `CloudflaredListResponsesV4PagePaginationArray`
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-features">Features</h4>
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-abuse-reports-client-abusereports">Abuse Reports (<code>client.abuseReports</code>)</h4>
- **Reports**: `create`, `list`, `get`
- **Mitigations**: sub-resource for abuse mitigations
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-ai-search-client-aisearch">AI Search (<code>client.aisearch</code>)</h4>
- **Instances**: `create`, `update`, `list`, `delete`, `read`, `stats`
- **Items**: `list`, `get`
- **Jobs**: `create`, `list`, `get`, `logs`
- **Tokens**: `create`, `update`, `list`, `delete`, `read`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-connectivity-client-connectivity">Connectivity (<code>client.connectivity</code>)</h4>
- **Directory Services**: `create`, `update`, `list`, `delete`, `get`
- Supports IPv4, IPv6, dual-stack, and hostname configurations
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-organizations-client-organizations">Organizations (<code>client.organizations</code>)</h4>
- **Organizations**: `create`, `update`, `list`, `delete`, `get`
- **OrganizationProfile**: `update`, `get`
- Hierarchical organization support with parent/child relationships
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-r2-data-catalog-client-r2datacatalog">R2 Data Catalog (<code>client.r2DataCatalog</code>)</h4>
- **Catalog**: `list`, `enable`, `disable`, `get`
- **Credentials**: `create`
- **MaintenanceConfigs**: `update`, `get`
- **Namespaces**: `list`
- **Tables**: `list`, maintenance config management
- Apache Iceberg integration
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-realtime-kit-client-realtimekit">Realtime Kit (<code>client.realtimeKit</code>)</h4>
- **Apps**: `get`, `post`
- **Meetings**: `create`, `get`, participant management
- **Livestreams**: 10+ methods for streaming
- **Recordings**: start, pause, stop, get
- **Sessions**: transcripts, summaries, chat
- **Webhooks**: full CRUD
- **ActiveSession**: polls, kick participants
- **Analytics**: organization analytics
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-token-validation-client-tokenvalidation">Token Validation (<code>client.tokenValidation</code>)</h4>
- **Configuration**: `create`, `list`, `delete`, `edit`, `get`
- **Credentials**: `update`
- **Rules**: `create`, `list`, `delete`, `bulkCreate`, `bulkEdit`, `edit`, `get`
- JWT validation with RS256/384/512, PS256/384/512, ES256, ES384
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-alerting-silences-client-alerting-silences">Alerting Silences (<code>client.alerting.silences</code>)</h4>
- `create`, `update`, `list`, `delete`, `get`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-iam-sso-client-iam-sso">IAM SSO (<code>client.iam.sso</code>)</h4>
- `create`, `update`, `list`, `delete`, `get`, `beginVerification`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-pipelines-v1-client-pipelines">Pipelines v1 (<code>client.pipelines</code>)</h4>
- **Sinks**: `create`, `list`, `delete`, `get`
- **Streams**: `create`, `update`, `list`, `delete`, `get`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-ai-controls-mcp-client-zerotrust-access-aicontrols-mcp">Zero-Trust AI Controls / MCP (<code>client.zeroTrust.access.aiControls.mcp</code>)</h4>
- **Portals**: `create`, `update`, `list`, `delete`, `read`
- **Servers**: `create`, `update`, `list`, `delete`, `read`, `sync`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-accounts">Accounts</h4>
- `managed_by` field with `parent_org_id`, `parent_org_name`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-addressing-loa-documents">Addressing LOA Documents</h4>
- `auto_generated` field on `LOADocumentCreateResponse`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-addressing-prefixes">Addressing Prefixes</h4>
- `delegate_loa_creation`, `irr_validation_state`, `ownership_validation_state`, `ownership_validation_token`, `rpki_validation_state`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-ai">AI</h4>
- Added `toMarkdown.supported()` method to get all supported conversion formats
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-ai-gateway">AI Gateway</h4>
- `zdr` field added to all responses and params
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-alerting">Alerting</h4>
- New alert type: `abuse_report_alert`
- `type` field added to PolicyFilter
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-browser-rendering">Browser Rendering</h4>
- `ContentCreateParams`: refined to discriminated union (`Variant0 | Variant1`)
- Split into URL-based and HTML-based parameter variants for better type safety
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-client-certificates">Client Certificates</h4>
- `reactivate` parameter in edit
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-cloudforceone">CloudforceOne</h4>
- `ThreatEventCreateParams.indicatorType`: required → optional
- `hasChildren` field added to all threat event response types
- `datasetIds` query parameter on `AttackerListParams`, `CategoryListParams`, `TargetIndustryListParams`
- `categoryUuid` field on `TagCreateResponse`
- `indicators` array for multi-indicator support per event
- `uuid` and `preserveUuid` fields for UUID preservation in bulk create
- `format` query parameter (`'json' | 'stix2'`) on `ThreatEventListParams`
- `createdAt`, `datasetId` fields on `ThreatEventEditParams`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-content-scanning">Content Scanning</h4>
- Added `create()`, `update()`, `get()` methods
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-custom-pages">Custom Pages</h4>
- New page types: `basic_challenge`, `under_attack`, `waf_challenge`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-d1">D1</h4>
- `served_by_colo` - colo that handled query
- `jurisdiction` - `'eu' | 'fedramp'`
- **Time Travel** (`client.d1.database.timeTravel`): `getBookmark()`, `restore()` - point-in-time recovery
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-email-security">Email Security</h4>
- New fields on `InvestigateListResponse`/`InvestigateGetResponse`: `envelope_from`, `envelope_to`, `postfix_id_outbound`, `replyto`
- New detection classification: `'outbound_ndr'`
- Enhanced `Finding` interface with `attachment`, `detection`, `field`, `portion`, `reason`, `score`
- Added `cursor` query parameter to `InvestigateListParams`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-gateway-lists">Gateway Lists</h4>
- New list types: `CATEGORY`, `LOCATION`, `DEVICE`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-intel">Intel</h4>
- New issue type: `'configuration_suggestion'`
- `payload` field: `unknown` → typed `Payload` interface with `detection_method`, `zone_tag`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-leaked-credential-checks">Leaked Credential Checks</h4>
- Added `detections.get()` method
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-logpush">Logpush</h4>
- New datasets: `dex_application_tests`, `dex_device_state_events`, `ipsec_logs`, `warp_config_changes`, `warp_toggle_changes`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-load-balancers">Load Balancers</h4>
- `Monitor.port`: `number` → `number | null`
- `Pool.load_shedding`: `LoadShedding` → `LoadShedding | null`
- `Pool.origin_steering`: `OriginSteering` → `OriginSteering | null`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-magic-transit">Magic Transit</h4>
- `license_key` field on connectors
- `provision_license` parameter for auto-provisioning
- IPSec: `custom_remote_identities` with FQDN support
- Snapshots: Bond interface, `probed_mtu` field
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-pages-1">Pages</h4>
- New response types: `ProjectCreateResponse`, `ProjectListResponse`, `ProjectEditResponse`, `ProjectGetResponse`
- Deployment methods return specific response types instead of generic `Deployment`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-queues">Queues</h4>
- Added `subscriptions.get()` method
- Enhanced `SubscriptionGetResponse` with typed event source interfaces
- New event source types: Images, KV, R2, Vectorize, Workers AI, Workers Builds, Workflows
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-r2-1">R2</h4>
- Sippy: new provider `s3` (S3-compatible endpoints)
- Sippy: `bucketUrl` field for S3-compatible sources
- Super Slurper: `keys` field on source response schemas (specify specific keys to migrate)
- Super Slurper: `pathPrefix` field on source schemas
- Super Slurper: `region` field on S3 source params
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-radar-1">Radar</h4>
- Added `geolocations.list()`, `geolocations.get()` methods
- Added V2 dimension-based methods (`summaryV2`, `timeseriesGroupsV2`) to radar sub-resources
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-resource-sharing-1">Resource Sharing</h4>
- Added `terminal` boolean field to Resource Error interfaces
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-rules">Rules</h4>
- Added `id` field to `ItemDeleteParams.Item`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-rulesets">Rulesets</h4>
- New buffering fields on `SetConfigRule`: `request_body_buffering`, `response_body_buffering`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-secrets-store">Secrets Store</h4>
- New scopes: `'dex'`, `'access'` (in addition to `'workers'`, `'ai_gateway'`)
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-ssl-certificate-packs">SSL Certificate Packs</h4>
- Response types now proper interfaces (was `unknown`)
- Fields now required: `id`, `certificates`, `hosts`, `status`, `type`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-security-center">Security Center</h4>
- `payload` field: `unknown` → typed `Payload` interface with `detection_method`, `zone_tag`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-shared-types">Shared Types</h4>
- Added: `CloudflareTunnelsV4PagePaginationArray` pagination class
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-workers-1">Workers</h4>
- Added `subdomains.delete()` method
- `Worker.references` - track external dependencies (domains, Durable Objects, queues)
- `Worker.startup_time_ms` - startup timing
- `Script.observability` - observability settings with logging
- `Script.tag`, `Script.tags` - immutable ID and tags
- Placement: support for region, hostname, host-based placement
- `tags`, `tail_consumers` now accept `| null`
- Telemetry: `traces` field, `$containers` event info, `durableObjectId`, `transactionName`, `abr_level` fields
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-workers-for-platforms">Workers for Platforms</h4>
- `ScriptUpdateResponse`: new fields `entry_point`, `observability`, `tag`, `tags`
- `placement` field now union of 4 variants (smart mode, region, hostname, host)
- `tags`, `tail_consumers` now nullable
- `TagUpdateParams.body` now accepts `null`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-workflows">Workflows</h4>
- `instance_retention`: `unknown` → typed `InstanceRetention` interface with `error_retention`, `success_retention`
- New status option: `'restart'` added to `StatusEditParams.status`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-devices">Zero-Trust Devices</h4>
- External emergency disconnect settings (4 new fields)
- `antivirus` device posture check type
- `os_version_extra` documentation improvements
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zones">Zones</h4>
- New response types: `SubscriptionCreateResponse`, `SubscriptionUpdateResponse`, `SubscriptionGetResponse`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-access-applications">Zero-Trust Access Applications</h4>
- New `ApplicationType` values: `'mcp'`, `'mcp_portal'`, `'proxy_endpoint'`
- New destination type: `ViaMcpServerPortalDestination` for MCP server access
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-gateway">Zero-Trust Gateway</h4>
- Added `rules.listTenant()` method
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-gateway-proxy-endpoints">Zero-Trust Gateway - Proxy Endpoints</h4>
- `ProxyEndpoint`: interface → discriminated union (`ZeroTrustGatewayProxyEndpointIP | ZeroTrustGatewayProxyEndpointIdentity`)
- `ProxyEndpointCreateParams`: interface → union type
- Added `kind` field: `'ip' | 'identity'`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-tunnels-1">Zero-Trust Tunnels</h4>
- `WARPConnector*Response`: union type → interface
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-deprecations">Deprecations</h4>
<ul>
<li><strong>API Gateway</strong>: <code>UserSchemas</code>, <code>Settings</code>, <code>SchemaValidation</code> resources</li>
<li><strong>Audit Logs</strong>: <code>auditLogId.not</code> (use <code>id.not</code>)</li>
<li><strong>CloudforceOne</strong>: <code>ThreatEvents.get()</code>, <code>IndicatorTypes.list()</code></li>
<li><strong>Devices</strong>: <code>public_ip</code> field (use DEX API)</li>
<li><strong>Email Security</strong>: <code>item_count</code> field in Move responses</li>
<li><strong>Pipelines</strong>: v0 methods (use v1)</li>
<li><strong>Radar</strong>: old <code>summary()</code> and <code>timeseriesGroups()</code> methods (use V2)</li>
<li><strong>Rulesets</strong>: <code>disable_apps</code>, <code>mirage</code> fields</li>
<li><strong>WARP Connector</strong>: <code>connections</code> field</li>
<li><strong>Workers</strong>: <code>environment</code> parameter in Domains</li>
<li><strong>Zones</strong>: <code>ResponseBuffering</code> page rule</li>
</ul>
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>mcp:</strong> correct code tool API endpoint (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/599703c45672dc899455d74b124018efd4b75095">599703c</a>)</li>
<li><strong>mcp:</strong> return correct lines on typescript errors (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/5d6f9998ed9999aaa95e1bda8cf50929f3555cf1">5d6f999</a>)</li>
<li><strong>organization_profile:</strong> fix bad reference (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/d84ea77094400055c06554812b84c2f0c8d00cc4">d84ea77</a>)</li>
<li><strong>schema_validation:</strong> correctly reflect model to openapi mapping (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/bb861516774b159d80e0f46a5f3abc5a4c9f9d49">bb86151</a>)</li>
<li><strong>workers:</strong> fix tests (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/2ee37f7adf5a4637d65f61fc225e135eec2579fc">2ee37f7</a>)</li>
</ul>
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-documentation">Documentation</h4>
<ul>
<li>Added deprecation notices with migration paths</li>
<li><strong>api_gateway:</strong> deprecate API Shield Schema Validation resources (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/8a4b20f7a572422f74179fbdb4f1c4fb555e3e40">8a4b20f</a>)</li>
<li>Improved JSDoc examples across all resources</li>
<li><strong>workers:</strong> expose subdomain delete documentation (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/4f7cc1f2b8861a5b8abc193d287f78264a425062">4f7cc1f</a>)</li>
</ul>


<h2 id="terraform-v5-16-0-now-available"><a href="/changelog/post/2026-01-20-terraform-v5.16.0-provider/">Terraform v5.16.0 now available</a></h2>
<p><em>2026-01-20</em></p>
<p>In January 2025, we announced the launch of the new Terraform v5 Provider. We greatly appreciate the proactive engagement and valuable feedback from the Cloudflare community following the v5 release. In response, we've established a consistent and rapid <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> for releasing targeted improvements, demonstrating our commitment to stability and reliability.</p>
<p>With the help of the community, we have a growing number of resources that we have marked as <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">stable</a>, with that list continuing to grow with every release. The most used <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">resources</a> are on track to be stable by the end of March 2026, when we will also be releasing a new migration tool to you migrate from v4 to v5 with ease.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes bug fixes, the stabilization of even more popular resources, and more.</p>
<h4 id="2026-01-20-terraform-v5.16.0-provider-features">Features</h4>
<ul>
<li><strong>custom_pages:</strong> add &quot;waf_challenge&quot; as new supported error page type identifier in both resource and data source schemas</li>
<li><strong>list:</strong> enhance CIDR validator to check for normalized CIDR notation requiring network address for IPv4 and IPv6</li>
<li><strong>magic_wan_gre_tunnel:</strong> add automatic_return_routing attribute for automatic routing control</li>
<li><strong>magic_wan_gre_tunnel:</strong> add BGP configuration support with new BGP model attribute</li>
<li><strong>magic_wan_gre_tunnel:</strong> add bgp_status computed attribute for BGP connection status information</li>
<li><strong>magic_wan_gre_tunnel:</strong> enhance schema with BGP-related attributes and validators</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> add automatic_return_routing attribute for automatic routing control</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> add BGP configuration support with new BGP model attribute</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> add bgp_status computed attribute for BGP connection status information</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> add custom_remote_identities attribute for custom identity configuration</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> enhance schema with BGP and identity-related attributes</li>
<li><strong>ruleset:</strong> add request body buffering support</li>
<li><strong>ruleset:</strong> enhance ruleset data source with additional configuration options</li>
<li><strong>workers_script:</strong> add observability logs attributes to list data source model</li>
<li><strong>workers_script:</strong> enhance list data source schema with additional configuration options</li>
</ul>
<h4 id="2026-01-20-terraform-v5.16.0-provider-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>account_member</strong>: fix resource importability issues</li>
<li><strong>dns_record:</strong> remove unnecessary fmt.Sprintf wrapper around LoadTestCase call in test configuration helper function</li>
<li><strong>load_balancer:</strong> fix session_affinity_ttl type expectations to match Float64 in initial creation and Int64 after migration</li>
<li><strong>workers_kv:</strong> handle special characters correctly in URL encoding</li>
</ul>
<h4 id="2026-01-20-terraform-v5.16.0-provider-documentation">Documentation</h4>
<ul>
<li><strong>account_subscription:</strong> update schema description for rate_plan.sets attribute to clarify it returns an array of strings</li>
<li><strong>api_shield:</strong> add resource-level description for API Shield management of auth ID characteristics</li>
<li><strong>api_shield:</strong> enhance auth_id_characteristics.name attribute description to include JWT token configuration format requirements</li>
<li><strong>api_shield:</strong> specify JSONPath expression format for JWT claim locations</li>
<li><strong>hyperdrive_config:</strong> add description attribute to name attribute explaining its purpose in dashboard and API identification</li>
<li><strong>hyperdrive_config:</strong> apply description improvements across resource, data source, and list data source schemas</li>
<li><strong>hyperdrive_config:</strong> improve schema descriptions for cache settings to clarify default values</li>
<li><strong>hyperdrive_config:</strong> update port description to clarify defaults for different database types</li>
</ul>
<h4 id="2026-01-20-terraform-v5.16.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](/terraform/)
- [List of stabilized resources](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)


<h2 id="use-auxiliary-workers-alongside-full-stack-frameworks"><a href="/changelog/post/2026-01-20-auxiliary-workers/">Use auxiliary Workers alongside full-stack frameworks</a></h2>
<p><em>2026-01-20</em></p>
<p>Auxiliary Workers are now fully supported when using full-stack frameworks, such as <a href="/workers/framework-guides/web-apps/react-router/">React Router</a> and <a href="/workers/framework-guides/web-apps/tanstack-start/">TanStack Start</a>, that integrate with the <a href="/workers/vite-plugin/reference/api/">Cloudflare Vite plugin</a>.
They are included alongside the framework's build output in the build output directory.
Note that this feature requires Vite 7 or above.</p>
<p>Auxiliary Workers are additional Workers that can be called via <a href="/workers/runtime-apis/bindings/service-bindings/">service bindings</a> from your main (entry) Worker.
They are defined in the plugin config, as in the example below:</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { tanstackStart } from &quot;@tanstack/react-start/plugin/vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		tanstackStart(),&#10;		cloudflare({&#10;			viteEnvironment: { name: &quot;ssr&quot; },&#10;			auxiliaryWorkers: [{ configPath: &quot;./wrangler.aux.jsonc&quot; }],&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>See the Vite plugin <a href="/workers/vite-plugin/reference/api/">API docs</a> for more info.</p>


<h2 id="import-sql-files-as-additional-modules-by-default"><a href="/changelog/post/2026-01-20-sql-module-rule/">Import SQL files as additional modules by default</a></h2>
<p><em>2026-01-20</em></p>
<p>The <code>.sql</code> file extension is now automatically configured to be importable in your Worker code when using <a href="/workers/wrangler/bundling/#including-non-javascript-modules">Wrangler</a> or the <a href="/workers/vite-plugin/reference/non-javascript-modules/">Cloudflare Vite plugin</a>.
This is particular useful for importing migrations in Durable Objects and means you no longer need to configure custom rules when using <a href="https://orm.drizzle.team/docs/connect-cloudflare-do">Drizzle</a>.</p>
<p>SQL files are imported as JavaScript strings:</p>
<pre tabindex="0"><code class="language-ts">// `example` will be a JavaScript string&#10;import example from &quot;./example.sql&quot;;&#10;</code></pre>


<h2 id="verify-warp-connector-connectivity-with-a-simple-ping"><a href="/changelog/post/2026-01-15-warp-connector-ping-support/">Verify WARP Connector connectivity with a simple ping</a></h2>
<p><em>2026-01-15</em></p>
<p>We have made it easier to validate connectivity when deploying <a href="/mesh/">WARP Connector</a> as part of your <a href="/reference-architecture/architectures/sase/#connecting-networks">software-defined private network</a>.</p>
<p>You can now <code>ping</code> the WARP Connector host directly on its LAN IP address immediately after installation. This provides a fast, familiar way to confirm that the Connector is online and reachable within your network before testing access to downstream services.</p>
<p>Starting with <a href="/changelog/2026-01-13-warp-linux-ga/">version 2025.10.186.0</a>, WARP Connector responds to traffic addressed to its own LAN IP, giving you immediate visibility into Connector reachability.</p>
<p>Learn more about deploying <a href="/mesh/">WARP Connector</a> and building private network connectivity with <a href="/cloudflare-one/">Cloudflare One</a>.</p>


<h2 id="launching-flux-2-klein-4b-on-workers-ai"><a href="/changelog/post/2026-01-15-flux-2-klein-4b-workers-ai/">Launching FLUX.2 [klein] 4B on Workers AI</a></h2>
<p><em>2026-01-15</em></p>
<p>We've partnered with Black Forest Labs (BFL) again to bring their optimized FLUX.2 [klein] 4B model to Workers AI! This distilled model offers faster generation and cost-effective pricing, while maintaining great output quality. With a fixed 4-step inference process, Klein 4B is ideal for rapid prototyping and real-time applications where speed matters.</p>
<p>Read the <a href="https://bfl.ai/blog">BFL blog</a> to learn more about the model itself, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-klein-4b/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="2026-01-15-flux-2-klein-4b-workers-ai-workers-ai-platform-specifics">Workers AI Platform specifics</h4>
<p>The model hosted on Workers AI is optimized for speed with a <strong>fixed 4-step inference process</strong> and supports up to 4 image inputs. Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted. Like FLUX.2 [dev], this image model uses multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-4b&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form width=1024 \&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre tabindex="0"><code class="language-javascript">const form = new FormData();&#10;form.append(&quot;prompt&quot;, &quot;a sunset with a dog&quot;);&#10;form.append(&quot;width&quot;, &quot;1024&quot;);&#10;form.append(&quot;height&quot;, &quot;1024&quot;);&#10;&#10;// FormData doesn&#x27;t expose its serialized body or boundary. Passing it to a&#10;// Request (or Response) constructor serializes it and generates the Content-Type&#10;// header with the boundary, which is required for the server to parse the multipart fields.&#10;const formResponse = new Response(form);&#10;const formStream = formResponse.body;&#10;const formContentType = formResponse.headers.get(&#x27;content-type&#x27;);&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-4b&quot;, {&#10;	multipart: {&#10;		body: formStream,&#10;		contentType: formContentType,&#10;	},&#10;});&#10;</code></pre>
<p>The parameters you can send to the model are detailed here:</p>
<details>
  <summary>JSON Schema for Model</summary>
**Required Parameters**
<ul>
<li><code>prompt</code> (string) - Text description of the image to generate</li>
</ul>
<p><strong>Optional Parameters</strong></p>
<ul>
<li><code>input_image_0</code> (string) - Binary image</li>
<li><code>input_image_1</code> (string) - Binary image</li>
<li><code>input_image_2</code> (string) - Binary image</li>
<li><code>input_image_3</code> (string) - Binary image</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
<p><strong>Note:</strong> Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted.</p>
</details>
<pre tabindex="0"><code>&#10;&#35;# Multi-Reference Images&#10;&#10;The FLUX.2 klein-4b model supports generating images based on reference images, just like FLUX.2 [dev]. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generated images. You would use it with the same multipart form data structure, with the input images in binary. The model supports up to 4 input images.&#10;&#10;For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.&#10;&#10;Note: you have to name the input parameter as `input_image_0`, `input_image_1`, `input_image_2`, `input_image_3` for it to work correctly. All input images must be smaller than 512x512.&#10;</code></pre>
<p>curl --request POST <br />
--url '<a href="https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT%7D/ai/run/@cf/black-forest-labs/flux-2-klein-4b">https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-4b</a>' <br />
--header 'Authorization: Bearer {TOKEN}' <br />
--header 'Content-Type: multipart/form-data' <br />
--form 'prompt=take the subject of image 1 and style it like image 0' <br />
--form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png <br />
--form input_image_1=@/Users/johndoe/Desktop/me.png <br />
--form width=1024 <br />
--form height=1024</p>
<pre tabindex="0"><code>&#10;Through Workers AI Binding:&#10;</code></pre>
<p>//helper function to convert ReadableStream to Blob
async function streamToBlob(stream: ReadableStream, contentType: string): Promise<Blob> {
const reader = stream.getReader();
const chunks = [];</p>
<p>while (true) {
const { done, value } = await reader.read();
if (done) break;
chunks.push(value);
}</p>
<p>return new Blob(chunks, { type: contentType });
}</p>
<p>const image0 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const image1 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const form = new FormData();</p>
<p>const image_blob0 = await streamToBlob(image0.body, &quot;image/png&quot;);
const image_blob1 = await streamToBlob(image1.body, &quot;image/png&quot;);
form.append('input_image_0', image_blob0)
form.append('input_image_1', image_blob1)
form.append('prompt', 'take the subject of image 1 and style it like image 0')</p>
<p>// FormData doesn't expose its serialized body or boundary. Passing it to a
// Request (or Response) constructor serializes it and generates the Content-Type
// header with the boundary, which is required for the server to parse the multipart fields.
const formResponse = new Response(form);
const formStream = formResponse.body;
const formContentType = formResponse.headers.get('content-type');</p>
<p>const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-4b&quot;, {
multipart: {
body: formStream,
contentType: formContentType
}
})</p>
<pre tabindex="0"><code></code></pre>


<h2 id="wrangler-types-now-generates-types-for-all-environments"><a href="/changelog/post/2026-01-13-wrangler-types-multi-environment/">`wrangler types` now generates types for all environments</a></h2>
<p><em>2026-01-13</em></p>
<p>The <code>wrangler types</code> command now generates TypeScript types for bindings from <strong>all environments</strong> defined in your Wrangler configuration file by default.</p>
<p>Previously, <code>wrangler types</code> only generated types for bindings in the top-level configuration (or a single environment when using the <code>--env</code> flag). This meant that if you had environment-specific bindings — for example, a KV namespace only in production or an R2 bucket only in staging — those bindings would be missing from your generated types, causing TypeScript errors when accessing them.</p>
<p>Now, running <code>wrangler types</code> collects bindings from all environments and includes them in the generated <code>Env</code> type. This ensures your types are complete regardless of which environment you deploy to.</p>
<h4 id="2026-01-13-wrangler-types-multi-environment-generating-types-for-a-specific-environment">Generating types for a specific environment</h4>
<p>If you want the previous behavior of generating types for only a specific environment, you can use the <code>--env</code> flag:</p>
<pre tabindex="0"><code class="language-sh">wrangler types --env production&#10;</code></pre>
<p>Learn more about <a href="/workers/wrangler/commands/general/#types">generating types for your Worker</a> in the Wrangler documentation.</p>


<h2 id="validate-your-generated-types-with-wrangler-types-check"><a href="/changelog/post/2026-01-11-wrangler-types-check/">Validate your generated types with `wrangler types --check`</a></h2>
<p><em>2026-01-12</em></p>
<p>Wrangler now supports a <code>--check</code> flag for the <code>wrangler types</code> command. This flag validates that your generated types are up to date without writing any changes to disk.</p>
<p>This is useful in CI/CD pipelines where you want to ensure that developers have regenerated their types after making changes to their Wrangler configuration. If the types are out of date, the command will exit with a non-zero status code.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler types --check&#10;</code></pre>
<p>If your types are up to date, the command will succeed silently. If they are out of date, you'll see an error message indicating which files need to be regenerated.</p>
<p>For more information, see the <a href="/workers/wrangler/commands/general/#types">Wrangler types documentation</a>.</p>


<h2 id="get-notified-when-your-workers-builds-succeed-or-fail"><a href="/changelog/post/2025-12-11-builds-event-subscriptions/">Get notified when your Workers builds succeed or fail</a></h2>
<p><em>2026-01-09</em></p>
<p>You can now receive notifications when your Workers' builds start, succeed, fail, or get cancelled using <a href="/queues/event-subscriptions/">Event Subscriptions</a>.</p>
<p><a href="/workers/ci-cd/builds/">Workers Builds</a> publishes events to a <a href="/queues/">Queue</a> that your Worker can read messages from, and then send notifications wherever you need — Slack, Discord, email, or any webhook endpoint.</p>
<p>You can deploy <a href="https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template">this Worker</a> to your own Cloudflare account to send build notifications to Slack:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>The template includes:</p>
<ul>
<li>Build status with Preview/Live URLs for successful deployments</li>
<li>Inline error messages for failed builds</li>
<li>Branch, commit hash, and author name</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workers/builds-notifications-slack.png" alt="Slack notifications showing build events" /></p>
<p>For setup instructions, refer to the <a href="https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template#readme">template README</a> or the <a href="/queues/event-subscriptions/manage-event-subscriptions/">Event Subscriptions documentation</a>.</p>


<h2 id="shell-tab-completions-for-wrangler-cli"><a href="/changelog/post/2026-01-09-wrangler-tab-completion/">Shell tab completions for Wrangler CLI</a></h2>
<p><em>2026-01-09</em></p>
<p>Wrangler now includes built-in shell tab completion support, making it faster and easier to navigate commands without memorizing every option. Press Tab as you type to autocomplete commands, subcommands, flags, and even option values like log levels.</p>
<p>Tab completions are supported for Bash, Zsh, Fish, and PowerShell.</p>
<h4 id="2026-01-09-wrangler-tab-completion-setup">Setup</h4>
<p>Generate the completion script for your shell and add it to your configuration file:</p>
<pre tabindex="0"><code class="language-sh">&#35; Bash&#10;wrangler complete bash &gt;&gt; ~/.bashrc&#10;&#10;&#35; Zsh&#10;wrangler complete zsh &gt;&gt; ~/.zshrc&#10;&#10;&#35; Fish&#10;wrangler complete fish &gt;&gt; ~/.config/fish/config.fish&#10;&#10;&#35; PowerShell&#10;wrangler complete powershell &gt;&gt; $PROFILE&#10;</code></pre>
<p>After adding the script, restart your terminal or source your configuration file for the changes to take effect. Then you can simply press Tab to see available completions:</p>
<pre tabindex="0"><code class="language-sh">wrangler d&lt;TAB&gt;          # completes to &#x27;deploy&#x27;, &#x27;dev&#x27;, &#x27;d1&#x27;, etc.&#10;wrangler kv &lt;TAB&gt;        # shows subcommands: namespace, key, bulk&#10;</code></pre>
<p>Tab completions are dynamically generated from Wrangler's command registry, so they stay up-to-date as new commands and options are added. This feature is powered by <a href="https://github.com/bombshell-dev/tab/"><code>@bomb.sh/tab</code></a>.</p>
<p>See the <a href="/workers/wrangler/commands/general/#complete"><code>wrangler complete</code> documentation</a> for more details.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/12/">Previous</a><span>Page 13 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/14/">Next</a></nav>
