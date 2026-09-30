---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-http-content/
  description: Gate HTTP endpoints with x402 payments using a Cloudflare Worker proxy.
  full_title: Charge for HTTP content · Cloudflare Agents docs
  head_html: <title>Charge for HTTP content · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Gate HTTP endpoints with x402 payments using a Cloudflare Worker proxy."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-http-content/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-http-content/index.md"><meta property="og:title" content="Charge for HTTP content · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Gate HTTP endpoints with x402 payments using a Cloudflare Worker proxy."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-http-content/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-http-content/#page","headline":"Charge for HTTP content \u00b7 Cloudflare Agents docs","description":"Gate HTTP endpoints with x402 payments using a Cloudflare Worker proxy.","url":"https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-http-content/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/payments/x402/charge-for-http-content/
  schema: 1
---
<p>The x402-proxy template is a Cloudflare Worker that sits in front of any HTTP backend. When a request hits a protected route, the proxy returns a 402 response with payment instructions. After the client pays, the proxy verifies the payment and forwards the request to your origin.</p>
<p>Deploy the x402-proxy template to your Cloudflare account:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/x402-proxy-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></li>
<li>An HTTP backend to gate</li>
<li>A wallet address to receive payments</li>
</ul>
<h2 id="configuration">Configuration</h2>
<p>Define protected routes in <code>wrangler.jsonc</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;vars&quot;: {&#10;		&quot;PAY_TO&quot;: &quot;0xYourWalletAddress&quot;,&#10;		&quot;NETWORK&quot;: &quot;base-sepolia&quot;,&#10;		&quot;PROTECTED_PATTERNS&quot;: [&#10;			{&#10;				&quot;pattern&quot;: &quot;/api/premium/*&quot;,&#10;				&quot;price&quot;: &quot;$0.10&quot;,&#10;				&quot;description&quot;: &quot;Premium API access&quot;&#10;			}&#10;		]&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2701.md")
</aside>
<h2 id="selective-gating-with-bot-management">Selective gating with Bot Management</h2>
<p>With <a href="/bots/">Bot Management</a>, the proxy can charge crawlers while keeping the site free for humans:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;pattern&quot;: &quot;/content/*&quot;,&#10;	&quot;price&quot;: &quot;$0.10&quot;,&#10;	&quot;description&quot;: &quot;Content access&quot;,&#10;	&quot;bot_score_threshold&quot;: 30,&#10;	&quot;except_detection_ids&quot;: [117479730]&#10;}&#10;</code></pre>
<p>Requests with a bot score at or below <code>bot_score_threshold</code> are directed to the paywall. Use <code>except_detection_ids</code> to allowlist specific crawlers by <a href="/ai-crawl-control/reference/bots/">detection ID</a>.</p>
<h2 id="deploy">Deploy</h2>
<p>Clone the template, edit <code>wrangler.jsonc</code>, and deploy:</p>
<pre tabindex="0"><code class="language-sh">git clone https://github.com/cloudflare/templates&#10;cd templates/x402-proxy-template&#10;npm install&#10;npx wrangler deploy&#10;</code></pre>
<p>For full configuration options and Bot Management examples, refer to the <a href="https://github.com/cloudflare/templates/tree/main/x402-proxy-template">template README</a>.</p>
<h2 id="custom-worker-endpoints">Custom Worker endpoints</h2>
<p>For more control, add x402 middleware directly to your Worker using Hono:</p>
<pre tabindex="0"><code class="language-ts">import { Hono } from &quot;hono&quot;;&#10;import { paymentMiddleware } from &quot;x402-hono&quot;;&#10;&#10;const app = new Hono&lt;{ Bindings: Env }&gt;();&#10;&#10;app.use(&#10;	paymentMiddleware(&#10;		&quot;0xYourWalletAddress&quot; as `0x${string}`,&#10;		{&#10;			&quot;/premium&quot;: {&#10;				price: &quot;$0.10&quot;,&#10;				network: &quot;base-sepolia&quot;,&#10;				config: { description: &quot;Premium content&quot; },&#10;			},&#10;		},&#10;		{ url: &quot;https://x402.org/facilitator&quot; },&#10;	),&#10;);&#10;&#10;app.get(&quot;/premium&quot;, (c) =&gt; c.json({ message: &quot;Thanks for paying!&quot; }));&#10;&#10;export default app;&#10;</code></pre>
<p>Refer to the <a href="https://github.com/cloudflare/agents/tree/main/examples/x402">x402 Workers example</a> for a complete implementation.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/ai-crawl-control/features/pay-per-crawl/">Pay Per Crawl</a> — Native Cloudflare monetization without custom code</li>
<li><a href="/agents/tools/payments/x402/charge-for-mcp-tools/">Charge for MCP tools</a> — Charge per tool call instead of per request</li>
<li><a href="https://x402.org">x402.org</a> — Protocol specification</li>
</ul>
