---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-16-markdown-for-agents-improvements/
  description: New updates and improvements at Cloudflare.
  full_title: Content encoding support for Markdown for Agents and other improvements · Changelog
  head_html: <title>Content encoding support for Markdown for Agents and other improvements · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-16-markdown-for-agents-improvements/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Content encoding support for Markdown for Agents and other improvements · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-16-markdown-for-agents-improvements/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-16-markdown-for-agents-improvements/#page","headline":"Content encoding support for Markdown for Agents and other improvements \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-16-markdown-for-agents-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-16-markdown-for-agents-improvements/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 16, 2026</time><h2 id="post-title">Content encoding support for Markdown for Agents and other improvements</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>When AI systems request pages from any website that uses Cloudflare and has <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> enabled, they can express the preference for <code>text/markdown</code> in the request: our network will automatically and efficiently convert the HTML to markdown, when possible, on the fly.</p>
<p>This release adds the following improvements:</p>
<ul>
<li>The origin response limit was raised from 1 MB to 2 MB (2,097,152 bytes).</li>
<li>We no longer require the origin to send the <code>content-length</code> header.</li>
<li>We now support content encoded responses from the origin.</li>
</ul>
<p>If you haven’t enabled automatic Markdown conversion yet, visit the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ai">AI Crawl Control</a> section of the Cloudflare dashboard and enable <strong>Markdown for Agents</strong>.</p>
<p>Refer to our <a href="/fundamentals/reference/markdown-for-agents/">developer documentation</a> for more details.</p>
</div></article></div>
