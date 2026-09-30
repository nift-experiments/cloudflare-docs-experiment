---
cp9:
  canonical: https://developers.cloudflare.com/automatic-platform-optimization/reference/page-rule-integration/
  description: Page Rules that control APO caching behavior for specific URL patterns.
  full_title: Page Rule integration with APO · Cloudflare Automatic Platform Optimization docs
  head_html: <title>Page Rule integration with APO · Cloudflare Automatic Platform Optimization docs</title><meta name="generator" content="Nift"><meta name="description" content="Page Rules that control APO caching behavior for specific URL patterns."><link rel="canonical" href="https://developers.cloudflare.com/automatic-platform-optimization/reference/page-rule-integration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/automatic-platform-optimization/reference/page-rule-integration/index.md"><meta property="og:title" content="Page Rule integration with APO · Cloudflare Automatic Platform Optimization docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Page Rules that control APO caching behavior for specific URL patterns."><meta property="og:url" content="https://developers.cloudflare.com/automatic-platform-optimization/reference/page-rule-integration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Automatic Platform Optimization"><meta name="algolia_product_filter" content="Automatic Platform Optimization"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Automatic Platform Optimization"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/automatic-platform-optimization/reference/page-rule-integration/#page","headline":"Page Rule integration with APO \u00b7 Cloudflare Automatic Platform Optimization docs","description":"Page Rules that control APO caching behavior for specific URL patterns.","url":"https://developers.cloudflare.com/automatic-platform-optimization/reference/page-rule-integration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /automatic-platform-optimization/reference/page-rule-integration/
  schema: 1
---
<p>The following Page Rules can control APO. Any changes to caching via Page Rules require purging the cache for the changes to take effect.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3342.md")
</aside>
<ul>
<li>
<p><strong>Cache Level: Bypass</strong> — APO bypasses pages with response header <code>cf-apo-via: origin,page-rules</code></p>
</li>
<li>
<p><strong>Cache Level: Ignore Query String</strong> — APO ignores all query strings when serving from Cache.</p>
</li>
<li>
<p><strong>Cache Level: Cache Everything</strong> — APO caches pages with all query strings.</p>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3341.md")
</aside>
<ul>
<li>
<p><strong>Bypass Cache on Cookie (Business and Enterprise plans only)</strong> — APO applies custom bypass cookies in addition to the default list.</p>
</li>
<li>
<p><strong>Edge Cache TTL</strong> — APO applies custom Edge TTL instead of 30 days. This page rule is helpful for pages that can generate CAPTCHAs or nonces.</p>
</li>
<li>
<p><strong>Browser Cache TTL</strong> — APO applies custom Browser TTL.</p>
</li>
<li>
<p><code>CDN-Cache-Control</code> and <code>Cloudflare-CDN-Cache-Control</code> – Enables users to have detailed control over cache TTLs without using a page rule. For more information on the <code>CDN-Cache-Control</code> and <code>Cloudflare-CDN-Cache-Control</code> headers, refer to <a href="/cache/concepts/cache-control/">CDN-Cache-Control</a>.</p>
</li>
</ul>
