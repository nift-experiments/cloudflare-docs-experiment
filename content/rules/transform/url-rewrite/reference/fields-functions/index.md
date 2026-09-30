<h2 id="filter-expressions">Filter expressions</h2>
<p>A URL rewrite rule <a href="/ruleset-engine/rules-language/expressions/">filter expression</a> (that is, the expression that defines which incoming requests match the rule) can include the following fields:</p>
<ul>
<li><code>cf.edge.server_ip</code></li>
<li><code>cf.edge.server_port</code></li>
<li><code>cf.edge.client_port</code></li>
<li><code>cf.edge.client_tcp</code></li>
<li><code>cf.edge.l4.delivery_rate</code></li>
<li><code>cf.hostname.metadata</code></li>
<li><code>cf.zone.name</code></li>
<li><code>cf.random_seed</code></li>
<li><code>cf.ray_id</code></li>
<li><code>cf.timings.client_quic_rtt_msec</code></li>
<li><code>cf.timings.client_tcp_rtt_msec</code></li>
<li><code>cf.tls_version</code></li>
<li><code>cf.tls_cipher</code></li>
<li><code>cf.tls_client_hello_length</code></li>
<li><code>cf.tls_client_random</code></li>
<li><code>cf.tls_client_extensions_sha1</code></li>
<li><code>cf.tls_client_extensions_sha1_le</code></li>
<li><code>cf.tls_client_ciphers_sha1</code></li>
<li><code>cf.tls_client_auth.*</code></li>
<li><code>cf.worker.upstream_zone</code></li>
<li><code>http.cookie</code></li>
<li><code>http.host</code></li>
<li><code>http.referer</code></li>
<li><code>http.request.accepted_languages</code></li>
<li><code>http.request.cookies</code></li>
<li><code>http.request.headers</code></li>
<li><code>http.request.headers.*</code></li>
<li><code>http.request.method</code></li>
<li><code>http.request.timestamp.sec</code></li>
<li><code>http.request.timestamp.msec</code></li>
<li><code>http.request.full_uri</code></li>
<li><code>http.request.uri</code></li>
<li><code>http.request.uri.*</code></li>
<li><code>http.request.version</code></li>
<li><code>raw.http.request.full_uri</code></li>
<li><code>raw.http.request.headers</code></li>
<li><code>raw.http.request.headers.*</code></li>
<li><code>raw.http.request.uri</code></li>
<li><code>raw.http.request.uri.*</code></li>
<li><code>http.user_agent</code></li>
<li><code>http.x_forwarded_for</code></li>
<li><code>ip.src</code></li>
<li><code>ip.src.lat</code></li>
<li><code>ip.src.lon</code></li>
<li><code>ip.src.asnum</code></li>
<li><code>ip.src.city</code></li>
<li><code>ip.src.country</code></li>
<li><code>ip.src.continent</code></li>
<li><code>ip.src.metro_code</code></li>
<li><code>ip.src.postal_code</code></li>
<li><code>ip.src.region</code></li>
<li><code>ip.src.region_code</code></li>
<li><code>ip.src.is_in_european_union</code></li>
<li><code>ip.src.subdivision_1_iso_code</code></li>
<li><code>ip.src.subdivision_2_iso_code</code></li>
<li><code>ssl</code></li>
<li><code>cf.worker.upstream_zone</code></li>
</ul>
<p>Refer to <a href="/ruleset-engine/rules-language/fields/reference/">Fields</a> for reference information on these fields.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/13185.md")
</aside>
<p>For information on the available functions, refer to <a href="/ruleset-engine/rules-language/functions/">Functions</a>.</p>
<h2 id="rewrite-expressions">Rewrite expressions</h2>
<p>A rewrite expression (that is, the expression that defines the dynamic URL rewrite to perform) can only include the following fields:</p>
<ul>
<li><code>http.request.uri.*</code></li>
<li><code>http.request.headers.*</code></li>
<li><code>http.request.accepted_languages</code></li>
</ul>
<p>Refer to the <a href="/ruleset-engine/rules-language/fields/reference/">Fields reference</a> for more information on these fields.</p>
<p>The <a href="/ruleset-engine/rules-language/functions/#concat"><code>concat()</code></a>, <a href="/ruleset-engine/rules-language/functions/#regex_replace"><code>regex_replace()</code></a>, and <a href="/ruleset-engine/rules-language/functions/#wildcard_replace"><code>wildcard_replace()</code></a> functions can appear only once in a rewrite expression. Additionally, you cannot nest the <code>regex_replace()</code> and <code>wildcard_replace()</code> functions.</p>
