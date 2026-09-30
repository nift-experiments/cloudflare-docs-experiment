---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-10-01-new-container-instance-types/
  description: New updates and improvements at Cloudflare.
  full_title: Larger Container instance types · Changelog
  head_html: <title>Larger Container instance types · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-10-01-new-container-instance-types/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Larger Container instance types · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-10-01-new-container-instance-types/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-01-new-container-instance-types/#page","headline":"Larger Container instance types \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-10-01-new-container-instance-types/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-10-01-new-container-instance-types/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 1, 2025</time><h2 id="post-title">Larger Container instance types</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>New instance types provide up to 4 vCPU, 12 GiB of memory, and 20 GB of disk per container instance.</p>
<table>
<thead>
<tr>
<th>Instance Type</th>
<th>vCPU</th>
<th>Memory</th>
<th>Disk</th>
</tr>
</thead>
<tbody>
<tr>
<td>lite</td>
<td>1/16</td>
<td>256 MiB</td>
<td>2 GB</td>
</tr>
<tr>
<td>basic</td>
<td>1/4</td>
<td>1 GiB</td>
<td>4 GB</td>
</tr>
<tr>
<td>standard-1</td>
<td>1/2</td>
<td>4 GiB</td>
<td>8 GB</td>
</tr>
<tr>
<td>standard-2</td>
<td>1</td>
<td>6 GiB</td>
<td>12 GB</td>
</tr>
<tr>
<td>standard-3</td>
<td>2</td>
<td>8 GiB</td>
<td>16 GB</td>
</tr>
<tr>
<td>standard-4</td>
<td>4</td>
<td>12 GiB</td>
<td>20 GB</td>
</tr>
</tbody>
</table>
<p>The <code>dev</code> and <code>standard</code> instance types are preserved for backward compatibility and are aliases for <code>lite</code> and <code>standard-1</code>, respectively. The <code>standard-1</code> instance type now provides up to 8 GB of disk instead of only 4 GB.</p>
<p>See the <a href="/containers/get-started/">getting started guide</a> to deploy your first Container,
and the <a href="/containers/platform/limits/">limits documentation</a> for more details on the available instance types and limits.</p>
</div></article></div>
