---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/examples/use-kv-from-durable-objects/
  description: Read and write to/from KV within a Durable Object
  full_title: Durable Objects - Use KV within Durable Objects · Cloudflare Durable Objects docs
  head_html: <title>Durable Objects - Use KV within Durable Objects · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Read and write to/from KV within a Durable Object"><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/examples/use-kv-from-durable-objects/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/examples/use-kv-from-durable-objects/index.md"><meta property="og:title" content="Durable Objects - Use KV within Durable Objects · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Read and write to/from KV within a Durable Object"><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/examples/use-kv-from-durable-objects/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/examples/use-kv-from-durable-objects/#page","headline":"Durable Objects - Use KV within Durable Objects \u00b7 Cloudflare Durable Objects docs","description":"Read and write to/from KV within a Durable Object","url":"https://developers.cloudflare.com/durable-objects/examples/use-kv-from-durable-objects/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/examples/use-kv-from-durable-objects/
  schema: 1
---
<p class="article-summary">Read and write to/from Workers KV within a Durable Object</p>
<p>The following Worker script shows you how to configure a <span class="nb-glossary-tooltip" title="Durable Object">Durable Object</span> to read from and/or write to a <a href="/kv/concepts/how-kv-works/">Workers KV namespace</a>. This is useful when using a Durable Object to coordinate between multiple clients, and allows you to serialize writes to KV and/or broadcast a single read from KV to hundreds or thousands of clients connected to a single Durable Object <a href="/durable-objects/best-practices/websockets/">using WebSockets</a>.</p>
<p>Prerequisites:</p>
<ul>
<li>A <a href="/kv/api/">KV namespace</a> created via the Cloudflare dashboard or the <a href="/workers/wrangler/install-and-update/">wrangler CLI</a>.</li>
<li>A <a href="/kv/concepts/kv-bindings/">configured binding</a> for the <code>kv_namespace</code> in the Cloudflare dashboard or Wrangler file.</li>
<li>A <a href="/workers/wrangler/configuration/#durable-objects">Durable Object namespace binding</a>.</li>
</ul>
<p>Configure your Wrangler file as follows:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8190.md")
</div>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8193.md")
</div></div>
