---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/
  description: New updates and improvements at Cloudflare.
  full_title: RPKI ASPA Deployment Insights on Cloudflare Radar · Changelog
  head_html: <title>RPKI ASPA Deployment Insights on Cloudflare Radar · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="RPKI ASPA Deployment Insights on Cloudflare Radar · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/#page","headline":"RPKI ASPA Deployment Insights on Cloudflare Radar \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-25-radar-aspa-insights/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 25, 2026</time><h2 id="post-title">RPKI ASPA Deployment Insights on Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now includes <a href="https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/">Autonomous System Provider Authorization (ASPA)</a> deployment insights, providing visibility into the adoption and verification of ASPA objects across the global routing ecosystem.</p>
<h4 id="new-api-endpoints">New API endpoints</h4>
<p>The new <a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/"><code>ASPA</code></a> API provides the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot/"><code>/bgp/rpki/aspa/snapshot</code></a> - Retrieves current or historical ASPA objects.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/changes/"><code>/bgp/rpki/aspa/changes</code></a> - Retrieves changes to ASPA objects over time.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/timeseries/"><code>/bgp/rpki/aspa/timeseries</code></a> - Retrieves ASPA object counts over time as a timeseries.</li>
</ul>
<h4 id="new-radar-widgets">New Radar widgets</h4>
<p>The <a href="https://radar.cloudflare.com/routing">global routing page</a> now shows the ASPA deployment trend over time by counting daily ASPA objects.</p>
<p><img src="/assets/upstream/images/radar/aspa-global-trend.png" alt="Screenshot of the ASPA deployment trend chart" /></p>
<p>The global routing page also displays the most recent ASPA objects, searchable by ASN or AS name.</p>
<p><img src="/assets/upstream/images/radar/aspa-global-table.png" alt="Screenshot of the ASPA objects table" /></p>
<p>On country and region routing pages, a new widget shows the ASPA deployment rate for ASNs registered in the selected country or region.</p>
<p><img src="/assets/upstream/images/radar/aspa-germany-trend.png" alt="Screenshot of the ASPA deployment trent chart for Germany" /></p>
<p>On AS routing pages, the connectivity table now includes checkmarks for ASPA-verified upstreams. All ASPA upstreams are listed in a dedicated table, and a timeline shows ASPA changes at daily granularity.</p>
<p><img src="/assets/upstream/images/radar/aspa-asn-timeline.png" alt="Screenshot of the ASPA changes timeline on an AS routing page" /></p>
<p>Check out the <a href="https://radar.cloudflare.com/routing">Radar routing page</a> to explore the data.</p>
</div></article></div>
