---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/
  description: New updates and improvements at Cloudflare.
  full_title: Control where your Containers run with regional and jurisdictional placement · Changelog
  head_html: <title>Control where your Containers run with regional and jurisdictional placement · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Control where your Containers run with regional and jurisdictional placement · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/#page","headline":"Control where your Containers run with regional and jurisdictional placement \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-05-regional-placement/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 5, 2026</time><h2 id="post-title">Control where your Containers run with regional and jurisdictional placement</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>You can now specify placement constraints to control where your <a href="/containers/">Containers</a> run.</p>
<table>
<thead>
<tr>
<th>Constraint</th>
<th>Values</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>regions</code></td>
<td><code>ENAM</code>, <code>WNAM</code>, <code>EEUR</code>, <code>WEUR</code></td>
<td>Geographic placement</td>
</tr>
<tr>
<td><code>jurisdiction</code></td>
<td><code>eu</code>, <code>fedramp</code></td>
<td>Compliance boundaries</td>
</tr>
</tbody>
</table>
<p>Use <code>regions</code> to limit placement to specific geographic areas. Use <code>jurisdiction</code> to restrict containers to compliance boundaries — <code>eu</code> maps to European regions (EEUR, WEUR) and <code>fedramp</code> maps to North American regions (ENAM, WNAM).</p>
<p>Refer to <a href="/containers/concepts/placement/">Containers placement</a> for more details.</p>
</div></article></div>
