---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/
  description: New updates and improvements at Cloudflare.
  full_title: More SQL aggregate, date and time functions available in Workers Analytics Engine · Changelog
  head_html: <title>More SQL aggregate, date and time functions available in Workers Analytics Engine · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="More SQL aggregate, date and time functions available in Workers Analytics Engine · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/#page","headline":"More SQL aggregate, date and time functions available in Workers Analytics Engine \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 12, 2025</time><h2 id="post-title">More SQL aggregate, date and time functions available in Workers Analytics Engine</h2>
<div class="changelog-badges"><span>workers-analytics-engine</span><span>workers</span></div><div class="changelog-body"><p>You can now perform more powerful queries directly in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a> with a major expansion of our SQL function library.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.</p>
<p>Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:</p>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/"><strong>New aggregate functions:</strong></a></p>
<ul>
<li><code>countIf()</code> - count the number of rows which satisfy a provided condition</li>
<li><code>sumIf()</code> - calculate a sum from rows which satisfy a provided condition</li>
<li><code>avgIf()</code> - calculate an average from rows which satisfy a provided condition</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/date-time-functions/"><strong>New date and time functions:</strong></a></p>
<ul>
<li><code>toYear()</code></li>
<li><code>toMonth()</code></li>
<li><code>toDayOfMonth()</code></li>
<li><code>toDayOfWeek()</code></li>
<li><code>toHour()</code></li>
<li><code>toMinute()</code></li>
<li><code>toSecond()</code></li>
<li><code>toStartOfYear()</code></li>
<li><code>toStartOfMonth()</code></li>
<li><code>toStartOfWeek()</code></li>
<li><code>toStartOfDay()</code></li>
<li><code>toStartOfHour()</code></li>
<li><code>toStartOfFifteenMinutes()</code></li>
<li><code>toStartOfTenMinutes()</code></li>
<li><code>toStartOfFiveMinutes()</code></li>
<li><code>toStartOfMinute()</code></li>
<li><code>today()</code></li>
<li><code>toYYYYMM()</code></li>
</ul>
<h4 id="ready-to-get-started">Ready to get started?</h4>
Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started ](/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](/analytics/analytics-engine/sql-reference/).
</div></article></div>
