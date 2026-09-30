---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/wan-transformation/
  description: Transform WAN traffic with header and protocol modifications.
  full_title: WAN transformation · Cloudflare WAN docs
  head_html: <title>WAN transformation · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Transform WAN traffic with header and protocol modifications."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/wan-transformation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/wan-transformation/index.md"><meta property="og:title" content="WAN transformation · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Transform WAN traffic with header and protocol modifications."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/wan-transformation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/wan-transformation/#page","headline":"WAN transformation \u00b7 Cloudflare WAN docs","description":"Transform WAN traffic with header and protocol modifications.","url":"https://developers.cloudflare.com/cloudflare-wan/wan-transformation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/wan-transformation/
  schema: 1
---
<p>Traditional wide area networks (WANs) were designed for a world where applications ran in corporate data centers and employees worked from offices. These architectures rely on private circuits like Multiprotocol Label Switching (MPLS), hub-and-spoke routing through central data centers, and dedicated hardware at every branch.</p>
<p>As organizations adopt cloud services and support remote work, this model creates bottlenecks. Backhauling traffic to a central data center adds latency for cloud-bound traffic, and branch hardware requires ongoing maintenance and capital investment. WAN transformation replaces this architecture with cloud-native networking — routing traffic through a distributed global network instead of private circuits, and applying security inline rather than at a central chokepoint.</p>
<p>With Cloudflare One, your corporate WAN runs over Cloudflare's global network. You connect sites through <span class="nb-glossary-tooltip" title="anycast">anycast</span> <span class="nb-glossary-tooltip" title="IPsec tunnel">IPsec</span> or <span class="nb-glossary-tooltip" title="GRE tunnel">GRE</span> tunnels, and Cloudflare handles routing, security inspection, and traffic optimization at the nearest point of presence.</p>
<h2 id="why-transform-your-wan">Why transform your WAN</h2>
<h3 id="reduce-cost-and-rigidity">Reduce cost and rigidity</h3>
<p>MPLS circuits require multi-year contracts and take weeks or months to provision. Adding a new site means ordering a new circuit. Cloudflare One uses standard Internet circuits with anycast tunnels — you can connect a new site in minutes using any Internet connection and any device that supports IPsec or GRE.</p>
<h3 id="eliminate-internet-breakout-tradeoffs">Eliminate Internet breakout tradeoffs</h3>
<p>With traditional WANs, you have two options for Internet-bound traffic: backhaul it to a central data center for security inspection (adding latency), or break out directly at the branch (bypassing security controls). Cloudflare One eliminates this tradeoff. Traffic from every site reaches the nearest Cloudflare data center, where security policies are applied without the backhaul penalty.</p>
<h3 id="avoid-vendor-lock-in">Avoid vendor lock-in</h3>
<p>Proprietary SD-WAN appliances create dependency on a single vendor's hardware and software ecosystem. Cloudflare One uses open standards — IPsec, GRE, and BGP — and works with your existing third-party routers and firewalls. You can also use the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> for zero-touch provisioning at branch sites.</p>
<h3 id="simplify-operations">Simplify operations</h3>
<p>On-premises network and security appliances require manual firmware updates, patching, and capacity planning at every location. With Cloudflare One, networking and security services run in the cloud. Cloudflare manages updates and scaling globally, reducing the operational burden on your team.</p>
<h2 id="compare-wan-approaches">Compare WAN approaches</h2>
<table>
<thead>
<tr>
<th></th>
<th>Traditional WAN (MPLS)</th>
<th>SD-WAN</th>
<th>Cloudflare One</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Performance</strong></td>
<td>Predictable but limited to circuit capacity. High latency for cloud-bound traffic due to backhauling.</td>
<td>Improved path selection across multiple links. Still relies on branch appliances for processing.</td>
<td>Traffic routed to the nearest Cloudflare data center. Cloud-bound traffic egresses locally without backhauling.</td>
</tr>
<tr>
<td><strong>Cost model</strong></td>
<td>High fixed costs. Multi-year contracts for private circuits. Per-site hardware investment.</td>
<td>Lower circuit costs (uses Internet links). Per-site appliance licensing and hardware costs remain.</td>
<td>Internet circuit costs only. No per-site hardware required (optional). Pay-as-you-grow model.</td>
</tr>
<tr>
<td><strong>Agility</strong></td>
<td>Weeks to months to provision new circuits. Rigid topology changes.</td>
<td>Faster site deployment over Internet circuits. Still requires appliance staging and configuration.</td>
<td>Connect a new site in minutes. Tunnels auto-establish from any Internet connection.</td>
</tr>
<tr>
<td><strong>Security</strong></td>
<td>Security applied at central data center or per-site firewalls.</td>
<td>Varies by vendor. Some offer integrated security, others require separate appliances.</td>
<td>Integrated security at every data center — firewall, secure web gateway, and Zero Trust policies applied inline.</td>
</tr>
<tr>
<td><strong>Management</strong></td>
<td>Separate management for WAN circuits, routers, and security appliances.</td>
<td>Single console for WAN, but security often managed separately.</td>
<td>Single dashboard for network connectivity, routing, firewall rules, and security policies.</td>
</tr>
</tbody>
</table>
<h2 id="plan-your-migration">Plan your migration</h2>
<p>WAN transformation is not an all-or-nothing change. Most organizations follow an incremental approach, adding capabilities over time while decommissioning legacy infrastructure as each phase proves out.</p>
<h3 id="1-secure-user-access"><ol>
<li>Secure user access</li>
</ol></h3>
<p>Start by replacing VPN concentrators with Zero Trust Network Access (ZTNA). Deploy the Cloudflare One Client on user devices and use Cloudflare Access to enforce identity-based policies for application access. This step secures remote and hybrid workers without changing your existing network infrastructure.</p>
<p>For more information, refer to <a href="/cloudflare-wan/zero-trust/">Cloudflare One</a>.</p>
<h3 id="2-connect-your-networks"><ol start="2">
<li>Connect your networks</li>
</ol></h3>
<p>Set up site-to-site connectivity by establishing IPsec or GRE tunnels from your existing routers, deploying the Cloudflare One Appliance at branch locations, or using Cloudflare Network Interconnect for private connectivity. Your sites communicate through Cloudflare's network, and you manage routing through the dashboard or API.</p>
<ul>
<li><a href="/cloudflare-wan/get-started/">Get started</a> with Cloudflare WAN</li>
<li>Review <a href="/cloudflare-wan/zero-trust/connectivity-options/">connectivity options</a> to choose the right on-ramp</li>
<li>Explore all available <a href="/cloudflare-wan/on-ramps/">on-ramps</a></li>
</ul>
<h3 id="3-secure-internet-egress"><ol start="3">
<li>Secure Internet egress</li>
</ol></h3>
<p>Enable Cloudflare Gateway to apply secure web gateway (SWG) policies to Internet-bound traffic from your sites. Add Cloudflare Network Firewall rules to enforce packet-level filtering. Traffic from every site is inspected at the nearest Cloudflare data center — no backhaul required.</p>
<p>For a complete overview of which security services apply to WAN traffic, refer to <a href="/cloudflare-wan/zero-trust/security-services/">Secure WAN traffic</a>. For configuration details, refer to <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> and <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a>.</p>
<h3 id="4-reduce-infrastructure"><ol start="4">
<li>Reduce infrastructure</li>
</ol></h3>
<p>As Cloudflare handles routing and security in the cloud, you can begin decommissioning branch firewalls, VPN concentrators, and MPLS circuits. The end state is what some call &quot;coffee shop networking&quot; — every location, whether a corporate office, a home office, or a coffee shop, provides the same secure, performant experience. The network is managed centrally through Cloudflare, and local infrastructure is minimal.</p>
<p>Organizations that start with Cloudflare WAN for site-to-site connectivity and packet-level security can follow this same incremental path. Cloudflare One builds on the same network infrastructure, so you can add identity-based access controls, secure web gateway policies, and user-level security as your requirements grow — without re-architecting your deployment.</p>
<hr />
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/cloudflare-wan/get-started/">Get started</a>: Set up Cloudflare WAN with the Cloudflare One Appliance or a third-party device.</li>
<li><a href="/cloudflare-wan/zero-trust/connectivity-options/">Connectivity options</a>: Compare all Cloudflare One connectivity options and choose the right combination for your deployment.</li>
<li><a href="/cloudflare-wan/on-ramps/">On-ramps</a>: Review the full list of supported on-ramps for connecting your networks.</li>
<li><a href="/reference-architecture/architectures/sase/">SASE reference architecture</a>: Explore the architecture of Cloudflare One as a SASE platform.</li>
</ul>
