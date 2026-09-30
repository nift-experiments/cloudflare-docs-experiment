---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/saas/data-isolation/
  description: Isolate customer data in a multi-tenant SaaS platform using per-tenant databases, object storage, and key-value stores.
  full_title: Store and isolate customer data · Cloudflare use cases
  head_html: <title>Store and isolate customer data · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Isolate customer data in a multi-tenant SaaS platform using per-tenant databases, object storage, and key-value stores."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/saas/data-isolation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/saas/data-isolation/index.md"><meta property="og:title" content="Store and isolate customer data · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Isolate customer data in a multi-tenant SaaS platform using per-tenant databases, object storage, and key-value stores."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/saas/data-isolation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,Workers,D1,R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/saas/data-isolation/#page","headline":"Store and isolate customer data \u00b7 Cloudflare use cases","description":"Isolate customer data in a multi-tenant SaaS platform using per-tenant databases, object storage, and key-value stores.","url":"https://developers.cloudflare.com/use-cases/saas/data-isolation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/saas/data-isolation/
  schema: 1
---
<p>Multi-tenant platforms need to store customer data with appropriate isolation — per-tenant databases, separate object storage, or row-level separation. Cloudflare provides serverless storage options that support tenant isolation at the database, bucket, or key-prefix level.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="d1">D1</h3>
<p>Serverless SQL database built on SQLite, with global read replication. <a href="/d1/">Learn more about D1</a>.</p>
<ul>
<li><strong>Database per tenant</strong> - Create isolated D1 databases per customer for complete data separation, or use row-level isolation in a shared database</li>
</ul>
<h3 id="r2">R2</h3>
<p>S3-compatible object storage with zero egress fees. <a href="/r2/">Learn more about R2</a>.</p>
<ul>
<li><strong>Object storage</strong> - Store customer files and assets per tenant using prefix or bucket-level isolation, with no egress fees</li>
</ul>
<h3 id="durable-objects">Durable Objects</h3>
<p>Stateful objects with strongly consistent storage and coordination. <a href="/durable-objects/">Learn more about Durable Objects</a>.</p>
<ul>
<li><strong>Real-time coordination</strong> - Manage stateful workflows and provide strong consistency for multi-tenant operations</li>
</ul>
<h3 id="kv">KV</h3>
<p>Globally distributed key-value storage for low-latency reads. <a href="/kv/">Learn more about KV</a>.</p>
<ul>
<li><strong>Edge configuration</strong> - Store per-tenant settings, feature flags, and session data at the edge for low-latency reads</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/d1/get-started/">D1 get started</a></li>
<li><a href="/r2/get-started/">R2 get started</a></li>
<li><a href="/durable-objects/get-started/">Durable Objects get started</a></li>
</ol>
