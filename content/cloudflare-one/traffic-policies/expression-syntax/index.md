---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/expression-syntax/
  description: Learn about the expression syntax used to build Gateway DNS, HTTP, Network, Egress, and Resolver policies.
  full_title: Gateway policy expressions · Cloudflare One docs
  head_html: <title>Gateway policy expressions · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about the expression syntax used to build Gateway DNS, HTTP, Network, Egress, and Resolver policies."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/expression-syntax/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/expression-syntax/index.md"><meta property="og:title" content="Gateway policy expressions · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about the expression syntax used to build Gateway DNS, HTTP, Network, Egress, and Resolver policies."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/expression-syntax/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/expression-syntax/#page","headline":"Gateway policy expressions \u00b7 Cloudflare One docs","description":"Learn about the expression syntax used to build Gateway DNS, HTTP, Network, Egress, and Resolver policies.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/expression-syntax/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/expression-syntax/
  schema: 1
---
<p>Gateway policies use a wirefilter-based expression language to match traffic against selectors (criteria). This syntax is similar to, but distinct from, the <a href="/ruleset-engine/rules-language/">Rules language</a> used by WAF, Rules, and other Cloudflare products. Refer to <a href="#gateway-versus-ruleset-engine">Gateway versus Ruleset Engine</a> for details on the differences.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/4417.md")
</aside>
<h2 id="expression-syntax">Expression syntax</h2>
<p>Gateway expressions follow this pattern:</p>
<pre tabindex="0"><code class="language-txt">&lt;field&gt; &lt;operator&gt; &lt;value&gt;&#10;</code></pre>
<p>For example:</p>
<pre tabindex="0"><code class="language-txt">dns.fqdn == &quot;example.com&quot;&#10;http.request.host == &quot;api.example.com&quot;&#10;identity.email == &quot;user@company.com&quot;&#10;</code></pre>
<h3 id="operators">Operators</h3>
<p>Gateway supports the following operators:</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Name</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>==</code></td>
<td>Equals</td>
<td><code>dns.fqdn == &quot;example.com&quot;</code></td>
</tr>
<tr>
<td><code>!=</code></td>
<td>Does not equal</td>
<td><code>http.request.host != &quot;blocked.com&quot;</code></td>
</tr>
<tr>
<td><code>in</code></td>
<td>Value is in set</td>
<td><code>net.dst.port in {80 443}</code></td>
</tr>
<tr>
<td><code>matches</code></td>
<td>Matches regular expression</td>
<td><code>http.request.host matches &quot;.*\\.example\\.com&quot;</code></td>
</tr>
<tr>
<td><code>&gt;</code></td>
<td>Greater than</td>
<td><code>http.upload.file.size &gt; 10</code></td>
</tr>
<tr>
<td><code>&gt;=</code></td>
<td>Greater than or equal to</td>
<td><code>http.download.file.size &gt;= 100</code></td>
</tr>
<tr>
<td><code>&lt;</code></td>
<td>Less than</td>
<td><code>http.upload.file.size &lt; 50</code></td>
</tr>
<tr>
<td><code>&lt;=</code></td>
<td>Less than or equal to</td>
<td><code>http.download.file.size &lt;= 200</code></td>
</tr>
</tbody>
</table>
<h3 id="logical-operators">Logical operators</h3>
<p>Combine multiple conditions using logical operators:</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Name</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>and</code></td>
<td>Logical AND</td>
<td><code>dns.fqdn == &quot;example.com&quot; and identity.email == &quot;admin@company.com&quot;</code></td>
</tr>
<tr>
<td><code>or</code></td>
<td>Logical OR</td>
<td><code>net.dst.port == 80 or net.dst.port == 443</code></td>
</tr>
<tr>
<td><code>not</code></td>
<td>Logical NOT</td>
<td><code>not(identity.email == &quot;guest@company.com&quot;)</code></td>
</tr>
</tbody>
</table>
<h2 id="array-handling">Array handling</h2>
<p>Some Gateway fields return arrays (multiple values). Use the <code>any()</code> function to match if any element in the array meets the condition:</p>
<pre tabindex="0"><code class="language-txt">any(http.request.uri.content_category[*] in {17 85 102})&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">any(identity.groups[*].name in {&quot;Engineering&quot; &quot;Security&quot;})&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">any(http.request.domains[*] == &quot;example.com&quot;)&#10;</code></pre>
<p>The <code>[*]</code> notation indicates that the function should evaluate all elements in the array.</p>
<h2 id="list-handling">List handling</h2>
<p>You can reference <a href="/cloudflare-one/reusable-components/lists/">lists</a> in your expressions using the list UUID:</p>
<pre tabindex="0"><code class="language-txt">http.request.host in $&lt;LIST_UUID&gt;&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">any(http.request.domains[*] in $&lt;LIST_UUID&gt;)&#10;</code></pre>
<p>To find a list's UUID, go to <strong>My Team</strong> &gt; <strong>Lists</strong> in Zero Trust and select the list. The UUID appears in the browser URL.</p>
<h2 id="common-field-patterns">Common field patterns</h2>
<p>Each Gateway policy type has its own set of available fields. The following table shows the field prefixes used by each policy type:</p>
<table>
<thead>
<tr>
<th>Policy type</th>
<th>Field prefix</th>
<th>Example fields</th>
</tr>
</thead>
<tbody>
<tr>
<td>DNS</td>
<td><code>dns.</code></td>
<td><code>dns.fqdn</code>, <code>dns.content_category</code>, <code>dns.src_ip</code></td>
</tr>
<tr>
<td>HTTP</td>
<td><code>http.</code></td>
<td><code>http.request.host</code>, <code>http.request.uri</code>, <code>http.request.domains</code></td>
</tr>
<tr>
<td>Network</td>
<td><code>net.</code></td>
<td><code>net.dst.ip</code>, <code>net.dst.port</code>, <code>net.src.ip</code></td>
</tr>
<tr>
<td>Identity</td>
<td><code>identity.</code></td>
<td><code>identity.email</code>, <code>identity.groups</code>, <code>identity.name</code></td>
</tr>
<tr>
<td>Device posture</td>
<td><code>device_posture.</code></td>
<td><code>device_posture.checks.passed</code></td>
</tr>
</tbody>
</table>
<p>For a complete list of available fields for each policy type, refer to the selectors documentation linked at the top of this page.</p>
<h2 id="example-expressions">Example expressions</h2>
<h3 id="block-a-domain-in-a-dns-policy">Block a domain in a DNS policy</h3>
<pre tabindex="0"><code class="language-txt">dns.fqdn == &quot;example.com&quot;&#10;</code></pre>
<h3 id="block-multiple-content-categories-in-an-http-policy">Block multiple content categories in an HTTP policy</h3>
<pre tabindex="0"><code class="language-txt">any(http.request.uri.content_category[*] in {17 85 102})&#10;</code></pre>
<h3 id="allow-traffic-from-a-specific-user-group">Allow traffic from a specific user group</h3>
<pre tabindex="0"><code class="language-txt">any(identity.groups[*].name in {&quot;Engineering&quot;})&#10;</code></pre>
<h3 id="block-traffic-to-a-destination-ip-range-in-a-network-policy">Block traffic to a destination IP range in a Network policy</h3>
<pre tabindex="0"><code class="language-txt">net.dst.ip in {10.0.0.0/8}&#10;</code></pre>
<h3 id="combine-identity-and-traffic-conditions">Combine identity and traffic conditions</h3>
<pre tabindex="0"><code class="language-txt">http.request.host == &quot;internal.example.com&quot; and identity.email matches &quot;.*@company.com&quot;&#10;</code></pre>
<h2 id="gateway-versus-ruleset-engine">Gateway versus Ruleset Engine</h2>
<p>The following table summarizes the key differences between the Rules language](/ruleset-engine/rules-language/) (supported by the Ruleset Engine) and Gateway policy expressions:</p>
<table>
<thead>
<tr>
<th></th>
<th>Ruleset Engine</th>
<th>Gateway</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Products</strong></td>
<td>WAF, Transform Rules, Cache Rules, Configuration Rules</td>
<td>DNS, HTTP, Network, Egress, Resolver policies</td>
</tr>
<tr>
<td><strong>Field examples</strong></td>
<td><code>http.request.uri.path</code>, <code>cf.bot_management.score</code>, <code>ip.src</code></td>
<td><code>dns.fqdn</code>, <code>http.request.host</code>, <code>identity.email</code></td>
</tr>
<tr>
<td><strong>Identity fields</strong></td>
<td>Not available</td>
<td>Available (for example, <code>identity.email</code>, <code>identity.groups</code>)</td>
</tr>
<tr>
<td><strong>DNS fields</strong></td>
<td>Not available</td>
<td>Available (for example, <code>dns.fqdn</code>, <code>dns.content_category</code>)</td>
</tr>
<tr>
<td><strong>Documentation</strong></td>
<td><a href="/ruleset-engine/rules-language/">Rules language</a></td>
<td><a href="/cloudflare-one/traffic-policies/">Traffic policies</a></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4416.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a></li>
<li><a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a></li>
<li><a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a></li>
<li><a href="/cloudflare-one/traffic-policies/identity-selectors/">Identity-based policies</a></li>
<li><a href="/cloudflare-one/reusable-components/lists/">Lists</a></li>
</ul>
