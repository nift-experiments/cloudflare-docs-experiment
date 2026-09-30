---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/network-interconnect/
  description: '2026-03-24'
  full_title: network-interconnect changelog | Cloudflare Docs
  head_html: <title>network-interconnect changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-03-24"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/network-interconnect/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="network-interconnect changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-03-24"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/network-interconnect/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/network-interconnect/#page","headline":"network-interconnect changelog | Cloudflare Docs","description":"2026-03-24","url":"https://developers.cloudflare.com/changelog/product/network-interconnect/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/network-interconnect/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="interconnects-moved-to-connectors"><a href="/changelog/post/2026-03-24-interconnects-navigation-update/">Interconnects moved to Connectors</a></h2>
<p><em>2026-03-24</em></p>
<p>The top-level <strong>Interconnects</strong> page in the Cloudflare dashboard has been removed. Interconnects are now located under <strong>Connectors</strong> &gt; <strong>Interconnects</strong>.</p>
<p>Your existing configurations and functionality remain the same.</p>


<h2 id="cni-maintenance-alerts"><a href="/changelog/post/2025-06-20-cni-maintenance-alerts/">CNI maintenance alerts</a></h2>
<p><em>2025-06-20</em></p>
<p>Customers using Cloudflare Network Interconnect with the v1 dataplane can now subscribe to maintenance alert emails. These alerts notify you of planned maintenance windows that may affect your CNI circuits.</p>
<p>For more information, refer to <a href="/network-interconnect/monitoring-and-alerts/">Monitoring and alerts</a>.</p>


<h2 id="establish-bgp-peering-over-direct-cni-circuits"><a href="/changelog/post/2024-12-17-bgp-support-cni/">Establish BGP peering over Direct CNI circuits</a></h2>
<p><em>2024-12-17</em></p>
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


<h2 id="explore-product-updates-for-cloudflare-one"><a href="/changelog/post/2024-06-16-cloudflare-one/">Explore product updates for Cloudflare One</a></h2>
<p><em>2024-06-16</em></p>
<p>Welcome to your new home for product updates on <a href="/cloudflare-one/">Cloudflare One</a>.</p>
<p>Our <a href="/changelog/">new changelog</a> lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.</p>
<p>If you are looking for older product updates, refer to the following locations.</p>
<details class="nb-details" open><summary>Older product updates</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17707.md")</div></details>



