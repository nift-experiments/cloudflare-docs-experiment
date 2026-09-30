<p>If your <a href="/tunnel/">Cloudflare Tunnel</a> is <code>Healthy</code> but <code>app.example.com</code> fails, check the route's <code>Service URL</code>, origin certificate, and <a href="/ssl/origin-configuration/ssl-modes/">SSL/TLS encryption mode</a>.</p>
<p>A <code>Healthy</code> status confirms only that <code>cloudflared</code> connects to Cloudflare. It does not test the route's service or the local origin.</p>
<p>This guide covers an origin that already serves HTTPS with a Let's Encrypt certificate. You can keep the existing certificate installed.</p>
<p>For an Apache origin that redirects HTTP to HTTPS, use these settings:</p>
<ul>
<li><strong>Service URL</strong>: <code>https://localhost:443</code> when <code>cloudflared</code> runs on the Apache host</li>
<li><strong>Origin Server Name</strong>: The hostname covered by the certificate, such as <code>app.example.com</code></li>
<li><strong>Disable TLS certificate verification</strong>: Turned off</li>
<li><strong>Encryption mode</strong>: Leave <strong>Automatic SSL/TLS (recommended)</strong> selected, or choose <strong>Full (Strict)</strong></li>
</ul>
<h2 id="understand-the-route">Understand the route</h2>
<p>The public hostname is the URL that visitors request. The <code>Service URL</code> is the address, protocol, and port that <code>cloudflared</code> can reach. These values are not interchangeable. Do not use a public hostname as the service URL when that hostname points to the Tunnel CNAME.</p>
<p>For example, <code>http://localhost:80</code> uses HTTP for the local connection, while <code>https://localhost:443</code> uses HTTPS. Replace these examples with the address and port used by your origin.</p>
<p>The connection between Cloudflare and <code>cloudflared</code> is encrypted independently of the zone SSL/TLS mode. <code>cloudflared</code> validates the local origin certificate through origin parameters.</p>
<p>The zone SSL/TLS mode does not change the <code>Service URL</code>. Configure the local protocol in the route, then configure certificate validation with <a href="/tunnel/reference/origin-parameters/#originservername"><code>originServerName</code></a> and the other <a href="/tunnel/reference/origin-parameters/">origin parameters</a>.</p>
<p>If <code>originServerName</code> is empty, <code>cloudflared</code> expects the certificate to cover the host in the <code>Service URL</code>. For a service URL that uses <code>localhost</code>, set <code>originServerName</code> to the hostname covered by the certificate. This value also supplies the Server Name Indication (SNI) for the TLS connection.</p>
<h2 id="choose-route-and-ssl-tls-settings">Choose route and SSL/TLS settings</h2>
<p>Use the following decision tree to choose the local protocol and certificate settings:</p>
<pre><code class="language-mermaid">flowchart TD&#10;    accTitle: Service URL and SSL/TLS mode decision tree&#10;    accDescr: Choose the Service URL from the origin protocol, then configure certificate validation for HTTPS origins.&#10;    A{Origin accepts HTTPS?}&#10;    A --&gt;|No| B{HTTP redirects to HTTPS?}&#10;    B --&gt;|No| C[Use HTTP service URL]&#10;    B --&gt;|Yes| D{Keep the redirect?}&#10;    D --&gt;|No| C&#10;    D --&gt;|Yes| E[Configure an HTTPS listener]&#10;    A --&gt;|Yes| F[Use HTTPS service URL]&#10;    E --&gt; F&#10;    F --&gt; G{Certificate covers service host?}&#10;    G --&gt;|Yes| H[Keep TLS verification on]&#10;    G --&gt;|No| I[Set Origin Server Name and keep verification on]&#10;</code></pre>
<p>If the origin has no HTTPS listener, remove or adjust its redirect before keeping an HTTP <code>Service URL</code>. Do not point an HTTPS <code>Service URL</code> at an HTTP listener.</p>
<p>Use this table to compare common origin and zone settings:</p>
<table>
<thead>
<tr>
<th>Origin behavior</th>
<th>Service URL</th>
<th>Origin parameters</th>
<th>Zone SSL/TLS guidance</th>
</tr>
</thead>
<tbody>
<tr>
<td>HTTP only, with no redirect</td>
<td><code>http://127.0.0.1:80</code></td>
<td>No TLS parameters</td>
<td>Automatic, Flexible, Full, and Full (strict) do not change the local HTTP connection.</td>
</tr>
<tr>
<td>HTTP redirects to HTTPS</td>
<td><code>https://localhost:443</code>, or remove the redirect and use HTTP</td>
<td>Configure the route as HTTPS</td>
<td>Do not use <strong>Flexible</strong> to solve the redirect loop.</td>
</tr>
<tr>
<td>HTTPS with a valid Let's Encrypt certificate for <code>app.example.com</code></td>
<td><code>https://localhost:443</code></td>
<td>Set <code>originServerName: app.example.com</code>. Keep <strong>Disable TLS certificate verification</strong> turned off and omit <code>caPool</code>.</td>
<td>Choose the zone mode separately. It does not validate the local certificate.</td>
</tr>
<tr>
<td>HTTPS with a private certificate authority (CA)</td>
<td><code>https://localhost:443</code></td>
<td>Set <code>originServerName</code> and <code>caPool</code>. Keep <strong>Disable TLS certificate verification</strong> turned off.</td>
<td>Choose the zone mode separately. Fix certificate trust first.</td>
</tr>
</tbody>
</table>
<p>For a public HTTPS hostname, <strong>Full (strict)</strong> is compatible with this configuration. However, <code>cloudflared</code> validates the local Let's Encrypt certificate independently. The zone mode does not replace the route's <code>Service URL</code> or <code>originServerName</code> settings.</p>
<p><strong>Full</strong> also does not change the Tunnel service protocol or fix an origin certificate error. Do not switch to <strong>Flexible</strong> for either issue. Update the route's <strong>Service URL</strong> or origin parameters instead.</p>
<h2 id="update-a-remotely-managed-route">Update a remotely-managed route</h2>
<p>For a remotely-managed tunnel, update the route and its origin parameters in the dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/14857.md")
</div>
<p>The route does not require you to remove an existing Let's Encrypt certificate. <code>cloudflared</code> can validate that certificate when the origin name and service protocol match.</p>
<h2 id="keep-the-ssl-tls-mode-separate">Keep the SSL/TLS mode separate</h2>
<p>The zone SSL/TLS mode is separate from the Tunnel route. It does not select the local protocol or fix a certificate mismatch between <code>cloudflared</code> and the origin.</p>
<p>To review or change the zone mode:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/14858.md")
</div>
<p>For details about available modes, refer to <a href="/ssl/origin-configuration/ssl-modes/">SSL/TLS encryption modes</a>. If the origin redirects HTTP to HTTPS, an HTTP <code>Service URL</code> can cause a redirect loop. Refer to <a href="/ssl/troubleshooting/too-many-redirects/">ERR_TOO_MANY_REDIRECTS</a> for other redirect causes.</p>
<h2 id="configure-a-locally-managed-tunnel">Configure a locally-managed tunnel</h2>
<p>For a locally-managed tunnel, put the same settings in <code>config.yml</code>:</p>
<pre><code class="language-yml">tunnel: &lt;TUNNEL_UUID&gt;&#10;credentials-file: /path/to/&lt;TUNNEL_UUID&gt;.json&#10;&#10;ingress:&#10;  &#45; hostname: app.example.com&#10;    service: https://localhost:443&#10;    originRequest:&#10;      originServerName: app.example.com&#10;  &#45; service: http_status:404&#10;</code></pre>
<p>This example keeps TLS verification enabled. It omits <code>caPool</code> because standard Let's Encrypt certificates are publicly trusted. For a private CA, add <code>caPool: /path/to/ca.pem</code> under <code>originRequest</code>.</p>
<p>On Windows, if <code>cloudflared</code> reports that it cannot load the system root certificate pool, set <code>caPool</code> to a local PEM bundle that contains the certificate authority.</p>
<p>Use <code>noTLSVerify: true</code> only as a temporary last resort while you fix certificate trust or the origin name. Turn it off after you resolve the underlying issue.</p>
<p>The catch-all <code>http_status:404</code> rule is required at the end of the file. After editing <code>config.yml</code>, validate the ingress rules:</p>
<pre><code class="language-sh">cloudflared tunnel ingress validate&#10;</code></pre>
<h2 id="run-diagnostics">Run diagnostics</h2>
<p>Run these checks from the public Internet and from the same host as <code>cloudflared</code>:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/14859.md")
</div>
<p>For protocol details, refer to <a href="/tunnel/concepts/routing/#supported-protocols">supported Tunnel protocols</a>. For all origin settings, refer to <a href="/tunnel/reference/origin-parameters/">Tunnel origin parameters</a>.</p>
