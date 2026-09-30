---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/
  description: New updates and improvements at Cloudflare.
  full_title: Pipeline binding configuration field renamed to stream · Changelog
  head_html: <title>Pipeline binding configuration field renamed to stream · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Pipeline binding configuration field renamed to stream · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/#page","headline":"Pipeline binding configuration field renamed to stream \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-27-pipeline-binding-stream-field/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 4, 2026</time><h2 id="post-title">Pipeline binding configuration field renamed to stream</h2>
<div class="changelog-badges"><span>pipelines</span><span>workers</span></div><div class="changelog-body"><p>The <code>pipeline</code> field inside the <code>pipelines</code> binding configuration in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> has been renamed to <code>stream</code>. The old field is deprecated but still accepted.</p>
<p>Update your configuration to use <code>stream</code> to avoid the deprecation warning.</p>
<p><strong>Before (deprecated):</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17739.md")</div>
<p><strong>After:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17740.md")</div>
<p>No other changes are required. The binding name, TypeScript types, and runtime API (<code>env.MY_PIPELINE.send(...)</code>) remain the same.</p>
<p>For more information on configuring pipeline bindings, refer to <a href="/pipelines/streams/writing-to-streams/#configure-pipeline-binding">Writing to streams</a>.</p>
</div></article></div>
