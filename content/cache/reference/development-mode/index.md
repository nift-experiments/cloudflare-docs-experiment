---
cp9:
  canonical: https://developers.cloudflare.com/cache/reference/development-mode/
  description: Bypass the cache temporarily with Development Mode.
  full_title: Development Mode · Cloudflare Cache (CDN) docs
  head_html: <title>Development Mode · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Bypass the cache temporarily with Development Mode."><link rel="canonical" href="https://developers.cloudflare.com/cache/reference/development-mode/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/reference/development-mode/index.md"><meta property="og:title" content="Development Mode · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Bypass the cache temporarily with Development Mode."><meta property="og:url" content="https://developers.cloudflare.com/cache/reference/development-mode/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/reference/development-mode/#page","headline":"Development Mode \u00b7 Cloudflare Cache (CDN) docs","description":"Bypass the cache temporarily with Development Mode.","url":"https://developers.cloudflare.com/cache/reference/development-mode/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/reference/development-mode/
  schema: 1
---
<p>Development Mode temporarily suspends Cloudflare's edge caching and <a href="/images/polish/">Polish</a> features for three hours unless disabled beforehand. Development Mode allows customers to immediately observe changes to their <a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">cacheable content</a> like images, CSS, or JavaScript.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3799.md")
</aside>
<h2 id="enable-development-mode">Enable Development Mode</h2>
<p>Development Mode temporarily bypasses Cloudflare's cache and does not purge cached files. To instantly purge your Cloudflare cache, refer to <a href="/cache/how-to/purge-cache/">purge cache</a>.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configuration</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Toggle <strong>Development Mode</strong> to <strong>On</strong>.</li>
</ol>
