---
cp9:
  canonical: https://developers.cloudflare.com/dns/internal-dns/get-started/
  description: Set up Internal DNS for private name resolution.
  full_title: Get started · Cloudflare DNS docs
  head_html: <title>Get started · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Internal DNS for private name resolution."><link rel="canonical" href="https://developers.cloudflare.com/dns/internal-dns/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/internal-dns/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Internal DNS for private name resolution."><meta property="og:url" content="https://developers.cloudflare.com/dns/internal-dns/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="DNS"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/internal-dns/get-started/#page","headline":"Get started \u00b7 Cloudflare DNS docs","description":"Set up Internal DNS for private name resolution.","url":"https://developers.cloudflare.com/dns/internal-dns/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /dns/internal-dns/get-started/
  schema: 1
---
<p>Follow this guide to get started with Internal DNS.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>Make sure you have an Enterprise account with access to <a href="/cloudflare-one/traffic-policies/resolver-policies/">Gateway resolver policies</a> and <a href="/dns/internal-dns/">Internal DNS</a>.</li>
<li>Consider the different ways in which you can <a href="/dns/internal-dns/connectivity/">connect to Gateway resolver</a>.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7633.md")
</aside>
<ul>
<li>If you will be using an API token for authentication, make sure you have the following permissions:</li>
</ul>
<details class="nb-details"><summary>API token configuration</summary><div class="nb-details-body">
@input("content/.markup/bodies/7635.md")
</div></details>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="about-authentication">About authentication</h3>
@markup("md", "content/.markup/bodies/7632.md")
</aside>
<h2 id="1-set-up-your-internal-dns-zone"><ol>
<li>Set up your internal DNS zone</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7641.md")
</div></div>
<h3 id="optional-reference-a-zone-from-another-zone">(Optional) Reference a zone from another zone</h3>
<p>During an <a href="/dns/internal-dns/#architecture-overview">internal DNS query resolution</a>, if no internal record is found within a matching internal zone, Cloudflare will check if the matching internal zone is referencing another internal zone. Successive references can be followed with a maximum of five references in a chain.</p>
<p>For details, refer to <a href="/dns/internal-dns/internal-zones/reference-zones/">reference zones</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7645.md")
</div></div>
<h2 id="2-link-your-internal-zone-to-a-view"><ol start="2">
<li>Link your internal zone to a view</li>
</ol></h2>
<p>Since the resolver policy will require a <a href="/dns/internal-dns/dns-views/">DNS view</a>, you must have at least one view to be able to route requests to internal zones.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7650.md")
</div></div>
<h2 id="3-configure-gateway-policies"><ol start="3">
<li>Configure Gateway policies</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7630.md")
</aside>
<p>Besides selecting an internal DNS view when setting up your resolver policies, you can also enable the <strong>fallback through public DNS</strong> option.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7653.md")
</div></div>
<p>Once you add the Gateway resolver policy, it will be listed in the respective internal view under <strong>Resolver policies referencing this view</strong>.</p>
<h2 id="manage-with-terraform">Manage with Terraform</h2>
<p>You can also manage Internal DNS resources with the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a>. The patterns are identical to public DNS zones — the only difference is setting <code>type = &quot;internal&quot;</code> on the <code>cloudflare_zone</code> resource.</p>
<p>Use a zone-scoped API token for day-to-day management and an account-level token for creating new zones. If your token is scoped to specific zones, remember to update it when you add new internal zones. For a complete working example, refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider documentation</a>.</p>
