---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/
  description: New updates and improvements at Cloudflare.
  full_title: Billing is now enabled for R2 Data Catalog · Changelog
  head_html: <title>Billing is now enabled for R2 Data Catalog · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Billing is now enabled for R2 Data Catalog · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/#page","headline":"Billing is now enabled for R2 Data Catalog \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-03-r2-data-catalog-billing-enabled/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 3, 2026</time><h2 id="post-title">Billing is now enabled for R2 Data Catalog</h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p>Billing is now enabled for <a href="/r2-data-catalog/">R2 Data Catalog</a> on non-enterprise accounts. R2 Data Catalog usage beyond the included free tier will appear on your next invoice.</p>
<p>R2 Data Catalog charges based on two dimensions, in addition to standard <a href="/r2/pricing/">R2 storage and operations</a>:</p>
<ul>
<li><strong>Catalog operations</strong>: $9.00 / million operations for metadata requests such as creating tables, reading table metadata, and updating table properties.</li>
<li><strong>Compaction</strong>: $0.005 / GB processed and $2.00 / million objects processed. These charges only apply when <a href="/r2-data-catalog/table-maintenance/">automatic compaction</a> is turned on for a table.</li>
</ul>
<p>Each dimension includes a monthly free tier: 1 million catalog operations, 10 GB of compaction data processed, and 1 million compaction objects processed.</p>
<p>For example, a single Iceberg table with 50 GB of data, 500,000 catalog operations per month, and compaction turned on that processes 20 GB across 200,000 files would be billed as follows:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Usage</th>
<th>Included</th>
<th>Billable</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>Catalog operations</td>
<td>500,000</td>
<td>1,000,000</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td>Compaction (data processed)</td>
<td>20 GB</td>
<td>10 GB</td>
<td>10 GB</td>
<td>$0.05</td>
</tr>
<tr>
<td>Compaction (objects)</td>
<td>200,000</td>
<td>1,000,000</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td><strong>Total (Data Catalog)</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$0.05</strong></td>
</tr>
</tbody>
</table>
<p>Standard R2 storage charges ($0.015 / GB-month) apply separately for the 50 GB of data stored.</p>
<p>For full pricing details and billing examples, refer to <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog pricing</a>.</p>
</div></article></div>
