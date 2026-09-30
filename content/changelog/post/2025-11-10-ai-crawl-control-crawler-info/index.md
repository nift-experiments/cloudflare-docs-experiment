---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-11-10-ai-crawl-control-crawler-info/
  description: New updates and improvements at Cloudflare.
  full_title: Crawler drilldowns with extended actions menu · Changelog
  head_html: <title>Crawler drilldowns with extended actions menu · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-11-10-ai-crawl-control-crawler-info/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Crawler drilldowns with extended actions menu · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-11-10-ai-crawl-control-crawler-info/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-10-ai-crawl-control-crawler-info/#page","headline":"Crawler drilldowns with extended actions menu \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-11-10-ai-crawl-control-crawler-info/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-11-10-ai-crawl-control-crawler-info/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 10, 2025</time><h2 id="post-title">Crawler drilldowns with extended actions menu</h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>AI Crawl Control now supports per-crawler drilldowns with an extended actions menu and status code analytics. Drill down into Metrics, Cloudflare Radar, and Security Analytics, or export crawler data for use in <a href="/waf/custom-rules/">WAF custom rules</a>, <a href="/rules/url-forwarding/">Redirect Rules</a>, and robots.txt files.</p>
<h4 id="what-s-new">What's new</h4>
<h4 id="status-code-distribution-chart">Status code distribution chart</h4>
<p>The <strong>Metrics</strong> tab includes a status code distribution chart showing HTTP response codes (2xx, 3xx, 4xx, 5xx) over time. Filter by individual crawler, category, operator, or time range to analyze how specific crawlers interact with your site.</p>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-status-codes.png" alt="AI Crawl Control status code distribution chart" /></p>
<h4 id="extended-actions-menu">Extended actions menu</h4>
<p>Each crawler row includes a three-dot menu with per-crawler actions:</p>
<ul>
<li><strong>View Metrics</strong> — Filter the AI Crawl Control Metrics page to the selected crawler.</li>
<li><strong>View on Cloudflare Radar</strong> — Access verified crawler details on Cloudflare Radar.</li>
<li><strong>Copy User Agent</strong> — Copy user agent strings for use in WAF custom rules, Redirect Rules, or robots.txt files.</li>
<li><strong>View in Security Analytics</strong> — Filter Security Analytics by detection IDs (Bot Management customers).</li>
<li><strong>Copy Detection ID</strong> — Copy detection IDs for use in WAF custom rules (Bot Management customers).</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-crawler-info.png" alt="AI Crawl Control crawler actions menu" /></p>
<h4 id="get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard, and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Metrics</strong> to access the status code distribution chart.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Crawlers</strong> and select the three-dot menu for any crawler to access per-crawler actions.</li>
<li>Select multiple crawlers to use bulk copy buttons for user agents or detection IDs.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control/">AI Crawl Control</a>.</p>
</div></article></div>
