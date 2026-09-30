---
cp9:
  canonical: https://developers.cloudflare.com/speed/optimization/images/mirage/
  description: Lazy-load images and reduce bandwidth on mobile connections.
  full_title: Cloudflare Mirage (deprecated) · Cloudflare Speed docs
  head_html: <title>Cloudflare Mirage (deprecated) · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Lazy-load images and reduce bandwidth on mobile connections."><link rel="canonical" href="https://developers.cloudflare.com/speed/optimization/images/mirage/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/optimization/images/mirage/index.md"><meta property="og:title" content="Cloudflare Mirage (deprecated) · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Lazy-load images and reduce bandwidth on mobile connections."><meta property="og:url" content="https://developers.cloudflare.com/speed/optimization/images/mirage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Speed"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/speed/optimization/images/mirage/#page","headline":"Cloudflare Mirage (deprecated) \u00b7 Cloudflare Speed docs","description":"Lazy-load images and reduce bandwidth on mobile connections.","url":"https://developers.cloudflare.com/speed/optimization/images/mirage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /speed/optimization/images/mirage/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/13925.md")
</aside>
<h2 id="what-was-mirage">What was Mirage?</h2>
<p>Cloudflare Mirage was a mobile image optimization feature that reduced bandwidth usage and accelerated image loading on slow mobile connections and HTTP/1.</p>
<p>Mirage worked by:</p>
<ul>
<li>Replacing images with low-resolution thumbnails bundled together into one file.</li>
<li>Acting as a lazy loader, deferring loading of higher-resolution images until they become visible.</li>
</ul>
<h2 id="why-was-it-deprecated">Why was it deprecated?</h2>
<p>Modern web standards and browser capabilities have evolved to provide native support for many of Mirage's features:</p>
<ul>
<li>Native lazy loading with the <code>loading=&quot;lazy&quot;</code> HTML attribute.</li>
<li>Responsive images using <code>srcset</code> and <code>&lt;picture&gt;</code> elements.</li>
<li>HTTP/2 and HTTP/3 providing better performance.</li>
<li>Improved mobile networks reducing the need for aggressive optimization.</li>
</ul>
<h2 id="migration-path">Migration path</h2>
<p>Instead of Mirage, use:</p>
<ul>
<li><strong><a href="/images/polish/">Polish</a></strong> - Seamlessly optimizes images for all browsers, not only mobile, and keeps images at full resolution.</li>
<li><strong><a href="/images/optimization/transformations/overview/">Image Resizing</a></strong> - Combined with <code>loading=&quot;lazy&quot;</code> and <code>srcset</code> HTML attributes, provides modern responsive image delivery.</li>
<li><strong><a href="/images/tutorials/optimize-mobile-viewing/">Lazy loading guide</a></strong> - Learn how to implement native lazy loading.</li>
<li><strong><a href="/images/optimization/make-responsive-images/">Responsive images guide</a></strong> - Create images that adapt to different devices.</li>
</ul>
