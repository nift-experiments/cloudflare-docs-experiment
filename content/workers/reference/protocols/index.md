---
cp9:
  canonical: https://developers.cloudflare.com/workers/reference/protocols/
  description: Supported protocols on the Workers platform.
  full_title: Protocols · Cloudflare Workers docs
  head_html: <title>Protocols · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Supported protocols on the Workers platform."><link rel="canonical" href="https://developers.cloudflare.com/workers/reference/protocols/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/reference/protocols/index.md"><meta property="og:title" content="Protocols · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Supported protocols on the Workers platform."><meta property="og:url" content="https://developers.cloudflare.com/workers/reference/protocols/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/reference/protocols/#page","headline":"Protocols \u00b7 Cloudflare Workers docs","description":"Supported protocols on the Workers platform.","url":"https://developers.cloudflare.com/workers/reference/protocols/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/reference/protocols/
  schema: 1
---
<p>Cloudflare Workers support the following protocols and interfaces:</p>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Inbound</th>
<th>Outbound</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>HTTP / HTTPS</strong></td>
<td>Handle incoming HTTP requests using the <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch()</code> handler</a></td>
<td>Make HTTP subrequests using the <a href="/workers/runtime-apis/fetch/"><code>fetch()</code> API</a></td>
</tr>
<tr>
<td><strong>Direct TCP sockets</strong></td>
<td>Support for handling inbound TCP connections is <a href="https://blog.cloudflare.com/workers-tcp-socket-api-connect-databases/">coming soon</a></td>
<td>Create outbound TCP connections using the <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code> API</a></td>
</tr>
<tr>
<td><strong>WebSockets</strong></td>
<td>Accept incoming WebSocket connections using the <a href="/workers/runtime-apis/websockets/"><code>WebSocket</code> API</a></td>
<td></td>
</tr>
<tr>
<td><strong>HTTP/3 (QUIC)</strong></td>
<td>Accept inbound requests over <a href="https://www.cloudflare.com/learning/performance/what-is-http3/">HTTP/3</a> by enabling it on your <a href="/fundamentals/concepts/accounts-and-zones/#zones">zone</a> in <strong>Speed</strong> &gt; <strong>Settings</strong> &gt; <strong>Protocol Optimization</strong> area of the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</td>
<td></td>
</tr>
<tr>
<td><strong>SMTP</strong></td>
<td>Use <a href="/email-service/api/route-emails/email-handler/">Email Workers</a> to process and forward email, without having to manage TCP connections to SMTP email servers</td>
<td><a href="/email-service/api/route-emails/email-handler/">Email Workers</a></td>
</tr>
</tbody>
</table>
