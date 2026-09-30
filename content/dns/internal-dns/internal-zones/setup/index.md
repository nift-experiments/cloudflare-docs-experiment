---
cp9:
  canonical: https://developers.cloudflare.com/dns/internal-dns/internal-zones/setup/
  description: Understand how to set up and manage internal DNS zones with Cloudflare. Explore configuration conditions, zone creation, and available API endpoints.
  full_title: Manage internal zones · Cloudflare DNS docs
  head_html: <title>Manage internal zones · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand how to set up and manage internal DNS zones with Cloudflare. Explore configuration conditions, zone creation, and available API endpoints."><link rel="canonical" href="https://developers.cloudflare.com/dns/internal-dns/internal-zones/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/internal-dns/internal-zones/setup/index.md"><meta property="og:title" content="Manage internal zones · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand how to set up and manage internal DNS zones with Cloudflare. Explore configuration conditions, zone creation, and available API endpoints."><meta property="og:url" content="https://developers.cloudflare.com/dns/internal-dns/internal-zones/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/internal-dns/internal-zones/setup/#page","headline":"Manage internal zones \u00b7 Cloudflare DNS docs","description":"Understand how to set up and manage internal DNS zones with Cloudflare. Explore configuration conditions, zone creation, and available API endpoints.","url":"https://developers.cloudflare.com/dns/internal-dns/internal-zones/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /dns/internal-dns/internal-zones/setup/
  schema: 1
---
<p>Refer to the following sections to learn how to manage your <a href="/dns/internal-dns/internal-zones/">internal DNS zones</a>.</p>
<h2 id="configuration-conditions">Configuration conditions</h2>
<p>When setting up internal zones, observe the following conditions:</p>
<ul>
<li>Internal zones can contain the same <a href="/dns/manage-dns-records/reference/dns-record-types/">DNS record types</a> that Cloudflare supports for public zones.</li>
<li>An internal zone can have the same name as a public zone in the same account.</li>
<li>Each internal zone can be linked to multiple <a href="/dns/internal-dns/dns-views/">views</a>.<sup>1</sup></li>
<li>There can be several internal zones with the same name in one account. However, two internal zones with the same name cannot be linked to the same view.</li>
<li>Internal zones are not subject to any top-level domain (TLD) restrictions. This means that an internal zone can be created if its TLD is not registered publicly (for example, <code>xyz.local</code>), if it is created on the TLD itself (<code>local</code>), or even if on the root (<code>.</code>).</li>
</ul>
<p><sup>1</sup> Logical groupings of internal DNS zones that are referenced by Gateway resolver policies to define how a specific query should be resolved.</p>
<h2 id="create-an-internal-zone">Create an internal zone</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7753.md")
</div></div>
<h2 id="other-api-actions">Other API actions</h2>
<p>The API endpoints to manage internal zones are the same as for managing public zones. The main difference is that the zone type must be set to <code>internal</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7748.md")
</aside>
<p>Refer to the following API documentation for details:</p>
<ul>
<li><a href="/api/resources/zones/methods/edit/">Update an internal zone</a> (<code>PATCH</code>)</li>
<li><a href="/api/resources/zones/methods/get/">Get internal zone details</a> (<code>GET</code>)</li>
<li><a href="/api/resources/zones/methods/list/">List internal zones</a> (<code>GET</code>)</li>
<li><a href="/api/resources/zones/methods/delete/">Delete an internal zone</a> (<code>DELETE</code>)</li>
</ul>
