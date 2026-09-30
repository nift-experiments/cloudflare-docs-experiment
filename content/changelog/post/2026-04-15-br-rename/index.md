---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/
  description: New updates and improvements at Cloudflare.
  full_title: Browser Rendering is now Browser Run · Changelog
  head_html: <title>Browser Rendering is now Browser Run · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Browser Rendering is now Browser Run · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/#page","headline":"Browser Rendering is now Browser Run \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-15-br-rename/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 15, 2026</time><h2 id="post-title">Browser Rendering is now Browser Run</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>We are renaming Browser Rendering to <strong><a href="/browser-run/">Browser Run</a></strong>. The name Browser Rendering never fully captured what the product does. Browser Run lets you run full browser sessions on Cloudflare's global network, drive them with code or AI, record and replay sessions, crawl pages for content, debug in real time, and let humans intervene when your agent needs help.</p>
<p>Along with the rename, we have increased limits for Workers Paid plans and redesigned the Browser Run dashboard.</p>
<p>We have 4x-ed concurrency limits for Workers Paid plan users:</p>
<ul>
<li><strong>Concurrent browsers per account</strong>: 30 → <strong>120 per account</strong></li>
<li><strong>New browser instances</strong>: 30 per minute → <strong>1 per second</strong></li>
<li><strong>REST API rate limits</strong>: recently increased from <a href="/changelog/post/2026-03-04-br-rest-api-limit-increase/">3 to 10 requests per second</a></li>
</ul>
<p>Rate limits across the <a href="/browser-run/limits/">limits page</a> are now expressed in per-second terms, matching how they are enforced. No action is needed to benefit from the higher limits.</p>
<p>The <a href="https://dash.cloudflare.com/?to=/:account/workers/browser-run">redesigned dashboard</a> now shows every request in a single Runs tab, not just browser sessions but also quick actions like screenshots, PDFs, markdown, and crawls. Filter by endpoint, view target URLs, status, and duration, and expand any row for more detail.</p>
<p><img src="/images/browser-run/BRdashboardredesign.png" alt="Browser Run dashboard Runs tab with browser sessions and quick actions visible in one list, and an expanded crawl job showing its progress" /></p>
<p>We are also shipping several new features:</p>
<ul>
<li><strong><a href="/changelog/post/2026-04-15-br-observability/">Live View, Human in the Loop, and Session Recordings</a></strong> - See what your agent is doing in real time, let humans step in when automation hits a wall, and replay any session after it ends.</li>
<li><strong><a href="/changelog/post/2026-04-15-br-webmcp/">WebMCP</a></strong> - Websites can expose structured tools for AI agents to discover and call directly, replacing slow screenshot-analyze-click loops.</li>
</ul>
<p>For the full story, read our Agents Week blog <a href="https://blog.cloudflare.com/browser-run-for-ai-agents">Browser Run: Give your agents a browser</a>.</p>
</div></article></div>
