---
cp9:
  canonical: https://developers.cloudflare.com/client-ip-geolocation/get-started/
  description: Set up Client IP Geolocation for your network.
  full_title: Get started · Cloudflare Client IP Geolocation docs
  head_html: <title>Get started · Cloudflare Client IP Geolocation docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Client IP Geolocation for your network."><link rel="canonical" href="https://developers.cloudflare.com/client-ip-geolocation/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/client-ip-geolocation/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Client IP Geolocation docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Client IP Geolocation for your network."><meta property="og:url" content="https://developers.cloudflare.com/client-ip-geolocation/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Client IP Geolocation"><meta name="algolia_product_filter" content="Cloudflare Client IP Geolocation"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Client IP Geolocation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/client-ip-geolocation/get-started/#page","headline":"Get started \u00b7 Cloudflare Client IP Geolocation docs","description":"Set up Client IP Geolocation for your network.","url":"https://developers.cloudflare.com/client-ip-geolocation/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /client-ip-geolocation/get-started/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1356.md")
</aside>
<p>There are several things you can do to best handle traffic from Cloudflare VPN and forward-proxy users:</p>
<ul>
<li><strong>Origin operators</strong>:
<ul>
<li>Do not block IP addresses associated with our VPN and proxy products (see the <a href="/client-ip-geolocation/about/">About section</a> for more details)</li>
<li>To get even more accurate geolocation data, ensure your origin is <a href="/client-ip-geolocation/faq/">reachable via IPv6</a></li>
</ul>
</li>
<li><strong>Geolocation data providers</strong>:
<ul>
<li>Regularly pull updated geolocation data from the <a href="https://api.cloudflare.com/local-ip-ranges.csv">Cloudflare API</a></li>
</ul>
</li>
<li><strong>Users of WARP and 1.1.1.1</strong>:
<ul>
<li>Review the <a href="/client-ip-geolocation/faq/#cloudflare-vpn-users">FAQs</a> and <a href="/client-ip-geolocation/about/">About section</a> to learn exactly how, how much, and why we share geolocation data</li>
</ul>
</li>
</ul>
