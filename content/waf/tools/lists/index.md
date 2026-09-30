---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/lists/
  description: Use lists to reference groups of items in rule expressions.
  full_title: Lists · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Lists · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Use lists to reference groups of items in rule expressions."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/lists/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/lists/index.md"><meta property="og:title" content="Lists · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use lists to reference groups of items in rule expressions."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/lists/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/waf/tools/lists/#page","headline":"Lists \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Use lists to reference groups of items in rule expressions.","url":"https://developers.cloudflare.com/waf/tools/lists/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/tools/lists/
  schema: 1
---
<p>Lists allow you to group items such as IP addresses, hostnames, or autonomous system numbers (ASNs), and reference them by name in Cloudflare <a href="/ruleset-engine/rules-language/expressions/">rule expressions</a>. Instead of adding each item individually to every rule that needs it, you define the group once and reuse it across rules and zones.</p>
<p>You can create your own <a href="/waf/tools/lists/custom-lists/">custom lists</a> or use <a href="/waf/tools/lists/managed-lists/">Managed Lists</a> maintained by Cloudflare, such as Managed IP Lists that provide threat intelligence data.</p>
<p>Lists have the following advantages:</p>
<ul>
<li>When creating a rule, using a list is easier and less error-prone than adding a long list of items such as IP addresses to a rule expression.</li>
<li>When updating a set of rules that target the same group of IP addresses (or hostnames), using an IP list (or a hostname list) is easier and less error prone than editing multiple rules.</li>
<li>Lists are easier to read and more informative, particularly when you use descriptive names for your lists.</li>
</ul>
<p>When you update the content of a list, any rules that use the list are automatically updated, so you can make a single change to your list rather than modify rules individually.</p>
<p>Cloudflare stores your lists at the account level. You can use the same list in rules of different zones in your Cloudflare account.</p>
<h2 id="supported-lists">Supported lists</h2>
<p>Cloudflare supports the following lists:</p>
<ul>
<li><a href="/waf/tools/lists/custom-lists/">Custom lists</a>: Includes custom IP lists, hostname lists, and ASN lists.</li>
<li><a href="/waf/tools/lists/managed-lists/">Managed Lists</a>: Lists managed and updated by Cloudflare, such as Managed IP Lists.</li>
</ul>
<p>Refer to each page for details.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/15713.md")
</aside>
<p>You can also use <a href="/ruleset-engine/rules-language/values/#inline-lists">inline lists</a> in rule expressions. Inline lists allow you to include values directly in an expression without creating a separate list first. However, any changes to the values require editing the rule itself.</p>
<h2 id="list-names">List names</h2>
<p>The name of a list must comply with the following requirements:</p>
<ul>
<li>The name uses only lowercase letters, numbers, and the underscore (<code>_</code>) character in the name. A valid name satisfies this regular expression: <code>^[a-z0-9_]+$</code>.</li>
<li>The maximum length of a list name is 50 characters.</li>
</ul>
<h2 id="work-with-lists">Work with lists</h2>
<h3 id="create-and-edit-lists">Create and edit lists</h3>
<p>You can <a href="/waf/tools/lists/create-dashboard/">create lists in the Cloudflare dashboard</a> or using the <a href="/waf/tools/lists/lists-api/">Lists API</a>.</p>
<p>After creating a list, you can add and remove items from the list, but you cannot change the list name or type.</p>
<h3 id="use-lists-in-expressions">Use lists in expressions</h3>
<p>Both the Cloudflare dashboard and the Cloudflare API support lists:</p>
<ul>
<li>To use lists in an expression from the Cloudflare dashboard, refer to <a href="/waf/tools/lists/use-in-expressions/">Use lists in expressions</a>.</li>
<li>To reference a list in an API expression, refer to <a href="/ruleset-engine/rules-language/values/#lists">Lists</a> in the Rules language reference.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15712.md")
</aside>
<h3 id="search-list-items">Search list items</h3>
<p>You can search for list items in the dashboard or <a href="/api/resources/rules/subresources/lists/subresources/items/methods/list/">via API</a>.</p>
<p>For IP lists, Cloudflare returns IP addresses or ranges that start with your search query. For example, searching <code>192.0.2</code> matches <code>192.0.2.1</code> and <code>192.0.2.0/24</code>, but searching for <code>192.0.2.100</code> does not match a <span class="nb-glossary-tooltip" title="CIDR">CIDR range</span> like <code>192.0.2.0/24</code> that contains that address.</p>
<p>For Bulk Redirect Lists, Cloudflare returns entries where the source URL or target URL contains your search query.</p>
<h2 id="availability">Availability</h2>
<p>List availability varies according to the list type and your Cloudflare plan and subscriptions.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Number of custom lists (any type)</td>
<td>1</td>
<td>10</td>
<td>10</td>
<td>1,000</td>
</tr>
<tr>
<td>Max. number of list items (across all custom lists)</td>
<td>10,000</td>
<td>10,000</td>
<td>10,000</td>
<td>500,000</td>
</tr>
<tr>
<td>IP lists</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Other custom lists (hostnames, ASNs)</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Managed IP Lists</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>Notes:</p>
<ul>
<li>
<p>The number of available custom lists depends on the highest plan in your account. Any account with at least one paid plan will get the highest quota.</p>
</li>
<li>
<p>Customers on Enterprise plans can create a maximum of 1,000 custom lists in total across different list types. The following additional limits apply:</p>
<ul>
<li>Up to 40 hostname lists, with a maximum of 10,000 list items across all hostname lists.</li>
<li>Up to 40 ASN lists, with a maximum of 30,000 list items across all ASN lists.</li>
</ul>
</li>
<li>
<p>Customers on Enterprise plans may contact their account team if they need more custom lists or a larger maximum number of items across lists.</p>
</li>
<li>
<p>For details on the availability of Bulk Redirect Lists, refer to the <a href="/rules/url-forwarding/#availability">Rules</a> documentation.</p>
</li>
</ul>
<hr />
<h2 id="user-role-requirements">User role requirements</h2>
<p>The following user roles have access to the list management functionality:</p>
<ul>
<li>Super Administrator</li>
<li>Administrator</li>
<li>Firewall</li>
</ul>
<h2 id="final-remarks">Final remarks</h2>
<p>You can only delete a list when no rules (enabled or disabled) reference it.</p>
<p>Cloudflare will apply the following rules when you add items to an existing list (either manually or via CSV file):</p>
<ul>
<li>Do not remove any existing list items before updating/adding items.</li>
<li>Update items that were already in the list.</li>
<li>Add items that were not present in the list.</li>
</ul>
<p>To replace the entire contents of a list at once, format the data as an array and use the <a href="/api/resources/rules/subresources/lists/subresources/items/methods/update/">Update all list items</a> operation in the <a href="/waf/tools/lists/lists-api/endpoints/">Lists API</a>.</p>
<p>The Cloudflare dashboard does not support downloading a list as a CSV file. To export list contents, use the <a href="/api/resources/rules/subresources/lists/subresources/items/methods/list/">Get list items</a> API operation.</p>
