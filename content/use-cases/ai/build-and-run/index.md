---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/ai/build-and-run/
  description: Build AI applications with serverless compute, edge inference, multi-provider gateways, and stateful coordination.
  full_title: Build and run AI applications · Cloudflare use cases
  head_html: <title>Build and run AI applications · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Build AI applications with serverless compute, edge inference, multi-provider gateways, and stateful coordination."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/ai/build-and-run/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/ai/build-and-run/index.md"><meta property="og:title" content="Build and run AI applications · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build AI applications with serverless compute, edge inference, multi-provider gateways, and stateful coordination."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/ai/build-and-run/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,Workers,Workers AI,AI Gateway,Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/ai/build-and-run/#page","headline":"Build and run AI applications \u00b7 Cloudflare use cases","description":"Build AI applications with serverless compute, edge inference, multi-provider gateways, and stateful coordination.","url":"https://developers.cloudflare.com/use-cases/ai/build-and-run/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/ai/build-and-run/
  schema: 1
---
<p>To build and deploy an AI application, you need compute for application logic, a way to run inference, and a gateway to manage costs across providers. Cloudflare Workers hosts your application logic and serves your frontend. Workers AI runs inference at the edge with pay-per-use pricing. AI Gateway adds caching, rate limiting, and observability across OpenAI, Anthropic, and other providers. Durable Objects coordinate stateful workflows and multi-turn conversations.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="workers">Workers</h3>
<p>Build and deploy serverless applications on Cloudflare's global network. <a href="/workers/">Learn more about Workers</a>.</p>
<ul>
<li><strong>Streaming responses</strong> - Stream AI responses token-by-token as they generate, without buffering the full reply</li>
<li><strong>Full-stack deployment</strong> - Serve frontend and backend from a single deployment without managing separate infrastructure</li>
</ul>
<h3 id="workers-ai">Workers AI</h3>
<p>Run inference on Cloudflare's global network via a Workers binding, with pay-per-use pricing. <a href="/workers-ai/">Learn more about Workers AI</a>.</p>
<ul>
<li><strong>Global inference</strong> - Run models at the Cloudflare location nearest to the user, reducing round-trip latency</li>
<li><strong>Pay-per-use pricing</strong> - No GPU reservations or idle costs; pay only for tokens processed</li>
</ul>
<h3 id="ai-gateway">AI Gateway</h3>
<p>Proxy requests to any AI provider with caching, rate limiting, and unified analytics. <a href="/ai-gateway/">Learn more about AI Gateway</a>.</p>
<ul>
<li><strong>Provider flexibility</strong> - Route requests to OpenAI, Anthropic, Workers AI, or any other provider through a single endpoint</li>
<li><strong>Unified observability</strong> - Track request volume, latency, costs, and errors across all providers in one place</li>
</ul>
<h3 id="durable-objects">Durable Objects</h3>
<p>Stateful objects with strongly consistent storage and coordination. <a href="/durable-objects/">Learn more about Durable Objects</a>.</p>
<ul>
<li><strong>Stateful workflows</strong> - Coordinate multi-step AI pipelines and maintain conversation state across requests</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/workers-ai/get-started/">Workers AI get started</a></li>
<li><a href="/ai-gateway/get-started/">AI Gateway get started</a></li>
<li><a href="/durable-objects/get-started/">Durable Objects get started</a></li>
</ol>
