---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/
  description: Reference information for Protocols for published applications in Zero Trust networking.
  full_title: Protocols for published applications · Cloudflare One docs
  head_html: <title>Protocols for published applications · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Protocols for published applications in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/index.md"><meta property="og:title" content="Protocols for published applications · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Protocols for published applications in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/#page","headline":"Protocols for published applications \u00b7 Cloudflare One docs","description":"Reference information for Protocols for published applications in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/
  schema: 1
---
<p>When you <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#2a-publish-an-application">add a published application route</a> to a Cloudflare Tunnel, you are instructing Cloudflare to proxy requests for your public hostname to a service running privately behind <code>cloudflared</code>.</p>
<p>The table below lists the service types you can route to a public hostname. Non-HTTP services require <a href="/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/">installing <code>cloudflared</code> on the client</a> for end users to connect.</p>
<table>
<thead>
<tr>
<th>Service type</th>
<th>Description</th>
<th>Example <code>service</code> value</th>
</tr>
</thead>
<tbody>
<tr>
<td>HTTP</td>
<td>Proxies incoming HTTPS requests to your local web service over HTTP.</td>
<td><code>http://localhost:8000</code></td>
</tr>
<tr>
<td>HTTPS</td>
<td>Proxies incoming HTTPS requests directly to your local web service. You can <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#notlsverify">disable TLS verification</a> for self-signed certificates.</td>
<td><code>https://localhost:8000</code></td>
</tr>
<tr>
<td>UNIX</td>
<td>Same as HTTP, but uses a Unix socket.</td>
<td><code>unix:/home/production/echo.sock</code></td>
</tr>
<tr>
<td>UNIX + TLS</td>
<td>Same as HTTPS, but uses a Unix socket.</td>
<td><code>unix+tls:/home/production/echo.sock</code></td>
</tr>
<tr>
<td>TCP</td>
<td>Streams TCP over a WebSocket connection. End users run <code>cloudflared access tcp</code> to <a href="/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/arbitrary-tcp/">connect</a>. For long-lived connections, use <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/">Client-to-Tunnel</a> instead.</td>
<td><code>tcp://localhost:2222</code></td>
</tr>
<tr>
<td>SSH</td>
<td>Streams SSH over a WebSocket connection. End users run <code>cloudflared access ssh</code> to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-cloudflared-authentication/">connect</a>. For long-lived connections, use <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Client-to-Tunnel</a> instead.</td>
<td><code>ssh://localhost:22</code></td>
</tr>
<tr>
<td>RDP</td>
<td>Streams RDP over a WebSocket connection. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/">Connect to RDP with client-side cloudflared</a>.</td>
<td><code>rdp://localhost:3389</code></td>
</tr>
<tr>
<td>SMB</td>
<td>Streams SMB over a WebSocket connection. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/smb/#connect-to-smb-server-with-cloudflared-access">Connect to SMB with client-side cloudflared</a>.</td>
<td><code>smb://localhost:445</code></td>
</tr>
<tr>
<td>HTTP_STATUS</td>
<td>Responds to all requests with a fixed HTTP status code.</td>
<td><code>http_status:404</code></td>
</tr>
<tr>
<td>BASTION</td>
<td>Allows <code>cloudflared</code> to act as a jump host, providing access to any local address.</td>
<td><code>bastion</code></td>
</tr>
<tr>
<td>HELLO_WORLD</td>
<td>Test server for validating your Cloudflare Tunnel connection (for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/#file-structure-for-published-applications">locally managed tunnels</a> only).</td>
<td><code>hello_world</code></td>
</tr>
</tbody>
</table>
<h2 id="ipv6-service-addresses">IPv6 service addresses</h2>
<p>When the service value is an IPv6 literal, wrap the address in square brackets as defined by <a href="https://datatracker.ietf.org/doc/html/rfc3986#section-3.2.2">RFC 3986</a>. The brackets are required so that the <code>:</code> characters in the address are not confused with the port separator.</p>
<table>
<thead>
<tr>
<th>Service type</th>
<th>Example <code>service</code> value</th>
</tr>
</thead>
<tbody>
<tr>
<td>HTTP</td>
<td><code>http://[2001:db8::1]:8000</code></td>
</tr>
<tr>
<td>HTTPS</td>
<td><code>https://[2001:db8::1]:443</code></td>
</tr>
<tr>
<td>TCP</td>
<td><code>tcp://[2001:db8::1]:2222</code></td>
</tr>
<tr>
<td>SSH</td>
<td><code>ssh://[2001:db8::1]:22</code></td>
</tr>
<tr>
<td>RDP</td>
<td><code>rdp://[2001:db8::1]:3389</code></td>
</tr>
</tbody>
</table>
<p>Hostnames and IPv4 addresses do not need brackets — <code>http://localhost:8000</code> and <code>http://192.0.2.1:8000</code> are valid as-is.</p>
