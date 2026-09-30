---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/
  description: New updates and improvements at Cloudflare.
  full_title: 'New in Images: text rasterization and updates to the binding · Changelog'
  head_html: '<title>New in Images: text rasterization and updates to the binding · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New in Images: text rasterization and updates to the binding · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/#page","headline":"New in Images: text rasterization and updates to the binding \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>'
  markdown: false
  noindex: false
  route: /changelog/post/2026-09-02-images-binding-updates/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 2, 2026</time><h2 id="post-title">New in Images: text rasterization and updates to the binding</h2>
<div class="changelog-badges"><span>images</span></div><div class="changelog-body"><p>We've added more ways to manage and manipulate images with the <a href="/images/optimization/binding/">Images binding</a>. Here's what's new:</p>
<p><strong>Render text into an image.</strong> Output a string of text into its own image or draw it over another image.</p>
<ul>
<li>Use the <a href="/images/optimization/binding/#textcontent-options"><code>.text()</code></a> method to rasterize text with the Images binding.</li>
<li>Style content using the <code>font</code>, <code>size</code>, and <code>color</code> options.</li>
<li>The <a href="/images/optimization/draw-overlays/#draw-with-cfimage"><code>draw</code></a> array in <code>cf.image</code> now accepts a <code>text</code> key.</li>
</ul>
<p><strong>Manage hosted images without an API token.</strong></p>
<ul>
<li><strong>Metadata filtering:</strong> Pass <code>filter.metadata</code> to <a href="/images/storage/binding/#listoptions"><code>.list()</code></a> to return images by custom metadata. Match a bounded range by setting two operators in one condition, for example, <code>priority: { gte: 2, lte: 5 }</code>.</li>
<li><strong>Server-side signing:</strong> Get a signed URL for a private image with <a href="/images/storage/binding/#imageimageidsignedurloptions"><code>.signedUrl()</code></a>.</li>
<li><strong>User uploads:</strong> Create a Direct Creator Upload link with <a href="/images/storage/binding/#createdirectuploadoptions"><code>.createDirectUpload()</code></a> so that a client can upload an image to your storage.</li>
</ul>
<p><strong>Set headers in a single call.</strong></p>
<ul>
<li>Pass a <code>headers</code> option to <a href="/images/optimization/binding/#responseoptions"><code>.response()</code></a> to set headers without rebuilding the <code>Response</code>.</li>
<li><code>Content-Type</code> is always taken from the optimized image and can't be overridden by a specified header.</li>
<li>Set <code>Cache-Control</code> with <a href="/workers/cache/">Workers Cache</a> to cache your optimized image at the edge.</li>
</ul>
<p>For more information, refer to <a href="/images/optimization/binding/">Optimize with Workers</a>, <a href="/images/optimization/draw-overlays/">Draw overlays and watermarks</a>, and <a href="/images/storage/binding/">Manage hosted images with Workers</a>.</p>
</div></article></div>
