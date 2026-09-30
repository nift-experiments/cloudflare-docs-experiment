---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/ai/store-and-retrieve-context/
  description: Store vector embeddings, conversation history, and application state for AI applications using serverless databases and object storage.
  full_title: Store and retrieve context · Cloudflare use cases
  head_html: <title>Store and retrieve context · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Store vector embeddings, conversation history, and application state for AI applications using serverless databases and object storage."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/ai/store-and-retrieve-context/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/ai/store-and-retrieve-context/index.md"><meta property="og:title" content="Store and retrieve context · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Store vector embeddings, conversation history, and application state for AI applications using serverless databases and object storage."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/ai/store-and-retrieve-context/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,Vectorize,D1,R2,KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/ai/store-and-retrieve-context/#page","headline":"Store and retrieve context \u00b7 Cloudflare use cases","description":"Store vector embeddings, conversation history, and application state for AI applications using serverless databases and object storage.","url":"https://developers.cloudflare.com/use-cases/ai/store-and-retrieve-context/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/ai/store-and-retrieve-context/
  schema: 1
---
<p>AI applications need specialized storage for vector embeddings, conversation history, training data, and cached responses. Cloudflare Vectorize stores and queries embeddings for Retrieval Augmented Generation (RAG), D1 provides SQL storage for structured data, R2 stores documents and assets, and KV caches frequent responses at the edge.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="vectorize">Vectorize</h3>
<p>Vector database for storing and querying embeddings. <a href="/vectorize/">Learn more about Vectorize</a>.</p>
<ul>
<li><strong>Vector search</strong> - Store embeddings and find semantically similar content for Retrieval Augmented Generation (RAG) and recommendation features</li>
</ul>
<h3 id="d1">D1</h3>
<p>Serverless SQL database built on SQLite, with global read replication. <a href="/d1/">Learn more about D1</a>.</p>
<ul>
<li><strong>Structured storage</strong> - Structured Query Language (SQL) database for conversation history, user data, and application metadata</li>
</ul>
<h3 id="r2">R2</h3>
<p>S3-compatible object storage with zero egress fees. <a href="/r2/">Learn more about R2</a>.</p>
<ul>
<li><strong>Object storage</strong> - Store documents, training data, and generated assets with no egress fees</li>
</ul>
<h3 id="kv">KV</h3>
<p>Globally distributed key-value storage for low-latency reads. <a href="/kv/">Learn more about KV</a>.</p>
<ul>
<li><strong>Edge caching</strong> - Cache frequent AI responses at the edge to reduce inference costs and latency</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/vectorize/get-started/">Vectorize get started</a></li>
<li><a href="/d1/get-started/">D1 get started</a></li>
<li><a href="/r2/get-started/">R2 get started</a></li>
</ol>
