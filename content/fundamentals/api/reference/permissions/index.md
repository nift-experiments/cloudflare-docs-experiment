---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/api/reference/permissions/
  description: Review available Cloudflare API token permissions for user, account, and zone resources.
  full_title: API token permissions · Cloudflare Fundamentals docs
  head_html: <title>API token permissions · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Review available Cloudflare API token permissions for user, account, and zone resources."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/index.md"><meta property="og:title" content="API token permissions · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review available Cloudflare API token permissions for user, account, and zone resources."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/api/reference/permissions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,API documentation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/api/reference/permissions/#page","headline":"API token permissions \u00b7 Cloudflare Fundamentals docs","description":"Review available Cloudflare API token permissions for user, account, and zone resources.","url":"https://developers.cloudflare.com/fundamentals/api/reference/permissions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/api/reference/permissions/
  schema: 1
---
<p>Permissions are segmented into three categories based on resource:</p>
<ul>
<li>Zone permissions</li>
<li>Account permissions</li>
<li>User permissions</li>
</ul>
<p>Each category contains permission groups related to those resources. DNS permissions belong to the Zone category, while Billing permissions belong to the Account category. Below is a list of the available token permissions.</p>
<p>To obtain an updated list of token permissions, including the permission ID and the scope of each permission, use the <a href="/api/resources/user/subresources/tokens/subresources/permission_groups/methods/list/">List permission groups</a> endpoint.</p>
<h2 id="user-permissions">User permissions</h2>
<p>The applicable scope of user permissions is <code>com.cloudflare.api.user</code>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8968.md")
</div></div>
<h2 id="account-permissions">Account permissions</h2>
<p>The applicable scope of account permissions is <code>com.cloudflare.api.account</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8965.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8971.md")
</div></div>
<h2 id="zone-permissions">Zone permissions</h2>
<p>The applicable scope of zone permissions is <code>com.cloudflare.api.account.zone</code>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8974.md")
</div></div>
