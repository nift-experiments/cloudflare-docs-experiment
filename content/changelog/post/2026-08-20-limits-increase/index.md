---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/
  description: New updates and improvements at Cloudflare.
  full_title: Run more headless browsers concurrently with Browser Run · Changelog
  head_html: <title>Run more headless browsers concurrently with Browser Run · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Run more headless browsers concurrently with Browser Run · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/#page","headline":"Run more headless browsers concurrently with Browser Run \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-20-limits-increase/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 20, 2026</time><h2 id="post-title">Run more headless browsers concurrently with Browser Run</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Run</a> lets you automate headless browsers on Cloudflare's global network. Run full browser sessions for interactive workflows, or use <a href="/browser-run/quick-actions/">Quick Actions</a> for one-request tasks such as screenshots, PDFs, and capturing page content.</p>
<p>If you are on the <a href="/workers/platform/pricing/">Workers Paid plan</a>, your default <a href="/browser-run/limits/#workers-paid">limits</a> are now higher:</p>
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
<td>Concurrent browsers</td>
<td>120</td>
<td><strong>200</strong></td>
</tr>
<tr>
<td>New browser instances / second</td>
<td>1</td>
<td><strong>3</strong></td>
</tr>
<tr>
<td>Quick Actions requests / second</td>
<td>10</td>
<td><strong>30</strong></td>
</tr>
</tbody>
</table>
<p>You can now run hundreds of browser sessions in parallel, launch new browsers faster, and process three times as many <a href="/browser-run/quick-actions/">Quick Actions</a> per second. These published limits are defaults, not maximums. If your workload needs more more concurrent browsers, <a href="https://forms.gle/CdueDKvb26mTaepa9">request higher limits</a>.</p>
</div></article></div>
