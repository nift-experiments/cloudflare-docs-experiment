---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/
  description: New updates and improvements at Cloudflare.
  full_title: Bind the Images API to your Worker · Changelog
  head_html: <title>Bind the Images API to your Worker · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Bind the Images API to your Worker · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/#page","headline":"Bind the Images API to your Worker \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-02-21-images-bindings-in-workers/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 24, 2025</time><h2 id="post-title">Bind the Images API to your Worker</h2>
<div class="changelog-badges"><span>images</span></div><div class="changelog-body"><p>You can now <a href="/images/optimization/binding/">interact with the Images API</a> directly in your Worker.</p>
<p>This allows more fine-grained control over transformation request flows and cache behavior. For example, you can resize, manipulate, and overlay images without requiring them to be accessible through a URL.</p>
<p>The Images binding can be configured in the Cloudflare dashboard for your Worker or in the Wrangler configuration file in your project's directory:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17735.md")</div>
<p>Within your Worker code, you can interact with this binding by using <code>env.IMAGES</code>.</p>
<p>Here's how you can rotate, resize, and blur an image, then output the image as AVIF:</p>
<pre tabindex="0"><code class="language-ts">const info = await env.IMAGES.info(stream);&#10;// stream contains a valid image, and width/height is available on the info object&#10;&#10;const response = (&#10;	await env.IMAGES.input(stream)&#10;		.transform({ rotate: 90 })&#10;		.transform({ width: 128 })&#10;		.transform({ blur: 20 })&#10;		.output({ format: &quot;image/avif&quot; })&#10;).response();&#10;&#10;return response;&#10;</code></pre>
<p>For more information, refer to <a href="/images/optimization/binding/">Images Bindings</a>.</p>
</div></article></div>
