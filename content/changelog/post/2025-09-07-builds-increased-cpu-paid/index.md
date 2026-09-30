---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/
  description: New updates and improvements at Cloudflare.
  full_title: Increased vCPU for Workers Builds on paid plans · Changelog
  head_html: <title>Increased vCPU for Workers Builds on paid plans · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Increased vCPU for Workers Builds on paid plans · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/#page","headline":"Increased vCPU for Workers Builds on paid plans \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-07-builds-increased-cpu-paid/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 18, 2025</time><h2 id="post-title">Increased vCPU for Workers Builds on paid plans</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We recently <a href="/changelog/2025-08-04-builds-increased-disk-size/">increased the available disk space</a> from 8 GB to 20 GB for <strong>all</strong> plans. Building on that improvement, we’re now doubling the CPU power available for paid plans — from 2 vCPU to <strong>4 vCPU</strong>.</p>
<p>These changes continue our focus on making <a href="/workers/ci-cd/builds/">Workers Builds</a> faster and more reliable.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Free Plan</th>
<th>Paid Plans</th>
</tr>
</thead>
<tbody>
<tr>
<td>CPU</td>
<td>2 vCPU</td>
<td><strong>4 vCPU</strong></td>
</tr>
</tbody>
</table>
<h4 id="performance-improvements">Performance Improvements</h4>
- **Fast build times**: Even single-threaded workloads benefit from having more vCPUs 
- **2x faster multi-threaded builds**: Tools like [esbuild](https://esbuild.github.io/) and [webpack](https://webpack.js.org/) can now utilize additional cores, delivering near-linear performance scaling
<p>All other <a href="/workers/ci-cd/builds/limits-and-pricing/">build limits</a> — including memory, build minutes, and timeout remain unchanged.</p>
</div></article></div>
