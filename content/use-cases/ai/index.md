---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/ai/
  description: Build AI applications on Cloudflare with Workers AI inference, AI Gateway, Vectorize, and serverless storage.
  full_title: AI applications · Use cases · Cloudflare use cases
  head_html: <title>AI applications · Use cases · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Build AI applications on Cloudflare with Workers AI inference, AI Gateway, Vectorize, and serverless storage."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/ai/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/ai/index.md"><meta property="og:title" content="AI applications · Use cases · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build AI applications on Cloudflare with Workers AI inference, AI Gateway, Vectorize, and serverless storage."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/ai/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Use cases,Workers AI,AI Gateway,Vectorize"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/use-cases/ai/#page","headline":"AI applications \u00b7 Use cases \u00b7 Cloudflare use cases","description":"Build AI applications on Cloudflare with Workers AI inference, AI Gateway, Vectorize, and serverless storage.","url":"https://developers.cloudflare.com/use-cases/ai/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/ai/
  schema: 1
---
<p>Build and deploy AI applications on Cloudflare's global network with inference at the edge, vector databases, and model gateways. Workers AI runs Large Language Models (LLMs), text embeddings, image generation, and other models with pay-per-use pricing. AI Gateway proxies requests to OpenAI, Anthropic, and other providers with caching and unified analytics. Vectorize stores embeddings for Retrieval Augmented Generation (RAG) workflows.</p>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/uv1Cz_BDFmo" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<p>AI applications can present unique infrastructure challenges, such as unpredictable inference costs, latency-sensitive user experiences, and the need to work with multiple model providers. Cloudflare provides a complete platform for building AI applications that are fast, cost-effective, and globally distributed.</p>
<ul class="directory-listing"><li><a href="/use-cases/ai/build-and-run/">Build and run AI applications</a></li><li><a href="/use-cases/ai/store-and-retrieve-context/">Store and retrieve context</a></li><li><a href="/use-cases/ai/control-costs/">Control costs and improve quality</a></li></ul>
<h2 id="architecture-patterns">Architecture patterns</h2>
<h3 id="retrieval-augmented-generation-rag">Retrieval Augmented Generation (RAG)</h3>
<p>Combine vector search with Large Language Model (LLM) inference to ground responses in your own data:</p>
<ul>
<li><strong>Vectorize</strong> stores embeddings of your knowledge base</li>
<li><strong>Workers</strong> receives user queries and searches for relevant context</li>
<li><strong>Workers AI</strong> or <strong>AI Gateway</strong> generates responses using retrieved context</li>
</ul>
<h3 id="multi-provider-ai-gateway">Multi-provider AI gateway</h3>
<p>Use AI Gateway to route requests across providers while maintaining a single interface:</p>
<ul>
<li><strong>AI Gateway</strong> proxies requests to OpenAI, Anthropic, or Workers AI</li>
<li>Built-in caching reduces costs for repeated queries</li>
<li>Unified logging and analytics across all providers</li>
</ul>
<h3 id="real-time-ai-features">Real-time AI features</h3>
<p>Deploy low-latency AI features directly at the edge:</p>
<ul>
<li><strong>Workers</strong> handles requests at the nearest Cloudflare location and runs inference via the Workers AI binding — no round-trips to origin servers</li>
<li><strong>KV</strong> caches frequent responses to reduce inference calls and latency</li>
<li><strong>D1</strong> stores session state and conversation history alongside the inference logic</li>
</ul>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<h3 id="create-a-new-application">Create a new application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li><a href="https://nodejs.org/">Node.js</a> (version 16.17.0 or later) installed on your machine.</li>
<li><a href="/workers/wrangler/install-and-update/">Wrangler</a> installed. Wrangler is the command-line interface (CLI) for deploying Workers and managing bindings.</li>
</ul>
<h3 id="use-an-existing-application">Use an existing application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li><a href="/ai-gateway/">AI Gateway</a> does not require a domain added to Cloudflare. You can place it in front of any existing AI provider (OpenAI, Anthropic, and others) by updating your API endpoint to route through AI Gateway.</li>
<li>If you plan to add Workers AI inference or Vectorize to an existing application, you also need <a href="https://nodejs.org/">Node.js</a> (version 16.17.0 or later) and <a href="/workers/wrangler/install-and-update/">Wrangler</a> installed.</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/15249.md")
</div>
