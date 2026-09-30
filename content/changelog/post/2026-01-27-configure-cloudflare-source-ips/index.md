---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/
  description: New updates and improvements at Cloudflare.
  full_title: Configure Cloudflare source IPs (beta) · Changelog
  head_html: <title>Configure Cloudflare source IPs (beta) · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Configure Cloudflare source IPs (beta) · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/#page","headline":"Configure Cloudflare source IPs (beta) \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-01-27-configure-cloudflare-source-ips/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 27, 2026</time><h2 id="post-title">Configure Cloudflare source IPs (beta)</h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>Cloudflare source IPs are the IP addresses used by Cloudflare services (such as Load Balancing, Gateway, and Browser Isolation) when sending traffic to your private networks.</p>
<p>For customers using legacy mode routing, traffic to private networks is sourced from public Cloudflare IPs, which may cause IP conflicts. For customers using Unified Routing mode (beta), traffic to private networks is sourced from dedicated, non-Internet-routable private IPv4 range to ensure:</p>
<ul>
<li>Symmetric routing over private network connections</li>
<li>Proper firewall state preservation</li>
<li>Private traffic stays on secure paths</li>
</ul>
<p>Key details:</p>
<ul>
<li><strong>IPv4</strong>: Sourced from <code>100.64.0.0/12</code> by default, configurable to any <code>/12</code> CIDR</li>
<li><strong>IPv6</strong>: Sourced from <code>2606:4700:cf1:5000::/64</code> (not configurable)</li>
<li><strong>Affected connectors</strong>: GRE, IPsec, CNI, WARP Connector, and WARP Client (Cloudflare Tunnel is not affected)</li>
</ul>
<p>Configuring Cloudflare source IPs requires Unified Routing (beta) and the <code>Cloudflare One Networks Write</code> permission.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">Configure Cloudflare source IPs</a>.</p>
</div></article></div>
