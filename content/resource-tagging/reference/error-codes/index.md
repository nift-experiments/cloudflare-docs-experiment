---
cp9:
  canonical: https://developers.cloudflare.com/resource-tagging/reference/error-codes/
  description: Tagging API error codes, causes, and resolutions.
  full_title: Error codes · Cloudflare Resource Tagging docs
  head_html: <title>Error codes · Cloudflare Resource Tagging docs</title><meta name="generator" content="Nift"><meta name="description" content="Tagging API error codes, causes, and resolutions."><link rel="canonical" href="https://developers.cloudflare.com/resource-tagging/reference/error-codes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/resource-tagging/reference/error-codes/index.md"><meta property="og:title" content="Error codes · Cloudflare Resource Tagging docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Tagging API error codes, causes, and resolutions."><meta property="og:url" content="https://developers.cloudflare.com/resource-tagging/reference/error-codes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Resource Tagging"><meta name="algolia_product_filter" content="Resource Tagging"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/resource-tagging/reference/error-codes/#page","headline":"Error codes \u00b7 Cloudflare Resource Tagging docs","description":"Tagging API error codes, causes, and resolutions.","url":"https://developers.cloudflare.com/resource-tagging/reference/error-codes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /resource-tagging/reference/error-codes/
  schema: 1
---
<h2 id="error-code-reference">Error code reference</h2>
<table>
<thead>
<tr>
<th>Code</th>
<th>HTTP status</th>
<th>Message</th>
<th>Likely cause</th>
<th>Resolution</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1002</code></td>
<td>400</td>
<td>Invalid set payload</td>
<td>Request body is malformed or missing required fields</td>
<td>Verify the body is valid JSON with <code>resource_type</code>, <code>resource_id</code>, and <code>tags</code></td>
</tr>
<tr>
<td><code>1003</code></td>
<td>400</td>
<td><code>resource_type</code> and <code>resource_id</code> are required</td>
<td>Missing query parameters</td>
<td>Include both <code>resource_type</code> and <code>resource_id</code> in the query string</td>
</tr>
<tr>
<td><code>1006</code></td>
<td>400</td>
<td>Invalid resource type</td>
<td>Unsupported resource type</td>
<td>Use a <a href="/resource-tagging/reference/resource-types/">supported resource type</a></td>
</tr>
<tr>
<td><code>1007</code></td>
<td>400</td>
<td>tag parameter must be in format...</td>
<td>Tag filter syntax is incorrect</td>
<td>Refer to <a href="/resource-tagging/how-to/filter-resources/">tag filtering syntax</a></td>
</tr>
<tr>
<td><code>1009</code></td>
<td>400</td>
<td><code>tag_key</code> is required</td>
<td>Missing <code>tag_key</code> parameter</td>
<td>Include the <code>tag_key</code> path parameter</td>
</tr>
<tr>
<td><code>1010</code></td>
<td>400</td>
<td>too many tag filters (maximum 20)</td>
<td>More than 20 <code>tag</code> query parameters</td>
<td>Reduce filters to 20 or fewer, or split across multiple requests</td>
</tr>
<tr>
<td><code>1011</code></td>
<td>400</td>
<td>tag key too long (maximum 256 characters)</td>
<td>Tag key exceeds 256 characters</td>
<td>Shorten the tag key</td>
</tr>
<tr>
<td><code>1012</code></td>
<td>400</td>
<td>tag value too long (maximum 1024 characters)</td>
<td>Tag value exceeds 1,024 characters</td>
<td>Shorten the tag value</td>
</tr>
<tr>
<td><code>1013</code></td>
<td>400</td>
<td>too many OR values in tag filter (maximum 10)</td>
<td>More than 10 comma-separated values in a single filter</td>
<td>Split into multiple filters</td>
</tr>
<tr>
<td><code>1014</code></td>
<td>400</td>
<td>Invalid tag key</td>
<td>Key contains invalid characters</td>
<td>Use only letters, digits, <code>_</code>, <code>.</code>, <code>-</code></td>
</tr>
<tr>
<td><code>1015</code></td>
<td>400</td>
<td>Invalid delete payload</td>
<td>Delete request body is malformed</td>
<td>Verify the body includes <code>resource_type</code> and <code>resource_id</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="error-1007-note">Error 1007 note</h3>
@markup("md", "content/.markup/bodies/12766.md")
</aside>
<h2 id="resource-not-found-behavior">Resource not found behavior</h2>
<p>In the current beta, <code>GET /accounts/{account_id}/tags</code> returns <code>500 Internal Server Error</code> for resources that do not exist or have never been tagged:</p>
<pre tabindex="0"><code>&quot;resource not found: type={resource_type} id={resource_id}&quot;&#10;</code></pre>
<p>List endpoints (<code>/tags/resources</code>, <code>/tags/keys</code>, <code>/tags/values/{key}</code>) return <code>200 OK</code> with an empty result array when no matches are found -- this is expected, not an error.</p>
<p>This <code>500</code> behavior is a known beta limitation and may change to <code>404</code> in a future release.</p>
