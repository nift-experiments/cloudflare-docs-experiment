---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/
  description: New updates and improvements at Cloudflare.
  full_title: 'Rewind, Replay, Resume: Introducing DVR for Stream Live · Changelog'
  head_html: '<title>Rewind, Replay, Resume: Introducing DVR for Stream Live · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Rewind, Replay, Resume: Introducing DVR for Stream Live · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/#page","headline":"Rewind, Replay, Resume: Introducing DVR for Stream Live \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>'
  markdown: false
  noindex: false
  route: /changelog/post/2025-02-14-introducing-dvr-for-stream-live/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 14, 2025</time><h2 id="post-title">Rewind, Replay, Resume: Introducing DVR for Stream Live</h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>Previously, all viewers watched &quot;the live edge,&quot; or the latest content of the
broadcast, synchronously. If a viewer paused for more than a few seconds,
the player would automatically &quot;catch up&quot; when playback started again. Seeking
through the broadcast was only available once the recording was available after
it concluded.</p>
<p>Starting today, customers can make a small adjustment to the player
embed or manifest URL to enable the DVR experience for their viewers. By
offering this feature as an opt-in adjustment, our customers are empowered to
pick the best experiences for their applications.</p>
<p>When building a player embed code or manifest URL, just add <code>dvrEnabled=true</code> as
a query parameter. There are some things to be aware of when using this option.
For more information, refer to <a href="/stream/stream-live/dvr-for-live/">DVR for Live</a>.</p>
</div></article></div>
