---
cp9:
  canonical: https://developers.cloudflare.com/ai-crawl-control/reference/graphql-api/
  description: Query AI Crawl Control analytics data using the GraphQL Analytics API.
  full_title: GraphQL API · Cloudflare AI Crawl Control docs
  head_html: <title>GraphQL API · Cloudflare AI Crawl Control docs</title><meta name="generator" content="Nift"><meta name="description" content="Query AI Crawl Control analytics data using the GraphQL Analytics API."><link rel="canonical" href="https://developers.cloudflare.com/ai-crawl-control/reference/graphql-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-crawl-control/reference/graphql-api/index.md"><meta property="og:title" content="GraphQL API · Cloudflare AI Crawl Control docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query AI Crawl Control analytics data using the GraphQL Analytics API."><meta property="og:url" content="https://developers.cloudflare.com/ai-crawl-control/reference/graphql-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Crawl Control"><meta name="algolia_product_filter" content="AI Crawl Control"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="AI Crawl Control"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-crawl-control/reference/graphql-api/#page","headline":"GraphQL API \u00b7 Cloudflare AI Crawl Control docs","description":"Query AI Crawl Control analytics data using the GraphQL Analytics API.","url":"https://developers.cloudflare.com/ai-crawl-control/reference/graphql-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-crawl-control/reference/graphql-api/
  schema: 1
---
<p>AI Crawl Control analytics are available through Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can query the same data shown in the dashboard to build custom reports, integrate with monitoring systems, or export for analysis. Test queries using the <a href="https://graphql.cloudflare.com/">GraphQL API Explorer</a>, or capture the exact queries the dashboard uses via <a href="/analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard/">Chrome DevTools</a>.</p>
<h2 id="key-filters">Key filters</h2>
<table>
<thead>
<tr>
<th>Filter</th>
<th>Description</th>
<th>Availability</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>requestSource: &quot;eyeball&quot;</code></td>
<td>Real client requests only. Excludes internal Cloudflare traffic.</td>
<td>All plans</td>
</tr>
<tr>
<td><code>userAgent_like: &quot;%...%&quot;</code></td>
<td>Filter by <a href="/ai-crawl-control/reference/bots/">user agent</a>. Can be spoofed.</td>
<td>All plans</td>
</tr>
<tr>
<td><code>edgeResponseStatus_geq</code> / <code>_lt</code></td>
<td>Filter by HTTP status code range.</td>
<td>All plans</td>
</tr>
<tr>
<td><code>clientRequestPath_like: &quot;%...%&quot;</code></td>
<td>Filter by URL path pattern.</td>
<td>All plans</td>
</tr>
<tr>
<td><code>clientRefererHost_like: &quot;%...%&quot;</code></td>
<td>Filter by <a href="/ai-crawl-control/reference/bots/#referrer-domains-by-operator">referrer domain</a>.</td>
<td>Paid plans only</td>
</tr>
<tr>
<td><code>botDetectionIds_hasany: [...]</code></td>
<td>Filter by <a href="/ai-crawl-control/reference/bots/">detection IDs</a>. Reliably verified by Cloudflare.</td>
<td><a href="/bots/get-started/bot-management/">Bot Management</a></td>
</tr>
</tbody>
</table>
<h2 id="query-examples">Query examples</h2>
<details class="nb-details"><summary>Get AI crawler requests over time using detection IDs</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2719.md")
</div></details>
<details class="nb-details"><summary>Get AI crawler requests over time using user agent</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2720.md")
</div></details>
<details class="nb-details"><summary>Get top crawled paths</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2721.md")
</div></details>
<details class="nb-details"><summary>Get AI referral traffic</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2722.md")
</div></details>
<details class="nb-details"><summary>Get data transfer by crawler</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2723.md")
</div></details>
<h2 id="related">Related</h2>
<ul>
<li><a href="/ai-crawl-control/reference/bots/">Bot reference</a> — Detection IDs and user agents</li>
<li><a href="/analytics/graphql-api/">GraphQL Analytics API</a> — Full API documentation</li>
</ul>
