---
cp9:
  canonical: https://developers.cloudflare.com/workers-vpc/reference/troubleshooting/
  description: Debug Workers VPC connection errors, tunnel issues, and common configuration problems.
  full_title: Troubleshoot and debug · Cloudflare Workers VPC
  head_html: <title>Troubleshoot and debug · Cloudflare Workers VPC</title><meta name="generator" content="Nift"><meta name="description" content="Debug Workers VPC connection errors, tunnel issues, and common configuration problems."><link rel="canonical" href="https://developers.cloudflare.com/workers-vpc/reference/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-vpc/reference/troubleshooting/index.md"><meta property="og:title" content="Troubleshoot and debug · Cloudflare Workers VPC"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Debug Workers VPC connection errors, tunnel issues, and common configuration problems."><meta property="og:url" content="https://developers.cloudflare.com/workers-vpc/reference/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers VPC"><meta name="algolia_product_filter" content="Workers VPC"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers VPC"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-vpc/reference/troubleshooting/#page","headline":"Troubleshoot and debug \u00b7 Cloudflare Workers VPC","description":"Debug Workers VPC connection errors, tunnel issues, and common configuration problems.","url":"https://developers.cloudflare.com/workers-vpc/reference/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-vpc/reference/troubleshooting/
  schema: 1
---
<p>Troubleshoot and debug errors commonly associated with Workers VPC.</p>
<h2 id="connection-error-codes">Connection error codes</h2>
<p>When Workers VPC cannot establish a connection to your private service, <code>fetch()</code> will throw an exception with an error code describing what went wrong. These error codes are also visible in the <strong>Metrics</strong> tab of your VPC Service in the Cloudflare dashboard.</p>
<p>Errors are grouped into three categories based on the likely cause. These categories match the labels shown in the <strong>Metrics</strong> tab of your VPC Service in the dashboard.</p>
<ul>
<li><strong>Bad Upstream</strong> — Your tunnel or private service is not reachable. Check tunnel health, service availability, and network/TLS configuration.</li>
<li><strong>Client</strong> — Your VPC Service configuration or Worker code caused the failure. Check your target hostname and Worker request behavior.</li>
<li><strong>Internal</strong> — A Cloudflare infrastructure issue. Contact Cloudflare support if this persists.</li>
</ul>
<h3 id="bad-upstream-errors">Bad Upstream errors</h3>
<p>These errors indicate that Cloudflare attempted to reach your private service but the connection failed. The tunnel may be down, the service may not be listening, or there is a network or TLS issue between Cloudflare and your origin.</p>
<table>
<thead>
<tr>
<th>Error code</th>
<th>Description</th>
<th>Recommended fix</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>connection_refused</code></td>
<td>Your private service refused the TCP connection.</td>
<td>Verify your service is running and listening on the expected port. Check firewall rules.</td>
</tr>
<tr>
<td><code>connection_terminated</code></td>
<td>The connection was closed by your service before a response was received.</td>
<td>Check your service logs for crashes or resource exhaustion.</td>
</tr>
<tr>
<td><code>connection_timeout</code></td>
<td>The connection attempt to your service timed out.</td>
<td>Verify your service is reachable from the tunnel. Check for network latency or firewall rules blocking traffic.</td>
</tr>
<tr>
<td><code>connection_limit_reached</code></td>
<td>The maximum number of concurrent connections to your service has been reached.</td>
<td>Scale your service to handle more connections, or reduce connection concurrency in your Worker.</td>
</tr>
<tr>
<td><code>destination_unavailable</code></td>
<td>Your service is considered unavailable.</td>
<td>Verify your tunnel is running and your service is healthy.</td>
</tr>
<tr>
<td><code>destination_not_found</code></td>
<td>No route could be determined for this request.</td>
<td>Check that your VPC Service configuration points to a valid host and that your tunnel is configured to route traffic to it.</td>
</tr>
<tr>
<td><code>destination_ip_prohibited</code></td>
<td>The destination IP address is prohibited.</td>
<td>Verify the IP address configured for your VPC Service is correct and not on a restricted list.</td>
</tr>
<tr>
<td><code>destination_ip_unroutable</code></td>
<td>No network route exists to the destination IP.</td>
<td>Check that the IP address is correct and reachable from within your private network.</td>
</tr>
<tr>
<td><code>proxy_loop_detected</code></td>
<td>The request would be forwarded back to the same proxy, creating a loop.</td>
<td>Review your VPC Service and tunnel configuration for circular routing.</td>
</tr>
<tr>
<td><code>dns_error</code></td>
<td>DNS resolution failed (for example, SERVFAIL).</td>
<td>Check that the hostname configured for your VPC Service is resolvable from within your private network. Verify your DNS resolver is working correctly. Refer to <a href="#tunnel-errors">Tunnel errors</a> for common DNS causes.</td>
</tr>
<tr>
<td><code>dns_timeout</code></td>
<td>DNS resolution timed out.</td>
<td>Check your DNS resolver is reachable and responding. Consider configuring a custom DNS resolver in your VPC Service settings.</td>
</tr>
<tr>
<td><code>tls_protocol_error</code></td>
<td>A TLS handshake or protocol error occurred when connecting to your service.</td>
<td>Verify your service's TLS configuration. Ensure the TLS version and cipher suites are compatible.</td>
</tr>
<tr>
<td><code>tls_certificate_error</code></td>
<td>Your service's TLS certificate failed verification.</td>
<td>Ensure your service presents a valid certificate from a <a href="/ssl/reference/certificate-authorities/">publicly trusted CA</a> or a <a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA certificate</a>.</td>
</tr>
<tr>
<td><code>http_request_error</code></td>
<td>An HTTP request error occurred.</td>
<td>Check your service logs for details on what caused the error response.</td>
</tr>
<tr>
<td><code>http_upgrade_failed</code></td>
<td>An HTTP upgrade (for example, WebSocket) failed.</td>
<td>Verify your service supports the requested protocol upgrade.</td>
</tr>
<tr>
<td><code>http_request_denied</code></td>
<td>The request was rejected by policy before being forwarded.</td>
<td>Review your service's access policies and configuration.</td>
</tr>
<tr>
<td><code>http_protocol_error</code></td>
<td>An HTTP protocol error occurred when communicating with your service.</td>
<td>Check that your service is responding with valid HTTP.</td>
</tr>
<tr>
<td><code>http_response_incomplete</code></td>
<td>Your service returned an incomplete HTTP response.</td>
<td>Check your service for issues that may cause it to close connections mid-response.</td>
</tr>
</tbody>
</table>
<h3 id="client-errors">Client errors</h3>
<p>These errors indicate a problem with your VPC Service setup or your Worker's behavior — not with the private service itself.</p>
<table>
<thead>
<tr>
<th>Error code</th>
<th>Description</th>
<th>Recommended fix</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>dns_error</code> (NXDOMAIN)</td>
<td>The hostname configured for your VPC Service does not exist in DNS.</td>
<td>Verify the hostname in your VPC Service configuration is correct and that a DNS record exists for it.</td>
</tr>
<tr>
<td><code>connection_read_timeout</code></td>
<td>The connection was established but no data was received within the time limit.</td>
<td>Check your Worker code for stalled or slow requests. Ensure your Worker is reading the response in a timely manner.</td>
</tr>
<tr>
<td><code>connection_write_timeout</code></td>
<td>Data could not be written to the connection (buffers full).</td>
<td>Check your Worker code for slow consumption of response data.</td>
</tr>
<tr>
<td><code>rate_limited</code></td>
<td>The connection rate limit to this origin has been exceeded.</td>
<td>Reduce the rate of new connections from your Worker to this service.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15862.md")
</aside>
<h3 id="internal-errors">Internal errors</h3>
<p>These errors indicate an issue within Cloudflare's infrastructure that is not caused by your configuration or your origin service.</p>
<table>
<thead>
<tr>
<th>Error code</th>
<th>Description</th>
<th>Recommended fix</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>proxy_internal_error</code></td>
<td>An internal error occurred within the Cloudflare proxy.</td>
<td>This is not caused by your configuration. If this error persists, contact <a href="https://support.cloudflare.com">Cloudflare support</a>.</td>
</tr>
</tbody>
</table>
<h2 id="tunnel-errors">Tunnel errors</h2>
<p>Workers VPC may return errors at runtime when connecting to private services through Cloudflare Tunnel.</p>
<table>
<thead>
<tr>
<th>Error Message</th>
<th>Details</th>
<th>Recommended fixes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Error: ProxyError: dns_error</code></td>
<td>DNS resolution failed when attempting to connect to your private service through the tunnel.</td>
<td>This error may occur if your <code>cloudflared</code> version is outdated. Ensure you are running <code>cloudflared</code> version 2025.7.0 or later (latest version recommended). See <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/update-cloudflared/">Cloudflare Tunnel update instructions</a>.</td>
</tr>
<tr>
<td><code>Error: ProxyError: dns_error</code></td>
<td>Cloudflare Tunnel may be configured with <code>http2</code> protocol (<code>TUNNEL_TRANSPORT_PROTOCOL:http2</code>), which works for Cloudflare Zero Trust <a href="/workers-vpc/configuration/tunnel/#create-and-run-tunnel-cloudflared">(see note)</a> traffic but prevents DNS resolution from Workers VPC.</td>
<td>Workers VPC requires Cloudflare Tunnel to connect using the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#protocol">QUIC transport protocol</a>. Ensure outbound UDP traffic on port 7844 is allowed through your firewall.</td>
</tr>
<tr>
<td>Requests not staying within VPC</td>
<td>Worker requests using <code>.fetch()</code> with a public hostname are routing out of the VPC to the hostname configured for the VPC Service.</td>
<td>Ensure your Worker code and the VPC Service use the internal VPC hostname for backend services, not a public hostname.</td>
</tr>
</tbody>
</table>
<h2 id="permission-errors">Permission errors</h2>
<p>If you cannot view, create, or bind VPC Services and Tunnels in the dashboard or via Wrangler, ensure your user has the required roles.</p>
<p>Workers VPC uses the following account roles:</p>
<ul>
<li><code>Connectivity Directory Read</code> to view Workers VPC Services and Tunnels.</li>
<li><code>Connectivity Directory Bind</code> to list, read, and bind VPC Services in Workers.</li>
<li><code>Connectivity Directory Admin</code> to create, update, and delete VPC Services, and bind directly to tunnels through a VPC Network binding.</li>
</ul>
<p>For role definitions, refer to <a href="/fundamentals/manage-members/roles/#account-scoped-roles">Roles</a>.</p>
<p>If your roles were recently updated and commands are still failing, refresh Wrangler authentication:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler logout&#10;npx wrangler login&#10;</code></pre>
<p>If you authenticate with an API token (<code>CLOUDFLARE_API_TOKEN</code>), ensure the token belongs to a user with the required roles.</p>
