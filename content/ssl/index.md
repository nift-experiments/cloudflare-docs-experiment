---
cp9:
  canonical: https://developers.cloudflare.com/ssl/
  description: Manage SSL/TLS certificates for encrypted connections between visitors, Cloudflare, and your origin server.
  full_title: Overview · Cloudflare SSL/TLS docs
  head_html: <title>Overview · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage SSL/TLS certificates for encrypted connections between visitors, Cloudflare, and your origin server."><link rel="canonical" href="https://developers.cloudflare.com/ssl/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/index.md"><meta property="og:title" content="Overview · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage SSL/TLS certificates for encrypted connections between visitors, Cloudflare, and your origin server."><meta property="og:url" content="https://developers.cloudflare.com/ssl/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/ssl/#page","headline":"Overview \u00b7 Cloudflare SSL/TLS docs","description":"Manage SSL/TLS certificates for encrypted connections between visitors, Cloudflare, and your origin server.","url":"https://developers.cloudflare.com/ssl/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/307.md")
</div>
<div class="nb-plan">
<p>Available on all plans</p>
</div>
<p>SSL/TLS certificates encrypt traffic between visitors and your website, preventing eavesdropping and data tampering. Because Cloudflare sits between your visitors and your origin server, two certificates can be involved in a single request: an <a href="/ssl/concepts/#edge-certificate">edge certificate</a> (visitor to Cloudflare) and an <a href="/ssl/concepts/#origin-certificate">origin certificate</a> (Cloudflare to your server).</p>
<p>Cloudflare automatically issues free certificates through <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL</a> and offers additional options for custom certificate management. Refer to <a href="/ssl/get-started/">Get started</a> to set up SSL/TLS for your domain.</p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/308.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/309.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/310.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/311.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/312.md")
</div>
