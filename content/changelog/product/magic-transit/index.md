---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/magic-transit/
  description: '2026-08-19'
  full_title: magic-transit changelog | Cloudflare Docs
  head_html: <title>magic-transit changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-08-19"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/magic-transit/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="magic-transit changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-08-19"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/magic-transit/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/magic-transit/#page","headline":"magic-transit changelog | Cloudflare Docs","description":"2026-08-19","url":"https://developers.cloudflare.com/changelog/product/magic-transit/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/magic-transit/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="threat-intel-lists-supported-in-unified-routing"><a href="/changelog/post/2026-08-19-unified-routing-threat-lists/">Threat Intel Lists supported in Unified Routing</a></h2>
<p><em>2026-08-19</em></p>
<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> Threat Intel Lists are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. This feature requires a Cloudflare Advanced Network Firewall subscription.</p>
<p>Support for additional features - Rate Limiting and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="ip-lists-ids-and-sip-rules-supported-in-unified-routing"><a href="/changelog/post/2026-07-08-unified-routing-iplist-ids-sip/">IP lists, IDS, and SIP rules supported in Unified Routing</a></h2>
<p><em>2026-07-08</em></p>
<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> IP lists, IDS, and SIP rules are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. These features require a Cloudflare Advanced Network Firewall subscription.</p>
<p>Support for additional features - Threat Intel Lists, Rate Limiting, and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


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


<h2 id="country-rules-supported-in-unified-routing"><a href="/changelog/post/2026-04-21-unified-routing-geoip-country-rules/">Country rules supported in Unified Routing</a></h2>
<p><em>2026-04-21T12:00:00</em></p>
<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> Country rules are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. This feature requires a Cloudflare Advanced Network Firewall subscription.</p>
<p>You can create firewall rules that match traffic based on source or destination country to enforce geographic access policies across your network.</p>
<p>This is the first of the Cloudflare Advanced Network Firewall features to become available in Unified Routing. Support for additional features - IP Lists, ASN Lists, Threat Intel Lists, IDS, Rate Limiting, SIP, and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


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


<h2 id="network-services-navigation-update"><a href="/changelog/post/2026-01-15-networking-navigation-update/">Network Services navigation update</a></h2>
<p><em>2026-01-15</em></p>
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


<h2 id="magic-transit-and-magic-wan-health-check-data-is-fully-compatible-with-the-cmb-eu-setting"><a href="/changelog/post/2025-07-30-mt-mwan-health-check-cmb-eu/">Magic Transit and Magic WAN health check data is fully compatible with the CMB EU setting.</a></h2>
<p><em>2025-07-30</em></p>
<p>Today, we are excited to announce that all Magic Transit and Magic WAN customers with CMB EU (<a href="/data-localization/metadata-boundary/">Customer Metadata Boundary - Europe</a>) enabled in their account will be able to access GRE, IPsec, and CNI health check and traffic volume data in the Cloudflare dashboard and via API.</p>
<p>This ensures that all Magic Transit and Magic WAN customers with CMB EU enabled will be able to access all Magic Transit and Magic WAN features.</p>
<p>Specifically, these two GraphQL endpoints are now compatible with CMB EU:</p>
<ul>
<li><code>magicTransitTunnelHealthChecksAdaptiveGroups</code></li>
<li><code>magicTransitTunnelTrafficAdaptiveGroups</code></li>
</ul>


<h2 id="graceful-withdrawal-of-byoip-prefixes"><a href="/changelog/post/2025-06-30-graceful-byoip-withdrawal/">Graceful withdrawal of BYOIP prefixes</a></h2>
<p><em>2025-06-30</em></p>
<p>Magic Transit customers can now configure AS prepending on their BYOIP prefixes advertised at the Cloudflare edge. This allows for smoother traffic migration and minimizes packet loss when changing providers.</p>
<p>AS prepending makes the Cloudflare route less preferred by increasing the AS path length. You can use this to gradually shift traffic away from Cloudflare before withdrawing a prefix, avoiding abrupt routing changes.</p>
<p>Prepending can be configured via the API or through BGP community values when peering with the Magic Transit routing table. For more information, refer to <a href="/magic-transit/how-to/advertise-prefixes/">Advertise prefixes</a>.</p>


<h2 id="establish-bgp-peering-over-direct-cni-circuits"><a href="/changelog/post/2024-12-17-bgp-support-cni/">Establish BGP peering over Direct CNI circuits</a></h2>
<p><em>2024-12-17</em></p>
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


<h2 id="explore-product-updates-for-cloudflare-one"><a href="/changelog/post/2024-06-16-cloudflare-one/">Explore product updates for Cloudflare One</a></h2>
<p><em>2024-06-16</em></p>
<p>Welcome to your new home for product updates on <a href="/cloudflare-one/">Cloudflare One</a>.</p>
<p>Our <a href="/changelog/">new changelog</a> lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.</p>
<p>If you are looking for older product updates, refer to the following locations.</p>
<details class="nb-details" open><summary>Older product updates</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17707.md")</div></details>



