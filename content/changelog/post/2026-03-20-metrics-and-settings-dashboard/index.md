---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/
  description: New updates and improvements at Cloudflare.
  full_title: Observability for Workers VPC Services · Changelog
  head_html: <title>Observability for Workers VPC Services · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Observability for Workers VPC Services · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/#page","headline":"Observability for Workers VPC Services \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-20-metrics-and-settings-dashboard/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 20, 2026</time><h2 id="post-title">Observability for Workers VPC Services</h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p>Each VPC Service now has a <strong>Metrics</strong> tab so you can monitor connection health and debug failures without leaving the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers-vpc/2026-03-20-metrics-dashboard.png" alt="Workers VPC Metrics dashboard showing connections, latency, and errors charts" /></p>
<ul>
<li><strong>Connections</strong> — See successful and failed connections over time, broken down by what is responsible: your origin (Bad Upstream), your configuration (Client), or Cloudflare (Internal).</li>
<li><strong>Latency</strong> — Track connection and DNS resolution latency trends.</li>
<li><strong>Errors</strong> — Drill into specific error codes grouped by category, with filters to isolate upstream, client, or internal failures.</li>
</ul>
<p>You can also view and edit your VPC Service configuration, host details, and port assignments from the <strong>Settings</strong> tab.</p>
<p>For a full list of error codes and what they mean, refer to <a href="/workers-vpc/reference/troubleshooting/">Troubleshooting</a>.</p>
</div></article></div>
