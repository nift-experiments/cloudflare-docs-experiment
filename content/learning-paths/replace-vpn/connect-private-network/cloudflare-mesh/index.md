---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflare-mesh/
  description: Connect your network using Cloudflare Mesh.
  full_title: Connect with Cloudflare Mesh · Cloudflare Learning Paths
  head_html: <title>Connect with Cloudflare Mesh · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Connect your network using Cloudflare Mesh."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflare-mesh/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflare-mesh/index.md"><meta property="og:title" content="Connect with Cloudflare Mesh · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect your network using Cloudflare Mesh."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflare-mesh/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One,Access,Cloudflare Tunnel,Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflare-mesh/#page","headline":"Connect with Cloudflare Mesh \u00b7 Cloudflare Learning Paths","description":"Connect your network using Cloudflare Mesh.","url":"https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflare-mesh/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/replace-vpn/connect-private-network/cloudflare-mesh/
  schema: 1
---
<p><a href="/mesh/">Cloudflare Mesh</a> (formerly WARP Connector) connects your private networks to Cloudflare using the Cloudflare One Client (<code>warp-cli</code>) running in headless mode on a Linux server. Every enrolled device and node receives a private Mesh IP and can communicate with any other participant over TCP, UDP, or ICMP.</p>
<p>Mesh supports bidirectional traffic — devices can reach servers, servers can reach devices, and networks can reach other networks. This makes it the recommended approach for replacing a VPN, as it covers both user-to-network and network-to-network connectivity.</p>
<h2 id="set-up-cloudflare-mesh">Set up Cloudflare Mesh</h2>
<p>To connect your private network using Cloudflare Mesh, refer to <a href="/mesh/get-started/">Get started with Cloudflare Mesh</a>.</p>
<p>The setup wizard in the dashboard configures enrollment, device profiles, and connectivity settings automatically. Once a node is online, add <a href="/mesh/features/routes/">CIDR routes</a> to make the subnet behind it reachable from any enrolled device.</p>
<h2 id="when-to-use-mesh">When to use Mesh</h2>
<ul>
<li>Replacing a VPN for remote access to private networks</li>
<li>Bidirectional connectivity (VoIP, SIP, Active Directory, SCCM, DevOps pipelines)</li>
<li>Long-lived TCP connections sensitive to interruptions (SAP, database replication, ERP systems, RDP sessions)</li>
<li>Site-to-site networking between offices, data centers, or cloud VPCs</li>
<li>Client-to-client connectivity (two laptops reaching each other by private IP)</li>
<li>Any L3/L4 workload where source IP preservation matters</li>
</ul>
<h2 id="best-practices">Best practices</h2>
<ul>
<li>Enable <a href="/mesh/features/high-availability/">high availability</a> for production nodes with CIDR routes.</li>
<li>Use <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a> to control which users and devices can reach specific resources.</li>
<li>Refer to <a href="/mesh/best-practices/">Tips and best practices</a> for cloud VPC configuration and running alongside Cloudflare Tunnel.</li>
</ul>
