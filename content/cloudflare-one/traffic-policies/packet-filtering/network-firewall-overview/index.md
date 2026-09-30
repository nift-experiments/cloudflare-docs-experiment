---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/network-firewall-overview/
  description: Overview in Gateway.
  full_title: Overview · Cloudflare One docs
  head_html: <title>Overview · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Overview in Gateway."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/network-firewall-overview/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/network-firewall-overview/index.md"><meta property="og:title" content="Overview · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Overview in Gateway."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/network-firewall-overview/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/network-firewall-overview/#page","headline":"Overview \u00b7 Cloudflare One docs","description":"Overview in Gateway.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/network-firewall-overview/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/packet-filtering/network-firewall-overview/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/6410.md")
</div>
<div class="nb-plan">
<p>Enterprise-only</p>
</div>
<p>Unwanted network traffic — from DDoS floods to unauthorized scans — can overwhelm your infrastructure. Cloudflare Network Firewall is a <span class="nb-glossary-tooltip" title="firewall-as-a-service">firewall-as-a-service (FWaaS)</span> delivered from the Cloudflare global network, meaning Cloudflare runs the firewall for you in the cloud instead of on your own hardware. You can apply filter rules on a variety of criteria, such as protocol (for example, TCP or UDP) and <span class="nb-glossary-tooltip" title="data packet">packet</span> length, to filter unwanted traffic before it reaches your network.</p>
<p>Cloudflare Network Firewall uses Wireshark display filter syntax — a rule language originally from the popular network analysis tool <a href="https://www.wireshark.org/">Wireshark</a>, widely used in networking and the same syntax used across other Cloudflare products. With this syntax, you can craft rules to precisely allow or deny any traffic in or out of your network.</p>
<p>Cloudflare Network Firewall is available with the purchase of <a href="/magic-transit/">Magic Transit</a> or <a href="/cloudflare-wan/">Cloudflare WAN</a>.</p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/6413.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/6414.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/6415.md")
</div>
