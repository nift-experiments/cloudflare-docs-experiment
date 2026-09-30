---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/ai/4/
  description: '2026-04-08'
  full_title: AI changelog - page 4 | Cloudflare Docs
  head_html: <title>AI changelog - page 4 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-04-08"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/ai/4/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="AI changelog - page 4"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-04-08"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/ai/4/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/ai/4/#page","headline":"AI changelog - page 4 | Cloudflare Docs","description":"2026-04-08","url":"https://developers.cloudflare.com/changelog/product-group/ai/4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/ai/4/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="website-source-css-content-selectors-for-precise-content-extraction-in-ai-search"><a href="/changelog/post/2026-04-09-ai-search-content-selectors/">Website Source CSS content selectors for precise content extraction in AI Search</a></h2>
<p><em>2026-04-08</em></p>
<p><a href="/ai-search/">AI Search</a> now supports <a href="/ai-search/configuration/data-source/website/content-selectors/">CSS content selectors</a> for website data sources. You can now define which parts of a crawled page are extracted and indexed by specifying CSS selectors paired with URL glob patterns.</p>
<p>Content selectors solve the problem of indexing only relevant content while ignoring navigation, sidebars, footers, and other boilerplate. When a page URL matches a glob pattern, only elements matching the corresponding CSS selector are extracted and converted to Markdown for indexing.</p>
<p>Configure content selectors via the dashboard or API:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-search/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-ai-search&quot;,&#10;    &quot;source&quot;: &quot;https://example.com&quot;,&#10;    &quot;type&quot;: &quot;web-crawler&quot;,&#10;    &quot;source_params&quot;: {&#10;      &quot;web_crawler&quot;: {&#10;        &quot;parse_options&quot;: {&#10;          &quot;content_selector&quot;: [&#10;            {&#10;              &quot;path&quot;: &quot;**/blog/**&quot;,&#10;              &quot;selector&quot;: &quot;article .post-body&quot;&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Selectors are evaluated in order, and the first matching pattern wins. You can define up to 10 content selector entries per instance.</p>
<p>For configuration details and examples, refer to the <a href="/ai-search/configuration/data-source/website/content-selectors/">content selectors documentation</a>.</p>


<h2 id="new-workers-ai-models-for-text-generation-and-embedding-in-ai-search"><a href="/changelog/post/2026-04-09-new-workers-ai-models/">New Workers AI models for text generation and embedding in AI Search</a></h2>
<p><em>2026-04-08</em></p>
<p><a href="/ai-search/">AI Search</a> now supports four additional <a href="/workers-ai/">Workers AI</a> models across text generation and embedding.</p>
<h4 id="2026-04-09-new-workers-ai-models-text-generation">Text generation</h4>
<table>
<thead>
<tr>
<th>Model</th>
<th>Context window (tokens)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/zai-org/glm-4.7-flash</code></td>
<td>131,072</td>
</tr>
<tr>
<td><code>@cf/qwen/qwen3-30b-a3b-fp8</code></td>
<td>32,000</td>
</tr>
</tbody>
</table>
<p>GLM-4.7-Flash is a lightweight model from Zhipu AI with a 131,072 token context window, suitable for long-document summarization and retrieval tasks. Qwen3-30B-A3B is a mixture-of-experts model from Alibaba that activates only 3 billion parameters per forward pass, keeping inference fast while maintaining strong response quality.</p>
<h4 id="2026-04-09-new-workers-ai-models-embedding">Embedding</h4>
<table>
<thead>
<tr>
<th>Model</th>
<th>Vector dims</th>
<th>Input tokens</th>
<th>Metric</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/qwen/qwen3-embedding-0.6b</code></td>
<td>1,024</td>
<td>4,096</td>
<td>cosine</td>
</tr>
<tr>
<td><code>@cf/google/embeddinggemma-300m</code></td>
<td>768</td>
<td>512</td>
<td>cosine</td>
</tr>
</tbody>
</table>
<p>Qwen3-Embedding-0.6B supports up to 4,096 input tokens, making it a good fit for indexing longer text chunks. EmbeddingGemma-300M from Google produces 768-dimension vectors and is optimized for low-latency embedding workloads.</p>
<p>All four models are available without additional provider keys since they run on Workers AI. Select them when creating or updating an AI Search instance in the dashboard or through the API.</p>
<p>For the full list of supported models, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>


<h2 id="google-gemma-4-26b-a4b-now-available-on-workers-ai"><a href="/changelog/post/2026-04-04-gemma-4-26b-a4b-workers-ai/">Google Gemma 4 26B A4B now available on Workers AI</a></h2>
<p><em>2026-04-04</em></p>
<p>We are partnering with Google to bring <a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a> to Workers AI. Gemma 4 26B A4B is a Mixture-of-Experts (MoE) model built from Gemini 3 research, with 26B total parameters and only 4B active per forward pass. By activating a small subset of parameters during inference, the model runs almost as fast as a 4B-parameter model while delivering the quality of a much larger one.</p>
<p>Gemma 4 is Google's most capable family of open models, designed to maximize intelligence-per-parameter.</p>
<h4 id="2026-04-04-gemma-4-26b-a4b-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Mixture-of-Experts architecture</strong> with 8 active experts out of 128 total (plus 1 shared expert), delivering frontier-level performance at a fraction of the compute cost of dense models</li>
<li><strong>256,000 token context window</strong> for retaining full conversation history, tool definitions, and long documents across extended sessions</li>
<li><strong>Built-in thinking mode</strong> that lets the model reason step-by-step before answering, improving accuracy on complex tasks</li>
<li><strong>Vision understanding</strong> for object detection, document and PDF parsing, screen and UI understanding, chart comprehension, OCR (including multilingual), and handwriting recognition, with support for variable aspect ratios and resolutions</li>
<li><strong>Function calling</strong> with native support for structured tool use, enabling agentic workflows and multi-step planning</li>
<li><strong>Multilingual</strong> with out-of-the-box support for 35+ languages, pre-trained on 140+ languages</li>
<li><strong>Coding</strong> for code generation, completion, and correction</li>
</ul>
<p>Use Gemma 4 26B A4B through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, or the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/gemma-4-26b-a4b-it/">Gemma 4 26B A4B model page</a>.</p>


<h2 id="automatically-retry-on-upstream-provider-failures-on-ai-gateway"><a href="/changelog/post/2026-04-02-auto-retry-upstream-failures/">Automatically retry on upstream provider failures on AI Gateway</a></h2>
<p><em>2026-04-02</em></p>
<p>AI Gateway now supports automatic retries at the gateway level. When an upstream provider returns an error, your gateway retries the request based on the retry policy you configure, without requiring any client-side changes.</p>
<p>You can configure the retry count (up to 5 attempts), the delay between retries (from 100ms to 5 seconds), and the backoff strategy (Constant, Linear, or Exponential). These defaults apply to all requests through the gateway, and per-request headers can override them.</p>
<p><img src="/assets/upstream/images/ai-gateway/auto-retry-changelog.png" alt="Retry Requests settings in the AI Gateway dashboard" /></p>
<p>This is particularly useful when you do not control the client making the request and cannot implement retry logic on the caller side. For more complex failover scenarios — such as failing across different providers — use <a href="/ai-gateway/features/dynamic-routing/">Dynamic Routing</a>.</p>
<p>For more information, refer to <a href="/ai-gateway/configuration/manage-gateway/#retry-requests">Manage gateways</a>.</p>


<h2 id="create-manage-search-ai-search-instances-with-wrangler-cli"><a href="/changelog/post/2026-04-01-ai-search-wrangler-commands/">Create, manage, search AI Search instances with Wrangler CLI</a></h2>
<p><em>2026-04-01</em></p>
<p><a href="/ai-search/">AI Search</a> supports a <code>wrangler ai-search</code> command namespace. Use it to manage instances from the command line.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler ai-search create</code></td>
<td>Create a new instance with an interactive wizard</td>
</tr>
<tr>
<td><code>wrangler ai-search list</code></td>
<td>List all instances in your account</td>
</tr>
<tr>
<td><code>wrangler ai-search get</code></td>
<td>Get details of a specific instance</td>
</tr>
<tr>
<td><code>wrangler ai-search update</code></td>
<td>Update the configuration of an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search delete</code></td>
<td>Delete an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search search</code></td>
<td>Run a search query against an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search stats</code></td>
<td>Get usage statistics for an instance</td>
</tr>
</tbody>
</table>
<p>The <code>create</code> command guides you through setup, choosing a name, source type (<code>r2</code> or <code>web</code>), and data source. You can also pass all options as flags for non-interactive use:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search create my-instance --type r2 --source my-bucket&#10;</code></pre>
<p>Use <code>wrangler ai-search search</code> to query an instance directly from the CLI:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search search my-instance --query &quot;how do I configure caching?&quot;&#10;</code></pre>
<p>All commands support <code>--json</code> for structured output that scripts and AI agents can parse directly.</p>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">Wrangler commands documentation</a>.</p>


<h2 id="advanced-waf-customization-for-ai-crawl-control-blocks"><a href="/changelog/post/2026-03-24-waf-rule-preservation/">Advanced WAF customization for AI Crawl Control blocks</a></h2>
<p><em>2026-03-24</em></p>
<p>AI Crawl Control now supports extending the underlying WAF rule with custom modifications. Any changes you make directly in the WAF custom rules editor — such as adding path-based exceptions, extra user agents, or additional expression clauses — are preserved when you update crawler actions in AI Crawl Control.</p>
<p>If the WAF rule expression has been modified in a way AI Crawl Control cannot parse, a warning banner appears on the <strong>Crawlers</strong> page with a link to view the rule directly in WAF.</p>
<p>For more information, refer to <a href="/ai-crawl-control/features/manage-ai-crawlers/#waf-rule-management">WAF rule management</a>.</p>


<h2 id="agents-sdk-v0-8-0-readable-state-idempotent-schedules-typed-agentclient-and-zod-4"><a href="/changelog/post/2026-03-23-agents-sdk-v0.8.0/">Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4</a></h2>
<p><em>2026-03-23</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> exposes agent state as a readable property, prevents duplicate schedule rows across Durable Object restarts, brings full TypeScript inference to <code>AgentClient</code>, and migrates to Zod 4.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-readable-state-on-useagent-and-agentclient">Readable <code>state</code> on <code>useAgent</code> and <code>AgentClient</code></h4>
<p>Both <code>useAgent</code> (React) and <code>AgentClient</code> (vanilla JS) now expose a <code>state</code> property that reflects the current agent state. Previously, reading state required manually tracking it through the <code>onStateUpdate</code> callback.</p>
<p><strong>React (<code>useAgent</code>)</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17655.md")</div>
<p><code>agent.state</code> is reactive — the component re-renders when state changes from either the server or a client-side <code>setState()</code> call.</p>
<p><strong>Vanilla JS (<code>AgentClient</code>)</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17656.md")</div>
<p>State starts as <code>undefined</code> and is populated when the server sends the initial state on connect (from <code>initialState</code>) or when <code>setState()</code> is called. Use optional chaining (<code>agent.state?.field</code>) for safe access. The <code>onStateUpdate</code> callback continues to work as before — the new <code>state</code> property is additive.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-idempotent-schedule">Idempotent <code>schedule()</code></h4>
<p><code>schedule()</code> now supports an <code>idempotent</code> option that deduplicates by <code>(type, callback, payload)</code>, preventing duplicate rows from accumulating when called in places that run on every Durable Object restart such as <code>onStart()</code>.</p>
<p><strong>Cron schedules are idempotent by default.</strong> Calling <code>schedule(&quot;0 * * * *&quot;, &quot;tick&quot;)</code> multiple times with the same callback, expression, and payload returns the existing schedule row instead of creating a new one. Pass <code>{ idempotent: false }</code> to override.</p>
<p>Delayed and date-scheduled types support opt-in idempotency:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17657.md")</div>
<p>Two new warnings help catch common foot-guns:</p>
<ul>
<li>Calling <code>schedule()</code> inside <code>onStart()</code> without <code>{ idempotent: true }</code> emits a <code>console.warn</code> with actionable guidance (once per callback; skipped for cron and when <code>idempotent</code> is set explicitly).</li>
<li>If an alarm cycle processes 10 or more stale one-shot rows for the same callback, the SDK emits a <code>console.warn</code> and a <code>schedule:duplicate_warning</code> diagnostics channel event.</li>
</ul>
<h4 id="2026-03-23-agents-sdk-v0.8.0-typed-agentclient-with-call-inference-and-stub-proxy">Typed <code>AgentClient</code> with <code>call</code> inference and <code>stub</code> proxy</h4>
<p><code>AgentClient</code> now accepts an optional agent type parameter for full type inference on RPC calls, matching the typed experience already available with <code>useAgent</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17658.md")</div>
<p>State is automatically inferred from the agent type, so <code>onStateUpdate</code> is also typed:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17659.md")</div>
<p>Existing untyped usage continues to work without changes. The RPC type utilities (<code>AgentMethods</code>, <code>AgentStub</code>, <code>RPCMethods</code>) are now exported from <code>agents/client</code> for advanced typing scenarios.
<code>agents</code>, <code>@cloudflare/ai-chat</code>, and <code>@cloudflare/codemode</code> now require <code>zod ^4.0.0</code>. Zod v3 is no longer supported.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-cloudflare-ai-chat-fixes"><code>@cloudflare/ai-chat</code> fixes</h4>
<ul>
<li><strong>Turn serialization</strong> — <code>onChatMessage()</code> and <code>_reply()</code> work is now queued so user requests, tool continuations, and <code>saveMessages()</code> never stream concurrently.</li>
<li><strong>Duplicate messages on stop</strong> — Clicking stop during an active stream no longer splits the assistant message into two entries.</li>
<li><strong>Duplicate messages after tool calls</strong> — Orphaned client IDs no longer leak into persistent storage.</li>
</ul>
<h4 id="2026-03-23-agents-sdk-v0.8.0-keepalive-and-keepalivewhile-are-no-longer-experimental"><code>keepAlive()</code> and <code>keepAliveWhile()</code> are no longer experimental</h4>
<p><code>keepAlive()</code> now uses a lightweight in-memory ref count instead of schedule rows. Multiple concurrent callers share a single alarm cycle. The <code>@experimental</code> tag has been removed from both <code>keepAlive()</code> and <code>keepAliveWhile()</code>.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-cloudflare-codemode-tanstack-ai-integration"><code>@cloudflare/codemode</code>: TanStack AI integration</h4>
<p>A new entry point <code>@cloudflare/codemode/tanstack-ai</code> adds support for <a href="https://tanstack.com/ai">TanStack AI's</a> <code>chat()</code> as an alternative to the Vercel AI SDK's <code>streamText()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17660.md")</div>
<h4 id="2026-03-23-agents-sdk-v0.8.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="new-ai-search-rest-api-endpoints-for-search-and-chat-completions"><a href="/changelog/post/2026-03-23-ai-search-new-rest-api/">New AI Search REST API endpoints for /search and /chat/completions</a></h2>
<p><em>2026-03-23</em></p>
<p><a href="/ai-search/">AI Search</a> now offers new <a href="/ai-search/api/search/rest-api/">REST API</a> endpoints for search and chat that use an OpenAI compatible format. This means you can use the familiar <code>messages</code> array structure that works with existing OpenAI SDKs and tools. The messages array also lets you pass previous messages within a session, so the model can maintain context across multiple turns.</p>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Path</th>
</tr>
</thead>
<tbody>
<tr>
<td>Chat Completions</td>
<td><code>POST /accounts/{account_id}/ai-search/instances/{name}/chat/completions</code></td>
</tr>
<tr>
<td>Search</td>
<td><code>POST /accounts/{account_id}/ai-search/instances/{name}/search</code></td>
</tr>
</tbody>
</table>
<p>Here is an example request to the Chat Completions endpoint using the new <code>messages</code> array format:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/chat/completions \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer {API_TOKEN}&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;system&quot;,&#10;        &quot;content&quot;: &quot;You are a helpful documentation assistant.&quot;&#10;      },&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;How do I get started?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/api/search/rest-api/">AI Search REST API guide</a>.</p>
<h4 id="2026-03-23-ai-search-new-rest-api-migration-from-existing-autorag-api-recommended">Migration from existing AutoRAG API (recommended)</h4>
<p>If you are using the previous AutoRAG API endpoints (<code>/autorag/rags/</code>), we recommend migrating to the new endpoints. The previous AutoRAG API endpoints will continue to be fully supported.</p>
<p>Refer to the <a href="/ai-search/api/migration/rest-api/">migration guide</a> for step-by-step instructions.</p>


<h2 id="ai-search-ui-snippets-and-mcp-support"><a href="/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/">AI Search UI snippets and MCP support</a></h2>
<p><em>2026-03-23</em></p>
<p><a href="/ai-search/">AI Search</a> now supports public endpoints, UI snippets, and MCP, making it easy to add search to your website or connect AI agents.</p>
<p>Public endpoints allow you to expose AI Search capabilities without requiring API authentication. To enable public endpoints:</p>
<ol>
<li>Go to <strong>AI Search</strong> in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your instance, and turn on **Public Endpoint** in **Settings**.
   For more details, refer to [Public endpoint configuration](/ai-search/configuration/retrieval/public-endpoint/).
<h4 id="2026-03-23-ai-search-public-endpoint-and-snippets-ui-snippets">UI snippets</h4>
<p>UI snippets are pre-built search and chat components you can embed in your website. Visit <a href="https://search.ai.cloudflare.com/">search.ai.cloudflare.com</a> to configure and preview components for your AI Search instance.</p>
<p><img src="/assets/upstream/images/ai-search/ui-snippet-search-modal.png" alt="Example of the search-modal-snippet component" /></p>
<p>To add a search modal to your page:</p>
<pre tabindex="0"><code class="language-html">&lt;script&#10;	type=&quot;module&quot;&#10;	src=&quot;https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/assets/v0.0.25/search-snippet.es.js&quot;&#10;&gt;&lt;/script&gt;&#10;&#10;&lt;search-modal-snippet&#10;	api-url=&quot;https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/&quot;&#10;	placeholder=&quot;Search...&quot;&#10;&gt;&#10;&lt;/search-modal-snippet&gt;&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/">UI snippets documentation</a>.</p>
<h4 id="2026-03-23-ai-search-public-endpoint-and-snippets-mcp">MCP</h4>
<p>The MCP endpoint allows AI agents to search your content via the Model Context Protocol. Connect your MCP client to:</p>
<pre tabindex="0"><code class="language-txt">https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/mcp&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/api/search/mcp/">MCP documentation</a>.</p>


<h2 id="custom-metadata-filtering-for-ai-search"><a href="/changelog/post/2026-03-23-custom-metadata-filtering/">Custom metadata filtering for AI Search</a></h2>
<p><em>2026-03-23</em></p>
<p><a href="/ai-search/">AI Search</a> now supports custom metadata filtering, allowing you to define your own metadata fields and filter search results based on attributes like category, version, or any custom field you define.</p>
<h4 id="2026-03-23-custom-metadata-filtering-define-a-custom-metadata-schema">Define a custom metadata schema</h4>
<p>You can define up to 5 custom metadata fields per AI Search instance. Each field has a name and data type (<code>text</code>, <code>number</code>, or <code>boolean</code>):</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer {API_TOKEN}&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-instance&quot;,&#10;    &quot;type&quot;: &quot;r2&quot;,&#10;    &quot;source&quot;: &quot;my-bucket&quot;,&#10;    &quot;custom_metadata&quot;: [&#10;      { &quot;field_name&quot;: &quot;category&quot;, &quot;data_type&quot;: &quot;text&quot; },&#10;      { &quot;field_name&quot;: &quot;version&quot;, &quot;data_type&quot;: &quot;number&quot; },&#10;      { &quot;field_name&quot;: &quot;is_public&quot;, &quot;data_type&quot;: &quot;boolean&quot; }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-03-23-custom-metadata-filtering-add-metadata-to-your-documents">Add metadata to your documents</h4>
<p>How you attach metadata depends on your data source:</p>
<ul>
<li><strong>R2 bucket</strong>: Set metadata using S3-compatible custom headers (<code>x-amz-meta-*</code>) when uploading objects. Refer to <a href="/ai-search/configuration/data-source/r2/#custom-metadata">R2 custom metadata</a> for examples.</li>
<li><strong>Website</strong>: Add <code>&lt;meta&gt;</code> tags to your HTML pages. Refer to <a href="/ai-search/configuration/data-source/website/custom-metadata/">Website custom metadata</a> for details.</li>
</ul>
<h4 id="2026-03-23-custom-metadata-filtering-filter-search-results">Filter search results</h4>
<p>Use custom metadata fields in your search queries alongside built-in attributes like <code>folder</code> and <code>timestamp</code>:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/search \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer {API_TOKEN}&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;How do I configure authentication?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ],&#10;    &quot;ai_search_options&quot;: {&#10;      &quot;retrieval&quot;: {&#10;        &quot;filters&quot;: {&#10;          &quot;category&quot;: &quot;documentation&quot;,&#10;          &quot;version&quot;: { &quot;$gte&quot;: 2.0 }&#10;        }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Learn more in the <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>


<h2 id="moonshot-ai-kimi-k2-5-now-available-on-workers-ai"><a href="/changelog/post/2026-03-19-kimi-k2-5-workers-ai/">Moonshot AI Kimi K2.5 now available on Workers AI</a></h2>
<p><em>2026-03-19</em></p>
<p>Workers AI is officially in the big models game. <a href="/workers-ai/models/kimi-k2.5/"><code>@cf/moonshotai/kimi-k2.5</code></a> is the first frontier-scale open-source model on our AI inference platform — a large model with a full 256k context window, multi-turn tool calling, vision inputs, and structured outputs. By bringing a frontier-scale model directly onto the Cloudflare Developer Platform, you can now run the entire agent lifecycle on a single, unified platform.</p>
<p>The model has proven to be a fast, efficient alternative to larger proprietary models without sacrificing quality. As AI adoption increases, the volume of inference is skyrocketing — now you can access frontier intelligence at a fraction of the cost.</p>
<h4 id="2026-03-19-kimi-k2-5-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>256,000 token context window</strong> for retaining full conversation history, tool definitions, and entire codebases across long-running agent sessions</li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Structured outputs</strong> with JSON mode and JSON Schema support for reliable downstream parsing</li>
<li><strong>Function calling</strong> for integrating external tools and APIs into agent workflows</li>
</ul>
<h4 id="2026-03-19-kimi-k2-5-workers-ai-prefix-caching-and-session-affinity">Prefix caching and session affinity</h4>
<p>When an agent sends a new prompt, it resends all previous prompts, tools, and context from the session. The delta between consecutive requests is usually just a few new lines of input. Prefix caching avoids reprocessing the shared context, saving time and compute from the prefill stage. This means faster Time to First Token (TTFT) and higher Tokens Per Second (TPS) throughput.</p>
<p>Workers AI has done prefix caching, but we are now surfacing cached tokens as a usage metric and offering a discount on cached tokens compared to input tokens (pricing is listed on the <a href="/workers-ai/models/kimi-k2.5/">model page</a>).</p>
<pre tabindex="0"><code class="language-bash">curl -X POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/moonshotai/kimi-k2.5&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;x-session-affinity: ses_12345678&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;system&quot;,&#10;        &quot;content&quot;: &quot;You are a helpful assistant.&quot;&#10;      },&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is prefix caching and why does it matter?&quot;&#10;      }&#10;    ],&#10;    &quot;max_tokens&quot;: 2400,&#10;    &quot;stream&quot;: true&#10;  }&#x27;&#10;</code></pre>
<p>Some clients like <a href="https://opencode.ai">OpenCode</a> implement session affinity automatically. The <a href="https://github.com/cloudflare/agents">Agents SDK</a> starter also sets up the wiring for you.</p>
<h4 id="2026-03-19-kimi-k2-5-workers-ai-redesigned-asynchronous-api">Redesigned asynchronous API</h4>
<p>For volumes of requests that exceed synchronous rate limits, you can submit batches of inferences to be completed asynchronously. We have revamped the <a href="/workers-ai/features/batch-api/">Asynchronous Batch API</a> with a pull-based system that processes queued requests as soon as capacity is available. With internal testing, async requests usually execute within 5 minutes, but this depends on live traffic.</p>
<p>The async API is the best way to avoid capacity errors in durable workflows. It is ideal for use cases that are not real-time, such as code scanning agents or research agents.</p>
<p>To use the asynchronous API, pass <code>queueRequest: true</code>:</p>
<pre tabindex="0"><code class="language-js">// 1. Push a batch of requests into the queue&#10;const res = await env.AI.run(&#10;	&quot;@cf/moonshotai/kimi-k2.5&quot;,&#10;	{&#10;		requests: [&#10;			{&#10;				messages: [{ role: &quot;user&quot;, content: &quot;Tell me a joke&quot; }],&#10;			},&#10;			{&#10;				messages: [{ role: &quot;user&quot;, content: &quot;Explain the Pythagoras theorem&quot; }],&#10;			},&#10;		],&#10;	},&#10;	{ queueRequest: true },&#10;);&#10;&#10;// 2. Grab the request ID&#10;const requestId = res.request_id;&#10;&#10;// 3. Poll for the result&#10;const result = await env.AI.run(&quot;@cf/moonshotai/kimi-k2.5&quot;, {&#10;	request_id: requestId,&#10;});&#10;&#10;if (result.status === &quot;queued&quot; || result.status === &quot;running&quot;) {&#10;	// Retry by polling again&#10;} else {&#10;	return Response.json(result);&#10;}&#10;</code></pre>
<p>You can also set up <a href="/workers-ai/platform/event-subscriptions/">event notifications</a> to know when inference is complete instead of polling.</p>
<h4 id="2026-03-19-kimi-k2-5-workers-ai-get-started">Get started</h4>
<p>Use Kimi K2.5 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, <a href="/ai-gateway/">AI Gateway</a>, or via the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.5/">Kimi K2.5 model page</a>, <a href="/workers-ai/platform/pricing/">pricing</a>, and <a href="/workers-ai/features/prompt-caching/">prompt caching</a>.</p>


<h2 id="cloudflare-codemode-v0-2-1-mcp-barrel-export-zero-dependency-main-entry-point-and-custom-sandbox-modules"><a href="/changelog/post/2026-03-17-codemode-sdk-v0.2.1/">@cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules</a></h2>
<p><em>2026-03-17</em></p>
<p>The latest releases of <a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a> add a new MCP barrel export, remove <code>ai</code> and <code>zod</code> as required peer dependencies from the main entry point, and give you more control over the sandbox.</p>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-new-cloudflare-codemode-mcp-export">New <code>@cloudflare/codemode/mcp</code> export</h4>
<p>A new <code>@cloudflare/codemode/mcp</code> entry point provides two functions that wrap MCP servers with Code Mode:</p>
<ul>
<li><strong><code>codeMcpServer({ server, executor })</code></strong> — wraps an existing MCP server with a single <code>code</code> tool where each upstream tool becomes a typed <code>codemode.*</code> method.</li>
<li><strong><code>openApiMcpServer({ spec, executor, request })</code></strong> — creates <code>search</code> and <code>execute</code> MCP tools from an OpenAPI spec with host-side request proxying and automatic <code>$ref</code> resolution.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17652.md")</div>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-zero-dependency-main-entry-point">Zero-dependency main entry point</h4>
<p><strong>Breaking change in v0.2.0:</strong> <code>generateTypes</code> and the <code>ToolDescriptor</code> / <code>ToolDescriptors</code> types have moved to <code>@cloudflare/codemode/ai</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17653.md")</div>
<p>The main entry point (<code>@cloudflare/codemode</code>) no longer requires the <code>ai</code> or <code>zod</code> peer dependencies. It now exports:</p>
<table>
<thead>
<tr>
<th>Export</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sanitizeToolName</code></td>
<td>Sanitize tool names into valid JS identifiers</td>
</tr>
<tr>
<td><code>normalizeCode</code></td>
<td>Normalize LLM-generated code into async arrow functions</td>
</tr>
<tr>
<td><code>generateTypesFromJsonSchema</code></td>
<td>Generate TypeScript type definitions from plain JSON Schema</td>
</tr>
<tr>
<td><code>jsonSchemaToType</code></td>
<td>Convert a single JSON Schema to a TypeScript type string</td>
</tr>
<tr>
<td><code>DynamicWorkerExecutor</code></td>
<td>Sandboxed code execution via Dynamic Worker Loader</td>
</tr>
<tr>
<td><code>ToolDispatcher</code></td>
<td>RPC target for dispatching tool calls from sandbox to host</td>
</tr>
</tbody>
</table>
<p>The <code>ai</code> and <code>zod</code> peer dependencies are now optional — only required when importing from <code>@cloudflare/codemode/ai</code>.</p>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-custom-sandbox-modules">Custom sandbox modules</h4>
<p><code>DynamicWorkerExecutor</code> now accepts an optional <code>modules</code> option to inject custom ES modules into the sandbox:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17654.md")</div>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-internal-normalization-and-sanitization">Internal normalization and sanitization</h4>
<p><code>DynamicWorkerExecutor</code> now normalizes code and sanitizes tool names internally. You no longer need to call <code>normalizeCode()</code> or <code>sanitizeToolName()</code> before passing code and functions to <code>execute()</code>.</p>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-upgrade">Upgrade</h4>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/codemode@latest&#10;</code></pre>
<p>See the <a href="/agents/tools/codemode/">Code Mode documentation</a> for the full API reference.</p>


<h2 id="log-ai-gateway-request-metadata-without-storing-payloads"><a href="/changelog/post/2026-03-17-collect-log-payload-header/">Log AI Gateway request metadata without storing payloads</a></h2>
<p><em>2026-03-17</em></p>
<p>AI Gateway now supports the <code>cf-aig-collect-log-payload</code> header, which controls whether request and response bodies are stored in logs. By default, this header is set to <code>true</code> and payloads are stored alongside metadata. Set this header to <code>false</code> to skip payload storage while still logging metadata such as token counts, model, provider, status code, cost, and duration.</p>
<p>This is useful when you need usage metrics but do not want to persist sensitive prompt or response data.</p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/$ACCOUNT_ID/$GATEWAY_ID/openai/chat/completions \&#10;  &#45;-header &quot;Authorization: Bearer $TOKEN&quot; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;cf-aig-collect-log-payload: false&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;gpt-4o-mini&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is the email address and phone number of user123?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>For more information, refer to <a href="/ai-gateway/observability/logging/#collect-log-payload-cf-aig-collect-log-payload">Logging</a>.</p>


<h2 id="return-up-to-50-query-results-with-values-or-metadata"><a href="/changelog/post/2026-03-16-topk-limit-increased-to-50/">Return up to 50 query results with values or metadata</a></h2>
<p><em>2026-03-16</em></p>
<p>You can now set <code>topK</code> up to <code>50</code> when a Vectorize query returns values or full metadata. This raises the previous limit of <code>20</code> for queries that use <code>returnValues: true</code> or <code>returnMetadata: &quot;all&quot;</code>.</p>
<p>Use the higher limit when you need more matches in a single query response without dropping values or metadata. Refer to the <a href="/vectorize/reference/client-api/">Vectorize API reference</a> for query options and current <code>topK</code> limits.</p>


<h2 id="nvidia-nemotron-3-super-now-available-on-workers-ai"><a href="/changelog/post/2026-03-11-nemotron-3-super-workers-ai/">NVIDIA Nemotron 3 Super now available on Workers AI</a></h2>
<p><em>2026-03-11</em></p>
<p>We're excited to partner with NVIDIA to bring <a href="/workers-ai/models/nemotron-3-120b-a12b/"><code>@cf/nvidia/nemotron-3-120b-a12b</code></a> to Workers AI. NVIDIA Nemotron 3 Super is a Mixture-of-Experts (MoE) model with a hybrid Mamba-transformer architecture, 120B total parameters, and 12B active parameters per forward pass.</p>
<p>The model is optimized for running many collaborating agents per application. It delivers high accuracy for reasoning, tool calling, and instruction following across complex multi-step tasks.</p>
<p><strong>Key capabilities:</strong></p>
<ul>
<li><strong>Hybrid Mamba-transformer architecture</strong> delivers over 50% higher token generation throughput compared to leading open models, reducing latency for real-world applications</li>
<li><strong>Tool calling</strong> support for building AI agents that invoke tools across multiple conversation turns</li>
<li><strong>Multi-Token Prediction (MTP)</strong> accelerates long-form text generation by predicting several future tokens simultaneously in a single forward pass</li>
<li><strong>32,000 token context window</strong> for retaining conversation history and plan states across multi-step agent workflows</li>
</ul>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2026-03-11-nemotron-3-super-workers-ai-prompt-caching">Prompt caching</h4>
@markup("md", "content/.markup/bodies/17818.md")</aside>
<p>Use Nemotron 3 Super through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, or the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/nemotron-3-120b-a12b/">Nemotron 3 Super model page</a>.</p>


<h2 id="crawl-entire-websites-with-a-single-api-call-using-browser-rendering"><a href="/changelog/post/2026-03-10-br-crawl-endpoint/">Crawl entire websites with a single API call using Browser Rendering</a></h2>
<p><em>2026-03-10</em></p>
<p><em>Edit: this post has been edited to clarify crawling behavior with respect to site guidance.</em></p>
<p>You can now crawl an entire website with a single API call using <a href="/browser-run/">Browser Rendering</a>'s new <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code> endpoint</a>, available in open beta. Submit a starting URL, and pages are automatically discovered, rendered in a headless browser, and returned in multiple formats, including HTML, Markdown, and structured JSON. The endpoint is a <a href="/bots/concepts/bot/verified-bots/">verified bot (intermediary agent)</a> that respects robots.txt and <a href="https://www.cloudflare.com/ai-crawl-control/">AI Crawl Control</a> by default, making it easy for developers to comply with website rules, and making it less likely for crawlers to ignore web-owner guidance. This is great for training models, building RAG pipelines, and researching or monitoring content across a site.</p>
<p>Crawl jobs run asynchronously. You submit a URL, receive a job ID, and check back for results as pages are processed.</p>
<pre tabindex="0"><code class="language-sh">&#35; Initiate a crawl&#10;curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://blog.cloudflare.com/&quot;&#10;  }&#x27;&#10;&#10;&#35; Check results&#10;curl -X GET &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl/{job_id}&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27;&#10;</code></pre>
<p>Key features:</p>
<ul>
<li><strong>Multiple output formats</strong> - Return crawled content as HTML, Markdown, and structured JSON (powered by <a href="/workers-ai/">Workers AI</a>)</li>
<li><strong>Crawl scope controls</strong> - Configure crawl depth, page limits, and wildcard patterns to include or exclude specific URL paths</li>
<li><strong>Automatic page discovery</strong> - Discovers URLs from sitemaps, page links, or both</li>
<li><strong>Incremental crawling</strong> - Use <code>modifiedSince</code> and <code>maxAge</code> to skip pages that haven't changed or were recently fetched, saving time and cost on repeated crawls</li>
<li><strong>Static mode</strong> - Set <code>render: false</code> to fetch static HTML without spinning up a browser, for faster crawling of static sites</li>
<li><strong>Well-behaved bot</strong> - Honors <code>robots.txt</code> directives, including <code>crawl-delay</code></li>
</ul>
<p>Available on both the Workers Free and Paid plans.</p>
<p><strong>Note</strong>: the /crawl endpoint cannot bypass Cloudflare bot detection or captchas, and self-identifies as a bot.</p>
<p>To get started, refer to the <a href="/browser-run/quick-actions/crawl-endpoint/">crawl endpoint documentation</a>.
If you are setting up your own site to be crawled, review the <a href="/browser-run/reference/robots-txt/">robots.txt and sitemaps best practices</a>.</p>


<h2 id="real-time-transcription-in-realtimekit-now-supports-10-languages-with-regional-variants"><a href="/changelog/post/2026-03-06-realtimekit-multilingual-transcription/">Real-time transcription in RealtimeKit now supports 10 languages with regional variants</a></h2>
<p><em>2026-03-06</em></p>
<p><a href="/realtime/realtimekit/ai/transcription/">Real-time transcription</a> in RealtimeKit now supports 10 languages with regional variants, powered by <a href="/workers-ai/models/nova-3/">Deepgram Nova-3</a> running on <a href="/workers-ai/">Workers AI</a>.</p>
<p>During a meeting, participant audio is routed through <a href="/ai-gateway/">AI Gateway</a> to Nova-3 on Workers AI — so transcription runs on Cloudflare's network end-to-end, reducing latency compared to routing through external speech-to-text services.</p>
<p>Set the language when <a href="/realtime/realtimekit/concepts/meeting/">creating a meeting</a> via <code>ai_config.transcription.language</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;ai_config&quot;: {&#10;		&quot;transcription&quot;: {&#10;			&quot;language&quot;: &quot;fr&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Supported languages include English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch — with regional variants like <code>en-AU</code>, <code>en-GB</code>, <code>en-IN</code>, <code>en-NZ</code>, <code>es-419</code>, <code>fr-CA</code>, <code>de-CH</code>, <code>pt-BR</code>, and <code>pt-PT</code>. Use <code>multi</code> for automatic multilingual detection.</p>
<p>If you are building voice agents or real-time translation workflows, your agent can now transcribe in the caller's language natively — no extra services or routing logic needed.</p>
<ul>
<li><a href="/realtime/realtimekit/ai/transcription/">Transcription docs</a></li>
<li><a href="/workers-ai/models/nova-3/">Nova-3 model page</a></li>
<li><a href="/workers-ai/">Workers AI</a></li>
<li><a href="/ai-gateway/">AI Gateway</a></li>
</ul>


<h2 id="browser-rendering-3x-higher-rest-api-request-rate"><a href="/changelog/post/2026-03-04-br-rest-api-limit-increase/">Browser Rendering: 3x higher REST API request rate</a></h2>
<p><em>2026-03-04</em></p>
<p><a href="/browser-run/">Browser Rendering</a> REST API rate limits for Workers Paid plans have been increased from 3 requests per second (180/min) to <strong>10 requests per second (600/min)</strong>. No action is needed to benefit from the higher limit.</p>
<p><img src="/assets/upstream/images/changelog/browser-run/rest-api-limit-increase.png" alt="Browser Rendering REST API rate limit increased from 3 to 10 requests per second" /></p>
<p>The <a href="/browser-run/quick-actions/">REST API</a> lets you perform common browser tasks with a single API call, and you can now do it at a higher rate.</p>
<ul>
<li><a href="/browser-run/quick-actions/content-endpoint/">/content - Fetch HTML</a></li>
<li><a href="/browser-run/quick-actions/screenshot-endpoint/">/screenshot - Capture screenshot</a></li>
<li><a href="/browser-run/quick-actions/pdf-endpoint/">/pdf - Render PDF</a></li>
<li><a href="/browser-run/quick-actions/markdown-endpoint/">/markdown - Extract Markdown from a webpage</a></li>
<li><a href="/browser-run/quick-actions/snapshot/">/snapshot - Take a webpage snapshot</a></li>
<li><a href="/browser-run/quick-actions/scrape-endpoint/">/scrape - Scrape HTML elements</a></li>
<li><a href="/browser-run/quick-actions/json-endpoint/">/json - Capture structured data using AI</a></li>
<li><a href="/browser-run/quick-actions/links-endpoint/">/links - Retrieve links from a webpage</a></li>
</ul>
<p>If you use the <a href="/browser-run/#integration-methods">Browser Sessions</a> method, increases to concurrent browser and new browser limits are coming soon. Stay tuned.</p>
<p>For full details, refer to the <a href="/browser-run/limits/">Browser Rendering limits page</a>.</p>


<h2 id="new-conversion-options-for-markdown-conversion"><a href="/changelog/post/2026-03-04-new-markdown-conversion-options/">New conversion options for Markdown Conversion</a></h2>
<p><em>2026-03-04</em></p>
<p>You can now customize how the <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> service processes different file types by passing a <code>conversionOptions</code> object.</p>
<p>Available options:</p>
<ul>
<li><strong>Images</strong>: Set the language for AI-generated image descriptions</li>
<li><strong>HTML</strong>: Use CSS selectors to extract specific content, or provide a hostname to resolve relative links</li>
<li><strong>PDF</strong>: Exclude metadata from the output</li>
</ul>
<p>Use the <a href="/workers-ai/features/markdown-conversion/usage/binding/"><code>env.AI</code></a> binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17817.md")</div>
<p>Or call the REST API:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  &#45;F &#x27;files=@index.html&#x27; \&#10;  &#45;F &#x27;conversionOptions={&quot;html&quot;: {&quot;cssSelector&quot;: &quot;article.content&quot;}}&#x27;&#10;</code></pre>
<p>For more details, refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/">Conversion Options</a>.</p>


<h2 id="real-time-file-watching-in-sandboxes"><a href="/changelog/post/2026-03-03-sandbox-watch-file-events/">Real-time file watching in Sandboxes</a></h2>
<p><em>2026-03-03</em></p>
<p><a href="/sandbox/">Sandboxes</a> now support real-time filesystem watching via <code>sandbox.watch()</code>. The method returns a <a href="https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events">Server-Sent Events</a> stream backed by native inotify, so your Worker receives <code>create</code>, <code>modify</code>, <code>delete</code>, and <code>move</code> events as they happen inside the container.</p>
<h4 id="2026-03-03-sandbox-watch-file-events-sandbox-watch-path-options"><code>sandbox.watch(path, options)</code></h4>
<p>Pass a directory path and optional filters. The returned stream is a standard <code>ReadableStream</code> you can proxy directly to a browser client or consume server-side.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17650.md")</div>
<h4 id="2026-03-03-sandbox-watch-file-events-server-side-consumption-with-parsessestream">Server-side consumption with <code>parseSSEStream</code></h4>
<p>Use <code>parseSSEStream</code> to iterate over events inside a Worker without forwarding them to a client.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17651.md")</div>
<p>Each event includes a <code>type</code> field (<code>create</code>, <code>modify</code>, <code>delete</code>, or <code>move</code>) and the affected <code>path</code>. Move events also include a <code>from</code> field with the original path.</p>
<h4 id="2026-03-03-sandbox-watch-file-events-options">Options</h4>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>recursive</code></td>
<td><code>boolean</code></td>
<td>Watch subdirectories. Defaults to <code>false</code>.</td>
</tr>
<tr>
<td><code>include</code></td>
<td><code>string[]</code></td>
<td>Glob patterns to filter events. Omit to receive all events.</td>
</tr>
</tbody>
</table>
<h4 id="2026-03-03-sandbox-watch-file-events-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/sandbox@latest&#10;</code></pre>
<p>For full API details, refer to the <a href="/sandbox/api/file-watching/">Sandbox file watching reference</a>.</p>


<h2 id="agents-sdk-v0-7-0-observability-rewrite-keepalive-and-waitformcpconnections"><a href="/changelog/post/2026-03-02-agents-sdk-v0.7.0/">Agents SDK v0.7.0: Observability rewrite, keepAlive, and waitForMcpConnections</a></h2>
<p><em>2026-03-02</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> rewrites observability from scratch with <code>diagnostics_channel</code>, adds <code>keepAlive()</code> to prevent Durable Object eviction during long-running work, and introduces <code>waitForMcpConnections</code> so MCP tools are always available when <code>onChatMessage</code> runs.</p>
<h4 id="2026-03-02-agents-sdk-v0.7.0-observability-rewrite">Observability rewrite</h4>
<p>The previous observability system used <code>console.log()</code> with a custom <code>Observability.emit()</code> interface. v0.7.0 replaces it with structured events published to <a href="/workers/runtime-apis/nodejs/diagnostics-channel/">diagnostics channels</a> — silent by default, zero overhead when nobody is listening.</p>
<p>Every event has a <code>type</code>, <code>payload</code>, and <code>timestamp</code>. Events are routed to seven named channels:</p>
<table>
<thead>
<tr>
<th>Channel</th>
<th>Event types</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agents:state</code></td>
<td><code>state:update</code></td>
</tr>
<tr>
<td><code>agents:rpc</code></td>
<td><code>rpc</code>, <code>rpc:error</code></td>
</tr>
<tr>
<td><code>agents:message</code></td>
<td><code>message:request</code>, <code>message:response</code>, <code>message:clear</code>, <code>message:cancel</code>, <code>message:error</code>, <code>tool:result</code>, <code>tool:approval</code></td>
</tr>
<tr>
<td><code>agents:schedule</code></td>
<td><code>schedule:create</code>, <code>schedule:execute</code>, <code>schedule:cancel</code>, <code>schedule:retry</code>, <code>schedule:error</code>, <code>queue:retry</code>, <code>queue:error</code></td>
</tr>
<tr>
<td><code>agents:lifecycle</code></td>
<td><code>connect</code>, <code>destroy</code></td>
</tr>
<tr>
<td><code>agents:workflow</code></td>
<td><code>workflow:start</code>, <code>workflow:event</code>, <code>workflow:approved</code>, <code>workflow:rejected</code>, <code>workflow:terminated</code>, <code>workflow:paused</code>, <code>workflow:resumed</code>, <code>workflow:restarted</code></td>
</tr>
<tr>
<td><code>agents:mcp</code></td>
<td><code>mcp:client:preconnect</code>, <code>mcp:client:connect</code>, <code>mcp:client:authorize</code>, <code>mcp:client:discover</code></td>
</tr>
</tbody>
</table>
<p>Use the typed <code>subscribe()</code> helper from <code>agents/observability</code> for type-safe access:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17645.md")</div>
<p>In production, all diagnostics channel messages are automatically forwarded to <a href="/workers/observability/logs/tail-workers/">Tail Workers</a> — no subscription code needed in the agent itself:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17646.md")</div>
<p>The custom <code>Observability</code> override interface is still supported for users who need to filter or forward events to external services.</p>
<p>For the full event reference, refer to the <a href="/agents/runtime/operations/observability/diagnostics-channels/">Diagnostics channels documentation</a>.</p>
<h4 id="2026-03-02-agents-sdk-v0.7.0-keepalive-and-keepalivewhile"><code>keepAlive()</code> and <code>keepAliveWhile()</code></h4>
<p>Durable Objects are evicted after a period of inactivity (typically 70-140 seconds with no incoming requests, WebSocket messages, or alarms). During long-running operations — streaming LLM responses, waiting on external APIs, running multi-step computations — the agent can be evicted mid-flight.</p>
<p><code>keepAlive()</code> prevents this by creating a 30-second heartbeat schedule. The alarm firing resets the inactivity timer. Returns a disposer function that cancels the heartbeat when called.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17647.md")</div>
<p><code>keepAliveWhile()</code> wraps an async function with automatic cleanup — the heartbeat starts before the function runs and stops when it completes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17648.md")</div>
<p>Key details:</p>
<ul>
<li><strong>Multiple concurrent callers</strong> — Each <code>keepAlive()</code> call returns an independent disposer. Disposing one does not affect others.</li>
<li><strong>AIChatAgent built-in</strong> — <code>AIChatAgent</code> automatically calls <code>keepAlive()</code> during streaming responses. You do not need to add it yourself.</li>
<li><strong>Uses the scheduling system</strong> — The heartbeat does not conflict with your own schedules. It shows up in <code>getSchedules()</code> if you need to inspect it.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17644.md")</aside>
<p>For the full API reference and when-to-use guidance, refer to <a href="/agents/runtime/execution/schedule-tasks/#keeping-the-agent-alive">Schedule tasks — Keeping the agent alive</a>.</p>
<h4 id="2026-03-02-agents-sdk-v0.7.0-waitformcpconnections"><code>waitForMcpConnections</code></h4>
<p><code>AIChatAgent</code> now waits for MCP server connections to settle before calling <code>onChatMessage</code>. This ensures <code>this.mcp.getAITools()</code> returns the full set of tools, especially after Durable Object hibernation when connections are being restored in the background.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17649.md")</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>{ timeout: 10_000 }</code></td>
<td>Wait up to 10 seconds (default)</td>
</tr>
<tr>
<td><code>{ timeout: N }</code></td>
<td>Wait up to <code>N</code> milliseconds</td>
</tr>
<tr>
<td><code>true</code></td>
<td>Wait indefinitely until all connections ready</td>
</tr>
<tr>
<td><code>false</code></td>
<td>Do not wait (old behavior before 0.2.0)</td>
</tr>
</tbody>
</table>
<p>For lower-level control, call <code>this.mcp.waitForConnections()</code> directly inside <code>onChatMessage</code> instead.</p>
<h4 id="2026-03-02-agents-sdk-v0.7.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>MCP deduplication by name and URL</strong> — <code>addMcpServer</code> with HTTP transport now deduplicates on both server name and URL. Calling it with the same name but a different URL creates a new connection. URLs are normalized before comparison (trailing slashes, default ports, hostname case).</li>
<li><strong><code>callbackHost</code> optional for non-OAuth servers</strong> — <code>addMcpServer</code> no longer requires <code>callbackHost</code> when connecting to MCP servers that do not use OAuth.</li>
<li><strong>MCP URL security</strong> — Server URLs are validated before connection to prevent SSRF. Private IP ranges, loopback addresses, link-local addresses, and cloud metadata endpoints are blocked.</li>
<li><strong>Custom denial messages</strong> — <code>addToolOutput</code> now supports <code>state: &quot;output-error&quot;</code> with <code>errorText</code> for custom denial messages in human-in-the-loop tool approval flows.</li>
<li><strong><code>requestId</code> in chat options</strong> — <code>onChatMessage</code> options now include a <code>requestId</code> for logging and correlating events.</li>
</ul>
<h4 id="2026-03-02-agents-sdk-v0.7.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="get-started-with-ai-gateway-automatically"><a href="/changelog/post/2026-03-02-default-gateway/">Get started with AI Gateway automatically</a></h2>
<p><em>2026-03-02</em></p>
<p>You can now start using AI Gateway with a single API call — no setup required. Use <code>default</code> as your gateway ID, and AI Gateway creates one for you automatically on the first request.</p>
<p>To try it out, <a href="/fundamentals/api/get-started/create-token/">create an API token</a> with <code>AI Gateway - Read</code>, <code>AI Gateway - Edit</code>, and <code>Workers AI - Read</code> permissions, then run:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/$CLOUDFLARE_ACCOUNT_ID/default/compat/chat/completions \&#10;  &#45;-header &quot;cf-aig-authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>AI Gateway gives you logging, caching, rate limiting, and access to multiple AI providers through a single endpoint. For more information, refer to <a href="/ai-gateway/get-started/">Get started</a>.</p>


<h2 id="agents-sdk-v0-6-0-rpc-transport-for-mcp-optional-oauth-hardened-schema-conversion-and-cloudflare-ai-chat-fixes"><a href="/changelog/post/2026-02-25-agents-sdk-v0.6.0/">Agents SDK v0.6.0: RPC transport for MCP, optional OAuth, hardened schema conversion, and @cloudflare/ai-chat fixes</a></h2>
<p><em>2026-02-25</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> lets you define an Agent and an McpAgent in the same Worker and connect them over RPC — no HTTP, no network overhead. It also makes OAuth opt-in for simple MCP connections, hardens the schema converter for production workloads, and ships a batch of <code>@cloudflare/ai-chat</code> reliability fixes.</p>
<h4 id="2026-02-25-agents-sdk-v0.6.0-rpc-transport-for-mcp">RPC transport for MCP</h4>
<p>You can now connect an Agent to an McpAgent in the same Worker using a Durable Object binding instead of an HTTP URL. The connection stays entirely within the Cloudflare runtime — no network round-trips, no serialization overhead.</p>
<p>Pass the Durable Object namespace directly to <code>addMcpServer</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17642.md")</div>
<p>The <code>addMcpServer</code> method now accepts <code>string | DurableObjectNamespace</code> as the second parameter with full TypeScript overloads, so HTTP and RPC paths are type-safe and cannot be mixed.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>Hibernation support</strong> — RPC connections survive Durable Object hibernation automatically. The binding name and props are persisted to storage and restored on wake-up, matching the behavior of HTTP MCP connections.</li>
<li><strong>Deduplication</strong> — Calling <code>addMcpServer</code> with the same server name returns the existing connection instead of creating duplicates. Connection IDs are stable across hibernation restore.</li>
<li><strong>Smaller surface area</strong> — The RPC transport internals have been rewritten and reduced from 609 lines to 245 lines. <code>RPCServerTransport</code> now uses <code>JSONRPCMessageSchema</code> from the MCP SDK for validation instead of hand-written checks.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17641.md")</aside>
<h4 id="2026-02-25-agents-sdk-v0.6.0-optional-oauth-for-mcp-connections">Optional OAuth for MCP connections</h4>
<p><code>addMcpServer()</code> no longer eagerly creates an OAuth provider for every connection. For servers that do not require authentication, a simple call is all you need:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17643.md")</div>
<p>If the server responds with a 401, the SDK throws a clear error: <code>&quot;This MCP server requires OAuth authentication. Provide callbackHost in addMcpServer options to enable the OAuth flow.&quot;</code> The restore-from-storage flow also handles missing callback URLs gracefully, skipping auth provider creation for non-OAuth servers.</p>
<h4 id="2026-02-25-agents-sdk-v0.6.0-hardened-json-schema-to-typescript-converter">Hardened JSON Schema to TypeScript converter</h4>
<p>The schema converter used by <code>generateTypes()</code> and <code>getAITools()</code> now handles edge cases that previously caused crashes in production:</p>
<ul>
<li><strong>Depth and circular reference guards</strong> — Prevents stack overflows on recursive or deeply nested schemas</li>
<li><strong><code>$ref</code> resolution</strong> — Supports internal JSON Pointers (<code>#/definitions/...</code>, <code>#/$defs/...</code>, <code>#</code>)</li>
<li><strong>Tuple support</strong> — <code>prefixItems</code> (JSON Schema 2020-12) and array <code>items</code> (draft-07)</li>
<li><strong>OpenAPI 3.0 <code>nullable: true</code></strong> — Supported across all schema branches</li>
<li><strong>Per-tool error isolation</strong> — One malformed schema cannot crash the full pipeline in <code>generateTypes()</code> or <code>getAITools()</code></li>
<li><strong>Missing <code>inputSchema</code> fallback</strong> — <code>getAITools()</code> falls back to <code>{ type: &quot;object&quot; }</code> instead of throwing</li>
</ul>
<h4 id="2026-02-25-agents-sdk-v0.6.0-cloudflare-ai-chat-fixes"><code>@cloudflare/ai-chat</code> fixes</h4>
<ul>
<li><strong>Tool denial flow</strong> — Denied tool approvals (<code>approved: false</code>) now transition to <code>output-denied</code> with a <code>tool_result</code>, fixing Anthropic provider compatibility. Custom denial messages are supported via <code>state: &quot;output-error&quot;</code> and <code>errorText</code>.</li>
<li><strong>Abort/cancel support</strong> — Streaming responses now properly cancel the reader loop when the abort signal fires and send a done signal to the client.</li>
<li><strong>Duplicate message persistence</strong> — <code>persistMessages()</code> now reconciles assistant messages by content and order, preventing duplicate rows when clients resend full history.</li>
<li><strong><code>requestId</code> in <code>OnChatMessageOptions</code></strong> — Handlers can now send properly-tagged error responses for pre-stream failures.</li>
<li><strong><code>redacted_thinking</code> preservation</strong> — The message sanitizer no longer strips Anthropic <code>redacted_thinking</code> blocks.</li>
<li><strong><code>/get-messages</code> reliability</strong> — Endpoint handling moved from a prototype <code>onRequest()</code> override to a constructor wrapper, so it works even when users override <code>onRequest</code> without calling <code>super.onRequest()</code>.</li>
<li><strong>Client tool APIs undeprecated</strong> — <code>createToolsFromClientSchemas</code>, <code>clientTools</code>, <code>AITool</code>, <code>extractClientToolSchemas</code>, and the <code>tools</code> option on <code>useAgentChat</code> are restored for SDK use cases where tools are defined dynamically at runtime.</li>
<li><strong><code>jsonSchema</code> initialization</strong> — Fixed <code>jsonSchema not initialized</code> error when calling <code>getAITools()</code> in <code>onChatMessage</code>.</li>
</ul>
<h4 id="2026-02-25-agents-sdk-v0.6.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="backup-and-restore-api-for-sandbox-sdk"><a href="/changelog/post/2026-02-23-sandbox-backup-restore-api/">Backup and restore API for Sandbox SDK</a></h2>
<p><em>2026-02-23</em></p>
<p><a href="/sandbox/">Sandboxes</a> now support <code>createBackup()</code> and <code>restoreBackup()</code> methods for creating and restoring point-in-time snapshots of directories.</p>
<p>This allows you to restore environments quickly. For instance, in order to develop in a sandbox, you may need to include a user's codebase and run a build step.
Unfortunately <code>git clone</code> and <code>npm install</code> can take minutes, and you don't want to run these steps every time the user starts their sandbox.</p>
<p>Now, after the initial setup, you can just call <code>createBackup()</code>, then <code>restoreBackup()</code> the next time this environment is needed. This makes it practical to pick up exactly
where a user left off, even after days of inactivity, without repeating expensive setup steps.</p>
<pre tabindex="0"><code class="language-ts">const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;&#10;// Make non-trivial changes to the file system&#10;await sandbox.gitCheckout(endUserRepo, { targetDir: &quot;/workspace&quot; });&#10;await sandbox.exec(&quot;npm install&quot;, { cwd: &quot;/workspace&quot; });&#10;&#10;// Create a point-in-time backup of the directory&#10;const backup = await sandbox.createBackup({ dir: &quot;/workspace&quot; });&#10;&#10;// Store the handle for later use&#10;await env.KV.put(`backup:${userId}`, JSON.stringify(backup));&#10;&#10;// ... in a future session...&#10;&#10;// Restore instead of re-cloning and reinstalling&#10;await sandbox.restoreBackup(backup);&#10;</code></pre>
<p>Backups are stored in <a href="/r2">R2</a> and can take advantage of <a href="/sandbox/guides/backup-restore/#configure-r2-lifecycle-rules-for-automatic-cleanup">R2 object lifecycle rules</a> to ensure they do not persist forever.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>Persist and reuse across sandbox sessions</strong> — Easily store backup handles in KV, D1, or Durable Object storage for use in subsequent sessions</li>
<li><strong>Usable across multiple instances</strong> — Fork a backup across many sandboxes for parallel work</li>
<li><strong>Named backups</strong> — Provide optional human-readable labels for easier management</li>
<li><strong>TTLs</strong> — Set time-to-live durations so backups are automatically removed from storage once they are no longer needed</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17640.md")</aside>
<p>To get started, refer to the <a href="/sandbox/guides/backup-restore/">backup and restore guide</a> for setup instructions and usage patterns, or the <a href="/sandbox/api/backups/">Backups API reference</a> for full method documentation.</p>


<h2 id="cloudflare-codemode-v0-1-0-a-new-runtime-agnostic-modular-architecture"><a href="/changelog/post/2026-02-20-codemode-sdk-rewrite/">@cloudflare/codemode v0.1.0: a new runtime agnostic modular architecture</a></h2>
<p><em>2026-02-20</em></p>
<p>The <a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a> package has been rewritten into a modular, runtime-agnostic SDK.</p>
<p><a href="https://blog.cloudflare.com/code-mode/">Code Mode</a> enables LLMs to write and execute code that orchestrates your tools, instead of calling them one at a time. This can (and does) yield significant token savings, reduces context window pressure and improves overall model performance on a task.</p>
<p>The new <code>Executor</code> interface is runtime agnostic and comes with a prebuilt <code>DynamicWorkerExecutor</code> to run generated code in a <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker Loader</a>.</p>
<h4 id="2026-02-20-codemode-sdk-rewrite-breaking-changes">Breaking changes</h4>
<ul>
<li>Removed <code>experimental_codemode()</code> and <code>CodeModeProxy</code> — the package no longer owns an LLM call or model choice</li>
<li>New import path: <code>createCodeTool()</code> is now exported from <code>@cloudflare/codemode/ai</code></li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-new-features">New features</h4>
<ul>
<li><strong><code>createCodeTool()</code></strong> — Returns a standard AI SDK <code>Tool</code> to use in your AI agents.</li>
<li><strong><code>Executor</code> interface</strong> — Minimal <code>execute(code, fns)</code> contract. Implement for any code sandboxing primitive or runtime.</li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-dynamicworkerexecutor"><code>DynamicWorkerExecutor</code></h4>
<p>Runs code in a <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a>. It comes with the following features:</p>
<ul>
<li><strong>Network isolation</strong> — <code>fetch()</code> and <code>connect()</code> blocked by default (<code>globalOutbound: null</code>) when using <code>DynamicWorkerExecutor</code></li>
<li><strong>Console capture</strong> — <code>console.log/warn/error</code> captured and returned in <code>ExecuteResult.logs</code></li>
<li><strong>Execution timeout</strong> — Configurable via <code>timeout</code> option (default 30s)</li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-usage">Usage</h4>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17638.md")</div>
<h4 id="2026-02-20-codemode-sdk-rewrite-wrangler-configuration">Wrangler configuration</h4>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17639.md")</div>
<p>See the <a href="/agents/tools/codemode/">Code Mode documentation</a> for full API reference and examples.</p>
<h4 id="2026-02-20-codemode-sdk-rewrite-upgrade">Upgrade</h4>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/codemode@latest&#10;</code></pre>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/ai/3/">Previous</a><span>Page 4 of 7</span><a class="pagination-next" rel="next" href="/changelog/product-group/ai/5/">Next</a></nav>
