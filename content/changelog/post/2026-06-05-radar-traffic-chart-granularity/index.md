---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-05-radar-traffic-chart-granularity/
  description: New updates and improvements at Cloudflare.
  full_title: Finer-grained chart granularity on Cloudflare Radar for longer time ranges · Changelog
  head_html: <title>Finer-grained chart granularity on Cloudflare Radar for longer time ranges · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-05-radar-traffic-chart-granularity/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Finer-grained chart granularity on Cloudflare Radar for longer time ranges · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-05-radar-traffic-chart-granularity/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-05-radar-traffic-chart-granularity/#page","headline":"Finer-grained chart granularity on Cloudflare Radar for longer time ranges \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-05-radar-traffic-chart-granularity/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-05-radar-traffic-chart-granularity/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 5, 2026</time><h2 id="post-title">Finer-grained chart granularity on Cloudflare Radar for longer time ranges</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now provides finer-grained traffic charts for longer time ranges. Previously, selecting a 1-3 month view on HTTP and NetFlows charts defaulted to weekly aggregation, which was too coarse to surface meaningful trends. Views longer than 3 months defaulted to monthly aggregation, returning as few as 7 data points for a 6-month range.</p>
<p>The new defaults are:</p>
<ul>
<li><strong>1-3 months</strong>: daily granularity (7x more data points)</li>
<li><strong>Longer than 3 months</strong> (HTTP and NetFlows): weekly granularity (4x more data points)</li>
</ul>
<p>For example, a 12-week traffic view previously showed weekly data:</p>
<p><img src="/assets/upstream/images/radar/traffic-granularity-12w-before.png" alt="Traffic trends chart with weekly granularity for a 12-week view" /></p>
<p>The same view now shows daily data:</p>
<p><img src="/assets/upstream/images/radar/traffic-granularity-12w-after.png" alt="Traffic trends chart with daily granularity for a 12-week view" /></p>
<p>Similarly, a 1-year HTTP traffic view that previously showed just 12 monthly data points now provides 52 weekly data points.</p>
<p>Visit <a href="https://radar.cloudflare.com/?dateRange=12w#traffic-trends">Cloudflare Radar</a> to explore the new granular views.</p>
</div></article></div>
