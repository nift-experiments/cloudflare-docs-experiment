---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/leaked-credentials/
  description: Scan incoming requests for usernames and passwords exposed in known data breaches.
  full_title: Leaked credentials detection · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Leaked credentials detection · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Scan incoming requests for usernames and passwords exposed in known data breaches."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/leaked-credentials/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/leaked-credentials/index.md"><meta property="og:title" content="Leaked credentials detection · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Scan incoming requests for usernames and passwords exposed in known data breaches."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/leaked-credentials/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Leaked credentials detection"><meta name="pcx_tags" content="Authentication,Account takeover"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/leaked-credentials/#page","headline":"Leaked credentials detection \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Scan incoming requests for usernames and passwords exposed in known data breaches.","url":"https://developers.cloudflare.com/waf/detections/leaked-credentials/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Authentication","Account takeover"]}</script>
  markdown: true
  noindex: false
  route: /waf/detections/leaked-credentials/
  schema: 1
---
<p>The leaked credentials <a href="/waf/detections/">traffic detection</a> scans incoming requests for credentials (usernames and passwords) previously leaked from <a href="https://www.cloudflare.com/learning/security/what-is-a-data-breach/">data breaches</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15518.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>When you turn on leaked credentials detection, Cloudflare scans incoming HTTP requests for usernames and passwords. The scan checks authentication patterns from <a href="#default-scan-locations">common web applications</a> and any <a href="#custom-detection-locations">custom detection locations</a> you configure.</p>
<p>Detected credentials are compared against a database of known leaked credentials. This database consists of:</p>
<ul>
<li>The <a href="https://haveibeenpwned.com">Have I Been Pwned (HIBP)</a> matched passwords dataset (passwords only)</li>
<li>Cloudflare-collected credentials (usernames)</li>
<li>Leaked credentials pairs (username and password)</li>
</ul>
<p>Based on the results, Cloudflare populates <a href="#leaked-credentials-fields">leaked credentials fields</a> for scanned requests. You can use these fields in two ways:</p>
<ul>
<li><strong>Analyze traffic</strong>: Review detection results in the <a href="/waf/analytics/security-analytics/">Security Analytics</a> dashboard to understand how often leaked credentials appear in your traffic.</li>
<li><strong>Create rules</strong>: Use the fields in <a href="/waf/custom-rules/">custom rules</a> or <a href="/waf/rate-limiting-rules/">rate limiting rules</a> to challenge or block requests that contain compromised credentials.</li>
</ul>
<p>Leaked credentials can appear in your traffic for different reasons. An attacker may be performing a <a href="https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/">credential stuffing</a> attack, or a legitimate user may be reusing a previously leaked password.</p>
<h3 id="notify-your-origin-server">Notify your origin server</h3>
<p>Leaked credentials detection provides a <a href="/rules/transform/managed-transforms/reference/#add-leaked-credentials-checks-header">managed transform</a> that adds an <code>Exposed-Credential-Check</code> request header to matching requests. The header value indicates what was leaked — for example, <code>1</code> if both username and password were a leaked pair, <code>2</code> if the username was leaked, or <code>4</code> if only the password was leaked.</p>
<p>You can use this header at your origin server to warn users and prompt them to reset their password.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15517.md")
</aside>
<h2 id="availability">Availability</h2>
<p>For details on available features per plan, refer to <a href="/waf/detections/#availability">Availability</a> in the traffic detections page.</p>
<h2 id="default-scan-locations">Default scan locations</h2>
<p>Leaked credentials detection includes rules for identifying credentials in HTTP requests for the following well-known web applications:</p>
<ul>
<li>Drupal</li>
<li>Joomla</li>
<li>Ghost</li>
<li>Magento</li>
<li>Plone</li>
<li>WordPress</li>
<li>Microsoft Exchange OWA</li>
</ul>
<p>Additionally, the scan includes generic rules for other common web authentication patterns.</p>
<p>You can also configure <a href="#custom-detection-locations">custom detection locations</a> to address the specific authentication mechanism used in your web applications. A custom detection location tells the Cloudflare WAF where to find usernames and passwords in HTTP requests of your web application.</p>
<h2 id="custom-detection-locations">Custom detection locations</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15516.md")
</aside>
<p>The default scan covers <a href="#default-scan-locations">common web applications</a>, but your application may send credentials in a different format or field name. Custom detection locations allow you to tell Cloudflare exactly where to find usernames and passwords in HTTP requests.</p>
<p>For example, if the JSON body of an HTTP request authenticating a user looks like the following:</p>
<pre tabindex="0"><code class="language-json">{ &quot;user&quot;: &quot;&lt;username&gt;&quot;, &quot;secret&quot;: &quot;&lt;password&gt;&quot; }&#10;</code></pre>
<p>You could configure a custom detection location with the following settings:</p>
<ul>
<li>Custom location for username:<br/>
<code>lookup_json_string(http.request.body.raw, &quot;user&quot;)</code></li>
<li>Custom location for password:<br/>
<code>lookup_json_string(http.request.body.raw, &quot;secret&quot;)</code></li>
</ul>
<p>When specifying a custom detection location, only the location of the username field is required.</p>
<p>The following table includes example detection locations for different request types:</p>
<table>
<thead>
<tr>
<th>Request type</th>
<th>Username location / Password location</th>
</tr>
</thead>
<tbody>
<tr>
<td>JSON body</td>
<td><code>lookup_json_string(http.request.body.raw, &quot;user&quot;)</code><br/><code>lookup_json_string(http.request.body.raw, &quot;secret&quot;)</code></td>
</tr>
<tr>
<td>URL-encoded form</td>
<td><code>url_decode(http.request.body.form[&quot;user&quot;][0])</code><br/><code>url_decode(http.request.body.form[&quot;secret&quot;][0])</code></td>
</tr>
<tr>
<td>Multipart form</td>
<td><code>url_decode(http.request.body.multipart[&quot;user&quot;][0])</code><br/><code>url_decode(http.request.body.multipart[&quot;secret&quot;][0])</code></td>
</tr>
</tbody>
</table>
<p>Expressions used to specify custom detection locations can include the following fields and functions:</p>
<ul>
<li>Fields:
<ul>
<li><a href="/ruleset-engine/rules-language/fields/reference/http.request.body.form/"><code>http.request.body.form</code></a></li>
<li><a href="/ruleset-engine/rules-language/fields/reference/http.request.body.multipart/"><code>http.request.body.multipart</code></a></li>
<li><a href="/ruleset-engine/rules-language/fields/reference/http.request.body.raw/"><code>http.request.body.raw</code></a></li>
<li><a href="/ruleset-engine/rules-language/fields/reference/http.request.headers/"><code>http.request.headers</code></a></li>
<li><a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.args/"><code>http.request.uri.args</code></a></li>
<li><a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.query/"><code>http.request.uri.query</code></a></li>
</ul>
</li>
<li>Functions:
<ul>
<li><a href="/ruleset-engine/rules-language/functions/#lookup_json_string"><code>lookup_json_string()</code></a></li>
<li><a href="/ruleset-engine/rules-language/functions/#url_decode"><code>url_decode()</code></a></li>
</ul>
</li>
</ul>
<p>For instructions on configuring a custom detection location, refer to <a href="/waf/detections/leaked-credentials/get-started/#4-optional-configure-a-custom-detection-location">Get started</a>.</p>
<h2 id="leaked-credentials-fields">Leaked credentials fields</h2>
<p>The following fields indicate the type of leaked credential match Cloudflare detected. Use these fields in <a href="/waf/custom-rules/">custom rules</a> or <a href="/waf/rate-limiting-rules/">rate limiting rules</a> to act on requests containing compromised credentials.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Password Leaked <br/> [<code>cf.waf.credential_check.password_leaked</code>][1] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether the password detected in the request was previously leaked. <br/> Available on all plans.</td>
</tr>
<tr>
<td>User and Password Leaked <br/> [<code>cf.waf.credential_check.username_and_password_leaked</code>][2] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether the username-password pair detected in the request were previously leaked. <br/> Requires a Pro plan or above.</td>
</tr>
<tr>
<td>Username Leaked <br/> [<code>cf.waf.credential_check.username_leaked</code>][3] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether the username detected in the request was previously leaked. <br/> Requires an Enterprise plan.</td>
</tr>
<tr>
<td>Similar Password Leaked <br/> [<code>cf.waf.credential_check.username_password_similar</code>][4] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether a similar version of the username and password credentials detected in the request were previously leaked. <br/> Requires an Enterprise plan.</td>
</tr>
<tr>
<td>Authentication detected <br/> [<code>cf.waf.auth_detected</code>][5] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether Cloudflare detected authentication credentials in the request. <br/> Requires an Enterprise plan.</td>
</tr>
</tbody>
</table>
