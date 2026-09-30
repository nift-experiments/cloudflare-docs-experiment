---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/ai-gateway/
  description: '2026-09-14'
  full_title: ai-gateway changelog | Cloudflare Docs
  head_html: <title>ai-gateway changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-14"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/ai-gateway/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="ai-gateway changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-14"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/ai-gateway/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/ai-gateway/#page","headline":"ai-gateway changelog | Cloudflare Docs","description":"2026-09-14","url":"https://developers.cloudflare.com/changelog/product/ai-gateway/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/ai-gateway/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="prevent-unified-billing-fallback-for-byok-third-party-providers"><a href="/changelog/post/2026-09-14-require-provider-credentials/">Prevent Unified Billing fallback for BYOK third-party providers</a></h2>
<p><em>2026-09-14</em></p>
<p>AI Gateway can now require credentials for third-party provider requests. Credentials must accompany the request or be stored on the gateway. This setting prevents fallback to Unified Billing with Cloudflare-managed credentials.</p>
<p>Turn on <strong>Require provider credentials</strong> in your gateway settings. To use the API, set <code>byok_only</code> to <code>true</code> in the request body of a <a href="/api/resources/ai_gateway/methods/update/"><code>PUT</code> request to update the gateway</a>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;byok_only&quot;: true&#10;}&#10;</code></pre>
<p>To require provider credentials for one third-party request, set the <code>cf-aig-no-wholesale</code> header to <code>true</code>. This header cannot relax the gateway setting.</p>
<p>Requests without applicable credentials then return an HTTP <code>400</code> response. Workers AI requests remain allowed, and the setting does not change their configured billing mode.</p>
<p>For configuration details and request-level controls, refer to <a href="/ai-gateway/features/unified-billing/#prevent-unified-billing-fallback-for-byok-third-party-providers">Prevent Unified Billing fallback for BYOK third-party providers</a>.</p>


<h2 id="ai-gateway-custom-costs-support-cache-tokens"><a href="/changelog/post/2026-09-09-custom-cache-token-costs/">AI Gateway custom costs support cache tokens</a></h2>
<p><em>2026-09-09</em></p>
<p>AI Gateway custom costs now support cache-read and cache-write token rates. This lets custom cost metrics reflect negotiated cache pricing across providers.</p>
<p>Add <code>per_cache_read_token</code> or <code>per_cache_write_token</code> to the <code>cf-aig-custom-cost</code> header:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;per_token_in&quot;: 0.000001,&#10;	&quot;per_token_out&quot;: 0.000002,&#10;	&quot;per_cache_read_token&quot;: 0.0000001,&#10;	&quot;per_cache_write_token&quot;: 0.0000005&#10;}&#10;</code></pre>
<p>Cache-token pricing activates when either cache rate is present. An omitted cache rate defaults to <code>per_token_in</code>. If both cache rates are omitted, AI Gateway preserves the existing input and output calculation.</p>
<p>Providers can include cache tokens within input tokens or report them separately. AI Gateway automatically accounts for these differences and prevents double-counting.</p>
<p>For more information, refer to <a href="/ai-gateway/configuration/custom-costs/">Custom costs</a>.</p>


<h2 id="ai-gateway-consolidates-monthly-usage-invoice-line-items-and-standardizes-model-names"><a href="/changelog/post/2026-09-01-billing-and-model-names/">AI Gateway consolidates monthly usage invoice line items and standardizes model names</a></h2>
<p><em>2026-09-01</em></p>
<p>AI Gateway monthly usage invoices, issued at the beginning of each month for the previous month's usage, now show a single total cost for each model. These invoices no longer break out input and output token quantities and unit prices into separate line items. This change does not apply to invoices for AI Gateway credit purchases.</p>
<p>For example, an invoice that previously included these separate line items:</p>
<ul>
<li><code>anthropic claude-haiku-4-5-20251001 Input Tokens</code>: 40,000 tokens at $0.000001 ($0.04)</li>
<li><code>anthropic claude-haiku-4-5-20251001 Output Tokens</code>: 24,000 tokens at $0.000005 ($0.12)</li>
</ul>
<p>The updated invoice includes one line item: <code>anthropic/claude-haiku-4.5</code>: $0.16.</p>
<p>AI Gateway has also standardized model names across invoices and logs. Model variants that previously appeared with provider-specific version suffixes now use a consistent <code>provider/model</code> identifier.</p>
<p>For more information, refer to the <a href="/ai-gateway/features/unified-billing/">Unified Billing documentation</a> and <a href="/ai-gateway/observability/logging/">AI Gateway logging documentation</a>.</p>


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


<h2 id="workers-ai-and-ai-gateway-unify-model-access-and-billing"><a href="/changelog/post/2026-08-07-workers-ai-unified-billing/">Workers AI and AI Gateway unify model access and billing</a></h2>
<p><em>2026-08-07</em></p>
<p>Workers AI and AI Gateway now provide a unified path for accessing models and managing inference traffic. Use the same AI binding and REST API to call models hosted on Workers AI or by supported third-party providers, with AI Gateway providing observability, logging, caching, security, and billing controls.</p>
<h4 id="2026-08-07-workers-ai-unified-billing-unified-entrypoints-and-observability">Unified entrypoints and observability</h4>
<p>The <a href="/ai-gateway/usage/worker-binding-methods/">AI binding</a> supports both Workers AI and third-party models through <code>env.AI.run()</code>. The <a href="/ai-gateway/usage/rest-api/">REST API</a> provides shared <code>/ai/</code> endpoints with Cloudflare authentication across providers.</p>
<p>Route a Workers AI request through AI Gateway by specifying a gateway ID. Use <code>default</code> to automatically create a gateway on the first authenticated request, or specify an existing gateway to separate applications and workloads:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17687.md")</div>
<p>Requests routed through AI Gateway can be logged and included in analytics for request volume, errors, latency, token usage, and costs. You can also configure controls such as caching, rate limiting, and request retries on the gateway.</p>
<h4 id="2026-08-07-workers-ai-unified-billing-unified-billing-and-higher-rate-limits">Unified billing and higher rate limits</h4>
<p>You can now use prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a> to pay for Workers AI inference. This provides one credit balance for Workers AI and supported third-party model providers. To use credits for Workers AI, set the gateway's <a href="/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing">Workers AI billing setting</a> to <strong>Unified billing</strong>. Workers AI requests routed through that gateway deduct from your credit balance in real time.</p>
<p>Prepaid credits also provide access to the following Workers AI frontier models without requiring the Workers Paid plan. Each frontier Workers AI model has a rate limit of 50 requests per minute per account, per model when billed with AI Gateway credits, compared to 20 requests per minute through standard Workers AI billing:</p>
<ul>
<li><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a></li>
<li><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a></li>
<li><a href="/workers-ai/models/glm-5.2/"><code>@cf/zai-org/glm-5.2</code></a></li>
</ul>
<p>These limits are designed for typical agentic and coding workloads, where requests to frontier models can take longer to complete.</p>
<p>For details, refer to <a href="/workers-ai/platform/limits/">Workers AI limits</a>, <a href="/workers-ai/platform/pricing/">Workers AI pricing</a>, <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>, and the <a href="/ai/models/">AI Gateway model catalog</a>.</p>


<h2 id="track-ai-spend-and-catch-anomalous-usage-with-user-insights"><a href="/changelog/post/2026-08-05-user-insights/">Track AI spend and catch anomalous usage with User Insights</a></h2>
<p><em>2026-08-05T12:00:00-08:00</em></p>
<p>AI Gateway now includes User Insights, a dashboard that gives you two things at once: clear visibility into how much your organization spends on AI, and a security signal that surfaces users whose usage suddenly looks abnormal. It works on the traffic already flowing through your gateway, so there is no additional setup.</p>
<p>On the spend side, User Insights shows organization-wide totals for cost, requests, tokens, and adoption, and lets you drill into an individual user to see their spend, top models and providers, cache hit rate, and more. To attribute usage to individual users, add a user identifier with custom metadata or put your gateway behind Cloudflare Access.</p>
<p>On the security side, User Insights baselines each user's normal usage from their 95th percentile (p95) session cost over the last 30 days, then flags sessions that exceed both that baseline and an organization-level threshold. A sudden jump above a user's own pattern is often the first sign of a compromised credential or a misbehaving agent, so you can investigate before it shows up on your bill.</p>
<p>User Insights is available to all AI Gateway customers at no additional cost.</p>


<h2 id="identity-aware-controls-are-now-available-in-ai-gateway"><a href="/changelog/post/2026-08-05-access-user-id-metadata/">Identity-aware controls are now available in AI Gateway</a></h2>
<p><em>2026-08-05</em></p>
<p>AI Gateway now integrates with Cloudflare Access, giving you two new capabilities:</p>
<ul>
<li><strong>Protect your gateway endpoint.</strong> Put your AI Gateway behind Access so you can set policies that control who is allowed to call a specific gateway's endpoint.</li>
<li><strong>Identity-aware controls.</strong> When traffic reaches AI Gateway through an Access-protected custom domain, AI Gateway can use the authenticated user's Access identity in logs, analytics, routing, and spend controls.</li>
</ul>
<p>With identity-aware controls, you can set spend limits by authenticated user, control which gateways different users can access, filter logs by user, and build policies without passing user IDs from the client application. AI Gateway adds the verified Access user ID to request metadata as <code>cf.user_id</code>.</p>
<p>For setup instructions, refer to <a href="/ai-gateway/configuration/cloudflare-access/">Cloudflare Access</a>.</p>


<h2 id="view-the-user-agent-of-requests-in-ai-gateway-logs"><a href="/changelog/post/2026-06-12-user-agent-logging/">View the user agent of requests in AI Gateway logs</a></h2>
<p><em>2026-06-12</em></p>
<p>AI Gateway logs now capture the user agent of the client that made each request, making it easier to identify which SDK, library, or application sent the traffic flowing through your gateway. For example, you can tell apart requests coming from <code>openai-python</code> versus a custom application or a Cloudflare Worker.</p>
<p>The user agent appears alongside the other details in each log entry, and you can filter logs by user agent (equals, does not equal, or contains) in the dashboard.</p>
<p>For more information, refer to <a href="/ai-gateway/observability/logging/">Logging</a>.</p>


<h2 id="control-ai-costs-with-spend-limits"><a href="/changelog/post/2026-06-05-spend-limits/">Control AI costs with spend limits</a></h2>
<p><em>2026-06-05</em></p>
<p>AI Gateway now supports spend limits — cost-based budgets that track cumulative dollar spend and block requests when the budget is exceeded. Unlike rate limiting, which caps the number of requests, spend limits track actual cost based on token usage and model pricing.</p>
<p>You can scope limits by model, provider, or custom metadata dimensions. For example, give each user a $200/day budget, cap total gateway spend at $10,000/day, or limit a specific model to $50/day per user. Each rule uses a configurable time window with fixed or sliding enforcement.</p>
<p>Spend limits work with both <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> and <a href="/ai-gateway/configuration/bring-your-own-keys/">BYOK</a> requests for models with known pricing.</p>
<p>For more details, refer to the <a href="/ai-gateway/features/spend-limits/">Spend limits documentation</a>.</p>


<h2 id="call-any-ai-model-through-ai-gateway-s-new-rest-api"><a href="/changelog/post/2026-05-21-rest-api/">Call any AI model through AI Gateway's new REST API</a></h2>
<p><em>2026-05-21</em></p>
<p>AI Gateway now uses the AI REST API on <code>api.cloudflare.com</code>. You can call any model — whether from OpenAI, Anthropic, Google, or hosted on Workers AI — through one unified API, using the same endpoints and authentication regardless of provider. Four endpoints are available:</p>
<ul>
<li><code>POST /ai/run</code> — universal endpoint for all models and modalities</li>
<li><code>POST /ai/v1/chat/completions</code> — OpenAI SDK compatible</li>
<li><code>POST /ai/v1/responses</code> — OpenAI Responses API compatible</li>
<li><code>POST /ai/v1/messages</code> — Anthropic SDK compatible</li>
</ul>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-5.5&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]&#10;  }&#x27;&#10;</code></pre>
<p>All AI Gateway features — logging, caching, rate limiting, and guardrails — are applied automatically. Third-party models are billed through <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>, so you do not need to manage separate provider API keys.</p>
<p>Third-party model requests are routed through your account's default gateway, which is created automatically on first use. To route requests through a specific gateway, add the <code>cf-aig-gateway-id</code> header.</p>
<p>If you are already calling Workers AI models through the existing REST API, that path (<code>/ai/run/@cf/{model}</code>) continues to work. To call Workers AI models through AI Gateway, use the <code>@cf/</code> model prefix (for example, <code>@cf/moonshotai/kimi-k2.6</code>) and include the <code>cf-aig-gateway-id</code> header to specify which gateway to route through.</p>
<p>For more details and examples, refer to the <a href="/ai-gateway/usage/rest-api/">REST API documentation</a>.</p>


<h2 id="automatically-retry-on-upstream-provider-failures-on-ai-gateway"><a href="/changelog/post/2026-04-02-auto-retry-upstream-failures/">Automatically retry on upstream provider failures on AI Gateway</a></h2>
<p><em>2026-04-02</em></p>
<p>AI Gateway now supports automatic retries at the gateway level. When an upstream provider returns an error, your gateway retries the request based on the retry policy you configure, without requiring any client-side changes.</p>
<p>You can configure the retry count (up to 5 attempts), the delay between retries (from 100ms to 5 seconds), and the backoff strategy (Constant, Linear, or Exponential). These defaults apply to all requests through the gateway, and per-request headers can override them.</p>
<p><img src="/assets/upstream/images/ai-gateway/auto-retry-changelog.png" alt="Retry Requests settings in the AI Gateway dashboard" /></p>
<p>This is particularly useful when you do not control the client making the request and cannot implement retry logic on the caller side. For more complex failover scenarios — such as failing across different providers — use <a href="/ai-gateway/features/dynamic-routing/">Dynamic Routing</a>.</p>
<p>For more information, refer to <a href="/ai-gateway/configuration/manage-gateway/#retry-requests">Manage gateways</a>.</p>


<h2 id="log-ai-gateway-request-metadata-without-storing-payloads"><a href="/changelog/post/2026-03-17-collect-log-payload-header/">Log AI Gateway request metadata without storing payloads</a></h2>
<p><em>2026-03-17</em></p>
<p>AI Gateway now supports the <code>cf-aig-collect-log-payload</code> header, which controls whether request and response bodies are stored in logs. By default, this header is set to <code>true</code> and payloads are stored alongside metadata. Set this header to <code>false</code> to skip payload storage while still logging metadata such as token counts, model, provider, status code, cost, and duration.</p>
<p>This is useful when you need usage metrics but do not want to persist sensitive prompt or response data.</p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/$ACCOUNT_ID/$GATEWAY_ID/openai/chat/completions \&#10;  &#45;-header &quot;Authorization: Bearer $TOKEN&quot; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;cf-aig-collect-log-payload: false&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;gpt-4o-mini&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is the email address and phone number of user123?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>For more information, refer to <a href="/ai-gateway/observability/logging/#collect-log-payload-cf-aig-collect-log-payload">Logging</a>.</p>


<h2 id="get-started-with-ai-gateway-automatically"><a href="/changelog/post/2026-03-02-default-gateway/">Get started with AI Gateway automatically</a></h2>
<p><em>2026-03-02</em></p>
<p>You can now start using AI Gateway with a single API call — no setup required. Use <code>default</code> as your gateway ID, and AI Gateway creates one for you automatically on the first request.</p>
<p>To try it out, <a href="/fundamentals/api/get-started/create-token/">create an API token</a> with <code>AI Gateway - Read</code>, <code>AI Gateway - Edit</code>, and <code>Workers AI - Read</code> permissions, then run:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/$CLOUDFLARE_ACCOUNT_ID/default/compat/chat/completions \&#10;  &#45;-header &quot;cf-aig-authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>AI Gateway gives you logging, caching, rate limiting, and access to multiple AI providers through a single endpoint. For more information, refer to <a href="/ai-gateway/get-started/">Get started</a>.</p>


<h2 id="ai-dashboard-experience-improvements"><a href="/changelog/post/2026-02-19-ai-dashboard-experience-improvements/">AI dashboard experience improvements</a></h2>
<p><em>2026-02-19</em></p>
<p><a href="/workers-ai/">Workers AI</a> and <a href="/ai-gateway/">AI Gateway</a> have received a series of dashboard improvements to help you get started faster and manage your AI workloads more easily.</p>
<p><strong>Navigation and discoverability</strong></p>
<p>AI now has its own top-level section in the Cloudflare dashboard sidebar, so you can find AI features without digging through menus.</p>
<p><img src="/assets/upstream/images/ai-gateway/sidebar-navigation.png" alt="AI sidebar navigation in the Cloudflare dashboard" />
<em>The new top-level AI section in the dashboard sidebar.</em></p>
<p><strong>Onboarding and getting started</strong></p>
<p><a href="/ai-gateway/get-started/">Getting started</a> with AI Gateway is now simpler. When you create your first gateway, we now show your gateway's OpenAI-compatible endpoint and step-by-step guidance to help you configure it. The Playground also includes helpful prompts, and usage pages have clear next steps if you have not made any requests yet.</p>
<p><img src="/assets/upstream/images/ai-gateway/onboarding-flow.png" alt="AI Gateway onboarding flow" />
<em>The first-run setup experience for new gateways.</em></p>
<p>We've also combined the previously separate code example sections into one view with dropdown selectors for API type, provider, SDK, and authentication method so you can now customize the exact code snippet you need from one place.</p>
<p><strong>Dynamic Routing</strong></p>
<ul>
<li>The <a href="/ai-gateway/features/dynamic-routing/">route builder</a> is now more performant and responsive.</li>
<li>You can now copy route names to your clipboard with a single click.</li>
<li>Code examples use the <a href="/ai-gateway/usage/universal/">Universal Endpoint</a> format, making it easier to integrate routes into your application.</li>
</ul>
<p><strong>Observability and analytics</strong></p>
<ul>
<li>Small monetary values now display correctly in <a href="/ai-gateway/observability/costs/">cost analytics</a> charts, so you can accurately track spending at any scale.</li>
</ul>
<p><strong>Accessibility</strong></p>
<ul>
<li>Improvements to keyboard navigation within the AI Gateway, specifically when exploring usage by <a href="/ai-gateway/usage/providers/">provider</a>.</li>
<li>Improvements to sorting and filtering components on the <a href="/workers-ai/models/">Workers AI</a> models page.</li>
</ul>
<p>For more information, refer to the <a href="/ai-gateway/">AI Gateway documentation</a>.</p>


<h2 id="manage-and-deploy-your-ai-provider-keys-through-bring-your-own-key-byok-with-ai-gateway-now-powered-by-cloudflare-secrets-store"><a href="/changelog/post/2025-08-25-secrets-store-ai-gateway/">Manage and deploy your AI provider keys through Bring Your Own Key (BYOK) with AI Gateway, now powered by Cloudflare Secrets Store</a></h2>
<p><em>2025-08-25T11:00:00+00:00</em></p>
<p>Cloudflare Secrets Store is now integrated with AI Gateway, allowing you to store, manage, and deploy your AI provider keys in a secure and seamless configuration through <a href="https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Key</a>. Instead of passing your AI provider keys directly in every request header, you can centrally manage each key with Secrets Store and deploy in your gateway configuration using only a reference, rather than passing the value in plain text.</p>
<p>You can now create a secret directly from your AI Gateway <a href="http://dash.cloudflare.com/?to=/:account/ai-gateway">in the dashboard</a> by navigating into your gateway -&gt; <strong>Provider Keys</strong> -&gt; <strong>Add</strong>.</p>
<p><img src="/assets/upstream/images/ssl/add-secret-ai-gateway.png" alt="Import repo or choose template" /></p>
<p>You can also create your secret with the newly available <strong>ai_gateway</strong> scope via <a href="https://developers.cloudflare.com/workers/wrangler/commands/">wrangler</a>, the <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">Secrets Store dashboard</a>, or the <a href="https://developers.cloudflare.com/api/resources/secrets_store/">API</a>.</p>
<p>Then, pass the key in the request header using its Secrets Store reference:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic/v1/messages \&#10; &#45;-header &#x27;cf-aig-authorization: ANTHROPIC_KEY_1 \&#10; &#45;-header &#x27;anthropic-version: 2023-06-01&#x27; \&#10; &#45;-header &#x27;Content-Type: application/json&#x27; \&#10; &#45;-data  &#x27;{&quot;model&quot;: &quot;claude-3-opus-20240229&quot;, &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]}&#x27;&#10;</code></pre>
<p>Or, using Javascript:</p>
<pre tabindex="0"><code>import Anthropic from &#x27;@anthropic-ai/sdk&#x27;;&#10;&#10;&#10;const anthropic = new Anthropic({&#10; apiKey: &quot;ANTHROPIC_KEY_1&quot;,&#10; baseURL: &quot;https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic&quot;,&#10;});&#10;&#10;&#10;const message = await anthropic.messages.create({&#10; model: &#x27;claude-3-opus-20240229&#x27;,&#10; messages: [{role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot;}],&#10; max_tokens: 1024&#10;});&#10;</code></pre>
<p>For more information, check out the <a href="https://blog.cloudflare.com/ai-gateway-aug-2025-refresh">blog</a>!</p>


<h2 id="ai-gateway-adds-openai-compatible-endpoint"><a href="/changelog/post/2025-06-03-aig-openai-compatible-endpoint/">AI Gateway adds OpenAI compatible endpoint</a></h2>
<p><em>2025-06-03</em></p>
<p>Users can now use an <a href="/ai-gateway/usage/chat-completion/">OpenAI Compatible endpoint</a> in AI Gateway to easily switch between providers, while keeping the exact same request and response formats. We're launching now with the chat completions endpoint, with the embeddings endpoint coming up next.</p>
<p>To get started, use the OpenAI compatible chat completions endpoint URL with your own account id and gateway id and switch between providers by changing the <code>model</code> and <code>apiKey</code> parameters.</p>
<pre tabindex="0"><code class="language-js">import OpenAI from &quot;openai&quot;;&#10;const client = new OpenAI({&#10;	apiKey: &quot;YOUR_PROVIDER_API_KEY&quot;, // Provider API key&#10;	baseURL:&#10;		&quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat&quot;,&#10;});&#10;&#10;const response = await client.chat.completions.create({&#10;	model: &quot;google-ai-studio/gemini-2.0-flash&quot;,&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;});&#10;&#10;console.log(response.choices[0].message.content);&#10;</code></pre>
<p>Additionally, the <a href="/ai-gateway/usage/chat-completion/">OpenAI Compatible endpoint</a> can be combined with our <a href="/ai-gateway/usage/universal/">Universal Endpoint</a> to add fallbacks across multiple providers. That means AI Gateway will return every response in the same standardized format, no extra parsing logic required!</p>
<p>Learn more in the <a href="/ai-gateway/usage/chat-completion/">OpenAI Compatibility</a> documentation.</p>


<h2 id="ai-gateway-launches-realtime-websockets-api"><a href="/changelog/post/2025-03-20-websockets/">AI Gateway launches Realtime WebSockets API</a></h2>
<p><em>2025-03-21</em></p>
<p>We are excited to announce that <a href="/ai-gateway/">AI Gateway</a> now supports real-time AI interactions with the new <a href="/ai-gateway/usage/websockets-api/realtime-api/">Realtime WebSockets API</a>.</p>
<p>This new capability allows developers to establish persistent, low-latency connections between their applications and AI models, enabling natural, real-time conversational AI experiences, including speech-to-speech interactions.</p>
<p>The Realtime WebSockets API works with the <a href="https://platform.openai.com/docs/guides/realtime#connect-with-websockets">OpenAI Realtime API</a>, <a href="https://ai.google.dev/gemini-api/docs/multimodal-live">Google Gemini Live API</a>, and supports real-time text and speech interactions with models from <a href="https://docs.cartesia.ai/api-reference/tts/tts">Cartesia</a>, and <a href="https://elevenlabs.io/docs/conversational-ai/api-reference/conversational-ai/websocket">ElevenLabs</a>.</p>
<p>Here's how you can connect AI Gateway to <a href="https://platform.openai.com/docs/guides/realtime#connect-with-websockets">OpenAI's Realtime API</a> using WebSockets:</p>
<pre tabindex="0"><code class="language-javascript">import WebSocket from &quot;ws&quot;;&#10;&#10;const url =&#10;	&quot;wss://gateway.ai.cloudflare.com/v1/&lt;account_id&gt;/&lt;gateway&gt;/openai?model=gpt-4o-realtime-preview-2024-12-17&quot;;&#10;const ws = new WebSocket(url, {&#10;	headers: {&#10;		&quot;cf-aig-authorization&quot;: process.env.CLOUDFLARE_API_KEY,&#10;		Authorization: &quot;Bearer &quot; + process.env.OPENAI_API_KEY,&#10;		&quot;OpenAI-Beta&quot;: &quot;realtime=v1&quot;,&#10;	},&#10;});&#10;&#10;ws.on(&quot;open&quot;, () =&gt; console.log(&quot;Connected to server.&quot;));&#10;ws.on(&quot;message&quot;, (message) =&gt; console.log(JSON.parse(message.toString())));&#10;&#10;ws.send(&#10;	JSON.stringify({&#10;		type: &quot;response.create&quot;,&#10;		response: { modalities: [&quot;text&quot;], instructions: &quot;Tell me a joke&quot; },&#10;	}),&#10;);&#10;</code></pre>
<p>Get started by checking out the <a href="/ai-gateway/usage/websockets-api/realtime-api/">Realtime WebSockets API</a> documentation.</p>


<h2 id="introducing-guardrails-in-ai-gateway"><a href="/changelog/post/2025-02-26-guardrails/">Introducing Guardrails in AI Gateway</a></h2>
<p><em>2025-02-26</em></p>
<p><a href="/ai-gateway/">AI Gateway</a> now includes <a href="/ai-gateway/features/guardrails/">Guardrails</a>, to help you monitor your AI apps for harmful or inappropriate content and deploy safely.</p>
<p>Within the AI Gateway settings, you can configure:</p>
<ul>
<li><strong>Guardrails</strong>: Enable or disable content moderation as needed.</li>
<li><strong>Evaluation scope</strong>: Select whether to moderate user prompts, model responses, or both.</li>
<li><strong>Hazard categories</strong>: Specify which categories to monitor and determine whether detected inappropriate content should be blocked or flagged.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/Guardrails.png" alt="Guardrails in AI Gateway" /></p>
<p>Learn more in the <a href="https://blog.cloudflare.com/guardrails-in-ai-gateway/">blog</a> or our <a href="/ai-gateway/features/guardrails/">documentation</a>.</p>


<h2 id="request-timeouts-and-retries-with-ai-gateway"><a href="/changelog/post/2025-02-05-aig-request-handling/">Request timeouts and retries with AI Gateway</a></h2>
<p><em>2025-02-06</em></p>
<p>AI Gateway adds additional ways to handle requests - <a href="/ai-gateway/configuration/request-handling/#request-timeouts">Request Timeouts</a> and <a href="/ai-gateway/configuration/request-handling/#request-retries">Request Retries</a>, making it easier to keep your applications responsive and reliable.</p>
<p>Timeouts and retries can be used on both the <a href="/ai-gateway/usage/universal/">Universal Endpoint</a> or directly to a <a href="/ai-gateway/usage/providers/">supported provider</a>.</p>
<p><strong>Request timeouts</strong>
A <a href="/ai-gateway/configuration/request-handling/#request-timeouts">request timeout</a> allows you to trigger <a href="/ai-gateway/configuration/fallbacks/">fallbacks</a> or a retry if a provider takes too long to respond.</p>
<p>To set a request timeout directly to a provider, add a <code>cf-aig-request-timeout</code> header.</p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/workers-ai/@cf/meta/llama-3.1-8b-instruct \&#10; &#45;-header &#x27;Authorization: Bearer {cf_api_token}&#x27; \&#10; &#45;-header &#x27;Content-Type: application/json&#x27; \&#10; &#45;-header &#x27;cf-aig-request-timeout: 5000&#x27;&#10; &#45;-data &#x27;{&quot;prompt&quot;: &quot;What is Cloudflare?&quot;}&#x27;&#10;</code></pre>
<p><strong>Request retries</strong>
A <a href="/ai-gateway/configuration/request-handling/#request-retries">request retry</a> automatically retries failed requests, so you can recover from temporary issues without intervening.</p>
<p>To set up request retries directly to a provider, add the following headers:</p>
<ul>
<li>cf-aig-max-attempts (number)</li>
<li>cf-aig-retry-delay (number)</li>
<li>cf-aig-backoff (&quot;constant&quot; | &quot;linear&quot; | &quot;exponential)</li>
</ul>


<h2 id="ai-gateway-adds-cerebras-elevenlabs-and-cartesia-as-new-providers"><a href="/changelog/post/2025-02-04-aig-provider-cartesia-eleven-cerebras/">AI Gateway adds Cerebras, ElevenLabs, and Cartesia as new providers</a></h2>
<p><em>2025-02-05</em></p>
<p><a href="/ai-gateway/">AI Gateway</a> has added three new providers: <a href="/ai-gateway/usage/providers/cartesia/">Cartesia</a>, <a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a>, and <a href="/ai-gateway/usage/providers/elevenlabs/">ElevenLabs</a>, giving you more even more options for providers you can use through AI Gateway. Here's a brief overview of each:</p>
<ul>
<li><a href="/ai-gateway/usage/providers/cartesia/">Cartesia</a> provides text-to-speech models that produce natural-sounding speech with low latency.</li>
<li><a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a> delivers low-latency AI inference to Meta's Llama 3.1 8B and Llama 3.3 70B models.</li>
<li><a href="/ai-gateway/usage/providers/elevenlabs/">ElevenLabs</a> offers text-to-speech models with human-like voices in 32 languages.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/cerebras2.png" alt="Example of Cerebras log in AI Gateway" /></p>
<p>To get started with AI Gateway, just update the base URL. Here's how you can send a request to <a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a> using cURL:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/ACCOUNT_TAG/GATEWAY/cerebras/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer CEREBRAS_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;llama-3.3-70b&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>


<h2 id="ai-gateway-introduces-new-worker-binding-methods"><a href="/changelog/post/2025-01-26-worker-binding-methods/">AI Gateway Introduces New Worker Binding Methods</a></h2>
<p><em>2025-01-30</em></p>
<p>We have released new <a href="/ai-gateway/usage/worker-binding-methods/">Workers bindings API methods</a>, allowing you to connect Workers applications to AI Gateway directly. These methods simplify how Workers calls AI services behind your AI Gateway configurations, removing the need to use the REST API and manually authenticate.</p>
<p>To add an AI binding to your Worker, include the following in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<p><img src="/assets/upstream/images/ai-gateway/add-binding.png" alt="Add an AI binding to your Worker." /></p>
<p>With the new AI Gateway binding methods, you can now:</p>
<ul>
<li>Send feedback and update metadata with <code>patchLog</code>.</li>
<li>Retrieve detailed log information using <code>getLog</code>.</li>
<li>Execute <a href="/ai-gateway/usage/universal/">universal requests</a> to any AI Gateway provider with <code>run</code>.</li>
</ul>
<p>For example, to send feedback and update metadata using <code>patchLog</code>:</p>
<p><img src="/assets/upstream/images/ai-gateway/send-feedback.png" alt="Send feedback and update metadata using patchLog:" /></p>


<h2 id="ai-gateway-adds-deepseek-as-a-provider"><a href="/changelog/post/2025-01-07-aig-provider-deepseek/">AI Gateway adds DeepSeek as a Provider</a></h2>
<p><em>2025-01-02</em></p>
<p><a href="/ai-gateway/"><strong>AI Gateway</strong></a> now supports <a href="/ai-gateway/usage/providers/deepseek/"><strong>DeepSeek</strong></a>, including their cutting-edge DeepSeek-V3 model. With this addition, you have even more flexibility to manage and optimize your AI workloads using AI Gateway. Whether you're leveraging DeepSeek or other providers, like OpenAI, Anthropic, or <a href="/workers-ai/">Workers AI</a>, AI Gateway empowers you to:</p>
<ul>
<li><strong>Monitor</strong>: Gain actionable insights with analytics and logs.</li>
<li><strong>Control</strong>: Implement caching, rate limiting, and fallbacks.</li>
<li><strong>Optimize</strong>: Improve performance with feedback and evaluations.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/deepseek.png" alt="AI Gateway adds DeepSeek as a provider" /></p>
<p>To get started, simply update the base URL of your DeepSeek API calls to route through AI Gateway. Here's how you can send a request using cURL:</p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer DEEPSEEK_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;deepseek-chat&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<p>For detailed setup instructions, see our <a href="/ai-gateway/usage/providers/deepseek/">DeepSeek provider documentation</a>.</p>



