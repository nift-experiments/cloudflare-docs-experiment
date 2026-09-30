---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/cloudflare-wan/
  description: '2026-09-02'
  full_title: cloudflare-wan changelog | Cloudflare Docs
  head_html: <title>cloudflare-wan changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-02"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/cloudflare-wan/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cloudflare-wan changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-02"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/cloudflare-wan/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/cloudflare-wan/#page","headline":"cloudflare-wan changelog | Cloudflare Docs","description":"2026-09-02","url":"https://developers.cloudflare.com/changelog/product/cloudflare-wan/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/cloudflare-wan/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="define-custom-applications-for-breakout-and-prioritized-traffic-from-the-cloudflare-one-appliance-dashboard"><a href="/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/">Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard</a></h2>
<p><em>2026-09-02</em></p>
<p>You can now define <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#create-edit-or-delete-a-custom-application">custom applications</a> for <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">breakout</a> and <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">prioritized</a> traffic on the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> directly from the dashboard, without calling the API.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-09-01-appliance-custom-application-traffic-steering.gif" alt="Adding a custom application by hostname, IP subnet, and source subnet from the Traffic Steering tab of an appliance profile" /></p>
<ul>
<li>In <strong>Traffic Steering</strong> &gt; <strong>Breakout traffic</strong> or <strong>Prioritized traffic</strong>, select <strong>Assign application traffic</strong> &gt; <strong>Add</strong> to create a custom application matched by <strong>Hostnames</strong>, <strong>IP subnets</strong>, and/or the new <strong>Source subnets</strong> field, alongside Cloudflare-managed applications.</li>
<li>Edit or delete an existing custom application from the same panel, no API round-trip required.</li>
<li><strong>Source subnets</strong> lets you match traffic by its source IP range, complementing the existing <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source">source LAN interface breakout criteria</a>.</li>
</ul>
<p>This complements the existing API and Terraform workflow for managing applications.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">Breakout traffic</a> and <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">Prioritized traffic</a>.</p>


<h2 id="configure-dhcp-options-from-the-dashboard-on-cloudflare-one-appliance"><a href="/changelog/post/2026-09-02-appliance-dhcp-options-ui/">Configure DHCP options from the dashboard on Cloudflare One Appliance</a></h2>
<p><em>2026-09-02</em></p>
<p>You can now configure <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">custom DHCP options</a> directly from the dashboard when the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> is acting as the DHCP server for a LAN.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-09-01-appliance-dhcp-options-ui.gif" alt="Adding a custom DHCP option to a LAN's DHCP server from the Network Configuration tab of an appliance profile" /></p>
<ul>
<li>In <strong>LAN configuration</strong>, under <strong>DHCP server options</strong>, select <strong>Add DHCP option</strong> to choose from common options for PXE / iPXE boot, VoIP phone provisioning, and vendor-specific configuration, or select <strong>Add custom option</strong> to enter your own option code, type, and value.</li>
<li>This complements the existing <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/#configure-dhcp-options">API and Terraform workflow</a> for configuring DHCP options.</li>
</ul>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">DHCP server options</a>.</p>


<h2 id="create-multiple-cloudflare-tunnel-and-cloudflare-mesh-routes-at-once"><a href="/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/">Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once</a></h2>
<p><em>2026-09-02</em></p>
<p>You can now create multiple <a href="/tunnel/">Cloudflare Tunnel</a> and <a href="/mesh/">Cloudflare Mesh</a> routes from the Routes page in a single action, instead of submitting one route at a time.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/2026-09-01-tunnel-mesh-bulk.gif" alt="Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page" /></p>
<p>When creating a route, you can now:</p>
<ul>
<li><strong>Add multiple destinations at once</strong> — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.</li>
<li><strong>Queue up multiple routes</strong> — Select <strong>Add another</strong> to stage additional routes, including different types or connectors, before creating them all in one action.</li>
<li><strong>Retry only what failed</strong> — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.</li>
</ul>
<p>The same Routes UI already supports bulk creation for <a href="/cloudflare-wan/">Cloudflare WAN</a> static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.</p>
<div class="nb-dash-button"></div>
<p>For setup steps, refer to <a href="/cloudflare-one/networks/routes/add-routes/">Add routes</a>.</p>


<h2 id="download-the-cloudflare-one-virtual-appliance-for-your-hypervisor-from-the-dashboard"><a href="/changelog/post/2026-08-24-virtual-appliance-self-serve-download/">Download the Cloudflare One Virtual Appliance for your hypervisor from the dashboard</a></h2>
<p><em>2026-08-24</em></p>
<p>When you register a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Virtual Appliance</a>, you can now select your hypervisor and download the appliance directly from the dashboard — no need to look up asset URLs.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-08-24-virtual-appliance-self-serve-download.png" alt="Selecting a hypervisor and downloading the Cloudflare One Virtual Appliance from the Connectors page" /></p>
<ul>
<li>On the <strong>Connectors</strong> page, select <strong>Add an appliance</strong>, choose <strong>Virtual appliance</strong>, then select your hypervisor: <strong>VMware ESXi</strong>, <strong>Proxmox</strong>, or <strong>libvirt/KVM</strong>.</li>
<li>Download the OVA image (VMware ESXi) or the install script (Proxmox and libvirt/KVM) for the selected hypervisor.</li>
<li>Use <strong>View setup guide</strong> to open deployment instructions for your platform.</li>
</ul>
<p>This complements the existing self-serve <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key">registration and license key generation</a> in the dashboard.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#configure-a-virtual-machine">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="threat-intel-lists-supported-in-unified-routing"><a href="/changelog/post/2026-08-19-unified-routing-threat-lists/">Threat Intel Lists supported in Unified Routing</a></h2>
<p><em>2026-08-19</em></p>
<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> Threat Intel Lists are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. This feature requires a Cloudflare Advanced Network Firewall subscription.</p>
<p>Support for additional features - Rate Limiting and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="restart-reboot-or-shut-down-a-cloudflare-one-appliance-from-the-dashboard"><a href="/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/">Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard</a></h2>
<p><em>2026-07-17</em></p>
<p>You can now restart, reboot, or shut down a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> directly from the dashboard or via API.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-07-17-appliance-restart-reboot-shutdown.gif" alt="Restarting a Cloudflare One Appliance from the Operations section of the Edit Appliance page" /></p>
<ul>
<li><strong>Restart</strong> — Restart managed services. Purges temporary and (optionally) persistent state.</li>
<li><strong>Reboot</strong> — Power cycle the appliance. Optionally, purge persistent state. Re-applies configuration starting from scratch.</li>
<li><strong>Shutdown</strong> — Power off the appliance. Optionally, purge persistent state. The machine will be offline until manually powered on again.</li>
</ul>
<p>In the dashboard, go to <strong>Networking</strong> &gt; <strong>Connectors</strong> &gt; <strong>Appliances</strong>, select an appliance, then <strong>Edit</strong> &gt; <strong>Operations</strong> to send an operation. Via API, <code>POST</code> to the <code>/accounts/{account_id}/magic/connectors/{connector_id}/interrupts</code> endpoint.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/">Appliance operations</a>.</p>


<h2 id="ipsec-downgrade-protection-beta"><a href="/changelog/post/2026-07-08-ipsec-downgrade-protection/">IPsec downgrade protection (beta)</a></h2>
<p><em>2026-07-08</em></p>
<p>Cloudflare IPsec now supports the <a href="https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-downgrade-prevention/"><code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code></a> IKEv2 extension to protect against downgrade attacks on IPsec tunnels.</p>
<p>IKEv2's original authentication design has each endpoint sign only its own outbound messages, not the full handshake transcript. A quantum-capable <a href="https://www.cloudflare.com/learning/security/threats/on-path-attack/">on-path attacker</a> can exploit this to bypass post-quantum key exchange by downgrading the connection to classical cryptography. The <code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code> extension addresses this by having both peers sign the entire handshake transcript during the authentication exchange, preventing an attacker from manipulating the negotiation without detection.</p>
<p>Key details:</p>
<ul>
<li>Available in beta for Cloudflare WAN and Magic Transit IPsec tunnels.</li>
<li>Cloudflare sends the <code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code> notification unconditionally as a responder when the feature flag is enabled.</li>
<li>Both the initiator (your device) and responder (Cloudflare) must support the extension for downgrade protection to be effective.</li>
<li>This feature is currently gated by a per-account feature flag. Contact your account team to turn it on.</li>
</ul>
<p>Refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#improved-downgrade-protection-beta">Downgrade protection</a> for more details.</p>


<h2 id="ip-lists-ids-and-sip-rules-supported-in-unified-routing"><a href="/changelog/post/2026-07-08-unified-routing-iplist-ids-sip/">IP lists, IDS, and SIP rules supported in Unified Routing</a></h2>
<p><em>2026-07-08</em></p>
<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> IP lists, IDS, and SIP rules are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. These features require a Cloudflare Advanced Network Firewall subscription.</p>
<p>Support for additional features - Threat Intel Lists, Rate Limiting, and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="self-serve-registration-of-cloudflare-one-virtual-appliance-in-the-dashboard"><a href="/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/">Self-serve registration of Cloudflare One Virtual Appliance in the dashboard</a></h2>
<p><em>2026-07-06</em></p>
<p>You can now register a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Virtual Appliance</a> and generate its license key directly from the dashboard, without contacting your account team.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-07-06-virtual-appliance-self-serve-ui.gif" alt="Registering a Cloudflare One Virtual Appliance and generating its authentication key from the Connectors page" /></p>
<ul>
<li>On the <strong>Connectors</strong> page, select <strong>Add an appliance</strong> and choose <strong>Virtual appliance</strong> to register a virtual appliance and generate its authentication key.</li>
<li>Use <strong>Regenerate authentication key</strong> from a virtual appliance connector's menu to rotate its key. The previous key is immediately and irrevocably revoked.</li>
<li>The authentication key is shown only once — copy and store it securely.</li>
</ul>
<p>This complements the existing <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key">API and Terraform self-serve workflow</a> for provisioning virtual appliances. Hardware appliances continue to use the existing account-team fulfillment workflow.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="manage-all-your-routes-from-one-page-in-the-dashboard"><a href="/changelog/post/2026-06-19-unified-routes-page/">Manage all your routes from one page in the dashboard</a></h2>
<p><em>2026-06-19</em></p>
<p>The <strong>Routes</strong> page in the Cloudflare dashboard now shows the routes across all of your connectors — <a href="/mesh/">Cloudflare Mesh</a> and <a href="/tunnel/">Cloudflare Tunnel</a> routes alongside <a href="/cloudflare-wan/">Cloudflare WAN</a> and <a href="/magic-transit/">Magic Transit</a> static routes — in a single table, instead of a separate routes view per product.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/2026-06-19-unified-routes.gif" alt="The unified Routes page in the Cloudflare dashboard, showing routes across connectors in a single table" /></p>
<p>From the unified Routes page you can:</p>
<ul>
<li><strong>Visualize your network with an interactive map</strong> that shows how your destinations flow through to your connectors — including equal-cost multi-path (ECMP) routes where the same prefix is served by several connectors. Select a node to filter the table down to the routes behind it.</li>
<li><strong>See every route in one table</strong>, with its destination, type, connector, priority, and source, and filter or sort to find what you need.</li>
<li><strong>Create, edit, and delete routes</strong> of any supported type without leaving the page. When adding a Cloudflare WAN or Magic Transit static route, you now pick the next hop by <strong>connector name</strong> instead of typing its IP.</li>
<li><strong>Manage <a href="/cloudflare-one/networks/virtual-networks/">virtual networks</a></strong> from a dedicated tab.</li>
<li><strong>Test a route</strong> to see which connector and next hop a destination resolves to before you commit a change.</li>
</ul>
<p>To find it, go to <strong>Networking</strong> &gt; <strong>Routes</strong> in the dashboard sidebar.</p>
<div class="nb-dash-button"></div>
<p>Your existing routes, APIs, and configurations are unchanged — this is a dashboard experience that brings them together in one place. Learn how to <a href="/cloudflare-one/networks/routes/add-routes/">add routes</a> and <a href="/cloudflare-one/networks/virtual-networks/">manage virtual networks</a>.</p>


<h2 id="cisco-ios-xe"><a href="/changelog/post/2026-06-02-cisco-ios-xe/">Cisco IOS XE</a></h2>
<p><em>2026-06-02</em></p>
<p>The Cisco IOS XE third-party integration guide for Cloudflare WAN has been updated to include:</p>
<ul>
<li>Post Quantum Cryptography (PQC)</li>
<li>Policy-Based Routing (PBR)</li>
<li>IP Service Level Agreement (IP SLA)</li>
</ul>
<p>This link will take you directly to the updated <a href="/cloudflare-wan/configuration/third-party/cisco-ios-xe/">Cisco IOS XE</a> guide.</p>


<h2 id="network-analytics-support-for-unified-routing"><a href="/changelog/post/2026-05-18-unified-routing-network-analytics/">Network Analytics support for Unified Routing</a></h2>
<p><em>2026-05-18</em></p>
<p><a href="/analytics/network-analytics/">Network Analytics</a> is now fully supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. Traffic that traverses Unified Routing onramps and offramps is now visible in Network Analytics with the same dimensions and filters as traffic on the standard data plane.</p>
<p>This closes a parity gap for customers who had moved tunnels onto Unified Routing and lost visibility into their dataplane traffic in the Network Analytics dashboard. No configuration change is required — analytics data is collected automatically for all accounts with Unified Routing enabled.</p>
<p>For the remaining beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="new-accounts-assigned-a-single-ipv4-anycast-address"><a href="/changelog/post/2026-05-12-single-anycast-ip-default/">New accounts assigned a single IPv4 anycast address</a></h2>
<p><em>2026-05-12</em></p>
<p>New Magic Transit and Cloudflare WAN accounts are now assigned a single IPv4 anycast address by default.</p>
<p>Cloudflare handles failures on its network automatically by advertising your endpoint IP from multiple nodes across many globally distributed data centers. To handle failures on your network, configure two tunnels from separate routers.</p>
<p>To request additional anycast IP addresses for your account, contact your account team.</p>
<p>For tunnel configuration guidance, refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a> for Cloudflare WAN or <a href="/magic-transit/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a> for Magic Transit.</p>


<h2 id="nat-t-support-for-ike-on-udp-port-500"><a href="/changelog/post/2026-05-11-nat-t-port-500/">NAT-T support for IKE on UDP port 500</a></h2>
<p><em>2026-05-11</em></p>
<p>Cloudflare IPsec now supports the standard NAT traversal (NAT-T) flow, where IKE begins on UDP port <code>500</code> and switches to UDP port <code>4500</code> after NAT is detected.</p>
<p>Previously, devices behind NAT had to be configured to initiate IKE on UDP port <code>4500</code> directly. Devices that started on UDP port <code>500</code> could not complete the IKE handshake when NAT was in the path. This required custom configuration on devices such as VeloCloud SD-WAN edges, Cisco IOS-XE routers, and Juniper SRX firewalls, and was not possible on every platform.</p>
<p>What changed:</p>
<ul>
<li>Devices behind NAT can now initiate IKE on either UDP port <code>500</code> or UDP port <code>4500</code>.</li>
<li>Devices that start IKE on UDP port <code>500</code> and switch to UDP port <code>4500</code> after NAT detection now complete the handshake successfully.</li>
<li>No configuration change is required on Cloudflare. The change is available for all IPsec tunnels on Cloudflare WAN and Magic Transit.</li>
</ul>
<p>This change does not affect existing tunnels:</p>
<ul>
<li>Tunnels using UDP port <code>500</code> with no NAT detected continue to operate as before.</li>
<li>Tunnels configured to start IKE on UDP port <code>4500</code> continue to operate as before.</li>
<li>NAT detection logic is unchanged.</li>
</ul>
<p>For configuration details, refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/">GRE and IPsec tunnels</a>.</p>


<h2 id="custom-dhcp-options-on-cloudflare-one-appliance"><a href="/changelog/post/2026-05-07-appliance-dhcp-options/">Custom DHCP options on Cloudflare One Appliance</a></h2>
<p><em>2026-05-07</em></p>
<p>When the Cloudflare One Appliance is acting as the DHCP server for a LAN, you can now configure custom DHCP options on the leases it issues. This unlocks workflows such as PXE / iPXE boot, VoIP phone provisioning, and vendor-specific client configuration.</p>
<p>Each option is defined by <code>option_number</code>, <code>value</code>, and one of four value types: <code>text</code>, <code>integer</code>, <code>hex</code>, or <code>ip</code>. Configurations are validated on the appliance before being applied — invalid configurations are rejected and the underlying error is returned to the API caller, so a bad option will not disrupt the live DHCP service.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">DHCP server options</a>.</p>


<h2 id="source-based-breakout-and-prioritization-on-cloudflare-one-appliance"><a href="/changelog/post/2026-05-07-appliance-source-based-breakout/">Source-based breakout and prioritization on Cloudflare One Appliance</a></h2>
<p><em>2026-05-07</em></p>
<p>Breakout and traffic prioritization rules on the Cloudflare One Appliance can now match by <strong>source</strong> in addition to destination application. You can pin breakout or priority behavior to:</p>
<ul>
<li>A source LAN interface — VLANs attached to that LAN are included automatically.</li>
<li>A source IP address, range, or CIDR block.</li>
</ul>
<p>This is the natural way to break out a guest VLAN to the local Internet, or to prioritize traffic from a specific subnet, without enumerating destination applications.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source">Breakout traffic</a>.</p>


<h2 id="self-serve-provisioning-of-cloudflare-one-virtual-appliance-via-api"><a href="/changelog/post/2026-05-07-virtual-appliance-self-serve-api/">Self-serve provisioning of Cloudflare One Virtual Appliance via API</a></h2>
<p><em>2026-05-07</em></p>
<p>You can now create, rotate, and delete Cloudflare One Virtual Appliance instances and their license keys directly via the API and Terraform.</p>
<ul>
<li>Create a virtual appliance and receive a license key: <code>POST /accounts/{account_id}/magic/connectors</code> with <code>device.provision_license: true</code>.</li>
<li>Rotate the license key for an existing virtual appliance: <code>PATCH /accounts/{account_id}/magic/connectors/{connector_id}</code> with <code>provision_license: true</code>. The previous key is immediately and irrevocably revoked.</li>
<li>Delete a virtual appliance to release the associated licensed device.</li>
</ul>
<p>The license key is returned in the response only once, at create or rotate time. Copy and store it securely.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="post-quantum-ipsec-interoperability-with-third-party-devices"><a href="/changelog/post/2026-04-30-ipsec-post-quantum-third-party/">Post-quantum IPsec interoperability with third-party devices</a></h2>
<p><em>2026-04-30</em></p>
<p>Cloudflare IPsec now supports post-quantum key agreement with compatible third-party devices. <a href="https://www.cisco.com/">Cisco</a> and <a href="https://www.fortinet.com/">Fortinet</a> are the first third-party vendors validated to interoperate with Cloudflare IPsec using ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).</p>
<p>Post-quantum IPsec uses <a href="https://datatracker.ietf.org/doc/rfc9370/">RFC 9370</a> and <a href="https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/">draft-ietf-ipsecme-ikev2-mlkem</a> to negotiate hybrid key agreement during the IKEv2 <code>IKE_INTERMEDIATE</code> phase. This combines classical Diffie-Hellman (Group 20) with ML-KEM-768 or ML-KEM-1024 to protect against <a href="https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later">harvest-now, decrypt-later</a> attacks.</p>
<p>Key details:</p>
<ul>
<li>Compatible with Cisco 8000 Series Secure Routers with IOS XR Release 26.1.1 and Fortinet FortiOS 7.6.6 and later.</li>
<li>Uses ML-KEM-768 or ML-KEM-1024 as an additional Key Exchange to DH Group 20.</li>
<li>Follows RFC 9370 and draft-ietf-ipsecme-ikev2-mlkem standards.</li>
<li>No additional licensing required.</li>
</ul>
<p>Post-quantum IPsec with third-party devices is now generally available with confirmed interoperability for the platforms listed above. Cloudflare intends to support interoperability with more vendors as they build out support for draft-ietf-ipsecme-ikev2-mlkem. Contact your account team to discuss support for additional vendors.</p>
<p>For supported key exchange methods and the list of validated platforms, refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#tested-third-party-vendor-interoperability">GRE and IPsec tunnels</a>.</p>


<h2 id="country-rules-supported-in-unified-routing"><a href="/changelog/post/2026-04-21-unified-routing-geoip-country-rules/">Country rules supported in Unified Routing</a></h2>
<p><em>2026-04-21T12:00:00</em></p>
<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> Country rules are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. This feature requires a Cloudflare Advanced Network Firewall subscription.</p>
<p>You can create firewall rules that match traffic based on source or destination country to enforce geographic access policies across your network.</p>
<p>This is the first of the Cloudflare Advanced Network Firewall features to become available in Unified Routing. Support for additional features - IP Lists, ASN Lists, Threat Intel Lists, IDS, Rate Limiting, SIP, and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="link-aggregation-lacp-support-for-cloudflare-one-appliance"><a href="/changelog/post/2026-04-07-link-aggregation-lacp-appliance/">Link aggregation (LACP) support for Cloudflare One Appliance</a></h2>
<p><em>2026-04-07</em></p>
<p>Cloudflare One Appliance now supports Link Aggregation Control Protocol (LACP), allowing you to bundle up to six physical LAN ports into a single logical interface. Link aggregation increases available bandwidth and eliminates single points of failure on the LAN side of the appliance.</p>
<p>This feature is available in beta on physical appliance hardware with the latest OS. No entitlement is required.</p>
<p>To configure a Link Aggregation Group, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/link-aggregation/">Configure link aggregation groups</a>.</p>


<h2 id="cloudflare-one-product-name-updates"><a href="/changelog/post/2026-02-17-product-name-updates/">Cloudflare One Product Name Updates</a></h2>
<p><em>2026-02-17</em></p>
<p>We are updating naming related to some of our Networking products to better clarify their place in the Zero Trust and Secure Access Service Edge (SASE) journey.</p>
<p>We are retiring some older brand names in favor of names that describe exactly what the products do within your network. We are doing this to help customers build better, clearer mental models for comprehensive SASE architecture delivered on Cloudflare.</p>
<h4 id="2026-02-17-product-name-updates-what-s-changing">What's changing</h4>
<ul>
<li><strong>Magic WAN</strong> → <strong>Cloudflare WAN</strong></li>
<li><strong>Magic WAN IPsec</strong> → <strong>Cloudflare IPsec</strong></li>
<li><strong>Magic WAN GRE</strong> → <strong>Cloudflare GRE</strong></li>
<li><strong>Magic WAN Connector</strong> → <strong>Cloudflare One Appliance</strong></li>
<li><strong>Magic Firewall</strong> → <strong>Cloudflare Network Firewall</strong></li>
<li><strong>Magic Network Monitoring</strong> → <strong>Network Flow</strong></li>
<li><strong>Magic Cloud Networking</strong> → <strong>Cloudflare One Multi-cloud Networking</strong></li>
</ul>
<p><strong>No action is required by you</strong> — all functionality, existing configurations, and billing will remain exactly the same.</p>
<p>For more information, visit the <a href="/cloudflare-one/">Cloudflare One documentation</a>.</p>


<h2 id="anycast-ips-displayed-on-the-dashboard"><a href="/changelog/post/2026-02-12-anycast-ips-on-dashboard/">Anycast IPs displayed on the dashboard</a></h2>
<p><em>2026-02-12</em></p>
<p>Cloudflare WAN now displays your Anycast IP addresses directly in the dashboard when you configure IPsec or GRE tunnels.</p>
<p>Previously, customers received their Anycast IPs during onboarding or had to retrieve them with an API call. The dashboard now pre-loads these addresses, reducing setup friction and preventing configuration errors.</p>
<p>No action is required. All Cloudflare WAN customers can see their Anycast IPs in the tunnel configuration form automatically.</p>
<p>For more information, refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a>.</p>


<h2 id="post-quantum-encryption-support-for-cloudflare-one-appliance"><a href="/changelog/post/2026-02-11-appliance-post-quantum-encryption/">Post-quantum encryption support for Cloudflare One Appliance</a></h2>
<p><em>2026-02-11</em></p>
<p>Cloudflare One Appliance version 2026.2.0 adds <a href="/ssl/post-quantum-cryptography/">post-quantum encryption</a> support using hybrid ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).</p>
<p>The appliance now uses TLS 1.3 with hybrid ML-KEM for its connection to the Cloudflare edge. During the TLS handshake, the appliance and the edge share a symmetric secret over the TLS connection and inject it into the ESP layer of IPsec. This protects IPsec data plane traffic against harvest-now, decrypt-later attacks.</p>
<p>This upgrade deploys automatically to all appliances during their configured interrupt windows with no manual action required.</p>
<p>For more information, refer to <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a>.</p>


<h2 id="bgp-over-gre-and-ipsec-tunnels"><a href="/changelog/post/2026-01-30-bgp-over-tunnels/">BGP over GRE and IPsec tunnels</a></h2>
<p><em>2026-01-30</em></p>
<p>Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using IPsec and GRE tunnel on-ramps (beta).</p>
<p>Using BGP peering allows customers to:</p>
<ul>
<li>Automate the process of adding or removing networks and subnets.</li>
<li>Take advantage of failure detection and session recovery features.</li>
</ul>
<p>With this functionality, customers can:</p>
<ul>
<li>Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via IPsec and GRE tunnel on-ramps.</li>
<li>Secure the session by MD5 authentication to prevent misconfigurations.</li>
<li>Exchange routes dynamically between their devices and their Magic routing table.</li>
</ul>
<p>For configuration details, refer to:</p>
<ul>
<li><a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes">Configure BGP routes for Magic WAN</a></li>
<li><a href="/magic-transit/how-to/configure-routes/#configure-bgp-routes">Configure BGP routes for Magic Transit</a></li>
</ul>


<h2 id="configure-cloudflare-source-ips-beta"><a href="/changelog/post/2026-01-27-configure-cloudflare-source-ips/">Configure Cloudflare source IPs (beta)</a></h2>
<p><em>2026-01-27</em></p>
<p>Cloudflare source IPs are the IP addresses used by Cloudflare services (such as Load Balancing, Gateway, and Browser Isolation) when sending traffic to your private networks.</p>
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


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 2</span><a class="pagination-next" rel="next" href="/changelog/product/cloudflare-wan/2/">Next</a></nav>
