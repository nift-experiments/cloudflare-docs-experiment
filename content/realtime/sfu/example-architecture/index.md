---
cp9:
  canonical: https://developers.cloudflare.com/realtime/sfu/example-architecture/
  description: Reference architecture for building a video calling application with Realtime SFU.
  full_title: Example architecture · Cloudflare Realtime docs
  head_html: <title>Example architecture · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference architecture for building a video calling application with Realtime SFU."><link rel="canonical" href="https://developers.cloudflare.com/realtime/sfu/example-architecture/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/sfu/example-architecture/index.md"><meta property="og:title" content="Example architecture · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference architecture for building a video calling application with Realtime SFU."><meta property="og:url" content="https://developers.cloudflare.com/realtime/sfu/example-architecture/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/sfu/example-architecture/#page","headline":"Example architecture \u00b7 Cloudflare Realtime docs","description":"Reference architecture for building a video calling application with Realtime SFU.","url":"https://developers.cloudflare.com/realtime/sfu/example-architecture/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/sfu/example-architecture/
  schema: 1
---
<div class="full-img">
<p><img src="/assets/upstream/images/realtime/video-calling-application.png" alt="Example Architecture" /></p>
</div>
<ol>
<li>Clients connect to the backend service</li>
<li>Backend service manages the relationship between the clients and the tracks they should subscribe to</li>
<li>Backend service contacts the Cloudflare Realtime API to pass the SDP from the clients to establish the WebRTC connection.</li>
<li>Realtime API relays back the Realtime API SDP reply and renegotiation messages.</li>
<li>If desired, headless clients can be used to record the content from other clients or publish content.</li>
<li>Admin manages the rooms and room members.</li>
</ol>
