---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/
  description: New updates and improvements at Cloudflare.
  full_title: Manage hosted images with the Images binding · Changelog
  head_html: <title>Manage hosted images with the Images binding · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Manage hosted images with the Images binding · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/#page","headline":"Manage hosted images with the Images binding \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-10-hosted-images-binding/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 10, 2026</time><h2 id="post-title">Manage hosted images with the Images binding</h2>
<div class="changelog-badges"><span>images</span></div><div class="changelog-body"><p>Use the Images binding to upload, list, retrieve, update, and delete images stored in Images directly from your Worker without managing API tokens or making HTTP requests.</p>
<p>The <code>env.IMAGES.hosted</code> namespace supports the following storage and management operations:</p>
<ul>
<li><a href="/images/storage/binding/#uploadimage-options"><code>.upload(image, options)</code></a> — Upload a new image to your account.</li>
<li><a href="/images/storage/binding/#listoptions"><code>.list(options)</code></a> — List images with pagination.</li>
<li><a href="/images/storage/binding/#imageimageiddetails"><code>.image(imageId).details()</code></a> — Get image metadata.</li>
<li><a href="/images/storage/binding/#imageimageidbytes"><code>.image(imageId).bytes()</code></a> — Stream the original image bytes.</li>
<li><a href="/images/storage/binding/#imageimageidupdateoptions"><code>.image(imageId).update(options)</code></a> — Update metadata or access controls.</li>
<li><a href="/images/storage/binding/#imageimageiddelete"><code>.image(imageId).delete()</code></a> — Delete an image.</li>
</ul>
<p>For example, you can upload an image from a request body and return its metadata:</p>
<pre tabindex="0"><code class="language-ts">const image = await env.IMAGES.hosted.upload(request.body, {&#10;	filename: &quot;upload.jpg&quot;,&#10;	metadata: { source: &quot;worker&quot; },&#10;});&#10;&#10;return Response.json(image);&#10;</code></pre>
<p>Or retrieve and serve the original bytes of a hosted image:</p>
<pre tabindex="0"><code class="language-ts">const bytes = await env.IMAGES.hosted.image(&quot;IMAGE_ID&quot;).bytes();&#10;return new Response(bytes);&#10;</code></pre>
<p>For more information, refer to the <a href="/images/storage/binding/">Images binding</a>.</p>
</div></article></div>
