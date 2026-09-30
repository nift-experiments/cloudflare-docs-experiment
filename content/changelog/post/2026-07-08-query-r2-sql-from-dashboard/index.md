---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-07-08-query-r2-sql-from-dashboard/
  description: New updates and improvements at Cloudflare.
  full_title: Query R2 Data Catalog tables with R2 SQL from the dashboard · Changelog
  head_html: <title>Query R2 Data Catalog tables with R2 SQL from the dashboard · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-07-08-query-r2-sql-from-dashboard/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Query R2 Data Catalog tables with R2 SQL from the dashboard · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-07-08-query-r2-sql-from-dashboard/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-08-query-r2-sql-from-dashboard/#page","headline":"Query R2 Data Catalog tables with R2 SQL from the dashboard \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-07-08-query-r2-sql-from-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-07-08-query-r2-sql-from-dashboard/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 8, 2026</time><h2 id="post-title">Query R2 Data Catalog tables with R2 SQL from the dashboard</h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p>You can now query your <a href="/r2-data-catalog/">R2 Data Catalog</a> tables with <a href="/r2-sql/">R2 SQL</a> directly from the Cloudflare dashboard, without installing a CLI or wiring up a client. This makes it easy to explore your <a href="https://iceberg.apache.org/">Apache Iceberg</a> data, validate queries, and inspect results in one place.</p>
<img src="/assets/upstream/images/r2-sql/r2-sql-studio.png" alt="R2 SQL Query Editor" />
<p>To get started, go to <a href="https://dash.cloudflare.com/?to=/:account/data-catalog/overview">R2 Data Catalog</a> in the Cloudflare dashboard and select <strong>Query data</strong> to launch the built-in SQL editor. From there you can:</p>
<ul>
<li><strong>Write and run queries interactively</strong> — Iterate on R2 SQL directly in the browser with syntax highlighting and autocomplete, instead of re-running commands through Wrangler or the REST API.</li>
<li><strong>Explore your data</strong> — Explore your namespaces and tables alongside the editor so you can discover what's queryable without leaving the page or using other tools.</li>
<li><strong>Understand results and performance</strong> — View result sets with per-query statistics, export them, and get helpful <code>EXPLAIN</code> outputs to see exactly how a query runs.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17743.md")</aside>
</div></article></div>
