---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/examples/readable-stream/
  description: Stream ReadableStream from Durable Objects.
  full_title: Use ReadableStream with Durable Object and Workers · Cloudflare Durable Objects docs
  head_html: <title>Use ReadableStream with Durable Object and Workers · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Stream ReadableStream from Durable Objects."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/examples/readable-stream/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/examples/readable-stream/index.md"><meta property="og:title" content="Use ReadableStream with Durable Object and Workers · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Stream ReadableStream from Durable Objects."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/examples/readable-stream/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/examples/readable-stream/#page","headline":"Use ReadableStream with Durable Object and Workers \u00b7 Cloudflare Durable Objects docs","description":"Stream ReadableStream from Durable Objects.","url":"https://developers.cloudflare.com/durable-objects/examples/readable-stream/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/examples/readable-stream/
  schema: 1
---
<p class="article-summary">Stream ReadableStream from Durable Objects.</p>
<p>This example demonstrates:</p>
<ul>
<li>A Worker receives a request, and forwards it to a Durable Object <code>my-id</code>.</li>
<li>The Durable Object streams an incrementing number every second, until it receives <code>AbortSignal</code>.</li>
<li>The Worker reads and logs the values from the stream.</li>
<li>The Worker then cancels the stream after 5 values.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8211.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8210.md")
</aside>
