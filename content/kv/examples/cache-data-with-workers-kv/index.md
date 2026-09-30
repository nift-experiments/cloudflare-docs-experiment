---
cp9:
  canonical: https://developers.cloudflare.com/kv/examples/cache-data-with-workers-kv/
  description: Example of how to use Workers KV to build a distributed application configuration store.
  full_title: Cache data with Workers KV · Cloudflare Workers KV docs
  head_html: <title>Cache data with Workers KV · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Example of how to use Workers KV to build a distributed application configuration store."><link rel="canonical" href="https://developers.cloudflare.com/kv/examples/cache-data-with-workers-kv/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/examples/cache-data-with-workers-kv/index.md"><meta property="og:title" content="Cache data with Workers KV · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Example of how to use Workers KV to build a distributed application configuration store."><meta property="og:url" content="https://developers.cloudflare.com/kv/examples/cache-data-with-workers-kv/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/examples/cache-data-with-workers-kv/#page","headline":"Cache data with Workers KV \u00b7 Cloudflare Workers KV docs","description":"Example of how to use Workers KV to build a distributed application configuration store.","url":"https://developers.cloudflare.com/kv/examples/cache-data-with-workers-kv/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/examples/cache-data-with-workers-kv/
  schema: 1
---
<p class="article-summary">Cache data or API responses in Workers KV to improve application performance</p>
<p>Workers KV can be used as a persistent, single, global cache accessible from Cloudflare Workers to speed up your application.
Data cached in Workers KV is accessible from all other Cloudflare locations as well, and persists until expiry or deletion.</p>
<p>After fetching data from external resources in your Workers application, you can write the data to Workers KV.
On subsequent Worker requests (in the same region or in other regions), you can read the cached data from Workers KV instead of calling the external API.
This improves your Worker application's performance and resilience while reducing load on external resources.</p>
<p>This example shows how you can cache data in Workers KV and read cached data from Workers KV in a Worker application.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/9519.md")
</aside>
<h2 id="cache-data-in-workers-kv-from-your-worker-application">Cache data in Workers KV from your Worker application</h2>
<p>In the following <code>index.ts</code> file, the Worker fetches data from an external server and caches the response in Workers KV. If the data is already cached in Workers KV, the Worker reads the cached data from Workers KV instead of calling the external API.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9522.md")
</div></div>
<p>This code snippet demonstrates how to read and update cached data in Workers KV from your Worker.
If the data is not in the Workers KV cache, the Worker fetches the data from an external server and caches it in Workers KV.</p>
<p>In this example, we convert HTML to JSON to demonstrate how to cache JSON data with Workers KV, but any type of data
can be cached in Workers KV. For instance, you could cache API responses, HTML content, or any other data that you want to persist across requests.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/languages/rust/">Rust support in Workers</a>.</li>
<li><a href="/kv/get-started/">Using KV in Workers</a>.</li>
</ul>
