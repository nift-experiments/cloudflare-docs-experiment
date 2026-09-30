---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/
  description: New updates and improvements at Cloudflare.
  full_title: Increased concurrency, creation rate, and queued instance limits for Workflows instances · Changelog
  head_html: <title>Increased concurrency, creation rate, and queued instance limits for Workflows instances · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Increased concurrency, creation rate, and queued instance limits for Workflows instances · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/#page","headline":"Increased concurrency, creation rate, and queued instance limits for Workflows instances \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-15-workflows-limits-raised/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 15, 2026</time><h2 id="post-title">Increased concurrency, creation rate, and queued instance limits for Workflows instances</h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> limits have been raised to the following:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Previous</th>
<th>New</th>
</tr>
</thead>
<tbody>
<tr>
<td>Concurrent instances (running in parallel)</td>
<td>10,000</td>
<td>50,000</td>
</tr>
<tr>
<td>Instance creation rate (per account)</td>
<td>100/second per account</td>
<td>300/second per account, 100/second per workflow</td>
</tr>
<tr>
<td>Queued instances per Workflow <sup><a href="#footnote-1">1</a></sup></td>
<td>1 million</td>
<td>2 million</td>
</tr>
</tbody>
</table>
<p>These increases apply to all users on the <a href="/workers/platform/pricing/">Workers Paid plan</a>. Refer to the <a href="/workflows/reference/limits/">Workflows limits documentation</a> for more details.</p>
<section class="footnotes"><h4 id="footnotes">Footnotes</h4><ol><li id="footnote-1">Queued instances are instances that have been created or awoken and are waiting for a concurrency slot.</li></ol></section>
</div></article></div>
