---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/
  description: New updates and improvements at Cloudflare.
  full_title: New Confidence Intervals in GraphQL Analytics API · Changelog
  head_html: <title>New Confidence Intervals in GraphQL Analytics API · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New Confidence Intervals in GraphQL Analytics API · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/#page","headline":"New Confidence Intervals in GraphQL Analytics API \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-10-01-confidence-intervals/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 1, 2025</time><h2 id="post-title">New Confidence Intervals in GraphQL Analytics API</h2>
<div class="changelog-badges"><span>analytics</span></div><div class="changelog-body"><p>The GraphQL Analytics API now supports confidence intervals for <code>sum</code> and <code>count</code> fields on adaptive (sampled) datasets. Confidence intervals provide a statistical range around sampled results, helping verify accuracy and quantify uncertainty.</p>
<ul>
<li><strong>Supported datasets</strong>: Adaptive (sampled) datasets only.</li>
<li><strong>Supported fields</strong>: All <code>sum</code> and <code>count</code> fields.</li>
<li><strong>Usage</strong>: The confidence <code>level</code> must be provided as a decimal between 0 and 1 (e.g. <code>0.90</code>, <code>0.95</code>, <code>0.99</code>).</li>
<li><strong>Default</strong>: If no confidence level is specified, no intervals are returned.</li>
</ul>
<p>For examples and more details, see the <a href="/analytics/graphql-api/features/confidence-intervals/">GraphQL Analytics API documentation</a>.</p>
</div></article></div>
