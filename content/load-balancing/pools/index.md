---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/pools/
  description: Pools of origin servers for load balancing traffic distribution.
  full_title: Pools · Cloudflare Load Balancing docs
  head_html: <title>Pools · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Pools of origin servers for load balancing traffic distribution."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/pools/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/pools/index.md"><meta property="og:title" content="Pools · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Pools of origin servers for load balancing traffic distribution."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/pools/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/pools/#page","headline":"Pools \u00b7 Cloudflare Load Balancing docs","description":"Pools of origin servers for load balancing traffic distribution.","url":"https://developers.cloudflare.com/load-balancing/pools/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/pools/
  schema: 1
---
<div class="nb-glossary-definition"><p>Within Cloudflare, pools represent your endpoints and how they are organized. As such, a pool can be a group of several endpoints, or you could also have only one endpoint (an origin server, for example) per pool.</p>
<p>If you are familiar with DNS terminology, think of a pool as a “record set,” except Cloudflare only returns addresses that are considered healthy. You can attach health monitors to individual pools for customized monitoring. A pool can have either a single monitor or a monitor group attached — but not both.</p></div>
<p>For more details about how endpoints and pools become unhealthy, refer to <a href="/load-balancing/understand-basics/health-details/">Endpoint and pool health</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10354.md")
</aside>
<hr />
<h2 id="properties">Properties</h2>
<p>For an up-to-date list of pool properties, refer to <a href="/api/resources/load_balancers/subresources/pools/methods/list/">Pool properties</a> in our API documentation.</p>
<hr />
<h2 id="create-pools">Create pools</h2>
<p>For step-by-step guidance, refer to <a href="/load-balancing/pools/create-pool/">Create pools</a>.</p>
<hr />
<h2 id="per-endpoint-host-header-override">Per-endpoint Host header override</h2>
<p>When your application needs specialized routing (<code>CNAME</code> setup or custom hosts like Heroku), change the <code>Host</code> header used in health monitor requests. For more details, refer to <a href="/load-balancing/additional-options/override-http-host-headers/">Override HTTP Host headers</a>.</p>
<hr />
<h2 id="api-commands">API commands</h2>
<p>The Cloudflare API supports the following commands for pools. Examples are given for user-level endpoint but apply to the account-level endpoint as well.</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Method</th>
<th>Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/methods/create/">Create Pool</a></td>
<td><code>POST</code></td>
<td><code>accounts/:account_id/load_balancers/pools</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/methods/delete/">Delete Pool</a></td>
<td><code>DELETE</code></td>
<td><code>accounts/:account_id/load_balancers/pools/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/methods/list/">List Pools</a></td>
<td><code>GET</code></td>
<td><code>accounts/:account_id/load_balancers/pools</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/methods/get/">Pool Details</a></td>
<td><code>GET</code></td>
<td><code>accounts/:account_id/load_balancers/pools/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/subresources/health/methods/get/">Pool Health Details</a></td>
<td><code>GET</code></td>
<td><code>account/:account_id/load_balancers/pools/:id/health</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/methods/edit/">Overwrite specific properties</a></td>
<td><code>PATCH</code></td>
<td><code>accounts/:account_id/load_balancers/pools/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/methods/update/">Overwrite existing pool</a></td>
<td><code>PUT</code></td>
<td><code>accounts/:account_id/load_balancers/pools/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/subresources/health/methods/create/">Preview Pool</a></td>
<td><code>POST</code></td>
<td><code>account/:account_id/load_balancers/pools/:id/preview</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/subresources/references/methods/get/">List Pool References</a></td>
<td><code>GET</code></td>
<td><code>accounts/:account_id/load_balancers/pools/:id/references</code></td>
</tr>
</tbody>
</table>
