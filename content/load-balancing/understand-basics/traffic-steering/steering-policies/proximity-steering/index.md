---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/
  description: Route traffic to the nearest pool by geographic proximity.
  full_title: Proximity steering · Cloudflare Load Balancing docs
  head_html: <title>Proximity steering · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Route traffic to the nearest pool by geographic proximity."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/index.md"><meta property="og:title" content="Proximity steering · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route traffic to the nearest pool by geographic proximity."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/#page","headline":"Proximity steering \u00b7 Cloudflare Load Balancing docs","description":"Route traffic to the nearest pool by geographic proximity.","url":"https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/
  schema: 1
---
<p><strong>Proximity steering</strong> routes visitors or internal services to the closest physical data center.</p>
<p>To use proximity steering on a load balancer, you first need to add GPS coordinates to each pool.</p>
<h2 id="when-to-add-proximity-steering">When to add proximity steering</h2>
<ul>
<li>For new pools, add GPS coordinates when you create a pool.</li>
<li>For existing pools, add GPS coordinates when <a href="/load-balancing/pools/create-pool/#edit-a-pool">managing pools</a> or in the <strong>Add Traffic steering</strong> step of <a href="/load-balancing/load-balancers/create-load-balancer/">creating a load balancer</a>.</li>
</ul>
<h2 id="how-to-add-proximity-steering">How to add proximity steering</h2>
<p>To add coordinates when creating or editing a pool:</p>
<ol>
<li>Click the <em>Configure coordinates for Proximity Steering</em> dropdown.</li>
<li>Enter the latitude and longitude or drag a marker on the map.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning:</h3>
@markup("md", "content/.markup/bodies/10450.md")
</aside>
