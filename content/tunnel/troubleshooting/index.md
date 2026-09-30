---
cp9:
  canonical: https://developers.cloudflare.com/tunnel/troubleshooting/
  description: Resolve common Cloudflare Tunnel connection and configuration issues.
  full_title: Troubleshooting · Cloudflare Docs
  head_html: <title>Troubleshooting · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve common Cloudflare Tunnel connection and configuration issues."><link rel="canonical" href="https://developers.cloudflare.com/tunnel/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tunnel/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve common Cloudflare Tunnel connection and configuration issues."><meta property="og:url" content="https://developers.cloudflare.com/tunnel/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Tunnel"><meta name="algolia_product_filter" content="Cloudflare Tunnel"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cloudflare Tunnel"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tunnel/troubleshooting/#page","headline":"Troubleshooting \u00b7 Cloudflare Docs","description":"Resolve common Cloudflare Tunnel connection and configuration issues.","url":"https://developers.cloudflare.com/tunnel/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /tunnel/troubleshooting/
  schema: 1
---
<p>Use this page to diagnose and resolve common issues with Cloudflare Tunnel. Many issues are resolved by upgrading to the latest version of <code>cloudflared</code> — refer to <a href="/tunnel/guides/update-cloudflared/">Update cloudflared</a> before investigating further.</p>
<p>For tunnel health monitoring, logs, and metrics, refer to <a href="/tunnel/observability/">Observability</a>.</p>
<p>If your tunnel is <code>Healthy</code> but an HTTPS route fails or redirects, refer to <a href="/tunnel/troubleshooting/https-origins/">Troubleshoot HTTPS origins</a>.</p>
<h2 id="connection-errors">Connection errors</h2>
<p>When <code>cloudflared</code> cannot reach the Cloudflare network, it <a href="/tunnel/observability/#logs">logs</a> specific error messages that indicate whether the issue is DNS resolution, QUIC (UDP), or TCP connectivity.</p>
<h3 id="dns-resolution-failures">DNS resolution failures</h3>
<h4 id="edge-discovery-error-looking-up-cloudflare-edge-ips"><code>edge discovery: error looking up Cloudflare edge IPs</code></h4>
<pre tabindex="0"><code class="language-txt">ERR edge discovery: error looking up Cloudflare edge IPs: the DNS query failed&#10;    error=&quot;lookup _v2-origintunneld._tcp.argotunnel.com on 172.19.64.1:53: no such host&quot;&#10;</code></pre>
<p>This error means the DNS resolver configured on your machine cannot resolve the SRV records that <code>cloudflared</code> uses to discover the <a href="/tunnel/configuration/#firewall-rules">Cloudflare Tunnel destination IPs</a>. Common causes include corporate DNS resolvers that strip or block SRV records, and DNS resolvers that return compressed SRV records.</p>
<p><strong>To diagnose:</strong></p>
<p>On the <code>cloudflared</code> host machine, run:</p>
<pre tabindex="0"><code class="language-sh">dig SRV _v2-origintunneld._tcp.argotunnel.com&#10;</code></pre>
<p>If you receive <code>SERVFAIL</code>, <code>NXDOMAIN</code>, or an empty answer, test against Cloudflare's public resolver:</p>
<pre tabindex="0"><code class="language-sh">dig SRV _v2-origintunneld._tcp.argotunnel.com @1.1.1.1&#10;</code></pre>
<p><strong>To resolve:</strong></p>
<ul>
<li>If <code>1.1.1.1</code> returns results but your local resolver does not, configure the host to use <a href="/1.1.1.1/setup/">Cloudflare DNS (1.1.1.1)</a> or another public resolver.</li>
<li>If neither resolver returns results, your firewall is likely blocking outbound DNS queries (UDP port <code>53</code>). Work with your network administrator to allow DNS traffic.</li>
</ul>
<h4 id="dns-query-failed-i-o-timeout"><code>DNS query failed ... i/o timeout</code></h4>
<pre tabindex="0"><code class="language-txt">ERR edge discovery: error looking up Cloudflare edge IPs: the DNS query failed&#10;    error=&quot;lookup _v2-origintunneld._tcp.argotunnel.com on 127.0.0.11:53:&#10;    read udp 127.0.0.1:53467-&gt;127.0.0.11:53: i/o timeout&quot;&#10;</code></pre>
<p>This variant means DNS queries from <code>cloudflared</code> are being blocked or dropped entirely — the resolver never responds. This is common in container environments (Docker, Kubernetes) where the internal DNS resolver (<code>127.0.0.11</code>) is unreachable or misconfigured.</p>
<p><strong>To resolve:</strong></p>
<ul>
<li>In Docker, verify your container's DNS configuration (<code>/etc/resolv.conf</code>). You can override the resolver with <code>--dns 1.1.1.1</code> when running the container.</li>
<li>In Kubernetes, verify the <code>kube-dns</code> or <code>CoreDNS</code> service is running and reachable from the pod.</li>
<li>On the <code>cloudflared</code> host, verify that the resolver listed in <code>/etc/resolv.conf</code> is reachable and responding to queries.</li>
</ul>
<h3 id="quic-handshake-timeout">QUIC handshake timeout</h3>
<h4 id="failed-to-dial-a-quic-connection"><code>Failed to dial a quic connection</code></h4>
<pre tabindex="0"><code class="language-txt">ERR Failed to dial a quic connection error=&quot;failed to dial to edge with quic:&#10;    timeout: handshake did not complete in time&quot; connIndex=0 ip=198.41.192.227&#10;INF Retrying connection in up to 2s connIndex=0 ip=198.41.192.227&#10;</code></pre>
<p>This error means <code>cloudflared</code> resolved the <a href="/tunnel/configuration/#firewall-rules">Cloudflare Tunnel destination IPs</a> but could not complete a QUIC handshake over UDP port <code>7844</code>. Your network or firewall is blocking outbound UDP traffic to Cloudflare.</p>
<p><code>cloudflared</code> retries with exponential backoff (2, 4, 8, 16, 32, up to 64 seconds). After exhausting retries, it falls back to HTTP/2 over TCP:</p>
<pre tabindex="0"><code class="language-txt">INF Switching to fallback protocol http2 connIndex=0&#10;</code></pre>
<p>If the fallback also fails, you will see a <a href="#tcp-connection-timeout">TCP connection timeout</a> error.</p>
<p><strong>To diagnose:</strong></p>
<p>On the <code>cloudflared</code> host machine, test connectivity on port <code>7844</code>:</p>
<pre tabindex="0"><code class="language-sh">nc -uvz -w 3 198.41.192.227 7844&#10;</code></pre>
<p>Replace <code>198.41.192.227</code> with the IP shown in your <a href="#failed-to-dial-a-quic-connection">error message</a>. If the port is closed or blocked by a firewall, the command will return <code>Connection refused</code> or time out.</p>
<p><strong>To resolve:</strong></p>
<ul>
<li>Allow outbound UDP traffic to port <code>7844</code> on your firewall or security group. Refer to the <a href="/tunnel/configuration/#firewall-rules">full list of IPs and ports</a>.</li>
<li>If you cannot open UDP, <code>cloudflared</code> will fall back to HTTP/2 over TCP automatically. You can also force HTTP/2 by setting the <code>--protocol http2</code> <a href="/tunnel/configuration/#run-parameters">run parameter</a>, but QUIC is recommended for better performance.</li>
</ul>
<h3 id="tcp-connection-timeout">TCP connection timeout</h3>
<h4 id="dialcontext-error-dial-tcp-i-o-timeout"><code>DialContext error: dial tcp ... i/o timeout</code></h4>
<pre tabindex="0"><code class="language-txt">ERR Unable to establish connection with Cloudflare edge&#10;    error=&quot;DialContext error: dial tcp 198.41.200.43:7844: i/o timeout&quot; connIndex=0&#10;ERR Serve tunnel error&#10;    error=&quot;DialContext error: dial tcp 198.41.200.43:7844: i/o timeout&quot; connIndex=0&#10;</code></pre>
<p>This error means <code>cloudflared</code> cannot reach Cloudflare over TCP port <code>7844</code>. If you also see the <a href="#failed-to-dial-a-quic-connection">QUIC handshake timeout</a> above it, both UDP and TCP are blocked — the tunnel cannot connect at all.</p>
<p><strong>To diagnose:</strong></p>
<p>As a quick test, run:</p>
<pre tabindex="0"><code class="language-sh">curl -v https://region1.v2.argotunnel.com:7844&#10;</code></pre>
<p>If the connection hangs, traffic is being dropped between your host and Cloudflare.</p>
<p>To test if <code>cloudflared</code> can connect on port <code>7844</code>, run:</p>
<pre tabindex="0"><code class="language-sh">nc -vz -w 3 198.41.200.43 7844&#10;</code></pre>
<p>Replace <code>198.41.200.43</code> with the IP shown in your <a href="#dialcontext-error-dial-tcp--io-timeout">error message</a>. If the port is closed or blocked by a firewall, the command will return <code>Connection refused</code> or time out.</p>
<p><strong>To resolve:</strong></p>
<ul>
<li>Allow outbound TCP traffic to port <code>7844</code> to the <a href="/tunnel/configuration/#firewall-rules">Cloudflare Tunnel IP ranges</a>.</li>
<li>If your environment blocks port <code>7844</code> entirely (both UDP and TCP), the tunnel cannot function. Work with your network administrator to allow outbound traffic on this port.</li>
</ul>
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
<li>Set <a href="/tunnel/reference/origin-parameters/#capool"><code>caPool</code></a> to a local PEM file that contains the CA certificate.</li>
<li>As a temporary last resort, set <a href="/tunnel/reference/origin-parameters/#notlsverify"><code>noTLSVerify</code></a> to <code>true</code>. Turn it off after you fix the certificate trust chain.</li>
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
<p>To identify the specific cause, review your <a href="/tunnel/observability/#logs">Tunnel logs</a> for <code>error</code>-level messages. Common causes include:</p>
<h4 id="origin-service-is-not-running">Origin service is not running</h4>
<p>If the origin service has stopped or never started, <code>cloudflared</code> logs will show an error similar to:</p>
<pre tabindex="0"><code class="language-txt">error=&quot;dial tcp [::1]:8080: connect: connection refused&quot;&#10;</code></pre>
<p>To resolve, verify the service is running and listening on the expected port:</p>
<pre tabindex="0"><code class="language-sh">curl -v http://localhost:8080&#10;</code></pre>
<p>If the service is not running, start or restart it. You can confirm the service is listening by running <code>ss -tlnp | grep &lt;PORT&gt;</code> (Linux) or <code>lsof -iTCP -sTCP:LISTEN -nP | grep &lt;PORT&gt;</code> (macOS).</p>
<h4 id="origin-service-url-uses-the-wrong-protocol">Origin service URL uses the wrong protocol</h4>
<p>If the origin expects HTTPS but the tunnel route specifies <code>http://</code>, or vice versa, <code>cloudflared</code> logs will show an error similar to:</p>
<pre tabindex="0"><code class="language-txt">error=&quot;net/http: HTTP/1.x transport connection broken: malformed HTTP response \&quot;\x15\x03\x01\x00\x02\x02\&quot;&quot;&#10;</code></pre>
<p>To resolve, update the service URL in your tunnel route to match the <a href="/tunnel/concepts/routing/#supported-protocols">protocol</a> your origin expects. For example, change <code>http://localhost:8080</code> to <code>https://localhost:8080</code>. If you are using a locally-managed tunnel, update your ingress rule in the <a href="/tunnel/features/locally-managed-tunnels/configuration-file/">configuration file</a>.</p>
<h4 id="origin-service-url-points-to-the-wrong-port">Origin service URL points to the wrong port</h4>
<p>If the port in your tunnel route does not match the port your service is listening on, <code>cloudflared</code> will log a <code>connection refused</code> error for that port. Double-check the service URL in your ingress rule and compare it against the port your application is bound to.</p>
<h4 id="cloudflared-cannot-validate-the-origin-certificate"><code>cloudflared</code> cannot validate the origin certificate</h4>
<p>If the origin presents a TLS certificate that <code>cloudflared</code> cannot verify, the logs will show an error similar to:</p>
<pre tabindex="0"><code class="language-txt">error=&quot;x509: certificate is valid for example.com, not localhost&quot;&#10;</code></pre>
<p>This error indicates that the certificate does not cover the service hostname. An <code>x509: certificate signed by unknown authority</code> error instead indicates that <code>cloudflared</code> does not trust the certificate authority.</p>
<p>To resolve, use one of the following approaches:</p>
<ul>
<li>Set <a href="/tunnel/reference/origin-parameters/#originservername"><code>originServerName</code></a> to the hostname on the origin certificate in your tunnel route. If you are using a locally-managed tunnel, here is an example of a <a href="/tunnel/features/locally-managed-tunnels/configuration-file/">configuration file</a>:</li>
</ul>
<pre tabindex="0"><code class="language-yml">ingress:&#10;  &#45; hostname: app.example.com&#10;    service: https://localhost:443&#10;    originRequest:&#10;      originServerName: app.example.com&#10;</code></pre>
<ul>
<li>Provide the CA certificate using <a href="/tunnel/reference/origin-parameters/#capool"><code>caPool</code></a>:</li>
</ul>
<pre tabindex="0"><code class="language-yml">ingress:&#10;  &#45; hostname: app.example.com&#10;    service: https://localhost:443&#10;    originRequest:&#10;      caPool: /path/to/ca-cert.pem&#10;</code></pre>
<ul>
<li>As a temporary last resort, disable TLS verification with <a href="/tunnel/reference/origin-parameters/#notlsverify"><code>noTLSVerify</code></a>. Turn it off after resolving the certificate issue.</li>
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
<p>If your <a href="/tunnel/observability/#logs">Cloudflare Tunnel logs</a> return a <code>socket: too many open files</code> error, it means that <code>cloudflared</code> has exhausted the open files limit on your machine. The maximum number of open files, or file descriptors, is an operating system setting that determines how many files a process is allowed to open. To increase the open file limit, you will need to <a href="/tunnel/platform/system-requirements/#ulimits-linux-and-macos">configure ulimit settings</a> on the machine running <code>cloudflared</code>.</p>
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
<h2 id="cloudflare-tunnel-fails-to-connect-through-palo-alto-networks-next-generation-firewall">Cloudflare Tunnel fails to connect through Palo Alto Networks Next-Generation Firewall</h2>
<p>Cloudflare recently became aware of a change in Palo Alto Networks Next Generation Firewall (NGFW) App-ID database version 9128 that affects the requirements for permitting Cloudflare Tunnel and Cloudflare One Client traffic.</p>
<p>Palo Alto Networks Next Generation Firewall (NGFW) detects both Cloudflare Tunnel (<code>cloudflared</code>) and the Cloudflare One Client (WARP with Zero Trust) as <code>cloudflare-warp</code>, regardless of the App-ID database version. There is currently no separate App-ID for <code>cloudflared</code>.</p>
<p>This issue is likely to impact the Cloudflare One Client and WARP client, because Palo Alto Networks NGFW identifies their traffic as <code>cloudflare-warp</code>.</p>
<p>This section focuses on Cloudflare Tunnel (<code>cloudflared</code>) connecting to Cloudflare over QUIC (UDP port <code>7844</code>).</p>
<p>Starting with App-ID database version 9128 (released on July 27, 2026), NGFW changed the requirements for permitting this traffic. App-ID database version 9128 and later requires you to explicitly allow the <code>quic-base</code> application in addition to the previously required App-IDs and their dependencies.</p>
<p>To restore connectivity, either revert the App-ID database or explicitly allow the required applications and UDP port.</p>
<h3 id="option-1-revert-the-app-id-database">Option 1: Revert the App-ID database</h3>
<p>Revert to App-ID database version 9127 and disable automatic App-ID updates until Palo Alto Networks provides a permanent resolution.</p>
<p>If you revert the App-ID database, treat this as a temporary mitigation and coordinate with your security team. Re-enable automatic updates once Palo Alto Networks provides a permanent resolution.</p>
<h3 id="option-2-configure-an-explicit-firewall-policy">Option 2: Configure an explicit firewall policy</h3>
<h4 id="create-a-custom-service-for-udp-port-7844">Create a custom service for UDP port 7844</h4>
<ol>
<li>In PAN-OS, go to <strong>Objects</strong> &gt; <strong>Services</strong>.</li>
<li>Create a service with the following settings:</li>
</ol>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Name</td>
<td><code>cloudflared_7844_udp</code></td>
</tr>
<tr>
<td>Description</td>
<td>Optional</td>
</tr>
<tr>
<td>Protocol</td>
<td>UDP</td>
</tr>
<tr>
<td>Destination Port</td>
<td><code>7844</code></td>
</tr>
<tr>
<td>Source Port</td>
<td>Leave blank</td>
</tr>
<tr>
<td>Session Timeout</td>
<td>Inherit from application</td>
</tr>
</tbody>
</table>
<ol start="3">
<li>Select <strong>OK</strong>.</li>
</ol>
<h4 id="create-or-update-a-firewall-rule">Create or update a firewall rule</h4>
<ol>
<li>Go to <strong>Policies</strong>.</li>
<li>Create or modify a <strong>universal</strong> or <strong>interzone</strong> firewall rule.</li>
<li>Configure the <strong>Source</strong> and <strong>Destination</strong> criteria to match the relevant traffic flows in your environment:
<ul>
<li><strong>Source</strong>: Select the appropriate Source Zone and/or Source Address.</li>
<li><strong>Destination</strong>: Select the appropriate Destination Zone and/or Destination Address.</li>
</ul>
</li>
<li>Under <strong>Application</strong>, add all of the following applications:
<ul>
<li><code>cloudflare-warp</code></li>
<li><code>quic-base</code></li>
</ul>
</li>
<li>Under <strong>Service/URL Category</strong>, add the custom service <code>cloudflared_7844_udp</code>.</li>
<li>Set the rule <strong>Action</strong> to <strong>Allow</strong>.</li>
<li>Enable logging according to your organization's security policy.</li>
<li>Commit the policy change, then verify that Cloudflare Tunnel can establish and maintain connections through the firewall.</li>
</ol>
<h2 id="how-do-i-contact-support">How do I contact support?</h2>
<p>For the fastest possible troubleshooting, ensure your support ticket includes comprehensive details. The more context you provide, the faster your issue can be identified and resolved.</p>
<p>To ensure efficient resolution when <a href="/support/contacting-cloudflare-support/">contacting support</a>, include as much relevant detail as possible in your ticket:</p>
<ul>
<pre tabindex="0"><code>&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Context: Briefly describe the scenario or use&#10;		case (for example, where the user was, what they were trying to do).&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Reproduction steps: Describe the steps you took&#10;		to reproduce the issue during troubleshhooting.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Timestamps: Be specific and include the exact&#10;		time and time zone when the issue occurred.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Troubleshooting attempts: Outline any&#10;		troubleshooting steps or changes already attempted to resolve the issue.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Tunnel ID and tunnel name.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; &lt;code&gt;cloudflared&lt;/code&gt; version (run &lt;code&gt;cloudflared --version&lt;/code&gt;).&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; How the tunnel was set up (locally-managed or remotely-managed via the dashboard).&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Tunnel logs: Include the &lt;a href=&quot;/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/#view-logs-on-your-local-machine&quot;&gt;logs from your local machine&lt;/a&gt;.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Tunnel diagnostic logs: Include &lt;a href=&quot;/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/&quot;&gt;tunnel diagnostic logs&lt;/a&gt;.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;</code></pre>
</ul>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="write-a-detailed-ticket-to-resolve-your-issue-faster">Write a detailed ticket to resolve your issue faster</h3>
@markup("md", "content/.markup/bodies/14856.md")
</aside>
<h3 id="collect-debug-logs">Collect debug logs</h3>
<p>To capture verbose output for troubleshooting:</p>
<ul>
<li><strong>Locally-managed tunnels</strong>: Run <code>cloudflared</code> with the <code>--loglevel debug</code> flag:</li>
</ul>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel --loglevel debug run&#10;</code></pre>
<p>To persist logs to a file, add the <code>--logfile</code> flag:</p>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel --loglevel debug --logfile /var/log/cloudflared/cloudflared.log run&#10;</code></pre>
<ul>
<li><strong>Remotely-managed tunnels</strong> (created via the dashboard): Configure logging in the tunnel's <a href="/tunnel/reference/run-parameters/#loglevel">run parameters</a>. You can also stream logs in real time using the <a href="/tunnel/observability/#remote-log-streaming">remote log streaming</a> feature.</li>
</ul>
<p>Attach the debug logs when contacting support — refer to the checklist above for the full list of information to include.</p>
