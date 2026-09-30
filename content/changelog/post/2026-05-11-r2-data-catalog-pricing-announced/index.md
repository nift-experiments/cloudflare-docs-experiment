---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/
  description: New updates and improvements at Cloudflare.
  full_title: R2 Data Catalog pricing announced · Changelog
  head_html: <title>R2 Data Catalog pricing announced · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="R2 Data Catalog pricing announced · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/#page","headline":"R2 Data Catalog pricing announced \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-11-r2-data-catalog-pricing-announced/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 28, 2026</time><h2 id="post-title">R2 Data Catalog pricing announced</h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> data catalog built directly into R2 buckets, queryable by any Iceberg-compatible engine such as Spark, Snowflake, and DuckDB. R2 Data Catalog now has published pricing for catalog operations and table compaction, in addition to standard <a href="/r2/pricing/">R2 storage and operations</a>.</p>
<p>Billing is not yet enabled. We will provide at least 30 days notice before we start charging for R2 Data Catalog usage.</p>
<p>Pricing is based on two dimensions:</p>
<ul>
<li><strong>Catalog operations</strong>: $9.00 / million operations for metadata requests such as creating tables, reading table metadata, and updating table properties.</li>
<li><strong>Compaction</strong>: $0.005 / GB processed and $2.00 / million objects processed. These charges only apply when automatic compaction is turned on for a table.</li>
</ul>
<p>Both dimensions include a monthly free tier: 1 million catalog operations, 10 GB of compaction data processed, and 1 million compaction objects processed.</p>
<p>For full pricing details and billing examples, refer to <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog pricing</a>.</p>
</div></article></div>
