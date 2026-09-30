---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/
  description: Actions available in custom load balancing rules.
  full_title: Load Balancing actions · Cloudflare Load Balancing docs
  head_html: <title>Load Balancing actions · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Actions available in custom load balancing rules."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/index.md"><meta property="og:title" content="Load Balancing actions · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Actions available in custom load balancing rules."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/#page","headline":"Load Balancing actions \u00b7 Cloudflare Load Balancing docs","description":"Actions available in custom load balancing rules.","url":"https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/additional-options/load-balancing-rules/actions/
  schema: 1
---
<p>Add <strong>actions</strong> to customize how your load balancer responds to certain HTTP requests.</p>
<p>Each load balancing rule includes one or more actions.</p>
<h2 id="supported-actions">Supported Actions</h2>
<p>This table lists the actions available for Load Balancing rules. For a walkthrough, refer to <a href="/load-balancing/additional-options/load-balancing-rules/create-rules/">Create Load Balancing rules</a>.</p>
<table style='width:100%'>
<thead>
<tr>
<th style='width:20%'>Action</th>
<th style='width:20%'>Options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Fixed response</em></td>
<td><em>N/A</em></td>
<td>Respond to the request with an HTTP status code and an optional message.</td>
</tr>
<tr>
<td><em>Override</em></td>
<td><em>Session affinity</em></td>
<td>Set the <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a> for the request. You can customize cookie behavior and session time-to-live (TTL).</td>
</tr>
<tr>
<td><em>Override</em></td>
<td><em>Load balancer TTL</em></td>
<td>Customize the load balancer session time-to-live (TTL).</td>
</tr>
<tr>
<td><em>Override</em></td>
<td><em>Steering policy</em></td>
<td>Update the <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">steering policy</a> associated with your load balancer.</td>
</tr>
<tr>
<td><em>Override</em></td>
<td><em>Fallback pool</em></td>
<td>Update the <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/#off---failover">fallback pools</a> associated with your load balancer.</td>
</tr>
<tr>
<td><em>Override</em></td>
<td><em>Pools</em></td>
<td>Update the <a href="/load-balancing/pools/">pools</a> associated with your load balancer.</td>
</tr>
<tr>
<td><em>Override</em></td>
<td><em>Region pools</em></td>
<td>Update the <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/">region pools</a> associated with your load balancer.</td>
</tr>
<tr>
<td><em>Override</em></td>
<td><em>Country pools</em></td>
<td>Update the <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/">country pools</a> associated with your load balancer.</td>
</tr>
<tr>
<td><em>Override</em></td>
<td><em>Terminates</em></td>
<td>Stop processing Load Balancing rules and apply the current load balancing logic to the request.</td>
</tr>
</tbody>
</table>
