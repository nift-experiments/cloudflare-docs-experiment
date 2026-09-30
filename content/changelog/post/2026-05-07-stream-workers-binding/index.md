---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/
  description: New updates and improvements at Cloudflare.
  full_title: Introducing Stream Bindings for Workers · Changelog
  head_html: <title>Introducing Stream Bindings for Workers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Introducing Stream Bindings for Workers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/#page","headline":"Introducing Stream Bindings for Workers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-07-stream-workers-binding/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 7, 2026</time><h2 id="post-title">Introducing Stream Bindings for Workers</h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>You can now interact with your Stream video library using new bindings for Workers! This allows customers to upload content to Stream, provision direct uploads, manage videos, and generate signed URLs from a Worker without making authenticated API calls. We're excited to bring Stream and Workers closer together to empower more programmatic pipelines, tighter integrations, and support generative AI and inference workloads.</p>
<p>Use the Stream binding when you want to:</p>
<ul>
<li>Upload videos from URLs or create basic direct upload links for end users</li>
<li>Generate signed playback tokens without managing signing keys</li>
<li>Manage video metadata, captions, downloads, and watermarks</li>
<li>Build video pipelines entirely within Workers</li>
</ul>
<p>To get started, add the Stream binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17756.md")</div>
<p><strong>Generate a video with AI and upload directly to Stream</strong> or send a URL of a file you already have:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17757.md")</div>
<p><strong>Generate a signed URL without using a signing key</strong> or an API call:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17758.md")</div>
<p><strong>Get and set video properties</strong> easily:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17759.md")</div>
<p>For setup instructions and the full API reference, refer to <a href="/stream/manage-video-library/bindings/">Bind to Workers API</a>.</p>
<h4 id="get-started-with-your-agent">Get started with your Agent</h4>
<blockquote>
<p>Add a binding for Cloudflare Stream (env.STREAM). On the watch page, use the
Stream binding to get info based on the ID, and leverage video.meta.name as
the page title.</p>
</blockquote>
</div></article></div>
