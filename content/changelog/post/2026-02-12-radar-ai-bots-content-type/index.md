---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/
  description: New updates and improvements at Cloudflare.
  full_title: Content Type Dimension for AI Bots in Cloudflare Radar · Changelog
  head_html: <title>Content Type Dimension for AI Bots in Cloudflare Radar · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Content Type Dimension for AI Bots in Cloudflare Radar · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/#page","headline":"Content Type Dimension for AI Bots in Cloudflare Radar \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-12-radar-ai-bots-content-type/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 12, 2026</time><h2 id="post-title">Content Type Dimension for AI Bots in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now includes content type insights for AI bot and crawler traffic. The new <code>content_type</code> dimension and filter shows the distribution of content types returned to AI crawlers, grouped by MIME type category.</p>
<p>The content type dimension and filter are available via the following API endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ai/subresources/bots/methods/summary_v2/"><code>/ai/bots/summary/content_type</code></a></li>
<li><a href="/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries_groups/"><code>/ai/bots/timeseries_groups/content_type</code></a></li>
</ul>
<p>Content type categories:</p>
<ul>
<li><strong>HTML</strong> - Web pages (<code>text/html</code>)</li>
<li><strong>Images</strong> - All image formats (<code>image/*</code>)</li>
<li><strong>JSON</strong> - JSON data and API responses (<code>application/json</code>, <code>*+json</code>)</li>
<li><strong>JavaScript</strong> - Scripts (<code>application/javascript</code>, <code>text/javascript</code>)</li>
<li><strong>CSS</strong> - Stylesheets (<code>text/css</code>)</li>
<li><strong>Plain Text</strong> - Unformatted text (<code>text/plain</code>)</li>
<li><strong>Fonts</strong> - Web fonts (<code>font/*</code>, <code>application/font-*</code>)</li>
<li><strong>XML</strong> - XML documents and feeds (<code>text/xml</code>, <code>application/xml</code>, <code>application/rss+xml</code>, <code>application/atom+xml</code>)</li>
<li><strong>YAML</strong> - Configuration files (<code>text/yaml</code>, <code>application/yaml</code>)</li>
<li><strong>Video</strong> - Video content and streaming (<code>video/*</code>, <code>application/ogg</code>, <code>*mpegurl</code>)</li>
<li><strong>Audio</strong> - Audio content (<code>audio/*</code>)</li>
<li><strong>Markdown</strong> - Markdown documents (<code>text/markdown</code>)</li>
<li><strong>Documents</strong> - PDFs, Office documents, ePub, CSV (<code>application/pdf</code>, <code>application/msword</code>, <code>text/csv</code>)</li>
<li><strong>Binary</strong> - Executables, archives, WebAssembly (<code>application/octet-stream</code>, <code>application/zip</code>, <code>application/wasm</code>)</li>
<li><strong>Serialization</strong> - Binary API formats (<code>application/protobuf</code>, <code>application/grpc</code>, <code>application/msgpack</code>)</li>
<li><strong>Other</strong> - All other content types</li>
</ul>
<p>Additionally, individual <a href="https://radar.cloudflare.com/bots/directory/gptbot">bot information pages</a> now display content type distribution for AI crawlers that exist in both the Verified Bots and AI Bots datasets.</p>
<p><img src="/assets/upstream/images/radar/ai-bots-content-type.png" alt="Screenshot of the Content Type Distribution chart on the AI Insights page" /></p>
<p>Check out the <a href="https://radar.cloudflare.com/ai-insights#content-type">AI Insights page</a> to explore the data.</p>
</div></article></div>
