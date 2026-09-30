---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/velocloud/
  description: Integrate Velocloud with Zero Trust networking.
  full_title: Velocloud · Cloudflare One docs
  head_html: <title>Velocloud · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Velocloud with Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/velocloud/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/velocloud/index.md"><meta property="og:title" content="Velocloud · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Velocloud with Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/velocloud/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="IPsec"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/velocloud/#page","headline":"Velocloud \u00b7 Cloudflare One docs","description":"Integrate Velocloud with Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/velocloud/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["IPsec"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/velocloud/
  schema: 1
---
<p>This document is intended to provide Arista VeloCloud customers with the steps to provision non SD-WAN destinations through Edge for connectivity with Cloudflare WAN (formerly Magic WAN).</p>
<h2 id="velocloud-edge-nodes-profile-configuration">VeloCloud Edge Nodes profile configuration</h2>
<ol>
<li>Log into VeloCloud Orchestrator and go to <strong>Configure</strong> &gt; <strong>Profiles</strong>.</li>
<li>Select <strong>New profile</strong> to create a new profile (for example, <code>vc-edge-03-profile</code>).</li>
<li>Select the <strong>Device</strong> tab and expand the <strong>Interfaces</strong> section.</li>
<li>Select the <strong>Edge Model</strong> corresponding to the device (Virtual Edge). The default interface scheme for the Virtual Edge will be displayed. For example: eight interfaces, from GE1 to GE8.</li>
<li>You are only using interfaces <strong>GE3</strong> and <strong>GE4.</strong> Disable all unused interfaces to ensure anyone with physical access to the edge node cannot connect any unused interfaces. Do this by selecting each interface one at a time and unchecking <strong>Interface Enabled</strong> followed by <strong>Save</strong>.</li>
</ol>
<h3 id="configure-interfaces">Configure interfaces</h3>
<p>This documentation assumes:</p>
<ul>
<li><strong>GE3</strong>: WAN Interface (Static IP)</li>
<li><strong>GE4</strong>: LAN Interface (Static IP)</li>
</ul>
<h3 id="interface-ge3-wan-interface">Interface GE3 - WAN interface</h3>
<p>Configure interface GE3 with the following settings:</p>
<ul>
<li><strong>Interface enabled</strong>: Enabled</li>
<li><strong>Capability</strong>: Routed</li>
<li><strong>Segments</strong>: All Segments</li>
<li><strong>Radius Authentication</strong>: Not applicable</li>
<li><strong>ICMP Echo Response</strong>: Enabled</li>
<li><strong>Underlay Accounting</strong>: Enabled</li>
<li><strong>Enable WAN Link</strong>: Enabled</li>
<li><strong>Edge to Edge Encryption</strong>: Enabled</li>
<li><strong>DNS Proxy</strong>: Disabled</li>
<li><strong>VLAN</strong>: Unspecified (this example assumes the device is connected to an access-layer switch port)</li>
<li><strong>EVDSL Modem Attached</strong>: Disabled</li>
</ul>
<h4 id="ipv4-settings">IPv4 settings</h4>
<ul>
<li><strong>Addressing Type</strong>: Static</li>
<li><strong>WAN Link</strong>: User Defined</li>
<li><strong>OSPF</strong>: Not applicable</li>
<li><strong>Multicast</strong>: Not applicable</li>
<li><strong>Advertise</strong>: Disabled</li>
<li><strong>NAT Direct Traffic</strong>: Enabled</li>
<li><strong>Trusted Source</strong>: Disabled</li>
<li><strong>Reverse Path Forwarding</strong>: (unspecified)</li>
</ul>
<h4 id="ipv6-settings">IPv6 settings</h4>
<p>IPv6 is currently not supported with Cloudflare WAN. Uncheck the <strong>Enabled</strong> checkbox.</p>
<p><strong>Router Advertisement Host Settings</strong></p>
<ul>
<li>Disabled</li>
</ul>
<p><strong>L2 Settings</strong></p>
<ul>
<li><strong>Autonegotiate</strong>: Enabled</li>
<li><strong>MTU</strong>: 1500</li>
</ul>
<p>Select <strong>Save</strong> to apply changes for Interface <strong>GE3</strong>.</p>
<h3 id="interface-ge4-lan-interface">Interface GE4 - LAN Interface</h3>
<ul>
<li><strong>Interface Enabled</strong>: Enabled</li>
<li><strong>Capability</strong>: Routed</li>
<li><strong>Segments</strong>: Global Segment</li>
<li><strong>Radius Authentication</strong>: Disabled (Not applicable)</li>
<li><strong>ICMP Echo Response</strong>: Enabled</li>
<li><strong>Underlay Accounting</strong>: Enabled</li>
<li><strong>WAN Link</strong>: Disabled</li>
<li><strong>Edge To Edge Encryption</strong>: Enabled</li>
<li><strong>DNS Proxy</strong>: Disabled</li>
<li><strong>VLAN</strong>: Unspecified (this example assumes the device is connected to an access-layer switch port)</li>
<li><strong>EVDSL Modem Attached</strong>: Disabled</li>
</ul>
<h4 id="ipv4-settings-1">IPv4 Settings</h4>
<ul>
<li><strong>Addressing Type</strong>: DHCP or Static (example assumes Static IP)</li>
<li><strong>WAN Link</strong>: User Defined</li>
<li><strong>OSPF</strong>: Not applicable</li>
<li><strong>Multicast</strong>: Not applicable</li>
<li><strong>Advertise</strong>: Disabled</li>
<li><strong>NAT Direct Traffic</strong>: Enabled</li>
<li><strong>Trusted Source</strong>: Disabled</li>
<li><strong>Reverse Path Forwarding</strong>: Unspecified</li>
</ul>
<h4 id="ipv6-settings-1">IPv6 Settings</h4>
<p>IPv6 is currently not supported with Cloudflare WAN. Uncheck the <strong>Enabled</strong> checkbox.</p>
<p><strong>Router Advertisement Host Settings</strong></p>
<ul>
<li>Disabled</li>
</ul>
<p><strong>L2 Settings</strong></p>
<ul>
<li><strong>Autonegotiate</strong>: Enabled</li>
<li><strong>MTU</strong>: 1500</li>
</ul>
<p>Select <strong>Save</strong> to apply changes for Interface <strong>GE4</strong>.</p>
<p>The Interfaces section should indicate the <strong>GE3</strong> (WAN) and <strong>GE4</strong> (LAN) interfaces are configured and all other interfaces are administratively disabled.</p>
<h3 id="vpn-services">VPN Services</h3>
<ul>
<li>Enable <strong>Cloud VPN</strong>.</li>
</ul>
<p>Select <strong>Save</strong> to apply changes for the Profile.</p>
<h2 id="network-services">Network Services</h2>
<ol>
<li>Go to <strong>Configure</strong> &gt; <strong>Network Services</strong>.</li>
<li>Expand <strong>Non SD-WAN Destinations through Edge</strong> and select <strong>New</strong>.</li>
</ol>
<h3 id="general">General</h3>
<ul>
<li><strong>Service</strong> <strong>Name</strong>: Name of destination here. For example, <code>Magic_WAN_vc-edge-03</code>.</li>
<li><strong>Tunneling Protocol</strong>: <strong>IPsec</strong></li>
<li><strong>Service Type</strong>: <em>Generic IKEv2 Router (Route Based VPN)</em></li>
<li><strong>Tunnel Mode</strong>: <em>Active/Hot-Standby</em> or <em>Active/Standby</em></li>
</ul>
<h3 id="ike-ipsec-settings">IKE/IPsec settings</h3>
<ol>
<li>In the <strong>IKE/IPsec Settings</strong> tab, select:
<ol>
<li><strong>IP Version</strong>: <em>IPv4</em></li>
<li><strong>Primary VPN Gateway</strong>
<ol>
<li><strong>Public IP</strong>: Specify one of the two Cloudflare anycast IP addresses assigned to your account, available in <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space">Leased IPs</a>.</li>
</ol>
</li>
</ol>
</li>
<li>In <strong>IKE Proposal</strong>, expand <strong>View advanced settings for IKE Proposal</strong>:
<ol>
<li><strong>Encryption</strong>: <em>AES 256 CBC</em></li>
<li><strong>DH Group</strong>: <em>14</em></li>
<li><strong>Hash</strong>: <em>SHA-256</em></li>
<li><strong>IKE SA Lifetime (min)</strong>: <em>1440</em></li>
<li><strong>DPD Timeout(sec)</strong>: <strong>20</strong></li>
</ol>
</li>
<li>Expand <strong>View advanced settings for IPsec Proposal</strong>:
<ol>
<li><strong>Encryption</strong>: <em>AES 256 CBC</em></li>
<li><strong>PFS</strong>: <em>14</em></li>
<li><strong>Hash</strong>: <em>SHA 256</em></li>
<li><strong>IPsec SA Lifetime (min)</strong>: <strong>480</strong></li>
</ol>
</li>
<li>Scroll up <strong>Secondary VPN Gateway</strong>, and select <strong>Add</strong>.
<ol>
<li><strong>Public IP</strong>: Specify the second of the two Cloudflare anycast IP addresses</li>
<li><strong>Keep Tunnel Active</strong>: Enabled (this is read-only and cannot be modified)</li>
<li>Tunnel settings are the same as the primary — therefore they are greyed out in this section.</li>
</ol>
</li>
</ol>
<h2 id="provision-edge-devices">Provision Edge Devices</h2>
<ol>
<li>Go to <strong>Configure</strong> &gt; <strong>Edges</strong>, and select <strong>Add Edge</strong>.</li>
<li>Select the following settings:
<ol>
<li><strong>Mode</strong>: SD-WAN Edge</li>
<li><strong>Name</strong>: The name for your edge. For example, <code> vc-edge-03</code></li>
<li><strong>Model</strong>: <em>Virtual Edge</em> (select the model of your Arista VeloCloud Edge appliance)</li>
<li><strong>Profile</strong>: Select the Profile created in the Provision configuration section. For example, <code>vc-edge-03-profile</code></li>
<li><strong>Edge License</strong>: Select the appropriate license</li>
<li><strong>Authentication</strong>: <em>Certificate Acquire</em></li>
<li><strong>Encrypt Device Secrets</strong>: Unchecked (do not select)</li>
<li><strong>High Availability</strong>: Unchecked (configure accordingly based on your environment)</li>
<li><strong>Contact Info</strong>: Provide a local contact name and local contact email</li>
</ol>
</li>
<li>Select <strong>Next</strong> to advance to the next section.</li>
</ol>
<h3 id="additional-settings">Additional settings</h3>
<ol>
<li>Configure the following settings based on your environment — left blank in the following example.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/velocloud/image1.png" alt="This example was left blank. You should configure this based on your environment." /></p>
<ol start="2">
<li>Select <strong>Add Edge</strong> to save changes.</li>
</ol>
<h3 id="edge-device-settings">Edge — Device Settings</h3>
<p>Once the Edge device is added, you should land on the <strong>Device</strong> tab.</p>
<h4 id="connectivity-interfaces">Connectivity — Interfaces</h4>
<ol>
<li>Expand the <strong>Interfaces</strong> section.</li>
<li>Note the interface configuration is inherited from the Profile configured in the previous section. Interfaces <strong>GE3</strong> and <strong>GE4</strong> will display a <code>WARNING</code> indicator as these interfaces require additional configuration.</li>
<li>Select <strong>GE3</strong> to open the properties for the WAN interface.</li>
<li>Many of the properties in this section were inherited from the Profile — as such, they are greyed out. You can select <strong>Override</strong> to modify the configuration specifically for this interface.</li>
<li>Scroll down to <strong>IPv4 Settings</strong>, and configure the following options:
<ol>
<li><strong>Addressing Type</strong>: <em>Static</em> (this is inherited from the Profile)</li>
<li><strong>IP Address</strong>: Specify the WAN interface IP address</li>
<li><strong>CIDR Prefix</strong>: Add your subnet mask in Classless Inter-Domain Routing (CIDR) notation</li>
<li><strong>Gateway</strong>: Default Gateway (<code>0.0.0.0/0</code>)</li>
<li>All other settings are inherited from the Profile.</li>
</ol>
</li>
<li>Scroll down and select <strong>Save</strong>.</li>
<li>Select <strong>GE4</strong> to open the properties for the LAN interface.</li>
<li>Scroll down to <strong>IPv4 Settings</strong>, and configure the following options:
<ol>
<li><strong>Addressing Type</strong>: Static (inherited from the Profile)</li>
<li><strong>IP Address</strong>: Specify the WAN interface IP address</li>
<li><strong>CIDR Prefix</strong>: (subnet mask in CIDR notation)</li>
<li><strong>Gateway</strong>: Default Gateway (0.0.0.0/0)</li>
<li>All other settings are inherited from the Profile.</li>
</ol>
</li>
<li>Scroll down and select <strong>Save</strong>.</li>
</ol>
<h4 id="user-defined-wan-link">User Defined WAN Link</h4>
<p>Note the indicator next to <strong>GE3</strong>. The steps in the Profile section disabled <strong>Auto WAN Link Detection</strong>. As a result,  the WAN Link must be specified.</p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/velocloud/image2.png" alt="Note the indicator next to GE3." /></p>
<ol>
<li>Scroll down to <strong>WAN Link Configuration</strong> &gt; <strong>Add User Defined WAN Link</strong>, and configure the following options:
<ol>
<li><strong>Link Type</strong>: <em>Public</em> (the WAN interface is connected directly to the Internet in this example — you may need to select <em>Private</em> depending on your environment)</li>
<li><strong>Interfaces</strong>: Check the box for <strong>GE3</strong> (WAN Interface)</li>
</ol>
</li>
<li>This example assumes default settings under <strong>View optional</strong> <strong>configuration</strong> and <strong>View advanced settings</strong>.</li>
<li>Select <strong>Add Link</strong> to save the changes.</li>
<li>Confirm the <strong>User Defined WAN Link</strong> is displayed and an indicator no longer appears next to interface <strong>GE3</strong>.</li>
</ol>
<h4 id="vpn-services-1">VPN Services</h4>
<ol>
<li>Scroll down to <strong>VPN Services</strong>.</li>
<li>Expand <strong>Non SD-WAN Destination through Edge</strong> and select the <strong>Override</strong> checkbox.</li>
<li>Select <strong>Add</strong>.</li>
<li>Select the drop-down under the <strong>Name</strong> column.</li>
<li>Select the <strong>Network Service</strong> defined earlier. For example, <code>Magic_WAN_vc-edge-03</code>.</li>
<li>In the <strong>Action</strong> column, select the <strong>+</strong> button, and configure the following options:
<ol>
<li><strong>Public WAN Link</strong>: Choose the Public WAN Link (refer to User-Defined WAN Link)</li>
<li><strong>Local Identification Type</strong>: <em>FQDN</em></li>
<li><strong>Local Identification</strong>: Enter the FQDN specified when configuring Cloudflare WAN IPsec tunnels through the Custom FQDN IKE ID API endpoint.</li>
<li><strong>PSK</strong>: Enter the Pre-Shared Key. Ensure you use the same PSK for both Cloudflare WAN IPsec tunnels.</li>
<li><strong>Destination Primary Public IP</strong>: Pre-populated from the Network Service defined earlier.</li>
<li><strong>Destination Secondary Public IP</strong>: Pre-populated from the Network Service defined earlier.</li>
</ol>
</li>
<li>Select <strong>Save</strong> to finish defining the IPsec tunnel settings.</li>
<li>Scroll down to the bottom of the Edge configuration page, and select <strong>Save Changes</strong> to finalize the Edge device configuration.</li>
</ol>
<h2 id="velocloud-to-cloudflare-wan-routing">VeloCloud to Cloudflare WAN routing</h2>
<p>Configure the <strong>Site Subnets</strong> to facilitate:</p>
<ul>
<li>Routing traffic from one Cloudflare WAN site to other Cloudflare WAN sites.</li>
<li>Ensure Cloudflare WAN IPsec tunnel health checks perform optimally.</li>
</ul>
<ol>
<li>Go to <strong>Configure</strong> &gt; <strong>Network Services</strong>.</li>
<li>Expand the <strong>Non SD-WAN Destinations through Edge</strong> section.</li>
<li>Select the desired non SD-WAN destination, like <code>Magic_WAN_vc-edge-03</code>.</li>
</ol>
<h3 id="site-subnets">Site Subnets</h3>
<p>Configure a minimum of three IPsec tunnels. This example demonstrates two routes for tunnel health checks and two routes for traffic destined for remote sites:</p>
<ul>
<li>Cloudflare WAN IPsec tunnel health checks</li>
<li>Primary VPN Gateway:
<ul>
<li>To the respective Cloudflare WAN IPv4 interface address associated with the primary Cloudflare anycast tunnel endpoint IP address</li>
<li>Routed through the Primary VPN Gateway.</li>
</ul>
</li>
<li>Secondary VPN Gateway:
<ul>
<li>To the respective Cloudflare WAN IPv4 interface address associated with the secondary Cloudflare anycast tunnel endpoint IP address</li>
<li>Routed through the Secondary VPN Gateway.</li>
</ul>
</li>
<li>Remote Cloudflare WAN site(s): CIDR blocks to route through Cloudflare WAN
<ul>
<li>The LAN interface for vc-edge-03 is:
<ul>
<li>172.16.34.254/24 (subnet address: 172.16.34.0/24).</li>
<li>This does not need to be specified under Site Subnets as it is local.</li>
</ul>
</li>
<li>Assume two remote sites, each of which need to be defined as Site Subnets and routed through both the Primary VPN Gateway and Secondary VPN Gateway.
<ul>
<li>172.16.32.0/24</li>
<li>172.16.33.0/24</li>
</ul>
</li>
</ul>
</li>
</ul>
<ol>
<li>Select the <strong>Site Subnets</strong> &gt; <strong>Add</strong>. Then, select the following configurations for routes:
<ol>
<li>Tunnel Health Check - Primary:
<ol>
<li>10.252.11.4/32 - Primary VPN Gateway</li>
</ol>
</li>
<li>Tunnel Health Check - Secondary:
<ol>
<li>10.252.11.6/32 - Secondary VPN Gateway</li>
</ol>
</li>
<li>Site vc-edge-01:
<ol>
<li>172.16.32.0/24 - Primary and Secondary VPN Gateways</li>
</ol>
</li>
<li>Site vc-edge-02:
<ol>
<li>172.16.33.0/24 - Primary and Secondary VPN Gateways</li>
</ol>
</li>
</ol>
</li>
<li>The <strong>Site Subnets</strong> tab should look like the following when configured as indicated:</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/velocloud/image3.png" alt="An example of how the Site Subnets tab should look like when configured as indicated." /></p>
<ol start="3">
<li>Select <strong>Save</strong> to commit changes to the Site Subnets.</li>
</ol>
<h2 id="cloudflare-wan-and-cloudflare-gateway">Cloudflare WAN and Cloudflare Gateway</h2>
<p>Cloudflare WAN and Secure Web Gateway (Cloudflare Gateway) are tightly integrated. Arista VeloCloud customers can easily route traffic through Cloudflare WAN to Cloudflare Gateway. All Internet egress traffic is subject to Cloudflare Gateway policies.</p>
<p>Arista VeloCloud's Business Policies allow for intelligent routing of traffic destined for the Internet with only a few selections.</p>
<h3 id="configure-business-policy">Configure Business Policy</h3>
<ol>
<li>Go to <strong>Configure</strong> &gt; <strong>Edges</strong>, and select the appropriate Edge appliance.</li>
<li>Select the <strong>Business Policy</strong> tab.</li>
<li>Select <strong>Add</strong> to create a Business Policy Rule:
<ol>
<li><strong>Rule Name</strong>: Provide a meaningful name to describe Internet traffic routed through the Cloudflare global anycast network.</li>
<li><strong>IP Version</strong>: <em>IPv4</em></li>
<li><strong>Match</strong>
<ol>
<li><strong>Source</strong>: Select <em>Any</em>, <em>Object Groups</em>, or <em>Define</em> to classify the relevant traffic flows.</li>
<li><strong>Destination</strong>: Select <em>Define</em> &gt; <em>Internet</em></li>
<li><strong>Application</strong>: <em>Any</em></li>
</ol>
</li>
<li><strong>Action</strong>
<ol>
<li><strong>Priority</strong>: Normal</li>
<li><strong>Enable Rate Limit</strong>: Unchecked</li>
<li><strong>Network Service</strong>: <em>Internet Backhaul</em> &gt; <em>Non SD-WAN Destination through Edge / Cloud Security Service</em>.</li>
<li><strong>Non SD-WAN Destination through Edge / Cloud Security Service</strong>: Select the Network Service associated with the respective Edge device. For example, <code>Magic_WAN_vc-edge-03</code>.</li>
</ol>
</li>
</ol>
</li>
<li>Select <strong>Create</strong> to save the rule.</li>
</ol>
