---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/
  description: Migrate caching Page Rules to Cache Rules.
  full_title: Migration from Page Rules · Cloudflare Cache (CDN) docs
  head_html: <title>Migration from Page Rules · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Migrate caching Page Rules to Cache Rules."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/index.md"><meta property="og:title" content="Migration from Page Rules · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Migrate caching Page Rules to Cache Rules."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cache / CDN"><meta name="pcx_tags" content="Migration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/#page","headline":"Migration from Page Rules \u00b7 Cloudflare Cache (CDN) docs","description":"Migrate caching Page Rules to Cache Rules.","url":"https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Migration"]}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/cache-rules/page-rules-migration/
  schema: 1
---
<p>If you are migrating from Page Rules, there is a behavior change between Page Rules and Cache Rules.</p>
<p>When you create a new Cache Rule and select <strong>Eligible for cache</strong>, the Cache Everything feature is enabled by default. With Page Rules, you had to specifically enable the Cache Everything option.</p>
<p>To maintain the same behavior you had with Page Rules (that is, not enabling Cache Everything), you need to create these two specific rules in this order before creating any additional rules.</p>
<p>Multiple matching cache rules can be combined and applied to the same request. After rule 1 matches, Cloudflare will keep evaluating other cache rules checking for matches. For more information, refer to <a href="/cache/how-to/cache-rules/order/">Order and priority</a>.</p>
<h2 id="rule-1">Rule 1</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3902.md")
</div></div>
<h2 id="rule-2">Rule 2</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3905.md")
</div></div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3899.md")
</aside>
