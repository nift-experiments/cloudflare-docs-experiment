---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/
  description: New updates and improvements at Cloudflare.
  full_title: Billing is now enabled for R2 SQL · Changelog
  head_html: <title>Billing is now enabled for R2 SQL · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Billing is now enabled for R2 SQL · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/#page","headline":"Billing is now enabled for R2 SQL \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-03-r2-sql-billing-enabled/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 3, 2026</time><h2 id="post-title">Billing is now enabled for R2 SQL</h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p>Billing is now enabled for <a href="/r2-sql/">R2 SQL</a> on non-enterprise accounts. R2 SQL usage beyond the included free tier will appear on your next invoice.</p>
<p>R2 SQL charges based on a single dimension:</p>
<ul>
<li><strong>Data scanned</strong>: $0.0025 / GB ($2.50 / TB) of compressed data read from R2 to execute your query.</li>
</ul>
<p>All plans include 10 GB of data scanned per month. Each query is billed for a minimum of 10 MB of data scanned. R2 SQL pricing is additive to standard <a href="/r2/pricing/">R2 storage and operations</a> and <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges. R2 does not charge for egress, so there is no additional data transfer cost.</p>
<p>For example, a user who stores 500 GB of Parquet data in R2 Data Catalog and runs queries that scan a total of 50 GB of compressed data during the month would be billed as follows:</p>
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
<td>R2 storage</td>
<td>500 GB-month</td>
<td>10 GB-month</td>
<td>490 GB-month</td>
<td>$7.35</td>
</tr>
<tr>
<td>R2 SQL (data scanned)</td>
<td>50 GB</td>
<td>10 GB</td>
<td>40 GB</td>
<td>$0.10</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$7.45</strong></td>
</tr>
</tbody>
</table>
<p>For full pricing details and billing examples, refer to <a href="/r2-sql/platform/pricing/">R2 SQL pricing</a>.</p>
</div></article></div>
