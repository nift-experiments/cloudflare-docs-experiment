---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/
  description: Configure HTTP policies in Gateway.
  full_title: HTTP policies · Cloudflare One docs
  head_html: <title>HTTP policies · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure HTTP policies in Gateway."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/index.md"><meta property="og:title" content="HTTP policies · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure HTTP policies in Gateway."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="TLS,SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#page","headline":"HTTP policies \u00b7 Cloudflare One docs","description":"Configure HTTP policies in Gateway.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS","SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/http-policies/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6505.md")
</aside>
<p>HTTP policies allow you to filter all HTTP and HTTPS requests based on URLs, hostnames, HTTP methods, file types, and other request attributes. Unlike <a href="/cloudflare-one/traffic-policies/network-policies/">network policies</a> which operate at Layer 4 (TCP/UDP), HTTP policies operate at Layer 7 and can inspect the full content of web traffic.</p>
<p>By default, Gateway inspects HTTP traffic on port <code>80</code> and, with <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> turned on, HTTPS traffic on port <code>443</code>. You can also configure Gateway to <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">inspect HTTP/HTTPS traffic on all ports</a>. Gateway supports HTTP/3 inspection with the <a href="/cloudflare-one/traffic-policies/http-policies/http3/">UDP proxy</a> turned on.</p>
<p>An HTTP policy consists of an <strong>Action</strong> and a logical expression that determines the scope of the policy. To build an expression, choose a <strong>Selector</strong> and an <strong>Operator</strong>, then enter a value or range of values in the <strong>Value</strong> field. You can use <strong>And</strong> and <strong>Or</strong> logical operators to evaluate multiple conditions.</p>
<ul>
<li><a href="#actions">Actions</a></li>
<li><a href="#selectors">Selectors</a></li>
<li><a href="#comparison-operators">Comparison operators</a></li>
<li><a href="#value">Value</a></li>
<li><a href="#logical-operators">Logical operators</a></li>
</ul>
<p>If a condition in an expression joins a query attribute (such as <em>Source IP</em>) and a response attribute (such as <em>Resolved IP</em>), then the condition will be evaluated when the response is received.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="terraform-provider-v4-precedence-limitation">Terraform provider v4 precedence limitation</h3>
@markup("md", "content/.markup/bodies/6504.md")
</aside>
<h2 id="actions">Actions</h2>
<p>Actions in HTTP policies allow you to choose what to do with a given set of elements (domains, IP addresses, file types, and so on). You can assign one action per policy.</p>
<h3 id="allow">Allow</h3>
<p>API value: <code>allow</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6506.md")
</div></details>
<p>The Allow action allows outbound traffic to reach destinations you specify within the <a href="#selectors">Selectors</a> and <a href="#value">Value</a> fields. For example, the following configuration allows traffic to reach all websites we categorize as belonging to the Education content category:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Content Categories</td>
<td>in</td>
<td><em>Education</em></td>
<td>Allow</td>
</tr>
</tbody>
</table>
<h4 id="untrusted-certificates">Untrusted certificates</h4>
<p>The <strong>Untrusted certificate action</strong> determines how to handle insecure requests.</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Error</td>
<td>Display Gateway error page. Matches the default behavior when no action is configured.</td>
</tr>
<tr>
<td>Block</td>
<td>Display <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">block page</a> as set in the Cloudflare dashboard.</td>
</tr>
<tr>
<td>Pass through</td>
<td>Bypass insecure connection warnings and seamlessly connect to the upstream. For more information on what statuses are bypassed, refer to <a href="/cloudflare-one/traffic-policies/troubleshooting/#error-526-invalid-ssl-certificate">Troubleshooting Gateway</a>.</td>
</tr>
</tbody>
</table>
<h4 id="custom-headers">Custom headers</h4>
<p>Allow policies can modify HTTP request headers before forwarding traffic to the destination. You can add, overwrite, or delete headers, and use dynamic variables to inject identity, device, and network context into header values.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/tenant-control/">Custom headers</a>.</p>
<h3 id="block">Block</h3>
<p>API value: <code>block</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6507.md")
</div></details>
<p>The Block action blocks outbound traffic from reaching destinations you specify within the <a href="#selectors">Selectors</a> and <a href="#value">Value</a> fields. For example, the following configuration blocks users from being able to upload any file type to Google Drive:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td>in</td>
<td><code>Google Drive</code></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Upload Mime Type</td>
<td>matches regex</td>
<td><code>.*</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h4 id="cloudflare-one-client-block-notifications">Cloudflare One Client block notifications</h4>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6508.md")
</div></details>
<p>Turn on <p><strong>Display block notification for Cloudflare One Client</strong></p>
to display notifications for Gateway block events. Blocked users will receive an operating system notification from the Cloudflare One Client with a custom message you set. If you do not set a custom message, the Cloudflare One Client will display a default message. Custom messages must be 100 characters or less. The Cloudflare One Client will only display one notification per minute.</p>
<p>Upon selecting the notification, the Cloudflare One Client will direct your users to the <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">Gateway block page</a> you have configured. Optionally, you can direct users to a custom URL, such as an internal support form.</p>
<p>When you turn on <strong>Send policy context</strong>, Gateway will append details of the matching request to the redirected URL as a query string. Not every context field will be included. Potential policy context fields include:</p>
<details class="nb-details"><summary>Policy context fields</summary><div class="nb-details-body">
@input("content/.markup/bodies/6509.md")
</div></details>
<div class="nb-data-component" data-cf-component="Render"></div>
<h3 id="redirect">Redirect</h3>
<p>API value: <code>redirect</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6510.md")
</div></details>
<p>The Redirect action allows you to redirect matched HTTP requests to a different URL you specify. For example, if your users browse to the public web page of a SaaS app, you can redirect them to your own self-hosted instance, a single sign-on page, or an internal policy page.</p>
<p>To redirect URLs with a Block action and the block page, refer to <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#redirect-to-a-block-page">Redirect to a block page</a>.</p>
<h4 id="policy-settings">Policy settings</h4>
<p>In <strong>Policy URL redirect</strong>, you can define what URL to redirect matched requests to. The redirect URL can contain paths and queries. For example, you can redirect <code>example.com</code> to <code>cloudflare.com/path/to/page?querystring=x</code>.</p>
<p>When you turn on <strong>Send policy context</strong>, Gateway will append details of the matching request to the redirected URL as a query string. Not every context field will be included. Potential policy context fields include:</p>
<details class="nb-details"><summary>Policy context fields</summary><div class="nb-details-body">
@input("content/.markup/bodies/6511.md")
</div></details>
<p>When you turn on <strong>Preserve original path and query string</strong>, Gateway will append the original path and query string to the redirected URL. Paths and queries in the redirect URL take precedence over the original URL. For example, if the original URL is <code>example.com/path/to/page?querystring=X</code> and the redirect URL is <code>cloudflare.com/redirect-path?querystring=Y</code>, Gateway will redirect requests to:</p>
<pre tabindex="0"><code class="language-txt">cloudflare.com/redirect-path/path/to/page?querystring=Y&#10;</code></pre>
<p>When you turn on both options, Gateway will preserve the original path and query string, then append policy context to the end of the redirect URL. For example, if the original URL is <code>example.com/path/to/page?querystring=X&amp;k=1</code> and the redirect URL is <code>cloudflare.com/redirect-path?querystring=Y</code>, Gateway will redirect requests to:</p>
<pre tabindex="0"><code class="language-txt">cloudflare.com/redirect-path/path/to/page?querystring=Y&amp;k=1&amp;cf_user_email=user@example.com&#10;</code></pre>
<h3 id="isolate">Isolate</h3>
<p>API value: <code>isolate</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6512.md")
</div></details>
<p>The Isolate action serves matched traffic to users via <a href="/cloudflare-one/remote-browser-isolation/">Cloudflare Browser Isolation</a>. For more information on this action, refer to <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#isolate">Isolation policies</a>.</p>
<h3 id="do-not-inspect">Do Not Inspect</h3>
<p>API value: <code>off</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6513.md")
</div></details>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="visibility-limitation">Visibility limitation</h3>
@markup("md", "content/.markup/bodies/6503.md")
</aside>
<p>Do Not Inspect lets you bypass certain elements from inspection. To prevent Gateway from decrypting and inspecting HTTPS traffic, your policy must match against the Server Name Indication (SNI) in the TLS header. When accessing a Do Not Inspect site in the browser, your browser may display a <strong>Your connection is not private</strong> warning, which you can proceed through to connect. For more information about applications which may require a Do Not Inspect policy, refer to <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#inspection-limitations">TLS decryption limitations</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6502.md")
</aside>
<h3 id="do-not-isolate">Do Not Isolate</h3>
<p>API value: <code>noisolate</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6514.md")
</div></details>
<p>The Do Not Isolate action turns off browser isolation for matched traffic. For more information on this action, refer to <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#do-not-isolate">Isolation policies</a>.</p>
<h3 id="do-not-scan">Do Not Scan</h3>
<p>API value: <code>noscan</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6515.md")
</div></details>
<p>When an admin enables AV scanning for uploads and/or downloads, Gateway will scan every supported file. Admins can selectively choose to disable scanning by leveraging the HTTP rules. For example, to prevent AV scanning of files uploaded to or downloaded from <code>example.com</code>, an admin would configure the following rule:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hostname</td>
<td>matches regex</td>
<td><code>.*example.com</code></td>
<td>Do Not Scan</td>
</tr>
</tbody>
</table>
<p>When a Do Not Scan rule matches, nothing is scanned, regardless of file size or whether the file type is supported or not.</p>
<h3 id="quarantine">Quarantine</h3>
<p>API value: <code>quarantine</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6516.md")
</div></details>
<p>The Quarantine action sends files in matching requests to a file sandbox to scan for malware. Gateway will only quarantine files not previously seen in the file sandbox. For more information on this action, refer to <a href="/cloudflare-one/traffic-policies/http-policies/file-sandboxing/">File sandboxing</a>.</p>
<h4 id="sandbox-file-types">Sandbox file types</h4>
<p>In <strong>Sandbox file types</strong>, you can select which file types to quarantine with your policy. You must select at least one file type.</p>
<p>File sandboxing supports scanning the following file types:</p>
<details class="nb-details"><summary>Supported sandboxing file types</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6517.md")
</div></details>
<h2 id="selectors">Selectors</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6501.md")
</aside>
<p>Gateway matches HTTP traffic against the following selectors, or criteria:</p>
<h3 id="access-infrastructure-target">Access Infrastructure Target</h3>
<p>All <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target">targets</a> secured by an <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access infrastructure application</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Access Infrastructure Target</td>
<td><code>access.target</code></td>
</tr>
</tbody>
</table>
<h3 id="access-private-app">Access Private App</h3>
<p>All destination IPs and hostnames secured by an <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Access self-hosted private application</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Self-hosted Access App with Private Address</td>
<td><code>access.private_app</code></td>
</tr>
</tbody>
</table>
<h3 id="application-approval-status">Application Approval Status</h3>
<p>The review approval status of an application from <a href="/cloudflare-one/insights/analytics/shadow-it-discovery/">Shadow IT Discovery</a> or the <a href="/cloudflare-one/team-and-resources/app-library/">Application Library</a>. For more information, refer to <a href="/cloudflare-one/team-and-resources/app-library/#review-applications">Review applications</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application Status</td>
<td><code>any(app.statuses[*] == &quot;approved&quot;)</code></td>
</tr>
</tbody>
</table>
<h3 id="application">Application</h3>
<p>You can apply HTTP policies to a growing list of popular web applications. Refer to <a href="/cloudflare-one/traffic-policies/application-app-types/">Application and app types</a> for more information.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td><code>any(app.ids[*] in {505})</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="multiple-api-selectors-required-for-terraform">Multiple API selectors required for Terraform</h3>
@markup("md", "content/.markup/bodies/6500.md")
</aside>
<h4 id="granular-controls">Granular controls</h4>
<p>When using the <em>is</em> operator with the <em>Application</em> selector, you can use Application Granular Controls to choose specific actions and operations to match application traffic. For example, you can block file uploads to ChatGPT without blocking all ChatGPT traffic:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Controls</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td>is</td>
<td><em>ChatGPT</em></td>
<td><em>Upload</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>You can match traffic based on <strong>Application Controls</strong>, which group multiple user actions together, or <strong>Operations</strong>, which allow for granular control of supported API-level actions for an application.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/granular-controls/">Application Granular Controls</a>.</p>
<h3 id="body-phase">Body Phase</h3>
<p>The phase of an HTTP request. You can use this selector to specify whether to scan either the data sent in an HTTP request to your user's device or from your user's device to a destination. Policies without this selector will scan both the HTTP request and response bodies.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Body Phase</td>
<td><code>http.body_phase == \&quot;download\&quot;</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="body-phase-mismatch">Body phase mismatch</h3>
@markup("md", "content/.markup/bodies/6499.md")
</aside>
<h3 id="browser-isolation">Browser Isolation <span class="nb-badge">Beta</span></h3>
<p>Whether the current session is running inside <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation</a>. Use this selector to apply different policy behavior to isolated and non-isolated traffic.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Browser Isolation</td>
<td><code>net.is_isolated == true</code></td>
</tr>
</tbody>
</table>
<h3 id="content-categories">Content Categories</h3>
<p>Applications within a specific <a href="/cloudflare-one/traffic-policies/domain-categories/#content-categories">security category</a> as categorized by <a href="/radar/glossary/#content-categories">Cloudflare Radar</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Content Categories</td>
<td><code>any(http.request.uri.content_category[*] in {1})</code></td>
</tr>
</tbody>
</table>
<h3 id="destination-continent">Destination Continent</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6498.md")
</aside>
<p>The continent where the request is destined. Geolocation is determined from the target IP address. To specify a continent, enter its two-letter code into the <strong>Value</strong> field:</p>
<table>
<thead>
<tr>
<th>Continent</th>
<th>Code</th>
</tr>
</thead>
<tbody>
<tr>
<td>Africa</td>
<td><code>AF</code></td>
</tr>
<tr>
<td>Antarctica</td>
<td><code>AN</code></td>
</tr>
<tr>
<td>Asia</td>
<td><code>AS</code></td>
</tr>
<tr>
<td>Europe</td>
<td><code>EU</code></td>
</tr>
<tr>
<td>North America</td>
<td><code>NA</code></td>
</tr>
<tr>
<td>Oceania</td>
<td><code>OC</code></td>
</tr>
<tr>
<td>South America</td>
<td><code>SA</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination Continent IP Geolocation</td>
<td><code>http.dst_ip.geo.continent == &quot;EU&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="destination-country">Destination Country</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6497.md")
</aside>
<p>The country that the request is destined for. Geolocation is determined from the target IP address. To specify a country, enter its <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2 code</a> in the <strong>Value</strong> field.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination Country IP Geolocation</td>
<td><code>http.dst_ip.geo.country == &quot;RU&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="destination-ip">Destination IP</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6496.md")
</aside>
<p>The IP address of the request's target.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination IP</td>
<td><code>any(http.conn.dst_ip[*] in {10.0.0.0/8})</code></td>
</tr>
</tbody>
</table>
<h3 id="device-posture">Device Posture</h3>
<p>With the Device Posture selector, admins can use signals from end-user devices to secure access to their internal and external resources. For example, a security admin can choose to limit all access to internal applications based on whether specific software is installed on a device and/or if the device or software are configured in a particular way.</p>
<p>For more information on device posture checks, refer to <a href="/cloudflare-one/reusable-components/posture-checks/">Device posture</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Passed Device Posture Checks</td>
<td><code>any(device_posture.checks.failed[*] in {&quot;1308749e-fcfb-4ebc-b051-fe022b632644&quot;})</code>, <code>any(device_posture.checks.passed[*] in {&quot;1308749e-fcfb-4ebc-b051-fe022b632644&quot;})&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="domain">Domain</h3>
<p>Use this selector to match against a domain and all subdomains. For example, you can match <code>example.com</code> and its subdomains, such as <code>www.example.com</code>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td><code>any(http.request.domains[*] == &quot;example.com&quot;)</code></td>
</tr>
</tbody>
</table>
<p>Gateway policies do not support domains with non-Latin characters directly. To use a domain with non-Latin characters, add it to a <a href="/cloudflare-one/reusable-components/lists/">list</a>.</p>
<h3 id="download-and-upload-file-size">Download and Upload File Size</h3>
<p>Use these selectors to limit the file size of upload or download transactions. File sizes are measured in mebibytes (MiB).</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Download File Size (MiB)</td>
<td><code>http.download.file.size &gt;= 10</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Upload File Size (MiB)</td>
<td><code>http.upload.file.size &lt; 10</code></td>
</tr>
</tbody>
</table>
<h3 id="download-and-upload-file-types">Download and Upload File Types</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecated-selectors">Deprecated selectors</h3>
@markup("md", "content/.markup/bodies/6495.md")
</aside>
<p>These selectors will scan file signatures in the HTTP body. You can select from file categories or <a href="#supported-file-types">specific file types</a>, such as executables, archives and compressed files, unscannable files, Microsoft 365/Office documents, and Adobe files.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Download File Types</td>
<td><code>any(http.download.file.types[*] in {&quot;docx&quot; &quot;7z&quot;})</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Upload File Types</td>
<td><code>any(http.upload.file.types[*] in {&quot;compressed&quot;})</code></td>
</tr>
</tbody>
</table>
<h4 id="supported-file-types">Supported file types</h4>
<p>Gateway supports the following file types for use with the <em>Download File Types</em> and <em>Upload File Types</em> selectors:</p>
<details class="nb-details"><summary>Compressed</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6518.md")
</div></details>
<details class="nb-details"><summary>Documents</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6519.md")
</div></details>
<details class="nb-details"><summary>Executable</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6520.md")
</div></details>
<details class="nb-details"><summary>Image</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6521.md")
</div></details>
<details class="nb-details"><summary>Other</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6522.md")
</div></details>
<details class="nb-details"><summary>System</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6523.md")
</div></details>
<details class="nb-details"><summary>Unscannable</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6524.md")
</div></details>
<h3 id="download-and-upload-mime-type">Download and Upload Mime Type</h3>
<p>These selectors depend on the <code>Content-Type</code> header being present in the request (for uploads) or response (for downloads). The MIME type value must match the format used in the <code>Content-Type</code> header (for example, <code>image/png</code>, <code>application/pdf</code>).</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Download Mime Type</td>
<td><code>http.download.mime == &quot;image/png&quot;</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Upload Mime Type</td>
<td><code>http.upload.mime == &quot;image/png&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="dlp-profile">DLP Profile</h3>
<p>Use <a href="/cloudflare-one/data-loss-prevention/">Cloudflare Data Loss Prevention (DLP)</a> to scan HTTP traffic for the presence of sensitive data such as personally identifiable information (PII) or source code. You must configure a <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profile</a> before you can use this selector in a policy.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>DLP Profile</td>
<td><code>any(dlp.profiles[*] in {\&quot;a0cabf16-7491-4c9a-ac02-f64cabc66394\&quot;})</code></td>
</tr>
</tbody>
</table>
<h3 id="is-mcp">Is MCP <span class="nb-badge">Beta</span></h3>
<p>Whether the HTTP request was identified as <a href="https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/">Model Context Protocol (MCP)</a> traffic. Gateway detects MCP traffic by inspecting protocol-specific headers and payload characteristics. Use this selector to build policies that allow, block, or isolate MCP traffic across your network.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Is MCP</td>
<td><code>experimental.is_mcp == true</code></td>
</tr>
</tbody>
</table>
<p>For example, the following policy blocks MCP traffic that does not arrive through an <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP portal</a>:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Is MCP</td>
<td>is</td>
<td><em>True</em></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Traffic Source</td>
<td>is not</td>
<td><em>MCP portal</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="host">Host</h3>
<p>Use this selector to match against only the hostname specified. For example, you can match <code>test.example.com</code> but not <code>example.com</code> or <code>www.test.example.com</code>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td><code>http.request.host == &quot;example.com&quot;</code></td>
</tr>
</tbody>
</table>
<p>Gateway policies do not support hostnames with non-Latin characters directly. To use a hostname with non-Latin characters, add it to a <a href="/cloudflare-one/reusable-components/lists/">list</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6494.md")
</aside>
<h3 id="http-method">HTTP Method</h3>
<p>The HTTP request method used in the traffic.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>HTTP Method</td>
<td><code>http.request.method == &quot;GET&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="http-response">HTTP Response</h3>
<p>The HTTP response status code received by the traffic.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>URL</td>
<td><code>http.response.status_code == &quot;200&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="package-ecosystem">Package Ecosystem</h3>
<p>The package registry ecosystem detected from the HTTP request URL. For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/package-registry-security/">Package registry security</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Package Ecosystem</td>
<td><code>pkg.ecosystem == &quot;npm&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="package-name">Package Name</h3>
<p>The name of the package detected from the HTTP request URL.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Package Name</td>
<td><code>pkg.name == &quot;lodash&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="package-namespace">Package Namespace</h3>
<p>The namespace of the package, when the ecosystem supports one. For npm, this is the scope. For Maven, this is the group ID. For Go, this is the module path.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Package Namespace</td>
<td><code>pkg.namespace == &quot;@babel&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="package-url-purl">Package URL (PURL)</h3>
<p>The <a href="https://github.com/package-url/purl-spec">Package URL</a> derived from the detected package coordinates.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Package URL</td>
<td><code>pkg.purl == &quot;pkg:npm/lodash@4.17.21&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="package-version">Package Version</h3>
<p>The version of the package detected from the HTTP request URL. Supports exact match and ecosystem-aware version comparison operators. For more information on version comparison semantics, refer to <a href="/cloudflare-one/traffic-policies/http-policies/package-registry-security/#version-comparison-operators">Package registry security</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Package Version</td>
<td><code>pkg.version == &quot;4.17.21&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="proxy-endpoint">Proxy Endpoint</h3>
<p>The <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy server</a> where your browser forwards HTTP traffic.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Proxy Endpoint</td>
<td><code>proxy.endpoint == &quot;3ele0ss56t.proxy.cloudflare-gateway.com&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="security-risks">Security Risks</h3>
<p>Applications within a specific <a href="/cloudflare-one/traffic-policies/domain-categories/#security-categories">security category</a> as categorized by <a href="/radar/glossary/#content-categories">Cloudflare Radar</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Security Categories</td>
<td><code>any(http.request.uri.security_category[*] in {1})</code></td>
</tr>
</tbody>
</table>
<h3 id="source-continent">Source Continent</h3>
<p>The continent of the user making the request.</p>
<p>Geolocation is determined from the device's public IP address (typically assigned by the user's ISP). To specify a continent, enter its two-letter code into the <strong>Value</strong> field:</p>
<table>
<thead>
<tr>
<th>Continent</th>
<th>Code</th>
</tr>
</thead>
<tbody>
<tr>
<td>Africa</td>
<td><code>AF</code></td>
</tr>
<tr>
<td>Antarctica</td>
<td><code>AN</code></td>
</tr>
<tr>
<td>Asia</td>
<td><code>AS</code></td>
</tr>
<tr>
<td>Europe</td>
<td><code>EU</code></td>
</tr>
<tr>
<td>North America</td>
<td><code>NA</code></td>
</tr>
<tr>
<td>Oceania</td>
<td><code>OC</code></td>
</tr>
<tr>
<td>South America</td>
<td><code>SA</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source Continent IP Geolocation</td>
<td><code>http.src_ip.geo.continent == &quot;North America&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="source-country">Source Country</h3>
<p>The country of the user making the request.</p>
<p>Geolocation is determined from the device's public IP address (typically assigned by the user's ISP). To specify a country, enter its <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha-2 code</a> in the <strong>Value</strong> field.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source Country IP Geolocation</td>
<td><code>http.src_ip.geo.country == &quot;RU&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="source-internal-ip">Source Internal IP</h3>
<p>Use this selector to apply HTTP policies to a private IP address, assigned by a user's local network, that requests arrive to Gateway from.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source Internal IP</td>
<td><code>http.conn.internal_src_ip == &quot;192.168.86.0/27&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="source-ip">Source IP</h3>
<p>The originating IP address or addresses of a device proxied by Gateway.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source IP</td>
<td><code>http.conn.src_ip[*] in {10.0.0.0/8}</code></td>
</tr>
</tbody>
</table>
<h3 id="traffic-source">Traffic Source <span class="nb-badge">Beta</span></h3>
<p>The method used to on-ramp traffic to Cloudflare. Use this selector to apply policies based on how traffic reaches Gateway.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Traffic Source</td>
<td><code>net.onramp.type == &quot;device_client&quot;</code></td>
</tr>
</tbody>
</table>
<p>Available values: <code>device_client</code> (Device client), <code>mesh</code> (Mesh), <code>cloudflare_wan</code> (Cloudflare WAN), <code>clientless_rdp</code> (Clientless RDP), <code>proxy_endpoint</code> (Proxy endpoint), <code>agentless_biso</code> (Clientless Browser Isolation), <code>mcp_portal</code> (MCP portal).</p>
<h3 id="url">URL</h3>
<p>Gateway ignores trailing forward slashes (<code>/</code>) in URLs. For example, <code>https://example.com</code> and <code>https://example.com/</code> will count as the same URL and may return a duplicate error.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>URL</td>
<td><code>http.request.uri matches &quot;/r/gaming&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="url-path">URL Path</h3>
<p>The pathname of a webpage's URL.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>URL Path</td>
<td><code>http.request.uri.path == \&quot;/foo/bar\&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="url-path-and-query">URL Path and Query</h3>
<p>The pathname and query of a webpage's URL.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>URL Path and Query</td>
<td><code>http.request.uri.path_and_query == \&quot;/foo/bar?ab%242=%2A342\&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="url-query">URL Query</h3>
<p>The query of a webpage's URL.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>URL Query</td>
<td><code>http.request.uri.query == &quot;ab%242=%2A342&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="users">Users</h3>
<p>Use these selectors to match against identity attributes.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Email</td>
<td><code>identity.email == &quot;user@example.com&quot;</code></td>
</tr>
<tr>
<td>User Name</td>
<td><code>identity.name == &quot;Test User&quot;</code></td>
</tr>
<tr>
<td>User Group IDs</td>
<td><code>any(identity.groups[*].id in {&quot;group_id&quot;})</code></td>
</tr>
<tr>
<td>User Group Names</td>
<td><code>any(identity.groups[*].name in {&quot;group_name&quot;})</code></td>
</tr>
<tr>
<td>User Group Emails</td>
<td><code>any(identity.groups[*].email in {&quot;group@example.com&quot;})</code></td>
</tr>
<tr>
<td>SAML Attributes</td>
<td><code>any(identity.saml_attributes[&quot;http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name&quot;] in {&quot;Test User&quot;})</code></td>
</tr>
</tbody>
</table>
<h3 id="virtual-network">Virtual Network</h3>
<p>Use this selector to match all traffic routed through a specific <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">Virtual Network</a> via the Cloudflare One Client.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Virtual Network</td>
<td><code>http.conn.vnet_id == &quot;957fc748-591a-e96s-a15d-1j90204a7923&quot;</code></td>
</tr>
</tbody>
</table>
<h2 id="comparison-operators">Comparison operators</h2>
<p>Comparison operators are the way Gateway matches traffic to a selector. When you choose a <strong>Selector</strong> in the dashboard policy builder, the <strong>Operator</strong> dropdown menu will display the available options for that selector.</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>is</td>
<td>equals the defined value</td>
</tr>
<tr>
<td>is not</td>
<td>does not equal the defined value</td>
</tr>
<tr>
<td>in</td>
<td>matches at least one of the defined values</td>
</tr>
<tr>
<td>not in</td>
<td>does not match any of the defined values</td>
</tr>
<tr>
<td>in list</td>
<td>in a pre-defined <a href="/cloudflare-one/reusable-components/lists/">list</a> of values</td>
</tr>
<tr>
<td>not in list</td>
<td>not in a pre-defined <a href="/cloudflare-one/reusable-components/lists/">list</a> of values</td>
</tr>
<tr>
<td>matches regex</td>
<td>regex evaluates to true</td>
</tr>
<tr>
<td>does not match regex</td>
<td>regex evaluates to false</td>
</tr>
<tr>
<td>greater than</td>
<td>exceeds the defined number</td>
</tr>
<tr>
<td>greater than or equal to</td>
<td>exceeds or equals the defined number</td>
</tr>
<tr>
<td>less than</td>
<td>below the defined number</td>
</tr>
<tr>
<td>less than or equal to</td>
<td>below or equals the defined number</td>
</tr>
</tbody>
</table>
<h2 id="value">Value</h2>
<p>In the <strong>Value</strong> field, you can input a single value when using an equality comparison operator (such as <em>is</em>) or multiple values when using a containment comparison operator (such as <em>in</em>). Additionally, you can use <a href="#regular-expressions">regular expressions</a> (or regex) to specify a range of values for supported selectors.</p>
<h3 id="regular-expressions">Regular expressions</h3>
<p>Regular expressions are evaluated using Rust. The Rust implementation is slightly different than regex libraries used elsewhere. For more information, refer to our guide for <a href="/cloudflare-one/access-controls/policies/app-paths/#wildcards">Wildcards</a>. To evaluate if your regex matches, you can use <a href="https://rustexp.lpil.uk/">Rustexp</a>.</p>
<p>If you want to match multiple values, you can use the pipe symbol (<code>|</code>) as an OR operator. You do not need to use an escape character (<code>\</code>) before the pipe symbol. For example, the following expression evaluates to true when the hostname matches either <code>.*whispersystems.org</code> or <code>.*signal.org</code>:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td>matches regex</td>
<td><code>.*whispersystems.org|.*signal.org</code></td>
</tr>
</tbody>
</table>
<p>In addition to regular expressions, you can use <a href="#logical-operators">logical operators</a> to match multiple values.</p>
<h2 id="logical-operators">Logical operators</h2>
<p>To evaluate multiple conditions in an expression, select the <strong>And</strong> logical operator. These expressions can be compared further with the <strong>Or</strong> logical operator.</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>And</td>
<td>match all of the conditions in the expression</td>
</tr>
<tr>
<td>Or</td>
<td>match any of the conditions in the expression</td>
</tr>
</tbody>
</table>
<p>The <strong>Or</strong> operator will only work with conditions in the same expression group. For example, you cannot compare conditions in <strong>Traffic</strong> with conditions in <p><strong>Identity</strong> or <strong>Device Posture</strong></p>
.</p>
<p>If a condition in an expression joins a request attribute (such as <em>Source IP</em>) and a response attribute (such as <em>a DLP Profile</em>), then the condition will be evaluated when the response is received.</p>
