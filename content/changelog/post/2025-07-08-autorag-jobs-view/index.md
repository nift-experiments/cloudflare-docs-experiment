---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-07-08-autorag-jobs-view/
  description: New updates and improvements at Cloudflare.
  full_title: Faster indexing and new Jobs view in AutoRAG · Changelog
  head_html: <title>Faster indexing and new Jobs view in AutoRAG · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-07-08-autorag-jobs-view/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Faster indexing and new Jobs view in AutoRAG · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-07-08-autorag-jobs-view/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-08-autorag-jobs-view/#page","headline":"Faster indexing and new Jobs view in AutoRAG \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-07-08-autorag-jobs-view/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-07-08-autorag-jobs-view/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 8, 2025</time><h2 id="post-title">Faster indexing and new Jobs view in AutoRAG</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>You can now expect <strong>3-5× faster indexing</strong> in AutoRAG, and with it, a brand new <strong>Jobs view</strong> to help you monitor indexing progress.</p>
<p>With each AutoRAG, indexing jobs are automatically triggered to sync your data source (i.e. R2 bucket) with your Vectorize index, ensuring new or updated files are reflected in your query results. You can also trigger jobs manually via the <a href="/api/resources/ai-search/subresources/rags/">Sync API</a> or by clicking “Sync index” in the dashboard.</p>
<p>With the new jobs observability, you can now:</p>
<ul>
<li>View the status, job ID, source, start time, duration and last sync time for each indexing job</li>
<li>Inspect real-time logs of job events (e.g. <code>Starting indexing data source...</code>)</li>
<li>See a history of past indexing jobs under the Jobs tab of your AutoRAG</li>
</ul>
<p>This makes it easier to understand what’s happening behind the scenes.</p>
<p><strong>Coming soon:</strong> We’re adding APIs to programmatically check indexing status, making it even easier to integrate AutoRAG into your workflows.</p>
<p>Try it out today on the <a href="https://dash.cloudflare.com/?to=/:account/ai/autorag">Cloudflare dashboard</a>.</p>
</div></article></div>
