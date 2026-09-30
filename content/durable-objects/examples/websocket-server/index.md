---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/examples/websocket-server/
  description: Build a WebSocket server using Durable Objects and Workers.
  full_title: Build a WebSocket server · Cloudflare Durable Objects docs
  head_html: <title>Build a WebSocket server · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Build a WebSocket server using Durable Objects and Workers."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/examples/websocket-server/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/examples/websocket-server/index.md"><meta property="og:title" content="Build a WebSocket server · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build a WebSocket server using Durable Objects and Workers."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/examples/websocket-server/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Durable Objects"><meta name="pcx_tags" content="WebSockets"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/examples/websocket-server/#page","headline":"Build a WebSocket server \u00b7 Cloudflare Durable Objects docs","description":"Build a WebSocket server using Durable Objects and Workers.","url":"https://developers.cloudflare.com/durable-objects/examples/websocket-server/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["WebSockets"]}</script>
  markdown: true
  noindex: false
  route: /durable-objects/examples/websocket-server/
  schema: 1
---
<p class="article-summary">Build a WebSocket server using Durable Objects and Workers.</p>
<p>This example shows how to build a WebSocket server using <span class="nb-glossary-tooltip" title="Durable Object">Durable Objects</span> and Workers. The example exposes an endpoint to create a new WebSocket connection. This WebSocket connection echos any message while including the total number of WebSocket connections currently established. For more information, refer to <a href="/durable-objects/best-practices/websockets/">Use Durable Objects with WebSockets</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8177.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8181.md")
</div></div>
<p>Finally, configure your Wrangler file to include a Durable Object <a href="/durable-objects/get-started/#4-configure-durable-object-bindings">binding</a> and <a href="/durable-objects/reference/durable-objects-migrations/">migration</a> based on the <span class="nb-glossary-tooltip" title="namespace">namespace</span> and class name chosen previously.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8183.md")
</div>
<h3 id="related-resources">Related resources</h3>
<ul>
<li><a href="https://github.com/cloudflare/workers-chat-demo">Durable Objects: Edge Chat Demo</a>.</li>
</ul>
