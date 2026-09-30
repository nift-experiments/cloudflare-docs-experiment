<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-08-28">Aug 28, 2026</time><div>
<h2 id="post-2026-08-28-durable-objects-dynamic-workers-limit"><a href="/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/">Durable Objects can use up to ten Dynamic Workers concurrently</a></h2>
<div class="changelog-badges"><span>workers</span><span>durable-objects</span></div><div class="changelog-body"><p><a href="/durable-objects/">Durable Objects</a> can have up to ten distinct <a href="/dynamic-workers/">Dynamic Workers</a> with in-flight requests, increased from four. This limit applies across all concurrent requests to the same Durable Object because they share an input/output (I/O) context. Other Workers can have up to four distinct Dynamic Workers with in-flight requests per request.</p>
<p>Multiple in-flight requests to the same Dynamic Worker count as one toward this limit.</p>
<p>For more information, refer to <a href="/dynamic-workers/platform/limits/">Dynamic Workers limits</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-28">Aug 28, 2026</time><div>
<h2 id="post-2026-08-28-glm-5.3-workers-ai"><a href="/changelog/post/2026-08-28-glm-5.3-workers-ai/">Z.ai GLM-5.3 now available on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p><a href="/workers-ai/models/glm-5.3/"><code>@cf/zai-org/glm-5.3</code></a> is now available on Workers AI. It is Z.ai's flagship agentic coding model, built for long-running, tool-driven development workflows rather than single-turn chat.</p>
<p>GLM-5.3 uses the same base model as GLM-5.2, with every gain coming from post-training. The results are substantial on coding and agentic benchmarks: <a href="https://huggingface.co/zai-org/GLM-5.3">Z.ai reports</a> a 50% improvement over GLM-5.2 on its in-house Z.ai Code Bench, and calls GLM-5.3 the most capable open-weights model for coding. On public benchmarks, it scores 88.2 on Terminal Bench 2.1 (up from 81.0), 28.3 on Terminal Bench 3.0 — open-source state of the art, up from 4.6 — 66.9 on DeepSWE (up from 46.2), 78.1 on FrontierSWE (up from 67.5), and 42.5 on SWE-Marathon (up from 19.4). It is also the top-scoring model in Z.ai's comparisons on CyberGym for vulnerability discovery (84.5) and on long-horizon automation tasks like AutomationBench (48.2).</p>
<p>The price-to-performance ratio is the compelling part. On Workers AI, GLM-5.3 costs the same as GLM-5.2 — $1.40 per M input tokens, $0.26 per M cached input tokens, and $4.40 per M output tokens — while roughly doubling GLM-5.2's scores on long-horizon benchmarks like SWE-Marathon, and improving them by more than 6x on Terminal Bench 3.0.</p>
<p>GLM-5.3 requires the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> or prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>.</p>
<p>Use GLM-5.3 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API, the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/glm-5.3/">GLM-5.3 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-27">Aug 27, 2026</time><div>
<h2 id="post-2026-08-27-accept-header-caching"><a href="/changelog/post/2026-08-27-accept-header-caching/">APO caches more crawler and bot traffic again</a></h2>
<div class="changelog-badges"><span>automatic-platform-optimization</span></div><div class="changelog-body"><p>We fixed a regression where Automatic Platform Optimization (APO) stopped caching some HTML requests that did not send an explicit <code>Accept: text/html</code> header — commonly crawlers, bots, and uptime monitors. These requests were being served from your origin (<code>cf-cache-status: DYNAMIC</code>) instead of the cache.</p>
<p>APO now caches these requests again. No action is needed. If you added a Transform Rule to set <code>Accept: text/html</code> as a workaround, you can remove it.</p>
<p>For details on how APO decides what to cache, refer to <a href="/automatic-platform-optimization/about/">About APO</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-26">Aug 26, 2026</time><div>
<h2 id="post-2026-08-26-service-token-secret-format"><a href="/changelog/post/2026-08-26-service-token-secret-format/">Access service token secrets use a scannable format</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access service token Client Secrets created on or after August 26, 2026, use the format <code>cfast_[40 alphanumeric characters][8-character checksum]</code>. The prefix and checksum make these credentials easier for secret scanning tools to identify with fewer false positives.</p>
<p>Existing service token secrets continue to work and do not require rotation. Both formats use the same Client ID and the same <code>CF-Access-Client-Id</code> and <code>CF-Access-Client-Secret</code> authentication headers.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Service tokens</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-26">Aug 26, 2026</time><div>
<h2 id="post-2026-08-26-new-workers-ai-models"><a href="/changelog/post/2026-08-26-new-workers-ai-models/">New Workers AI text generation models in AI Search</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports six additional <a href="/workers-ai/">Workers AI</a> models for text generation:</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-26">Aug 26, 2026</time><div>
<h2 id="post-2026-08-26-app-scoped-tokens"><a href="/changelog/post/2026-08-26-app-scoped-tokens/">Create app-scoped API tokens for Flagship</a></h2>
<div class="changelog-badges"><span>flagship</span></div><div class="changelog-body"><p>You can now create <strong>app-scoped API tokens</strong> for <a href="/flagship/">Flagship</a>. These tokens grant access only to the Flagship apps you select, instead of every app in the account.</p>
<p>When you create a custom token, open the resource dropdown (it defaults to <strong>Entire Account</strong>) and select <strong>Specified Flagship apps</strong>. Then choose the app and a <strong>Flagship App</strong> permission: Evaluate, Read, or Write. Account-wide Flagship Evaluate, Read, and Write permissions still exist when you need access to every app.</p>
<p>Use app-scoped tokens in trusted server-side environments, such as Wrangler, CI, or a backend service that should only touch one app.</p>
<p>To create a token, refer to <a href="/flagship/api-tokens/">API tokens</a> or <a href="https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=%5B%7B%22key%22:%22flagship_app%22,%22type%22:%22evaluate%22%7D%5D&amp;scope=specified_flagship_app">open the app-scoped token form</a> in the dashboard.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-26">Aug 26, 2026</time><div>
<h2 id="post-2026-08-26-dataset-deletion"><a href="/changelog/post/2026-08-26-dataset-deletion/">Delete Log Explorer datasets</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>Cloudflare Log Explorer customers can now permanently delete account and zone datasets from the Cloudflare dashboard or API.</p>
<p>Deletion protection is enabled by default to prevent accidental data loss. In the dashboard, go to <a href="/log-explorer/manage-datasets/">Manage datasets</a>, disable deletion protection for the dataset, select <strong>Delete</strong>, and enter the dataset name to confirm.</p>
<p>To delete a dataset through the API, first set <code>deletion_protection</code> to <code>false</code> with the <a href="/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/update/">Update an account or zone dataset</a> method. Then use the <a href="/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/delete/">Delete an account or zone dataset</a> method.</p>
<p>Dataset deletion is irreversible and runs asynchronously. You cannot recreate the same dataset while deletion is in progress.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-26">Aug 26, 2026</time><div>
<h2 id="post-2026-08-26-sentinel-functions-connector-deprecation"><a href="/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/">Azure Functions-based Microsoft Sentinel connector deprecation</a></h2>
<div class="changelog-badges"><span>logpush-connectors</span><span>logs</span></div><div class="changelog-body"><p>Cloudflare Enterprise customers using the <a href="https://marketplace.microsoft.com/en-us/product/cloudflare.cloudflare_sentinel?tab=Overview">Azure Functions-based Microsoft Sentinel connector</a> must migrate to the <a href="https://marketplace.microsoft.com/en-us/product/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">Cloudflare for Microsoft Sentinel Codeless Connector Framework (CCF) connector</a> by 2026-09-14.</p>
<p>Microsoft is deprecating the Azure Monitor HTTP Data Collector API. Support for the API ends on 2026-09-14. As a result, Cloudflare will no longer maintain the Azure Functions-based connector after that date.</p>
<p>To migrate, follow the <a href="/analytics/analytics-integrations/sentinel/">Microsoft Sentinel integration setup guide</a>.</p>
<h4 id="2026-08-26-sentinel-functions-connector-deprecation-additional-resources">Additional resources</h4>
<ul>
<li><a href="https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">Download Cloudflare's CCF Sentinel Solution</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview">Microsoft Sentinel data lake overview</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/sentinel/create-codeless-connector">About the CCF platform</a></li>
</ul>
<p>For more information, refer to Microsoft's <a href="https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/logs/data-collector-api?tabs=powershell">Azure Monitor HTTP Data Collector API deprecation notice</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-26">Aug 26, 2026</time><div>
<h2 id="post-2026-08-26-radar-researcher-improvements"><a href="/changelog/post/2026-08-26-radar-researcher-improvements/">Radar Researcher adds richer sources and URL Scanner explanations</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Cloudflare Radar</strong></a> expands the <a href="https://radar.cloudflare.com/?prompt=">Radar Researcher</a> beta with richer sources and new ways to investigate Internet data.</p>
<h4 id="2026-08-26-radar-researcher-improvements-connected-insights">Connected insights</h4>
<p>Radar Researcher responses can now link to relevant Radar pages, reports, and Cloudflare Blog posts.</p>
<p><img src="/assets/upstream/images/radar/radar-researcher-page-links.png" alt="Radar Researcher response linking to the IP Address Information and Network Quality Test pages" /></p>
<h4 id="2026-08-26-radar-researcher-improvements-url-scanner-report-explanations">URL Scanner report explanations</h4>
<p>Select <strong>Explain with AI</strong> on a <a href="https://radar.cloudflare.com/scan">URL Scanner report</a> to have Radar Researcher explain its findings and answer follow-up questions about the scanned site.</p>
<p><img src="/assets/upstream/images/radar/radar-researcher-url-scanner-explanation.png" alt="Radar Researcher explaining findings from an example.com URL Scanner report" /></p>
<h4 id="2026-08-26-radar-researcher-improvements-improved-shared-sessions">Improved shared sessions</h4>
<p>Shared conversations now open in fullscreen, while the share URL remains available until you close the panel or start a new conversation.</p>
<p>Open <a href="https://radar.cloudflare.com/?prompt=">Radar Researcher</a> to explore these improvements.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-26">Aug 26, 2026</time><div>
<h2 id="post-2026-08-26-emergency-waf-release"><a href="/changelog/post/2026-08-26-emergency-waf-release/">WAF Release - 2026-08-26 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This emergency release updates an existing Next.js remote code execution rule to identify CVE-2026-75604 and adds a new rule for remote code execution in the Next.js Image Optimizer via crafted AVIF images.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2026-75604 affects Windows-hosted Next.js applications using both the Pages Router and App Router without Cache Components and can lead to unauthenticated remote code execution.</p>
</li>
<li>
<p>GHSA-2xp9-vwfh-vxw4 affects the Next.js Image Optimizer and can lead to unauthenticated remote code execution when it optimizes an attacker-controlled AVIF image.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Next.js recommends updating to version 16.3.3 or 15.5.24 to address these vulnerabilities.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2b6b94ec864d47f99630ecf72ca6cce3">2ca6cce3</code>
</td>
<td>N/A</td>
<td>Next.js - Remote Code Execution - CVE:CVE-2026-75604</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="18b22b0bd423423c945b3a0180256efe">80256efe</code>
</td>
<td>N/A</td>
<td>Next.js - Image Optimizer Remote Code Execution via Crafted AVIF</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-26">Aug 26, 2026</time><div>
<h2 id="post-2026-08-26-glm-5.3-flash-workers-ai"><a href="/changelog/post/2026-08-26-glm-5.3-flash-workers-ai/">Z.ai GLM-5.3 Flash now available on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p><a href="/workers-ai/models/glm-5.3-flash/"><code>@cf/zai-org/glm-5.3-flash</code></a> is now available on Workers AI. It is the first natively multimodal model in the GLM-5 series, built on a Mixture-of-Experts architecture with 320B total parameters and 18B active per token.</p>
<p>GLM-5.3 Flash is the first GLM-family model on Workers AI to support multimodal inputs. It outperforms GLM-5.2 across benchmarks and real-world workloads at a lower price, while approaching Claude Opus 4.8 on coding and agentic benchmarks.</p>
<p>GLM-5.3 Flash requires the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> or prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>.</p>
<p>Use GLM-5.3 Flash through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API, the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/glm-5.3-flash/">GLM-5.3 Flash model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-25">Aug 25, 2026</time><div>
<h2 id="post-2026-08-25-service-token-rotation-grace-periods"><a href="/changelog/post/2026-08-25-service-token-rotation-grace-periods/">Grace periods for service token rotation</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access administrators can now choose a grace period when rotating a service token secret. Both secrets remain valid during the grace period, giving administrators time to update services without interrupting authentication.</p>
<p>The dashboard offers grace periods from one hour to 30 days. Administrators can also revoke the previous secret immediately. The API accepts an RFC 3339 expiration time for custom rotation schedules.</p>
<p>For configuration instructions, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#rotate-service-token-secrets">Rotate service token secrets</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-25">Aug 25, 2026</time><div>
<h2 id="post-2026-08-25-service-token-status-controls"><a href="/changelog/post/2026-08-25-service-token-status-controls/">Temporarily turn off Access service tokens</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access administrators can now temporarily turn off service tokens without deleting them. A disabled token cannot authenticate, but its configuration remains available so administrators can turn it on again later.</p>
<p>Turning off a token also stops any previous secret in an active rotation grace period. Use this control to contain suspected credential exposure or pause an automated service.</p>
<p>For configuration instructions, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#turn-a-service-token-on-or-off">Turn a service token on or off</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-25">Aug 25, 2026</time><div>
<h2 id="post-2026-08-25-larger-custom-metadata-values"><a href="/changelog/post/2026-08-25-larger-custom-metadata-values/">Store larger custom metadata values in AI Search</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>AI Search supports larger custom metadata values within a shared 10 KiB metadata envelope for each vector. The envelope includes AI Search system metadata and JSON overhead, so it is not a per-field limit. The first 64 UTF-8 bytes of each indexed string remain filterable.</p>
<p>For details, refer to <a href="/ai-search/configuration/indexing/metadata/">Metadata attributes</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-25">Aug 25, 2026</time><div>
<h2 id="post-2026-08-25-symmetric-jwt-validation"><a href="/changelog/post/2026-08-25-symmetric-jwt-validation/">Symmetric key support for JWT validation</a></h2>
<div class="changelog-badges"><span>api-shield</span></div><div class="changelog-body"><p>API Shield <a href="/api-shield/security/jwt-validation/">JSON Web Token validation</a> now supports symmetric keys that use the <code>HS256</code>, <code>HS384</code>, and <code>HS512</code> algorithms. You can configure HMAC verification keys in the Cloudflare dashboard or with the Cloudflare API.</p>
<p>Cloudflare never stores symmetric credentials in plaintext. API responses do not include the credential.</p>
<p>Refer to <a href="/api-shield/security/jwt-validation/api/#credentials">Configure JWT validation via the API</a> for supported key formats and credential requirements.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-25">Aug 25, 2026</time><div>
<h2 id="post-2026-08-25-mcp-portals-mcp-2026-07-28"><a href="/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/">MCP server portals support MCP 2026-07-28 specification</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support the stateless MCP <code>2026-07-28</code> specification for client and upstream server connections.</p>
<p>The portal's <code>/mcp</code> endpoint automatically accepts stateless MCP <code>2026-07-28</code> requests and earlier 2025 Streamable HTTP clients. When the portal connects to an upstream Streamable HTTP server, it checks for MCP <code>2026-07-28</code> support and falls back to the 2025 handshake when needed. Client and upstream protocol selection are independent, so clients and servers can upgrade separately without portal configuration changes.</p>
<p>SSE connections continue to use the legacy protocol. For details, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#transport">MCP server portal transport and protocol compatibility</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-25">Aug 25, 2026</time><div>
<h2 id="post-2026-08-25-durable-object-alarm-abort-no-retry"><a href="/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/">Prevent Durable Object alarm retries when using `ctx.abort()`</a></h2>
<div class="changelog-badges"><span>durable-objects</span></div><div class="changelog-body"><p>By default, an alarm interrupted by <code>ctx.abort()</code> retries after the Durable Object resets. Pass <code>{ retryAlarm: false }</code> when the alarm should stop instead:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17720.md")</div>
<p>For example, an alarm that deletes its storage can use this option to avoid repeating the cleanup or re-running the Durable Object constructor.</p>
<p>Alarms can run concurrently with other requests to the same Durable Object. If another request calls <code>ctx.abort()</code> while an alarm is running, the <code>retryAlarm</code> option on that call also controls whether the alarm retries.</p>
<p>The default retry prevents an unrelated request from permanently canceling the alarm. Set <code>retryAlarm: false</code> on every abort path that should stop an in-progress alarm, not only on calls from the alarm handler. Existing calls to <code>ctx.abort()</code> keep retrying alarms.</p>
<p>For local development, <code>retryAlarm</code> requires Wrangler 4.126.0 or later.</p>
<p>For more information, refer to <a href="/durable-objects/api/state/#abort"><code>ctx.abort()</code></a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-25">Aug 25, 2026</time><div>
<h2 id="post-2026-08-25-waf-release"><a href="/changelog/post/2026-08-25-waf-release/">WAF Release - 2026-08-25</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release moves four new detections from Log to Block, merges the XSS, HTML Injection - Script Tag - Beta rule into the original rule, and adds a Generic Rules - Remote Code Execution rule in Block mode.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Four new detections move from Log to Block: HTTP/2 Request Smuggling - Request Body Anomaly and XSS - JavaScript Event Handler Coercion across Headers, Body, and URI.</p>
</li>
<li>
<p>The XSS, HTML Injection - Script Tag - Beta rule is merged into the original rule.</p>
</li>
<li>
<p>A Generic Rules - Remote Code Execution detection is added in Block mode.</p>
</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a80f214f0947435dabb2ba2d1489d892">1489d892</code>
</td>
<td>N/A</td>
<td>HTTP/2 Request Smuggling - Request Body Anomaly</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="58a184412d2b4113bca6379b20646260">20646260</code>
</td>
<td>N/A</td>
<td>XSS - JavaScript Event Handler Coercion - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e79cb939d6aa41db984e6db3d706d517">d706d517</code>
</td>
<td>N/A</td>
<td>XSS - JavaScript Event Handler Coercion - Body</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7e3249c7a5d8469697478746660886c8">660886c8</code>
</td>
<td>N/A</td>
<td>XSS - JavaScript Event Handler Coercion - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d34bc5db8cbc4e18a44ed115c293b926">c293b926</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Script Tag - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "XSS, HTML Injection - Script Tag" (ID:{" "}<code class="nb-rule-id" title="9c8dda9708cc4452ac76e7be7b58420b">7b58420b</code>).</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2b6b94ec864d47f99630ecf72ca6cce3">2ca6cce3</code>
</td>
<td>N/A</td>
<td>Generic Rules - Remote Code Execution</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-24">Aug 24, 2026</time><div>
<h2 id="post-2026-08-24-virtual-appliance-self-serve-download"><a href="/changelog/post/2026-08-24-virtual-appliance-self-serve-download/">Download the Cloudflare One Virtual Appliance for your hypervisor from the dashboard</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>When you register a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Virtual Appliance</a>, you can now select your hypervisor and download the appliance directly from the dashboard — no need to look up asset URLs.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-08-24-virtual-appliance-self-serve-download.png" alt="Selecting a hypervisor and downloading the Cloudflare One Virtual Appliance from the Connectors page" /></p>
<ul>
<li>On the <strong>Connectors</strong> page, select <strong>Add an appliance</strong>, choose <strong>Virtual appliance</strong>, then select your hypervisor: <strong>VMware ESXi</strong>, <strong>Proxmox</strong>, or <strong>libvirt/KVM</strong>.</li>
<li>Download the OVA image (VMware ESXi) or the install script (Proxmox and libvirt/KVM) for the selected hypervisor.</li>
<li>Use <strong>View setup guide</strong> to open deployment instructions for your platform.</li>
</ul>
<p>This complements the existing self-serve <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key">registration and license key generation</a> in the dashboard.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#configure-a-virtual-machine">Configure a Cloudflare One Virtual Appliance</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-24">Aug 24, 2026</time><div>
<h2 id="post-2026-08-24-radar-aspa-validation"><a href="/changelog/post/2026-08-24-radar-aspa-validation/">RPKI ASPA path validation on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> adds an <a href="https://radar.cloudflare.com/routing/aspa-validation">ASPA validation tool</a> to its <a href="https://radar.cloudflare.com/routing">Routing section</a>. Enter a BGP <code>AS_PATH</code> and the tool checks it against the <a href="https://blog.cloudflare.com/aspa-secure-internet/">Autonomous System Provider Authorization (ASPA)</a> records currently published in the RPKI, returning a verdict of <code>Valid</code>, <code>Invalid</code>, or <code>Unknown</code>. An <code>Invalid</code> verdict means no chain of provider authorizations covers the whole path, which is the signature of a route leak.</p>
<p>Validation follows <a href="https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/">draft-ietf-sidrops-aspa-verification</a>, so verdicts match those produced by validators implementing the same draft. The draft is still a work in progress and not yet an RFC.</p>
<h4 id="2026-08-24-radar-aspa-validation-enter-a-path">Enter a path</h4>
<p>Paths are read in BGP wire order: the rightmost AS is the origin, and the leftmost AS is the one closest to the collector or router that observed the route. AS numbers can be separated by spaces, commas, or hyphens, with or without an <code>AS</code> prefix. The full ASPA snapshot is loaded into the browser once, so the verdict, graph, and trace update as the path is edited, with no further requests. A set of example paths covers the interesting cases, including a route leak with an AS0 ASPA, where an AS declares that it has no providers at all.</p>
<h4 id="2026-08-24-radar-aspa-validation-choose-an-algorithm">Choose an algorithm</h4>
<p>The draft defines two verification algorithms that differ only in whether a down-ramp is permitted:</p>
<ul>
<li><strong>Upstream</strong> (<a href="https://datatracker.ietf.org/doc/html/draft-ietf-sidrops-aspa-verification#section-5.4">section 5.4</a>) — for routes received from a customer, peer, route server client, or route server. Only an up-ramp is permitted.</li>
<li><strong>Downstream</strong> (<a href="https://datatracker.ietf.org/doc/html/draft-ietf-sidrops-aspa-verification#section-5.5">section 5.5</a>) — for routes received from a provider. Both an up-ramp and a down-ramp are permitted.</li>
</ul>
<p>An <strong>up-ramp</strong> is the run of consecutive customer-to-provider hops from the origin to the apex of the path, and a <strong>down-ramp</strong> is the equivalent run from the announcing neighbor back to that apex. The tool evaluates both algorithms at once and labels each with its verdict, so a path that is legitimate when received from one session type and a leak when received from another is visible without switching modes. Selecting an algorithm drives the graph and the trace.</p>
<h4 id="2026-08-24-radar-aspa-validation-read-the-result">Read the result</h4>
<p>The <strong>ASPA validation graph</strong> draws the path hop by hop, labeling each AS with its role, whether it publishes an ASPA, and how many providers that ASPA authorizes. Every hop is marked <code>Provider+</code>, <code>Not Provider+</code>, or <code>No attestation</code>, and the maximum and minimum bounds of each ramp are drawn against the length of the path. Hops that no ramp reaches are highlighted, because a path the ramps cannot cover end to end is <code>Invalid</code>. The accompanying <strong>ASPA records</strong> table lists every AS in the path with its ASPA status and its authorized providers, each linked to its Radar AS page.</p>
<p><img src="/assets/upstream/images/radar/aspa-validation-graph.png" alt="ASPA validation graph for the path 1003 6939 1299 553, showing a Valid verdict under the downstream algorithm, the Provider+, Not Provider+, and No attestation outcome on each hop, and the up-ramp and down-ramp bounds that together cover the path" /></p>
<h4 id="2026-08-24-radar-aspa-validation-follow-the-algorithm">Follow the algorithm</h4>
<p>The <strong>Algorithm step by step</strong> section shows the derivation rather than just the answer. Two columns run the same scans under different stopping rules: the upper bounds, which test for <code>Invalid</code> and stop only on <code>Not Provider+</code>, and the lower bounds, which test for <code>Unknown</code> and also stop on <code>No Attestation</code>. A hop is <code>Not Provider+</code> when the AS publishes an ASPA that does not list the next AS as a provider, and <code>No Attestation</code> when the AS publishes no ASPA at all. Each column lists the outcome for every hop scanned, marks where the scan stopped, gives the resulting ramp length, and then evaluates the verdict rule with the numbers filled in.</p>
<p><img src="/assets/upstream/images/radar/aspa-validation-algorithm-trace.png" alt="Step-by-step trace for the same path, with the upper-bound and lower-bound columns each listing the up-ramp and down-ramp scans, the ramp lengths they produce, and the verdict rule that neither Invalid nor Unknown satisfies, leaving a Valid verdict" /></p>
<h4 id="2026-08-24-radar-aspa-validation-share-a-validation">Share a validation</h4>
<p>The path and the selected algorithm are kept in the URL, so a link reproduces a result exactly — for example, this <a href="https://radar.cloudflare.com/routing/aspa-validation?path=22652-1299-9498-149765-14789">route leak with an AS0 ASPA</a>. Appending <code>&amp;mode=upstream</code> pins the link to the upstream algorithm. The graph is a standard Radar widget, so it can also be embedded or shared as an image.</p>
<p>The records behind the tool are the same ones served by the <a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot/"><code>/bgp/rpki/aspa/snapshot</code></a> endpoint of the <a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/"><code>ASPA</code></a> API, and the number of records loaded and the snapshot timestamp are shown alongside the input.</p>
<p>Try the <a href="https://radar.cloudflare.com/routing/aspa-validation">ASPA validation tool</a> with a path of your own.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-24">Aug 24, 2026</time><div>
<h2 id="post-2026-08-24-preserve-exception-info"><a href="/changelog/post/2026-08-24-preserve-exception-info/">Preserve exception details in console logs</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Console methods now preserve exception details in your Worker's logs. When your Worker logs an exception, the corresponding log entry includes the exception name, message, and stack.</p>
<p>For example, your Worker can catch and log an exception:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17814.md")</div>
<p>If you use <a href="/workers/observability/">Workers Observability</a>, your log is automatically enriched with structured error information. The following example shows how the enriched log appears in the Cloudflare dashboard:</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-08-24-error-info.png" alt="Workers Observability log entry showing a caught exception and its stack trace" /></p>
<p>The exception's stack trace appears directly in the log message.</p>
<p>If you send telemetry to a <a href="/workers/observability/logs/tail-workers/">Tail Worker</a>, the Tail Worker now receives a log entry with an <code>errorInfo</code> array:</p>
<pre><code class="language-json">{&#10;	&quot;message&quot;: [&quot;Request failed:&quot;, &quot;RangeError: Value out of range&quot;],&#10;	&quot;errorInfo&quot;: [&#10;		null,&#10;		{&#10;			&quot;name&quot;: &quot;RangeError&quot;,&#10;			&quot;message&quot;: &quot;Value out of range&quot;,&#10;			&quot;stack&quot;: &quot;RangeError: Value out of range\n    at ...&quot;&#10;		}&#10;	],&#10;	&quot;level&quot;: &quot;error&quot;,&#10;	&quot;timestamp&quot;: 1784851200000&#10;}&#10;</code></pre>
<p>Each <code>errorInfo</code> item corresponds to the console argument at the same index in <code>message</code>. Arguments that are not exceptions have a <code>null</code> entry.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-22">Aug 22, 2026</time><div>
<h2 id="post-2026-08-22-wrangler-mcp-optional-oauth-scopes"><a href="/changelog/post/2026-08-22-wrangler-mcp-optional-oauth-scopes/">Choose OAuth scopes for Wrangler and the Cloudflare API MCP server</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>Wrangler and the <a href="/agents/model-context-protocol/cloudflare/servers-for-cloudflare/">Cloudflare API MCP server</a> now use optional OAuth scopes. During authorization, you can choose which optional scopes to grant instead of approving every scope requested by each client.</p>
<p>The consent dialog now includes the option to edit the permissions you grant to Wrangler or the Cloudflare API MCP server:</p>
<p><img src="/assets/upstream/images/agents/oauth-optional-scopes-review.png" alt="OAuth consent dialog with an Edit Permissions button" /></p>
<p>You can then choose which specific permissions to grant:</p>
<p><img src="/assets/upstream/images/agents/oauth-optional-scopes-edit.png" alt="OAuth permission editor with controls for individual scopes" /></p>
<p>Required scopes remain selected. Choosing fewer optional scopes limits each tool's access to the permissions needed for your workflow.</p>
<p>If a command or tool call needs a scope that you declined, reauthorize the client and grant that scope.</p>
<p>For more information, refer to <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a> and <a href="/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions">Edit optional permissions</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-21">Aug 21, 2026</time><div>
<h2 id="post-2026-08-21-casb-policies"><a href="/changelog/post/2026-08-21-casb-policies/">Automatically remediate Microsoft 365 and Google Workspace findings with API-based CASB remediation policies</a></h2>
<div class="changelog-badges"><span>casb</span></div><div class="changelog-body"><p><a href="/cloudflare-one/integrations/cloud-and-saas/">Cloudflare CASB</a> is an API-based (agentless) tool that continuously scans your SaaS and cloud applications for security misconfigurations and data exposure. You can now use <strong>CASB remediation policies</strong> to automatically fix a finding or send a webhook the moment CASB detects it, without manual triage.</p>
<h4 id="2026-08-21-casb-policies-remediate-microsoft-365-and-google-workspace-findings">Remediate Microsoft 365 and Google Workspace findings</h4>
<p>A policy can perform a first-party remediation action directly against the SaaS integration API. When a policy triggers, Cloudflare revokes the external sharing configuration without human intervention.</p>
<p>Remediation is currently supported for file-sharing findings in Microsoft 365 and Google Workspace. Support for additional finding types and integrations is coming soon. For the full list of supported finding types, refer to <a href="/cloudflare-one/cloud-and-saas-findings/policies/#run-remediations">Run remediations</a> in the CASB remediation policies documentation.</p>
<h4 id="2026-08-21-casb-policies-send-webhooks">Send webhooks</h4>
<p>A policy can send posture finding data to Slack, ServiceNow, or any other webhook destination. Webhook actions are supported for all posture finding types across CASB integrations.</p>
<p>A single policy can perform both actions: remediate a finding and send a webhook.</p>
<h4 id="2026-08-21-casb-policies-get-started">Get started</h4>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Policies</strong>.</li>
<li>Select <strong>Create a policy</strong>.</li>
<li>Under <strong>Basic information</strong>, enter a <strong>Policy name</strong> and, optionally, a <strong>Description</strong>.</li>
<li>Under <strong>Choose how you want to trigger the policy</strong>, select a <strong>Vendor</strong>, <strong>Integration</strong>, and <strong>Finding type</strong>.</li>
<li>Under <strong>Define what to do with findings that match your trigger</strong>, choose <strong>Run Remediation</strong>, <strong>Send webhooks</strong>, or both.</li>
<li>Under <strong>Status</strong>, turn on <strong>Enable policy</strong>.</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<h4 id="2026-08-21-casb-policies-learn-more">Learn more</h4>
<ul>
<li>Learn how to <a href="/cloudflare-one/cloud-and-saas-findings/policies/">create and manage CASB remediation policies</a> in Cloudflare One.</li>
<li>Configure <a href="/cloudflare-one/integrations/cloud-and-saas/webhooks/">CASB webhooks</a> as a policy destination.</li>
<li>Learn how to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/">manage findings</a> in Cloudflare One.</li>
</ul>
<p>CASB remediation policies are now available in Cloudflare One.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-21">Aug 21, 2026</time><div>
<h2 id="post-2026-08-21-dlp-test-scan"><a href="/changelog/post/2026-08-21-dlp-test-scan/">Test Data Loss Prevention profiles without sending traffic through Gateway</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p><strong>Test scan</strong> lets you check how <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention (DLP)</a> evaluates sample content before you apply a profile to production traffic. Paste text, upload a file, or upload a HAR file, then select the profiles you want to test.</p>
<p><img src="/assets/upstream/images/changelog/dlp/dlp-test-scan.gif" alt="Test scan results showing matched profiles, detection entries, and match context" /></p>
<p>Test scan sends content directly to the DLP scanner. Gateway policies are not evaluated, no traffic passes through Gateway, and no Gateway activity logs are created. Results include matched profiles, detection entries, confidence levels, match context, proximity keywords, file metadata, antivirus status, and OCR output.</p>
<p>Test scan is available to all Cloudflare Zero Trust customers. Profile availability depends on your <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">Zero Trust plan</a>.</p>
<p>For more details, refer to the <a href="/cloudflare-one/data-loss-prevention/test-scan/">Test scan documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-21">Aug 21, 2026</time><div>
<h2 id="post-2026-08-20-contextual-403s"><a href="/changelog/post/2026-08-20-contextual-403s/">Enriched 403 responses for the Cloudflare API</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare API <code>403 Forbidden</code> responses now include a <code>documentation_url</code> field that links directly to the API documentation for the endpoint that was denied. This gives developers, administrators, and agents an immediate path to the relevant docs with role information instead of guessing at which role or permission they are missing for that endpoint.</p>
<p><strong>What's New</strong></p>
<p><strong>Enriched 403 error responses</strong>: When a Cloudflare API request is denied, the error response now includes a <code>documentation_url</code> field that points to the documentation for that specific endpoint. Contextual 403 responses are now available across nearly all Cloudflare product APIs.</p>
<p><strong>Faster troubleshooting</strong>: The linked API docs surface the roles required for each endpoint, making it easier to self-serve access issues.</p>
<p><strong>Better support for tools and agents</strong>: Agents can use the \documentation_url` field to immediately fetch the endpoint's documentation from the 403 error response, identify the accepted permissions for the denied action, and use that context to drive third-party approval workflows.`</p>
<p>Example 403 response:</p>
<pre><code class="language-json">{&#10;  &quot;success&quot;: false,&#10;  &quot;errors&quot;: [&#10;    {&#10;      &quot;code&quot;: 10000,&#10;      &quot;message&quot;: &quot;Forbidden&quot;,&#10;      &quot;documentation_url&quot;: &quot;https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/list&quot;&#10;    }&#10;  ],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: null&#10;}&#10;</code></pre>
<p>For more info:</p>
<ul>
<li><a href="/api/">Browse the Cloudflare API documentation</a></li>
<li><a href="/fundamentals/manage-members/roles/">Review Cloudflare roles</a></li>
<li><a href="/fundamentals/api/reference/permissions/">Review API token permissions</a></li>
</ul>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/2/">Previous</a><span>Page 3 of 50</span><a class="pagination-next" rel="next" href="/changelog/4/">Next</a></nav>
</div>
