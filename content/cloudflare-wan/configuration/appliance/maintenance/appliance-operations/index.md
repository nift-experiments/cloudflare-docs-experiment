---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/
  description: Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard or via API.
  full_title: Appliance operations · Cloudflare WAN docs
  head_html: <title>Appliance operations · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard or via API."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/index.md"><meta property="og:title" content="Appliance operations · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard or via API."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/#page","headline":"Appliance operations \u00b7 Cloudflare WAN docs","description":"Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard or via API.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/appliance/maintenance/appliance-operations/
  schema: 1
---
<hr />
<hr />
<p>You can restart, reboot, or shut down a Cloudflare One Appliance (formerly Magic WAN Connector) from the dashboard or via API. Operations are asynchronous — the appliance executes them the next time it checks in.</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Effect</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Restart</strong></td>
<td>Restart managed services. Purges temporary and (optionally) persistent state.</td>
</tr>
<tr>
<td><strong>Reboot</strong></td>
<td>Power cycle the appliance. Optionally, purge persistent state. Re-applies configuration starting from scratch.</td>
</tr>
<tr>
<td><strong>Shutdown</strong></td>
<td>Power off the appliance. Optionally, purge persistent state. The machine will be offline until manually powered on again.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6993.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6997.md")
</div></div>
