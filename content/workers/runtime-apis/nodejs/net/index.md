---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/nodejs/net/
  description: Use the Node.js net module in Cloudflare Workers to create TCP socket connections to external servers.
  full_title: net · Cloudflare Workers docs
  head_html: <title>net · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the Node.js net module in Cloudflare Workers to create TCP socket connections to external servers."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/net/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/net/index.md"><meta property="og:title" content="net · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the Node.js net module in Cloudflare Workers to create TCP socket connections to external servers."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/nodejs/net/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/net/#page","headline":"net \u00b7 Cloudflare Workers docs","description":"Use the Node.js net module in Cloudflare Workers to create TCP socket connections to external servers.","url":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/net/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/nodejs/net/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17141.md")
</aside>
<p>You can use <a href="https://nodejs.org/api/net.html"><code>node:net</code></a> to create a direct connection to servers via a TCP sockets
with <a href="https://nodejs.org/api/net.html#class-netsocket"><code>net.Socket</code></a>.</p>
<p>These functions use <a href="/workers/runtime-apis/tcp-sockets/#connect"><code>connect</code></a> functionality from the built-in <code>cloudflare:sockets</code> module.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17142.md")
</div>
<p>Additionally, other APIs such as <a href="https://nodejs.org/api/net.html#class-netblocklist"><code>net.BlockList</code></a>
and <a href="https://nodejs.org/api/net.html#class-netsocketaddress"><code>net.SocketAddress</code></a> are available.</p>
<p>Note that the <a href="https://nodejs.org/api/net.html#class-netserver"><code>net.Server</code></a> class is not supported by Workers.</p>
<p>The full <code>node:net</code> API is documented in the <a href="https://nodejs.org/api/net.html">Node.js documentation for <code>node:net</code></a>.</p>
<pre tabindex="0"><code>&#10;</code></pre>
