---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/web-apps/real-time/
  description: Build interactive applications with WebSockets, real-time collaboration, and live updates.
  full_title: Add real-time features · Cloudflare use cases
  head_html: <title>Add real-time features · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Build interactive applications with WebSockets, real-time collaboration, and live updates."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/web-apps/real-time/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/web-apps/real-time/index.md"><meta property="og:title" content="Add real-time features · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build interactive applications with WebSockets, real-time collaboration, and live updates."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/web-apps/real-time/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,Durable Objects,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/web-apps/real-time/#page","headline":"Add real-time features \u00b7 Cloudflare use cases","description":"Build interactive applications with WebSockets, real-time collaboration, and live updates.","url":"https://developers.cloudflare.com/use-cases/web-apps/real-time/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/web-apps/real-time/
  schema: 1
---
<p>Real-time features, such as live chat, collaborative editing, and multiplayer interactions, require persistent connections and strongly consistent state. Cloudflare Durable Objects maintain WebSocket connections and coordinate shared state, while Queues handle background event processing.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="durable-objects">Durable Objects</h3>
<p>Stateful objects with strongly consistent storage and coordination. <a href="/durable-objects/">Learn more about Durable Objects</a>.</p>
<ul>
<li><strong>WebSocket support</strong> - Maintain persistent connections and broadcast messages across clients in real time</li>
<li><strong>Collaborative editing</strong> - Build multiplayer and co-editing experiences with strongly consistent shared state</li>
<li><strong>Strong consistency</strong> - Coordinate state across many concurrent connections with transactional guarantees</li>
</ul>
<h3 id="queues">Queues</h3>
<p>Reliable message queuing and background processing for Workers. <a href="/queues/">Learn more about Queues</a>.</p>
<ul>
<li><strong>Event processing</strong> - Handle webhooks and background jobs reliably without blocking the main request path</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/durable-objects/get-started/">Durable Objects get started</a></li>
<li><a href="/durable-objects/examples/websocket-hibernation-server/">WebSocket connections with Durable Objects</a></li>
<li><a href="/queues/get-started/">Queues get started</a></li>
</ol>
