<p>Origin parameters determine how <code>cloudflared</code> sends requests to the origin server of your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">published application</a>.</p>
<h2 id="update-origin-parameters">Update origin parameters</h2>
<p>This section describes how to update origin parameters for a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5370.md")
</div>. If you are using a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/5371.md")
</div>, add these parameters to your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/">configuration file</a>.
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5373.md")
</div></div>
<h2 id="tls-settings">TLS settings</h2>
<h3 id="originservername">originServerName</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;&quot;</code></td>
<td>Origin Server Name</td>
</tr>
</tbody>
</table>
<p>Hostname that <code>cloudflared</code> should expect from your origin server certificate. If empty, <code>cloudflared</code> uses the hostname from the service URL, for example <code>localhost</code> if the service is <code>https://localhost:443</code>.</p>
<h3 id="matchsnitohost">matchSNItoHost</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>false</code></td>
<td>Match SNI to host</td>
</tr>
</tbody>
</table>
<p>When <code>true</code>, <code>cloudflared</code> sets the Server Name Indication (SNI) during the TLS handshake to the request <code>Host</code> value sent to the origin. If you configure <a href="#httphostheader">HTTP Host Header</a>, <code>cloudflared</code> uses that value for SNI. This setting overrides <a href="#originservername">Origin Server Name</a> for each request.</p>
<p>This setting is useful when directing traffic to entry points that host multiple services and rely on SNI to route requests or present the correct certificate. It eliminates the need to explicitly configure <a href="#originservername"><code>originServerName</code></a> for individual services when using wildcard routing.</p>
<h3 id="capool">caPool</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;&quot;</code></td>
<td>CA Pool</td>
</tr>
</tbody>
</table>
<p>Local file path to the certificate authority (CA) for your origin server certificate (for example, <code>/root/certs/ca.pem</code>). The path should point to a certificate store file or a bundle file in <code>.pem</code> or <code>.crt</code> format that contains one or more trusted root CA certificates. <code>cloudflared</code> adds these certificates to its default trust pool. Configure this setting when a private CA signs the certificate and the CA is not in the default trust pool.</p>
<h3 id="notlsverify">noTLSVerify</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>false</code></td>
<td>Disable TLS certificate verification</td>
</tr>
</tbody>
</table>
<p>When <code>false</code>, TLS verification is performed on the certificate presented by your origin.</p>
<p>When <code>true</code>, TLS verification is disabled. This will allow any certificate from the origin to be accepted.</p>
<h3 id="tlstimeout">tlsTimeout</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10s</code></td>
<td>TLS Timeout</td>
</tr>
</tbody>
</table>
<p>Timeout for completing a TLS handshake to your origin server, if you have chosen to connect Tunnel to an HTTPS server.</p>
<h3 id="http2origin">http2Origin</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>false</code></td>
<td>Use HTTP/2 to origin</td>
</tr>
</tbody>
</table>
<p>When <code>false</code>, <code>cloudflared</code> will connect to your origin with HTTP/1.1.</p>
<p>When <code>true</code>, <code>cloudflared</code> attempts to connect to your origin server using HTTP/2 instead of HTTP/1.1. HTTP/2 to the origin requires HTTPS. For a certificate signed by a private CA, configure <a href="#capool">CA Pool</a> and keep TLS verification enabled.</p>
<h2 id="http-settings">HTTP settings</h2>
<h3 id="httphostheader">httpHostHeader</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;&quot;</code></td>
<td>HTTP Host Header</td>
</tr>
</tbody>
</table>
<p>Sets the HTTP <code>Host</code> header on requests sent to the local service.</p>
<h3 id="disablechunkedencoding">disableChunkedEncoding</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>false</code></td>
<td>Disable Chunked Encoding</td>
</tr>
</tbody>
</table>
<p>When <code>false</code>, <code>cloudflared</code> performs chunked transfer encoding when transferring data over HTTP/1.1.</p>
<p>When <code>true</code>, chunked transfer encoding is disabled. This is useful if you are running a Web Server Gateway Interface (WSGI) server.</p>
<h2 id="connection-settings">Connection settings</h2>
<h3 id="connecttimeout">connectTimeout</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>30s</code></td>
<td>Connect Timeout</td>
</tr>
</tbody>
</table>
<p>Timeout for establishing a new TCP connection to your origin server. This excludes the time taken to
establish TLS, which is controlled by tlsTimeout.</p>
<h3 id="nohappyeyeballs">noHappyEyeballs</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>false</code></td>
<td>No Happy Eyeballs</td>
</tr>
</tbody>
</table>
<p>When <code>false</code>, <code>cloudflared</code> uses the Happy Eyeballs algorithm for IPv4/IPv6 fallback if your local network has misconfigured one of the protocols.</p>
<p>When <code>true</code>, Happy Eyeballs is disabled.</p>
<h3 id="proxytype">proxyType</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;&quot;</code></td>
<td>Proxy Type</td>
</tr>
</tbody>
</table>
<p><code>cloudflared</code> starts a proxy server to translate HTTP traffic into TCP when proxying, for example, SSH or RDP.
This configures what type of proxy will be started. Valid options are:</p>
<ul>
<li><code>&quot;&quot;</code> for the regular proxy</li>
<li><code>&quot;socks&quot;</code> for a SOCKS5 proxy. Refer to the <a href="/cloudflare-one/tutorials/kubectl/">tutorial on connecting through Cloudflare Access using kubectl</a> for more information.</li>
</ul>
<h3 id="proxyaddress">proxyAddress</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5369.md")
</aside>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>127.0.0.1</code></td>
<td>--</td>
</tr>
</tbody>
</table>
<p><code>cloudflared</code> starts a proxy server to translate HTTP traffic into TCP when proxying, for example, SSH or RDP.
This configures the listen address for that proxy.</p>
<h3 id="proxyport">proxyPort</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5368.md")
</aside>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>0</code></td>
<td>--</td>
</tr>
</tbody>
</table>
<p><code>cloudflared</code> starts a proxy server to translate HTTP traffic into TCP when proxying, for example, SSH or RDP.
This configures the listen port for that proxy. If set to zero, an unused port will randomly be chosen.</p>
<h3 id="keepalivetimeout">keepAliveTimeout</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1m30s</code></td>
<td>Idle Connection Expiration Time</td>
</tr>
</tbody>
</table>
<p>Timeout after which an idle keepalive connection can be discarded.</p>
<h3 id="keepaliveconnections">keepAliveConnections</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>100</code></td>
<td>Keep Alive Connections</td>
</tr>
</tbody>
</table>
<p>Default: <code>100</code></p>
<p>Maximum number of idle keepalive connections between <code>cloudflared</code> and your origin. This does not restrict the total number of concurrent connections.</p>
<h3 id="tcpkeepalive">tcpKeepAlive</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>30s</code></td>
<td>TCP Keep Alive Interval</td>
</tr>
</tbody>
</table>
<p>Default: <code>30s</code></p>
<p>The timeout after which <code>cloudflared</code> sends a TCP keepalive packet to the origin server.</p>
<h2 id="access-settings">Access settings</h2>
<h3 id="access">access</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;&quot;</code></td>
<td>Protect with Access</td>
</tr>
</tbody>
</table>
<p>Requires <code>cloudflared</code> to validate the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/">Cloudflare Access JWT</a> prior to proxying traffic to your origin. You can enforce this check on public hostname services that are protected by an Access application. For all L7 requests to these hostnames, Access will send the JWT to <code>cloudflared</code> as a <code>Cf-Access-Jwt-Assertion</code> request header.</p>
<p>To enable this security control in a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/">configuration file</a>, <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/#get-your-aud-tag">get the AUD tag</a> for your Access application and add the following rule to <code>originRequest</code>:</p>
<pre><code class="language-yml">access:&#10;  required: true&#10;  teamName: &lt;your-team-name&gt;&#10;  audTag:&#10;    &#45; &lt;Access-application-audience-tag&gt;&#10;    &#45; &lt;Optional-additional-tags&gt;&#10;</code></pre>
