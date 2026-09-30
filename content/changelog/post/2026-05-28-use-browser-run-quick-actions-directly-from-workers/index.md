---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/
  description: New updates and improvements at Cloudflare.
  full_title: Use Browser Run Quick Actions directly from Workers · Changelog
  head_html: <title>Use Browser Run Quick Actions directly from Workers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Use Browser Run Quick Actions directly from Workers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/#page","headline":"Use Browser Run Quick Actions directly from Workers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 28, 2026</time><h2 id="post-title">Use Browser Run Quick Actions directly from Workers</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>You can now call <a href="/browser-run/quick-actions/">Browser Run Quick Actions</a> directly from a <a href="/workers/">Cloudflare Worker</a> using the <code>quickAction()</code> method on the browser binding. This simplifies how Workers interact with Browser Run by removing the need for API tokens or external HTTP requests. Your Worker communicates with Browser Run directly over Cloudflare's network, resulting in simpler code and lower latency.</p>
<p>With the <code>quickAction()</code> method you can:</p>
<ul>
<li><a href="/browser-run/quick-actions/screenshot-endpoint/">Capture screenshots</a> from URLs or HTML</li>
<li><a href="/browser-run/quick-actions/pdf-endpoint/">Generate PDFs</a> with custom styling, headers, and footers</li>
<li><a href="/browser-run/quick-actions/content-endpoint/">Extract HTML content</a> from fully rendered pages</li>
<li><a href="/browser-run/quick-actions/markdown-endpoint/">Convert pages to Markdown</a></li>
<li><a href="/browser-run/quick-actions/json-endpoint/">Extract structured JSON</a> using AI</li>
<li><a href="/browser-run/quick-actions/scrape-endpoint/">Scrape elements</a> with CSS selectors</li>
<li><a href="/browser-run/quick-actions/links-endpoint/">Get all links</a> from a page</li>
<li><a href="/browser-run/quick-actions/snapshot/">Capture snapshots</a> (HTML + screenshot in one request)</li>
</ul>
<p>To get started, add a browser binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17694.md")</div>
<p>Then call any Quick Action directly from your Worker. For example, to capture a screenshot:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17695.md")</div>
<p>The <code>quickAction()</code> method requires a compatibility date of <code>2026-03-24</code> or later.</p>
<p>For setup instructions and the full list of available actions, refer to <a href="/browser-run/quick-actions/">Browser Run Quick Actions</a>.</p>
</div></article></div>
