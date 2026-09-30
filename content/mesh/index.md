---
cp9:
  canonical: https://developers.cloudflare.com/mesh/
  description: Connect services and devices with post-quantum encrypted private networking through Cloudflare.
  full_title: Cloudflare Mesh - Private networking · Cloudflare Docs
  head_html: <title>Cloudflare Mesh - Private networking · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect services and devices with post-quantum encrypted private networking through Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/mesh/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/mesh/index.md"><meta property="og:title" content="Cloudflare Mesh - Private networking · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect services and devices with post-quantum encrypted private networking through Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/mesh/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Mesh"><meta name="algolia_product_filter" content="Cloudflare Mesh"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare Mesh"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/mesh/#page","headline":"Cloudflare Mesh - Private networking \u00b7 Cloudflare Docs","description":"Connect services and devices with post-quantum encrypted private networking through Cloudflare.","url":"https://developers.cloudflare.com/mesh/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /mesh/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/749.md")
</div>
<p>Cloudflare Mesh gives every enrolled server, laptop, and phone a private Mesh IP. Participants can communicate by IP over TCP, UDP, or ICMP, including device-to-device connections that do not require customer-managed networking infrastructure.</p>
<p>Mesh nodes run the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> in headless mode on Linux. They can also advertise routes to make private subnets and hostnames reachable from other Mesh participants.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/mesh-network-map.gif" alt="The Mesh network map in the Cloudflare dashboard showing nodes and devices connected through Cloudflare" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/748.md")
</aside>
<p><span id="how-it-works"></span>
<span id="protocol-requirement"></span>
<span id="mesh-ips"></span></p>
<p>For details about how Mesh works, protocol requirements, and Mesh IP assignment, refer to <a href="/mesh/concepts/">Concepts</a>.</p>
<h2 id="use-cases">Use cases</h2>
<ul>
<li>Connect enrolled devices to each other by private IP.</li>
<li>Provide bidirectional connectivity between servers, cloud networks, and sites.</li>
<li>Route traffic to devices that cannot run the Cloudflare One Client.</li>
<li>Preserve long-lived TCP connections for databases, replication, ERP systems, and remote administration.</li>
</ul>
<h2 id="get-started">Get started</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/754.md")
</div>
<p><span id="mesh-vs-tunnel"></span></p>
<h2 id="mesh-vs-cloudflare-tunnel">Mesh vs. Cloudflare Tunnel</h2>
<p>Use Mesh when participants need bidirectional private IP connectivity or when a workload requires stable, long-lived connections. Use <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> when you want to publish specific applications, hostnames, or IP routes through an outbound-only connector.</p>
<p>For a detailed comparison, refer to <a href="/mesh/concepts/#mesh-vs-tunnel">How Cloudflare Mesh works</a>.</p>
