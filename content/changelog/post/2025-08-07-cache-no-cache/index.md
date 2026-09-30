---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-08-07-cache-no-cache/
  description: New updates and improvements at Cloudflare.
  full_title: Requests made from Cloudflare Workers can now force a revalidation of their cache with the origin · Changelog
  head_html: <title>Requests made from Cloudflare Workers can now force a revalidation of their cache with the origin · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-08-07-cache-no-cache/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Requests made from Cloudflare Workers can now force a revalidation of their cache with the origin · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-08-07-cache-no-cache/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-07-cache-no-cache/#page","headline":"Requests made from Cloudflare Workers can now force a revalidation of their cache with the origin \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-08-07-cache-no-cache/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-08-07-cache-no-cache/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 7, 2025</time><h2 id="post-title">Requests made from Cloudflare Workers can now force a revalidation of their cache with the origin</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>By setting the value of the <code>cache</code> property to <code>no-cache</code>, you can force <a href="/workers/reference/how-the-cache-works/">Cloudflare's
cache</a> to revalidate its contents with the origin when
making subrequests from <a href="/workers">Cloudflare Workers</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17783.md")</div>
<p>When <code>no-cache</code> is set, the Worker request will first look for a match in Cloudflare's cache, then:</p>
<ul>
<li>If there is a match, a conditional request is sent to the origin, regardless of whether or not the match is fresh or stale. If the resource has not changed, the
cached version is returned. If the resource has changed, it will be downloaded from the origin, updated in the cache, and returned.</li>
<li>If there is no match, Workers will make a standard request to the origin and cache the response.</li>
</ul>
<p>This increases compatibility with NPM packages and JavaScript frameworks that rely on setting the
<a href="/workers/runtime-apis/request/#options"><code>cache</code></a> property, which is a cross-platform standard part
of the <a href="/workers/runtime-apis/request/"><code>Request</code></a> interface. Previously, if you set the <code>cache</code>
property on <code>Request</code> to <code>'no-cache'</code>, the Workers runtime threw an exception.</p>
<ul>
<li>Learn <a href="/workers/reference/how-the-cache-works/">how the Cache works with Cloudflare Workers</a></li>
<li>Enable <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> for your Cloudflare Worker</li>
<li>Explore <a href="/workers/runtime-apis/">Runtime APIs</a> and <a href="/workers/runtime-apis/bindings/">Bindings</a> available in Cloudflare Workers</li>
</ul>
</div></article></div>
