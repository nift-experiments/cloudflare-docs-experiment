---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/
  description: Reference information for Common errors in Zero Trust networking.
  full_title: Common errors · Cloudflare One docs
  head_html: <title>Common errors · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Common errors in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/index.md"><meta property="og:title" content="Common errors · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Common errors in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#page","headline":"Common errors \u00b7 Cloudflare One docs","description":"Reference information for Common errors in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/
  schema: 1
---
<p>This section covers the most common errors you might encounter when connecting resources with Cloudflare Tunnel. If you do not see your issue listed below, refer to <a href="/cloudflare-one/troubleshooting/">Troubleshooting Cloudflare One</a>, view your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel logs</a>, or <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a>.</p>
<h2 id="tunnel-status">Tunnel status</h2>
<p>You can check your tunnel's connection status either from the Cloudflare dashboard (by going to <strong>Networking</strong> &gt; <strong>Tunnels</strong>) or by running the <code>cloudflared tunnel list</code> command. Each tunnel displays a status that reflects its current connection state:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Meaning</th>
<th>Recommended Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Healthy</strong></td>
<td>The tunnel is active and serving traffic through four connections to the Cloudflare global network.</td>
<td>No action is required. Your tunnel is running correctly.</td>
</tr>
<tr>
<td><strong>Inactive</strong></td>
<td>The tunnel has been created (via the API or dashboard) but the <code>cloudflared</code> connector has never been run to establish a connection.</td>
<td>Install and run <code>cloudflared</code> on your origin server to connect the tunnel to Cloudflare. You can find the installation command in the Cloudflare dashboard under <strong>Networking</strong> &gt; <strong>Tunnels</strong> — select your tunnel, then on the <strong>Overview</strong> tab select <strong>Add a replica</strong>. For API-based setup, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/#4-install-and-run-the-tunnel">Install and run the tunnel</a>.</td>
</tr>
<tr>
<td><strong>Down</strong></td>
<td>The tunnel was previously connected but is currently disconnected because the <code>cloudflared</code> process has stopped.</td>
<td>1. Ensure the <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/">service</a> or process is actively running on your server. <br /> 2. Check for server-side issues, such as the machine being powered off, an application crash, or recent network changes.</td>
</tr>
<tr>
<td><strong>Degraded</strong></td>
<td>The <code>cloudflared</code> connector is running and the tunnel is serving traffic, but at least one individual connection has failed. Further degradation in <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">tunnel availability</a> could risk the tunnel going down and failing to serve traffic.</td>
<td>1. Review your <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">logs</a> for connection failures or error messages. <br /> 2. Investigate local network and firewall rules to ensure they are not blocking connections to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Cloudflare Tunnel IPs and ports</a>. <br /></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="tunnel-status-scope">Tunnel status scope</h3>
@markup("md", "content/.markup/bodies/5278.md")
</aside>
<h2 id="i-see-cloudflared-service-is-already-installed">I see <code>cloudflared service is already installed</code>.</h2>
<p>If you see this error when installing a remotely-managed tunnel, ensure that no other <code>cloudflared</code> instances are running as a service on this machine. Only a single instance of <code>cloudflared</code> may run as a service on any given machine. Instead, add additional routes to your existing tunnel. Alternatively, you can run <code>sudo cloudflared service uninstall</code> to uninstall <code>cloudflared</code>.</p>
<h2 id="i-see-an-a-aaaa-or-cname-record-with-that-host-already-exists">I see <code>An A, AAAA, or CNAME record with that host already exists</code>.</h2>
<p>If you are unable to save your tunnel's public hostname, choose a different hostname or delete the existing DNS record. <a href="/dns/manage-dns-records/how-to/create-dns-records/">Check the DNS records</a> for your domain from the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>.</p>
<h2 id="tunnel-credentials-file-does-not-exist-or-is-not-a-file">Tunnel credentials file does not exist or is not a file.</h2>
<p>If you encounter the following error when running a tunnel, double check your <code>config.yml</code> file and ensure that the <code>credentials-file</code> points to the correct location. You may need to change <code>/root/</code> to your home directory.</p>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel run&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">2021-06-04T06:21:16Z INF Starting tunnel tunnelID=928655cc-7f95-43f2-8539-2aba6cf3592d&#10;Tunnel credentials file &#x27;/root/.cloudflared/928655cc-7f95-43f2-8539-2aba6cf3592d.json&#x27; doesn&#x27;t exist or is not a file&#10;</code></pre>
<h2 id="my-tunnel-fails-to-authenticate">My tunnel fails to authenticate.</h2>
<p>To start using Cloudflare Tunnel, a super administrator in the Cloudflare account must first log in through <code>cloudflared login</code>. The client will launch a browser window and prompt the user to select a hostname in their Cloudflare account. Once selected, Cloudflare generates a certificate that consists of three components:</p>
<ul>
<li>The public key of the origin certificate for that hostname</li>
<li>The private key of the origin certificate for that domain</li>
<li>A token that is unique to Cloudflare Tunnel</li>
</ul>
<p>Those three components are bundled into a single PEM file that is downloaded one time during that login flow. The host certificate is valid for the root domain and any subdomain one-level deep. Cloudflare uses that certificate file to authenticate <code>cloudflared</code> to create DNS records for your domain in Cloudflare.</p>
<p>The third component, the token, consists of the zone ID (for the selected domain) and an API token scoped to the user who first authenticated with the login command. When user permissions change (if that user is removed from the account or becomes an admin of another account, for example), Cloudflare rolls the user's API key. However, the certificate file downloaded through <code>cloudflared</code> retains the older API key and can cause authentication failures. The user will need to login once more through <code>cloudflared</code> to regenerate the certificate. Alternatively, the administrator can create a dedicated service user to authenticate.</p>
<h2 id="i-see-an-error-x509-certificate-signed-by-unknown-authority">I see an error: x509: certificate signed by unknown authority.</h2>
<p>This means the origin is using a certificate that <code>cloudflared</code> does not trust. For example, you may get this error if you are using SSL/TLS inspection in a proxy between your server and Cloudflare. To resolve:</p>
<ul>
<li>Add the CA certificate to the system trust store, then restart <code>cloudflared</code>.</li>
<li>Set <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#capool"><code>caPool</code></a> to a local PEM file that contains the CA certificate.</li>
<li>As a temporary last resort, set <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#notlsverify"><code>noTLSVerify</code></a> to <code>true</code>. Turn it off after you fix the certificate trust chain.</li>
</ul>
<p>The <code>--origin-ca-pool</code> and <code>--no-tls-verify</code> command-line flags apply only when you define a single origin with <code>--url</code>. For ingress rules, configure these settings under <code>originRequest</code>.</p>
<h2 id="i-see-an-error-1033-when-attempting-to-run-a-tunnel">I see an error 1033 when attempting to run a tunnel.</h2>
<p>A <code>1033</code> error indicates your tunnel is not connected to Cloudflare's network because Cloudflare's network cannot find a healthy <code>cloudflared</code> instance to receive the traffic.</p>
<p>First, review whether your tunnel is listed as <code>Active</code> in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> by going to <strong>Networking</strong> &gt; <strong>Tunnels</strong> or run <code>cloudflared tunnel list</code>. If the tunnel is not <code>Active</code>, review the following and take the action necessary for your tunnel status:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Meaning</th>
<th>Recommended Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Healthy</strong></td>
<td>The tunnel is active and serving traffic through four connections to the Cloudflare global network.</td>
<td>No action is required. Your tunnel is running correctly.</td>
</tr>
<tr>
<td><strong>Inactive</strong></td>
<td>The tunnel has been created (via the API or dashboard) but the <code>cloudflared</code> connector has never been run to establish a connection.</td>
<td>Install and run <code>cloudflared</code> on your origin server to connect the tunnel to Cloudflare. You can find the installation command in the Cloudflare dashboard under <strong>Networking</strong> &gt; <strong>Tunnels</strong> — select your tunnel, then on the <strong>Overview</strong> tab select <strong>Add a replica</strong>. For API-based setup, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/#4-install-and-run-the-tunnel">Install and run the tunnel</a>.</td>
</tr>
<tr>
<td><strong>Down</strong></td>
<td>The tunnel was previously connected but is currently disconnected because the <code>cloudflared</code> process has stopped.</td>
<td>1. Ensure the <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/">service</a> or process is actively running on your server. <br /> 2. Check for server-side issues, such as the machine being powered off, an application crash, or recent network changes.</td>
</tr>
<tr>
<td><strong>Degraded</strong></td>
<td>The <code>cloudflared</code> connector is running and the tunnel is serving traffic, but at least one individual connection has failed. Further degradation in <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">tunnel availability</a> could risk the tunnel going down and failing to serve traffic.</td>
<td>1. Review your <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">logs</a> for connection failures or error messages. <br /> 2. Investigate local network and firewall rules to ensure they are not blocking connections to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Cloudflare Tunnel IPs and ports</a>. <br /></td>
</tr>
</tbody>
</table>
<p>For more information, refer to the <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">comprehensive list of Cloudflare 1xxx errors</a>.</p>
<h2 id="i-see-a-502-bad-gateway-error-when-connecting-to-an-http-or-https-application-through-tunnel">I see a 502 Bad Gateway error when connecting to an HTTP or HTTPS application through tunnel.</h2>
<p>A <code>502 Bad Gateway</code> error with <code>Unable to reach the origin service. The service may be down or it may not be responding to traffic from cloudflared</code> on a tunnel route means the tunnel itself is connected to the Cloudflare network, but <code>cloudflared</code> cannot reach the origin service defined in your ingress rule. Unlike <a href="#i-see-an-error-1033-when-attempting-to-run-a-tunnel">error 1033</a>, which indicates the tunnel is not connected to Cloudflare, a 502 error indicates the problem is between <code>cloudflared</code> and your local service.</p>
<p>To identify the specific cause, review your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel logs</a> for <code>error</code>-level messages. Common causes include:</p>
<h4 id="origin-service-is-not-running">Origin service is not running</h4>
<p>If the origin service has stopped or never started, <code>cloudflared</code> logs will show an error similar to:</p>
<pre tabindex="0"><code class="language-txt">error=&quot;dial tcp [::1]:8080: connect: connection refused&quot;&#10;</code></pre>
<p>To resolve, verify the service is running and listening on the expected port:</p>
<pre tabindex="0"><code class="language-sh">curl -v http://localhost:8080&#10;</code></pre>
<p>If the service is not running, start or restart it. You can confirm the service is listening by running <code>ss -tlnp | grep &lt;PORT&gt;</code> (Linux) or <code>lsof -iTCP -sTCP:LISTEN -nP | grep &lt;PORT&gt;</code> (macOS).</p>
<h4 id="origin-service-url-uses-the-wrong-protocol">Origin service URL uses the wrong protocol</h4>
<p>If the origin expects HTTPS but the tunnel route specifies <code>http://</code>, or vice versa, <code>cloudflared</code> logs will show an error similar to:</p>
<pre tabindex="0"><code class="language-txt">error=&quot;net/http: HTTP/1.x transport connection broken: malformed HTTP response \&quot;\x15\x03\x01\x00\x02\x02\&quot;&quot;&#10;</code></pre>
<p>To resolve, update the service URL in your tunnel route to match the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/">protocol</a> your origin expects. For example, change <code>http://localhost:8080</code> to <code>https://localhost:8080</code>. If you are using a locally-managed tunnel, update your ingress rule in the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/">configuration file</a>.</p>
<h4 id="origin-service-url-points-to-the-wrong-port">Origin service URL points to the wrong port</h4>
<p>If the port in your tunnel route does not match the port your service is listening on, <code>cloudflared</code> will log a <code>connection refused</code> error for that port. Double-check the service URL in your ingress rule and compare it against the port your application is bound to.</p>
<h4 id="cloudflared-cannot-validate-the-origin-certificate"><code>cloudflared</code> cannot validate the origin certificate</h4>
<p>If the origin presents a TLS certificate that <code>cloudflared</code> cannot verify, the logs will show an error similar to:</p>
<pre tabindex="0"><code class="language-txt">error=&quot;x509: certificate is valid for example.com, not localhost&quot;&#10;</code></pre>
<p>This error indicates that the certificate does not cover the service hostname. An <code>x509: certificate signed by unknown authority</code> error instead indicates that <code>cloudflared</code> does not trust the certificate authority.</p>
<p>To resolve, use one of the following approaches:</p>
<ul>
<li>Set <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#originservername"><code>originServerName</code></a> to the hostname on the origin certificate in your tunnel route. If you are using a locally-managed tunnel, here is an example of a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/">configuration file</a>:</li>
</ul>
<pre tabindex="0"><code class="language-yml">ingress:&#10;  &#45; hostname: app.example.com&#10;    service: https://localhost:443&#10;    originRequest:&#10;      originServerName: app.example.com&#10;</code></pre>
<ul>
<li>Provide the CA certificate using <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#capool"><code>caPool</code></a>:</li>
</ul>
<pre tabindex="0"><code class="language-yml">ingress:&#10;  &#45; hostname: app.example.com&#10;    service: https://localhost:443&#10;    originRequest:&#10;      caPool: /path/to/ca-cert.pem&#10;</code></pre>
<ul>
<li>As a temporary last resort, disable TLS verification with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#notlsverify"><code>noTLSVerify</code></a>. Turn it off after resolving the certificate issue.</li>
</ul>
<pre tabindex="0"><code class="language-yml">ingress:&#10;  &#45; hostname: app.example.com&#10;    service: https://localhost:443&#10;    originRequest:&#10;      noTLSVerify: true&#10;</code></pre>
<h2 id="a-published-application-returns-err-too-many-redirects">A published application returns <code>ERR_TOO_MANY_REDIRECTS</code>.</h2>
<p>This error can occur when the origin redirects HTTP requests to HTTPS but the published application route uses an <code>http://</code> <code>Service URL</code>. Each request reaches the origin over HTTP and receives the same redirect.</p>
<p>To choose the correct service URL and origin settings, refer to <a href="/tunnel/troubleshooting/https-origins/">Troubleshoot HTTPS origins</a>. If the redirect chain alternates between HTTP and HTTPS, also refer to <a href="/ssl/troubleshooting/too-many-redirects/">ERR_TOO_MANY_REDIRECTS</a>.</p>
<h2 id="cloudflared-access-shows-an-error-websocket-bad-handshake"><code>cloudflared access</code> shows an error <code>websocket: bad handshake</code>.</h2>
<p>This means that your <code>cloudflared access</code> client is unable to reach your <code>cloudflared tunnel</code> origin. To diagnose this, look at the <code>cloudflared tunnel</code> logs. A common root cause is that the <code>cloudflared tunnel</code> is unable to proxy to your origin (for example, because the ingress is misconfigured, the origin is down, or the origin HTTPS certificate cannot be validated by <code>cloudflared tunnel</code>). If <code>cloudflared tunnel</code> has no logs, it means Cloudflare's network is not able to route the websocket traffic to it.</p>
<p>There are several possible root causes behind this error:</p>
<ul>
<li>Your <code>cloudflared tunnel</code> is either not running or not connected to Cloudflare's network.</li>
<li>WebSockets are not <a href="/network/websockets/#enable-websockets">enabled</a>.</li>
<li>Your Cloudflare account has Universal SSL enabled but your SSL/TLS encryption mode is set to <strong>Off (not secure)</strong>. To resolve, go to <strong>SSL/TLS</strong> &gt; <strong>Overview</strong> in the Cloudflare dashboard and set your SSL/TLS encryption mode to <strong>Flexible</strong>, <strong>Full</strong>, or <strong>Full (strict)</strong>.</li>
<li>Your requests are blocked by <a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a>. To resolve, make sure you set <strong>Definitely automated</strong> to <em>Allow</em> in the bot fight mode settings.</li>
<li>Your SSH or RDP Access application has the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#binding-cookie">Binding Cookie</a> enabled. To disable the cookie, go to <strong>Access controls</strong> &gt; <strong>Applications</strong> and edit the application settings.</li>
<li>One or more <a href="/workers/configuration/routing/routes/">Workers routes</a> are overlapping with the tunnel hostname, and the Workers do not properly handle the traffic. To resolve, either exclude your tunnel from the Worker route by not defining a route that includes the tunnel's hostname, or update your Worker to only handle specific paths and forward all other requests to the origin (for example, by using <code>return fetch(req)</code>).</li>
</ul>
<h2 id="tunnel-connections-fail-with-ssl-error">Tunnel connections fail with SSL error.</h2>
<p>If <code>cloudflared</code> returns error <code>error=&quot;remote error: tls: handshake failure&quot;</code>, check to make sure the hostname in question is covered by a SSL certificate. If using a multi-level subdomain, an <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificate</a> may be required as the Universal SSL will not cover more than one level of subdomain. This may surface in the browser as <code>ERR_SSL_VERSION_OR_CIPHER_MISMATCH</code>.</p>
<h2 id="tunnel-connections-fail-with-too-many-open-files-error">Tunnel connections fail with <code>Too many open files</code> error.</h2>
<p>If your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Cloudflare Tunnel logs</a> return a <code>socket: too many open files</code> error, it means that <code>cloudflared</code> has exhausted the open files limit on your machine. The maximum number of open files, or file descriptors, is an operating system setting that determines how many files a process is allowed to open. To increase the open file limit, you will need to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/#ulimits">configure ulimit settings</a> on the machine running <code>cloudflared</code>.</p>
<h2 id="i-see-failed-to-sufficiently-increase-receive-buffer-size-in-my-cloudflared-logs">I see <code>failed to sufficiently increase receive buffer size</code> in my cloudflared logs.</h2>
<p>This buffer size increase is reported by the <a href="https://github.com/quic-go/quic-go">quic-go library</a> leveraged by <a href="https://github.com/cloudflare/cloudflared">cloudflared</a>. You can learn more about the log message in the <a href="https://github.com/quic-go/quic-go/wiki/UDP-Buffer-Sizes">quic-go repository</a>. This log message is generally not impactful and can be safely ignored when troubleshooting. However, if you have deployed <code>cloudflared</code> within a unique, high-bandwidth environment then buffer size can be manually overridden for testing purposes.</p>
<p>To set the maximum receive buffer size on Linux:</p>
<ol>
<li>Create a new file under <code>/etc/sysctl.d/</code>:</li>
</ol>
<pre tabindex="0"><code class="language-sh">sudo vi 98-core-rmem-max.conf&#10;</code></pre>
<ol start="2">
<li>In the file, define the desired buffer size:</li>
</ol>
<pre tabindex="0"><code class="language-txt">net.core.rmem_max=2500000&#10;</code></pre>
<ol start="3">
<li>
<p>Reboot the host machine running <code>cloudflared</code>.</p>
</li>
<li>
<p>To validate that these changes have taken effect, use the <code>grep</code> command:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">sudo sysctl -a | grep net.core.rmem_max&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">net.core.rmem_max = 2500000&#10;</code></pre>
<h2 id="cloudflare-tunnel-is-buffering-my-streaming-response-instead-of-streaming-it-live">Cloudflare Tunnel is buffering my streaming response instead of streaming it live.</h2>
<p>Proxied traffic through Cloudflare Tunnel is buffered by default unless the origin server includes the <code>Content-Type: text/event-stream</code> response header. This header tells <code>cloudflared</code> to stream data as it arrives instead of buffering the entire response.</p>
<h2 id="my-tunnel-randomly-disconnects">My tunnel randomly disconnects.</h2>
<p>Long-lived connections initiated through Cloudflare One, such as SSH sessions, can last up to eight hours. However, disruptions along the service path may result in more frequent disconnects. Often, these disconnects are caused by regularly scheduled maintenance events such as data center, server, or service updates and restarts. If you believe these events are not the cause of disconnects in your environment, collect the relevant <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/">client logs</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel logs</a> and contact Support.</p>
<p>If the disconnects mainly affect idle SSH sessions, WebSocket connections, or other long-lived connections, the transport protocol may be relevant.</p>
<p>When <code>cloudflared</code> uses QUIC, idle sessions can be more sensitive to network devices that aggressively time out UDP traffic. If idle connections drop repeatedly, try one or more of the following:</p>
<ul>
<li>Configure application-layer keepalives, such as <code>ServerAliveInterval</code> for SSH.</li>
<li>Test with <code>cloudflared</code> set to <code>protocol: http2</code>.</li>
<li>Review local firewalls, NAT devices, and upstream network equipment for short UDP idle timers.</li>
</ul>
<p>For connection setup failures caused by blocked QUIC traffic, refer to the QUIC troubleshooting sections above.</p>
<h2 id="ping-and-traceroute-commands-do-not-work"><code>ping</code> and <code>traceroute</code> commands do not work.</h2>
<p>To ping an IP address behind Cloudflare Tunnel, your system must allow ICMP traffic through <code>cloudflared</code>. For configuration instructions, refer to the <a href="/cloudflare-one/traffic-policies/proxy/#icmp">ICMP proxy documentation</a>.</p>
<h2 id="i-see-error-this-route-s-network-is-inside-an-existing-subnet-s-network-at-100-96-0-0-12">I see <code>Error: This route's network is inside an existing subnet's network at &quot;100.96.0.0/12&quot;</code>.</h2>
<p>This error occurs when you try to add a CIDR route that falls within the Cloudflare One Client's <span class="nb-glossary-tooltip" title="WARP CGNAT IP">CGNAT IP range</span>. The <code>100.96.0.0/12</code> range, which covers addresses from <code>100.96.0.1</code> to <code>100.111.255.254</code>, is reserved for internal WARP routing and cannot be added as a Cloudflare Tunnel route. To connect your private network, you will need to change its IP/CIDR so that it does not overlap with <code>100.96.0.0/12</code>.</p>
<h2 id="i-see-this-site-can-t-provide-a-secure-connection">I see <code>This site can't provide a secure connection.</code></h2>
<p>If you see an error with the title <code>This site can't provide a secure connection</code> and a subtitle of <code>&lt;hostname&gt; uses an unsupported protocol</code>, you must <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/#create-a-certificate">order an Advanced Certificate</a>.</p>
<p>If you added a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#2a-connect-an-application">multi-level subdomain</a> (more than one level of subdomain), you must <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#2a-connect-an-application">order an Advanced Certificate for the hostname</a> as Cloudflare's Universal certificate will not cover the public hostname by default.</p>
<p>For more information on Tunnel errors, view your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel logs</a> or <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a>.</p>
