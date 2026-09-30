---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/websockets-api/
  description: Use persistent WebSocket connections through AI Gateway for real-time and non-realtime AI interactions.
  full_title: WebSockets API · Cloudflare AI Gateway docs
  head_html: <title>WebSockets API · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Use persistent WebSocket connections through AI Gateway for real-time and non-realtime AI interactions."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/websockets-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/websockets-api/index.md"><meta property="og:title" content="WebSockets API · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use persistent WebSocket connections through AI Gateway for real-time and non-realtime AI interactions."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/websockets-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/websockets-api/#page","headline":"WebSockets API \u00b7 Cloudflare AI Gateway docs","description":"Use persistent WebSocket connections through AI Gateway for real-time and non-realtime AI interactions.","url":"https://developers.cloudflare.com/ai-gateway/usage/websockets-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/websockets-api/
  schema: 1
---
<p>The AI Gateway WebSockets API provides a persistent connection for AI interactions, eliminating repeated handshakes and reducing latency. This API is divided into two categories:</p>
<ul>
<li><strong>Realtime APIs</strong> - Designed for AI providers that offer low-latency, multimodal interactions over WebSockets.</li>
<li><strong>Non-Realtime APIs</strong> - Supports standard WebSocket communication for AI providers, including those that do not natively support WebSockets.</li>
</ul>
<h2 id="when-to-use-websockets">When to use WebSockets</h2>
<p>WebSockets are long-lived TCP connections that enable bi-directional, real-time and non realtime communication between client and server. Unlike HTTP connections, which require repeated handshakes for each request, WebSockets maintain the connection, supporting continuous data exchange with reduced overhead. WebSockets are ideal for applications needing low-latency, real-time data, such as voice assistants.</p>
<h2 id="key-benefits">Key benefits</h2>
<ul>
<li><strong>Reduced overhead</strong>: Avoid overhead of repeated handshakes and TLS negotiations by maintaining a single, persistent connection.</li>
<li><strong>Provider compatibility</strong>: Works with all AI providers in AI Gateway. Even if your chosen provider does not support WebSockets, Cloudflare handles it for you, managing the requests to your preferred AI provider.</li>
</ul>
<h2 id="key-differences">Key differences</h2>
<table>
<thead>
<tr>
<th align="left">Feature</th>
<th align="left">Realtime APIs</th>
<th align="left">Non-Realtime APIs</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Purpose</strong></td>
<td align="left">Enables real-time, multimodal AI interactions for providers that offer dedicated WebSocket endpoints.</td>
<td align="left">Supports WebSocket-based AI interactions with providers that do not natively support WebSockets.</td>
</tr>
<tr>
<td align="left"><strong>Use Case</strong></td>
<td align="left">Streaming responses for voice, video, and live interactions.</td>
<td align="left">Text-based queries and responses, such as LLM requests.</td>
</tr>
<tr>
<td align="left"><strong>AI Provider Support</strong></td>
<td align="left"><a href="/ai-gateway/usage/websockets-api/realtime-api/#supported-providers">Limited to providers offering real-time WebSocket APIs.</a></td>
<td align="left"><a href="/ai-gateway/usage/providers/">All AI providers in AI Gateway.</a></td>
</tr>
<tr>
<td align="left"><strong>Streaming Support</strong></td>
<td align="left">Providers natively support real-time data streaming.</td>
<td align="left">AI Gateway handles streaming via WebSockets.</td>
</tr>
</tbody>
</table>
<p>For details on implementation, refer to the next sections:</p>
<ul>
<li><a href="/ai-gateway/usage/websockets-api/realtime-api/">Realtime WebSockets API</a></li>
<li><a href="/ai-gateway/usage/websockets-api/non-realtime-api/">Non-Realtime WebSockets API</a></li>
</ul>
