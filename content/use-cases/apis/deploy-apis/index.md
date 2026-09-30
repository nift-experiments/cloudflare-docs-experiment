---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/apis/deploy-apis/
  description: Deploy globally distributed APIs that scale automatically with no servers to manage.
  full_title: Deploy APIs at the edge · Cloudflare use cases
  head_html: <title>Deploy APIs at the edge · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Deploy globally distributed APIs that scale automatically with no servers to manage."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/apis/deploy-apis/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/apis/deploy-apis/index.md"><meta property="og:title" content="Deploy APIs at the edge · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy globally distributed APIs that scale automatically with no servers to manage."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/apis/deploy-apis/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,Workers,Queues"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/apis/deploy-apis/#page","headline":"Deploy APIs at the edge \u00b7 Cloudflare use cases","description":"Deploy globally distributed APIs that scale automatically with no servers to manage.","url":"https://developers.cloudflare.com/use-cases/apis/deploy-apis/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/apis/deploy-apis/
  schema: 1
---
<p>Deploying APIs on traditional infrastructure means managing servers, configuring regions, and provisioning for traffic spikes. Cloudflare Workers runs your API handlers in 300+ locations worldwide with automatic scaling and fast startup times.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="workers">Workers</h3>
<p>Build and deploy serverless applications on Cloudflare's global network. <a href="/workers/">Learn more about Workers</a>.</p>
<ul>
<li><strong>Global deployment</strong> - API handlers run in 300+ Cloudflare locations worldwide with no regional configuration</li>
<li><strong>Auto-scaling</strong> - Handle traffic spikes without provisioning servers or setting capacity limits</li>
</ul>
<h3 id="queues">Queues</h3>
<p>Reliable message queuing and background processing for Workers. <a href="/queues/">Learn more about Queues</a>.</p>
<ul>
<li><strong>Async processing</strong> - Offload webhook delivery and background jobs without blocking the API response</li>
</ul>
<h3 id="d1-and-durable-objects">D1 and Durable Objects</h3>
<p>Serverless SQL database built on SQLite, with global read replication (<a href="/d1/">learn more about D1</a>). Stateful objects with strongly consistent storage and coordination (<a href="/durable-objects/">learn more about Durable Objects</a>).</p>
<ul>
<li><strong>Integrated storage</strong> - Structured Query Language (SQL) database and strongly consistent state storage available as Worker bindings</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/workers/get-started/">Workers get started</a></li>
<li><a href="/d1/get-started/">D1 get started</a></li>
<li><a href="/queues/get-started/">Queues get started</a></li>
</ol>
