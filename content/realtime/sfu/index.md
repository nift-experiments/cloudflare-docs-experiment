---
cp9:
  canonical: https://developers.cloudflare.com/realtime/sfu/
  description: Build custom audio, video, and data applications from WebRTC primitives with Cloudflare Realtime SFU.
  full_title: Overview · Cloudflare Realtime docs
  head_html: <title>Overview · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Build custom audio, video, and data applications from WebRTC primitives with Cloudflare Realtime SFU."><link rel="canonical" href="https://developers.cloudflare.com/realtime/sfu/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/sfu/index.md"><meta property="og:title" content="Overview · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build custom audio, video, and data applications from WebRTC primitives with Cloudflare Realtime SFU."><meta property="og:url" content="https://developers.cloudflare.com/realtime/sfu/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/sfu/#page","headline":"Overview \u00b7 Cloudflare Realtime docs","description":"Build custom audio, video, and data applications from WebRTC primitives with Cloudflare Realtime SFU.","url":"https://developers.cloudflare.com/realtime/sfu/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/sfu/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/11576.md")
</div>
<p>Cloudflare Realtime SFU routes WebRTC media tracks and DataChannels between browser, native, server, and external media endpoints. Your application controls who publishes, who subscribes, and how participants discover each other.</p>
<p>Cloudflare Realtime SFU runs on <a href="https://www.cloudflare.com/network/">Cloudflare's global cloud network</a> in hundreds of cities worldwide.</p>
<h2 id="what-you-can-build">What you can build</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/11581.md")
</div>
<h2 id="application-architecture">Application architecture</h2>
<p>Each client creates a WebRTC PeerConnection. Your backend stores the application
secret and uses the Realtime SFU API to create the corresponding session. It
also authenticates users, authorizes publish and subscribe operations, and
shares session or track identifiers through your application state.</p>
<p>Realtime SFU forwards the selected media or data. It does not define rooms,
participants, roles, or presence for your application.</p>
<h2 id="explore-examples">Explore examples</h2>
<p>Use the <a href="https://github.com/cloudflare/realtime-examples">Realtime Examples repository</a>
to choose a starting point for what you want to build. Each example identifies
its status, credential boundary, and known limitations.</p>
<p><a class="nb-link-button" href="https://github.com/cloudflare/realtime-examples">Browse Realtime examples</a>
<a class="nb-link-button" href="/realtime/sfu/get-started/">Create an SFU application</a>
<a class="nb-link-button" href="https://dash.cloudflare.com/?to=/:account/calls">Realtime dashboard</a></p>
