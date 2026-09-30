---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-04-07-increase-trace-events-limit/
  description: New updates and improvements at Cloudflare.
  full_title: Capture up to 256 KB of log events in each Workers Invocation · Changelog
  head_html: <title>Capture up to 256 KB of log events in each Workers Invocation · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-04-07-increase-trace-events-limit/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Capture up to 256 KB of log events in each Workers Invocation · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-04-07-increase-trace-events-limit/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-07-increase-trace-events-limit/#page","headline":"Capture up to 256 KB of log events in each Workers Invocation \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-04-07-increase-trace-events-limit/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-04-07-increase-trace-events-limit/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 7, 2025</time><h2 id="post-title">Capture up to 256 KB of log events in each Workers Invocation</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now capture a maximum of 256 KB of log events per Workers invocation, helping you gain better visibility into application behavior.</p>
<p>All console.log() statements, exceptions, request metadata, and headers are automatically captured during the Worker invocation and emitted
as <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events">JSON object</a>. <a href="/workers/observability/logs/workers-logs">Workers Logs</a> deserializes
this object before indexing the fields and storing them. You can also capture, transform, and export the JSON object in a
<a href="/workers/observability/logs/tail-workers">Tail Worker</a>.</p>
<p>256 KB is a 2x increase from the previous 128 KB limit. After you exceed this limit, further context associated with the request will not be
recorded in your logs.</p>
<p>This limit is automatically applied to all Workers.</p>
</div></article></div>
