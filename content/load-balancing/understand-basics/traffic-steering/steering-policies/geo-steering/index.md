---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/
  description: Route traffic to pools based on visitor geographic location.
  full_title: Geo steering · Cloudflare Load Balancing docs
  head_html: <title>Geo steering · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Route traffic to pools based on visitor geographic location."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/index.md"><meta property="og:title" content="Geo steering · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route traffic to pools based on visitor geographic location."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Load Balancing"><meta name="pcx_tags" content="Geolocation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/#page","headline":"Geo steering \u00b7 Cloudflare Load Balancing docs","description":"Route traffic to pools based on visitor geographic location.","url":"https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Geolocation"]}</script>
  markdown: true
  noindex: false
  route: /load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/
  schema: 1
---
<p><strong>Geo steering</strong> directs traffic to pools tied to specific countries, regions, or — for Enterprise customers only — data centers.</p>
<p>This option is extremely useful when you want site visitors to access the endpoint closest to them, which improves page-loading performance.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10456.md")
</aside>
<h2 id="pool-assignment">Pool assignment</h2>
<p>You can assign multiple pools to the same area and the load balancer will use them in failover order. Any options not explicitly defined — whether in data centers, countries, or regions — will fall back to using default pools and failover.</p>
<h3 id="region-steering">Region steering</h3>
<p>Cloudflare has <a href="/load-balancing/reference/region-mapping-api/#list-of-load-balancer-regions">13 geographic regions</a> that span the world. The region of a client is determined by the region of the Cloudflare data center that answers the client’s DNS query.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10455.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10459.md")
</div></div>
<h3 id="country-steering">Country steering</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10462.md")
</div></div>
<h3 id="pop-steering">PoP steering</h3>
<p>When creating a load balancer <a href="/api/resources/load_balancers/methods/create/">via the API</a>, include the <code>pop_pools</code> object to map Cloudflare data centers to a list of pool IDs (ordered by their failover priority).</p>
<p>For help finding data center identifiers, refer to <a href="https://community.cloudflare.com/t/is-there-a-way-to-retrieve-cloudflare-pops-list-and-locations-programmatically/234643">this community thread</a>.</p>
<p>Any data center not explicitly defined will fall back to using the corresponding <code>country_pool</code>, then <code>region_pool</code> mapping (if it exists), and finally to associated default pools.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10454.md")
</aside>
<h3 id="failover-behavior">Failover behavior</h3>
<p>A fallback pool will be used if there is only one pool in the same region and it is unavailable.
If there are multiple pools in the same region, the order of the pools will be respected. For example, if the first pool is unavailable, the second pool will be used.</p>
