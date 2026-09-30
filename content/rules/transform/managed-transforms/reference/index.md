<p>This page lists the available Managed Transforms. They can modify HTTP request headers or response headers.</p>
<p>For more complex and customized header modifications, consider using <a href="/rules/snippets/">Snippets</a>.</p>
<h2 id="important-remarks">Important remarks</h2>
<ul>
<li>
<p>Enabling a Managed Transform may cause issues in your website. You should test any changes in a staging environment. If you detect any undesired or unexpected behavior, consider disabling the Managed Transform and creating a partial implementation using your own transform rule.</p>
</li>
<li>
<p>The names of HTTP headers are case-insensitive. Cloudflare may use a capitalization different from the one presented in this page. Make sure that your origin server can handle HTTP request headers regardless of the exact capitalization of their names.</p>
</li>
</ul>
<h2 id="http-request-headers">HTTP request headers</h2>
<h3 id="add-bot-protection-headers">Add bot protection headers</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13147.md")
</aside>
<p>Adds HTTP headers with bot-related values to the request sent to the origin server:</p>
<ul>
<li><code>cf-bot-score</code>: Contains the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/13148.md")
</div> (for example, `30`).
- `cf-verified-bot`: Contains `true` if the request comes from a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/13149.md")
</div>, or `false` otherwise.
- `cf-ja3-hash`: Contains the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/13150.md")
</div>.
- `cf-ja4`: Contains the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/13151.md")
</div>.
<h3 id="add-tls-client-auth-headers">Add TLS client auth headers</h3>
<p>Adds HTTP headers with <a href="/api-shield/security/mtls/">Mutual TLS</a> (mTLS) client authentication values to the request sent to the origin server:</p>
<ul>
<li><code>cf-cert-revoked</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_revoked/"><code>cf.tls_client_auth.cert_revoked</code></a> field.</li>
<li><code>cf-cert-verified</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_verified/"><code>cf.tls_client_auth.cert_verified</code></a> field.</li>
<li><code>cf-cert-presented</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_presented/"><code>cf.tls_client_auth.cert_presented</code></a> field.</li>
<li><code>cf-cert-issuer-dn</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_issuer_dn/"><code>cf.tls_client_auth.cert_issuer_dn</code></a> field.</li>
<li><code>cf-cert-subject-dn</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_subject_dn/"><code>cf.tls_client_auth.cert_subject_dn</code></a> field.</li>
<li><code>cf-cert-issuer-dn-rfc2253</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_issuer_dn_rfc2253/"><code>cf.tls_client_auth.cert_issuer_dn_rfc2253</code></a> field.</li>
<li><code>cf-cert-subject-dn-rfc2253</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_subject_dn_rfc2253/"><code>cf.tls_client_auth.cert_subject_dn_rfc2253</code></a> field.</li>
<li><code>cf-cert-issuer-dn-legacy</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_issuer_dn_legacy/"><code>cf.tls_client_auth.cert_issuer_dn_legacy</code></a> field.</li>
<li><code>cf-cert-subject-dn-legacy</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_subject_dn_legacy/"><code>cf.tls_client_auth.cert_subject_dn_legacy</code></a> field.</li>
<li><code>cf-cert-serial</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_serial/"><code>cf.tls_client_auth.cert_serial</code></a> field.</li>
<li><code>cf-cert-issuer-serial</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_issuer_serial/"><code>cf.tls_client_auth.cert_issuer_serial</code></a> field.</li>
<li><code>cf-cert-fingerprint-sha256</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_fingerprint_sha256/"><code>cf.tls_client_auth.cert_fingerprint_sha256</code></a> field.</li>
<li><code>cf-cert-fingerprint-sha1</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_fingerprint_sha1/"><code>cf.tls_client_auth.cert_fingerprint_sha1</code></a> field.</li>
<li><code>cf-cert-not-before</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_not_before/"><code>cf.tls_client_auth.cert_not_before</code></a> field.</li>
<li><code>cf-cert-not-after</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_not_after/"><code>cf.tls_client_auth.cert_not_after</code></a> field.</li>
<li><code>cf-cert-ski</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_ski/"><code>cf.tls_client_auth.cert_ski</code></a> field.</li>
<li><code>cf-cert-issuer-ski</code>: Value from the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_issuer_ski/"><code>cf.tls_client_auth.cert_issuer_ski</code></a> field.</li>
</ul>
<h3 id="add-visitor-location-headers">Add visitor location headers</h3>
<p>Adds HTTP headers with location information for the visitor's IP address to the request sent to the origin server:</p>
<ul>
<li><code>cf-ipcity</code>: The visitor's city (value from the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.city/"><code>ip.src.city</code></a> field).</li>
<li><code>cf-ipcountry</code>: The visitor's country (value from the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.country/"><code>ip.src.country</code></a> field).</li>
<li><code>cf-ipcontinent</code>: The visitor's continent (value from the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.continent/"><code>ip.src.continent</code></a> field).</li>
<li><code>cf-iplongitude</code>: The visitor's longitude (value from the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.lon/"><code>ip.src.lon</code></a> field).</li>
<li><code>cf-iplatitude</code>: The visitor's latitude (value from the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.lat/"><code>ip.src.lat</code></a> field).</li>
<li><code>cf-region</code>: The visitor's region (value from the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.region/"><code>ip.src.region</code></a> field).</li>
<li><code>cf-region-code</code>: The visitor's region code (value from the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.region_code/"><code>ip.src.region_code</code></a> field).</li>
<li><code>cf-metro-code</code>: The visitor's metro code (value from the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.metro_code/"><code>ip.src.metro_code</code></a> field).</li>
<li><code>cf-postal-code</code>: The visitor's postal code (value from the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.postal_code/"><code>ip.src.postal_code</code></a> field).</li>
<li><code>cf-timezone</code>: The name of the visitor's timezone (value from the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.timezone.name/"><code>ip.src.timezone.name</code></a> field).</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13146.md")
</aside>
<h4 id="encoding-of-non-ascii-header-values">Encoding of non-ASCII header values</h4>
<p>Cloudflare always converts non-ASCII characters to UTF-8 in HTTP request and response header values. This applies to location headers added by the <strong>Add visitor location headers</strong> managed transform.</p>
<h3 id="add-true-client-ip-header">Add &quot;True-Client-IP&quot; header</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13145.md")
</aside>
<p>Adds a <code>true-client-ip</code> request header with the visitor's IP address.</p>
<p>This Managed Transform is unavailable when <a href="#remove-visitor-ip-headers"><strong>Remove visitor IP headers</strong></a> is enabled.</p>
<h3 id="remove-visitor-ip-headers">Remove visitor IP headers</h3>
<p>Removes HTTP headers that may contain the visitor's IP address from the request sent to the origin server. Handles the following HTTP request headers:</p>
<ul>
<li><code>cf-connecting-ip</code></li>
<li><code>x-forwarded-for</code> (refer to the <a href="#visitor-ip-address-in-the-x-forwarded-for-http-header">notes</a> below)</li>
<li><code>true-client-ip</code></li>
</ul>
<p>This Managed Transform is unavailable when <a href="#add-true-client-ip-header"><strong>Add &quot;True-Client-IP&quot; header</strong></a> is enabled.</p>
<h4 id="visitor-ip-address-in-the-x-forwarded-for-http-header">Visitor IP address in the <code>x-forwarded-for</code> HTTP header</h4>
<p>For the <code>x-forwarded-for</code> HTTP request header, enabling <strong>Remove visitor IP headers</strong> will only remove the visitor IP from the header value when Cloudflare receives a request proxied by at least another CDN (content delivery network). In this case, Cloudflare will only keep the IP address of the last proxy.</p>
<p>For example, consider an incoming request proxied by two CDNs (<code>CDN_1</code> and <code>CDN_2</code>) before reaching the Cloudflare network. The <code>x-forwarded-for</code> header would be similar to the following:<br/>
<code>x-forwarded-for: &lt;VISITOR_IP&gt;, &lt;THIRD_PARTY_CDN_1_IP&gt;, &lt;THIRD_PARTY_CDN_2_IP&gt;</code></p>
<p>With <strong>Remove visitor IP headers</strong> enabled, the <code>x-forwarded-for</code> header sent to the origin server will be:<br/>
<code>x-forwarded-for: &lt;THIRD_PARTY_CDN_2_IP&gt;</code></p>
<h3 id="add-leaked-credentials-checks-header">Add leaked credentials checks header</h3>
<p>Adds an <code>Exposed-Credential-Check</code> request header whenever the WAF detects leaked credentials in the incoming request.</p>
<p>The header can have these values:</p>
<table>
<thead>
<tr>
<th>Header + Value</th>
<th>Description</th>
<th>Availability</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Exposed-Credential-Check: 1</code></td>
<td>Previously leaked username and password detected</td>
<td>Pro plan and above</td>
</tr>
<tr>
<td><code>Exposed-Credential-Check: 2</code></td>
<td>Previously leaked username detected</td>
<td>Enterprise plan</td>
</tr>
<tr>
<td><code>Exposed-Credential-Check: 3</code></td>
<td>Similar combination of previously leaked username and password detected</td>
<td>Enterprise plan</td>
</tr>
<tr>
<td><code>Exposed-Credential-Check: 4</code></td>
<td>Previously leaked password detected</td>
<td>All plans</td>
</tr>
</tbody>
</table>
<p>You will only receive this managed header at your origin server if:</p>
<ul>
<li>The <a href="/waf/detections/leaked-credentials/">leaked credentials detection</a> in the WAF is turned on.</li>
<li>The <strong>Add Leaked Credentials Checks Header</strong> managed transform is turned on.</li>
<li>Your Cloudflare plan supports the type of credentials detection. For example, Free plans can only know if a password was previously leaked. In this situation, Cloudflare will add an <code>Exposed-Credential-Check: 4</code> header to the request.</li>
</ul>
<h3 id="add-malicious-uploads-detection-header">Add malicious uploads detection header</h3>
<p>Adds a <code>Malicious-Uploads-Detection</code> request header indicating the outcome of scanning uploaded content for malicious signatures.</p>
<p>The header can have one of the following values:</p>
<table>
<thead>
<tr>
<th>Header + Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Malicious-Uploads-Detection: 1</code></td>
<td>The request contains at least one malicious content object (<a href="/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.has_malicious_obj/"><code>cf.waf.content_scan.has_malicious_obj</code></a> is <code>true</code>).</td>
</tr>
<tr>
<td><code>Malicious-Uploads-Detection: 2</code></td>
<td>The file scanner was unable to scan all the content objects detected in the request (<a href="/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.has_failed/"><code>cf.waf.content_scan.has_failed</code></a> is <code>true</code>).</td>
</tr>
<tr>
<td><code>Malicious-Uploads-Detection: 3</code></td>
<td>The request contains at least one content object (<a href="/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.has_obj/"><code>cf.waf.content_scan.has_obj</code></a> is <code>true</code>).</td>
</tr>
</tbody>
</table>
<p>For more information, refer to <a href="/waf/detections/malicious-uploads/">Malicious uploads detection</a>.</p>
<h2 id="http-response-headers">HTTP response headers</h2>
<h3 id="remove-x-powered-by-headers">Remove &quot;X-Powered-By&quot; headers</h3>
<p>Removes the <code>X-Powered-By</code> HTTP response header that provides information about the application at the origin server that handled the request.</p>
<h3 id="add-security-headers">Add security headers</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13144.md")
</aside>
<p>Adds several security-related HTTP response headers. The added response headers and values are the following:</p>
<ul>
<li><code>x-content-type-options: nosniff</code></li>
<li><code>x-xss-protection: 1; mode=block</code></li>
<li><code>x-frame-options: SAMEORIGIN</code></li>
<li><code>referrer-policy: same-origin</code></li>
<li><code>expect-ct: max-age=86400, enforce</code></li>
</ul>
<p>To increase protection, <a href="/ssl/edge-certificates/additional-options/http-strict-transport-security/">enable HTTP Strict Transport Security (HSTS)</a> for your website.</p>
