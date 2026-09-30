---
cp9:
  canonical: https://developers.cloudflare.com/dns/internal-dns/internal-zones/reference-zones/
  description: Learn about reference zones. Cloudflare Internal DNS allows zones to reference others for query resolution when no direct record is found.
  full_title: Reference zones · Cloudflare DNS docs
  head_html: <title>Reference zones · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about reference zones. Cloudflare Internal DNS allows zones to reference others for query resolution when no direct record is found."><link rel="canonical" href="https://developers.cloudflare.com/dns/internal-dns/internal-zones/reference-zones/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/internal-dns/internal-zones/reference-zones/index.md"><meta property="og:title" content="Reference zones · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about reference zones. Cloudflare Internal DNS allows zones to reference others for query resolution when no direct record is found."><meta property="og:url" content="https://developers.cloudflare.com/dns/internal-dns/internal-zones/reference-zones/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/internal-dns/internal-zones/reference-zones/#page","headline":"Reference zones \u00b7 Cloudflare DNS docs","description":"Learn about reference zones. Cloudflare Internal DNS allows zones to reference others for query resolution when no direct record is found.","url":"https://developers.cloudflare.com/dns/internal-dns/internal-zones/reference-zones/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /dns/internal-dns/internal-zones/reference-zones/
  schema: 1
---
<p>During an <a href="/dns/internal-dns/#architecture-overview">internal DNS query resolution</a>, if no internal record is found within a matching internal zone, Cloudflare will check if the matching internal zone is referencing another internal zone. Successive references can be followed with a maximum of five references in a chain.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7755.md")
</aside>
<h2 id="configuration-conditions">Configuration conditions</h2>
<ul>
<li>Each internal zone can only reference one other zone.</li>
<li>The same zone can be referenced by multiple internal zones.</li>
<li>Public zones cannot be used as reference zones.</li>
<li>Reference zones do not have to be linked to the same <a href="/dns/internal-dns/dns-views/">DNS view</a> as the zone referencing them. They may also not be linked to any view at all.</li>
</ul>
<h2 id="set-up">Set up</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7759.md")
</div></div>
