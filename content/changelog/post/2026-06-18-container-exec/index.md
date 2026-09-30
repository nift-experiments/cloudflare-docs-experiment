---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/
  description: New updates and improvements at Cloudflare.
  full_title: exec() is now available for Containers · Changelog
  head_html: <title>exec() is now available for Containers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="exec() is now available for Containers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/#page","headline":"exec() is now available for Containers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-18-container-exec/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 18, 2026</time><h2 id="post-title">exec() is now available for Containers</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p><code>exec()</code> is now available for <a href="/containers/">Containers</a>. Use <code>this.ctx.container.exec()</code> to start processes inside a running Container, stream standard input and output, inspect exit codes, and signal each process.</p>
<p>Call <code>exec()</code> from a class extending <code>Container</code>, or from another Durable Object through <code>this.ctx.container</code>. The associated Container must already be running.</p>
<p>This example starts the Container when needed, then reads its Node.js version:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17713.md")</div>
<p>The command array starts an executable directly, without an implicit shell. Invoke a shell explicitly for pipes, redirects, or variable expansion.</p>
<p>One RPC method can coordinate multiple <code>exec()</code> calls in one caller-to-Durable Object round trip. It can also pass byte-oriented <code>ReadableStream</code> input or return streamed output with flow control.</p>
<p>For options and streaming examples, refer to <a href="/containers/guides/execute-commands/">Execute commands</a>.</p>
</div></article></div>
