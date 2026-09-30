---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/
  description: New updates and improvements at Cloudflare.
  full_title: Regional Data in Cloudflare Radar · Changelog
  head_html: <title>Regional Data in Cloudflare Radar · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Regional Data in Cloudflare Radar · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/#page","headline":"Regional Data in Cloudflare Radar \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-29-radar-regional-data/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 29, 2025</time><h2 id="post-title">Regional Data in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now introduces Regional Data, providing traffic insights that bring a more localized perspective to the traffic trends shown on Radar.</p>
<p>The following API endpoints are now available:</p>
<ul>
<li><a href="/api/resources/radar/subresources/geolocations/methods/get/"><code>Get Geolocation</code></a> - Retrieves geolocation by <code>geoId</code>.</li>
<li><a href="/api/resources/radar/subresources/geolocations/methods/list/"><code>List Geolocations</code></a> - Lists geolocations.</li>
<li><a href="/api/resources/radar/subresources/netflows/methods/summary_v2/"><code>NetFlows Summary By Dimension</code></a> - Retrieves NetFlows summary by dimension.</li>
</ul>
<p>All <code>summary</code> and <code>timeseries_groups</code> endpoints in <a href="/api/resources/radar/subresources/http/"><code>HTTP</code></a> and <a href="/api/resources/radar/subresources/netflows/"><code>NetFlows</code></a> now include an <code>adm1</code> dimension for grouping data by first level administrative division (for example, state, province, etc.)</p>
<p>A new filter <code>geoId</code> was also added to all endpoints in <a href="/api/resources/radar/subresources/http/"><code>HTTP</code></a> and <a href="/api/resources/radar/subresources/netflows/"><code>NetFlows</code></a>, allowing filtering by a specific administrative division.</p>
<p>Check out the new Regional traffic insights on a country specific traffic page <a href="https://radar.cloudflare.com/traffic/pt">new Radar page</a>.</p>
</div></article></div>
