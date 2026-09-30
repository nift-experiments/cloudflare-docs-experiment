---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/automatic-platform-optimization/
  description: '2026-08-27'
  full_title: automatic-platform-optimization changelog | Cloudflare Docs
  head_html: <title>automatic-platform-optimization changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-08-27"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/automatic-platform-optimization/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="automatic-platform-optimization changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-08-27"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/automatic-platform-optimization/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/automatic-platform-optimization/#page","headline":"automatic-platform-optimization changelog | Cloudflare Docs","description":"2026-08-27","url":"https://developers.cloudflare.com/changelog/product/automatic-platform-optimization/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/automatic-platform-optimization/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="apo-caches-more-crawler-and-bot-traffic-again"><a href="/changelog/post/2026-08-27-accept-header-caching/">APO caches more crawler and bot traffic again</a></h2>
<p><em>2026-08-27</em></p>
<p>We fixed a regression where Automatic Platform Optimization (APO) stopped caching some HTML requests that did not send an explicit <code>Accept: text/html</code> header — commonly crawlers, bots, and uptime monitors. These requests were being served from your origin (<code>cf-cache-status: DYNAMIC</code>) instead of the cache.</p>
<p>APO now caches these requests again. No action is needed. If you added a Transform Rule to set <code>Accept: text/html</code> as a workaround, you can remove it.</p>
<p>For details on how APO decides what to cache, refer to <a href="/automatic-platform-optimization/about/">About APO</a>.</p>



