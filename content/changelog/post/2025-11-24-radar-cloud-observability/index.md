---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-11-24-radar-cloud-observability/
  description: New updates and improvements at Cloudflare.
  full_title: Cloud Services Observability in Cloudflare Radar · Changelog
  head_html: <title>Cloud Services Observability in Cloudflare Radar · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-11-24-radar-cloud-observability/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloud Services Observability in Cloudflare Radar · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-11-24-radar-cloud-observability/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-24-radar-cloud-observability/#page","headline":"Cloud Services Observability in Cloudflare Radar \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-11-24-radar-cloud-observability/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-11-24-radar-cloud-observability/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 24, 2025</time><h2 id="post-title">Cloud Services Observability in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> introduces HTTP Origins insights, providing visibility into the status of traffic between Cloudflare's global network and cloud-based origin infrastructure.</p>
<p>The new <a href="/api/resources/radar/subresources/origins/"><code>Origins</code></a> API provides provides the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/origins/methods/list/"><code>/origins</code></a> - Lists all origins (cloud providers and associated regions).</li>
<li><a href="/api/resources/radar/subresources/origins/methods/get/"><code>/origins/{origin}</code></a> - Retrieves information about a specific origin (cloud provider).</li>
<li><a href="/api/resources/radar/subresources/origins/methods/timeseries/"><code>/origins/timeseries</code></a> - Retrieves normalized time series data for a specific origin, including the following metrics:
<ul>
<li><code>REQUESTS</code>: Number of requests</li>
<li><code>CONNECTION_FAILURES</code>: Number of connection failures</li>
<li><code>RESPONSE_HEADER_RECEIVE_DURATION</code>: Duration of the response header receive</li>
<li><code>TCP_HANDSHAKE_DURATION</code>: Duration of the TCP handshake</li>
<li><code>TCP_RTT</code>: TCP round trip time</li>
<li><code>TLS_HANDSHAKE_DURATION</code>: Duration of the TLS handshake</li>
</ul>
</li>
<li><a href="/api/resources/radar/subresources/origins/methods/summary/"><code>/origins/summary</code></a> - Retrieves HTTP requests to origins summarized by a dimension.</li>
<li><a href="/api/resources/radar/subresources/origins/methods/timeseries_groups/"><code>/origins/timeseries_groups</code></a> - Retrieves timeseries data for HTTP requests to origins grouped by a dimension.</li>
</ul>
<p>The following dimensions are available for the <code>summary</code> and <code>timeseries_groups</code> endpoints:</p>
<ul>
<li><code>region</code>: Origin region</li>
<li><code>success_rate</code>: Success rate of requests (2XX versus 5XX response codes)</li>
<li><code>percentile</code>: Percentiles of metrics listed above</li>
</ul>
<p>Additionally, the <a href="/api/resources/radar/subresources/annotations/"><code>Annotations</code></a> and <a href="/api/resources/radar/subresources/traffic_anomalies/"><code>Traffic Anomalies</code></a> APIs have been extended to support origin outages and anomalies, enabling automated detection and alerting for origin infrastructure issues.</p>
<p><img src="/assets/upstream/images/radar/cloud-service-status.png" alt="Screenshot of the cloud service status heatmap" /></p>
<p>Check out the <a href="https://radar.cloudflare.com/cloud-observatory">new Radar page</a>.</p>
</div></article></div>
