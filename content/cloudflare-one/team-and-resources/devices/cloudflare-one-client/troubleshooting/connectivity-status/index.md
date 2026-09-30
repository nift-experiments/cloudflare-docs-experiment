---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/
  description: Reference information for Connectivity status in Zero Trust.
  full_title: Connectivity status · Cloudflare One docs
  head_html: <title>Connectivity status · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Connectivity status in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/index.md"><meta property="og:title" content="Connectivity status · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Connectivity status in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/#page","headline":"Connectivity status \u00b7 Cloudflare One docs","description":"Reference information for Connectivity status in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/
  schema: 1
---
<p>The Cloudflare One Client (formerly WARP) GUI displays the following status messages when transitioning from a <strong>Disconnected</strong> to <strong>Connected</strong> state. These messages indicate the connectivity stage of the Cloudflare One Client daemon as it establishes a connection from the device to Cloudflare. The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">client mode</a> determines which messages are displayed during the connection process. If the Cloudflare One Client encounters an error while connecting, the status message will change to an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/client-errors/">error code</a>.</p>
<p>To print status messages to the console, run the <code>warp-cli -l status</code> command before connecting the client.</p>
<table>
<thead>
<tr>
<th>Status message</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Verifying connection settings</td>
<td>Initializes connection components based on your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/">device client settings</a>.</td>
</tr>
<tr>
<td>Validating network</td>
<td>Validates Ethernet and/or Wi-Fi network connectivity.</td>
</tr>
<tr>
<td>Initializing IP connection</td>
<td>Checks for IPv4 and IPv6 connectivity to Cloudflare using the <a href="https://datatracker.ietf.org/doc/html/rfc6555">Happy Eyeballs algorithm</a>.</td>
</tr>
<tr>
<td>Establishing a connection</td>
<td>Connects to the endpoint discovered by Happy Eyeballs.</td>
</tr>
<tr>
<td>Building a Tunnel</td>
<td>Creates a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#virtual-interface">virtual network interface</a> on the operating system for the WARP tunnel.</td>
</tr>
<tr>
<td>Configuring the firewall</td>
<td>Configures the system firewall to allow WARP tunnel traffic.</td>
</tr>
<tr>
<td>Setting up your routing table</td>
<td>Updates the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#routing-table">system routing table</a> based on your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel rules</a>.</td>
</tr>
<tr>
<td>Configuring your firewall rules</td>
<td>Configures the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#system-firewall">system firewall</a> based on your Split Tunnel rules.</td>
</tr>
<tr>
<td>Checking connectivity to DNS</td>
<td>Checks connectivity to the DNS endpoint (<code>&lt;account-id&gt;.cloudflare-gateway.com</code>).</td>
</tr>
<tr>
<td>Setting local endpoint communication</td>
<td>Configures local DNS proxy sockets.</td>
</tr>
<tr>
<td>Configuring local DNS proxy</td>
<td>Creates a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#dns-traffic">local DNS proxy</a> for DNS resolution.</td>
</tr>
<tr>
<td>Applying DNS settings</td>
<td>Sets the local DNS proxy as the default DNS server on the device.</td>
</tr>
<tr>
<td>Configuring forward proxy</td>
<td>(Only in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Local proxy mode</a>) Configures the SOCKS proxy.</td>
</tr>
<tr>
<td>Confirming Tunnel connection</td>
<td>Checks connectivity to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#connectivity-checks">destinations</a> inside and outside of the WARP tunnel.</td>
</tr>
<tr>
<td>Validating DNS configuration</td>
<td>Verifies that DNS requests are answered by WARP's local DNS proxy.</td>
</tr>
<tr>
<td>Verifying SOCKS proxy configuration</td>
<td>(Only in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Local proxy mode</a>) Verifies the SOCKS proxy configuration.</td>
</tr>
<tr>
<td>Ensuring MTLS identity</td>
<td>(Only in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/">Posture only mode</a>) Installs a client certificate for mTLS authentication.</td>
</tr>
</tbody>
</table>
