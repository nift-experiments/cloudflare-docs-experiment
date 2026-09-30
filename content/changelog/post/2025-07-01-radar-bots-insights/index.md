---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-07-01-radar-bots-insights/
  description: New updates and improvements at Cloudflare.
  full_title: Bot & Crawler Insights in Cloudflare Radar · Changelog
  head_html: <title>Bot &amp; Crawler Insights in Cloudflare Radar · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-07-01-radar-bots-insights/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Bot &amp; Crawler Insights in Cloudflare Radar · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-07-01-radar-bots-insights/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-01-radar-bots-insights/#page","headline":"Bot & Crawler Insights in Cloudflare Radar \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-07-01-radar-bots-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-07-01-radar-bots-insights/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 1, 2025</time><h2 id="post-title">Bot &amp; Crawler Insights in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><h4 id="web-crawlers-insights">Web crawlers insights</h4>
<p><a href="/radar/"><strong>Radar</strong></a> now offers expanded insights into web crawlers, giving you greater visibility into aggregated trends in crawl and refer activity.</p>
<p>We have introduced the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/summary/"><code>/bots/crawlers/summary/{dimension}</code></a>: Returns an overview of crawler HTTP request distributions across key dimensions.</li>
<li><a href="/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/timeseries_groups/"><code>/bots/crawlers/timeseries_groups/{dimension}</code></a>: Provides time-series data on crawler request distributions across the same dimensions.</li>
</ul>
<p>These endpoints allow analysis across the following dimensions:</p>
<ul>
<li><code>user_agent</code>: Parsed data from the <code>User-Agent</code> header.</li>
<li><code>referer</code>: Parsed data from the <code>Referer</code> header.</li>
<li><code>crawl_refer_ratio</code>: Ratio of HTML page crawl requests to HTML page referrals by platform.</li>
</ul>
<h4 id="broader-bot-insights">Broader bot insights</h4>
<p>In addition to crawler-specific insights, Radar now provides a broader set of bot endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bots/"><code>/bots/</code></a>: Lists all bots.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/get/"><code>/bots/{bot_slug}</code></a>: Returns detailed metadata for a specific bot.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/timeseries/"><code>/bots/timeseries</code></a>: Time-series data for bot activity.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/summary/"><code>/bots/summary/{dimension}</code></a>: Returns an overview of bot HTTP request distributions across key dimensions.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/timeseries_groups/"><code>/bots/timeseries_groups/{dimension}</code></a>: Provides time-series data on bot request distributions across the same dimensions.</li>
</ul>
<p>These endpoints support filtering and breakdowns by:</p>
<ul>
<li><code>bot</code>: Bot name.</li>
<li><code>bot_operator</code>: The organization or entity operating the bot.</li>
<li><code>bot_category</code>: Classification of bot type.</li>
</ul>
<p>The previously available <code>verified_bots</code> endpoints have now been deprecated in favor of this set of bot insights APIs.
While current data still focuses on verified bots, we plan to expand support for unverified bot traffic in the future.</p>
<p>Learn more about the new Radar bot and crawler insights in our <a href="https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar">blog post</a>.</p>
</div></article></div>
