---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/
  description: New updates and improvements at Cloudflare.
  full_title: Billing is now enabled for Pipelines · Changelog
  head_html: <title>Billing is now enabled for Pipelines · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Billing is now enabled for Pipelines · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/#page","headline":"Billing is now enabled for Pipelines \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-03-pipelines-billing-enabled/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 3, 2026</time><h2 id="post-title">Billing is now enabled for Pipelines</h2>
<div class="changelog-badges"><span>pipelines</span></div><div class="changelog-body"><p>Billing is now enabled for <a href="/pipelines/">Cloudflare Pipelines</a> on non-enterprise accounts. Pipelines usage beyond the included free tier will appear on your next invoice.</p>
<p>Pipelines charges based on two usage dimensions. Ingress into a Pipeline stream remains free regardless of volume:</p>
<ul>
<li><strong>SQL transforms</strong>: $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).</li>
<li><strong>Sinks (egress)</strong>: $0.03 / GB for JSON output, $0.06 / GB for Parquet or Iceberg output.</li>
</ul>
<p>Workers Paid plans include 50 GB / month for both SQL transforms and sinks. Standard <a href="/r2/pricing/">R2 storage and operations</a> charges apply for data written to R2 buckets, and <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges apply when writing to Iceberg tables.</p>
<p>For example, a pipeline that ingests 500 GB of event data per month, uses a SQL transform to filter and reshape it, and writes 300 GB to an R2 Data Catalog Iceberg table would be billed as follows:</p>
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
<td>Streams</td>
<td>500 GB</td>
<td>Unlimited</td>
<td>0 GB</td>
<td>$0.00</td>
</tr>
<tr>
<td>SQL transforms</td>
<td>500 GB</td>
<td>50 GB</td>
<td>450 GB</td>
<td>$18.00</td>
</tr>
<tr>
<td>Sinks (Iceberg)</td>
<td>300 GB</td>
<td>50 GB</td>
<td>250 GB</td>
<td>$15.00</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$33.00</strong></td>
</tr>
</tbody>
</table>
<p>For full pricing details and billing examples, refer to <a href="/pipelines/platform/pricing/">Pipelines pricing</a>.</p>
</div></article></div>
