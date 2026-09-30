---
cp9:
  canonical: https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/
  description: API endpoints for managing filters and firewall rules.
  full_title: Endpoints - Firewall rules · Cloudflare Firewall Rules (deprecated) docs
  head_html: <title>Endpoints - Firewall rules · Cloudflare Firewall Rules (deprecated) docs</title><meta name="generator" content="Nift"><meta name="description" content="API endpoints for managing filters and firewall rules."><link rel="canonical" href="https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/index.md"><meta property="og:title" content="Endpoints - Firewall rules · Cloudflare Firewall Rules (deprecated) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API endpoints for managing filters and firewall rules."><meta property="og:url" content="https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Firewall Rules (deprecated)"><meta name="algolia_product_filter" content="Firewall Rules (deprecated)"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Firewall Rules (deprecated)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/#page","headline":"Endpoints - Firewall rules \u00b7 Cloudflare Firewall Rules (deprecated) docs","description":"API endpoints for managing filters and firewall rules.","url":"https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /firewall/api/cf-firewall-rules/endpoints/
  schema: 1
---
<p>To invoke a Cloudflare Firewall Rules API operation, append the endpoint to the Cloudflare API base URL:</p>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4/&#10;</code></pre>
<p>For authentication instructions, refer to <a href="/fundamentals/api/">Getting Started: Requests</a> in the Cloudflare API documentation.</p>
<p>For help with endpoints and pagination, refer to <a href="/fundamentals/api/">Getting Started: Endpoints</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8706.md")
</aside>
<p>The Cloudflare Firewall Rules API supports the operations outlined below. Visit the pages in this section for examples.</p>
<table style="table-layout:fixed; width:100%">
<thead>
<tr>
<th>Operation</th>
<th style="width: 60%">Method & Endpoint</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/create/">
          Create firewall rules
        </a>
</td>
<td>`POST zones/<ZONE_ID>/firewall/rules`</td>
<td>Handled as a single transaction. If there is an error, the entire operation fails.</td>
</tr>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/list/">
          List firewall rules
        </a>
</td>
<td>`GET zones/<ZONE_ID>/firewall/rules`</td>
<td>
        Lists all current firewall rules. Results return paginated with 25 items per page by default. Use optional parameters to narrow results.
</td>
</tr>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/get/">
          Get a firewall rule
        </a>
</td>
<td>`GET zones/<ZONE_ID>/firewall/rules/<RULE_ID>`</td>
<td>Retrieve a single firewall rule by ID.</td>
</tr>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/bulk_update/">
          Update firewall rules
        </a>
</td>
<td>`PUT zones/<ZONE_ID>/firewall/rules`</td>
<td>
        Handled as a single transaction. All rules must exist for operation to succeed. If there is
        an error, the entire operation fails.
</td>
</tr>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/update/">
          Update a firewall rule
        </a>
</td>
<td>`PUT zones/<ZONE_ID>/firewall/rules/<RULE_ID>`</td>
<td>Update a single firewall rule by ID.</td>
</tr>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/bulk_delete/">
          Delete firewall rules
        </a>
</td>
<td>`DELETE zones/<ZONE_ID>/firewall/rules`</td>
<td>
        <p>Delete existing firewall rules. Must specify list of firewall rule IDs.</p>
        <p>
          Empty requests result in no deletion. Returns HTTP status code 200 if a specified rule
          does not exist.
        </p>
</td>
</tr>
<tr>
<td>
        <a href="/api/resources/firewall/subresources/rules/methods/delete/">
          Delete a firewall rule
        </a>
</td>
<td>`DELETE zones/<ZONE_ID>/firewall/rules/<RULE_ID>`</td>
<td>
        <p>Delete a firewall rule by ID.</p>
</td>
</tr>
</tbody>
</table>
