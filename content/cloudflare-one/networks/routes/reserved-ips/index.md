---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/
  description: Reference information for Reserved IP addresses in Zero Trust networking.
  full_title: Reserved IP addresses · Cloudflare One docs
  head_html: <title>Reserved IP addresses · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Reserved IP addresses in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/index.md"><meta property="og:title" content="Reserved IP addresses · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Reserved IP addresses in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="IPv4,IPv6"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/#page","headline":"Reserved IP addresses \u00b7 Cloudflare One docs","description":"Reference information for Reserved IP addresses in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["IPv4","IPv6"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/routes/reserved-ips/
  schema: 1
---
<p>Cloudflare reserves several IPv4 and IPv6 ranges for internal routing and service functionality. Most of these ranges are drawn from the CGNAT address space (<code>100.64.0.0/10</code>). <a href="#gateway-initial-resolved-ips">Gateway initial resolved IPs</a> are the exception, using a public Cloudflare-owned range by default. To avoid routing conflicts, your Cloudflare Tunnel, Cloudflare Mesh, or WAN routes should not include subsets of these reserved ranges. Broader routes that contain a reserved range, such as <code>0.0.0.0/0</code>, are unaffected because longest-prefix match ensures the reserved ranges still take priority.</p>
<p>When planning your private network addressing and configuring <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel</a> entries, use the tables below to identify which IP ranges Cloudflare has reserved and whether they can be reconfigured.</p>
<h2 id="ipv4-ranges">IPv4 ranges</h2>
<table>
<thead>
<tr>
<th>Name</th>
<th>Default CIDR</th>
<th>Configurable</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#cloudflare-source-ips">Cloudflare source IPs</a></td>
<td><code>100.64.0.0/12</code></td>
<td>Yes</td>
</tr>
<tr>
<td><a href="#gateway-initial-resolved-ips">Gateway initial resolved IPs</a></td>
<td><code>172.64.128.0/20</code></td>
<td>Yes</td>
</tr>
<tr>
<td><a href="#device-ips">Device IPs</a></td>
<td><code>100.96.0.0/12</code></td>
<td>Yes</td>
</tr>
<tr>
<td><a href="#private-load-balancer-ips">Private Load Balancer IPs</a></td>
<td><code>100.112.0.0/16</code></td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>Unlike the other IPv4 ranges, Gateway initial resolved IPs are drawn from public Cloudflare address space rather than CGNAT (<code>100.64.0.0/10</code>) by default. If your account was created before this default changed, or if you configured a custom range, it may still fall within CGNAT space — refer to <a href="#gateway-initial-resolved-ips">Gateway initial resolved IPs</a>.</p>
<h2 id="ipv6-ranges">IPv6 ranges</h2>
<table>
<thead>
<tr>
<th>Name</th>
<th>Default CIDR</th>
<th>Configurable</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#device-ips">Device IPs</a></td>
<td><code>2606:4700:0cf1:1000::/64</code></td>
<td>No</td>
</tr>
<tr>
<td><a href="#gateway-initial-resolved-ips">Gateway initial resolved IPs</a></td>
<td><code>2606:4700:0cf1:4000::/64</code></td>
<td>No</td>
</tr>
<tr>
<td><a href="#cloudflare-source-ips">Cloudflare source IPs</a></td>
<td><code>2606:4700:0cf1:5000::/64</code></td>
<td>No</td>
</tr>
</tbody>
</table>
<h2 id="cloudflare-source-ips">Cloudflare source IPs</h2>
<p>Cloudflare source IPs are the source addresses used when a Cloudflare service sends traffic to your private networks. This range applies to customers using <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing (beta)</a>. Examples of requests that are sourced from this range include:</p>
<ul>
<li><a href="/load-balancing/monitors/">Load Balancing</a> — health check requests to private endpoints</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/">Gateway DNS resolver</a> — DNS resolution for private hostnames</li>
<li><a href="/workers/">Cloudflare Workers</a> — requests from Workers to private origins</li>
</ul>
<p>The default IPv4 range is <code>100.64.0.0/12</code>. You can change this to a different <code>/12</code> CIDR to avoid conflicts with your existing IP address management plan. For more information on affected services and configuration instructions, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">Configure Cloudflare source IPs</a>.</p>
<h2 id="gateway-initial-resolved-ips">Gateway initial resolved IPs</h2>
<p>Gateway initial resolved IPs (also called token IPs) are ephemeral addresses used to map hostnames to destination IPs at the network layer, where hostname information is not usually available.</p>
<p>The following features use this range:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">Private hostname routing</a> — routes traffic to private applications behind Cloudflare Tunnel using their hostnames.</li>
<li><a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">Public hostname routing</a> — egresses traffic through Cloudflare Tunnel to anchor source IPs for public destinations.</li>
<li><a href="/cloudflare-one/traffic-policies/egress-policies/host-selectors/">Egress policy host selectors</a> — evaluates Gateway egress policies using hostname-based selectors.</li>
<li><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Access private applications</a> — manage access to private applications using their private hostnames.</li>
</ul>
<p>Cloudflare assigns initial resolved IPs from the <code>172.64.128.0/20</code> (IPv4) or <code>2606:4700:0cf1:4000::/64</code> (IPv6) range by default. Unlike earlier CGNAT-based defaults, the IPv4 range is public Cloudflare address space, so it is not affected by <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/#google-chrome-restricts-access-to-private-hostnames">Google Chrome's Local Network Access restrictions</a>.</p>
<p>You can configure a custom IPv4 range if the default conflicts with your existing network or private routes. The IPv6 range is not configurable. For instructions, refer to <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">Configure initial resolved IPs</a>.</p>
<h2 id="device-ips">Device IPs</h2>
<p>Device IPs (also called Mesh IPs in <a href="/mesh/">Cloudflare Mesh</a>) are virtual addresses assigned to each Cloudflare One Client registration and each mesh node. These IPs identify and route traffic to specific devices for the following features:</p>
<ul>
<li><a href="/mesh/">Cloudflare Mesh</a> — mesh nodes and client devices communicate using their Mesh IPs for device-to-device, site-to-site, and mesh connectivity.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/">Cloudflare WAN</a> — on-ramps traffic from WAN tunnels to Cloudflare One Client devices.</li>
</ul>
<p>The default IPv4 range is <code>100.96.0.0/12</code>. If this range conflicts with services on your private network, you can configure custom IPv4 subnets drawn from RFC 1918 or CGNAT address space. If your account uses <a href="/cloudflare-wan/">Cloudflare WAN</a>, custom subnets require <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing (beta)</a>. For configuration instructions, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-ips/">Device IPs</a>.</p>
<h2 id="private-load-balancer-ips">Private Load Balancer IPs</h2>
<p>Private Load Balancer IPs are virtual addresses allocated to <a href="/load-balancing/private-network/">Private Network Load Balancers</a>. Each private load balancer receives a <code>/32</code> address from the <code>100.112.0.0/16</code> range by default, which serves as the load balancer's virtual IP for traffic distribution to private endpoints. Alternatively, you can configure a custom <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918</a> <code>/32</code> address for each load balancer.</p>
<h2 id="split-tunnel-configuration">Split Tunnel configuration</h2>
<p>For deployments that use the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>, ensure that the <a href="#ipv4-ranges">reserved IP ranges</a> required by your deployment route through <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">WARP Split Tunnels</a> to Cloudflare. Configuration depends on whether your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#change-split-tunnels-mode">Split Tunnels mode</a> is set to <strong>Exclude IPs and domains</strong> or <strong>Include IPs and domains</strong>.</p>
<h3 id="exclude-mode-default">Exclude mode (default)</h3>
<p>In <strong>Exclude IPs and domains</strong> mode, default device profiles exclude the CGNAT range (<code>100.64.0.0/10</code>) from Cloudflare. To route a reserved range within CGNAT space through Cloudflare, delete or narrow the CGNAT exclusion. The Mesh setup wizard does this automatically for the device IP range used by Mesh.</p>
<p><a href="#gateway-initial-resolved-ips">Gateway initial resolved IPs</a> are the exception: the default range (<code>172.64.128.0/20</code>) is public Cloudflare address space, not CGNAT, so it is <strong>not</strong> excluded by default in Exclude mode. The Cloudflare One Client also automatically removes this range, along with the entire <code>2606:4700:0cf1::/48</code> IPv6 range (which also covers <a href="#device-ips">device IPs</a> and <a href="#cloudflare-source-ips">Cloudflare source IPs</a> on IPv6), from any exclusions you configure — refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges">Automatically managed ranges</a>. No Split Tunnel changes are required for these ranges. This only applies to the default IPv4 range: if you configured a custom initial resolved IP range within CGNAT space, treat it the same as the other CGNAT-based ranges below.</p>
<p>Cloudflare recommends excluding CGNAT IPs that are not used for Cloudflare One services. This reduces the risk of conflicts with private network configurations that use CGNAT address space.</p>
<p>Use the following calculator to determine which ranges you can exclude based on the Cloudflare One features you use. For example, if your deployment requires <a href="#cloudflare-source-ips">Cloudflare source IPs</a> (<code>100.64.0.0/12</code>) and <a href="#device-ips">device IPs</a> (<code>100.96.0.0/12</code>), exclude <code>100.80.0.0/12</code> and <code>100.112.0.0/12</code>.</p>
<div class="nb-interactive-component" data-cf-component="SubtractIPCalculator"></div>
<h3 id="include-mode">Include mode</h3>
<p>In <strong>Include IPs and domains</strong> mode, the Cloudflare One Client sends only traffic for the included routes to Cloudflare. You must explicitly add the reserved IP ranges that your deployment depends on, except the default <a href="#gateway-initial-resolved-ips">Gateway initial resolved IP range</a> (<code>172.64.128.0/20</code>) and the entire <code>2606:4700:0cf1::/48</code> IPv6 range (which also covers <a href="#device-ips">device IPs</a> and <a href="#cloudflare-source-ips">Cloudflare source IPs</a> on IPv6) — the Cloudflare One Client automatically includes these. Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges">Automatically managed ranges</a> for details. If you use <a href="#gateway-initial-resolved-ips">hostname routing or egress policy host selectors</a> with a custom IPv4 initial resolved IP range, add that custom range to your Split Tunnels include list.</p>
