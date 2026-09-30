<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7519.md")
</aside>
<p>Set an override expression for the HTTP DDoS Attack Protection managed ruleset to define a specific scope for <a href="/ddos-protection/managed-rulesets/http/override-parameters/#sensitivity-level">sensitivity level</a> or <a href="/ddos-protection/managed-rulesets/http/override-parameters/#action">action</a> adjustments.</p>
<p>For example, you can set different sensitivity levels for different request URI paths: a medium sensitivity level for URI path <code>A</code> and a low sensitivity level for URI path <code>B</code>.</p>
<h2 id="available-expression-fields">Available expression fields</h2>
<p>You can use the following fields in override expressions:</p>
<ul>
<li><code>cf.bot_management.ja3_hash</code></li>
<li><code>cf.bot_management.ja4</code></li>
<li><code>cf.client.bot</code></li>
<li><code>cf.tls_cipher</code></li>
<li><code>cf.tls_client_auth.cert_verified</code></li>
<li><code>cf.tls_version</code></li>
<li><code>cf.verified_bot_category</code></li>
<li><code>http.cookie</code></li>
<li><code>http.host</code></li>
<li><code>http.referer</code></li>
<li><code>http.request.headers</code></li>
<li><code>http.request.headers.names</code></li>
<li><code>http.request.headers.truncated</code></li>
<li><code>http.request.headers.values</code></li>
<li><code>http.request.uri</code></li>
<li><code>http.request.uri.path</code></li>
<li><code>http.request.uri.path.extension</code></li>
<li><code>http.request.uri.query</code></li>
<li><code>http.request.full_uri</code></li>
<li><code>http.request.method</code></li>
<li><code>http.request.version</code></li>
<li><code>http.request.cookies</code></li>
<li><code>http.user_agent</code></li>
<li><code>http.x_forwarded_for</code></li>
<li><code>ip.src</code></li>
<li><code>ip.src.asnum</code></li>
<li><code>ip.src.continent</code></li>
<li><code>ip.src.country</code></li>
<li><code>ip.src.is_in_european_union</code></li>
<li><code>ssl</code></li>
</ul>
<p>Refer to the <a href="/ruleset-engine/rules-language/fields/reference/">Fields reference</a> in the Rules language documentation for more information.</p>
