---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-12-08-python-cold-start-improvements/
  description: New updates and improvements at Cloudflare.
  full_title: Python cold start improvements · Changelog
  head_html: <title>Python cold start improvements · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-12-08-python-cold-start-improvements/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Python cold start improvements · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-12-08-python-cold-start-improvements/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-08-python-cold-start-improvements/#page","headline":"Python cold start improvements \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-12-08-python-cold-start-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-12-08-python-cold-start-improvements/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 8, 2025</time><h2 id="post-title">Python cold start improvements</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Python Workers now feature improved cold start performance, reducing initialization time for new Worker instances.
This improvement is particularly noticeable for Workers with larger dependency sets or complex initialization logic.</p>
<p>Every time you deploy a Python Worker, a memory snapshot is captured after the top level of the Worker is executed.
This snapshot captures all imports, including package imports that are often costly to load. The memory snapshot is loaded
when the Worker is first started, avoiding the need to reload the Python runtime and all dependencies on each cold start.</p>
<p>We set up a benchmark that imports common packages (<a href="https://www.python-httpx.org/">httpx</a>,
<a href="https://fastapi.tiangolo.com/">fastapi</a> and <a href="https://docs.pydantic.dev/latest/">pydantic</a>)
to see how Python Workers stack up against other platforms:</p>
<table>
<thead>
<tr>
<th>Platform</th>
<th>Mean Cold Start (ms)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Python Workers</td>
<td>1027</td>
</tr>
<tr>
<td>AWS Lambda</td>
<td>2502</td>
</tr>
<tr>
<td>Google Cloud Run</td>
<td>3069</td>
</tr>
</tbody>
</table>
<p>These benchmarks run continuously. You can view the results and the methodology on our <a href="https://cold.edgeworker.net">benchmark page</a>.</p>
<p>In additional testing, we have found that without any memory snapshot, the cold start for this benchmark takes around 10 seconds, so this change improves cold start performance by roughly a factor of 10.</p>
<p>To get started with Python Workers, check out our <a href="/workers/languages/python/">Python Workers overview</a>.</p>
</div></article></div>
