---
cp9:
  canonical: https://developers.cloudflare.com/spectrum/reference/troubleshooting/
  description: Where to find logs and diagnostics for Spectrum applications.
  full_title: Troubleshooting · Cloudflare Spectrum docs
  head_html: <title>Troubleshooting · Cloudflare Spectrum docs</title><meta name="generator" content="Nift"><meta name="description" content="Where to find logs and diagnostics for Spectrum applications."><link rel="canonical" href="https://developers.cloudflare.com/spectrum/reference/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/spectrum/reference/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting · Cloudflare Spectrum docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Where to find logs and diagnostics for Spectrum applications."><meta property="og:url" content="https://developers.cloudflare.com/spectrum/reference/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Spectrum"><meta name="algolia_product_filter" content="Spectrum"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Spectrum"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/spectrum/reference/troubleshooting/#page","headline":"Troubleshooting \u00b7 Cloudflare Spectrum docs","description":"Where to find logs and diagnostics for Spectrum applications.","url":"https://developers.cloudflare.com/spectrum/reference/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /spectrum/reference/troubleshooting/
  schema: 1
---
<p>To investigate issues with a Spectrum application, use the logs and diagnostics described on this page. For API validation errors returned when creating or updating an application, refer to <a href="/spectrum/reference/error-codes/">Error codes</a>.</p>
<h2 id="spectrum-event-logs">Spectrum event logs</h2>
<p>Spectrum logs the lifecycle of every connection it proxies, including status codes for edge-to-origin failures (for example, <code>521</code> connection refused, <code>522</code> timeout, <code>523</code> unreachable). Refer to <a href="/spectrum/reference/logs/">Event logs</a>.</p>
<h2 id="virtual-network-origins">Virtual network origins</h2>
<p>When a Spectrum application uses a <a href="/spectrum/reference/configuration-options/#virtual-network-origin">virtual network origin</a>, traffic to the origin flows through the connector associated with the virtual network. Diagnose origin connectivity from the connector side using the sources for your connector type.</p>
<h3 id="cloudflare-tunnel-as-the-connector">Cloudflare Tunnel as the connector</h3>
<ul>
<li><strong>Tunnel logs</strong> record activity between <code>cloudflared</code> and Cloudflare's network and between <code>cloudflared</code> and your origin. Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Log streams</a>.</li>
<li><strong>Tunnel diagnostic logs</strong> collect a diagnostic report from a single <code>cloudflared</code> instance. Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/">Diagnostic logs</a>.</li>
<li><strong>Private network connectivity</strong> covers common causes when traffic does not reach a private origin through a tunnel. Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/private-networks/">Private network connectivity</a>.</li>
</ul>
<h3 id="cloudflare-wan-as-the-connector">Cloudflare WAN as the connector</h3>
<p>For tunnel health, BGP, and routing diagnostics on WAN-connected origins, refer to <a href="/cloudflare-wan/troubleshooting/">Troubleshoot Cloudflare WAN</a>.</p>
<h2 id="cannot-create-spectrum-application-dns-record-already-exists">Cannot create Spectrum application — DNS record already exists</h2>
<h3 id="symptoms">Symptoms</h3>
<ul>
<li>When creating a Spectrum application in the dashboard, you receive the error: <strong>&quot;An A, AAAA or CNAME record already exists with that host.&quot;</strong></li>
<li>You already have a manually-created proxied DNS record (<code>A</code>, <code>AAAA</code>, or <code>CNAME</code>) for the hostname you are trying to use for a new Spectrum application.</li>
</ul>
<h3 id="cause">Cause</h3>
<p>Cloudflare does not support having both a manually-created proxied DNS record (<code>A</code>, <code>AAAA</code>, or <code>CNAME</code>) and a Spectrum application on the same hostname. This is because Spectrum provisions and manages its own DNS record for the application, which conflicts with the existing manually-created record. This is a platform limitation, not a dashboard-only restriction.</p>
<p>This limitation only applies to manually-created proxied records. Multiple Spectrum applications — including a mix of HTTP/HTTPS and TCP/UDP application types — can share the same hostname, because Spectrum manages the DNS record for each of them.</p>
<h3 id="solution">Solution</h3>
<p>If you only need Spectrum applications on the hostname (for example, an HTTP/HTTPS Spectrum application alongside a TCP/UDP Spectrum application), you do not need a workaround — create the additional Spectrum application on the same hostname.</p>
<p>If you need to keep a manually-created proxied DNS record on the hostname (for example, to route standard HTTP/HTTPS traffic through the CDN and WAF instead of through Spectrum), use a <strong>split-hostname architecture</strong> instead, where the manually-created proxied record and the Spectrum application use different hostnames:</p>
<table>
<thead>
<tr>
<th>Traffic type</th>
<th>Hostname</th>
<th>Cloudflare service</th>
</tr>
</thead>
<tbody>
<tr>
<td>HTTPS (web UI, APIs)</td>
<td><code>app.example.com</code></td>
<td>Manually-created proxied DNS record with CDN/WAF</td>
</tr>
<tr>
<td>TCP (custom protocol, ICA/HDX, and similar)</td>
<td><code>app-tcp.example.com</code></td>
<td>Spectrum application</td>
</tr>
</tbody>
</table>
<p>Configure your application or client to use the appropriate hostname for each traffic type.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="common-use-case-citrix-gateway-vdi">Common use case: Citrix Gateway / VDI</h3>
@markup("md", "content/.markup/bodies/13863.md")
</aside>
<p>For more details on this limitation, refer to <a href="/spectrum/reference/limitations/">Spectrum Limitations</a>.</p>
<h2 id="origin-receives-http-instead-of-https-protocol-mismatch">Origin receives HTTP instead of HTTPS (protocol mismatch)</h2>
<h3 id="symptoms-1">Symptoms</h3>
<ul>
<li>Your Spectrum application edge port uses HTTP (for example, port 8012), and your origin expects HTTPS on port 443.</li>
<li>The origin rejects the connection or returns errors because it receives plaintext HTTP instead of encrypted HTTPS.</li>
<li>The configuration appears to work as: <code>http:8012 → Cloudflare Spectrum → http:443 (origin)</code> instead of the expected <code>http:8012 → Cloudflare Spectrum → https:443 (origin)</code>.</li>
</ul>
<h3 id="cause-1">Cause</h3>
<p>Spectrum operates at Layer 4 (TCP/UDP). When Edge TLS Termination is set to <strong>off</strong> (Passthrough), Spectrum forwards the raw TCP payload to the origin without modification. It does not perform protocol upgrade — connecting to an origin on port 443 does not automatically mean the connection will use HTTPS.</p>
<h3 id="solution-1">Solution</h3>
<p>To send encrypted traffic from Cloudflare to your origin, you must turn on <strong>Edge TLS Termination</strong> on the Spectrum application and set it to <strong>Full</strong> or <strong>Full (Strict)</strong>:</p>
<ul>
<li><strong>Full</strong>: Cloudflare connects to origin using TLS but does not validate the origin certificate.</li>
<li><strong>Full (Strict)</strong>: Cloudflare connects to origin using TLS and validates the origin certificate against a trusted CA or Cloudflare Origin CA.</li>
</ul>
<p>You can configure Edge TLS Termination in the Spectrum application settings in the dashboard, or via the API by setting the <code>tls</code> field to <code>full</code> or <code>strict</code>.</p>
<p>Refer to <a href="/spectrum/reference/configuration-options/#edge-tls-termination">Edge TLS Termination</a> for more details.</p>
<h2 id="tls-handshake-failures-error-525">TLS handshake failures (error 525)</h2>
<h3 id="symptoms-2">Symptoms</h3>
<ul>
<li>For TCP applications with Edge TLS Termination set to <strong>Full</strong> or <strong>Full (Strict)</strong>: connections to the origin fail. Spectrum event logs may show <code>521</code> (connection refused) or <code>522</code> (connection timeout) because a failed TLS handshake at the origin is reported as an origin connection failure. Refer to <a href="/spectrum/reference/logs/">Event logs</a> for the full status code reference.</li>
<li>For HTTP/HTTPS applications: clients receive error <code>525</code> (SSL handshake failed).</li>
</ul>
<p>These errors typically appear after creating a Spectrum application or modifying TLS settings.</p>
<h3 id="cause-2">Cause</h3>
<p>The TLS handshake between Cloudflare and your origin server failed. Common causes include:</p>
<ul>
<li><strong>Edge TLS Termination is set to Full or Full (Strict)</strong>, but the origin does not have a valid TLS certificate or does not accept TLS connections on the configured port.</li>
<li><strong>The Spectrum application origin points to another Cloudflare-proxied hostname</strong> (for example, <code>origin.example.com.cdn.cloudflare.net</code>). This creates a double-proxy chain that is not supported for TCP application types and can cause TLS handshake failures.</li>
<li><strong>TLS version or cipher mismatch</strong> between Cloudflare's edge and the origin server.</li>
</ul>
<h3 id="solution-2">Solution</h3>
<ol>
<li>Verify that your origin server has a valid TLS certificate and is configured to accept TLS connections on the origin port.</li>
<li>If using <strong>Full (Strict)</strong>, ensure the origin certificate is issued by a publicly trusted CA or a <a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA certificate</a>.</li>
<li>Confirm that the Spectrum application origin is not pointing to another Cloudflare-proxied hostname. Use a direct origin IP address or a DNS name that resolves directly to your origin server (not through Cloudflare's proxy).</li>
<li>If the origin only supports specific TLS versions, note that Spectrum supports TLS 1.1, 1.2, and 1.3 when Edge TLS Termination is turned on.</li>
</ol>
<h2 id="common-spectrum-event-log-status-codes">Common Spectrum event log status codes</h2>
<p>Spectrum uses its own set of connection status codes that are distinct from HTTP status codes used by Cloudflare's CDN layer. Some codes share numbers (for example, 444, 499) but have different meanings.</p>
<p>For the full status code table, refer to <a href="/spectrum/reference/logs/">Event logs</a>.</p>
<h3 id="common-patterns">Common patterns</h3>
<p>The following table lists frequently observed Spectrum status code patterns and their likely causes:</p>
<table>
<thead>
<tr>
<th>Pattern</th>
<th>Likely cause</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>High volume of <strong>444</strong> (Origin sent RST)</td>
<td>Origin server is actively resetting connections. May indicate origin overload, misconfigured firewall, or application crash.</td>
<td>Check origin server health, firewall rules, and application logs.</td>
</tr>
<tr>
<td>High volume of <strong>445</strong> (Origin timeout)</td>
<td>Established connections to origin are timing out. May indicate origin is slow to respond or network path issues.</td>
<td>Check origin server performance and network connectivity between Cloudflare and origin.</td>
</tr>
<tr>
<td>High volume of <strong>497</strong> (Client timeout)</td>
<td>Client connections are timing out. May indicate network issues between clients and Cloudflare edge, or clients with very long idle connections.</td>
<td>Review client network conditions and consider adjusting idle timeout expectations.</td>
</tr>
<tr>
<td>High volume of <strong>498</strong> (Client broken pipe)</td>
<td>Client connections are dropping mid-session. May indicate unstable client networks (for example, mobile users).</td>
<td>Often expected for mobile or unreliable networks. Monitor for trends.</td>
</tr>
<tr>
<td>High volume of <strong>499</strong> (Client sent RST)</td>
<td>Clients are actively closing connections. May indicate client-side timeouts or application-level disconnects.</td>
<td>Review client application timeout settings.</td>
</tr>
<tr>
<td><strong>521</strong> (Origin refused connection)</td>
<td>Origin is not accepting connections on the configured port.</td>
<td>Verify origin server is running and listening on the correct port. Check origin firewall.</td>
</tr>
<tr>
<td><strong>522</strong> (Origin connection timeout)</td>
<td>Cannot establish a TCP connection to origin.</td>
<td>Verify origin IP address, port, and that origin is reachable from Cloudflare.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13862.md")
</aside>
