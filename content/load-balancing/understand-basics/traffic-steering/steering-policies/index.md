---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/
  description: Policies that control how traffic is distributed across pools.
  full_title: Global traffic steering policies · Cloudflare Load Balancing docs
  head_html: <title>Global traffic steering policies · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Policies that control how traffic is distributed across pools."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/index.md"><meta property="og:title" content="Global traffic steering policies · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Policies that control how traffic is distributed across pools."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/#page","headline":"Global traffic steering policies \u00b7 Cloudflare Load Balancing docs","description":"Policies that control how traffic is distributed across pools.","url":"https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/understand-basics/traffic-steering/steering-policies/
  schema: 1
---
<p>Global traffic steering policies decide how a load balancer routes traffic to attached and healthy pools.
<br /></p>
<ul class="directory-listing"><li><a href="/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/">Standard</a></li><li><a href="/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/">Geo</a></li><li><a href="/load-balancing/understand-basics/traffic-steering/steering-policies/dynamic-steering/">Dynamic</a></li><li><a href="/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/">Proximity</a></li><li><a href="/load-balancing/understand-basics/traffic-steering/steering-policies/least-outstanding-requests/">Least Outstanding Requests</a></li></ul>
<h2 id="edns-client-subnet-ecs-support">EDNS Client Subnet (ECS) support</h2>
<p><span class="nb-glossary-tooltip" title="EDNS Client Subnet (ECS)">EDNS Client Subnet (ECS)</span> support provides customers with more control over location-based steering during
gray-clouded DNS resolutions and can be used for proximity or geo (country) steering.</p>
<p>Customers can configure their load balancer using the <code>location_strategy</code> parameter, which includes the properties <code>prefer_ecs</code> and <code>mode</code>.</p>
<p><code>prefer_ecs</code> determines whether the ECS geolocation should be preferred as the authoritative location.</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;always&quot;</code></td>
<td>Always prefers ECS.</td>
</tr>
<tr>
<td><code>&quot;never&quot;</code></td>
<td>Never prefers ECS.</td>
</tr>
<tr>
<td><code>&quot;proximity&quot;</code></td>
<td>Prefers ECS only when <code>steering_policy=&quot;proximity&quot;</code>.</td>
</tr>
<tr>
<td><code>&quot;geo&quot;</code></td>
<td>Prefers ECS only when <code>steering_policy=&quot;geo&quot;</code> and only supports country-level steering.</td>
</tr>
</tbody>
</table>
<p><code>mode</code> determines the authoritative location when ECS is not preferred, does not exist in the request, or its geolocation lookup is unsuccessful.</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;pop&quot;</code></td>
<td>Uses the Cloudflare PoP location.</td>
</tr>
<tr>
<td><code>&quot;resolver_ip&quot;</code></td>
<td>Uses the DNS resolver geolocation data. If the geolocation lookup is unsuccessful, it uses the Cloudflare PoP location.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10452.md")
</aside>
