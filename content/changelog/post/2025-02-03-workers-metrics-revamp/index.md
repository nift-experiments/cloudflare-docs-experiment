---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-02-03-workers-metrics-revamp/
  description: New updates and improvements at Cloudflare.
  full_title: Revamped Workers Metrics · Changelog
  head_html: <title>Revamped Workers Metrics · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-02-03-workers-metrics-revamp/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Revamped Workers Metrics · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-02-03-workers-metrics-revamp/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-03-workers-metrics-revamp/#page","headline":"Revamped Workers Metrics \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-02-03-workers-metrics-revamp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-02-03-workers-metrics-revamp/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 3, 2025</time><h2 id="post-title">Revamped Workers Metrics</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We've revamped the <a href="https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics/">Workers Metrics dashboard</a>.</p>
<p><img src="/assets/upstream/images/workers/observability/workers-metrics.png" alt="Workers Metrics dashboard" /></p>
<p>Now you can easily compare metrics across Worker versions, understand the current state of a <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployment</a>, and review key Workers metrics in a single view. This new interface enables you to:</p>
<ul>
<li>Drag-and-select using a graphical timepicker for precise metric selection.</li>
</ul>
<p><img src="/assets/upstream/images/workers/observability/metrics-graphical-timepicker.png" alt="Workers Metrics graphical timepicker" /></p>
<ul>
<li>Use histograms to visualize cumulative metrics, allowing you to bucket and compare rates over time.</li>
<li>Focus on Worker versions by directly interacting with the version numbers in the legend.</li>
</ul>
<p><img src="/assets/upstream/images/workers/observability/metrics-legend-selector.png" alt="Workers Metrics legend selector" /></p>
<ul>
<li>Monitor and compare active gradual deployments.</li>
<li>Track error rates across versions with grouping both by version and by invocation status.</li>
<li>Measure how <a href="/workers/configuration/placement/">Smart Placement</a> improves request duration.</li>
</ul>
<p>Learn more about <a href="/workers/observability/metrics-and-analytics">metrics</a>.</p>
</div></article></div>
