---
cp9:
  canonical: https://developers.cloudflare.com/network-interconnect/locations/
  description: Facilities offering Direct Cloudflare Network Interconnect for private connectivity to Cloudflare
  full_title: Direct CNI locations · Cloudflare Network Interconnect docs
  head_html: <title>Direct CNI locations · Cloudflare Network Interconnect docs</title><meta name="generator" content="Nift"><meta name="description" content="Facilities offering Direct Cloudflare Network Interconnect for private connectivity to Cloudflare"><link rel="canonical" href="https://developers.cloudflare.com/network-interconnect/locations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-interconnect/locations/index.md"><meta property="og:title" content="Direct CNI locations · Cloudflare Network Interconnect docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Facilities offering Direct Cloudflare Network Interconnect for private connectivity to Cloudflare"><meta property="og:url" content="https://developers.cloudflare.com/network-interconnect/locations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Interconnect"><meta name="algolia_product_filter" content="Network Interconnect"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Network Interconnect"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-interconnect/locations/#page","headline":"Direct CNI locations \u00b7 Cloudflare Network Interconnect docs","description":"Facilities offering Direct Cloudflare Network Interconnect for private connectivity to Cloudflare","url":"https://developers.cloudflare.com/network-interconnect/locations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network-interconnect/locations/
  schema: 1
---
<p>The following facilities offer <strong>Direct CNI</strong>, a dedicated physical connection between your network equipment and Cloudflare hardware in a shared data center.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="partner-cni-and-cloud-cni">Partner CNI and Cloud CNI</h3>
@markup("md", "content/.markup/bodies/693.md")
</aside>
<p>For public peering and best-effort interconnection at additional locations, refer to <a href="https://www.peeringdb.com/net/4224">Cloudflare on PeeringDB</a>.</p>
<h2 id="available-locations">Available locations</h2>
<p>The <a href="/network-interconnect/#dataplane">v1</a> and <a href="/network-interconnect/#dataplane">v2</a> columns show the Direct CNI dataplanes offered at each facility.</p>
<p>In this table, a metro has <em>device-level diversity</em> when at least two devices of the same dataplane provide paths to the rest of the Cloudflare network without a shared single point-of-failure device.</p>
<p><code>—</code> means the dataplane is not offered at this time.</p>
<h3 id="locations-in-diverse-metros">Locations in diverse metros</h3>
<p>Values show whether a dataplane is available through one or two connectivity devices in the site. Device-level redundancy can be achieved across multiple devices in different sites, if they are in the same metro. (Between metros, Cloudflare does not yet coordinate maintenances.)</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/698.md")
</div></div>
<h3 id="locations-in-non-diverse-metros">Locations in non-diverse metros</h3>
<p><code>✓</code> means that the dataplane is offered.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/703.md")
</div></div>
