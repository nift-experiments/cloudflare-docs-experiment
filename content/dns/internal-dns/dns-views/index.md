---
cp9:
  canonical: https://developers.cloudflare.com/dns/internal-dns/dns-views/
  description: Manage DNS views to return different responses by network.
  full_title: Manage DNS views · Cloudflare DNS docs
  head_html: <title>Manage DNS views · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage DNS views to return different responses by network."><link rel="canonical" href="https://developers.cloudflare.com/dns/internal-dns/dns-views/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/internal-dns/dns-views/index.md"><meta property="og:title" content="Manage DNS views · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage DNS views to return different responses by network."><meta property="og:url" content="https://developers.cloudflare.com/dns/internal-dns/dns-views/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/internal-dns/dns-views/#page","headline":"Manage DNS views \u00b7 Cloudflare DNS docs","description":"Manage DNS views to return different responses by network.","url":"https://developers.cloudflare.com/dns/internal-dns/dns-views/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /dns/internal-dns/dns-views/
  schema: 1
---
<p>Internal DNS views are logical groupings of <a href="/dns/internal-dns/internal-zones/">internal DNS zones</a>. As explained in the <a href="/dns/internal-dns/#architecture-overview">architecture overview</a>, DNS views are referenced by <a href="/cloudflare-one/traffic-policies/resolver-policies/">Gateway resolver policies</a> to define how a specific query should be resolved.</p>
<p>Refer to the sections below for details on how to manage your DNS views, or consider the <a href="/dns/internal-dns/get-started/">get started</a> for a complete workflow.</p>
<h2 id="configuration-conditions">Configuration conditions</h2>
<p>When setting up DNS views, observe the following conditions:</p>
<ul>
<li>DNS views can be empty, with no <a href="/dns/internal-dns/internal-zones/">internal zones</a> linked to them.</li>
<li>A DNS view cannot contain public DNS zones.<sup>1</sup></li>
<li>Each internal DNS zone name must be unique within a given DNS view.</li>
<li>Each DNS view name must be unique within a given Cloudflare account.</li>
</ul>
<p><sup>1</sup> DNS zones that contain public DNS records and are accessible by public resolvers.</p>
<h2 id="create-a-view">Create a view</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7657.md")
</div></div>
<h2 id="delete-a-view">Delete a view</h2>
<p>DNS views can be deleted even if they still have internal zones linked to them. The internal DNS zones will continue to exist but will be unlinked once the view is deleted.</p>
<p>It is also possible to delete a DNS view that is being referenced by a Gateway resolver policy. In this case, queries matching the policy will return SERVFAIL.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7660.md")
</div></div>
<h2 id="other-api-actions">Other API actions</h2>
<ul>
<li><a href="/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/edit/">Update a DNS view</a> (<code>PATCH</code>)</li>
<li><a href="/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/get/">Get view details</a> (<code>GET</code>)</li>
<li><a href="/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/list/">List DNS views</a> (<code>GET</code>)</li>
</ul>
