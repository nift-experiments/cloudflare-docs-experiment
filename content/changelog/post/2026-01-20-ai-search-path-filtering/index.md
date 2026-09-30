---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/
  description: New updates and improvements at Cloudflare.
  full_title: AI Search path filtering for website and R2 data sources · Changelog
  head_html: <title>AI Search path filtering for website and R2 data sources · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="AI Search path filtering for website and R2 data sources · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/#page","headline":"AI Search path filtering for website and R2 data sources \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-01-20-ai-search-path-filtering/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 20, 2026</time><h2 id="post-title">AI Search path filtering for website and R2 data sources</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now includes <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a> for both <a href="/ai-search/configuration/data-source/website/#path-filtering">website</a> and <a href="/ai-search/configuration/data-source/r2/#path-filtering">R2</a> data sources. You can now control which content gets indexed by defining include and exclude rules for paths.</p>
<p>By controlling what gets indexed, you can improve the relevance and quality of your search results. You can also use path filtering to split a single data source across multiple AI Search instances for specialized search experiences.</p>
<p><img src="/assets/upstream/images/ai-search/path-filtering.png" alt="Path filtering configuration in AI Search" /></p>
<p>Path filtering uses <a href="https://github.com/micromatch/micromatch">micromatch</a> patterns, so you can use <code>*</code> to match within a directory and <code>**</code> to match across directories.</p>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Include</th>
<th>Exclude</th>
</tr>
</thead>
<tbody>
<tr>
<td>Index docs but skip drafts</td>
<td><code>**/docs/**</code></td>
<td><code>**/docs/drafts/**</code></td>
</tr>
<tr>
<td>Keep admin pages out of results</td>
<td>—</td>
<td><code>**/admin/**</code></td>
</tr>
<tr>
<td>Index only English content</td>
<td><code>**/en/**</code></td>
<td>—</td>
</tr>
</tbody>
</table>
<p>Configure path filters when creating a new instance or update them anytime from <strong>Settings</strong>. Check out <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a> to learn more.</p>
</div></article></div>
