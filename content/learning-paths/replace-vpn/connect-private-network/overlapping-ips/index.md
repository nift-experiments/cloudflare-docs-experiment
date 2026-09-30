---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/overlapping-ips/
  description: Handle overlapping IP addresses with virtual networks.
  full_title: Manage overlapping IPs · Cloudflare Learning Paths
  head_html: <title>Manage overlapping IPs · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Handle overlapping IP addresses with virtual networks."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/overlapping-ips/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/overlapping-ips/index.md"><meta property="og:title" content="Manage overlapping IPs · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Handle overlapping IP addresses with virtual networks."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/overlapping-ips/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One,Access,Cloudflare Tunnel,Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/overlapping-ips/#page","headline":"Manage overlapping IPs \u00b7 Cloudflare Learning Paths","description":"Handle overlapping IP addresses with virtual networks.","url":"https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/overlapping-ips/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/replace-vpn/connect-private-network/overlapping-ips/
  schema: 1
---
<p>Virtual networks provide routing isolation within your Cloudflare account. Each virtual network maintains its own routing table, allowing you to separate traffic between different environments, partners, or applications.</p>
<p>For example, an organization may have separate &quot;production&quot; and &quot;staging&quot; VPC networks that both use the same private IP range (such as <code>10.128.0.0/24</code>). Without virtual networks, Cloudflare cannot distinguish between <code>10.128.0.1</code> in production and <code>10.128.0.1</code> in staging. By creating two virtual networks, you can deterministically route traffic to the correct environment. Users select which virtual network they want to connect to in the Cloudflare One Client.</p>
<p>For a conceptual overview of virtual networks, including how they work across Cloudflare products, refer to <a href="/cloudflare-one/networks/virtual-networks/">Virtual networks</a>.</p>
<h2 id="example">Example</h2>
<p>This example illustrates best practices for managing overlapping subnets. For this example, assume that you are connecting two different private networks: a production VPC that uses the <code>10.0.0.0/8</code> space holistically and a staging VPC that uses the <code>10.0.1.0/24</code> space. These networks are served by Tunnel-A and Tunnel-B respectively.</p>
<p>The following table shows the default configuration without a virtual network assigned:</p>
<table>
<thead>
<tr>
<th>Routes in Tunnel-A</th>
<th>Virtual network</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10.0.0.0/8</code></td>
<td>default</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Routes in Tunnel-B</th>
<th>Virtual network</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10.0.1.0/24</code></td>
<td>default</td>
</tr>
</tbody>
</table>
<p>In the above configuration, all user traffic to <code>10.0.1.0/24</code> takes the most specific path and routes to the staging VPC (Tunnel-B). All other <code>10.0.0.0/8</code> traffic routes to the production VPC (Tunnel-A). Users would not be able to reach the <code>10.0.1.0/24</code> subnet for the network served by Tunnel-A.</p>
<p>To solve this problem, add a <code>10.0.1.0/24</code> route to Tunnel-A and assign it the <code>production</code> virtual network. Next, assign the <code>staging</code> virtual network to <code>10.0.1.0/24</code> in Tunnel-B.</p>
<table>
<thead>
<tr>
<th>Routes in Tunnel-A</th>
<th>Virtual network</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10.0.0.0/8</code></td>
<td>default</td>
</tr>
<tr>
<td><code>10.0.1.0/24</code></td>
<td>production</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Routes in Tunnel-B</th>
<th>Virtual network</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10.0.1.0/24</code></td>
<td>staging</td>
</tr>
</tbody>
</table>
<p>The user can now <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/#connect-to-a-virtual-network">toggle between the two virtual networks</a> in their Cloudflare One Client, similar to the concept of switching VPN profiles in a VPN client. When a user selects <code>production</code>, they can connect to the entire <code>10.0.0.0/8</code> range served by Tunnel-A. When they select <code>staging</code>, they can connect to all of <code>10.0.0.0/8</code> in Tunnel-A except for <code>10.0.1.0/24</code>, which will be served by Tunnel-B.</p>
<h2 id="set-up-virtual-networks">Set up virtual networks</h2>
<p>For setup instructions, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/#create-a-virtual-network">Create a virtual network</a>.</p>
