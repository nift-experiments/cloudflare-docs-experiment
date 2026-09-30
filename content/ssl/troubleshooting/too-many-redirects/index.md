<p>After you <a href="/fundamentals/manage-domains/add-site/">add a new domain</a> to Cloudflare, your visitors' browsers might display <code>ERR_TOO_MANY_REDIRECTS</code> or <code>The page isn’t redirecting properly</code> errors.</p>
<p>This error occurs when visitors get stuck in a redirect loop.</p>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Redirect loops illustration&#10;A[Request for &lt;code&gt;http://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;] --&gt; B[Redirect to &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;]&#10;B --&gt; C[Redirect to &lt;code&gt;http://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;]&#10;C --&gt; B&#10;subgraph Redirect Loop&#10;B&#10;C&#10;end&#10;</code></pre>
<br />
<p>This error is commonly caused by:</p>
<ul>
<li>A misconfiguration of your <a href="#encryption-mode-misconfigurations">SSL/TLS Encryption mode</a>.</li>
<li>Various settings on the <a href="#edge-certificate-settings"><strong>Edge Certificates</strong></a> page.</li>
<li>A misconfigured <a href="#redirect-rules">redirect rule</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13956.md")
</aside>
<hr />
<h2 id="encryption-mode-misconfigurations">Encryption mode misconfigurations</h2>
<p>Your domain's <a href="/ssl/origin-configuration/ssl-modes/">SSL/TLS Encryption mode</a> controls how Cloudflare connects to your origin server and how SSL certificates presented by your origin will be validated.</p>
<p>This setting can cause redirect loops when the value you set in Cloudflare conflicts with the settings at your origin web server.</p>
<h3 id="flexible-encryption-mode">Flexible encryption mode</h3>
<p>If your domain's encryption mode is set to <a href="/ssl/origin-configuration/ssl-modes/flexible/"><strong>Flexible</strong></a>, Cloudflare sends unencrypted requests to your origin server over HTTP.</p>
<p>Redirect loops will occur if your origin server automatically redirects all HTTP requests to HTTPS.</p>
<pre><code class="language-mermaid">flowchart TD&#10;accTitle: Redirect loops illustration for Flexible mode&#10;A[Request for &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;] --&gt; B[Encryption mode redirects to &lt;code&gt;http://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;]&#10;B --&gt; C[Origin server redirects to &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;]&#10;C --&gt; B&#10;subgraph Cloudflare&#10;B&#10;end&#10;subgraph Origin server&#10;C&#10;end&#10;</code></pre>
<br />
<p>To solve this issue, either remove HTTPS redirects from your origin server or update your SSL/TLS Encryption Mode to be <a href="/ssl/origin-configuration/ssl-modes/full/"><strong>Full</strong></a> or higher (requires an SSL certificate configured at your origin server). To enforce HTTPS at the Cloudflare edge without setting up redirects at your origin, refer to <a href="/ssl/edge-certificates/encrypt-visitor-traffic/">Enforce HTTPS connections</a>.</p>
<h3 id="full-or-full-strict-encryption-mode">Full or Full (strict) encryption mode</h3>
<p>If your domain's encryption mode is set to <a href="/ssl/origin-configuration/ssl-modes/full/"><strong>Full</strong></a> or <a href="/ssl/origin-configuration/ssl-modes/full-strict/"><strong>Full (strict)</strong></a>, Cloudflare sends encrypted requests to your origin server over HTTPS.</p>
<p>Redirect loops will occur if your origin server automatically redirects all HTTPS requests to HTTP.</p>
<pre><code class="language-mermaid">flowchart TD&#10;accTitle: Redirect loops illustration for Full or Full (strict) mode&#10;A[Request for &lt;code&gt;http://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;] --&gt; B[Encryption mode redirects to &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;]&#10;B --&gt; C[Origin server redirects to &lt;code&gt;http://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;]&#10;C --&gt; B&#10;subgraph Cloudflare&#10;B&#10;end&#10;subgraph Origin server&#10;C&#10;end&#10;</code></pre>
<br />
<p>To solve this issue, remove HTTP redirects from your origin server.</p>
<hr />
<h2 id="edge-certificate-settings">Edge certificate settings</h2>
<h3 id="always-use-https">Always use HTTPS</h3>
<p>If you have <a href="/ssl/edge-certificates/additional-options/always-use-https/"><strong>Always Use HTTPS</strong></a> enabled for your domain, Cloudflare redirects all <code>http</code> requests to <code>https</code> for all subdomains and hosts in your application.</p>
<p>Redirect loops will occur if your origin server automatically redirects all HTTPS requests to HTTP.</p>
<pre><code class="language-mermaid">flowchart TD&#10;accTitle: Redirect loops illustration for Always Use HTTPS&#10;A[Request for &lt;code&gt;http://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;] --&gt; B[Always Use HTTPS redirects to &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;]&#10;B --&gt; C[Origin server redirects to &lt;code&gt;http://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;]&#10;C --&gt; B&#10;subgraph Cloudflare&#10;B&#10;end&#10;subgraph Origin server&#10;C&#10;end&#10;</code></pre>
<br />
<p>To solve this issue, remove HTTPS redirects from your origin server or <a href="/ssl/edge-certificates/additional-options/always-use-https/">disable <strong>Always Use HTTPS</strong></a>.</p>
<h3 id="hsts">HSTS</h3>
<p>If you have <a href="/ssl/edge-certificates/additional-options/http-strict-transport-security/"><strong>HTTP Strict Transport Security (HSTS)</strong></a> enabled for your domain, Cloudflare directs compliant web browsers to transform <code>http</code> links to <code>https</code> links.</p>
<p>Redirect loops will occur if your origin server automatically redirects all HTTPS requests to HTTP or if you have your domain's encryption mode set to <a href="/ssl/origin-configuration/ssl-modes/off/"><strong>Off</strong></a>.</p>
<pre><code class="language-mermaid">flowchart TD&#10;accTitle: Redirect loops illustration for HTTP Strict Transport Security&#10;A[Request for &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;] --&gt; B[Encryption mode redirects to &lt;code&gt;http://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;]&#10;B --&gt; C[HSTS redirects to &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;]&#10;C --&gt; B&#10;C --&gt; D[Origin server redirects to &lt;code&gt;http://&lt;/code&gt;&lt;code&gt;example.com&lt;/code&gt;]&#10;D --&gt; C&#10;subgraph Cloudflare&#10;B&#10;C&#10;end&#10;subgraph Origin server&#10;D&#10;end&#10;</code></pre>
<br />
<p>To solve this issue, remove HTTPS redirects from your origin server and make sure your domain's encryption mode is <a href="/ssl/origin-configuration/ssl-modes/flexible/"><strong>Flexible</strong></a> or higher.</p>
<p>Alternatively, <a href="/ssl/edge-certificates/additional-options/http-strict-transport-security/">disable <strong>HTTP Strict Transport Security (HSTS)</strong></a>.</p>
<hr />
<h2 id="redirect-rules">Redirect rules</h2>
<p>Redirect loops can also occur if you have conflicting URL redirects.</p>
<pre><code class="language-mermaid">flowchart TD&#10;accTitle: Redirect loops illustration for redirect rules&#10;A[Request for &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;a.example.com&lt;/code&gt;] --&gt; B[Redirect to &lt;code&gt;http://&lt;/code&gt;&lt;code&gt;b.example.com&lt;/code&gt;]&#10;B --&gt; C[Redirect to &lt;code&gt;https://&lt;/code&gt;&lt;code&gt;a.example.com&lt;/code&gt;]&#10;C --&gt; B&#10;subgraph Cloudflare&#10;B&#10;C&#10;end&#10;</code></pre>
<br />
<p>To solve this issue, review your various <a href="/rules/url-forwarding/">redirect rules</a> and <a href="/rules/page-rules/">Page Rules</a> to make sure no rules are not in conflict with each other.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13955.md")
</aside>
