---
cp9:
  canonical: https://developers.cloudflare.com/bots/additional-configurations/static-resources/
  description: Extend bot protection to static resources like images, CSS, and JavaScript files.
  full_title: Static resource protection · Cloudflare bot solutions docs
  head_html: <title>Static resource protection · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Extend bot protection to static resources like images, CSS, and JavaScript files."><link rel="canonical" href="https://developers.cloudflare.com/bots/additional-configurations/static-resources/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/additional-configurations/static-resources/index.md"><meta property="og:title" content="Static resource protection · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Extend bot protection to static resources like images, CSS, and JavaScript files."><meta property="og:url" content="https://developers.cloudflare.com/bots/additional-configurations/static-resources/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/additional-configurations/static-resources/#page","headline":"Static resource protection \u00b7 Cloudflare bot solutions docs","description":"Extend bot protection to static resources like images, CSS, and JavaScript files.","url":"https://developers.cloudflare.com/bots/additional-configurations/static-resources/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /bots/additional-configurations/static-resources/
  schema: 1
---
<p>Pro, Business, and Enterprise customers can use Cloudflare's bot solutions to protect their <span class="nb-glossary-tooltip" title="static content">static resources</span> from bots.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/3525.md")
</aside>
<h2 id="super-bot-fight-mode">Super Bot Fight Mode</h2>
<p>To enable this feature as a Pro or Business customer or an Enterprise customer without Bot Management:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3527.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3524.md")
</aside>
<h2 id="bot-management-for-enterprise">Bot Management for Enterprise</h2>
<p>Static resources are protected by default when you create <a href="/waf/custom-rules/">custom rules</a> using <code>cf.bot_management.score</code>.</p>
<p>To exclude static resources, you would need to include <code>not (cf.bot_management.static_resource)</code> as part of your custom rule.</p>
<h2 id="which-files-are-protected">Which files are protected?</h2>
<p>Static resources are files with the following extensions:</p>
<p><code>ico|jpg|png|jpeg|gif|css|js|tif|tiff|bmp|pict|webp|svg|svgz|class|jar|txt|csv|doc|docx|xls|xlsx|pdf|ps|pls|ppt|pptx|ttf|otf|woff|woff2|eot|eps|ejs|swf|torrent|midi|mid|m3u8|m4a|mp3|ogg|ts</code></p>
<p>Additionally, the <code>/.well-known/</code> URL path and all elements in it are considered a static resource, regardless of the file extension.</p>
