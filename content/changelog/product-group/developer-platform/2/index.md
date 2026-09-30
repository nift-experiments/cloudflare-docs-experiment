---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/developer-platform/2/
  description: '2026-08-31'
  full_title: Developer platform changelog - page 2 | Cloudflare Docs
  head_html: <title>Developer platform changelog - page 2 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-08-31"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/developer-platform/2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Developer platform changelog - page 2"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-08-31"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/developer-platform/2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/developer-platform/2/#page","headline":"Developer platform changelog - page 2 | Cloudflare Docs","description":"2026-08-31","url":"https://developers.cloudflare.com/changelog/product-group/developer-platform/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/developer-platform/2/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="crawl-endpoint-now-respects-the-content-signals-use-directive"><a href="/changelog/post/2026-08-31-crawl-content-use/">Crawl endpoint now respects the Content Signals `use` directive</a></h2>
<p><em>2026-08-31</em></p>
<p>The <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code></a> endpoint now respects the <code>use</code> directive of the <a href="https://contentsignals.org/">Content Signals</a> standard, letting site owners express the maximum level at which their content may be used.</p>
<p>You can declare your intended level with the new <code>contentUse</code> parameter. Allowed values, from least to most permissive, are <code>reference</code> and <code>full</code>, and the default is <code>full</code>. If a target site's <code>robots.txt</code> sets a <code>use</code> level that is more restrictive than your declared <code>contentUse</code>, the crawl request is rejected with a <code>400</code> error.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;,&#10;    &quot;contentUse&quot;: &quot;reference&quot;,&#10;    &quot;formats&quot;: [&quot;markdown&quot;]&#10;  }&#x27;&#10;</code></pre>
<p>For more information, refer to <a href="/browser-run/quick-actions/crawl-endpoint/#content-signals">Content Signals</a> in the <code>/crawl</code> endpoint documentation.</p>


<h2 id="ai-search-now-supports-glm-5-3-flash"><a href="/changelog/post/2026-08-30-glm-5.3-flash/">AI Search now supports GLM-5.3 Flash</a></h2>
<p><em>2026-08-30</em></p>
<p><a href="/ai-search/">AI Search</a> now supports <a href="/workers-ai/models/glm-5.3-flash/"><code>@cf/zai-org/glm-5.3-flash</code></a> for text generation. The model has a 1,048,576-token context window and runs on Workers AI.</p>
<p>To configure the model for an AI Search instance, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>


<h2 id="durable-objects-can-use-up-to-ten-dynamic-workers-concurrently"><a href="/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/">Durable Objects can use up to ten Dynamic Workers concurrently</a></h2>
<p><em>2026-08-28</em></p>
<p><a href="/durable-objects/">Durable Objects</a> can have up to ten distinct <a href="/dynamic-workers/">Dynamic Workers</a> with in-flight requests, increased from four. This limit applies across all concurrent requests to the same Durable Object because they share an input/output (I/O) context. Other Workers can have up to four distinct Dynamic Workers with in-flight requests per request.</p>
<p>Multiple in-flight requests to the same Dynamic Worker count as one toward this limit.</p>
<p>For more information, refer to <a href="/dynamic-workers/platform/limits/">Dynamic Workers limits</a>.</p>


<h2 id="z-ai-glm-5-3-now-available-on-workers-ai"><a href="/changelog/post/2026-08-28-glm-5.3-workers-ai/">Z.ai GLM-5.3 now available on Workers AI</a></h2>
<p><em>2026-08-28</em></p>
<p><a href="/workers-ai/models/glm-5.3/"><code>@cf/zai-org/glm-5.3</code></a> is now available on Workers AI. It is Z.ai's flagship agentic coding model, built for long-running, tool-driven development workflows rather than single-turn chat.</p>
<p>GLM-5.3 uses the same base model as GLM-5.2, with every gain coming from post-training. The results are substantial on coding and agentic benchmarks: <a href="https://huggingface.co/zai-org/GLM-5.3">Z.ai reports</a> a 50% improvement over GLM-5.2 on its in-house Z.ai Code Bench, and calls GLM-5.3 the most capable open-weights model for coding. On public benchmarks, it scores 88.2 on Terminal Bench 2.1 (up from 81.0), 28.3 on Terminal Bench 3.0 — open-source state of the art, up from 4.6 — 66.9 on DeepSWE (up from 46.2), 78.1 on FrontierSWE (up from 67.5), and 42.5 on SWE-Marathon (up from 19.4). It is also the top-scoring model in Z.ai's comparisons on CyberGym for vulnerability discovery (84.5) and on long-horizon automation tasks like AutomationBench (48.2).</p>
<p>The price-to-performance ratio is the compelling part. On Workers AI, GLM-5.3 costs the same as GLM-5.2 — $1.40 per M input tokens, $0.26 per M cached input tokens, and $4.40 per M output tokens — while roughly doubling GLM-5.2's scores on long-horizon benchmarks like SWE-Marathon, and improving them by more than 6x on Terminal Bench 3.0.</p>
<p>GLM-5.3 requires the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> or prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>.</p>
<p>Use GLM-5.3 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API, the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/glm-5.3/">GLM-5.3 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="new-workers-ai-text-generation-models-in-ai-search"><a href="/changelog/post/2026-08-26-new-workers-ai-models/">New Workers AI text generation models in AI Search</a></h2>
<p><em>2026-08-26</em></p>
<p><a href="/ai-search/">AI Search</a> now supports six additional <a href="/workers-ai/">Workers AI</a> models for text generation:</p>
<table>
<thead>
<tr>
<th>Model</th>
<th>Context window (tokens)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/deepseek-ai/deepseek-v4-flash-0731</code></td>
<td>1,048,576</td>
</tr>
<tr>
<td><code>@cf/deepseek-ai/deepseek-v4-pro-0813</code></td>
<td>1,048,576</td>
</tr>
<tr>
<td><code>@cf/openai/gpt-oss-120b</code></td>
<td>128,000</td>
</tr>
<tr>
<td><code>@cf/openai/gpt-oss-20b</code></td>
<td>128,000</td>
</tr>
<tr>
<td><code>@cf/qwen/qwen3.8-27b</code></td>
<td>262,144</td>
</tr>
<tr>
<td><code>@cf/moonshotai/kimi-k2.7-code</code></td>
<td>262,144</td>
</tr>
</tbody>
</table>
<p>These models run on Workers AI, so they do not require an additional provider key. Select a model when creating or updating an AI Search instance in the dashboard or through the API.</p>
<p>For the full list of supported models, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>


<h2 id="create-app-scoped-api-tokens-for-flagship"><a href="/changelog/post/2026-08-26-app-scoped-tokens/">Create app-scoped API tokens for Flagship</a></h2>
<p><em>2026-08-26</em></p>
<p>You can now create <strong>app-scoped API tokens</strong> for <a href="/flagship/">Flagship</a>. These tokens grant access only to the Flagship apps you select, instead of every app in the account.</p>
<p>When you create a custom token, open the resource dropdown (it defaults to <strong>Entire Account</strong>) and select <strong>Specified Flagship apps</strong>. Then choose the app and a <strong>Flagship App</strong> permission: Evaluate, Read, or Write. Account-wide Flagship Evaluate, Read, and Write permissions still exist when you need access to every app.</p>
<p>Use app-scoped tokens in trusted server-side environments, such as Wrangler, CI, or a backend service that should only touch one app.</p>
<p>To create a token, refer to <a href="/flagship/api-tokens/">API tokens</a> or <a href="https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=%5B%7B%22key%22:%22flagship_app%22,%22type%22:%22evaluate%22%7D%5D&amp;scope=specified_flagship_app">open the app-scoped token form</a> in the dashboard.</p>


<h2 id="z-ai-glm-5-3-flash-now-available-on-workers-ai"><a href="/changelog/post/2026-08-26-glm-5.3-flash-workers-ai/">Z.ai GLM-5.3 Flash now available on Workers AI</a></h2>
<p><em>2026-08-26</em></p>
<p><a href="/workers-ai/models/glm-5.3-flash/"><code>@cf/zai-org/glm-5.3-flash</code></a> is now available on Workers AI. It is the first natively multimodal model in the GLM-5 series, built on a Mixture-of-Experts architecture with 320B total parameters and 18B active per token.</p>
<p>GLM-5.3 Flash is the first GLM-family model on Workers AI to support multimodal inputs. It outperforms GLM-5.2 across benchmarks and real-world workloads at a lower price, while approaching Claude Opus 4.8 on coding and agentic benchmarks.</p>
<p>GLM-5.3 Flash requires the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> or prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>.</p>
<p>Use GLM-5.3 Flash through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API, the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/glm-5.3-flash/">GLM-5.3 Flash model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="store-larger-custom-metadata-values-in-ai-search"><a href="/changelog/post/2026-08-25-larger-custom-metadata-values/">Store larger custom metadata values in AI Search</a></h2>
<p><em>2026-08-25</em></p>
<p>AI Search supports larger custom metadata values within a shared 10 KiB metadata envelope for each vector. The envelope includes AI Search system metadata and JSON overhead, so it is not a per-field limit. The first 64 UTF-8 bytes of each indexed string remain filterable.</p>
<p>For details, refer to <a href="/ai-search/configuration/indexing/metadata/">Metadata attributes</a>.</p>


<h2 id="prevent-durable-object-alarm-retries-when-using-ctx-abort"><a href="/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/">Prevent Durable Object alarm retries when using `ctx.abort()`</a></h2>
<p><em>2026-08-25</em></p>
<p>By default, an alarm interrupted by <code>ctx.abort()</code> retries after the Durable Object resets. Pass <code>{ retryAlarm: false }</code> when the alarm should stop instead:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17720.md")</div>
<p>For example, an alarm that deletes its storage can use this option to avoid repeating the cleanup or re-running the Durable Object constructor.</p>
<p>Alarms can run concurrently with other requests to the same Durable Object. If another request calls <code>ctx.abort()</code> while an alarm is running, the <code>retryAlarm</code> option on that call also controls whether the alarm retries.</p>
<p>The default retry prevents an unrelated request from permanently canceling the alarm. Set <code>retryAlarm: false</code> on every abort path that should stop an in-progress alarm, not only on calls from the alarm handler. Existing calls to <code>ctx.abort()</code> keep retrying alarms.</p>
<p>For local development, <code>retryAlarm</code> requires Wrangler 4.126.0 or later.</p>
<p>For more information, refer to <a href="/durable-objects/api/state/#abort"><code>ctx.abort()</code></a>.</p>


<h2 id="preserve-exception-details-in-console-logs"><a href="/changelog/post/2026-08-24-preserve-exception-info/">Preserve exception details in console logs</a></h2>
<p><em>2026-08-24</em></p>
<p>Console methods now preserve exception details in your Worker's logs. When your Worker logs an exception, the corresponding log entry includes the exception name, message, and stack.</p>
<p>For example, your Worker can catch and log an exception:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17814.md")</div>
<p>If you use <a href="/workers/observability/">Workers Observability</a>, your log is automatically enriched with structured error information. The following example shows how the enriched log appears in the Cloudflare dashboard:</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-08-24-error-info.png" alt="Workers Observability log entry showing a caught exception and its stack trace" /></p>
<p>The exception's stack trace appears directly in the log message.</p>
<p>If you send telemetry to a <a href="/workers/observability/logs/tail-workers/">Tail Worker</a>, the Tail Worker now receives a log entry with an <code>errorInfo</code> array:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;message&quot;: [&quot;Request failed:&quot;, &quot;RangeError: Value out of range&quot;],&#10;	&quot;errorInfo&quot;: [&#10;		null,&#10;		{&#10;			&quot;name&quot;: &quot;RangeError&quot;,&#10;			&quot;message&quot;: &quot;Value out of range&quot;,&#10;			&quot;stack&quot;: &quot;RangeError: Value out of range\n    at ...&quot;&#10;		}&#10;	],&#10;	&quot;level&quot;: &quot;error&quot;,&#10;	&quot;timestamp&quot;: 1784851200000&#10;}&#10;</code></pre>
<p>Each <code>errorInfo</code> item corresponds to the console argument at the same index in <code>message</code>. Arguments that are not exceptions have a <code>null</code> entry.</p>


<h2 id="choose-oauth-scopes-for-wrangler-and-the-cloudflare-api-mcp-server"><a href="/changelog/post/2026-08-22-wrangler-mcp-optional-oauth-scopes/">Choose OAuth scopes for Wrangler and the Cloudflare API MCP server</a></h2>
<p><em>2026-08-22</em></p>
<p>Wrangler and the <a href="/agents/model-context-protocol/cloudflare/servers-for-cloudflare/">Cloudflare API MCP server</a> now use optional OAuth scopes. During authorization, you can choose which optional scopes to grant instead of approving every scope requested by each client.</p>
<p>The consent dialog now includes the option to edit the permissions you grant to Wrangler or the Cloudflare API MCP server:</p>
<p><img src="/assets/upstream/images/agents/oauth-optional-scopes-review.png" alt="OAuth consent dialog with an Edit Permissions button" /></p>
<p>You can then choose which specific permissions to grant:</p>
<p><img src="/assets/upstream/images/agents/oauth-optional-scopes-edit.png" alt="OAuth permission editor with controls for individual scopes" /></p>
<p>Required scopes remain selected. Choosing fewer optional scopes limits each tool's access to the permissions needed for your workflow.</p>
<p>If a command or tool call needs a scope that you declined, reauthorize the client and grant that scope.</p>
<p>For more information, refer to <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a> and <a href="/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions">Edit optional permissions</a>.</p>


<h2 id="web-analytics-improves-soft-navigation-measurement-for-single-page-applications-spas"><a href="/changelog/post/2026-08-21-improved-soft-navigation-measurement-for-single-page-applications/">Web Analytics improves soft navigation measurement for Single Page Applications (SPAs)</a></h2>
<p><em>2026-08-21</em></p>
<p>Cloudflare Web Analytics (Real User Monitoring) is rolling out accuracy improvements to client-side soft navigations. <strong>Update: this update is complete as of 2026-09-04.</strong></p>
<p><strong>This change may alter the volume of reported pageviews and visits in the dashboard and GraphQL API. The reported Largest Contentful Paint (LCP) metric may also fluctuate.</strong> The extent of these variances depend on your front-end architecture and visitor traffic patterns.</p>
<p>Single Page Applications (SPAs)—such as websites built with React, Angular, Vue, or Svelte—predominantly use soft navigations. Soft navigations avoid fully unloading the current page and rendering the next one from scratch as visitors navigate.</p>
<p>Any client-side navigation counts as a soft navigation, including navigations intercepted by <a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API">the Navigation API</a> or triggered by <a href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">the History API</a>. This means a non-SPA website can have soft navigation activity if its implementation uses these APIs.</p>
<p>The main improvement comes from <a href="https://developer.chrome.com/docs/web-platform/soft-navigations">Google Chrome's new Soft Navigation API</a>. It natively measures <a href="/web-analytics/data-metrics/core-web-vitals/#core-web-vitals-metrics">Largest Contentful Paint (LCP)</a> on soft navigations, removing a blind spot in perceived loading speed across pageviews.</p>
<p>We've extended our <code>navigationType</code> values to segment these different types of navigations:</p>
<table>
<thead>
<tr>
<th><code>navigationType</code></th>
<th>New?</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>navigate</code></td>
<td>❌</td>
<td>Hard navigations that traditional websites (or &quot;Multi Page Applications&quot;) perform when clicking links or submitting forms</td>
</tr>
<tr>
<td><code>soft-navigation</code></td>
<td>✅</td>
<td>Where <a href="https://developer.chrome.com/docs/web-platform/soft-navigations">the new Soft Navigation API</a> is available and a visitor makes a client-side navigation, we record these events</td>
</tr>
<tr>
<td><code>routing-apis</code></td>
<td>✅</td>
<td>Where the native Soft Navigation API is unavailable (e.g. Safari, Firefox, older Chromium-based browsers), we fallback to measuring soft navigations using <a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API">the Navigation API</a> or <a href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">History API</a>. We cannot collect LCP for these, but the other Core Web Vitals are present.</td>
</tr>
</tbody>
</table>
<p>Prior to this change, we only used History API and all navigations were bucketed into <code>navigate</code>.</p>
<p>For more information, refer to the <a href="/web-analytics/data-metrics/dimensions/#navigation-types">Navigation Types</a> and <a href="/web-analytics/get-started/web-analytics-spa/">Web Analytics SPA</a> documentation pages.</p>


<h2 id="run-more-headless-browsers-concurrently-with-browser-run"><a href="/changelog/post/2026-08-20-limits-increase/">Run more headless browsers concurrently with Browser Run</a></h2>
<p><em>2026-08-20</em></p>
<p><a href="/browser-run/">Browser Run</a> lets you automate headless browsers on Cloudflare's global network. Run full browser sessions for interactive workflows, or use <a href="/browser-run/quick-actions/">Quick Actions</a> for one-request tasks such as screenshots, PDFs, and capturing page content.</p>
<p>If you are on the <a href="/workers/platform/pricing/">Workers Paid plan</a>, your default <a href="/browser-run/limits/#workers-paid">limits</a> are now higher:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Previous</th>
<th>New</th>
</tr>
</thead>
<tbody>
<tr>
<td>Concurrent browsers</td>
<td>120</td>
<td><strong>200</strong></td>
</tr>
<tr>
<td>New browser instances / second</td>
<td>1</td>
<td><strong>3</strong></td>
</tr>
<tr>
<td>Quick Actions requests / second</td>
<td>10</td>
<td><strong>30</strong></td>
</tr>
</tbody>
</table>
<p>You can now run hundreds of browser sessions in parallel, launch new browsers faster, and process three times as many <a href="/browser-run/quick-actions/">Quick Actions</a> per second. These published limits are defaults, not maximums. If your workload needs more more concurrent browsers, <a href="https://forms.gle/CdueDKvb26mTaepa9">request higher limits</a>.</p>


<h2 id="use-fuse-in-local-containers-development"><a href="/changelog/post/2026-08-20-fuse-local-development/">Use FUSE in local Containers development</a></h2>
<p><em>2026-08-20</em></p>
<p>Miniflare now automatically grants local Containers the Docker privileges required for Filesystem in Userspace (FUSE). This applies to <code>wrangler dev</code>, the Cloudflare Vite plugin, and direct Miniflare use.</p>
<p>Miniflare grants these privileges when the local Docker daemon runs inside a virtual machine (VM). This includes Docker engines on macOS and through Windows Subsystem for Linux (WSL). On Linux, Miniflare grants the privileges for local rootless Docker when <code>/dev/fuse</code> is available.</p>
<p>Rootful Docker on Linux does not support FUSE by default during local development. Miniflare does not grant FUSE privileges when the Docker daemon does not meet these conditions or cannot be inspected.</p>
<p>For requirements and troubleshooting, refer to <a href="/containers/guides/local-dev/#fuse-support">FUSE support during local development</a>. For a complete example, refer to <a href="/containers/examples/r2-fuse-mount/">Mount R2 buckets with FUSE</a>.</p>


<h2 id="view-deployments-for-durable-objects-in-the-dashboard"><a href="/changelog/post/2026-08-20-durable-objects-deployments-tab/">View deployments for Durable Objects in the dashboard</a></h2>
<p><em>2026-08-20</em></p>
<p>Durable Object namespaces now have a <strong>Deployments</strong> tab in the Cloudflare dashboard, showing the <a href="/workers/versions-and-deployments/#versions">versions</a> of the backing Worker that are currently live and the traffic split between them.</p>
<p><img src="/assets/upstream/images/changelog/durable-objects/durable-objects-deployments-tab.png" alt="The Deployments tab for a Durable Object namespace, showing two versions with their traffic %, requests/sec, error rate, and median wall time" /></p>
<div class="nb-dash-button"></div>
<p>A Durable Object namespace is backed by a Worker script, so its deployments are the same as that Worker's deployments. Previously, checking on a <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployment</a> in progress for a Durable Object meant navigating to the backing Worker. The new tab surfaces that information directly on the namespace, alongside the metrics that matter for it: requests, error rate, and wall time per version.</p>
<p>The tab is read-only — promoting, rolling back, or splitting traffic on a deployment is still managed from the backing Worker's Deployments tab.</p>
<h4 id="2026-08-20-durable-objects-deployments-tab-actual-vs-configured-traffic-split">Actual vs. configured traffic split</h4>
<p>The <strong>Traffic %</strong> column, for both Workers and Durable Objects, now shows the actual, observed traffic share for each version next to the percentage you configured. Previously, this column only showed the configured percentage. If you moved a deployment from 50/50 to 100% on a new version, the configured number updated immediately, but requests take time to catch up, and there was no way to tell how far along that shift was without checking metrics elsewhere.</p>
<p>The configured split assigns Worker versions to individual Durable Objects, not to individual requests. Because <a href="/workers/versions-and-deployments/gradual-deployments/with-durable-objects/">each Durable Object is pinned to the version it started on until you create a new deployment</a> and some objects naturally receive more traffic than others, the observed split can differ from the configured one for as long as multiple versions are active.</p>
<p>Actual traffic share is calculated from the same <a href="/analytics/graphql-api/">GraphQL Analytics API</a> data that powers other Workers and Durable Objects metrics, so standard ingestion delay and <a href="/analytics/faq/graphql-api-inconsistent-results/">sampling</a> apply. Durable Objects analytics can lag Workers analytics by several minutes, so a version's actual share may take a little longer to catch up after a change.</p>
<p>To view this, go to <strong>Workers &amp; Pages</strong> &gt; <strong>Durable Objects</strong>, select a namespace, then select the <strong>Deployments</strong> tab. For more on how gradual deployments work, refer to <a href="/workers/versions-and-deployments/gradual-deployments/">Gradual deployments</a>.</p>


<h2 id="get-50-off-gpt-5-6-sol-through-ai-gateway"><a href="/changelog/post/2026-08-19-gpt-5-6-sol-discount/">Get 50% off GPT-5.6 Sol through AI Gateway</a></h2>
<p><em>2026-08-19</em></p>
<p>GPT-5.6 Sol is available through AI Gateway, and for a limited time you can use it at 50% off. If you are already using AI Gateway, point to the <code>openai/gpt-5.6-sol</code> model and the discounted pricing applies automatically — no promo code needed.</p>
<p>The promotion is available for <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> users only (not <a href="/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Keys</a>). Load credits onto AI Gateway and start sending requests to <code>openai/gpt-5.6-sol</code>.</p>
<p>Discounted pricing during the promotion:</p>
<table>
<thead>
<tr>
<th>Usage</th>
<th>Promotional price</th>
<th>Standard price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Input</td>
<td>$2.50 per 1M tokens</td>
<td>$5 per 1M tokens</td>
</tr>
<tr>
<td>Output</td>
<td>$15 per 1M tokens</td>
<td>$30 per 1M tokens</td>
</tr>
<tr>
<td>Cache read</td>
<td>$0.25 per 1M tokens</td>
<td>$0.50 per 1M tokens</td>
</tr>
</tbody>
</table>
<p>The promotion runs through September 18, 2026. After that date, GPT-5.6 Sol requests return to standard pricing.</p>
<p>For more details, refer to the <a href="/ai-gateway/features/unified-billing/">Unified Billing documentation</a> and the <a href="/ai/models/openai/gpt-5.6-sol/">GPT-5.6 Sol model page</a>.</p>


<h2 id="cloudflare-vitest-pool-workers-is-now-cloudflare-vitest-plugin"><a href="/changelog/post/2026-08-19-vitest-plugin/">@cloudflare/vitest-pool-workers is now @cloudflare/vitest-plugin</a></h2>
<p><em>2026-08-19</em></p>
<p>Version 1 of the Workers Vitest integration is published as <a href="https://www.npmjs.com/package/@cloudflare/vitest-plugin"><code>@cloudflare/vitest-plugin</code></a>. The package was formerly named <code>@cloudflare/vitest-pool-workers</code>.</p>
<p>The Vitest configuration API is unchanged. Existing projects must update the dependency name, package imports, and TypeScript <code>types</code> entries.</p>
<p>To migrate automatically, run:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx @cloudflare/codemods vitest:pool-workers-to-vitest-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx @cloudflare/codemods vitest:pool-workers-to-vitest-plugin" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn @cloudflare/codemods vitest:pool-workers-to-vitest-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn @cloudflare/codemods vitest:pool-workers-to-vitest-plugin" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm @cloudflare/codemods vitest:pool-workers-to-vitest-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm @cloudflare/codemods vitest:pool-workers-to-vitest-plugin" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The codemod updates your dependency, imports, and test TypeScript configuration. For manual migration steps, refer to <a href="/workers/testing/vitest-integration/migration-guides/migrate-to-vitest-plugin/">Migrate to Vitest plugin</a>.</p>
<p>For outbound request mocks in Workers tests, use the <a href="https://github.com/mswjs/cloudflare"><code>@msw/cloudflare</code></a> integration. Refer to <a href="/workers/testing/vitest-integration/mock-outbound-requests/">Mock outbound requests</a>.</p>


<h2 id="configure-origin-application-settings-for-cloudflare-tunnel-in-the-dashboard"><a href="/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/">Configure origin application settings for Cloudflare Tunnel in the dashboard</a></h2>
<p><em>2026-08-18</em></p>
<p>You can now configure origin application settings directly in the Cloudflare dashboard when adding or editing a published application route for a <a href="/tunnel/">Cloudflare Tunnel</a>. These settings control how <code>cloudflared</code> connects to your origin server and were previously only available in the Cloudflare One dashboard or via local configuration files.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-origin-settings-dashboard.gif" alt="Configure origin application settings in the Cloudflare dashboard" /></p>
<p>When editing a published application, expand <strong>Additional application settings</strong> to configure parameters organized into three categories:</p>
<ul>
<li><strong>HTTP</strong> — Set a custom HTTP Host header or disable chunked encoding.</li>
<li><strong>TLS</strong> — Configure origin server name, CA pool, TLS timeout, disable TLS verification, match SNI to host, or enable HTTP/2 to origin.</li>
<li><strong>Connection</strong> — Tune connect timeout, keep-alive timeout, keep-alive connections, TCP keep-alive interval, proxy type, or disable Happy Eyeballs.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For the full list of origin parameters, refer to <a href="/tunnel/reference/origin-parameters/">Origin parameters</a>.</p>


<h2 id="new-us-jurisdiction-for-r2"><a href="/changelog/post/2026-08-17-r2-us-jurisdiction/">New `us` jurisdiction for R2</a></h2>
<p><em>2026-08-17</em></p>
<p>R2 now supports a <code>us</code> <a href="/r2/reference/data-location/#jurisdictional-restrictions">jurisdiction</a>, which guarantees that bucket data is stored and processed within the United States. Use this jurisdiction when you need explicit US data residency guarantees.</p>
<p>Use the jurisdiction-specific S3 endpoint to create and access buckets in the <code>us</code> jurisdiction:</p>
<p><code>https://&lt;ACCOUNT_ID&gt;.us.r2.cloudflarestorage.com</code></p>
<p>To access a bucket in the <code>us</code> jurisdiction from Workers, set <code>jurisdiction</code> in your R2 binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17741.md")</div>
<p>Once an R2 bucket is created, its jurisdiction cannot be changed.</p>
<p>For setup instructions and the full list of supported jurisdictions, refer to <a href="/r2/reference/data-location/#jurisdictional-restrictions">R2 data location</a>.</p>


<h2 id="qwen-3-8-27b-now-available-on-workers-ai"><a href="/changelog/post/2026-08-17-qwen-3.8-27b-workers-ai/">Qwen 3.8 27B now available on Workers AI</a></h2>
<p><em>2026-08-17</em></p>
<p><a href="/workers-ai/models/qwen3.8-27b/"><code>@cf/qwen/qwen3.8-27b</code></a> is now available on Workers AI.</p>
<p>Qwen 3.8 27B is a 27-billion-parameter instruction-tuned vision language model from Alibaba's Qwen family. It processes images and text together, with reasoning and function calling for agentic workflows.</p>
<p><strong>Key capabilities:</strong></p>
<ul>
<li><strong>Vision</strong>: Accept image and text inputs and generate text responses.</li>
<li><strong>Reasoning</strong>: Support thinking mode for complex, step-by-step problem-solving.</li>
<li><strong>Function calling</strong>: Build agents that invoke tools and APIs across multiple conversation turns.</li>
<li><strong>262,144 token context window</strong>: Retain long conversations and multimodal inputs across extended agent sessions.</li>
</ul>
<p>Use Qwen 3.8 27B through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>) or the REST API at <code>/ai/run</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/qwen3.8-27b/">Qwen 3.8 27B model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="you-can-now-enable-access-on-a-worker-or-all-workers-at-once"><a href="/changelog/post/2026-08-14-workers-access/">You can now enable Access on a Worker or all Workers at once</a></h2>
<p><em>2026-08-14</em></p>
<p>You now have two new ways to protect your <a href="/workers/">Workers</a> with <a href="/workers/configuration/cloudflare-access/">Cloudflare Access</a>.</p>
<p><strong>Protect an application across all its domains at once</strong></p>
<p>Until now, if a Worker was reachable on a route, a Custom Domain, and a <code>workers.dev</code> URL, you had to manually add each one to an Access application and keep the list in sync whenever routes or domains changed.</p>
<p>Now, Access attaches the policy to the Worker itself, so every associated domain and preview URL stays protected even when its routes or domains change.</p>
<p><img src="/assets/upstream/images/changelog/workers/protect-one-worker.png" alt="Access setting for protecting a single Worker" /></p>
<p><strong>Protect all new and existing Workers by default</strong></p>
<p>Make all Workers private by default, so every existing and newly created Worker requires sign-in before anyone can reach it.</p>
<p><img src="/assets/upstream/images/changelog/workers/protect-all-workers.png" alt="Account-wide Access setting that protects all Workers" /></p>
<p>If a specific Worker should remain publicly accessible, add a Worker-level bypass to exempt it.</p>
<p><img src="/assets/upstream/images/changelog/workers/make-worker-public.png" alt="Make a Worker public when all Workers are protected" /></p>
<p>Whether you protect a single application or all Workers at once, you can choose whether to protect preview deployments only or both previews and production, and control who can sign in by Cloudflare account membership, email address, or email domain.</p>
<p>For more advanced policy options, edit the policy in <a href="https://dash.cloudflare.com/?to=/:account/one/access/apps">Zero Trust</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers/choose-who-can-sign-in.png" alt="Access policy configuration for controlling who can sign in" /></p>
<p><strong>View all of your Worker Access policies</strong></p>
<p>You can view and manage all of your Access policies in the <strong>Access</strong> tab of the Workers &amp; Pages section in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers/access-policies.png" alt="Access tab showing all configured Access policies" /></p>
<p><strong>See who is accessing your Worker</strong></p>
<p>When Access is enabled on your Worker, every authenticated request includes <code>ctx.access</code>. Call <a href="/workers/runtime-apis/context/#access"><code>ctx.access.getIdentity()</code></a> to get the user's email, name, and groups — no manual JWT validation required.</p>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    if (!ctx.access) {&#10;      return new Response(&quot;Access did not run&quot;, { status: 401 });&#10;    }&#10;&#10;    const identity = await ctx.access.getIdentity();&#10;    return Response.json({ aud: ctx.access.aud, email: identity?.email });&#10;  },&#10;};&#10;</code></pre>
<p><strong>Test Access locally</strong></p>
<p>You can now test Cloudflare Access locally with <code>wrangler dev</code>. Add a <code>dev</code> block to your <code>wrangler.jsonc</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;access&quot;: {&#10;    &quot;dev&quot;: {&#10;      &quot;aud&quot;: &quot;my-app&quot;,&#10;      &quot;identity&quot;: { &quot;email&quot;: &quot;admin@example.com&quot; }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Your Worker will receive this identity through <code>ctx.access</code> and <code>ctx.access.getIdentity()</code>, letting you test authenticated and unauthenticated flows without deploying. Remove the <code>dev</code> block to simulate unauthenticated requests.</p>
<p><strong>API and programmatic access</strong></p>
<p>You can also set up these policies through the <a href="/workers/configuration/cloudflare-access/">Workers API</a> instead of the dashboard.</p>


<h2 id="deepseek-v4-flash-and-pro-now-available-on-workers-ai"><a href="/changelog/post/2026-08-14-deepseek-v4-workers-ai/">DeepSeek V4 Flash and Pro now available on Workers AI</a></h2>
<p><em>2026-08-14</em></p>
<p><a href="/workers-ai/models/deepseek-v4-pro-0813/"><code>@cf/deepseek-ai/deepseek-v4-pro-0813</code></a> and <a href="/workers-ai/models/deepseek-v4-flash-0731/"><code>@cf/deepseek-ai/deepseek-v4-flash-0731</code></a> are now available on Workers AI.</p>
<p>DeepSeek V4 Flash and DeepSeek V4 Pro are the first Workers AI models with a full <strong>one million (1,048,576) token context window</strong>. Use them for long-horizon agentic workflows, large codebases, and multi-step reasoning that exceed the context limits of every other model hosted on the platform.</p>
<p>DeepSeek V4 Flash is the faster, lower-cost sibling. This release supersedes the preview version with substantially enhanced agentic capabilities.</p>
<p><strong>Key capabilities:</strong></p>
<ul>
<li><strong>Reasoning</strong>: Both models support thinking mode for complex, step-by-step problem-solving.</li>
<li><strong>Function calling</strong>: Build agents that invoke tools and APIs across multiple conversation turns.</li>
<li><strong>Long context</strong>: Both models support a full 1,048,576 token context window.</li>
</ul>
<p>Both models require the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> or prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>.</p>
<p>Use these models through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API, the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/deepseek-v4-pro-0813/">DeepSeek V4 Pro model page</a>, the <a href="/workers-ai/models/deepseek-v4-flash-0731/">DeepSeek V4 Flash model page</a>, and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="data-localization-support-for-artifacts"><a href="/changelog/post/2026-08-13-artifacts-jurisdictions/">Data localization support for Artifacts</a></h2>
<p><em>2026-08-13</em></p>
<p>Artifacts now supports jurisdictions, allowing you to select the European Union or the United States as the only location where repo data is stored and processed.</p>
<p>Select a jurisdiction when you create a namespace. Every repo in that namespace automatically uses the selected jurisdiction.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;namespace&quot;: &quot;my-eu-namespace&quot;,&#10;    &quot;jurisdiction&quot;: &quot;eu&quot;&#10;  }&#x27;&#10;</code></pre>
<p>Jurisdictions cannot be changed after namespace creation. If you omit the jurisdiction, Artifacts creates an unrestricted namespace.</p>
<p>For supported jurisdictions and usage details, refer to <a href="/artifacts/guides/data-localization/">Data localization</a>.</p>


<h2 id="control-realtime-sfu-datachannel-delivery"><a href="/changelog/post/2026-08-13-datachannels-reliability-ordering/">Control Realtime SFU DataChannel delivery</a></h2>
<p><em>2026-08-13</em></p>
<p><a href="/realtime/sfu/">Cloudflare Realtime SFU</a> is a <a href="/realtime/sfu/calls-vs-sfus/">WebRTC selective forwarding unit</a> that runs on Cloudflare's global network. It forwards audio, video, and application data between WebRTC clients without requiring you to manage SFU infrastructure or regions.</p>
<p><a href="/realtime/sfu/datachannels/">DataChannels</a> are WebRTC channels for application messages. A client publishes a named DataChannel to Realtime SFU, and the SFU forwards its messages to every client that subscribes to that channel. Use DataChannels for low-latency payloads such as chat messages, game state, sensor updates, and control events.</p>
<h4 id="2026-08-13-datachannels-reliability-ordering-what-changed">What changed</h4>
<p>Realtime SFU DataChannels now support unordered and partially reliable delivery. DataChannels remain reliable and ordered by default, so existing channels keep their current behavior.</p>
<p>With ordered delivery, a delayed message can block later messages. For game state or sensor updates, recent data may be more useful than recovering an older message. Unordered delivery lets later messages proceed, while partial reliability limits retransmission attempts or delivery time.</p>
<h4 id="2026-08-13-datachannels-reliability-ordering-choose-delivery-behavior">Choose delivery behavior</h4>
<p>Delivery settings answer two questions: whether newer messages can bypass a delayed message, and when the transport should stop retrying delivery.</p>
<p>Choose the policy that matches how long your payload remains useful:</p>
<table>
<thead>
<tr>
<th>Goal</th>
<th>Settings</th>
<th>Use when</th>
</tr>
</thead>
<tbody>
<tr>
<td>Reliable, ordered delivery (default)</td>
<td>Omit <code>ordered</code>, <code>maxRetransmits</code>, and <code>maxPacketLifeTime</code></td>
<td>Messages remain useful and must arrive in order</td>
</tr>
<tr>
<td>Reliable, unordered delivery</td>
<td>Set <code>ordered: false</code>; omit both retry fields</td>
<td>Messages remain useful, but later messages should not wait for earlier messages</td>
</tr>
<tr>
<td>No retries or ordering</td>
<td>Set <code>ordered: false</code> and <code>maxRetransmits: 0</code></td>
<td>The application tolerates message loss and discards out-of-date updates</td>
</tr>
<tr>
<td>Limited retries</td>
<td>Set <code>maxRetransmits: &lt;COUNT&gt;</code></td>
<td>Brief recovery is useful, but repeated retries are not</td>
</tr>
<tr>
<td>Time-bounded delivery</td>
<td>Set <code>maxPacketLifeTime: &lt;MILLISECONDS&gt;</code></td>
<td>A message loses value after a known time window</td>
</tr>
</tbody>
</table>
<p><code>ordered</code> controls ordering independently from retries. <code>maxRetransmits</code> and <code>maxPacketLifeTime</code> are alternative retry budgets, so set at most one for each channel. Omit both for reliable delivery, whether ordered or unordered.</p>
<h4 id="2026-08-13-datachannels-reliability-ordering-apply-the-policy-end-to-end">Apply the policy end to end</h4>
<p>Realtime DataChannels use negotiated IDs, so browsers do not receive delivery settings from the remote peer. Apply the same settings when the publisher creates the local channel, each subscriber pulls the remote channel, and each client calls <code>createDataChannel()</code>.</p>
<p>The following example configures unordered delivery with no retransmissions. It begins after you <a href="/realtime/sfu/datachannels/#set-up-a-datachannel">establish a DataChannel transport on both sessions and complete any required SDP exchange</a>. Run the API requests from your backend with <code>APP_ID</code>, <code>APP_TOKEN</code>, <code>PUBLISHER_SESSION_ID</code>, and <code>SUBSCRIBER_SESSION_ID</code> set in your environment.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17744.md")</div>
<h4 id="2026-08-13-datachannels-reliability-ordering-related-documentation">Related documentation</h4>
<ul>
<li><a href="/realtime/sfu/">Realtime SFU overview</a></li>
<li><a href="/realtime/sfu/datachannels/">DataChannels</a></li>
<li><a href="/realtime/sfu/https-api/">Connection API</a></li>
</ul>


<h2 id="pages-now-skips-superseded-queued-builds"><a href="/changelog/post/2026-08-11-skip-superseded-builds/">Pages now skips superseded queued builds</a></h2>
<p><em>2026-08-11</em></p>
<p>Pages now automatically skips a queued build when a newer build for the same project, branch, and deployment target is also queued.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/">Previous</a><span>Page 2 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/3/">Next</a></nav>
