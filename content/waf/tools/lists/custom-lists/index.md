---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/lists/custom-lists/
  description: Create custom lists of IPs, hostnames, or ASNs for use in rules.
  full_title: Custom lists · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Custom lists · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create custom lists of IPs, hostnames, or ASNs for use in rules."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/lists/custom-lists/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/lists/custom-lists/index.md"><meta property="og:title" content="Custom lists · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create custom lists of IPs, hostnames, or ASNs for use in rules."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/lists/custom-lists/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/tools/lists/custom-lists/#page","headline":"Custom lists \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Create custom lists of IPs, hostnames, or ASNs for use in rules.","url":"https://developers.cloudflare.com/waf/tools/lists/custom-lists/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/tools/lists/custom-lists/
  schema: 1
---
<p>A custom list contains one or more items of the same type (for example, IP addresses, hostnames, or ASNs) that you can reference collectively, by name, in rule expressions.</p>
<p>Cloudflare supports the following custom list types:</p>
<ul>
<li><a href="#ip-lists">Lists with IP addresses</a> (also known as IP lists)</li>
<li><a href="#lists-with-hostnames">Lists with hostnames</a></li>
<li><a href="#lists-with-asns">Lists with ASNs</a> (<a href="https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/">autonomous system</a> numbers)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15717.md")
</aside>
<p>Each type has its own properties and CSV file format. Refer to the following sections for details.</p>
<p>For more information on lists managed by Cloudflare, such as Managed IP Lists, refer to <a href="/waf/tools/lists/managed-lists/">Managed Lists</a>.</p>
<h2 id="create-a-custom-list">Create a custom list</h2>
<p>Refer to <a href="/waf/tools/lists/create-dashboard/">Create a list in the dashboard</a> or to the <a href="/waf/tools/lists/lists-api/">Lists API</a> page.</p>
<h2 id="use-a-custom-list">Use a custom list</h2>
<p>Use custom lists in rule <a href="/ruleset-engine/rules-language/expressions/">expressions</a> with the <code>in</code> operator and with a field supported by the custom list:</p>
<pre tabindex="0"><code class="language-txt">&lt;FIELD&gt; in $&lt;LIST_NAME&gt;&#10;</code></pre>
<p>The fields you can use vary according to the list item type:</p>
<table>
<thead>
<tr>
<th>List item type</th>
<th>Available fields</th>
</tr>
</thead>
<tbody>
<tr>
<td>IP address</td>
<td>Fields with type <code>IP address</code> listed in the <a href="/ruleset-engine/rules-language/fields/reference/">Fields reference</a></td>
</tr>
<tr>
<td>Hostname</td>
<td><code>http.host</code></td>
</tr>
<tr>
<td>ASN</td>
<td><code>ip.src.asnum</code></td>
</tr>
</tbody>
</table>
<p>For more information and examples, refer to <a href="/waf/tools/lists/use-in-expressions/">Use lists in expressions</a>.</p>
<hr />
<h2 id="custom-list-types">Custom list types</h2>
<h3 id="lists-with-ip-addresses-ip-lists-ip-lists">Lists with IP addresses (IP lists) </h3>
<p>List items in custom lists with IP addresses must be in one of the following formats:</p>
<ul>
<li>Individual IPv4 addresses</li>
<li>Individual IPv6 addresses</li>
<li>IPv4 CIDR ranges with a prefix from <code>/8</code> to <code>/32</code></li>
<li>IPv6 CIDR ranges with a prefix from <code>/12</code> to <code>/128</code></li>
</ul>
<p>The same list can contain both individual addresses and CIDR ranges.</p>
<p>You can use uppercase or lowercase characters for IPv6 addresses in lists. However, when you save the list, uppercase characters are converted to lowercase.</p>
<details class="nb-details"><summary>CSV file format</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15718.md")
</div></details>
<h3 id="lists-with-hostnames">Lists with hostnames</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15716.md")
</aside>
<p>List items in custom lists with hostnames must be Fully Qualified Domain Names (FQDNs). An item may contain a <code>*</code> prefix/subdomain wildcard, which must be followed by a <code>.</code> (period). An item cannot include a scheme (for example, <code>https://</code>) or a URL path.</p>
<p>For example, the following entries would be valid for a custom list with hostnames:</p>
<ul>
<li><code>example.com</code></li>
<li><code>api.example.com</code></li>
<li><code>*.example.com</code></li>
</ul>
<p>However, <code>example.com/path/subfolder</code> would not be a valid entry.</p>
<p>You can add any valid hostname (a valid FQDN) to a custom list with hostnames. The hostnames do not need to belong to the current Cloudflare account.</p>
<details class="nb-details"><summary>CSV file format</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15719.md")
</div></details>
<h3 id="lists-with-asns">Lists with ASNs</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15715.md")
</aside>
<p>List items in custom lists with autonomous system numbers (ASNs) must be integer values.</p>
<p>For example, the following entries would be valid for a list with ASNs:</p>
<ul>
<li><code>1</code></li>
<li><code>13335</code></li>
<li><code>64512</code></li>
</ul>
<details class="nb-details"><summary>CSV file format</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15720.md")
</div></details>
