---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/cloudflare-one-appliance/
  description: '2026-09-02'
  full_title: cloudflare-one-appliance changelog | Cloudflare Docs
  head_html: <title>cloudflare-one-appliance changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-02"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/cloudflare-one-appliance/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cloudflare-one-appliance changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-02"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/cloudflare-one-appliance/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/cloudflare-one-appliance/#page","headline":"cloudflare-one-appliance changelog | Cloudflare Docs","description":"2026-09-02","url":"https://developers.cloudflare.com/changelog/product/cloudflare-one-appliance/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/cloudflare-one-appliance/
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


<h2 id="link-aggregation-lacp-support-for-cloudflare-one-appliance"><a href="/changelog/post/2026-04-07-link-aggregation-lacp-appliance/">Link aggregation (LACP) support for Cloudflare One Appliance</a></h2>
<p><em>2026-04-07</em></p>
<p>Cloudflare One Appliance now supports Link Aggregation Control Protocol (LACP), allowing you to bundle up to six physical LAN ports into a single logical interface. Link aggregation increases available bandwidth and eliminates single points of failure on the LAN side of the appliance.</p>
<p>This feature is available in beta on physical appliance hardware with the latest OS. No entitlement is required.</p>
<p>To configure a Link Aggregation Group, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/link-aggregation/">Configure link aggregation groups</a>.</p>


<h2 id="post-quantum-encryption-support-for-cloudflare-one-appliance"><a href="/changelog/post/2026-02-11-appliance-post-quantum-encryption/">Post-quantum encryption support for Cloudflare One Appliance</a></h2>
<p><em>2026-02-11</em></p>
<p>Cloudflare One Appliance version 2026.2.0 adds <a href="/ssl/post-quantum-cryptography/">post-quantum encryption</a> support using hybrid ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).</p>
<p>The appliance now uses TLS 1.3 with hybrid ML-KEM for its connection to the Cloudflare edge. During the TLS handshake, the appliance and the edge share a symmetric secret over the TLS connection and inject it into the ESP layer of IPsec. This protects IPsec data plane traffic against harvest-now, decrypt-later attacks.</p>
<p>This upgrade deploys automatically to all appliances during their configured interrupt windows with no manual action required.</p>
<p>For more information, refer to <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a>.</p>


<h2 id="breakout-traffic-visibility-via-netflow"><a href="/changelog/post/2025-12-31-connector-breakout-traffic-netflow/">Breakout traffic visibility via NetFlow</a></h2>
<p><em>2025-12-31</em></p>
<p>Magic WAN Connector now exports NetFlow data for breakout traffic to Magic Network Monitoring (MNM), providing visibility into traffic that bypasses Cloudflare's security filtering.</p>
<p>This feature allows you to:</p>
<ul>
<li>Monitor breakout traffic statistics in the Cloudflare dashboard.</li>
<li>View traffic patterns for applications configured to bypass Cloudflare.</li>
<li>Maintain visibility across all traffic passing through your Magic WAN Connector.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-wan/analytics/netflow-analytics/">NetFlow statistics</a>.</p>


<h2 id="designate-wan-link-for-breakout-traffic"><a href="/changelog/post/2025-11-06-connector-designate-wan-link-breakout/">Designate WAN link for breakout traffic</a></h2>
<p><em>2025-11-06</em></p>
<p>Magic WAN Connector now allows you to designate a specific WAN port for breakout traffic, giving you deterministic control over the egress path for latency-sensitive applications.</p>
<p>With this feature, you can:</p>
<ul>
<li>Pin breakout traffic for specific applications to a preferred WAN port.</li>
<li>Ensure critical traffic (such as Zoom or Teams) always uses your fastest or most reliable connection.</li>
<li>Benefit from automatic failover to standard WAN port priority if the preferred port goes down.</li>
</ul>
<p>This is useful for organizations with multiple ISP uplinks who need predictable egress behavior for performance-sensitive traffic.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#designate-wan-ports-for-breakout-apps">Designate WAN ports for breakout apps</a>.</p>


<h2 id="virtual-cloudflare-one-appliance-with-kvm-support-open-beta"><a href="/changelog/post/2025-07-21-virtual-appliance-kvm-proxmox/">Virtual Cloudflare One Appliance with KVM support (open beta)</a></h2>
<p><em>2025-07-21</em></p>
<p>The KVM-based virtual Cloudflare One Appliance is now in open beta with official support for Proxmox VE.</p>
<p>Customers can deploy the virtual appliance on KVM hypervisors to connect branch or data center networks to Cloudflare WAN without dedicated hardware.</p>
<p>For setup instructions, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a virtual Cloudflare One Appliance</a>.</p>


<h2 id="cloudflare-one-appliance-supports-multiple-dns-server-ips"><a href="/changelog/post/2025-04-30-appliance-multiple-dns-servers/">Cloudflare One Appliance supports multiple DNS server IPs</a></h2>
<p><em>2025-04-30</em></p>
<p>Cloudflare One Appliance DHCP server settings now support specifying multiple DNS server IP addresses in the DHCP pool.</p>
<p>Previously, customers could only configure a single DNS server per DHCP pool. With this update, you can specify multiple DNS servers to provide redundancy for clients at branch locations.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/">DHCP server</a>.</p>


<h2 id="configure-your-magic-wan-connector-to-connect-via-static-ip-assignment"><a href="/changelog/post/2025-02-14-local-console-access/">Configure your Magic WAN Connector to connect via static IP assignment</a></h2>
<p><em>2025-02-14</em></p>
<p>You can now locally configure your <a href="/cloudflare-wan/configuration/appliance/">Magic WAN Connector</a> to work in a static IP configuration.</p>
<p>This local method does not require having access to a DHCP Internet connection. However, it does require being comfortable with using tools to access the serial port on Magic WAN Connector as well as using a serial terminal client to access the Connector's environment.</p>
<p>For more details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#bootstrap-via-serial-console">WAN with a static IP address</a>.</p>



