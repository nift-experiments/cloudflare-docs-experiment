---
cp9:
  canonical: https://developers.cloudflare.com/ssl/client-certificates/revoke-client-certificate/
  description: Revoke a client certificate to block its use.
  full_title: Revoke a client certificate · Cloudflare SSL/TLS docs
  head_html: <title>Revoke a client certificate · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Revoke a client certificate to block its use."><link rel="canonical" href="https://developers.cloudflare.com/ssl/client-certificates/revoke-client-certificate/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/client-certificates/revoke-client-certificate/index.md"><meta property="og:title" content="Revoke a client certificate · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Revoke a client certificate to block its use."><meta property="og:url" content="https://developers.cloudflare.com/ssl/client-certificates/revoke-client-certificate/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/client-certificates/revoke-client-certificate/#page","headline":"Revoke a client certificate \u00b7 Cloudflare SSL/TLS docs","description":"Revoke a client certificate to block its use.","url":"https://developers.cloudflare.com/ssl/client-certificates/revoke-client-certificate/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/client-certificates/revoke-client-certificate/
  schema: 1
---
<p>You can revoke a client certificate you previously generated with the default <a href="/ssl/client-certificates/">Cloudflare-managed CA</a>.</p>
<p>It is not possible to permanently delete client certificates generated with the default Cloudflare-managed CA. Once revoked, these client certificates will still be listed on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/client-certificates"><strong>Client Certificates</strong></a> page, and can be restored at any time.</p>
<h2 id="steps">Steps</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Client Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the certificate you want to revoke.</li>
<li>Select <strong>Revoke</strong> and confirm the operation.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="effect-on-quota">Effect on quota</h3>
@markup("md", "content/.markup/bodies/14014.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/14013.md")
</aside>
