---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/
  description: New updates and improvements at Cloudflare.
  full_title: Introducing Cloudflare Mesh · Changelog
  head_html: <title>Introducing Cloudflare Mesh · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Introducing Cloudflare Mesh · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/#page","headline":"Introducing Cloudflare Mesh \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-14-cloudflare-mesh/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 14, 2026</time><h2 id="post-title">Introducing Cloudflare Mesh</h2>
<div class="changelog-badges"><span>cloudflare-one</span></div><div class="changelog-body"><p><a href="/mesh/">Cloudflare Mesh</a> is now available (<a href="https://blog.cloudflare.com/mesh/">blog post</a>). Mesh connects your services and devices with post-quantum encrypted networking, allowing you to route traffic privately between servers, laptops, and phones over TCP, UDP, and ICMP.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/mesh-network-map.gif" alt="Cloudflare Mesh network map showing nodes and devices connected through Cloudflare" /></p>
<h4 id="what-cloudflare-mesh-does">What Cloudflare Mesh does</h4>
<ul>
<li>Assigns a private <a href="/mesh/concepts/#mesh-ips">Mesh IP</a> to every enrolled device and node.</li>
<li>Enables any participant to reach any other participant by IP — including client-to-client, without deploying any infrastructure.</li>
<li>Supports <a href="/mesh/features/routes/">CIDR routes</a> for subnet routing through Mesh nodes.</li>
<li>Supports <a href="/mesh/features/high-availability/">high availability</a> with active-passive replicas for nodes with routes.</li>
<li>All traffic flows through Cloudflare, so <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>, <a href="/cloudflare-one/reusable-components/posture-checks/">device posture checks</a>, and access rules apply to every connection.</li>
</ul>
<h4 id="what-changed">What changed</h4>
<ul>
<li><strong>WARP Connector</strong> is now <strong>Cloudflare Mesh</strong>. Existing WARP Connectors are now called mesh nodes. All existing deployments continue to work — no migration required.</li>
<li><strong>Peer-to-peer connectivity</strong> is now called <strong>Mesh connectivity</strong> and is part of the Cloudflare Mesh documentation.</li>
<li><strong>Mesh node limit</strong> increased from 10 to <strong>50 per account</strong>.</li>
<li>New <a href="https://dash.cloudflare.com/?to=/:account/mesh">dashboard experience</a> at <strong>Networking</strong> &gt; <strong>Mesh</strong> with an interactive network map, node management, route configuration, diagnostics, and a setup wizard.</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>Refer to the <a href="/mesh/">Cloudflare Mesh documentation</a> to set up your first Mesh network.</p>
</div></article></div>
