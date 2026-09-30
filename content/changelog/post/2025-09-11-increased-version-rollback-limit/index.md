---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/
  description: New updates and improvements at Cloudflare.
  full_title: Worker version rollback limit increased from 10 to 100 · Changelog
  head_html: <title>Worker version rollback limit increased from 10 to 100 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Worker version rollback limit increased from 10 to 100 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/#page","headline":"Worker version rollback limit increased from 10 to 100 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-11-increased-version-rollback-limit/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 11, 2025</time><h2 id="post-title">Worker version rollback limit increased from 10 to 100</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The number of recent versions available for a Worker rollback has been increased from 10 to 100.</p>
<p>This allows you to:</p>
<ul>
<li>
<p>Promote any of the 100 most recent versions to be the active deployment.</p>
</li>
<li>
<p>Split traffic using <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployments</a> between your latest code and any of the 100 most recent versions.</p>
</li>
</ul>
<p>You can do this through the Cloudflare dashboard or with <a href="/workers/wrangler/commands/general/#rollback">Wrangler's rollback command</a></p>
<p>Learn more about <a href="/workers/versions-and-deployments/">versioned deployments</a> and <a href="/workers/versions-and-deployments/rollbacks/">rollbacks</a>.</p>
</div></article></div>
