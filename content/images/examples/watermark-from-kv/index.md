---
cp9:
  canonical: https://developers.cloudflare.com/images/examples/watermark-from-kv/
  description: Draw a watermark from KV on an image from R2
  full_title: Watermarks · Cloudflare Images docs
  head_html: <title>Watermarks · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Draw a watermark from KV on an image from R2"><link rel="canonical" href="https://developers.cloudflare.com/images/examples/watermark-from-kv/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/examples/watermark-from-kv/index.md"><meta property="og:title" content="Watermarks · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Draw a watermark from KV on an image from R2"><meta property="og:url" content="https://developers.cloudflare.com/images/examples/watermark-from-kv/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Cloudflare Images,R2,KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/examples/watermark-from-kv/#page","headline":"Watermarks \u00b7 Cloudflare Images docs","description":"Draw a watermark from KV on an image from R2","url":"https://developers.cloudflare.com/images/examples/watermark-from-kv/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/examples/watermark-from-kv/
  schema: 1
---
<p class="article-summary">Draw a watermark from KV on an image from R2</p>
<p>Enable <a href="/workers/cache/">Workers Cache</a> so repeat requests for the same watermarked image are served from cache without re-running the Worker or re-transforming the image:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9454.md")
</div>
<p>Then set <code>Cache-Control</code> headers on your response to control the cache lifetime:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9455.md")
</div>
