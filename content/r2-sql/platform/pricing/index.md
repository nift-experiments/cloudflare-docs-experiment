---
cp9:
  canonical: https://developers.cloudflare.com/r2-sql/platform/pricing/
  description: R2 SQL pricing based on data scanned, with included usage details and billing examples.
  full_title: R2 SQL - Pricing · R2 SQL docs
  head_html: <title>R2 SQL - Pricing · R2 SQL docs</title><meta name="generator" content="Nift"><meta name="description" content="R2 SQL pricing based on data scanned, with included usage details and billing examples."><link rel="canonical" href="https://developers.cloudflare.com/r2-sql/platform/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2-sql/platform/pricing/index.md"><meta property="og:title" content="R2 SQL - Pricing · R2 SQL docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="R2 SQL pricing based on data scanned, with included usage details and billing examples."><meta property="og:url" content="https://developers.cloudflare.com/r2-sql/platform/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2 SQL"><meta name="algolia_product_filter" content="R2 SQL"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="R2 SQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2-sql/platform/pricing/#page","headline":"R2 SQL - Pricing \u00b7 R2 SQL docs","description":"R2 SQL pricing based on data scanned, with included usage details and billing examples.","url":"https://developers.cloudflare.com/r2-sql/platform/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2-sql/platform/pricing/
  schema: 1
---
<p>R2 SQL charges based on a single dimension:</p>
<ul>
<li><strong>Data scanned</strong>: The volume of compressed data read from R2 to execute your query.</li>
</ul>
<p>R2 SQL pricing is additive to standard <a href="/r2/pricing/">R2 storage and operations</a> and <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges. When the query engine reads files, those requests count as R2 Class B (read) operations. R2 does not charge for egress, so there is no additional data transfer cost.</p>
<p>All included usage is on a monthly basis.</p>
<h2 id="r2-sql-pricing">R2 SQL pricing</h2>
<table>
<thead>
<tr>
<th></th>
<th>Pricing</th>
</tr>
</thead>
<tbody>
<tr>
<td>Included</td>
<td>10 GB / month</td>
</tr>
<tr>
<td>Data scanned</td>
<td>$0.0025 / GB ($2.50 / TB)</td>
</tr>
</tbody>
</table>
<h3 id="what-counts-as-data-scanned">What counts as data scanned</h3>
<p>Data scanned is the compressed bytes read from R2 object storage to answer your query. This matches what you see in your R2 bucket — if a Parquet file is 100 MB on disk, scanning that file bills for 100 MB.</p>
<ul>
<li><strong>Minimum per query</strong>: 10 MB. If a query scans less than 10 MB, you are billed for 10 MB.</li>
<li><strong>Failed queries</strong>: Queries that fail due to a system error or syntax error caught before execution are not charged. Queries that fail mid-execution due to a runtime error are also not charged.</li>
<li><strong>Metadata-only operations</strong>: Operations such as <code>EXPLAIN</code>, <code>SHOW</code>, and <code>DESCRIBE</code> do not scan data and are free. Standard R2 and R2 Data Catalog request charges still apply.</li>
</ul>
<h2 id="billing-examples">Billing examples</h2>
<h3 id="example-1-ad-hoc-analytics-on-500-gb-of-parquet-data">Example 1: Ad-hoc analytics on 500 GB of Parquet data</h3>
<p>A user stores 500 GB of Parquet data in R2 Data Catalog and runs queries that scan a total of 50 GB of compressed data during the month.</p>
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
<h3 id="example-2-heavy-query-workload-on-10-tb-dataset">Example 2: Heavy query workload on 10 TB dataset</h3>
<p>A data team stores 10 TB of compressed Parquet/Iceberg data and scans 50 TB of data per month across their queries. The team also makes 2 million catalog operations with compaction processing 500 GB.</p>
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
<td>10,000 GB-month</td>
<td>10 GB-month</td>
<td>9,990 GB-month</td>
<td>$149.85</td>
</tr>
<tr>
<td>R2 SQL (data scanned)</td>
<td>50,000 GB</td>
<td>10 GB</td>
<td>49,990 GB</td>
<td>$124.98</td>
</tr>
<tr>
<td>R2 Data Catalog operations</td>
<td>2,000,000</td>
<td>1,000,000</td>
<td>1,000,000</td>
<td>$9.00</td>
</tr>
<tr>
<td>R2 Data Catalog compaction (data)</td>
<td>500 GB</td>
<td>10 GB</td>
<td>490 GB</td>
<td>$2.45</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$286.28</strong></td>
</tr>
</tbody>
</table>
<h2 id="frequently-asked-questions">Frequently asked questions</h2>
<h3 id="is-there-a-minimum-billing-increment-per-query">Is there a minimum billing increment per query?</h3>
<p>Yes. Each query is billed for a minimum of 10 MB of data scanned. This covers the overhead of initializing the query engine.</p>
<h3 id="does-data-scanned-include-r2-egress-fees">Does data scanned include R2 egress fees?</h3>
<p>No. R2 does not charge for egress. The query engine runs within the Cloudflare network adjacent to R2 storage, so there are no data transfer costs.</p>
<h2 id="cloudflare-billing-policy">Cloudflare billing policy</h2>
<p>To learn more about how usage is billed, refer to <a href="/billing/understand/billing-policy/">Cloudflare Billing Policy</a>.</p>
