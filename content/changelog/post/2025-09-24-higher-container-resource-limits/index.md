---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/
  description: New updates and improvements at Cloudflare.
  full_title: Run more Containers with higher resource limits · Changelog
  head_html: <title>Run more Containers with higher resource limits · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Run more Containers with higher resource limits · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/#page","headline":"Run more Containers with higher resource limits \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-24-higher-container-resource-limits/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 25, 2025</time><h2 id="post-title">Run more Containers with higher resource limits</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>You can now run more Containers concurrently with higher limits on CPU, memory, and disk.</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>New Limit</th>
<th>Previous Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Memory for concurrent live Container instances</td>
<td>400GiB</td>
<td>40GiB</td>
</tr>
<tr>
<td>vCPU for concurrent live Container instances</td>
<td>100</td>
<td>20</td>
</tr>
<tr>
<td>Disk for concurrent live Container instances</td>
<td>2TB</td>
<td>100GB</td>
</tr>
</tbody>
</table>
<p>You can now run 1000 instances of the <code>dev</code> instance type, 400 instances of <code>basic</code>, or 100 instances of <code>standard</code> concurrently.</p>
<p>This opens up new possibilities for running larger-scale workloads on Containers.</p>
<p>See the <a href="/containers/get-started/">getting started guide</a> to deploy your first Container,
and the <a href="/containers/platform/limits/">limits documentation</a> for more details on the available instance types and limits.</p>
</div></article></div>
