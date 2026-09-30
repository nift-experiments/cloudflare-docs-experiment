---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/changelog/
  description: Review recent changes to Cloudflare WAN (formerly Magic WAN).
  full_title: Changelog · Cloudflare WAN docs
  head_html: <title>Changelog · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Review recent changes to Cloudflare WAN (formerly Magic WAN)."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/changelog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/changelog/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/cloudflare-wan/changelog/index.xml"><meta property="og:title" content="Changelog · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review recent changes to Cloudflare WAN (formerly Magic WAN)."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/changelog/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/cloudflare-wan/changelog/#page","headline":"Changelog \u00b7 Cloudflare WAN docs","description":"Review recent changes to Cloudflare WAN (formerly Magic WAN).","url":"https://developers.cloudflare.com/cloudflare-wan/changelog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/changelog/
  schema: 1
---
<h2 id="2026-09-02">2026-09-02</h2>

<strong>Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard</strong>

<p>You can now define <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#create-edit-or-delete-a-custom-application">custom applications</a> for <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">breakout</a> and <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">prioritized</a> traffic on the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> directly from the dashboard, without calling the API.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-09-01-appliance-custom-application-traffic-steering.gif" alt="Adding a custom application by hostname, IP subnet, and source subnet from the Traffic Steering tab of an appliance profile" /></p>
<ul>
<li>In <strong>Traffic Steering</strong> &gt; <strong>Breakout traffic</strong> or <strong>Prioritized traffic</strong>, select <strong>Assign application traffic</strong> &gt; <strong>Add</strong> to create a custom application matched by <strong>Hostnames</strong>, <strong>IP subnets</strong>, and/or the new <strong>Source subnets</strong> field, alongside Cloudflare-managed applications.</li>
<li>Edit or delete an existing custom application from the same panel, no API round-trip required.</li>
<li><strong>Source subnets</strong> lets you match traffic by its source IP range, complementing the existing <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source">source LAN interface breakout criteria</a>.</li>
</ul>
<p>This complements the existing API and Terraform workflow for managing applications.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">Breakout traffic</a> and <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">Prioritized traffic</a>.</p>


<h2 id="2026-09-02-1">2026-09-02</h2>

<strong>Configure DHCP options from the dashboard on Cloudflare One Appliance</strong>

<p>You can now configure <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">custom DHCP options</a> directly from the dashboard when the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> is acting as the DHCP server for a LAN.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-09-01-appliance-dhcp-options-ui.gif" alt="Adding a custom DHCP option to a LAN's DHCP server from the Network Configuration tab of an appliance profile" /></p>
<ul>
<li>In <strong>LAN configuration</strong>, under <strong>DHCP server options</strong>, select <strong>Add DHCP option</strong> to choose from common options for PXE / iPXE boot, VoIP phone provisioning, and vendor-specific configuration, or select <strong>Add custom option</strong> to enter your own option code, type, and value.</li>
<li>This complements the existing <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/#configure-dhcp-options">API and Terraform workflow</a> for configuring DHCP options.</li>
</ul>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">DHCP server options</a>.</p>


<h2 id="2026-09-02-2">2026-09-02</h2>

<strong>Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once</strong>

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


<h2 id="2026-08-24">2026-08-24</h2>

<strong>Download the Cloudflare One Virtual Appliance for your hypervisor from the dashboard</strong>

<p>When you register a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Virtual Appliance</a>, you can now select your hypervisor and download the appliance directly from the dashboard — no need to look up asset URLs.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-08-24-virtual-appliance-self-serve-download.png" alt="Selecting a hypervisor and downloading the Cloudflare One Virtual Appliance from the Connectors page" /></p>
<ul>
<li>On the <strong>Connectors</strong> page, select <strong>Add an appliance</strong>, choose <strong>Virtual appliance</strong>, then select your hypervisor: <strong>VMware ESXi</strong>, <strong>Proxmox</strong>, or <strong>libvirt/KVM</strong>.</li>
<li>Download the OVA image (VMware ESXi) or the install script (Proxmox and libvirt/KVM) for the selected hypervisor.</li>
<li>Use <strong>View setup guide</strong> to open deployment instructions for your platform.</li>
</ul>
<p>This complements the existing self-serve <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key">registration and license key generation</a> in the dashboard.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#configure-a-virtual-machine">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="2026-08-19">2026-08-19</h2>

<strong>Threat Intel Lists supported in Unified Routing</strong>

<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> Threat Intel Lists are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. This feature requires a Cloudflare Advanced Network Firewall subscription.</p>
<p>Support for additional features - Rate Limiting and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="2026-07-17">2026-07-17</h2>

<strong>Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard</strong>

<p>You can now restart, reboot, or shut down a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> directly from the dashboard or via API.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-07-17-appliance-restart-reboot-shutdown.gif" alt="Restarting a Cloudflare One Appliance from the Operations section of the Edit Appliance page" /></p>
<ul>
<li><strong>Restart</strong> — Restart managed services. Purges temporary and (optionally) persistent state.</li>
<li><strong>Reboot</strong> — Power cycle the appliance. Optionally, purge persistent state. Re-applies configuration starting from scratch.</li>
<li><strong>Shutdown</strong> — Power off the appliance. Optionally, purge persistent state. The machine will be offline until manually powered on again.</li>
</ul>
<p>In the dashboard, go to <strong>Networking</strong> &gt; <strong>Connectors</strong> &gt; <strong>Appliances</strong>, select an appliance, then <strong>Edit</strong> &gt; <strong>Operations</strong> to send an operation. Via API, <code>POST</code> to the <code>/accounts/{account_id}/magic/connectors/{connector_id}/interrupts</code> endpoint.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/">Appliance operations</a>.</p>


<h2 id="2026-07-08">2026-07-08</h2>

<strong>IPsec downgrade protection (beta)</strong>

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


<h2 id="2026-07-08-1">2026-07-08</h2>

<strong>IP lists, IDS, and SIP rules supported in Unified Routing</strong>

<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> IP lists, IDS, and SIP rules are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. These features require a Cloudflare Advanced Network Firewall subscription.</p>
<p>Support for additional features - Threat Intel Lists, Rate Limiting, and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="2026-07-06">2026-07-06</h2>

<strong>Self-serve registration of Cloudflare One Virtual Appliance in the dashboard</strong>

<p>You can now register a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Virtual Appliance</a> and generate its license key directly from the dashboard, without contacting your account team.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-07-06-virtual-appliance-self-serve-ui.gif" alt="Registering a Cloudflare One Virtual Appliance and generating its authentication key from the Connectors page" /></p>
<ul>
<li>On the <strong>Connectors</strong> page, select <strong>Add an appliance</strong> and choose <strong>Virtual appliance</strong> to register a virtual appliance and generate its authentication key.</li>
<li>Use <strong>Regenerate authentication key</strong> from a virtual appliance connector's menu to rotate its key. The previous key is immediately and irrevocably revoked.</li>
<li>The authentication key is shown only once — copy and store it securely.</li>
</ul>
<p>This complements the existing <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key">API and Terraform self-serve workflow</a> for provisioning virtual appliances. Hardware appliances continue to use the existing account-team fulfillment workflow.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="2026-06-19">2026-06-19</h2>

<strong>Manage all your routes from one page in the dashboard</strong>

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


<h2 id="2026-06-02">2026-06-02</h2>

<strong>Cisco IOS XE</strong>

<p>The Cisco IOS XE third-party integration guide for Cloudflare WAN has been updated to include:</p>
<ul>
<li>Post Quantum Cryptography (PQC)</li>
<li>Policy-Based Routing (PBR)</li>
<li>IP Service Level Agreement (IP SLA)</li>
</ul>
<p>This link will take you directly to the updated <a href="/cloudflare-wan/configuration/third-party/cisco-ios-xe/">Cisco IOS XE</a> guide.</p>


<h2 id="2026-05-18">2026-05-18</h2>

<strong>Network Analytics support for Unified Routing</strong>

<p><a href="/analytics/network-analytics/">Network Analytics</a> is now fully supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. Traffic that traverses Unified Routing onramps and offramps is now visible in Network Analytics with the same dimensions and filters as traffic on the standard data plane.</p>
<p>This closes a parity gap for customers who had moved tunnels onto Unified Routing and lost visibility into their dataplane traffic in the Network Analytics dashboard. No configuration change is required — analytics data is collected automatically for all accounts with Unified Routing enabled.</p>
<p>For the remaining beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="2026-05-12">2026-05-12</h2>

<strong>New accounts assigned a single IPv4 anycast address</strong>

<p>New Magic Transit and Cloudflare WAN accounts are now assigned a single IPv4 anycast address by default.</p>
<p>Cloudflare handles failures on its network automatically by advertising your endpoint IP from multiple nodes across many globally distributed data centers. To handle failures on your network, configure two tunnels from separate routers.</p>
<p>To request additional anycast IP addresses for your account, contact your account team.</p>
<p>For tunnel configuration guidance, refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a> for Cloudflare WAN or <a href="/magic-transit/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a> for Magic Transit.</p>


<h2 id="2026-05-11">2026-05-11</h2>

<strong>NAT-T support for IKE on UDP port 500</strong>

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


<h2 id="2026-05-07">2026-05-07</h2>

<strong>Custom DHCP options on Cloudflare One Appliance</strong>

<p>When the Cloudflare One Appliance is acting as the DHCP server for a LAN, you can now configure custom DHCP options on the leases it issues. This unlocks workflows such as PXE / iPXE boot, VoIP phone provisioning, and vendor-specific client configuration.</p>
<p>Each option is defined by <code>option_number</code>, <code>value</code>, and one of four value types: <code>text</code>, <code>integer</code>, <code>hex</code>, or <code>ip</code>. Configurations are validated on the appliance before being applied — invalid configurations are rejected and the underlying error is returned to the API caller, so a bad option will not disrupt the live DHCP service.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">DHCP server options</a>.</p>


<h2 id="2026-05-07-1">2026-05-07</h2>

<strong>Source-based breakout and prioritization on Cloudflare One Appliance</strong>

<p>Breakout and traffic prioritization rules on the Cloudflare One Appliance can now match by <strong>source</strong> in addition to destination application. You can pin breakout or priority behavior to:</p>
<ul>
<li>A source LAN interface — VLANs attached to that LAN are included automatically.</li>
<li>A source IP address, range, or CIDR block.</li>
</ul>
<p>This is the natural way to break out a guest VLAN to the local Internet, or to prioritize traffic from a specific subnet, without enumerating destination applications.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source">Breakout traffic</a>.</p>


<h2 id="2026-05-07-2">2026-05-07</h2>

<strong>Self-serve provisioning of Cloudflare One Virtual Appliance via API</strong>

<p>You can now create, rotate, and delete Cloudflare One Virtual Appliance instances and their license keys directly via the API and Terraform.</p>
<ul>
<li>Create a virtual appliance and receive a license key: <code>POST /accounts/{account_id}/magic/connectors</code> with <code>device.provision_license: true</code>.</li>
<li>Rotate the license key for an existing virtual appliance: <code>PATCH /accounts/{account_id}/magic/connectors/{connector_id}</code> with <code>provision_license: true</code>. The previous key is immediately and irrevocably revoked.</li>
<li>Delete a virtual appliance to release the associated licensed device.</li>
</ul>
<p>The license key is returned in the response only once, at create or rotate time. Copy and store it securely.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="2026-04-30">2026-04-30</h2>

<strong>Post-quantum IPsec interoperability with third-party devices</strong>

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


<h2 id="2026-04-21">2026-04-21</h2>

<strong>Country rules supported in Unified Routing</strong>

<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> Country rules are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. This feature requires a Cloudflare Advanced Network Firewall subscription.</p>
<p>You can create firewall rules that match traffic based on source or destination country to enforce geographic access policies across your network.</p>
<p>This is the first of the Cloudflare Advanced Network Firewall features to become available in Unified Routing. Support for additional features - IP Lists, ASN Lists, Threat Intel Lists, IDS, Rate Limiting, SIP, and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="2026-04-07">2026-04-07</h2>

<strong>Link aggregation (LACP) support for Cloudflare One Appliance</strong>

<p>Cloudflare One Appliance now supports Link Aggregation Control Protocol (LACP), allowing you to bundle up to six physical LAN ports into a single logical interface. Link aggregation increases available bandwidth and eliminates single points of failure on the LAN side of the appliance.</p>
<p>This feature is available in beta on physical appliance hardware with the latest OS. No entitlement is required.</p>
<p>To configure a Link Aggregation Group, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/link-aggregation/">Configure link aggregation groups</a>.</p>


<h2 id="2026-02-17">2026-02-17</h2>

<strong>Cloudflare One Product Name Updates</strong>

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


<h2 id="2026-02-12">2026-02-12</h2>

<strong>Anycast IPs displayed on the dashboard</strong>

<p>Cloudflare WAN now displays your Anycast IP addresses directly in the dashboard when you configure IPsec or GRE tunnels.</p>
<p>Previously, customers received their Anycast IPs during onboarding or had to retrieve them with an API call. The dashboard now pre-loads these addresses, reducing setup friction and preventing configuration errors.</p>
<p>No action is required. All Cloudflare WAN customers can see their Anycast IPs in the tunnel configuration form automatically.</p>
<p>For more information, refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a>.</p>


<h2 id="2026-02-11">2026-02-11</h2>

<strong>Post-quantum encryption support for Cloudflare One Appliance</strong>

<p>Cloudflare One Appliance version 2026.2.0 adds <a href="/ssl/post-quantum-cryptography/">post-quantum encryption</a> support using hybrid ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).</p>
<p>The appliance now uses TLS 1.3 with hybrid ML-KEM for its connection to the Cloudflare edge. During the TLS handshake, the appliance and the edge share a symmetric secret over the TLS connection and inject it into the ESP layer of IPsec. This protects IPsec data plane traffic against harvest-now, decrypt-later attacks.</p>
<p>This upgrade deploys automatically to all appliances during their configured interrupt windows with no manual action required.</p>
<p>For more information, refer to <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a>.</p>


<h2 id="2026-01-30">2026-01-30</h2>

<strong>BGP over GRE and IPsec tunnels</strong>

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


<h2 id="2026-01-27">2026-01-27</h2>

<strong>Configure Cloudflare source IPs (beta)</strong>

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


<h2 id="2026-01-15">2026-01-15</h2>

<strong>Network Services navigation update</strong>

<p>The Network Services menu structure in Cloudflare's dashboard has been updated to reflect solutions and capabilities instead of product names. This will make it easier for you to find what you need and better reflects how our services work together.</p>
<p>Your existing configurations will remain the same, and you will have access to all of the same features and functionality.</p>
<p>The changes visible in your dashboard may vary based on the products you use. Overall, changes relate to <a href="https://developers.cloudflare.com/magic-transit/">Magic Transit</a>, <a href="https://developers.cloudflare.com/magic-wan/">Magic WAN</a>, and <a href="https://developers.cloudflare.com/cloudflare-network-firewall/">Magic Firewall</a>.</p>
<p><strong>Summary of changes:</strong></p>
<ul>
<li>A new <strong>Overview</strong> page provides access to the most common tasks across Magic Transit and Magic WAN.</li>
<li>Product names have been removed from top-level navigation.</li>
<li>Magic Transit and Magic WAN configuration is now organized under <strong>Routes</strong> and <strong>Connectors</strong>. For example, you will find IP Prefixes under <strong>Routes</strong>, and your GRE/IPsec Tunnels under <strong>Connectors.</strong></li>
<li>Magic Firewall policies are now called <strong>Firewall Policies.</strong></li>
<li>Magic WAN Connectors and Connector On-Ramps are now referenced in the dashboard as <strong>Appliances</strong> and <strong>Appliance profiles.</strong> They can be found under <strong>Connectors &gt; Appliances.</strong></li>
<li>Network analytics, network health, and real-time analytics are now available under <strong>Insights.</strong></li>
<li>Packet Captures are found under <strong>Insights &gt; Diagnostics.</strong></li>
<li>You can manage your Sites from <strong>Insights &gt; Network health.</strong></li>
<li>You can find Magic Network Monitoring under <strong>Insights &gt; Network flow</strong>.</li>
</ul>
<p>If you would like to provide feedback, complete <a href="https://forms.gle/htWyjRsTjw1usdis5">this form</a>. You can also find these details in the January 7, 2026 email titled <strong>[FYI] Upcoming Network Services Dashboard Navigation Update</strong>.</p>
<p>Preview:
<img src="/assets/upstream/images/changelog/cloudflare-network-firewall/networking-overview-and-navigation.png" alt="Networking Navigation" /></p>


<h2 id="2025-12-31">2025-12-31</h2>

<strong>Breakout traffic visibility via NetFlow</strong>

<p>Magic WAN Connector now exports NetFlow data for breakout traffic to Magic Network Monitoring (MNM), providing visibility into traffic that bypasses Cloudflare's security filtering.</p>
<p>This feature allows you to:</p>
<ul>
<li>Monitor breakout traffic statistics in the Cloudflare dashboard.</li>
<li>View traffic patterns for applications configured to bypass Cloudflare.</li>
<li>Maintain visibility across all traffic passing through your Magic WAN Connector.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-wan/analytics/netflow-analytics/">NetFlow statistics</a>.</p>


<h2 id="2025-11-06">2025-11-06</h2>

<strong>Automatic Return Routing (Beta)</strong>

<p>Magic WAN now supports Automatic Return Routing (ARR), allowing customers to configure Magic on-ramps (IPsec/GRE/CNI) to learn the return path for traffic flows without requiring static routes.</p>
<p>Key benefits:</p>
<ul>
<li><strong>Route-less mode</strong>: Static or dynamic routes are optional when using ARR.</li>
<li><strong>Overlapping IP space support</strong>: Traffic originating from customer sites can use overlapping private IP ranges.</li>
<li><strong>Symmetric routing</strong>: Return traffic is guaranteed to use the same connection as the original on-ramp.</li>
</ul>
<p>This feature is currently in beta and requires the new Unified Routing mode (beta).</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-automatic-return-routing-beta">Configure Automatic Return Routing</a>.</p>


<h2 id="2025-11-06-1">2025-11-06</h2>

<strong>Designate WAN link for breakout traffic</strong>

<p>Magic WAN Connector now allows you to designate a specific WAN port for breakout traffic, giving you deterministic control over the egress path for latency-sensitive applications.</p>
<p>With this feature, you can:</p>
<ul>
<li>Pin breakout traffic for specific applications to a preferred WAN port.</li>
<li>Ensure critical traffic (such as Zoom or Teams) always uses your fastest or most reliable connection.</li>
<li>Benefit from automatic failover to standard WAN port priority if the preferred port goes down.</li>
</ul>
<p>This is useful for organizations with multiple ISP uplinks who need predictable egress behavior for performance-sensitive traffic.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#designate-wan-ports-for-breakout-apps">Designate WAN ports for breakout apps</a>.</p>


<h2 id="2025-09-11">2025-09-11</h2>

<strong>DNS filtering for private network onramps</strong>

<p><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/#dns-filtering">Magic WAN</a> and <a href="/mesh/features/routes/#dns-filtering">WARP Connector</a> users can now securely route their DNS traffic to the Gateway resolver without exposing traffic to the public Internet.</p>
<p>Routing DNS traffic to the Gateway resolver allows DNS resolution and filtering for traffic coming from private networks while preserving source internal IP visibility. This ensures Magic WAN users have full integration with our Cloudflare One features, including <a href="/cloudflare-one/traffic-policies/resolver-policies/#internal-dns">Internal DNS</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites">hostname-based policies</a>.</p>
<p>To configure DNS filtering, change your Magic WAN or WARP Connector DNS settings to use Cloudflare's shared resolver IPs, <code>172.64.36.1</code> and <code>172.64.36.2</code>. Once you configure DNS resolution and filtering, you can use <em>Source Internal IP</em> as a traffic selector in your <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> for routing private DNS traffic to your <a href="/dns/internal-dns/">Internal DNS</a>.</p>


<h2 id="2025-09-08">2025-09-08</h2>

<strong>Custom IKE ID for IPsec Tunnels</strong>

<p>Now, Magic WAN customers can configure a custom IKE ID for their IPsec tunnels. Customers that are using Magic WAN and a VeloCloud SD-WAN device together can utilize this new feature to create a high availability configuration.</p>
<p>This feature is available via API only. Customers can read the Magic WAN documentation to learn more about the <a href="/cloudflare-wan/configuration/common-settings/custom-ike-id-ipsec/">Custom IKE ID feature and the API call to configure it</a>.</p>


<h2 id="2025-09-05">2025-09-05</h2>

<strong>Bidirectional tunnel health checks are compatible with all Magic on-ramps</strong>

<p>All bidirectional tunnel health check return packets are accepted by any Magic on-ramp.</p>
<p>Previously, when a Magic tunnel had a bidirectional health check configured, the bidirectional health check would pass when the return packets came back to Cloudflare over the same tunnel that was traversed by the forward packets.</p>
<p>There are SD-WAN devices, like VeloCloud, that do not offer controls to steer traffic over one tunnel versus another in a high availability tunnel configuration.</p>
<p>Now, when a Magic tunnel has a bidirectional health check configured, the bidirectional health check will pass when the return packet traverses over any tunnel in a high availability configuration.</p>


<h2 id="2025-07-31">2025-07-31</h2>

<strong>Terraform V5 support for tunnels and routes</strong>

<p>The Cloudflare Terraform provider resources for Cloudflare WAN tunnels and routes now support Terraform provider version 5. Customers using infrastructure-as-code workflows can manage their tunnel and route configuration with the latest provider version.</p>
<p>For more information, refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider documentation</a>.</p>


<h2 id="2025-07-30">2025-07-30</h2>

<strong>Magic Transit and Magic WAN health check data is fully compatible with the CMB EU setting.</strong>

<p>Today, we are excited to announce that all Magic Transit and Magic WAN customers with CMB EU (<a href="/data-localization/metadata-boundary/">Customer Metadata Boundary - Europe</a>) enabled in their account will be able to access GRE, IPsec, and CNI health check and traffic volume data in the Cloudflare dashboard and via API.</p>
<p>This ensures that all Magic Transit and Magic WAN customers with CMB EU enabled will be able to access all Magic Transit and Magic WAN features.</p>
<p>Specifically, these two GraphQL endpoints are now compatible with CMB EU:</p>
<ul>
<li><code>magicTransitTunnelHealthChecksAdaptiveGroups</code></li>
<li><code>magicTransitTunnelTrafficAdaptiveGroups</code></li>
</ul>


<h2 id="2025-07-21">2025-07-21</h2>

<strong>Virtual Cloudflare One Appliance with KVM support (open beta)</strong>

<p>The KVM-based virtual Cloudflare One Appliance is now in open beta with official support for Proxmox VE.</p>
<p>Customers can deploy the virtual appliance on KVM hypervisors to connect branch or data center networks to Cloudflare WAN without dedicated hardware.</p>
<p>For setup instructions, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a virtual Cloudflare One Appliance</a>.</p>


<h2 id="2025-04-30">2025-04-30</h2>

<strong>Cloudflare One Appliance supports multiple DNS server IPs</strong>

<p>Cloudflare One Appliance DHCP server settings now support specifying multiple DNS server IP addresses in the DHCP pool.</p>
<p>Previously, customers could only configure a single DNS server per DHCP pool. With this update, you can specify multiple DNS servers to provide redundancy for clients at branch locations.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/">DHCP server</a>.</p>


<h2 id="2025-02-14-1">2025-02-14</h2>

<strong>Configure your Magic WAN Connector to connect via static IP assignment</strong>

<p>You can now locally configure your <a href="/cloudflare-wan/configuration/appliance/">Magic WAN Connector</a> to work in a static IP configuration.</p>
<p>This local method does not require having access to a DHCP Internet connection. However, it does require being comfortable with using tools to access the serial port on Magic WAN Connector as well as using a serial terminal client to access the Connector's environment.</p>
<p>For more details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#bootstrap-via-serial-console">WAN with a static IP address</a>.</p>


<h2 id="2024-12-17-2">2024-12-17</h2>

<strong>Establish BGP peering over Direct CNI circuits</strong>

<p>Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using a Direct CNI on-ramp.</p>
<p>Using BGP peering allows customers to:</p>
<ul>
<li>Automate the process of adding or removing networks and subnets.</li>
<li>Take advantage of failure detection and session recovery features.</li>
</ul>
<p>With this functionality, customers can:</p>
<ul>
<li>Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via CNI.</li>
<li>Secure the session by MD5 authentication to prevent misconfigurations.</li>
<li>Exchange routes dynamically between their devices and their Magic routing table.</li>
</ul>
<p>Refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes">Magic WAN BGP peering</a> or <a href="/magic-transit/how-to/configure-routes/#configure-bgp-routes">Magic Transit BGP peering</a> to learn more about this feature and how to set it up.</p>


<h2 id="2025-02-14">2025-02-14</h2>
<p><strong>Sites feature available to all Magic WAN customers</strong></p>
<p>All Magic WAN customers now have full access to the Magic WAN sites feature. Customers can configure a Magic WAN site either with or without a Magic WAN connector.</p>
<h2 id="2024-12-17">2024-12-17</h2>
<p><strong>Magic WAN Connector configurable health checks</strong></p>
<p>Health check rate on Magic WAN Connector IPsec tunnels are now configurable.</p>
<h2 id="2024-12-17-1">2024-12-17</h2>
<p><strong>BGP support for Cloudflare Network Interconnect (CNI)</strong></p>
<p>Magic WAN customers can now establish BGP peering over Direct CNI circuits. Customers can now dynamically exchange routes and path availability status between their router device and the Magic WAN table.</p>
<h2 id="2024-12-12">2024-12-12</h2>
<p><strong>LAN Policy improvements for the Magic WAN Connector</strong></p>
<p>Magic WAN Connector LAN Policy now supports unidirectional traffic flows and port-ranges.</p>
<h2 id="2024-10-01">2024-10-01</h2>
<p><strong>Early access testing for BGP on CNI 2.0 circuits</strong></p>
<p>Customers can exchange routes dynamically with their Magic virtual network overlay via Direct CNI or Cloud CNI based connectivity.</p>
<h2 id="2024-09-27">2024-09-27</h2>
<p><strong>Magic WAN Connector sends Cloudflare One Client traffic to Internet</strong></p>
<p>All Magic WAN Connectors now route Cloudflare One Client traffic directly to the Internet, bypassing IPsec tunneling, to prevent double encapsulation of Cloudflare One Client traffic.</p>
<h2 id="2024-07-17">2024-07-17</h2>
<p><strong>Updates to High Availability on the Magic WAN Connector</strong></p>
<p>The High Availability feature on Magic WAN Connector now supports additional failover conditions, DHCP lease syncing, and staggered upgrades.</p>
<h2 id="2024-06-23">2024-06-23</h2>
<p><strong>ICMP support for traffic sourced from private IPs</strong></p>
<p>Magic WAN will now support ICMP traffic sourced from private IPs going to the Internet via Gateway.</p>
<h2 id="2024-06-05">2024-06-05</h2>
<p><strong>Application based prioritization</strong></p>
<p>The Magic WAN Connector can now prioritize traffic on a per-application basis.</p>
<h2 id="2024-05-31">2024-05-31</h2>
<p><strong>virtual IP addresses</strong></p>
<p>Customers using Gateway to filter traffic to Magic WAN destinations will now see traffic from Cloudflare egressing with the Cloudflare One Client virtual IP addresses (CGNAT range), rather than public Cloudflare IP addresses. This simplifies configuration and improves visibility for customers.</p>
<h2 id="2024-01-23">2024-01-23</h2>
<p><strong>Network segmentation</strong></p>
<p>You can define policies in your Connector to either allow traffic to flow between your LANs without it leaving your local premises or to forward it via the Cloudflare network where you can add additional security features.</p>


