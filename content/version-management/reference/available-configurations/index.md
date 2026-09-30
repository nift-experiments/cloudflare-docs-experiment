---
cp9:
  canonical: https://developers.cloudflare.com/version-management/reference/available-configurations/
  description: View which zone configurations support versioning.
  full_title: Available configurations · Cloudflare Version Management docs
  head_html: <title>Available configurations · Cloudflare Version Management docs</title><meta name="generator" content="Nift"><meta name="description" content="View which zone configurations support versioning."><link rel="canonical" href="https://developers.cloudflare.com/version-management/reference/available-configurations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/version-management/reference/available-configurations/index.md"><meta property="og:title" content="Available configurations · Cloudflare Version Management docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View which zone configurations support versioning."><meta property="og:url" content="https://developers.cloudflare.com/version-management/reference/available-configurations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Version Management"><meta name="algolia_product_filter" content="Version Management"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Version Management"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/version-management/reference/available-configurations/#page","headline":"Available configurations \u00b7 Cloudflare Version Management docs","description":"View which zone configurations support versioning.","url":"https://developers.cloudflare.com/version-management/reference/available-configurations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /version-management/reference/available-configurations/
  schema: 1
---
<p>When you use Version Management, you can edit various configurations, such as <a href="/waf/custom-rules/">WAF custom rules</a> and <a href="/cache/">Cache</a>.</p>
<p>Generally, you are allowed to edit all zone-level configurations except for the following:</p>
<ul>
<li><a href="/dns/">DNS</a></li>
<li><a href="/spectrum/">Spectrum</a></li>
<li>Traffic (<a href="/load-balancing/">Load Balancing</a>, <a href="/waiting-room/">Waiting Rooms</a>, Health Checks, and more)</li>
<li><a href="/cloudflare-one/">Zero Trust</a> and Access policies</li>
<li><a href="/ssl/edge-certificates/">SSL certificates</a> (though you can test these with a separate <a href="/ssl/edge-certificates/staging-environment/">staging certificates</a> feature)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15287.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>Version Management does not currently support or have limited support for the following products or features:</p>
<details class="nb-details"><summary>API Shield</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15288.md")
</div></details>
<details class="nb-details"><summary>Authenticated Origin Pull</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15289.md")
</div></details>
<details class="nb-details"><summary>Cache</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15290.md")
</div></details>
<details class="nb-details"><summary>Cache Rules when used with Cloudflare Images</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15291.md")
</div></details>
<details class="nb-details"><summary>Workers Cache API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15292.md")
</div></details>
<details class="nb-details"><summary>China Network</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15293.md")
</div></details>
<details class="nb-details"><summary>Cloudflare API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15294.md")
</div></details>
<details class="nb-details"><summary>Domain-scoped Roles</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15295.md")
</div></details>
<details class="nb-details"><summary>Image Transformations</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15296.md")
</div></details>
<details class="nb-details"><summary>Network Error Logging</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15297.md")
</div></details>
<details class="nb-details"><summary>Client-side security</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15298.md")
</div></details>
<details class="nb-details"><summary>Rules</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15299.md")
</div></details>
<details class="nb-details"><summary>Security Insights</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15300.md")
</div></details>
<details class="nb-details"><summary>Terraform</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15301.md")
</div></details>
<details class="nb-details"><summary>WAF Attack Score</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15302.md")
</div></details>
<details class="nb-details"><summary>Waiting Room</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15303.md")
</div></details>
<details class="nb-details"><summary>Wrangler</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15304.md")
</div></details>
