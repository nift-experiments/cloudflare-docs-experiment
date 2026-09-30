---
cp9:
  canonical: https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/
  description: Typical rate limiting configurations for login protection, API abuse, and more.
  full_title: Rate limiting best practices · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Rate limiting best practices · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Typical rate limiting configurations for login protection, API abuse, and more."><link rel="canonical" href="https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/index.md"><meta property="og:title" content="Rate limiting best practices · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Typical rate limiting configurations for login protection, API abuse, and more."><meta property="og:url" content="https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Rate limiting"><meta name="pcx_tags" content="GraphQL,Account takeover,Authentication,Scraping"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/#page","headline":"Rate limiting best practices \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Typical rate limiting configurations for login protection, API abuse, and more.","url":"https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["GraphQL","Account takeover","Authentication","Scraping"]}</script>
  markdown: true
  noindex: false
  route: /waf/rate-limiting-rules/best-practices/
  schema: 1
---
<p>The following sections cover typical rate limiting configurations for common use cases. You can combine the provided example rules and adjust them to your own scenario.</p>
<p>The main use cases for rate limiting are the following:</p>
<ul>
<li><a href="/waf/rate-limiting-rules/best-practices/#enforcing-granular-access-control">Enforce granular access control</a> to resources. Includes access control based on criteria such as user agent, IP address, referrer, host, country, and world region.</li>
<li><a href="/waf/rate-limiting-rules/best-practices/#protecting-against-credential-stuffing">Protect against credential stuffing</a> and account takeover attacks.</li>
<li><a href="/waf/rate-limiting-rules/best-practices/#limiting-the-number-of-operations">Limit the number of operations</a> performed by individual clients. Includes preventing scraping by bots, accessing sensitive data, bulk creation of new accounts, and programmatic buying in ecommerce platforms.</li>
<li><a href="/waf/rate-limiting-rules/best-practices/#protecting-rest-apis">Protect REST APIs</a> from resource exhaustion (targeted DDoS attacks) and resources from abuse in general.</li>
<li><a href="/waf/rate-limiting-rules/best-practices/#protecting-graphql-apis">Protect GraphQL APIs</a> by preventing server overload and limiting the number of operations.</li>
</ul>
<h2 id="enforcing-granular-access-control">Enforcing granular access control</h2>
<h3 id="limit-by-user-agent">Limit by user agent</h3>
<p>A common use case is to limit the rate of requests performed by individual user agents. The following example rule allows a mobile app to perform a maximum of 100 requests in 10 minutes. You could also create a separate rule limiting the rate for desktop browsers.</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>User Agent equals <code>MobileApp</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.user_agent eq &quot;MobileApp&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>100 requests / 10 minutes</td>
</tr>
<tr>
<td>Action</td>
<td>Managed Challenge</td>
</tr>
</tbody>
</table>
<h3 id="limit-reuse-of-a-single-cf-clearance-cookie">Limit reuse of a single <code>cf_clearance</code> cookie</h3>
<p>After a visitor successfully passes a Managed Challenge, Cloudflare issues a <code>cf_clearance</code> cookie to identify them as verified. However, malicious actors may attempt to reuse or share a single valid <code>cf_clearance</code> value across multiple requests or devices to bypass additional challenges.</p>
<p>This rate limiting rule helps mitigate such abuse by restricting how many requests can be made with the same <code>cf_clearance</code> value within a defined period. Legitimate human users will remain unaffected, while automated or replayed requests using a single clearance token will be blocked once the threshold is exceeded.</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/checkout</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/checkout&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>Cookie (<code>cf_clearance</code>)</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>100 requests / 10 minutes</td>
</tr>
<tr>
<td>Action</td>
<td>Block</td>
</tr>
</tbody>
</table>
<h3 id="allow-specific-ip-addresses-or-asns">Allow specific IP addresses or ASNs</h3>
<p>Another use case when controlling access to resources is to exclude or include IP addresses or Autonomous System Numbers (ASNs) from a rate limiting rule.</p>
<p>The following example rule allows up to 10 requests per minute from the same IP address doing a <code>GET</code> request for <code>/status</code>, as long as the visitor's IP address is not included in the <code>partner_ips</code> <a href="/waf/tools/lists/custom-lists/#ip-lists">IP list</a>.</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/status</code> and Request Method equals <code>GET</code> and IP Source Address is not in list <code>partner_ips</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/status&quot; and http.request.method eq &quot;GET&quot; and not ip.src in $partner_ips</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>10 requests / 1 minute</td>
</tr>
<tr>
<td>Action</td>
<td>Managed Challenge</td>
</tr>
</tbody>
</table>
<h3 id="limit-by-referrer">Limit by referrer</h3>
<p>Some applications receive requests originated by other sources (for example, used by advertisements linking to third-party pages). You may wish to limit the number of requests generated by individual referrer pages to manage quotas or avoid indirect DDoS attacks.</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/status</code> and Request Method equals <code>GET</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/status&quot; and http.request.method eq &quot;GET&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>Header (<code>Referer</code>) <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>100 requests / 10 minutes</td>
</tr>
<tr>
<td>Action</td>
<td>Block</td>
</tr>
</tbody>
</table>
<p><em>This example rule requires Advanced Rate Limiting.</em></p>
<h3 id="limit-by-destination-host">Limit by destination host</h3>
<p>SaaS applications or customers using <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare SSL for SaaS</a> might have thousands of hosts under the same zone, which makes creating individual rules per host impractical. To overcome this, you can create a rate limiting rule that uses the host as a counting characteristic.</p>
<p>The following example rule will track the rate of requests to the <code>/login</code> endpoint for each host:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/login</code> and Request Method equals <code>GET</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/login&quot; and http.request.method eq &quot;GET&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP and Host</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>10 requests / 10 minutes</td>
</tr>
<tr>
<td>Action</td>
<td>Block</td>
</tr>
</tbody>
</table>
<p><em>This example rule requires Advanced Rate Limiting.</em></p>
<h2 id="protecting-against-credential-stuffing">Protecting against credential stuffing</h2>
<p>A typical use case of rate limiting is to protect a login endpoint against attacks such as <a href="https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/">credential stuffing</a>. The following example contains three different rate limiting rules with increasing penalties to manage clients making too many requests.</p>
<p><strong>Rule #1</strong></p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>Hostname equals <code>example.com</code> and URI Path equals <code>/login</code> and Request Method equals <code>POST</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.host eq &quot;example.com&quot; and http.request.uri.path eq &quot;/login&quot; and http.request.method eq &quot;POST&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP</td>
</tr>
<tr>
<td>Increment counter when</td>
<td>URI Path equals <code>/login</code> and Method equals <code>POST</code> and Response code is in (401, 403)</td>
</tr>
<tr>
<td>Counting expression</td>
<td><code>http.request.uri.path eq &quot;/login&quot; and http.request.method eq &quot;POST&quot; and http.response.code in {401 403}</code></td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>4 requests / 1 minute</td>
</tr>
<tr>
<td>Action</td>
<td>Managed Challenge</td>
</tr>
</tbody>
</table>
<p><strong>Rule #2</strong></p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>Hostname equals <code>example.com</code> and URI Path equals <code>/login</code> and Request Method equals <code>POST</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.host eq &quot;example.com&quot; and http.request.uri.path eq &quot;/login&quot; and http.request.method eq &quot;POST&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP</td>
</tr>
<tr>
<td>Increment counter when</td>
<td>URI Path equals <code>/login</code> and Request Method equals <code>POST</code> and Response Status Code is in (401, 403)</td>
</tr>
<tr>
<td>Counting expression</td>
<td><code>http.request.uri.path eq &quot;/login&quot; and http.request.method eq &quot;POST&quot; and http.response.code in {401 403}</code></td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>10 requests / 10 minutes</td>
</tr>
<tr>
<td>Action</td>
<td>Managed Challenge</td>
</tr>
</tbody>
</table>
<p><strong>Rule #3</strong></p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>Host equals <code>example.com</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.host eq &quot;example.com&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP</td>
</tr>
<tr>
<td>Increment counter when</td>
<td>URI Path equals <code>/login</code> and Request Method equals <code>POST</code> and Response Status Code is in (401, 403)</td>
</tr>
<tr>
<td>Counting expression</td>
<td><code>http.request.uri.path eq &quot;/login&quot; and http.request.method eq &quot;POST&quot; and http.response.code in {401 403}</code></td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>20 requests / 1 hour</td>
</tr>
<tr>
<td>Action</td>
<td>Block for 1 day</td>
</tr>
</tbody>
</table>
<p><em>These example rules require a Business plan or above.</em></p>
<p>Rule #1 allows up to four requests per minute, after which a Managed Challenge is triggered. This configuration allows legitimate customers a few attempts to remember their password. If an automated actor makes several requests, that client will likely be blocked by an unsolved Managed Challenge. On the other hand, if a human gets and passes the challenge when reaching rule #1's rate limit, rule #2 will provide the next level of protection, allowing for up to 10 requests over the next 10 minutes. For clients exceeding this second threshold, rule #3 (the most severe) will apply, blocking the client for one day.</p>
<p>These three rules have a counting expression separate from the rule expression (also known as mitigation expression). When you configure a separate counting expression, the matching criteria will only be used when an action is triggered. In the counting expression you can include conditions based on the HTTP response status code and HTTP response headers, therefore integrating rate limiting with your backend logic.</p>
<p>You can also decide to have two different expressions — a counting expression and a rule/mitigation expression — to define:</p>
<ol>
<li>The requests used to compute the rate.</li>
<li>The requests actually acted upon.</li>
</ol>
<p>For example, rule #3 computes the rate considering <code>POST</code> requests to <code>/login</code> that returned a <code>401</code> or <code>403</code> HTTP status code. However, when the rate limit is exceeded, Cloudflare blocks every request to the <code>example.com</code> host generated by the same IP. For more information on counting expressions, refer to <a href="/waf/rate-limiting-rules/request-rate/#example-b">Request rate calculation</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="configuring-additional-protection">Configuring additional protection</h3>
@markup("md", "content/.markup/bodies/15374.md")
</aside>
<h3 id="protect-otp-and-verification-endpoints">Protect OTP and verification endpoints</h3>
<p>One-time password (OTP) and verification endpoints (such as <code>/api/otp/validate</code> or <code>/account/verify</code>) are frequent targets for brute force attacks. These endpoints are particularly sensitive because attackers attempt large volumes of requests with different codes to guess a valid OTP.</p>
<p>When configuring rate limiting for these endpoints, follow these guidelines:</p>
<ul>
<li><strong>Match the exact URI path</strong>: The rule expression must match the path that receives attack traffic. Verify the path in analytics before creating the rule. A rule targeting <code>/validate/otp</code> will not match requests to <code>/api/otp/validate</code>.</li>
<li><strong>Use response-based counting</strong>: Count only requests that return error responses (such as <code>401</code> or <code>403</code>) to avoid rate limiting legitimate users who submit valid codes.</li>
<li><strong>Scope geographic restrictions appropriately</strong>: If you restrict by country, verify that attack traffic originates from all the countries you observe in analytics, not just one.</li>
</ul>
<p>The following example rule protects an OTP validation endpoint by counting only failed attempts:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/api/otp/validate</code> and Request Method equals <code>POST</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/api/otp/validate&quot; and http.request.method eq &quot;POST&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP</td>
</tr>
<tr>
<td>Increment counter when</td>
<td>URI Path equals <code>/api/otp/validate</code> and Request Method equals <code>POST</code> and Response Status Code is in (401, 403)</td>
</tr>
<tr>
<td>Counting expression</td>
<td><code>http.request.uri.path eq &quot;/api/otp/validate&quot; and http.request.method eq &quot;POST&quot; and http.response.code in {401 403}</code></td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>5 requests / 1 minute</td>
</tr>
<tr>
<td>Action</td>
<td>Block for 10 minutes</td>
</tr>
</tbody>
</table>
<p><em>The above example rule requires a Business plan or higher.</em></p>
<p>If your OTP endpoint returns <code>200</code> for both valid and invalid codes (with the result in the response body), use request-based counting with a lower threshold instead:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/api/otp/validate</code> and Request Method equals <code>POST</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/api/otp/validate&quot; and http.request.method eq &quot;POST&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>10 requests / 1 minute</td>
</tr>
<tr>
<td>Action</td>
<td>Managed Challenge</td>
</tr>
</tbody>
</table>
<h2 id="limiting-the-number-of-operations">Limiting the number of operations</h2>
<p>You can use rate limiting to limit the number of operations performed by a client. The exact rule providing this protection will depend on your application. The following examples address <a href="https://www.cloudflare.com/learning/bots/what-is-content-scraping/">content scraping</a> via query string parameters or JSON body.</p>
<h3 id="prevent-content-scraping-via-query-string">Prevent content scraping (via query string)</h3>
<p>In this example, clients perform operations (such as looking up prices and adding to basket) on an ecommerce website using different query string parameters. For example, a typical request sent by a client could be similar to the following:</p>
<pre tabindex="0"><code class="language-txt">GET https://store.com/merchant?action=lookup_price&amp;product_id=215&#10;Cookie: session_id=12345&#10;</code></pre>
<p>Your security team might want to consider setting up a limit on the number of times a client can lookup prices to prevent bots — which may have eluded Cloudflare Bot Management — from scraping the store's entire catalog.</p>
<p><strong>Rule #1</strong></p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/merchant</code> and URI Query String contains <code>action=lookup_price</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/merchant&quot; and http.request.uri.query contains &quot;action=lookup_price&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>10 requests / 2 minutes</td>
</tr>
<tr>
<td>Action</td>
<td>Managed Challenge</td>
</tr>
</tbody>
</table>
<p><strong>Rule #2</strong></p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/merchant</code> and URI Query String contains <code>action=lookup_price</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/merchant&quot; and http.request.uri.query contains &quot;action=lookup_price&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>20 requests / 5 minute</td>
</tr>
<tr>
<td>Action</td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>These two rate limiting rules match requests performing a selected action (look up price, in this example) and use <code>IP</code> as the counting characteristic. Similarly to the <a href="#protecting-against-credential-stuffing">previous <code>/login</code> example</a>, the two rules will help reduce false positives in case of persistent (but legitimate) visitors.</p>
<p>To limit the lookup of a specific <code>product_id</code> via query string parameter, you could add that specific query parameter as a counting characteristic, so that the rate is calculated based on all the requests, regardless of the client. The following example rule limits the number of lookups for each <code>product_id</code> to 50 requests in 10 seconds.</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/merchant</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/merchant&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>Query (<code>product_id</code>)</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>50 requests / 10 seconds</td>
</tr>
<tr>
<td>Action</td>
<td>Block</td>
</tr>
</tbody>
</table>
<p><em>This example rule requires Advanced Rate Limiting.</em></p>
<p>You could follow the same pattern of rate limiting rules to protect applications handling reservations and bookings.</p>
<h3 id="prevent-content-scraping-via-body">Prevent content scraping (via body)</h3>
<p>Consider an application that handles the operation and its parameters through the request body in JSON format. For example, the <code>lookup_price</code> operation could look like the following:</p>
<pre tabindex="0"><code class="language-txt">POST https://api.store.com/merchant&#10;Cookie: session_id=12345&#10;&#10;Body:&#10;{&#10;  &quot;action&quot;: &quot;lookup_price&quot;,&#10;  &quot;product_id&quot;: 215&#10;}&#10;</code></pre>
<p>In this scenario, you could write a rule to limit the number of actions from individual sessions:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/merchant</code> and JSON String <code>action</code> equals <code>lookup_price</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/merchant&quot; and lookup_json_string(http.request.body.raw, &quot;action&quot;) eq &quot;lookup_price&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>Cookie (<code>session_id</code>)</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>10 requests / 2 minutes</td>
</tr>
<tr>
<td>Action</td>
<td>Managed Challenge</td>
</tr>
</tbody>
</table>
<p><em>This example rule requires Advanced Rate Limiting and payload inspection.</em></p>
<p>You could also limit the number of lookups of each <code>product_id</code> regardless of the client making the requests by deploying a rule like the following:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/merchant</code> and JSON field <code>action</code> equals <code>lookup_price</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/merchant&quot; and lookup_json_string(http.request.body.raw, &quot;action&quot;) eq &quot;lookup_price&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>JSON field (<code>product_id</code>)</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>50 requests / 10 seconds</td>
</tr>
<tr>
<td>Action</td>
<td>Block</td>
</tr>
</tbody>
</table>
<p><em>This example rule requires Advanced Rate Limiting and payload inspection.</em></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15373.md")
</aside>
<h3 id="limit-requests-from-bots">Limit requests from bots</h3>
<p>A general approach to identify traffic from bots is to rate limit requests that trigger a large volume of <code>403</code> or <code>404</code> response status codes from the origin server. This usually indicates automated activity from scraping applications.</p>
<p>In this situation, you could configure a rule similar to the following:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>Hostname equals <code>example.com</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.host eq &quot;example.com&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP</td>
</tr>
<tr>
<td>Increment counter when</td>
<td>Response Status Code is in (403, 404)</td>
</tr>
<tr>
<td>Counting expression</td>
<td><code>http.response.code in {403 404}</code></td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>5 requests / 3 minutes</td>
</tr>
<tr>
<td>Action</td>
<td>Managed Challenge</td>
</tr>
</tbody>
</table>
<p><em>This example rule requires a Business plan or above.</em></p>
<p>To control the rate of actions performed by automated sources, consider use rate limiting rules together with <a href="/bots/get-started/bot-management/">Bot Management</a>. With Bot Management, you can use the <a href="/bots/concepts/bot-score/">bot score</a> as part of the matching criteria to apply the rule only to automated or likely automated traffic. For example, you can use a maximum score (or threshold) of <code>30</code> for likely automated traffic and <code>10</code> for automated traffic.</p>
<p>If your application tracks sessions using a cookie, you can use the cookie to set the rate limiting context (that is, use it as a counting characteristic). By setting the rate limiting characteristic to Cookie, the rule will group together requests from different IP addresses but belonging to the same session, which is a common scenario when dealing with a bot network performing a distributed attack.</p>
<p><strong>Rule #1</strong></p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>Bot Score less than 30 and URI Query String contains <code>action=delete</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>cf.bot_management.score lt 30 and http.request.uri.query contains &quot;action=delete&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>Cookie (<code>session_id</code>)</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>10 requests / 1 minute</td>
</tr>
<tr>
<td>Action</td>
<td>Managed Challenge</td>
</tr>
</tbody>
</table>
<p><strong>Rule #2</strong></p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>Bot Score less than 10 and URI Query String contains <code>action=delete</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>cf.bot_management.score lt 10 and http.request.uri.query contains &quot;action=delete&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>Cookie (<code>session_id</code>)</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>20 requests / 5 minute</td>
</tr>
<tr>
<td>Action</td>
<td>Block</td>
</tr>
</tbody>
</table>
<p><em>These example rules require Advanced Rate Limiting and Bot Management.</em></p>
<p>If the application does not use a session cookie, you can use <a href="/bots/additional-configurations/ja3-ja4-fingerprint/">JA3 fingerprints</a> to identify individual clients. A JA3 fingerprint is a unique identifier, available to customers with <a href="/bots/get-started/bot-management/">Bot Management</a>, that allows Cloudflare to identify requests coming from the same client. All clients have an associated fingerprint, whether they are automated or not.</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/merchant</code> and Bot Score less than 10</td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/merchant&quot; and cf.bot_management.score lt 10</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>JA3 Fingerprint</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>10 requests / 1 minute</td>
</tr>
<tr>
<td>Action</td>
<td>Managed Challenge</td>
</tr>
</tbody>
</table>
<p><em>This example rule requires Advanced Rate Limiting and Bot Management.</em></p>
<h2 id="protecting-rest-apis">Protecting REST APIs</h2>
<p>APIs can put significant strain on the application backend because API requests can be expensive to compute or serve. These requests may also require complex operations (such as data processing and large data lookups) that, if abused, can eventually bring down an origin server.</p>
<h3 id="prevent-volumetric-attacks">Prevent volumetric attacks</h3>
<p>Advanced Rate Limiting can mitigate many types of volumetric attacks, like DDoS attacks, mass assignment, and data exfiltration.</p>
<p>A common concern is to limit <code>POST</code> actions. For authenticated traffic, you can use <a href="/api-shield/security/api-discovery/">API Discovery</a> to identify a suitable rate of request per endpoint, and then create a rate limiting rule like the following:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/endpoint1</code> and Request Method equals <code>POST</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/endpoint1&quot; and http.request.method eq &quot;POST&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>Header (<code>x-api-key</code>)</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>As suggested by API Discovery or assessed by analyzing past traffic.</td>
</tr>
<tr>
<td>Action</td>
<td>Block</td>
</tr>
</tbody>
</table>
<p><em>This example rule requires Advanced Rate Limiting. API Discovery requires an additional license.</em></p>
<p>The counting characteristic can be any header, key, token, cookie, query parameter, or even JSON body field, since some APIs include a session ID or user ID as part of the JSON body. Refer to the following sections for additional information:</p>
<ul>
<li>If your unique identifier is in the URI path, refer to <a href="#protect-resources">Protect resources</a>.</li>
<li>If your unique identifier is in the JSON body, refer to <a href="#prevent-content-scraping-via-body">Prevent content scraping (via body)</a>.</li>
</ul>
<h3 id="protect-resources">Protect resources</h3>
<p><code>GET</code> requests can also create excessive strain on an application or have an impact on costly resources, such as bandwidth. For example, consider an application with a large amount of stored files (such as images) where clients can download a file by accessing their specific URL:</p>
<pre tabindex="0"><code class="language-txt">GET https://api.store.com/files/&lt;FILE_ID&gt;&#10;Header: x-api-key=9375&#10;</code></pre>
<p>You probably wish to limit the number of downloads to avoid abuse, but you do not want to write individual rules for each file, given the size of the data storage. In this case, you could write a rule such as the following:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>Hostname equals <code>api.example.com</code> and Request Method equals <code>GET</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.host eq &quot;api.example.com&quot; and http.request.method eq &quot;GET&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>Path</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>As suggested by API Discovery or assessed by analyzing past traffic.</td>
</tr>
<tr>
<td>Action</td>
<td>Block</td>
</tr>
</tbody>
</table>
<p><em>This example rule requires Advanced Rate Limiting.</em></p>
<p>The rule defines a limit of 10 downloads in 10 minutes for every file under <code>https://api.store.com/files/*</code>. By using Path as the rule characteristic, you avoid having to write a new rule every time there is a new uploaded file with a different <code>&lt;FILE_ID&gt;</code>. With this rule, the rate is computed on every request, regardless of their source IP or session identifier.</p>
<p>You could also combine Path with the <code>x-api-key</code> header (or IP, if you do not have a key or token) to set the maximum number of downloads that a specific client, as identified by <code>x-api-key</code>, can make of a given file:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>Hostname equals <code>api.store.com</code> and Request Method equals <code>GET</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.host eq &quot;api.example.com&quot; and http.request.method eq &quot;GET&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>Path and Header (<code>x-api-key</code>)</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>As suggested by API Discovery or assessed by analyzing past traffic.</td>
</tr>
<tr>
<td>Action</td>
<td>Block</td>
</tr>
</tbody>
</table>
<p><em>This example rule requires Advanced Rate Limiting.</em></p>
<h2 id="protecting-graphql-apis">Protecting GraphQL APIs</h2>
<p>Preventing server overload for GraphQL APIs can be different from preventing overload for RESTful APIs. One of the biggest challenges posed by applications built on GraphQL is that a single path manages all queries to the server, and every request is usually a <code>POST</code> operation. This prevents different rate limits for different API use cases based on the HTTP method and URI path.</p>
<p>However, instead of using the method and path like a RESTful API, the purpose of the request is usually embedded in the body, which has information on what data the client wants to fetch or mutate (according to <a href="https://graphql.org/learn/queries/">GraphQL's terminology</a> for server-side data modification), along with any additional data required to carry out the action.</p>
<p>To prevent server overload, consider the following approaches:</p>
<ol>
<li>Limit the number of times a particular user can call the same GraphQL operation name.</li>
<li>Limit the total amount of query complexity any given user is allowed to request.</li>
<li>Limit any individual request's query complexity.</li>
</ol>
<p>The following examples are based on an application that accepts reviews for movies. A GraphQL request could look like the following:</p>
<pre tabindex="0"><code class="language-txt">POST https://moviereviews.example.com/graphql&#10;Cookie: session_id=12345&#10;&#10;Body:&#10;{&#10;  &quot;data&quot;: {&#10;    &quot;createReview&quot;: {&#10;      &quot;stars&quot;: 5,&#10;      &quot;commentary&quot;: &quot;This is a great movie!&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h3 id="limit-the-number-of-operations">Limit the number of operations</h3>
<p>To limit the rate of actions, you could use the following rule:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path equals <code>/graphql</code> and Body contains <code>createReview</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/graphql&quot; and http.request.body.raw contains &quot;createReview&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>Cookie (<code>session_id</code>)</td>
</tr>
<tr>
<td>Rate (Requests / Period)</td>
<td>5 requests / 1 hour</td>
</tr>
<tr>
<td>Action</td>
<td>Block</td>
</tr>
</tbody>
</table>
<p><em>This example rule requires Advanced Rate Limiting and payload inspection.</em></p>
<h3 id="limit-the-total-amount-of-query-complexity">Limit the total amount of query complexity</h3>
<p>The complexity necessary to handle a GraphQL request can vary significantly. Since the API uses a single endpoint, it is difficult to figure out the complexity of each request before it has been served.</p>
<p>To protect the origin server from resource exhaustion, rather than limiting the number of requests you need to limit the amount of complexity necessary to handle a single client over a period of time. Cloudflare Rate Limiting allows you to create rules that <a href="/waf/rate-limiting-rules/request-rate/#complexity-based-rate-limiting">track complexity over time</a> and block subsequent requests after reaching a complexity budget or limit.</p>
<p>This type of rate limiting requires that the server scores every served request according to the request's complexity. Additionally, the server must add this score to the response as an HTTP header. Then, the rate limiting mechanism will use this information to update the budget for that specific client.</p>
<p>For example, the following rule defines a total complexity budget of 1,000 per hour:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Matching criteria</td>
<td>URI Path contains <code>/graphql</code></td>
</tr>
<tr>
<td>Expression</td>
<td><code>http.request.uri.path eq &quot;/graphql&quot;</code></td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>Cookie (<code>session_id</code>)</td>
</tr>
<tr>
<td>Score per period</td>
<td>1,000</td>
</tr>
<tr>
<td>Period</td>
<td>1 hour</td>
</tr>
<tr>
<td>Response header name</td>
<td><code>score</code></td>
</tr>
<tr>
<td>Action</td>
<td>Block</td>
</tr>
</tbody>
</table>
<p><em>This example rule requires Advanced Rate Limiting and payload inspection.</em></p>
<p>When the origin server processes a request, it adds a <code>score</code> HTTP header to the response with a value representing how much work the origin has performed to handle it — for example, <code>100</code>. In the next hour, the same client can perform requests up to an additional budget of <code>900</code>. As soon as this budget is exceeded, later requests will be blocked until the timeout expires.</p>
<h3 id="limit-any-individual-query-s-complexity">Limit any individual query’s complexity</h3>
<p>API Shield customers can use GraphQL malicious query protection to protect their GraphQL APIs. GraphQL malicious query protection scans your GraphQL traffic for queries that could overload your origin and result in a denial of service. You can build rules that limit the query depth and size of incoming GraphQL queries in order to block suspiciously large or complex queries.</p>
<p>Refer to <a href="https://developers.cloudflare.com/api-shield/security/graphql-protection/">API Shield documentation</a> for more information on GraphQL malicious query protection.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">The HTTP header name uses a misspelling of "referrer".</li></ol></section>
