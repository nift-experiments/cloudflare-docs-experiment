---
cp9:
  canonical: https://developers.cloudflare.com/network-interconnect/changelog/
  description: Review recent changes to Cloudflare Network Interconnect.
  full_title: Changelog · Cloudflare Network Interconnect docs
  head_html: <title>Changelog · Cloudflare Network Interconnect docs</title><meta name="generator" content="Nift"><meta name="description" content="Review recent changes to Cloudflare Network Interconnect."><link rel="canonical" href="https://developers.cloudflare.com/network-interconnect/changelog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-interconnect/changelog/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/network-interconnect/changelog/index.xml"><meta property="og:title" content="Changelog · Cloudflare Network Interconnect docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review recent changes to Cloudflare Network Interconnect."><meta property="og:url" content="https://developers.cloudflare.com/network-interconnect/changelog/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="Network Interconnect"><meta name="algolia_product_filter" content="Network Interconnect"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="Network Interconnect"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/network-interconnect/changelog/#page","headline":"Changelog \u00b7 Cloudflare Network Interconnect docs","description":"Review recent changes to Cloudflare Network Interconnect.","url":"https://developers.cloudflare.com/network-interconnect/changelog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network-interconnect/changelog/
  schema: 1
---
<h2 id="2026-03-24">2026-03-24</h2>

<strong>Interconnects moved to Connectors</strong>

<p>The top-level <strong>Interconnects</strong> page in the Cloudflare dashboard has been removed. Interconnects are now located under <strong>Connectors</strong> &gt; <strong>Interconnects</strong>.</p>
<p>Your existing configurations and functionality remain the same.</p>


<h2 id="2025-06-20">2025-06-20</h2>

<strong>CNI maintenance alerts</strong>

<p>Customers using Cloudflare Network Interconnect with the v1 dataplane can now subscribe to maintenance alert emails. These alerts notify you of planned maintenance windows that may affect your CNI circuits.</p>
<p>For more information, refer to <a href="/network-interconnect/monitoring-and-alerts/">Monitoring and alerts</a>.</p>


<h2 id="2024-12-17">2024-12-17</h2>

<strong>Establish BGP peering over Direct CNI circuits</strong>

<p>Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using a Direct CNI on-ramp.</p>
<p>Using BGP peering allows customers to:</p>
<ul>
<li>Automate the process of adding or removing networks and subnets.</li>
<li>Take advantage of failure detection and session recovery features.</li>
</ul>
<p>With this functionality, customers can:</p>
<ul>
<li>Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via CNI.</li>
<li>Secure the session by MD5 authentication to prevent misconfigurations.</li>
<li>Exchange routes dynamically between their devices and their Magic routing table.</li>
</ul>
<p>Refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes">Magic WAN BGP peering</a> or <a href="/magic-transit/how-to/configure-routes/#configure-bgp-routes">Magic Transit BGP peering</a> to learn more about this feature and how to set it up.</p>


<h2 id="2024-10-01">2024-10-01</h2>
<p><strong>Early access testing for BGP on Direct CNI circuits</strong></p>
<p>Customers can exchange routes dynamically with their Magic virtual network overlay via Direct CNI or Cloud CNI based connectivity.</p>
<h2 id="2024-09-02">2024-09-02</h2>
<p><strong>Interconnect portal displays all available locations in a list</strong></p>
<p>Customers can now see all available Direct CNI locations when searching for a Cloudflare site in the Interconnects interface.</p>


