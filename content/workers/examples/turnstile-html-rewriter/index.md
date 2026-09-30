---
cp9:
  canonical: https://developers.cloudflare.com/workers/examples/turnstile-html-rewriter/
  description: Inject [Turnstile](/turnstile/) implicitly into HTML elements using the HTMLRewriter runtime API.
  full_title: Turnstile with Workers · Cloudflare Workers docs
  head_html: <title>Turnstile with Workers · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Inject [Turnstile](/turnstile/) implicitly into HTML elements using the HTMLRewriter runtime API."><link rel="canonical" href="https://developers.cloudflare.com/workers/examples/turnstile-html-rewriter/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/examples/turnstile-html-rewriter/index.md"><meta property="og:title" content="Turnstile with Workers · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Inject [Turnstile](/turnstile/) implicitly into HTML elements using the HTMLRewriter runtime API."><meta property="og:url" content="https://developers.cloudflare.com/workers/examples/turnstile-html-rewriter/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="JavaScript,TypeScript,Python"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/examples/turnstile-html-rewriter/#page","headline":"Turnstile with Workers \u00b7 Cloudflare Workers docs","description":"Inject Turnstile implicitly into HTML elements using the HTMLRewriter runtime API.","url":"https://developers.cloudflare.com/workers/examples/turnstile-html-rewriter/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript","TypeScript","Python"]}</script>
  markdown: true
  noindex: false
  route: /workers/examples/turnstile-html-rewriter/
  schema: 1
---
<p class="article-summary">Inject [Turnstile](/turnstile/) implicitly into HTML elements using the HTMLRewriter runtime API.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16329.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16324.md")
</aside>
<section class="nb-tab-panel" role="tabpanel" data-nb-tabs-content data-nb-tab-label="JavaScript">
@markup("md", "content/.markup/bodies/16330.md")
</section>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="prevent-potential-errors-when-accessing-request-body">Prevent potential errors when accessing request.body</h3>
@markup("md", "content/.markup/bodies/16323.md")
</aside>
