---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/setup/
  description: Learn how to set up Geo Key Manager and choose the geographical boundaries of where your private encryption keys are stored.
  full_title: Setup - Geo Key Manager · Cloudflare SSL/TLS docs
  head_html: <title>Setup - Geo Key Manager · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to set up Geo Key Manager and choose the geographical boundaries of where your private encryption keys are stored."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/setup/index.md"><meta property="og:title" content="Setup - Geo Key Manager · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to set up Geo Key Manager and choose the geographical boundaries of where your private encryption keys are stored."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Geo Key Manager"><meta name="pcx_tags" content="TLS,Compliance,Geolocation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/setup/#page","headline":"Setup - Geo Key Manager \u00b7 Cloudflare SSL/TLS docs","description":"Learn how to set up Geo Key Manager and choose the geographical boundaries of where your private encryption keys are stored.","url":"https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS","Compliance","Geolocation"]}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/geokey-manager/setup/
  schema: 1
---
<h2 id="geo-key-manager-v2">Geo Key Manager v2 <span class="nb-badge">Beta</span></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14062.md")
</aside>
<p>Geo Key Manager v2 gives customers flexibility when choosing the geographical boundaries of where their keys are stored.</p>
<p>Using the <code>policy</code> field, customers can define policies containing allow and block lists of countries or regions where the private key should be stored.</p>
<p>To use Geo Key Manager v2 with the API, generally, follow the steps to <a href="/ssl/edge-certificates/custom-certificates/uploading/#upload-a-custom-certificate">upload a custom certificate</a>.</p>
<p>When sending the <a href="/api/resources/custom_certificates/methods/create/"><code>POST</code></a> request, include the <code>policy</code> parameter to define policies containing allow and block lists of countries or regions where the private key should be stored.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14061.md")
</aside>
<h3 id="examples">Examples</h3>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/14063.md")
</div>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/14064.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14060.md")
</aside>
<h2 id="geo-key-manager-v1">Geo Key Manager v1</h2>
<p>The first version of Geo Key Manager supports 3 regions: U.S., E.U., and a set of High Security Data Centers. If you would like to restrict your private key to another country or region, <a href="https://www.cloudflare.com/lp/geo-key-manager/">apply for the closed beta</a> of the new version.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14067.md")
</div></div>
