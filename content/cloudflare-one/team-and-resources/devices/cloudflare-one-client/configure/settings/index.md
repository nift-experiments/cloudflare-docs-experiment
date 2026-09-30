---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/
  description: Reference information for Device client settings in Zero Trust.
  full_title: Device client settings · Cloudflare One docs
  head_html: <title>Device client settings · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Device client settings in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/index.md"><meta property="og:title" content="Device client settings · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Device client settings in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Wireguard,MASQUE"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#page","headline":"Device client settings \u00b7 Cloudflare One docs","description":"Reference information for Device client settings in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Wireguard","MASQUE"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/
  schema: 1
---
<p>Device client settings (formerly WARP) allow you to customize the Cloudflare One Client modes and permissions available to end users.</p>
<ul>
<li><a href="#global-device-client-settings">Global device client settings</a> are configurations which apply to all devices enrolled in your Zero Trust organization.</li>
<li><a href="#global-disconnection-settings">Global disconnection settings</a> allow administrators to force-disconnect all Cloudflare One Clients during an incident or outage.</li>
<li><a href="#device-profile-settings">Device profile settings</a> can vary across devices depending on which <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> is applied.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6209.md")
</aside>
<h2 id="global-device-client-settings">Global device client settings</h2>
<h3 id="allow-admin-override-codes">Allow admin override codes</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6210.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6208.md")
</aside>
<p>When <a href="#lock-device-client-switch"><strong>Lock device client switch</strong></a> is enabled, users cannot toggle the Cloudflare One Client on and off on their device. Enabling <strong>Allow admin override codes</strong> gives users the ability to temporarily connect or disconnect the Cloudflare One Client using an override code provided by an admin. <strong>Allow admin override codes</strong> is only needed in a configuration where <strong>Lock device client switch</strong> is enabled.</p>
<p>Example use cases for <strong>Allow admin override codes</strong> include:</p>
<ul>
<li>Allowing users to momentarily disconnect the Cloudflare One Client to work around a temporary network issue such as an incompatible public Wi-Fi, or a firewall at a customer site blocking the connection.</li>
<li>Allowing test users to connect the Cloudflare One Client while a global disconnect is in effect.</li>
</ul>
<p>As admin, you can set a <strong>Timeout</strong> to define how long a user can toggle the client's connection toggle on or off after entering the override code. Cloudflare generates a new override code every hour that an admin can send to end users. The override code's validity adheres to fixed-hour time blocks and aims to be generous to the end user.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="troubleshooting">Troubleshooting</h3>
@markup("md", "content/.markup/bodies/6207.md")
</aside>
<h4 id="retrieve-the-override-code">Retrieve the override code</h4>
<p>To retrieve the one-time code for a user:</p>
<ol>
<li>Enable <strong>Allow admin override codes</strong>.</li>
<li>Go to <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong>.</li>
<li>Select <strong>View details</strong> for a connected device.</li>
<li>Scroll down to <strong>User details</strong> and select the user's name.</li>
<li>Copy the 7-digit <strong>Override code</strong> shown in the side panel.</li>
<li>Share this code with the user for them to enter on their device.</li>
</ol>
<p>The user will have an unlimited amount of time to activate their code.</p>
<h4 id="enter-the-override-code">Enter the override code</h4>
<p>To activate the override code on a user device:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6213.md")
</div></div>
<p>The user can now toggle the client's connection toggle or use the <code>warp-cli connect</code> command. The client will automatically reconnect after the <a href="#auto-connect">Auto connect period</a>, but the user can continue to connect or disconnect the Cloudflare One Client until the override expires.</p>
<h3 id="install-ca-to-system-certificate-store">Install CA to system certificate store</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6214.md")
</div></details>
<p>When <code>Enabled</code>, the Cloudflare One Client will <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/">automatically install</a> your organization's root certificate on the device.</p>
<h3 id="assign-a-unique-ip-address-to-each-device">Assign a unique IP address to each device</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6215.md")
</div></details>
<p>Overrides the default IP address of the Cloudflare One Client's <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#ip-traffic">virtual network interface</a> such that each device has its own unique local interface IP.</p>
<p>This setting is primarily used as a prerequisite for <a href="/mesh/">Cloudflare Mesh</a> and <a href="#device-tunnel-protocol">MASQUE</a>. You can also use it when the default IP conflicts with other local services on your network.</p>
<p><strong>Value:</strong></p>
<ul>
<li>
<p><code>Disabled</code>: (default) Sets the local interface IP to <code>172.16.0.2</code> on all devices. This configuration is only respected by devices using <a href="#device-tunnel-protocol">WireGuard</a> and does not affect devices using <a href="#device-tunnel-protocol">MASQUE</a>.</p>
</li>
<li>
<p><code>Enabled</code>: Sets the local interface IP on each device to its <span class="nb-glossary-tooltip" title="WARP CGNAT IP">CGNAT IP</span> or to a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-ips/">custom device IP</a>.</p>
</li>
</ul>
<p>The IP assigned to a device is permanent until the device unregisters from your Zero Trust organization or switches to a different registration. Disconnects and reconnects do not change the IP address assignment.</p>
<h3 id="allow-all-cloudflare-one-traffic-to-reach-enrolled-devices">Allow all Cloudflare One traffic to reach enrolled devices</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6217.md")
</div></details>
<p>Allows traffic on-ramped using <a href="/mesh/">Cloudflare Mesh</a> or <a href="/cloudflare-one/networks/connectors/cloudflare-wan/">Cloudflare WAN</a> to route to devices enrolled in your Zero Trust organization.</p>
<p>Each device is assigned a virtual IP address in the <span class="nb-glossary-tooltip" title="WARP CGNAT IP">CGNAT IP</span> space (<code>100.96.0.0/12</code>) or a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-ips/">custom device IP range</a>. With this setting <code>Enabled</code>, users on your private network will be able to connect to these device IPs and access <a href="/cloudflare-one/traffic-policies/proxy/">TCP, UDP, and/or ICMP-based services</a> on your devices. You can create <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a> to control which users and devices can access the device IPs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6206.md")
</aside>
<h2 id="global-disconnection-settings">Global disconnection settings</h2>
<h3 id="disconnect-the-cloudflare-one-client-on-all-devices">Disconnect the Cloudflare One Client on all devices</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6219.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6205.md")
</aside>
<p><strong>Disconnect the Cloudflare One Client on all devices</strong> allows administrators to fail open the Cloudflare One Client in case of an incident occurring in your environment, independent from incidents or outages affecting Cloudflare's services. When you turn on <strong>Disconnect the Cloudflare One Client on all devices</strong>, Cloudflare will disconnect all Windows, macOS, and Linux Cloudflare One Clients that are connected to your Zero Trust organization. This includes end user devices and <a href="/mesh/">Cloudflare Mesh</a> nodes. End users will receive a notification on their device and the Cloudflare One Client will display <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/client-errors/#admin-directed-disconnect"><code>Admin directed disconnect</code></a>.</p>
<p>To resume normal operations, turn off <strong>Disconnect the Cloudflare One Client on all devices</strong>. The Cloudflare One Client will automatically reconnect.</p>
<p>For more information on how <strong>Disconnect the Cloudflare One Client on all devices</strong> works with other device client settings, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#device-client-settings-precedence">Device client settings precedence</a>.</p>
<h3 id="manage-device-connection-using-an-external-signal">Manage device connection using an external signal</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6220.md")
</div></details>
<p>Allows administrators to disconnect and reconnect the Cloudflare One Client independently from any Cloudflare infrastructure. When <code>Enabled</code>, Cloudflare One Clients will periodically poll the configured HTTPS endpoint and disconnect when they receive a valid disconnect signal.</p>
<p>To set up the external HTTPS endpoint, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">Emergency Disconnect</a>.</p>
<h3 id="manage-device-connection-using-a-local-file">Manage device connection using a local file</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6221.md")
</div></details>
<p>Allows administrators to disconnect and reconnect the Cloudflare One Client using a local JSON file on the device, without requiring any network connectivity. When <code>Enabled</code>, the Cloudflare One Client monitors a fixed file path for a disconnect signal. This is useful for disaster recovery scenarios where both Cloudflare and your own infrastructure may be unreachable.</p>
<p>To set up the local signal file, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-local-emergency-disconnect">Emergency Disconnect</a>.</p>
<h2 id="device-profile-settings">Device profile settings</h2>
<h3 id="captive-portal-detection">Captive portal detection</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6222.md")
</div></details>
<p>When <code>Enabled</code>, the Cloudflare One Client will automatically disconnect when it detects a <span class="nb-glossary-tooltip" title="captive portal">captive portal</span>, and it will automatically reconnect after the <strong>Timeout</strong> duration.</p>
<p>Since captive portal implementations vary, the Cloudflare One Client may not detect all captive portals. For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/captive-portals/">Captive portal detection</a>.</p>
<h3 id="mode-switch">Mode switch</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6224.md")
</div></details>
<p>When <code>Enabled</code>, users have the option to switch between <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-and-dns-mode-default">Traffic and DNS mode</a> and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode">DNS only mode</a>. This feature does not support switching between any other modes.</p>
<h3 id="device-tunnel-protocol">Device tunnel protocol</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6225.md")
</div></details>
<p>Configures the protocol used to route IP traffic from the device to Cloudflare Gateway. To check the active protocol on a device, open a terminal and run <code>warp-cli settings | grep protocol</code>.</p>
<p><strong>Value</strong>:</p>
<ul>
<li><strong>WireGuard</strong>: Establishes a <a href="https://www.wireguard.com/">WireGuard</a> connection to Cloudflare. The Cloudflare One Client will encrypt traffic using a non-FIPs compliant cipher suite, <code>TLS_CHACHA20_POLY1305_SHA256</code>. When switching from MASQUE to WireGuard, users may lose Internet connectivity if their Wi-Fi network blocks the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#warp-ingress-ip">ports and IPs</a> required for WireGuard to function.</li>
<li><strong>MASQUE</strong>: (default) Establishes an HTTP/3 connection to Cloudflare. The Cloudflare One Client will encrypt traffic using TLS 1.3 and a <a href="https://csrc.nist.gov/pubs/fips/140-3/final">FIPS 140-3</a> compliant cipher suite, <code>TLS_AES_256_GCM_SHA384</code>. <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#assign-a-unique-ip-address-to-each-device">Assign a unique IP address to each device</a> is enabled by default for devices with MASQUE enabled.</li>
</ul>
<p>For more details on WireGuard versus MASQUE, refer to our <a href="https://blog.cloudflare.com/zero-trust-warp-with-a-masque">blog post</a>.</p>
<h3 id="lock-device-client-switch">Lock device client switch</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6226.md")
</div></details>
<p>Allows the user to disconnect the Cloudflare One Client.</p>
<p><strong>Value:</strong></p>
<ul>
<li><code>Disabled</code>: (default) The user is able to connect or disconnect the Cloudflare One Client at their discretion. When the client is disconnected, the user will not have the ability to reach sites protected by Access that leverage certain device posture checks.</li>
<li><code>Enabled</code>: The user is prevented from disconnecting the Cloudflare One Client. The client will always start in the connected state.</li>
</ul>
<p>On MDM deployments, you must also include the <code>auto_connect</code> parameter with at least a value of <code>0</code>. This will prevent clients from being deployed in the off state without a way for users to manually enable them.</p>
<h3 id="allow-device-to-leave-organization">Allow device to leave organization</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6227.md")
</div></details>
<p>When <code>Enabled</code>, users can log out from your Zero Trust organization by selecting <strong>Logout from Zero Trust</strong> in the Cloudflare One Client UI. The <strong>Logout from Zero Trust</strong> button is only available for devices that were <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">enrolled manually</a>. Devices that enrolled using an <span class="nb-glossary-tooltip" title="MDM file">MDM file</span> are always prevented from leaving your Zero Trust organization.</p>
<h3 id="allow-updates">Allow updates</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6229.md")
</div></details>
<p>When <code>Enabled</code>, users will receive update notifications when a new version of the client is available. Only turn this on if your users are local administrators with the ability to add or remove software from their device.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6204.md")
</aside>
<h3 id="auto-connect">Auto connect</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6230.md")
</div></details>
<p>When <code>Enabled</code>, the client will automatically reconnect if it has been disabled for the specified <strong>Timeout</strong> value. This setting is best used in conjunction with <a href="#lock-device-client-switch">Lock device client switch</a> above.</p>
<p>We recommend keeping this set to a very low value — usually just enough time for a user to log in to hotel or airport Wi-Fi. If any value is specified, the client defaults to the Connected state (for example, after a reboot or the initial install).</p>
<p><strong>Value:</strong></p>
<ul>
<li><code>0</code>: Allow the switch to stay in the off position indefinitely until the user turns it back on.</li>
<li><code>1</code> to <code>1440</code>: Turn switch back on automatically after the specified number of minutes.</li>
</ul>
<h3 id="support-url">Support URL</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6231.md")
</div></details>
<p>When <code>Enabled</code>, the <strong>Send Feedback</strong> button in the Cloudflare One Client appears and will launch the URL specified. Example <strong>Support URL</strong> values are:</p>
<ul>
<li><code>https://support.example.com</code>: Use an https:// link to open your companies internal help site.</li>
<li><code>mailto:yoursupport@example.com</code>: Use a <code>mailto:</code> link to open your default mail client.</li>
</ul>
<h3 id="service-mode">Service mode</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6232.md")
</div></details>
<p>Allows you to choose the operational mode of the client. Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes">Client modes</a> for a detailed description of each mode.</p>
<h3 id="local-domain-fallback">Local Domain Fallback</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6233.md")
</div></details>
<p>Configures the Cloudflare One Client to redirect DNS requests to a private DNS resolver. For more information, refer to our <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> documentation.</p>
<h3 id="split-tunnels">Split Tunnels</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6234.md")
</div></details>
<p>Configures the Cloudflare One Client to exclude or include traffic to specific IP addresses or domains. For more information, refer to our <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel</a> documentation.</p>
<h3 id="directly-route-microsoft-365-traffic">Directly route Microsoft 365 traffic</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6235.md")
</div></details>
<p>Creates <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel</a> Exclude entries for all <a href="https://docs.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-ip-web-service">Microsoft 365 IP addresses specified by Microsoft</a>. To use this setting, <strong>Split Tunnels</strong> must be set to <strong>Exclude IPs and domains</strong>. Once enabled, all Microsoft 365 network traffic will bypass the Cloudflare One Client and Gateway.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6203.md")
</aside>
<h3 id="allow-users-to-enable-local-network-exclusion">Allow users to enable local network exclusion</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6236.md")
</div></details>
<p>This setting is intended as a workaround for users whose home network uses the same set of IP addresses as your corporate private network. To use this setting, <strong>Split Tunnels</strong> must be set to <strong>Exclude IPs and domains</strong>.</p>
<p>When <code>Enabled</code>, users have the option to access local network resources (such as printers and storage devices) while connected to the Cloudflare One Client. When the user turns on <a href="#access-local-network-as-a-user"><strong>Access Local Network</strong></a>, the Cloudflare One Client will detect the local IP range advertised by the user's home network (for example, <code>10.0.0.0/24</code>) and temporarily exclude this range from the WARP tunnel. The user will need to re-request access after the <strong>Timeout</strong> expires. Setting <strong>Timeout</strong> to <code>0 minutes</code> will allow LAN access until the next client reconnection, such as a reboot or a laptop waking from sleep.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/6202.md")
</aside>
<h4 id="access-local-network-as-a-user">Access local network as a user</h4>
<p>To turn on local network access in the Cloudflare One Client:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6241.md")
</div></div>
<h4 id="limitations">Limitations</h4>
<ul>
<li>The Cloudflare One Client will only exclude local networks in the <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918</a> address space. Other IP addresses such as CGNAT are not supported.</li>
<li>The maximum excluded subnet size is <code>/24</code>.</li>
<li>If a device has multiple network interfaces with distinct local IP ranges, the Cloudflare One Client will only exclude one of those networks. To access a specific local network, disable the other interfaces and disconnect/reconnect the Cloudflare One Client.</li>
</ul>
<h3 id="client-interface-ip-dns-registration">Client interface IP DNS registration</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6242.md")
</div></details>
<p>When <code>Enabled</code>, the operating system will register the Cloudflare One Client's <a href="#assign-a-unique-ip-address-to-each-device">local interface IP</a> (CGNAT IP or <code>172.16.0.2</code>) with your on-premise DNS server when the DNS server is reachable.</p>
<p>If you use on-premise DNS infrastructure (such as Active Directory), we recommend turning this setting on for remote <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a> and turning it off for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/managed-networks/">managed network</a> device profiles. In this configuration, remote devices will register their client interface IP, while on-premise devices will only register their local DHCP address. This allows the on-premise DNS server to resolve device hostnames no matter where the device is located.</p>
<h3 id="sccm-vpn-boundary-support">SCCM VPN boundary support</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6243.md")
</div></details>
<p>Microsoft's <a href="https://learn.microsoft.com/en-us/intune/configmgr/">System Center Configuration Manager</a> (SCCM) is used to manage software on Windows devices based on the <a href="https://learn.microsoft.com/en-us/intune/configmgr/core/servers/deploy/configure/define-site-boundaries-and-boundary-groups">boundary group</a>, or network location, to which they belong. You can assign Cloudflare One Clients to a SCCM boundary group based on their <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/managed-networks/">managed network</a> and other device profile attributes. When <strong>SCCM VPN Boundary Support</strong> is turned on, the Cloudflare One Client will modify the description field on its <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#ip-traffic">virtual network interface</a>. This allows you to define a VPN boundary group that matches on the network interface description.</p>
<p><strong>Value:</strong></p>
<ul>
<li>
<p><code>Disabled</code>: (default) The client network interface description is <code>Cloudflare WARP Interface Tunnel</code>.</p>
</li>
<li>
<p><code>Enabled</code>: The client network interface description is <code>(SCCM) Cloudflare WARP Interface Tunnel</code> for devices which have the <a href="https://learn.microsoft.com/en-us/intune/configmgr/core/clients/deploy/deploy-clients-to-windows-computers">SCCM client</a> installed. Devices without the SCCM client will still use the default <code>Cloudflare WARP Interface Tunnel</code> description. The Cloudflare One Client checks if the SCCM client is installed by looking for the SMS Agent Host (<code>ccmexec.exe</code>) Windows service.</p>
</li>
</ul>
<h4 id="example-sccm-configuration">Example SCCM configuration</h4>
<p>Assume you want to push software updates from a cloud based <a href="https://learn.microsoft.com/en-us/intune/configmgr/core/servers/deploy/configure/boundary-groups-distribution-points">distribution point</a> if the device is remote, but use on-prem servers if the device is on the office network. To set up these boundary groups:</p>
<ol>
<li>
<p>In Zero Trust:</p>
<pre tabindex="0"><code>a. Turn on **SCCM VPN Boundary Support** for remote [device profiles](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/).&#10;&#10;b. Turn off **SCCM VPN Boundary Support** for [on-prem device profiles](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/managed-networks/#4-configure-device-profile).&#10;&#10;c. (Optional) Verify device settings:&#10;</code></pre>
<details class="nb-details"><summary>Verify SCCM VPN Boundary Support</summary><div class="nb-details-body">
</li>
</ol>
@markup("md", "content/.markup/bodies/6244.md")
</div></details>
<ol start="2">
<li>
<p>In Microsoft SCCM:</p>
<pre tabindex="0"><code>a. [Create a boundary](https://learn.microsoft.com/en-us/intune/configmgr/core/servers/deploy/configure/boundaries#create-a-boundary) with the following settings:&#10;	- **Description**: `Remote Cloudflare One Clients`&#10;	- **Type**: _VPN_&#10;	- **Connection description**: `(SCCM) Cloudflare WARP Interface Tunnel`&#10;</code></pre>
<p>b. Assign this boundary to one or more boundary groups.</p>
</li>
</ol>
<p>When the device is remote, the client interface description changes to <code>(SCCM) Cloudflare WARP Interface Tunnel</code> and the SCCM server will determine that the device belongs to the VPN boundary group. The device can now download updates from the distribution point assigned to this boundary group. When a network change occurs and the Cloudflare One Client detects a managed network, it will revert the interface description to <code>Cloudflare WARP Interface Tunnel</code> and the boundary condition will no longer be satisfied. The device will match your local IP range and be considered as on-prem.</p>
<h3 id="netbios-over-tcpip">NetBIOS over TCPIP</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6245.md")
</div></details>
<p>NetBIOS over TCP/IP (NetBT) is a legacy protocol used for name resolution and other features on Windows. NetBT has been deprecated for years, but Windows has not removed it. The Cloudflare One Client disables NetBT on the tunnel interface by default for security reasons and to align with modern best practices. This setting allows you to override the default behavior and enable NetBT over the WARP tunnel.</p>
<h4 id="when-to-enable-netbt">When to enable NetBT</h4>
<p>You should turn on <strong>NetBIOS over TCPIP</strong> only if devices need to access internal resources over NetBT. Example scenarios include:</p>
<ul>
<li><strong>Legacy name resolution</strong>: You rely on NetBIOS to resolve single-label names (such as <code>\\SERVER01</code>), instead of modern alternatives like mDNS for single-label names or standard DNS for Fully Qualified Domain Names (such as <code>\\server01.corp.internal</code>).</li>
<li><strong>SMBv1</strong>: You are accessing very old file shares or printers that do not support modern SMB (v2/v3) and require NetBT for discovery.</li>
<li><strong>Legacy applications</strong>: You use specialized internal software that hard-codes NetBIOS for node-to-node communication.</li>
</ul>
<p>Otherwise, the recommendation is to always disable <strong>NetBIOS over TCPIP</strong>. You can choose a different setting for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">remote devices</a> versus <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/managed-networks/#4-configure-device-profile">on-prem devices</a>.</p>
<h4 id="verify-netbt-settings">Verify NetBT settings</h4>
<p>To check if <strong>NetBIOS over TCPIP</strong> is enabled on the client tunnel interface, run the following command:</p>
<pre tabindex="0"><code class="language-txt">warp-cli settings | findstr &quot;NetBT&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">(network policy) NetBT: true&#10;</code></pre>
<p>You can also verify network interface details for the <code>CloudflareWARP</code> adapter:</p>
<pre tabindex="0"><code class="language-txt">ipconfig /all&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">Windows IP Configuration&#10;...&#10;Unknown adapter CloudflareWARP:&#10;    Connection-specific DNS Suffix  . :&#10;    Description . . . . . . . . . . . : Cloudflare WARP Interface Tunnel&#10;    Physical Address. . . . . . . . . :&#10;    DHCP Enabled. . . . . . . . . . . : No&#10;    Autoconfiguration Enabled . . . . : Yes&#10;    IPv6 Address. . . . . . . . . . . : 2001:db8:110:8f79:145:f180:fc4:8106(Preferred)&#10;    Link-local IPv6 Address . . . . . : fe80::83b:d647:4bed:d388%49(Preferred)&#10;    IPv4 Address. . . . . . . . . . . : 172.16.0.2(Preferred)&#10;    Subnet Mask . . . . . . . . . . . : 255.255.255.255&#10;    Default Gateway . . . . . . . . . :&#10;    DNS Servers . . . . . . . . . . . : 127.0.2.2&#10;    																		127.0.2.3&#10;    NetBIOS over Tcpip. . . . . . . . : Enabled&#10;</code></pre>
<h3 id="vnet-availability">VNET availability <span class="nb-badge">Beta</span></h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6246.md")
</div></details>
<p>By default, the Cloudflare One Client shows every <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">virtual network</a> (VNET) in your account in the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/#connect-to-a-virtual-network">VNET dropdown</a>. <strong>VNET availability</strong> restricts the dropdown to a subset of VNETs and chooses a default VNET on a per-<a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> basis. The active profile controls which VNETs devices can see and switch between.</p>
<p>For example, if your QA team uses a <code>staging-vnet</code> and your sales team should never reach it, you can assign the sales device profile to only include <code>production-vnet</code>. Sales users will not see <code>staging-vnet</code> in the dropdown.</p>
<h3 id="dns-search-suffixes">DNS search suffixes <span class="nb-badge">Beta</span></h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6247.md")
</div></details>
<p>A DNS search suffix (also known as a search domain) automatically appends a domain to single-label names so that users can type <code>jira</code> into a browser and the operating system resolves <code>jira.internal.example</code>. Search suffixes are typically advertised by the local network over DHCP, but devices connected to the Cloudflare One Client use the WARP virtual interface instead, which does not inherit network-advertised suffixes.</p>
<p>Use <strong>DNS search suffixes</strong> to deploy an ordered list of up to 25 suffixes to the Cloudflare One Client on a per-<a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> basis. The client appends each suffix in order to single-label name queries until one resolves successfully. This setting replaces the per-device manual configuration described in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/#add-a-dns-suffix">Add a DNS suffix</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Current versions of iOS do not allow LAN traffic to route through the WARP tunnel. Therefore, this feature is not needed on iOS.</li></ol></section>
