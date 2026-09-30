---
cp9:
  canonical: https://developers.cloudflare.com/rules/transform/managed-transforms/reference/
  description: Learn about Cloudflare's Managed Transforms for modifying HTTP headers, including bot protection, TLS client auth, and leaked credentials checks.
  full_title: Available Managed Transforms · Cloudflare Rules docs
  head_html: <title>Available Managed Transforms · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about Cloudflare&#x27;s Managed Transforms for modifying HTTP headers, including bot protection, TLS client auth, and leaked credentials checks."><link rel="canonical" href="https://developers.cloudflare.com/rules/transform/managed-transforms/reference/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/transform/managed-transforms/reference/index.md"><meta property="og:title" content="Available Managed Transforms · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about Cloudflare&#x27;s Managed Transforms for modifying HTTP headers, including bot protection, TLS client auth, and leaked credentials checks."><meta property="og:url" content="https://developers.cloudflare.com/rules/transform/managed-transforms/reference/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="mTLS,Headers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/transform/managed-transforms/reference/#page","headline":"Available Managed Transforms \u00b7 Cloudflare Rules docs","description":"Learn about Cloudflare's Managed Transforms for modifying HTTP headers, including bot protection, TLS client auth, and leaked credentials checks.","url":"https://developers.cloudflare.com/rules/transform/managed-transforms/reference/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["mTLS","Headers"]}</script>
  markdown: true
  noindex: false
  route: /rules/transform/managed-transforms/reference/
  schema: 1
---
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
<li><code>cf-bot-score</code>: Contains the <span class="nb-glossary-tooltip" title="bot score">bot score</span> (for example, <code>30</code>).</li>
<li><code>cf-verified-bot</code>: Contains <code>true</code> if the request comes from a <span class="nb-glossary-tooltip" title="verified bot">verified bot</span>, or <code>false</code> otherwise.</li>
<li><code>cf-ja3-hash</code>: Contains the <span class="nb-glossary-tooltip" title="JA3 fingerprint">JA3 fingerprint</span>.</li>
<li><code>cf-ja4</code>: Contains the <span class="nb-glossary-tooltip" title="JA3 fingerprint">JA4 fingerprint</span>.</li>
</ul>
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
