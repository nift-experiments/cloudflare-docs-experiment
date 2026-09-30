---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-01-31-html-rewriter-streaming/
  description: New updates and improvements at Cloudflare.
  full_title: Transform HTML quickly with streaming content · Changelog
  head_html: <title>Transform HTML quickly with streaming content · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-01-31-html-rewriter-streaming/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Transform HTML quickly with streaming content · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-01-31-html-rewriter-streaming/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-01-31-html-rewriter-streaming/#page","headline":"Transform HTML quickly with streaming content \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-01-31-html-rewriter-streaming/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-01-31-html-rewriter-streaming/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 31, 2025</time><h2 id="post-title">Transform HTML quickly with streaming content</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now transform HTML elements with streamed content using <a href="/workers/runtime-apis/html-rewriter"><code>HTMLRewriter</code></a>.</p>
<p>Methods like <code>replace</code>, <code>append</code>, and <code>prepend</code> now accept <a href="/workers/runtime-apis/response/"><code>Response</code></a> and <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a>
values as <a href="/workers/runtime-apis/html-rewriter/#global-types"><code>Content</code></a>.</p>
<p>This can be helpful in a variety of situations. For instance, you may have a Worker in front of an origin,
and want to replace an element with content from a different source. Prior to this change, you would have to load
all of the content from the upstream URL and convert it into a string before replacing the element. This slowed
down overall response times.</p>
<p>Now, you can pass the <code>Response</code> object directly into the <code>replace</code> method, and HTMLRewriter will immediately
start replacing the content as it is streamed in. This makes responses faster.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17765.md")</div>
<p>For more information, see the <a href="/workers/runtime-apis/html-rewriter"><code>HTMLRewriter</code> documentation</a>.</p>
</div></article></div>
