---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/reference/
  description: Reference information for Appliance configuration.
  full_title: Reference · Cloudflare WAN docs
  head_html: <title>Reference · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Appliance configuration."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/reference/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/reference/index.md"><meta property="og:title" content="Reference · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Appliance configuration."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/reference/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/reference/#page","headline":"Reference \u00b7 Cloudflare WAN docs","description":"Reference information for Appliance configuration.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/reference/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/appliance/reference/
  schema: 1
---
<p>The Cloudflare One Appliance (formerly Magic WAN Connector) software is certified for use on the <a href="https://www.dell.com/support/home/en-us/product-support/product/dell-emc-networking-vep1445-vep1485/docs">Dell Networking Virtual Edge Platform</a>. It can be purchased with software pre-installed through our partner network for plug-and-play connectivity to Cloudflare One.</p>
<h2 id="security-and-other-information">Security and other information</h2>
<ul>
<li>Cloudflare ensures the Cloudflare One Appliance device is secure and is not altered via TPM/Secure boot (does not apply to Virtual Appliance).</li>
<li>Connectivity to the Cloudflare global network is secure and all traffic is encrypted through <span class="nb-glossary-tooltip" title="IPsec tunnel">IPsec</span> tunneling. The Cloudflare One Appliance uses ESP-in-UDP with GCM-AES-256 encryption. Cloudflare uses a non-IKE keying protocol built into our control plane, secured with TLS, that establishes the keys used to encrypt dataplane traffic in the IPsec ESP protocol. From Appliance version 2026.2.0, the control plane provides post-quantum protection for traffic with hybrid ML-KEM (X25519MLKEM768) over TLS 1.3 to establish the dataplane keys used in IPsec ESP.</li>
<li>The Cloudflare One Appliance does not support fail open.</li>
<li>Customers have the ability to layer on additional security features/policies that are enforced at the Cloudflare network.</li>
</ul>
<hr />
<h2 id="icmp-traffic">ICMP traffic</h2>
<p><span class="nb-glossary-tooltip" title="ICMP">ICMP traffic</span> is routed through the Internet and bypasses <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>. This enables you to ping resources on the Internet from the Cloudflare One Appliance directly, which can be useful for debugging.</p>
<hr />
<h2 id="vlan-id">VLAN ID</h2>
<p>This feature allows you to have multiple <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-lan/">virtual LANs</a> (VLANs) configured over the same physical port on your Cloudflare One Appliance. VLAN tagging adds an extra header to <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-packet/">packets</a> in order to identify which VLAN the packet belongs to and to route it appropriately. This effectively allows you to run multiple networks over the same physical port.</p>
<p>A non-zero value set up for the VLAN ID field in your WAN/LAN is used to handle VLAN-tagged traffic. Cloudflare uses the VLAN ID to handle traffic coming into your Cloudflare One Appliance device, and applies a VLAN tag with the configured VLAN ID for traffic going out of your Cloudflare One Appliance through WAN/LAN.</p>
<p>You can setup VLAN IDs both for WAN and LAN. For instructions on setting up VLAN IDs, refer to <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/">Configure hardware Appliance</a> or <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure Virtual Appliance</a>.</p>
<h2 id="high-availability-configurations">High availability configurations</h2>
<h3 id="terminology">Terminology</h3>
<ul>
<li><strong>Primary/Secondary</strong>: Used to identify the two nodes which are part of a high availability (HA) configuration pair of Cloudflare One Appliances. This identity allows the node to identify which configuration is attributed to it — for example, specifying a primary and secondary IP in a LAN configuration. This identity is configured by the user on the Cloudflare dashboard.</li>
<li><strong>Active/Standby</strong>: These are states that the two nodes in a HA pair will dynamically assume based on an election process. Only one node at any time is expected to be active.</li>
</ul>
<h3 id="high-availability">High availability</h3>
<p>A site set up in high availability (HA) mode has two Cloudflare One Appliances with the same configuration but replicated in two nodes. In case of failure of one Cloudflare One Appliance, the other Cloudflare One Appliance becomes the active node, taking over configuration of the LAN gateway IP and allowing traffic to continue without disruption.</p>
<h3 id="active-standby-election">Active/Standby Election</h3>
<p>During the LAN configuration, one of the LAN links is configured as a HA link, which is used to exchange heartbeats, resulting in the active / standby election of nodes.</p>
<p>The state election uses a <code>PRIORITY</code> parameter where the node with the higher priority becomes active and the other assumes the standby state. If the priority is the same, the state machine automatically picks one of the nodes as active.</p>
<p>The HA pair is configured in non-preemptive mode, meaning that once a node becomes active, it will remain active unless its priority drops below that of the other node.</p>
<h3 id="configuration">Configuration</h3>
<p>The two Cloudflare One Appliances of a high availability (HA) pair are part of a single site. You designate the Cloudflare One Appliance <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#create-a-high-availability-configuration">as primary and secondary</a> in the Cloudflare dashboard.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6944.md")
</aside>
<h3 id="failure-detection-and-failover">Failure detection and failover</h3>
<p>The Cloudflare One Appliance's health can be in one of three states:</p>
<ul>
<li><strong>Good</strong> : All health parameters are good</li>
<li><strong>Degraded</strong> : One of the following is true:
<ul>
<li>Health of at least one configured tunnel is <code>DOWN</code></li>
<li>At least one of the LAN links is disconnected (physically unplugged)</li>
</ul>
</li>
<li><strong>Down</strong> : If one of the following is true:
<ul>
<li>Health of all tunnels is <code>DOWN</code></li>
<li>All LAN interfaces are disconnected</li>
<li>Cloudflare One Appliance's software is not healthy</li>
</ul>
</li>
</ul>
<p>A failover happens when the active node's health declines to a level lower than that of the standby node. For example, from <code>GOOD</code> to <code>DEGRADED</code>, or from <code>DEGRADED</code> to <code>DOWN</code>. In the case of a failover where one Cloudflare One Appliance is acting as a DHCP server, DHCP leases will be synchronized.</p>
<p>When a failover occurs, traffic is moved to the new active node. It could take up to 30 seconds for traffic to be fully restored over the new active node.</p>
<h2 id="wan-settings">WAN settings</h2>
<p>This is where you add and configure your WAN connections. Each configured WAN will create one IPsec tunnel, unless you have more than one anycast IP configured in your account.</p>
<p>When you have more than one anycast IP configured in your account (set up during your Cloudflare WAN (formerly Magic WAN) onboarding), Cloudflare One Appliance will automatically create at most two tunnels per WAN port. This improves reliability and performance, and requires no additional configuration on your part.</p>
<p>When you have multiple WANs you can attribute different priorities to each one. Lower values mean a higher priority. This translates in Cloudflare One Appliance routing traffic through the higher priority WANs or, more precisely, over the IPsec tunnels established over that interface. On the other hand, if you configure multiple WANs of equal priority, traffic will be distributed over those links through <a href="/cloudflare-wan/reference/traffic-steering/#equal-cost-multi-path-routing">Equal-Cost Multi-Path (ECMP routing)</a>.</p>
<p>Creating several WAN connections also means Cloudflare One Appliance can failover between circuits according to their health.</p>
<h3 id="high-capacity-use-cases">High-capacity use cases</h3>
<p>For high-capacity use cases, multiple tunnels can be established with equal priority. Outgoing traffic is then distributed across all available connections using an <a href="/cloudflare-wan/reference/traffic-steering/#equal-cost-multi-path-routing">ECMP routing</a> algorithm, which balances the load base.</p>
<h3 id="configure-multiple-tunnels-in-the-same-wan-profile">Configure multiple tunnels in the same WAN profile</h3>
<p>If you do not have more than one anycast IP configured in your account, and you need to configure multiple tunnels for the same WAN profile, <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#create-a-wan">set up multiple WAN connections</a>. Each WAN is assigned one IPsec tunnel.</p>
<h3 id="wan-settings-1">WAN settings</h3>
<ul>
<li><strong>Interface number:</strong> When using the hardware version of Cloudflare One Appliance, this refers to the Ethernet port that you are using for your WAN. If you need a throughput higher than 1 Gbps, you can use one of the SFP+ ports. For details on supported hardware, refer to <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/sfp-port-information/">SFP+ port information</a>. <br />  If you are using Virtual Appliance, this needs to correspond to the virtual network interface on the Virtual Appliance instance you have set up in your virtual machine.</li>
<li><strong>VLAN ID</strong>: Allows you to have multiple virtual WANs configured over the same port on your Cloudflare One Appliance. Refer to <a href="#vlan-id">VLAN ID</a> for more information.</li>
<li><strong>Priority</strong>: Assigns a priority to the WAN interface. Lower numbers have higher priority. For details on how Cloudflare calculates priorities, refer to <a href="/cloudflare-wan/reference/traffic-steering/">Traffic steering</a>.</li>
<li><strong>Health check rate:</strong> Configures the health check frequency for your WAN. Options are low, mid, and high. For details, refer to <a href="/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency/">Update tunnel health checks frequency</a>.</li>
<li><strong>Addressing:</strong> Configures the Cloudflare One Appliance to work in a DHCP or static IP environment.</li>
</ul>
<h2 id="lan-settings">LAN settings</h2>
<ul>
<li><strong>Interface number:</strong> When using the hardware version of Cloudflare One Appliance, this refers to the Ethernet port that you are using for your LAN. If you need a throughput higher than 1 Gbps, you can use one of the SFP+ ports. For details on supported hardware, refer to <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/sfp-port-information/">SFP+ port information</a>. <br />  If you are using the Virtual Appliance, this needs to correspond to the virtual LAN interface on the Virtual Appliance instance you have set up in your virtual machine.</li>
<li><strong>VLAN ID</strong>: Allows you to have multiple virtual LANs configured over the same port on your Cloudflare One Appliance. Refer to <a href="#vlan-id">VLAN ID</a> for more information.</li>
<li><strong>Static addressing:</strong> Configures the type of IP addressing for your Appliance. Depending on your use case, this is where you configure your LAN interface IP address, or enable  DHCP server or DHCP relay. For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/">DHCP options</a>.</li>
<li><strong>Static NAT prefix</strong>: Enable NAT (network address translation). This is an optional setting.</li>
<li><strong>Routed subnets:</strong> Configures additional subnets behind a layer 3 router. For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/routed-subnets/">Routed subnets</a>.</li>
</ul>
<h3 id="restrict-traffic-to-your-premises">Restrict traffic to your premises</h3>
<p>Depending on your use case, you can define policies in your Cloudflare One Appliance to either allow traffic to flow between your LANs without it leaving your local premises or to forward it via the Cloudflare network where you can add additional security features. The default behavior is to drop all LAN-to-LAN traffic. These policies can be created for specific subnets, and link two LANs.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/network-segmentation/">Network segmentation</a>.</p>
