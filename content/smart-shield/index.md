---
cp9:
  canonical: https://developers.cloudflare.com/smart-shield/
  description: Use Smart Shield to protect your origin server, improve content availability, and reduce network latency.
  full_title: Overview · Cloudflare Smart Shield docs
  head_html: <title>Overview · Cloudflare Smart Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Smart Shield to protect your origin server, improve content availability, and reduce network latency."><link rel="canonical" href="https://developers.cloudflare.com/smart-shield/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/smart-shield/index.md"><meta property="og:title" content="Overview · Cloudflare Smart Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Smart Shield to protect your origin server, improve content availability, and reduce network latency."><meta property="og:url" content="https://developers.cloudflare.com/smart-shield/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Smart Shield"><meta name="algolia_product_filter" content="Smart Shield"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Smart Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/smart-shield/#page","headline":"Overview \u00b7 Cloudflare Smart Shield docs","description":"Use Smart Shield to protect your origin server, improve content availability, and reduce network latency.","url":"https://developers.cloudflare.com/smart-shield/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /smart-shield/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/346.md")
</div>
<p>Every request that reaches your origin server costs resources — bandwidth, compute, and connections. When traffic spikes or your content is requested from many locations simultaneously, your origin can become a bottleneck. Smart Shield is a bundle of origin protection and performance features that reduce the number of requests and connections between Cloudflare's network and your origin server.</p>
<p>Smart Shield includes <a href="/smart-shield/configuration/smart-tiered-cache/">Smart Tiered Cache</a>, which organizes Cloudflare data centers into upper-tier and lower-tier groups so that only upper-tier data centers contact your origin for uncached content. Combined with <a href="/smart-shield/concepts/connection-reuse/">connection reuse</a>, which packages multiple requests into a single connection to your origin, Smart Shield reduces both the volume of origin requests and the number of open connections.</p>
<p>Depending on your <a href="/smart-shield/get-started/#packages-and-availability">package tier</a>, Smart Shield can also include:</p>
<ul>
<li><a href="/smart-shield/configuration/argo/">Argo Smart Routing</a> — routes traffic through the fastest network paths to reduce latency.</li>
<li><a href="/smart-shield/configuration/regional-tiered-cache/">Regional Tiered Cache</a> — adds a regional cache layer between lower-tier and upper-tier data centers for geographic data locality (Enterprise plans, or Smart Shield Advanced).</li>
<li><a href="/smart-shield/configuration/cache-reserve/">Cache Reserve</a> — persistent cache storage that reduces cache misses for infrequently accessed content.</li>
<li><a href="/smart-shield/configuration/health-checks/">Health Checks</a> — monitors your origin server availability (Pro plans and above).</li>
<li><a href="/smart-shield/configuration/dedicated-egress-ips/">Dedicated CDN Egress IPs</a> — reserved IP addresses for origin allowlisting (Enterprise).</li>
</ul>
<p>For a visual overview of how these features work together, refer to the <a href="/smart-shield/concepts/network-diagram/">network diagram</a>.</p>
<p>Learn how to <a href="/smart-shield/get-started/">get started</a>.</p>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/347.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/348.md")
</div>
