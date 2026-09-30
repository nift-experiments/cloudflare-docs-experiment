---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/ai-search/
  description: Give agents retrieval capabilities with Cloudflare AI Search.
  full_title: AI Search · Cloudflare Agents docs
  head_html: <title>AI Search · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Give agents retrieval capabilities with Cloudflare AI Search."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/ai-search/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/ai-search/index.md"><meta property="og:title" content="AI Search · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Give agents retrieval capabilities with Cloudflare AI Search."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/ai-search/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/tools/ai-search/#page","headline":"AI Search \u00b7 Cloudflare Agents docs","description":"Give agents retrieval capabilities with Cloudflare AI Search.","url":"https://developers.cloudflare.com/agents/tools/ai-search/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/ai-search/
  schema: 1
---
<p>Agents can use <a href="/ai-search/">AI Search</a> to retrieve relevant information from indexed content and use it to augment <a href="/agents/runtime/operations/using-ai-models/">calls to AI models</a>. AI Search manages the retrieval pipeline for you, including indexing, search, and optional chat completions over your content.</p>
<p>Use AI Search when you want an agent to:</p>
<ul>
<li>Search product docs, support content, user files, or internal knowledge bases.</li>
<li>Retrieve relevant chunks before calling a model.</li>
<li>Use managed indexing instead of building retrieval infrastructure yourself.</li>
<li>Query content from an R2 bucket, website, or uploaded files.</li>
</ul>
<h2 id="basic-pattern">Basic pattern</h2>
<p>Bind AI Search to your Worker, then query an instance from an agent method.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1855.md")
</div>
<p>For answer generation, use <code>chatCompletions()</code> to retrieve relevant content and generate a response in one call.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1856.md")
</div>
<h2 id="configuration">Configuration</h2>
<p>Use an <code>ai_search_namespaces</code> binding when the agent needs to access AI Search instances by name.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1857.md")
</div>
<p>Use <code>remote: true</code> to query deployed AI Search instances during local development with <code>wrangler dev</code>.</p>
<h2 id="related-resources">Related resources</h2>
<div class="nb-card nb-link-card"><h3 id="card-ai-search-ai-search"><a href="/ai-search/">AI Search</a></h3><p>Create managed retrieval pipelines over websites, R2 buckets, and uploaded files.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-workers-binding-ai-search-api-search-workers-binding"><a href="/ai-search/api/search/workers-binding/">Workers binding</a></h3><p>Query AI Search directly from Workers code.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-create-an-ai-search-instance-ai-search-get-started"><a href="/ai-search/get-started/">Create an AI Search instance</a></h3><p>Create your first AI Search instance and run your first query.</p></div>
