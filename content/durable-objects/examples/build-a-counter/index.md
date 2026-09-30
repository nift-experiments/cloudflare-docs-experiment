---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/examples/build-a-counter/
  description: Build a counter using Durable Objects and Workers with RPC methods.
  full_title: Build a counter · Cloudflare Durable Objects docs
  head_html: <title>Build a counter · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Build a counter using Durable Objects and Workers with RPC methods."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/examples/build-a-counter/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/examples/build-a-counter/index.md"><meta property="og:title" content="Build a counter · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build a counter using Durable Objects and Workers with RPC methods."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/examples/build-a-counter/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Durable Objects,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/examples/build-a-counter/#page","headline":"Build a counter \u00b7 Cloudflare Durable Objects docs","description":"Build a counter using Durable Objects and Workers with RPC methods.","url":"https://developers.cloudflare.com/durable-objects/examples/build-a-counter/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/examples/build-a-counter/
  schema: 1
---
<p class="article-summary">Build a counter using Durable Objects and Workers with RPC methods.</p>
<p>This example shows how to build a counter using Durable Objects and Workers with <a href="/workers/runtime-apis/rpc">RPC methods</a> that can print, increment, and decrement a <code>name</code> provided by the URL query string parameter, for example, <code>?name=A</code>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8227.md")
</div></div>
<p>Finally, configure your Wrangler file to include a Durable Object <a href="/durable-objects/get-started/#4-configure-durable-object-bindings">binding</a> and <a href="/durable-objects/reference/durable-objects-migrations/">migration</a> based on the namespace and class name chosen previously.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8228.md")
</div>
<h3 id="related-resources">Related resources</h3>
<ul>
<li><a href="/workers/runtime-apis/rpc/">Workers RPC</a></li>
<li><a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">Durable Objects: Easy, Fast, Correct — Choose three</a>.</li>
</ul>
