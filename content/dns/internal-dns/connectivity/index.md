---
cp9:
  canonical: https://developers.cloudflare.com/dns/internal-dns/connectivity/
  description: Connect to the Internal DNS Gateway resolver.
  full_title: Connect to Gateway resolver · Cloudflare DNS docs
  head_html: <title>Connect to Gateway resolver · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect to the Internal DNS Gateway resolver."><link rel="canonical" href="https://developers.cloudflare.com/dns/internal-dns/connectivity/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/internal-dns/connectivity/index.md"><meta property="og:title" content="Connect to Gateway resolver · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect to the Internal DNS Gateway resolver."><meta property="og:url" content="https://developers.cloudflare.com/dns/internal-dns/connectivity/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DNS"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/internal-dns/connectivity/#page","headline":"Connect to Gateway resolver \u00b7 Cloudflare DNS docs","description":"Connect to the Internal DNS Gateway resolver.","url":"https://developers.cloudflare.com/dns/internal-dns/connectivity/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /dns/internal-dns/connectivity/
  schema: 1
---
<p>To connect to Cloudflare Gateway resolver - which is <a href="/dns/internal-dns/#architecture-overview">required to reach private resources in Internal DNS</a> - you can use the following options:</p>
<ul>
<li>DNS endpoints supported with <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations</a>
<ul>
<li>DNS over UDP/TCP port 53 (IPv4 or IPv6)</li>
<li>DNS over TLS</li>
<li>DNS over HTTPS</li>
</ul>
</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">Proxy Auto-Configuration (PAC) files</a></li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">WARP device client</a></li>
<li><a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#filter-dns-queries">Clientless browser isolation</a></li>
<li><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Cloudflare WAN</a></li>
</ul>
