---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/web-search/
  description: Use provider-native web search tools through AI Gateway, or reach search-first providers like Perplexity and Parallel through their proxy endpoints.
  full_title: Web Search · Cloudflare AI Gateway docs
  head_html: <title>Web Search · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Use provider-native web search tools through AI Gateway, or reach search-first providers like Perplexity and Parallel through their proxy endpoints."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/web-search/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/web-search/index.md"><meta property="og:title" content="Web Search · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use provider-native web search tools through AI Gateway, or reach search-first providers like Perplexity and Parallel through their proxy endpoints."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/web-search/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Gateway"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/web-search/#page","headline":"Web Search \u00b7 Cloudflare AI Gateway docs","description":"Use provider-native web search tools through AI Gateway, or reach search-first providers like Perplexity and Parallel through their proxy endpoints.","url":"https://developers.cloudflare.com/ai-gateway/usage/web-search/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/web-search/
  schema: 1
---
<p>AI Gateway proxies native web search tools from supported providers so models can answer questions about events after their training cutoff. Search runs on the upstream provider; AI Gateway applies its standard features — logging, caching, rate limiting, and guardrails — to the request.</p>
<p>How you enable web search depends on the provider. Activation is either a tool entry on a <code>tools</code> array or a top-level flag on the request body. The table below points you to the right section.</p>
<h2 id="supported-providers">Supported providers</h2>
<table>
<thead>
<tr>
<th>Provider</th>
<th>Endpoint</th>
<th>Activation</th>
</tr>
</thead>
<tbody>
<tr>
<td>Anthropic</td>
<td><code>POST /ai/v1/messages</code></td>
<td><code>tools: [{ &quot;type&quot;: &quot;web_search_20250305&quot;, &quot;name&quot;: &quot;web_search&quot;, &quot;max_uses&quot;: N }]</code></td>
</tr>
<tr>
<td>OpenAI</td>
<td><code>POST /ai/v1/responses</code></td>
<td><code>tools: [{ &quot;type&quot;: &quot;web_search_preview&quot; }]</code></td>
</tr>
<tr>
<td>xAI</td>
<td><code>POST /ai/v1/responses</code></td>
<td><code>tools: [{ &quot;type&quot;: &quot;web_search&quot; }]</code></td>
</tr>
<tr>
<td>Alibaba</td>
<td><code>POST /ai/v1/chat/completions</code></td>
<td>top-level <code>&quot;enable_search&quot;: true</code></td>
</tr>
</tbody>
</table>
<p>For providers whose product is search itself — Perplexity and Parallel — refer to <a href="#search-first-providers">Search-first providers</a>.</p>
<h2 id="anthropic-web-search">Anthropic web search</h2>
<p>Anthropic models expose web search through their native <a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool"><code>web_search_20250305</code> tool</a>. Add it to the <code>tools</code> array on a <code>POST /ai/v1/messages</code> request.</p>
<p>Supported models — <code>anthropic/claude-haiku-4.5</code>, <code>anthropic/claude-opus-4.5</code>, <code>anthropic/claude-opus-4.6</code>, <code>anthropic/claude-opus-4.7</code>, <code>anthropic/claude-opus-4.8</code>, <code>anthropic/claude-sonnet-4.5</code>, <code>anthropic/claude-sonnet-4.6</code>.</p>
<pre tabindex="0"><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;anthropic/claude-haiku-4.5&quot;,&#10;    &quot;max_tokens&quot;: 4096,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What were the top news stories about Cloudflare this week? Summarize in three bullets.&quot;&#10;      }&#10;    ],&#10;    &quot;tools&quot;: [&#10;      {&#10;        &quot;type&quot;: &quot;web_search_20250305&quot;,&#10;        &quot;name&quot;: &quot;web_search&quot;,&#10;        &quot;max_uses&quot;: 3&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>Equivalent call from a Worker using the AI binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2780.md")
</div>
<p>Search invocations and results appear in the response as <code>server_tool_use</code> and <code>web_search_tool_result</code> content blocks. Configurable parameters include <code>max_uses</code>, <code>allowed_domains</code>, <code>blocked_domains</code>, and <code>user_location</code> — refer to Anthropic's <a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool">web search tool documentation</a> for the full list.</p>
<h2 id="openai-web-search">OpenAI web search</h2>
<p>OpenAI models expose web search through the <a href="https://developers.openai.com/api/docs/guides/tools-web-search"><code>web_search_preview</code> tool</a> on the Responses API. Use the <code>POST /ai/v1/responses</code> endpoint and add the tool to the <code>tools</code> array.</p>
<p>Supported models — <code>openai/gpt-4.1</code>, <code>openai/gpt-4.1-mini</code>, <code>openai/gpt-4o</code>, <code>openai/gpt-4o-mini</code>, <code>openai/gpt-5</code>, <code>openai/gpt-5-mini</code>, <code>openai/gpt-5-nano</code>, <code>openai/gpt-5.1</code>, <code>openai/gpt-5.4</code>, <code>openai/gpt-5.4-mini</code>, <code>openai/gpt-5.4-nano</code>, <code>openai/gpt-5.4-pro</code>, <code>openai/gpt-5.5</code>, <code>openai/gpt-5.5-pro</code>, <code>openai/o3</code>, <code>openai/o4-mini</code>.</p>
<pre tabindex="0"><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-4o-mini&quot;,&#10;    &quot;input&quot;: &quot;What were the top news stories about Cloudflare this week? Summarize in three bullets.&quot;,&#10;    &quot;max_output_tokens&quot;: 4096,&#10;    &quot;tools&quot;: [&#10;      { &quot;type&quot;: &quot;web_search_preview&quot; }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>Equivalent call from a Worker using the AI binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2781.md")
</div>
<p>OpenAI web search is available only on the Responses API endpoint (<code>POST /ai/v1/responses</code>). The <code>/ai/v1/chat/completions</code> endpoint does not accept the <code>web_search_preview</code> tool.</p>
<p>Both <code>{ &quot;type&quot;: &quot;web_search_preview&quot; }</code> and <code>{ &quot;type&quot;: &quot;web_search&quot; }</code> are accepted on the Responses API. The examples here use <code>web_search_preview</code>.</p>
<h2 id="xai-web-search">xAI web search</h2>
<p>xAI's multi-agent Grok model exposes web search through the <a href="https://docs.x.ai/developers/tools/web-search"><code>web_search</code> tool</a> on the Responses API. Add <code>{ &quot;type&quot;: &quot;web_search&quot; }</code> to the <code>tools</code> array on a <code>POST /ai/v1/responses</code> request.</p>
<p>Supported models — <code>xai/grok-4.20-multi-agent-0309</code>.</p>
<pre tabindex="0"><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;xai/grok-4.20-multi-agent-0309&quot;,&#10;    &quot;input&quot;: &quot;What were the top news stories about Cloudflare this week? Summarize in three bullets.&quot;,&#10;    &quot;max_turns&quot;: 4,&#10;    &quot;tools&quot;: [&#10;      { &quot;type&quot;: &quot;web_search&quot; }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>Equivalent call from a Worker using the AI binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2782.md")
</div>
<p><code>xai/grok-4.20-multi-agent-0309</code> is the only xAI model that accepts web search through AI Gateway. For other Grok models, refer to <a href="#models-without-web-search-support">Models without web search support</a>.</p>
<h2 id="alibaba-qwen-web-search">Alibaba (Qwen) web search</h2>
<p>Alibaba DashScope Qwen models enable web search through a top-level <a href="https://www.alibabacloud.com/help/en/model-studio/qwen-search"><code>enable_search</code></a> flag on a chat completions request. Unlike Anthropic, OpenAI, and xAI, there is no <code>tools</code> entry — web search is activated by the flag alone.</p>
<p>Supported models — <code>alibaba/qwen3-max</code>, <code>alibaba/qwen3.5-397b-a17b</code>.</p>
<pre tabindex="0"><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;alibaba/qwen3-max&quot;,&#10;    &quot;enable_search&quot;: true,&#10;    &quot;max_tokens&quot;: 4096,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What were the top news stories about Cloudflare this week? Summarize in three bullets.&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>Equivalent call from a Worker using the AI binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2783.md")
</div>
<p>DashScope does not return search-grounded context as separate tool-call response blocks. It folds the fetched context into the prompt as additional input tokens — expect <code>prompt_tokens</code> to increase substantially on a successful search-grounded response.</p>
<h2 id="search-first-providers">Search-first providers</h2>
<p>For some providers, the primary API is a search endpoint rather than a chat endpoint with a web search tool. AI Gateway exposes them through their existing provider proxy endpoints at <code>gateway.ai.cloudflare.com</code>.</p>
<p>AI Gateway does not provide a provider-agnostic web search abstraction. Call the provider proxy directly using the patterns below.</p>
<h3 id="perplexity">Perplexity</h3>
<p>Call any <a href="https://docs.perplexity.ai/docs/sonar/models">Perplexity Sonar model</a> through the <a href="/ai-gateway/usage/providers/perplexity/">Perplexity provider proxy</a>.</p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/perplexity-ai/chat/completions \&#10;  &#45;-header &quot;Authorization: Bearer $PERPLEXITY_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;sonar&quot;,&#10;    &quot;messages&quot;: [&#10;      { &quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What were the top news stories about Cloudflare this week?&quot; }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h3 id="parallel">Parallel</h3>
<p>Call Parallel's Search API through the <a href="/ai-gateway/usage/providers/parallel/">Parallel provider proxy</a>. Refer to Parallel's <a href="https://docs.parallel.ai/search/search-quickstart">Search API documentation</a> for the full request schema.</p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/parallel/v1beta/search \&#10;  &#45;-header &quot;x-api-key: $PARALLEL_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;objective&quot;: &quot;Top news stories about Cloudflare this week.&quot;,&#10;    &quot;processor&quot;: &quot;base&quot;,&#10;    &quot;max_results&quot;: 10&#10;  }&#x27;&#10;</code></pre>
<h2 id="models-without-web-search-support">Models without web search support</h2>
<p>The following models do not accept web search through AI Gateway:</p>
<ul>
<li><strong>Google Gemini</strong> — not available through the unified <code>web_search</code> tool, because Vertex's OpenAI-compatible surface does not translate it into Gemini's native <code>googleSearch</code> tool. To use Gemini grounding, pass the native <code>google_search</code> tool to the <a href="/ai-gateway/usage/providers/vertex/#using-provider-specific-endpoint">provider-specific Vertex endpoint</a>.</li>
<li><strong>Grok chat-completions models</strong> — <code>xai/grok-4.20-0309-non-reasoning</code>, <code>xai/grok-4.20-0309-reasoning</code>, and <code>xai/grok-4.3</code> use the chat-completions endpoint, which does not accept the <code>web_search</code> tool. For Grok web search, refer to <a href="#xai-web-search">xAI web search</a>.</li>
<li><strong>DeepSeek <code>deepseek-v4-flash</code>, <code>deepseek-v4-pro</code></strong> — these models accept function tools only.</li>
<li><strong>MiniMax <code>m2.7</code>, <code>m3</code></strong> — these models accept <code>{ &quot;type&quot;: &quot;function&quot; }</code> tools only.</li>
<li><strong>OpenAI <code>gpt-4.1-nano</code>, <code>o1-pro</code>, <code>o3-mini</code></strong> — the upstream returns <code>invalid_request_error</code> for <code>web_search_preview</code> on these models.</li>
<li><strong>OpenAI <code>gpt-4o-search-preview</code>, <code>gpt-4o-mini-search-preview</code></strong> — these preview models are deprecated upstream.</li>
</ul>
<h2 id="pricing-and-logging">Pricing and logging</h2>
<p>Web search requests are billed at the upstream provider's web-search rates and flow through <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> along with the rest of the model call. AI Gateway does not charge a separate web-search fee.</p>
<p>Web search tool calls and their results are visible in AI Gateway <a href="/ai-gateway/observability/logging/">logs</a> alongside the rest of the request and response.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/ai-gateway/usage/rest-api/">REST API</a> — the four endpoints these examples target</li>
<li><a href="/ai-gateway/usage/worker-binding-methods/">Workers Bindings</a> — <code>env.AI.run</code> reference</li>
<li><a href="/ai-gateway/usage/providers/anthropic/">Anthropic provider</a></li>
<li><a href="/ai-gateway/usage/providers/openai/">OpenAI provider</a></li>
<li><a href="/ai-gateway/usage/providers/grok/">Grok (xAI) provider</a></li>
<li><a href="/ai-gateway/usage/providers/perplexity/">Perplexity provider</a></li>
<li><a href="/ai-gateway/usage/providers/parallel/">Parallel provider</a></li>
<li><a href="/ai-gateway/features/unified-billing/">Unified Billing</a></li>
</ul>
