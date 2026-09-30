---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/
  description: New updates and improvements at Cloudflare.
  full_title: Establish BGP peering over Direct CNI circuits · Changelog
  head_html: <title>Establish BGP peering over Direct CNI circuits · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Establish BGP peering over Direct CNI circuits · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/#page","headline":"Establish BGP peering over Direct CNI circuits \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2024-12-17-bgp-support-cni/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 17, 2024</time><h2 id="post-title">Establish BGP peering over Direct CNI circuits</h2>
<div class="changelog-badges"><span>magic-transit</span><span>cloudflare-wan</span><span>network-interconnect</span></div><div class="changelog-body"><p>Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using a Direct CNI on-ramp.</p>
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
</div></article></div>
