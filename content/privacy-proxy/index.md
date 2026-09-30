---
cp9:
  canonical: https://developers.cloudflare.com/privacy-proxy/
  description: Privacy Proxy is a MASQUE-based forward proxy that hides client IP addresses while preserving geolocation accuracy.
  full_title: Privacy Proxy · Cloudflare Privacy Proxy docs
  head_html: <title>Privacy Proxy · Cloudflare Privacy Proxy docs</title><meta name="generator" content="Nift"><meta name="description" content="Privacy Proxy is a MASQUE-based forward proxy that hides client IP addresses while preserving geolocation accuracy."><link rel="canonical" href="https://developers.cloudflare.com/privacy-proxy/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/privacy-proxy/index.md"><meta property="og:title" content="Privacy Proxy · Cloudflare Privacy Proxy docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Privacy Proxy is a MASQUE-based forward proxy that hides client IP addresses while preserving geolocation accuracy."><meta property="og:url" content="https://developers.cloudflare.com/privacy-proxy/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Privacy Proxy"><meta name="algolia_product_filter" content="Privacy Proxy"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Privacy Proxy"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/privacy-proxy/#page","headline":"Privacy Proxy \u00b7 Cloudflare Privacy Proxy docs","description":"Privacy Proxy is a MASQUE-based forward proxy that hides client IP addresses while preserving geolocation accuracy.","url":"https://developers.cloudflare.com/privacy-proxy/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /privacy-proxy/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/605.md")
</div>
<div class="nb-plan">
<p>Enterprise-only</p>
</div>
<p>Privacy Proxy is a managed proxy service that runs on Cloudflare's global network. It uses the <a href="https://datatracker.ietf.org/wg/masque/about/">MASQUE</a> protocol suite to proxy TCP and UDP traffic via HTTP CONNECT and CONNECT-UDP methods over HTTP/2 and HTTP/3.</p>
<p>Privacy Proxy separates user identity from user activity. Users authenticate to the proxy without revealing which destinations they visit, and destination servers see requests from Cloudflare IP addresses without learning who made them.</p>
<p>Privacy Proxy powers services like <a href="https://blog.cloudflare.com/cloudflare-now-powering-microsoft-edge-secure-network/">Microsoft Edge Secure Network</a> and serves as a second-hop relay for <a href="https://blog.cloudflare.com/icloud-private-relay/">iCloud Private Relay</a>.</p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/606.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/607.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/608.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/609.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/610.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/611.md")
</div>
<hr />
<h2 id="availability">Availability</h2>
<p>Privacy Proxy is available as a managed service for Enterprise customers. <a href="https://www.cloudflare.com/lp/privacy-edge/">Contact us</a> to discuss your use case and get started.</p>
