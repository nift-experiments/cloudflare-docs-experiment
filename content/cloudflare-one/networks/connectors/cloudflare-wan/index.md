---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/
  description: Overview of Cloudflare WAN in Zero Trust networking.
  full_title: Overview · Cloudflare One docs
  head_html: <title>Overview · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Overview of Cloudflare WAN in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/index.md"><meta property="og:title" content="Overview · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Overview of Cloudflare WAN in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/#page","headline":"Overview \u00b7 Cloudflare One docs","description":"Overview of Cloudflare WAN in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/5135.md")
</div>
<div class="nb-plan">
<p>Enterprise-only</p>
</div>
<p>Cloudflare WAN (formerly Magic WAN) connects your data centers, offices, and cloud resources through Cloudflare's global network. Instead of backhauling traffic through a central data center or maintaining dedicated MPLS circuits at every site, your traffic routes through the nearest Cloudflare data center where security policies apply inline.</p>
<p>Cloudflare WAN provides secure, performant <a href="https://www.cloudflare.com/learning/network-layer/what-is-routing/">routing</a> for your entire corporate network. <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> integrates with Cloudflare WAN, enabling you to enforce network firewall policies at Cloudflare's global network, across traffic from any entity within your network.</p>
<p>You connect your sites to Cloudflare through <span class="nb-glossary-tooltip" title="on-ramp">on-ramps</span> — tunnels or direct connections from your network to Cloudflare. Cloudflare WAN supports any device that uses <span class="nb-glossary-tooltip" title="anycast">anycast</span> <span class="nb-glossary-tooltip" title="GRE tunnel">GRE</span> or <span class="nb-glossary-tooltip" title="IPsec tunnel">IPsec</span> tunnels. Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/on-ramps/">On-ramps</a> for a full list of supported on-ramps.</p>
<p>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/wan-transformation/">WAN transformation</a> to compare approaches and plan your migration, or go straight to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/get-started/">get started</a>.</p>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/86f22d1f760b77cdc349f89b25b63c3e/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2Fe71b5fcd-6de8-4ec5-28b2-4667c34c3900%2Fpublic" title="SASE - Connect and secure from any network to anywhere" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/5140.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/5141.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/5142.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/5143.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/5144.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/5145.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/5146.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/5147.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/5148.md")
</div>
<hr />
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/5150.md")
</div>
