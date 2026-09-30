---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/
  description: New updates and improvements at Cloudflare.
  full_title: D1 enforces free tier daily query limits · Changelog
  head_html: <title>D1 enforces free tier daily query limits · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="D1 enforces free tier daily query limits · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/#page","headline":"D1 enforces free tier daily query limits \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-09-01-d1-free-tier-limit-enforcement/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 1, 2026</time><h2 id="post-title">D1 enforces free tier daily query limits</h2>
<div class="changelog-badges"><span>d1</span></div><div class="changelog-body"><p>Beginning September 1, 2026, D1 queries on the <a href="/workers/platform/pricing/#workers">Workers Free plan</a> will fail when an account exceeds the daily <a href="/d1/platform/pricing/">row read or row write limits</a>. Queries via the <a href="/d1/worker-api/">Workers Binding API</a> and the <a href="/d1/rest-api/">REST API</a> will return errors until the limit resets at midnight UTC. Stored data is not affected.</p>
<p>You will receive email alerts when the daily limit is reached. The following errors indicate that a limit has been exceeded:</p>
<table>
<thead>
<tr>
<th>Error</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Your account has exceeded D1's free tier daily row read limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue.</td>
<td>The account has reached its daily row read limit.</td>
</tr>
<tr>
<td>Your account has exceeded D1's free tier daily row write limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue.</td>
<td>The account has reached its daily row write limit.</td>
</tr>
</tbody>
</table>
<p>Inspect database query activity before the enforcement date to identify queries that may exceed these limits. To reduce row reads, add <a href="/d1/best-practices/use-indexes/">indexes</a> to tables and review queries that perform full table scans. If usage requires higher limits after optimization, upgrade to a <a href="/workers/platform/pricing/#workers">Workers Paid plan</a>.</p>
<p>For more information on D1 errors and how to handle them, refer to the <a href="/d1/observability/debug-d1/#error-list">D1 error list</a>.</p>
</div></article></div>
