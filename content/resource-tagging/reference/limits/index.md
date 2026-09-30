---
cp9:
  canonical: https://developers.cloudflare.com/resource-tagging/reference/limits/
  description: API limits, tag key validation rules, and pagination behavior.
  full_title: Limits and validation · Cloudflare Resource Tagging docs
  head_html: <title>Limits and validation · Cloudflare Resource Tagging docs</title><meta name="generator" content="Nift"><meta name="description" content="API limits, tag key validation rules, and pagination behavior."><link rel="canonical" href="https://developers.cloudflare.com/resource-tagging/reference/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/resource-tagging/reference/limits/index.md"><meta property="og:title" content="Limits and validation · Cloudflare Resource Tagging docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API limits, tag key validation rules, and pagination behavior."><meta property="og:url" content="https://developers.cloudflare.com/resource-tagging/reference/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Resource Tagging"><meta name="algolia_product_filter" content="Resource Tagging"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/resource-tagging/reference/limits/#page","headline":"Limits and validation \u00b7 Cloudflare Resource Tagging docs","description":"API limits, tag key validation rules, and pagination behavior.","url":"https://developers.cloudflare.com/resource-tagging/reference/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /resource-tagging/reference/limits/
  schema: 1
---
<h2 id="api-limits">API limits</h2>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
<th>Error code</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum tags per account</td>
<td>10,000 (beta)</td>
<td>N/A</td>
</tr>
<tr>
<td>Maximum tag key length</td>
<td>256 characters</td>
<td><code>1011</code></td>
</tr>
<tr>
<td>Maximum tag value length</td>
<td>1,024 characters</td>
<td><code>1012</code></td>
</tr>
<tr>
<td>Maximum tag filters per query</td>
<td>20</td>
<td><code>1010</code></td>
</tr>
<tr>
<td>Maximum OR values per filter</td>
<td>10</td>
<td><code>1013</code></td>
</tr>
<tr>
<td>Results per page</td>
<td>100 (fixed)</td>
<td>N/A</td>
</tr>
</tbody>
</table>
<p>When a limit is exceeded, the API returns <code>400 Bad Request</code> with the corresponding error code.</p>
<p>During the beta, each account is limited to 10,000 total tags. If you need a higher limit, contact <a href="/support/contacting-cloudflare-support/">Cloudflare support</a>.</p>
<h2 id="case-sensitivity">Case sensitivity</h2>
<p>Tag keys and values are case-sensitive. <code>Environment</code>, <code>environment</code>, and <code>ENVIRONMENT</code> are treated as three distinct keys. Be consistent with casing conventions across your organization to avoid duplicate keys.</p>
<h2 id="tag-key-validation">Tag key validation</h2>
<p>Tag keys must follow these character rules:</p>
<h3 id="allowed">Allowed</h3>
<ul>
<li>Unicode letters (any language)</li>
<li>Unicode digits (0-9)</li>
<li>Underscores (<code>_</code>)</li>
<li>Periods (<code>.</code>)</li>
<li>Hyphens (<code>-</code>)</li>
</ul>
<h3 id="not-allowed">Not allowed</h3>
<ul>
<li>Empty strings</li>
<li>Spaces</li>
<li>Special characters (except <code>_</code>, <code>.</code>, <code>-</code>)</li>
</ul>
<h3 id="examples">Examples</h3>
<table>
<thead>
<tr>
<th>Key</th>
<th>Valid</th>
<th>Reason</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>environment</code></td>
<td>Yes</td>
<td>Letters only</td>
</tr>
<tr>
<td><code>team_name</code></td>
<td>Yes</td>
<td>Underscore</td>
</tr>
<tr>
<td><code>cost-center</code></td>
<td>Yes</td>
<td>Hyphen</td>
</tr>
<tr>
<td><code>owner.email</code></td>
<td>Yes</td>
<td>Period</td>
</tr>
<tr>
<td><code>env123</code></td>
<td>Yes</td>
<td>Letters and digits</td>
</tr>
<tr>
<td><code>env name</code></td>
<td><strong>No</strong></td>
<td>Contains space</td>
</tr>
<tr>
<td><code>team@work</code></td>
<td><strong>No</strong></td>
<td>Special character <code>@</code></td>
</tr>
<tr>
<td>(empty)</td>
<td><strong>No</strong></td>
<td>Empty string</td>
</tr>
</tbody>
</table>
<p>Invalid tag keys return <code>400 Bad Request</code> with error code <code>1014</code>.</p>
<h2 id="pagination">Pagination</h2>
<p>List endpoints use cursor-based pagination with a fixed page size of 100. The page size is not configurable.</p>
<p>Paginated endpoints:</p>
<ul>
<li><code>GET /accounts/{account_id}/tags/keys</code></li>
<li><code>GET /accounts/{account_id}/tags/resources</code></li>
<li><code>GET /accounts/{account_id}/tags/values/{tag_key}</code></li>
</ul>
<p>Refer to <a href="/resource-tagging/how-to/filter-resources/#pagination">Filter resources by tag</a> for pagination examples.</p>
