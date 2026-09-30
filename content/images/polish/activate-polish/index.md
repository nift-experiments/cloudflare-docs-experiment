---
cp9:
  canonical: https://developers.cloudflare.com/images/polish/activate-polish/
  description: Turn on Cloudflare Polish in the dashboard to automatically optimize images with lossy or lossless compression.
  full_title: Activate Polish · Cloudflare Images docs
  head_html: <title>Activate Polish · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Turn on Cloudflare Polish in the dashboard to automatically optimize images with lossy or lossless compression."><link rel="canonical" href="https://developers.cloudflare.com/images/polish/activate-polish/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/polish/activate-polish/index.md"><meta property="og:title" content="Activate Polish · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Turn on Cloudflare Polish in the dashboard to automatically optimize images with lossy or lossless compression."><meta property="og:url" content="https://developers.cloudflare.com/images/polish/activate-polish/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/polish/activate-polish/#page","headline":"Activate Polish \u00b7 Cloudflare Images docs","description":"Turn on Cloudflare Polish in the dashboard to automatically optimize images with lossy or lossless compression.","url":"https://developers.cloudflare.com/images/polish/activate-polish/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/polish/activate-polish/
  schema: 1
---
<p>Images in the <a href="/cache/how-to/purge-cache/">cache must be purged</a> or expired before seeing any changes in Polish settings.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/9357.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account home</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the domain where you want to activate Polish.</li>
<li>Select <strong>Speed</strong> &gt; <strong>Settings</strong> &gt; <strong>Image Optimization</strong>.</li>
<li>Under <strong>Polish</strong>, select <em>Lossy</em> or <em>Lossless</em> from the drop-down menu. <a href="/images/polish/compression/#lossy"><em>Lossy</em></a> gives greater file size savings.</li>
<li>(Optional) Select <strong>WebP</strong>. Enable this option if you want to further optimize PNG and JPEG images stored in the origin server, and serve them as WebP files to browsers that support this format.</li>
</ol>
<p>To ensure WebP is not served from cache to a browser without WebP support, disable any WebP conversion utilities at your origin web server when using Polish.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9356.md")
</aside>
