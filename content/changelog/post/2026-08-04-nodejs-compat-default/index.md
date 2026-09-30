---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/
  description: New updates and improvements at Cloudflare.
  full_title: Node.js compatibility is now enabled by default · Changelog
  head_html: <title>Node.js compatibility is now enabled by default · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Node.js compatibility is now enabled by default · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/#page","headline":"Node.js compatibility is now enabled by default \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-04-nodejs-compat-default/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 4, 2026</time><h2 id="post-title">Node.js compatibility is now enabled by default</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers now enable the <code>nodejs_compat</code> and <code>nodejs_compat_v2</code> compatibility
flags by default for <a href="/workers/configuration/compatibility-dates/">compatibility dates</a>
of <code>2026-08-04</code> or later. These flags are not used for these compatibility
dates because the compatibility date enables the same behavior.</p>
<p>This means all <a href="/workers/runtime-apis/nodejs/">Node.js built-in APIs</a> supported
by the Workers runtime are available by default, including <code>node:crypto</code>,
<code>node:buffer</code>, <code>node:stream</code>, <code>node:net</code>, <code>node:dns</code>, <code>node:fs</code>, <code>node:http</code>,
and more. npm packages that depend on these APIs will work without additional
configuration.</p>
<p>Workers using an earlier compatibility date are not affected. They can still
opt in by adding <code>nodejs_compat</code> to <code>compatibility_flags</code>.</p>
<p>New projects do not need to add either flag. Existing projects can update their
compatibility date without removing them. Wrangler, Miniflare, the Cloudflare
Vite plugin, and Vitest Pool Workers ignore these redundant flags when starting
the runtime.</p>
<p>To turn off Node.js compatibility completely, remove any <code>nodejs_compat</code> and
<code>nodejs_compat_v2</code> flags. Then add both of the following flags:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17813.md")</div>
<p>For more information, refer to the <a href="/workers/runtime-apis/nodejs/">Node.js compatibility documentation</a>.</p>
</div></article></div>
