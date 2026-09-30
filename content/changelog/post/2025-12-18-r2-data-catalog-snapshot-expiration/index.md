---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/
  description: New updates and improvements at Cloudflare.
  full_title: R2 Data Catalog now supports automatic snapshot expiration · Changelog
  head_html: <title>R2 Data Catalog now supports automatic snapshot expiration · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="R2 Data Catalog now supports automatic snapshot expiration · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/#page","headline":"R2 Data Catalog now supports automatic snapshot expiration \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 18, 2025</time><h2 id="post-title">R2 Data Catalog now supports automatic snapshot expiration</h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p><a href="/r2-data-catalog/">R2 Data Catalog</a> now supports automatic snapshot expiration for Apache Iceberg tables.</p>
<p>In Apache Iceberg, a snapshot is metadata that represents the state of a table at a given point in time. Every mutation creates a new snapshot which enable powerful features like time travel queries and rollback capabilities but will accumulate over time.</p>
<p>Without regular cleanup, these accumulated snapshots can lead to:</p>
<ul>
<li>Metadata overhead</li>
<li>Slower table operations</li>
<li>Increased storage costs.</li>
</ul>
<p>Snapshot expiration in R2 Data Catalog automatically removes old table snapshots based on your configured retention policy, improving performance and storage costs.</p>
<pre tabindex="0"><code class="language-bash">&#35; Enable catalog-level snapshot expiration&#10;&#35; Expire snapshots older than 7 days, always retain at least 10 recent snapshots&#10;npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \&#10;  &#45;-older-than-days 7 \&#10;  &#45;-retain-last 10&#10;</code></pre>
<p>Snapshot expiration uses two parameters to determine which snapshots to remove:</p>
<ul>
<li><code>--older-than-days</code>: age threshold in days</li>
<li><code>--retain-last</code>: minimum snapshot count to retain</li>
</ul>
<p>Both conditions must be met before a snapshot is expired, ensuring you always retain recent snapshots even if they exceed the age threshold.</p>
<p>This feature complements <a href="/r2-data-catalog/table-maintenance/">automatic compaction</a>, which optimizes query performance by combining small data files into larger ones. Together, these automatic maintenance operations keep your Iceberg tables performant and cost-efficient without manual intervention.</p>
<p>For more information, refer to <a href="/r2-data-catalog/table-maintenance/">Table maintenance</a> or <a href="/r2-data-catalog/manage-catalogs/">Manage catalogs</a>.</p>
</div></article></div>
