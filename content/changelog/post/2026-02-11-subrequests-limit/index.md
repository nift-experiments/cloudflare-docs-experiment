---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/
  description: New updates and improvements at Cloudflare.
  full_title: Workers are no longer limited to 1000 subrequests · Changelog
  head_html: <title>Workers are no longer limited to 1000 subrequests · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Workers are no longer limited to 1000 subrequests · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/#page","headline":"Workers are no longer limited to 1000 subrequests \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-11-subrequests-limit/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 11, 2026</time><h2 id="post-title">Workers are no longer limited to 1000 subrequests</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers no longer have a limit of 1000 subrequests per invocation, allowing you to make more <code>fetch()</code> calls or requests
to Cloudflare services on every incoming request. This is especially important for long-running Workers requests, such as
open websockets on <a href="/durable-objects">Durable Objects</a> or long-running <a href="/workflows">Workflows</a>, as these could often exceed this limit and error.</p>
<p>By default, Workers on paid plans are now limited to 10,000 subrequests per invocation, but this
limit can be increased up to 10 million by setting the new <code>subrequests</code> limit in your Wrangler configuration file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17797.md")</div>
<p>Workers on the free plan remain limited to 50 external subrequests and 1000 subrequests to Cloudflare services per invocation.</p>
<p>To protect against runaway code or unexpected costs, you can also set a lower limit for both subrequests and CPU usage.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17798.md")</div>
<p>For more information, refer to the <a href="/workers/wrangler/configuration/#limits">Wrangler configuration documentation for limits</a> and <a href="/workers/platform/limits/#subrequests">subrequest limits</a>.</p>
</div></article></div>
