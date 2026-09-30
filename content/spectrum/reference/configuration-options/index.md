<p>Spectrum is a global TCP and UDP proxy running on Cloudflare's edge nodes. It does not terminate the connection in the application-layer sense. However, at Layer 4, Spectrum does terminate the TCP and UDP sockets in both directions. The L4 payloads of TCP segments and UDP datagrams are passed back and forth as-is, without modifications.</p>
<p>This means Spectrum does not inspect, modify, or upgrade application-layer protocols. For example, Spectrum cannot convert an HTTP connection to HTTPS, add HTTP headers, or apply WAF rules to TCP traffic. To add Layer 7 functionality such as CDN, Workers, or Bot Management, set the <a href="#application-type">application type</a> to <strong>HTTP/HTTPS</strong>.</p>
<p>For common issues and troubleshooting guidance, refer to <a href="/spectrum/reference/troubleshooting/">Spectrum Troubleshooting</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13872.md")
</aside>
<h2 id="application-type">Application type</h2>
<p>The application type determines the protocol by which data travels from the edge to your origin. Select <em>TCP/UDP</em> if you want to proxy directly to the origin. If you want to set up products like CDN, Workers, or Bot management, you need to select <em>HTTP/HTTPS</em>. In this case, traffic is routed through Cloudflare's pipeline instead of connecting directly to your origin.</p>
<h2 id="ip-addresses">IP addresses</h2>
<p>When a Spectrum application is created, it is assigned a unique IPv4 and IPv6 address, or you can provision the application to be IPv6 only. The addresses are not static, and they may change over time. The best way to look up the current addresses is by using DNS. The DNS name of the Spectrum application will always return the IPs currently dedicated to the application.</p>
<p>The addresses are anycasted from all Cloudflare data centers, with the exception of data centers in China.</p>
<h2 id="smtp">SMTP</h2>
<p>Spectrum can act as a TCP load balancer in front of an SMTP server but will not act as an intermediary mail server. Instead, Spectrum passes data through to your origin. The client IP shown on mail will be the Cloudflare edge IP. If the mail server requires knowing the true client IP, it should use Proxy Protocol to get the source IP from Cloudflare. Cloudflare recommends enabling Proxy Protocol on applications configured to proxy SMTP.</p>
<p>SMTP servers may perform a series of checks on servers attempting to send messages through it. These checks are intended to filter requests from illegitimate servers.</p>
<p>Messages may be rejected if:</p>
<ul>
<li>A reverse DNS lookup on the IP address of the connecting server returns a negative response.</li>
<li>The reverse DNS lookup produces a different hostname than what was sent in the SMTP <code>HELO</code>/<code>EHLO</code> message.</li>
<li>The reverse DNS lookup produces a different hostname than what is advertised in your SMTP server's banner.</li>
<li>The result of a reverse DNS lookup does not match a corresponding forward DNS lookup.</li>
</ul>
<p>Spectrum applications do not have reverse DNS entries.</p>
<p>Additionally, SMTP servers may perform a DNS lookup to find the MX records for a domain. Messages from your server may be rejected if an MX record for your domain is associated with a Spectrum application, as the IP address of server will not match the Spectrum IP address.</p>
<h2 id="ports">Ports</h2>
<p>Cloudflare supports all TCP ports.</p>
<h2 id="port-ranges">Port ranges</h2>
<p>Spectrum applications can be configured to proxy traffic on ranges of ports.</p>
<p>For direct origins:</p>
<pre><code class="language-json">{&#10;	&quot;protocol&quot;: &quot;tcp/1000-2000&quot;,&#10;	&quot;dns&quot;: {&#10;		&quot;type&quot;: &quot;CNAME&quot;,&#10;		&quot;name&quot;: &quot;range.example.com&quot;&#10;	},&#10;	&quot;origin_direct&quot;: [&quot;tcp://192.0.2.1:3000-4000&quot;]&#10;}&#10;</code></pre>
<p>For DNS origins:</p>
<pre><code class="language-json">{&#10;	&quot;protocol&quot;: &quot;tcp/1000-2000&quot;,&#10;	&quot;dns&quot;: {&#10;		&quot;type&quot;: &quot;CNAME&quot;,&#10;		&quot;name&quot;: &quot;range.example.com&quot;&#10;	},&#10;	&quot;origin_dns&quot;: {&#10;		&quot;name&quot;: &quot;origin.example.com&quot;,&#10;		&quot;ttl&quot;: 1200&#10;	},&#10;	&quot;origin_port&quot;: &quot;3000-4000&quot;&#10;}&#10;</code></pre>
<p>The number of ports in an origin port range must match the number of ports specified in the <code>protocol</code> field.
Connections to a port within a port range at the edge will be proxied to the equivalent port offset in the origin range.
For example, in the configurations above, a connection to <code>range.example.com:1005</code> would be proxied to port <code>3005</code> on the origin.</p>
<h2 id="ip-access-rules">IP Access rules</h2>
<p>If <a href="/waf/tools/ip-access-rules/create/">IP Access rules</a> are enabled for a Spectrum application, Cloudflare will respect the IP Access rules configured for that domain. Cloudflare only respects rules created for specific IP addresses, IP blocks, countries, or ASNs for Spectrum applications. Spectrum will also only respect rules created with the actions <code>allow</code> or <code>block</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13871.md")
</aside>
<h2 id="argo-smart-routing">Argo Smart Routing</h2>
<p>Once Argo Smart Routing is enabled for your application, traffic will automatically be routed through the fastest and most reliable network path available. Argo Smart Routing is available for TCP and UDP (beta) applications.</p>
<h2 id="virtual-network-origin">Virtual network origin</h2>
<p>Spectrum applications can route <code>origin_direct</code> traffic to a private origin through a Cloudflare Tunnel <a href="/cloudflare-one/networks/virtual-networks/">virtual network</a>. Set <code>virtual_network_id</code> on the application to the ID of the virtual network that the origin IP is routable within. Traffic to the application is delivered through the connector associated with that virtual network — typically a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> or a <a href="/cloudflare-wan/">Cloudflare WAN</a> (formerly Magic WAN) connection.</p>
<p>To create the virtual network and attach a route covering your origin IP, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">Manage virtual networks</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">Connect an IP/CIDR</a>.</p>
<p>The following restrictions apply when <code>virtual_network_id</code> is set:</p>
<ul>
<li>Application type must be TCP or UDP. HTTP/HTTPS applications do not support virtual network origins.</li>
<li>The origin must be specified with <code>origin_direct</code>. Hostname origins (<code>origin_dns</code>) are not supported.</li>
<li><code>origin_direct</code> must contain exactly one address. Multiple addresses are not supported.</li>
<li>The origin port must be a single port. Port ranges are not supported.</li>
<li>The origin IP must be routable within the specified virtual network. The virtual network must already have a route covering the IP.</li>
<li><a href="/spectrum/how-to/enable-proxy-protocol/">Proxy Protocol</a> is not supported. <code>proxy_protocol</code> must be set to <code>off</code>.</li>
</ul>
<p>For the validation error codes returned when these constraints are violated, refer to <a href="/spectrum/reference/error-codes/">Error codes</a>.</p>
<p>Spectrum virtual network origins are for TCP and UDP traffic only. For HTTP/HTTPS traffic to private origins, use <a href="/dns/private-origins/">Application Services for Private Origins</a>, which provides WAF, CDN caching, and the full Cloudflare proxy stack.</p>
<h2 id="edge-tls-termination">Edge TLS Termination</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="spectrum-does-not-perform-protocol-upgrade">Spectrum does not perform protocol upgrade</h3>
@markup("md", "content/.markup/bodies/13870.md")
</aside>
<p>If you enable <strong>Edge TLS Termination</strong> for a Spectrum application, Cloudflare will encrypt traffic for the application at the Edge. The Edge TLS Termination toggle applies only to TCP applications.</p>
<p>Spectrum offers three modes of TLS termination: 'Flexible', 'Full', and 'Full (Strict)'.</p>
<p>'Flexible' enables termination of the client connection at the edge, but does not enable TLS from Cloudflare to your origin. Traffic will be sent over an encrypted connection from the client to Cloudflare, but not from Cloudflare to the origin.</p>
<p>'Full' specifies that traffic from Cloudflare to the origin will also be encrypted but without certificate validation. When set to 'Full (Strict)', traffic from Cloudflare to the origin will also be encrypted with strict validation of the origin certificate.</p>
<p>TLS versions supported by Spectrum include TLS 1.1, TLS 1.2, and TLS 1.3.</p>
<p>You can manage this through the Spectrum app at the Cloudflare dashboard, or using the <a href="/api/resources/spectrum/subresources/apps/methods/update/">Spectrum API endpoint</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13869.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13868.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13867.md")
</aside>
<h2 id="origin-tls-termination">Origin TLS Termination</h2>
<p>Below are the cipher suites Cloudflare presents to origins during an SSL/TLS handshake. For cipher suites supported at our edge or presented to browsers and other user agents, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/">Cipher suites</a>.</p>
<p>The cipher suites below are ordered based on how they appear in the ClientHello, communicating our preference to the origin. Customers do not have the ability to modify the ciphers used by Spectrum.</p>
<h2 id="supported-cipher-suites-by-protocol">Supported cipher suites by protocol</h2>
<table>
<thead>
<tr>
<th>OpenSSL Name</th>
<th>TLS 1.1</th>
<th>TLS 1.2</th>
<th>TLS 1.3</th>
</tr>
</thead>
<tbody>
<tr>
<td>AEAD-AES128-GCM-SHA256<sup><a href="#footnote-1">1</a></sup></td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>AEAD-AES256-GCM-SHA384<sup><a href="#footnote-1">1</a></sup></td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>AEAD-CHACHA20-POLY1305-SHA256<sup><a href="#footnote-1">1</a></sup></td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>ECDHE-ECDSA-AES128-GCM-SHA256</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-GCM-SHA256</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-SHA</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>AES128-GCM-SHA256</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>AES128-SHA</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>AES256-SHA</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Although TLS 1.3 uses the same cipher suite space as previous versions of TLS, TLS 1.3 cipher suites are defined differently, only specifying the symmetric ciphers, and cannot be used with TLS 1.2. Similarly, TLS 1.2 and lower cipher suites cannot be used with TLS 1.3 ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446.html)). BoringSSL also hard-codes cipher preferences in this order for TLS 1.3. Refer to [TLS 1.3 cipher suites](/ssl/origin-configuration/cipher-suites/#tls-13-cipher-suites) for details.</li></ol></section>
