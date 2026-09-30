---
cp9:
  canonical: https://developers.cloudflare.com/waf/rate-limiting-rules/
  description: Documentation for the previous version of Rate Limiting.
  full_title: Rate Limiting (previous version) · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Rate Limiting (previous version) · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Documentation for the previous version of Rate Limiting."><link rel="canonical" href="https://developers.cloudflare.com/waf/rate-limiting-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/index.md"><meta property="og:title" content="Rate Limiting (previous version) · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Documentation for the previous version of Rate Limiting."><meta property="og:url" content="https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/rate-limiting-rules/#page","headline":"Rate Limiting (previous version) \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Documentation for the previous version of Rate Limiting.","url":"https://developers.cloudflare.com/waf/rate-limiting-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/reference/legacy/old-rate-limiting/
  schema: 1
---
<p>Cloudflare Rate Limiting automatically identifies and mitigates excessive request rates for specific URLs or for an entire domain.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15698.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="were-you-blocked-from-accessing-a-website">Were you blocked from accessing a website?</h3>
@markup("md", "content/.markup/bodies/15697.md")
</aside>
<p>Request rates are calculated locally for individual Cloudflare data centers. The most common uses for Rate Limiting are:</p>
<ul>
<li>Protect against <a href="https://www.cloudflare.com/learning/ddos/glossary/denial-of-service/">DDoS attacks</a></li>
<li>Protect against <a href="https://www.cloudflare.com/learning/bots/brute-force-attack/">Brute-force attack</a></li>
<li>Limit access to forum searches, API calls, or resources that involve database-intensive operations at your origin</li>
</ul>
<p>Once an individual IPv4 address or IPv6 <code>/64</code> IP range exceeds a rule threshold, further requests to the origin server are blocked with an <code>HTTP 429</code> response status code. The response includes a <code>Retry-After</code> header to indicate when the client can resume sending requests.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15696.md")
</aside>
<h3 id="rate-limiting-and-seo">Rate limiting and SEO</h3>
<p>Cached resources and known Search Engine crawlers are exempted from your rate limiting rules (previous version only). Therefore, they do not affect your website's <a href="/fundamentals/performance/improve-seo/">SEO ranking</a>.</p>
<hr />
<h2 id="availability">Availability</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15695.md")
</aside>
<p>The number of allowed rate limiting rules depends on the domain's plan:</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Rules</th>
<th>Rules matching response headers</th>
<th>Actions</th>
<th>Action Duration</th>
<th>Request Period</th>
</tr>
</thead>
<tbody>
<tr>
<td>Free</td>
<td>1</td>
<td>1</td>
<td>Block</td>
<td>1 minute or 1 hour</td>
<td>10 seconds or 1 minute</td>
</tr>
<tr>
<td>Pro</td>
<td>10</td>
<td>1</td>
<td>Block, Non-Interactive Challenge, Managed Challenge, Interactive Challenge, or Log</td>
<td>1 minute or 1 hour</td>
<td>10 seconds or 1 minute</td>
</tr>
<tr>
<td>Business</td>
<td>15</td>
<td>10</td>
<td>Block, Non-Interactive Challenge, Managed Challenge, Interactive Challenge, or Log</td>
<td>1 minute, 1 hour, or 24 hours</td>
<td>10 seconds, 1 minute, or 10 minutes</td>
</tr>
<tr>
<td>Enterprise</td>
<td>100</td>
<td>10</td>
<td>Block, Non-Interactive Challenge, Managed Challenge, Interactive Challenge, or Log</td>
<td>Any duration entered between 10 seconds and 86,400 seconds (24 hours)</td>
<td>Any value entered between 10 seconds and 3,600 seconds (1 hour)</td>
</tr>
</tbody>
</table>
<p>Cloudflare Rate Limiting supports multiple levels of configuration control depending on the domain’s Cloudflare plan. The table below maps out what you can do based on your plan:</p>
<table>
<thead>
<tr>
<th>Order</th>
<th>Task</th>
<th>Available in</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><a href="#task-1-configure-a-basic-rate-limiting-rule">Configure a basic rate limiting rule</a></td>
<td>All plans</td>
</tr>
<tr>
<td>2</td>
<td><a href="#task-2-configure-advanced-criteria-only-business-and-enterprise-plans">Configure Advanced Criteria</a></td>
<td>Business and Enterprise plans</td>
</tr>
<tr>
<td>3</td>
<td><a href="#task-3-configure-advanced-response-only-business-and-enterprise-plans">Configure Advanced Response</a></td>
<td>Business and Enterprise plans</td>
</tr>
<tr>
<td>4</td>
<td><a href="#task-4-configure-the-bypass-option-enterprise-plans-only">Configure the Bypass option</a></td>
<td>Enterprise plan</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="components-of-a-rate-limiting-rule">Components of a rate limiting rule</h2>
<p>A rate limiting rule consists of three distinct components:</p>
<ul>
<li><a href="#request-matching-criteria">Request matching criteria</a></li>
<li><a href="#rate-matching-criteria">Rate matching criteria</a></li>
<li><a href="#rule-mitigation">Rule mitigation</a></li>
</ul>
<h3 id="request-matching-criteria">Request matching criteria</h3>
<p>Incoming requests are matched based on request path, request scheme, request method, and (optionally) origin response code.</p>
<h4 id="request-path">Request path</h4>
<p>For example:</p>
<ul>
<li><code>http://example.com/example</code></li>
<li><code>http://example.com/example/*</code></li>
</ul>
<p>The request path is case insensitive. Patterns cannot match content after query strings (<code>?</code>) or anchors (<code>#</code>). An asterisk (<code>*</code>) matches any sequence of characters, including an empty sequence. For example:</p>
<ul>
<li><code>*.example.com/*</code> matches any path on any subdomain of <code>example.com</code>.</li>
<li><code>*example.com/example.html</code> matches <code>example.html</code> on <code>example.com</code> or any subdomain of <code>example.com</code>.</li>
<li><code>*</code> matches any page on your site.</li>
</ul>
<p>A request for <code>example.com/path</code> is not the same as <code>example.com/path/</code>. The only exception to this rule is the homepage: <code>example.com</code> matches <code>example.com/</code>.</p>
<h4 id="request-scheme">Request scheme</h4>
<p><em>HTTP</em> or <em>HTTPS</em>. If none is specified, both are matched, and the rule will list __ALL__.</p>
<h4 id="request-method">Request method</h4>
<p><em>POST</em> or <em>GET</em>. If none is specified, all methods are matched, and the rule will list __ALL__.</p>
<h4 id="optional-origin-response-code">(Optional) Origin response code</h4>
<p>For example, match a rate limiting rule only when the origin server returns an <code>HTTP 401</code> or <code>403</code> status code. A triggered rule matching the response code criteria blocks subsequent requests from that client regardless of origin response code.</p>
<h3 id="rate-matching-criteria">Rate matching criteria</h3>
<p>A rule can match on the number and time period of all requests coming from the same client.</p>
<h4 id="number-of-requests">Number of requests</h4>
<p>Specify a minimum of two requests. For single request blocking, make the path unavailable — for example, configure your origin server to return an <code>HTTP 403</code> status code.</p>
<h4 id="request-period">Request period</h4>
<p>A rule triggers once a client’s requests exceed the threshold for the specified duration.</p>
<h3 id="rule-mitigation">Rule mitigation</h3>
<p>Rule mitigations consist of mitigation action and ban duration.</p>
<h4 id="mitigation-action">Mitigation action</h4>
<p>Rate limit actions are based on the domain plan as mentioned in <a href="#availability">Availability</a>:</p>
<ul>
<li><strong>Block</strong>: Cloudflare issues an <code>HTTP 429</code> error when the threshold is exceeded.</li>
<li><strong>Non-Interactive Challenge</strong>: Visitor must pass a Cloudflare non-interactive challenge. If passed, Cloudflare allows the request.</li>
<li><strong>Managed Challenge</strong>: Visitor must pass a challenge dynamically chosen by Cloudflare based on the characteristics of the request. If passed, Cloudflare allows the request.</li>
<li><strong>Interactive Challenge</strong>: Visitor must pass an Interactive Challenge. If passed, Cloudflare allows the request.</li>
<li><strong>Log</strong>: Requests are logged in <a href="/logs/">Cloudflare Logs</a>. This helps test rules before applying to production.</li>
</ul>
<p>For more information on challenge actions, refer to <a href="/cloudflare-challenges/">Challenges</a>.</p>
<h4 id="ban-duration">Ban duration</h4>
<p>Setting a timeout shorter than the threshold causes the API to automatically increase the timeout to equal the threshold.</p>
<p>Visitors hitting a rate limit receive a default HTML page if a custom <a href="/rules/custom-errors/">error page</a> is not specified. In addition, Business and Enterprise customers can specify a response in the rule itself. Refer to <a href="#task-3-configure-advanced-response-only-business-and-enterprise-plans">Configure Advanced Response</a> for details.</p>
<hr />
<h2 id="identify-rate-limit-thresholds">Identify rate-limit thresholds</h2>
<p>To identify a general threshold for Cloudflare Rate Limiting, divide 24 hours of uncached website requests by the unique visitors for the same 24 hours. Then, divide by the estimated average minutes of a visit. Finally, multiply by 4 (or larger) to establish an estimated threshold per minute for your website. A value higher than 4 is fine since most attacks are an order of magnitude above typical traffic rates.</p>
<p>To identify URL rate limits for specific URLs, use 24 hours of uncached requests and unique visitors for the specific URL. Adjust thresholds based on user reports and your own monitoring.</p>
<hr />
<h2 id="task-1-configure-a-basic-rate-limiting-rule">Task 1: Configure a basic rate limiting rule</h2>
<p>The following sections cover two common types of rate limiting rules.</p>
<h3 id="enable-protect-your-login">Enable Protect your login</h3>
<p>Rate Limiting features a one-click <strong>Protect your login</strong> tool that creates a rule to block the client for 15 minutes when sending more than 5 POST requests within 5 minutes. This is sufficient to block most brute-force attempts.</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Rate limiting rules</strong>.</li>
<li>Under <strong>Rate Limiting</strong>, select <strong>Protect your login</strong>.</li>
<li>Enter <strong>Rule Name</strong> and <strong>Enter your login URL</strong> in the <strong>Protect your login</strong> dialog that appears.</li>
<li>Select <strong>Save</strong>.</li>
<li>The <strong>Rule Name</strong> appears in your <strong>Rate Limiting</strong> rules list.</li>
</ol>
<h3 id="create-a-custom-rate-limiting-rule">Create a custom rate limiting rule</h3>
<ol>
<li>
<p>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</p>
</li>
<li>
<p>Go to <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Rate limiting rules</strong>.</p>
</li>
<li>
<p>Select <strong>Create rate limiting rule</strong>. A dialog opens where you specify the details of your new rule.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/waf/reference/legacy/old-rate-limiting-create-rule.png" alt="Create rate limiting rule pop-up dialog with an example rule configuration. The rule will block requests from IP addresses that exceed 150 requests per minute for one hour." /></p>
<ol start="4">
<li>
<p>Enter a descriptive name for the rule in <strong>Rule Name</strong>.</p>
</li>
<li>
<p>For <strong>If Traffic Matching the URL</strong>, select an HTTP scheme from the dropdown and enter a URL.</p>
</li>
<li>
<p>In <strong>from the same IP address exceeds</strong>, enter an integer greater than 1 to represent the number of requests in a sampling period.</p>
</li>
<li>
<p>For <strong>requests per</strong>, select the sampling period (the period during which requests are counted). Domains on Enterprise plans can enter manually any duration between 10 seconds and 3,600 seconds (one hour).</p>
</li>
<li>
<p>For <strong>Then</strong>, pick one of the available actions based on your plan. Review the <a href="#rule-mitigation">Rule mitigation</a> section for details.</p>
</li>
<li>
<p>If you selected <em>Block</em> or <em>Log</em>, for <strong>matching traffic from that visitor for</strong>, select how long to apply the option once a threshold has been triggered. Domains on Enterprise plans can enter any value between 10 seconds and 86,400 seconds (24 hours).</p>
</li>
<li>
<p>To activate your new rule, select <strong>Save and Deploy</strong>.</p>
</li>
</ol>
<p>The new rule appears in the rate limiting rules list.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15694.md")
</aside>
<p>In general, when setting a lower threshold:</p>
<ol>
<li>Leave existing rules in place and add a new rule with the lower threshold.</li>
<li>Once the new rule is in place, wait for the action duration of the old rule to pass before deleting the old rule.</li>
</ol>
<p>When setting a higher threshold (due to legitimate client blocking), increase the threshold within the existing rule.</p>
<hr />
<h2 id="task-2-configure-advanced-criteria-only-business-and-enterprise-plans">Task 2: Configure Advanced Criteria (only Business and Enterprise plans)</h2>
<p>The <strong>Advanced Criteria</strong> option configures which HTTP methods, header responses, and origin response codes to match for your rate limiting rule.</p>
<p>To configure your advanced criteria for a new or existing rule:</p>
<ol>
<li>Expand <strong>Advanced Criteria</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/waf/reference/legacy/old-rate-limiting-advanced-criteria.png" alt="Available fields when configuring Advanced Criteria for a rate limiting rule." /></p>
<ol start="2">
<li>
<p>Select a value from <strong>Method(s)</strong>. The default value is <em>ANY</em>, which matches all HTTP methods.</p>
</li>
<li>
<p>Filter by <strong>HTTP Response Header(s)</strong>. Select <strong>Add header response field</strong> to include headers returned by your origin web server.</p>
<p>The <code>CF-Cache-Status</code> header appears by default so that Cloudflare serves cached resources rather than rate limit those resources. To also rate limit cached resources, remove this header by selecting <strong>X</strong> or enable <strong>Also apply rate limit to cached assets</strong>.</p>
<p>If you have more than one header under <strong>HTTP Response Header(s)</strong>, an <em>AND</em> boolean logic applies. To exclude a header, use the <em>Not Equals</em> option. Each header is case insensitive.</p>
</li>
<li>
<p>Under <strong>Origin Response code(s)</strong>, enter the numerical value of each HTTP response code to match. Separate two or more HTTP codes with a comma (for example: <code>401, 403</code>).</p>
</li>
<li>
<p>(Optional) Configure additional rate limiting features, based on your plan.</p>
</li>
<li>
<p>Select <strong>Save and Deploy</strong>.</p>
</li>
</ol>
<hr />
<h2 id="task-3-configure-advanced-response-only-business-and-enterprise-plans">Task 3: Configure Advanced Response (only Business and Enterprise plans)</h2>
<p>The <strong>Advanced Response</strong> option configures the information format returned by Cloudflare when a rule's threshold is exceeded. Use <strong>Advanced Response</strong> when you wish to return static plain text or JSON content.</p>
<p>To configure a plain text or JSON response:</p>
<ol>
<li>Expand <strong>Advanced Response</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/waf/reference/legacy/old-rate-limiting-advanced-response.png" alt="Available fields when configuring an Advance Response for a rate limiting rule." /></p>
<ol start="2">
<li>
<p>Select a <strong>Response type</strong> format other than the default: <em>Custom JSON</em> or <em>Custom TEXT</em>.</p>
</li>
<li>
<p>Enter the plain text or JSON response you wish to return. The maximum response size is 32 KB.</p>
</li>
<li>
<p>(Optional) Configure additional rate limiting features, based on your plan.</p>
</li>
<li>
<p>Select <strong>Save and Deploy</strong>.</p>
</li>
</ol>
<h3 id="using-a-custom-html-page-or-a-redirect">Using a custom HTML page or a redirect</h3>
<p>If you wish to display a custom HTML page, configure a custom page for <code>HTTP 429</code> errors (<code>Too many requests</code>) in the dashboard. Cloudflare will display this page when you select <em>Default Cloudflare Rate Limiting Page</em> in <strong>Response type</strong> (the default value for the field).</p>
<p>You can use the following method to redirect a rate-limited client to a specific URL:</p>
<ol>
<li>Create an HTML page on your server that will redirect to the final URL of the page you wish to display. Include a <a href="https://www.w3.org/TR/WCAG20-TECHS/H76.html">meta <code>refresh</code></a> tag in the page content, like in the following example:</li>
</ol>
<pre tabindex="0"><code class="language-html">&lt;!doctype html&gt;&#10;&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;meta charset=&quot;utf-8&quot; /&gt;&#10;		&lt;title&gt;Custom RL page&lt;/title&gt;&#10;		&lt;meta&#10;			http-equiv=&quot;refresh&quot;&#10;			content=&quot;0; url=&#x27;https://yourzonename/block&#x27;&quot;&#10;		/&gt;&#10;	&lt;/head&gt;&#10;&#10;	&lt;body&gt;&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<p>Take note of the public URL of the page you created.</p>
<ol start="2">
<li>In the Cloudflare dashboard, go to the <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>
<p>Go to <strong>Error Pages</strong>.</p>
</li>
<li>
<p>Next to <strong>Rate limiting block</strong>, select the three dots &gt; <strong>Edit</strong>.</p>
</li>
<li>
<p>Select <strong>Custom page</strong>.</p>
</li>
<li>
<p>In <strong>Custom page address</strong>, enter the URL of the page you created on your server — the page containing the meta <code>refresh</code> tag.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>Follow the same approach if you wish to return plain text or JSON content but the response is larger than 32 KB. In this case, the redirect URL would be the URL of the plain text or JSON resource you would like to display.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/15693.md")
</aside>
<hr />
<h2 id="task-4-configure-the-bypass-option-enterprise-plans-only">Task 4: Configure the Bypass option (Enterprise plans only)</h2>
<p><strong>Bypass</strong> creates an allowlist or exception so that no actions apply to a specific set of URLs even if the rate limit is matched.</p>
<p>To configure <strong>Bypass</strong>:</p>
<ol>
<li>
<p>Expand <strong>Bypass</strong>.</p>
</li>
<li>
<p>In <strong>Bypass rule for these URLs</strong>, enter the URL(s) to exempt from the rate limiting rule. Enter each URL on its own line. An HTTP or HTTPS specified in the URL is automatically removed when the rule is saved and instead applies to both HTTP and HTTPS.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/waf/reference/legacy/old-rate-limiting-bypass.png" alt="Configuring two URLs to bypass for a rate limiting rule (one per line)." /></p>
<ol start="3">
<li>
<p>(Optional) Configure additional rate limiting features, based on your plan.</p>
</li>
<li>
<p>Select <strong>Save and Deploy</strong>.</p>
</li>
</ol>
<hr />
<h2 id="analytics">Analytics</h2>
<p>View rate limiting analytics for your zone in <strong>Analytics &amp; logs</strong> &gt; <strong>Security</strong>. Rate Limiting analytics uses solid lines to represent traffic that matches simulated requests and dotted lines to portray actual blocked requests. Logs generated by a rate limiting rule are only visible to Enterprise customers via <a href="/logs/">Cloudflare Logs</a>.</p>
<p>Cloudflare returns an <code>HTTP 429</code> error for blocked requests. Details on blocked requests per location are provided to Enterprise customers under <strong>Status codes</strong> in the analytics dashboard available at <strong>Analytics</strong> &gt; <strong>Traffic</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15692.md")
</aside>
<hr />
<h2 id="order-of-rule-execution">Order of rule execution</h2>
<p>Rate limiting rules are evaluated from the most recently created rule to the oldest rule.</p>
<p>For example, if a request matches the following two rules:</p>
<ul>
<li>Rule #1: Matching with <code>test.example.com</code> (created on 2024-03-01)</li>
<li>Rule #2: Matching with <code>*.example.com*</code> (created on 2024-03-12)</li>
</ul>
<p>Then rule #2 will trigger first because it was created last.</p>
<p>Additionally, when there is a match and the WAF applies a <em>Log</em> action, it continues evaluating other rate limiting rules, since <em>Log</em> is a non-terminating action. If the WAF applies any other action, no other rules will be evaluated.</p>
<hr />
<h2 id="limitations">Limitations</h2>
<p>Rate Limiting is designed to limit surges in traffic that exceed a user-defined rate. The system is not designed to allow a precise number of requests to reach the origin server. There might be cases where a delay is introduced between detecting the request and updating the internal counter. Because of this delay, which can be up to a few seconds, excess requests could still reach the origin before an action such as blocking or challenging is enforced.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/waf/reference/legacy/old-rate-limiting/troubleshooting/">Troubleshooting Rate Limiting (previous version)</a></li>
<li><a href="/api/resources/rate_limits/methods/create/">Configure Rate Limiting via the Cloudflare API</a></li>
</ul>
