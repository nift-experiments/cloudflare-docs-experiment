---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/get-started/
  description: Set up AI Gateway and send your first request to observe and control AI API traffic.
  full_title: Getting started · Cloudflare AI Gateway docs
  head_html: <title>Getting started · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up AI Gateway and send your first request to observe and control AI API traffic."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/get-started/index.md"><meta property="og:title" content="Getting started · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up AI Gateway and send your first request to observe and control AI API traffic."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/get-started/#page","headline":"Getting started \u00b7 Cloudflare AI Gateway docs","description":"Set up AI Gateway and send your first request to observe and control AI API traffic.","url":"https://developers.cloudflare.com/ai-gateway/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/get-started/
  schema: 1
---
<p>In this guide, you will learn how to set up and use your first AI Gateway.</p>
<h2 id="get-your-account-id-and-authentication-token">Get your account ID and authentication token</h2>
<p>Before making requests, you need two things:</p>
<ol>
<li>Your <strong>Account ID</strong> — find it in the <a href="/fundamentals/account/find-account-and-zone-ids/">Cloudflare dashboard</a>.</li>
<li>A <strong>Cloudflare API token</strong> — <a href="/fundamentals/api/get-started/create-token/">create an API token</a> with <code>AI Gateway - Read</code>, <code>AI Gateway - Edit</code>, and <code>Workers AI - Read</code> permissions.</li>
</ol>
<h2 id="send-your-first-request">Send your first request</h2>
<p>Run the following command to make your first request through AI Gateway. This example calls a Workers AI model, which requires the <code>@cf/</code> model prefix and the <code>cf-aig-gateway-id</code> header.</p>
<pre tabindex="0"><code class="language-bash">&#35; Run `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN,&#10;&#35; and `wrangler whoami` to replace $CLOUDFLARE_ACCOUNT_ID.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;cf-aig-gateway-id: default&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;@cf/moonshotai/kimi-k2.6&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>The <code>cf-aig-gateway-id: default</code> header routes this Workers AI request through your account's default gateway. If the gateway does not exist, AI Gateway creates it on the first authenticated request. Routing through the gateway provides unified logging, analytics, caching, rate limiting, and security controls. The auto-created gateway uses <strong>Standard billing</strong> by default. To pay with prepaid AI Gateway credits, <a href="/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing">set its Workers AI billing setting to <strong>Unified billing</strong></a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1589.md")
</aside>
<details class="nb-details"><summary>Create a gateway manually</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1593.md")
</div></details>
<h2 id="provider-authentication">Provider authentication</h2>
<p>Authenticate with your upstream AI provider using one of the following options:</p>
<ul>
<li><strong>Unified Billing:</strong> Use prepaid AI Gateway credits for Workers AI and supported third-party model providers. Refer to <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>.</li>
<li><strong>BYOK (Store Keys):</strong> Store your own provider API Keys with Cloudflare, and AI Gateway will include them at runtime. Refer to <a href="/ai-gateway/configuration/bring-your-own-keys/">BYOK</a>.</li>
<li><strong>Request headers:</strong> Include your provider API Key in the request headers as you normally would (for example, <code>Authorization: Bearer &lt;OPENAI_API_KEY&gt;</code>).</li>
</ul>
<h2 id="integration-options">Integration options</h2>
<h3 id="rest-api">REST API</h3>
<p>Call any model — whether hosted on Cloudflare or by a third-party provider — through the same Cloudflare API. No provider SDKs or API keys needed — authentication and billing are handled through your Cloudflare account. Three endpoints are available: <code>/ai/run</code> for all modalities, <code>/ai/v1/chat/completions</code> for OpenAI SDK compatibility, and <code>/ai/v1/responses</code> for agentic workflows.</p>
<pre tabindex="0"><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-4.1-mini&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]&#10;  }&#x27;&#10;</code></pre>
<p>Refer to <a href="/ai-gateway/usage/rest-api/">REST API</a> for details and examples.</p>
<h3 id="provider-specific-endpoints">Provider-specific endpoints</h3>
<p>For direct integration with specific AI providers, use dedicated endpoints that maintain the original provider's API schema while adding AI Gateway features.</p>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/{provider}&#10;</code></pre>
<p><strong>Available providers:</strong></p>
<ul>
<li><a href="/ai-gateway/usage/providers/openai/">OpenAI</a> - GPT models and embeddings</li>
<li><a href="/ai-gateway/usage/providers/anthropic/">Anthropic</a> - Claude models</li>
<li><a href="/ai-gateway/usage/providers/google-ai-studio/">Google AI Studio</a> - Gemini models</li>
<li><a href="/ai-gateway/usage/providers/workersai/">Workers AI</a> - Cloudflare's inference platform</li>
<li><a href="/ai-gateway/usage/providers/bedrock/">AWS Bedrock</a> - Amazon's managed AI service</li>
<li><a href="/ai-gateway/usage/providers/azureopenai/">Azure OpenAI</a> - Microsoft's OpenAI service</li>
<li><a href="/ai-gateway/usage/providers/">and more...</a></li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/ai-gateway/features/caching/">caching</a> for faster requests and cost savings and <a href="/ai-gateway/features/rate-limiting/">rate limiting</a> to control how your application scales.</li>
<li>Explore how to specify model or provider <a href="/ai-gateway/features/dynamic-routing/">fallbacks, ratelimits, A/B tests</a> for resiliency.</li>
<li>Learn how to use low-cost, open source models on <a href="/ai-gateway/usage/providers/workersai/">Workers AI</a> - our AI inference service.</li>
</ul>
