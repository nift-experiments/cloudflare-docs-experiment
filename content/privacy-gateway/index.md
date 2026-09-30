---
cp9:
  canonical: https://developers.cloudflare.com/privacy-gateway/
  description: Privacy Gateway is a managed Oblivious HTTP (OHTTP) relay service that hides client IP addresses from application backends.
  full_title: Overview · Cloudflare Privacy Gateway docs
  head_html: <title>Overview · Cloudflare Privacy Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Privacy Gateway is a managed Oblivious HTTP (OHTTP) relay service that hides client IP addresses from application backends."><link rel="canonical" href="https://developers.cloudflare.com/privacy-gateway/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/privacy-gateway/index.md"><meta property="og:title" content="Overview · Cloudflare Privacy Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Privacy Gateway is a managed Oblivious HTTP (OHTTP) relay service that hides client IP addresses from application backends."><meta property="og:url" content="https://developers.cloudflare.com/privacy-gateway/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Privacy Gateway"><meta name="algolia_product_filter" content="Privacy Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Privacy Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/privacy-gateway/#page","headline":"Overview \u00b7 Cloudflare Privacy Gateway docs","description":"Privacy Gateway is a managed Oblivious HTTP (OHTTP) relay service that hides client IP addresses from application backends.","url":"https://developers.cloudflare.com/privacy-gateway/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /privacy-gateway/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/616.md")
</div>
<div class="nb-plan">
<p>Enterprise-only</p>
</div>
<p><a href="https://blog.cloudflare.com/building-privacy-into-internet-standards-and-how-to-make-your-app-more-private-today/">Privacy Gateway</a> is a managed service deployed on Cloudflare’s global network that implements part of the <a href="https://www.ietf.org/archive/id/draft-thomson-http-oblivious-01.html">Oblivious HTTP (OHTTP) IETF</a> standard. The goal of Privacy Gateway and Oblivious HTTP is to hide the client's IP address when interacting with an application backend.</p>
<p>OHTTP introduces a trusted third party between client and server, called a relay, whose purpose is to forward encrypted requests and responses between client and server. These messages are encrypted between client and server such that the relay learns nothing of the application data, beyond the length of the encrypted message and the server the client is interacting with.</p>
<hr />
<h2 id="availability">Availability</h2>
<p>Privacy Gateway is currently in closed beta – available to select privacy-oriented companies and partners. If you are interested, <a href="https://www.cloudflare.com/lp/privacy-edge/">contact us</a>.</p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/617.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/618.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/619.md")
</div>
