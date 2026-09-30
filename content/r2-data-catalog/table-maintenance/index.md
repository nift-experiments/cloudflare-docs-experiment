---
cp9:
  canonical: https://developers.cloudflare.com/r2-data-catalog/table-maintenance/
  description: Learn how R2 Data Catalog automates table maintenance
  full_title: Table maintenance · Cloudflare R2 Data Catalog docs
  head_html: <title>Table maintenance · Cloudflare R2 Data Catalog docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how R2 Data Catalog automates table maintenance"><link rel="canonical" href="https://developers.cloudflare.com/r2-data-catalog/table-maintenance/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2-data-catalog/table-maintenance/index.md"><meta property="og:title" content="Table maintenance · Cloudflare R2 Data Catalog docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how R2 Data Catalog automates table maintenance"><meta property="og:url" content="https://developers.cloudflare.com/r2-data-catalog/table-maintenance/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2 Data Catalog"><meta name="algolia_product_filter" content="R2 Data Catalog"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="R2 Data Catalog"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2-data-catalog/table-maintenance/#page","headline":"Table maintenance \u00b7 Cloudflare R2 Data Catalog docs","description":"Learn how R2 Data Catalog automates table maintenance","url":"https://developers.cloudflare.com/r2-data-catalog/table-maintenance/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2-data-catalog/table-maintenance/
  schema: 1
---
<p>Table maintenance encompasses a set of operations that keep your Apache Iceberg tables performant and cost-efficient over time. As data is written, updated, and deleted, tables accumulate metadata and files that can degrade query performance over time.</p>
<p>R2 Data Catalog automates two critical maintenance operations:</p>
<ul>
<li><strong>Compaction</strong>: Combines small data files into larger, more efficient files to improve query performance</li>
<li><strong>Snapshot expiration</strong>: Removes old table snapshots and any unreferenced data files to reduce metadata overhead and storage costs</li>
</ul>
<p>Without regular maintenance, tables can suffer from:</p>
<ul>
<li><strong>Query performance degradation</strong>: More files to scan means slower queries and higher compute costs</li>
<li><strong>Increased storage costs</strong>: Accumulation of small files and old snapshots consumes unnecessary storage</li>
<li><strong>Metadata overhead</strong>: Large metadata files slow down query planning and table operations</li>
</ul>
<p>By enabling automatic table maintenance, R2 Data Catalog ensures your tables remain optimized without having to manually run them yourself.</p>
<h2 id="view-and-queue-table-maintenance">View and queue table maintenance</h2>
<p>The <strong>Maintenance</strong> tab for each table shows the compaction and snapshot expiration configuration, schedule, and next eligibility time. It also provides a paginated history of maintenance runs with their status and duration.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/526.md")
</div>
<p><img src="/assets/upstream/images/r2-data-catalog/table-maintenance-view.png" alt="Maintenance tab for an R2 Data Catalog table showing schedules and recent runs" /></p>
<p>The <strong>Recent runs</strong> section displays five runs per page. Expand a run to view metrics for its manifest rewrite, compaction, and snapshot expiration operations. For manually queued runs, the expanded details include a searchable <code>request_id</code>.</p>
<h3 id="queue-compaction-manually">Queue compaction manually</h3>
<p>Manual queueing requests compaction for the selected table. The request enters the same queue used by automatic maintenance and starts when the scheduler next polls for eligible work.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/527.md")
</div>
<p>The dashboard checks your permissions before accepting the request. Queueing can also return the following errors:</p>
<ul>
<li><code>40903</code>: A maintenance executor conflict prevents the request from being queued.</li>
<li><code>42901</code>: The daily accepted-request limit has been reached.</li>
</ul>
<h2 id="why-do-i-need-compaction">Why do I need compaction?</h2>
<p>Every write operation in <a href="https://iceberg.apache.org/">Apache Iceberg</a>, no matter how small or large, results in a series of new files being generated. As time goes on, the number of files can grow unbounded. This can lead to:</p>
<ul>
<li>Slower queries and increased I/O operations: Without compaction, query engines will have to open and read each individual file, resulting in longer query times and increased costs.</li>
<li>Increased metadata overhead: Query engines must scan metadata files to determine which ones to read. With thousands of small files, query planning takes longer even before data is accessed.</li>
<li>Reduced compression efficiency: Smaller files compress less efficiently than larger files, leading to higher storage costs and more data to transfer during queries.</li>
</ul>
<h2 id="r2-data-catalog-automatic-compaction">R2 Data Catalog automatic compaction</h2>
<p>R2 Data Catalog can now <a href="/r2-data-catalog/manage-catalogs/">manage compaction</a> for Apache Iceberg tables stored in R2. When enabled, compaction runs automatically and combines new files that have not been compacted yet.</p>
<p>Compacted files are prefixed with <code>compacted-</code> in the <code>/data/</code> directory of a respective table.</p>
<h3 id="examples">Examples</h3>
<pre tabindex="0"><code class="language-bash">&#35; Enable catalog-level compaction (all tables)&#10;npx wrangler r2 bucket catalog compaction enable my-bucket \&#10;  &#45;-target-size 128 \&#10;  &#45;-token $R2_CATALOG_TOKEN&#10;&#10;&#35; Enable compaction for a specific table&#10;npx wrangler r2 bucket catalog compaction enable my-bucket my-namespace my-table \&#10;  &#45;-target-size 256&#10;&#10;&#35; Disable catalog-level compaction&#10;npx wrangler r2 bucket catalog compaction disable my-bucket&#10;&#10;&#35; Disable compaction for a specific table&#10;npx wrangler r2 bucket catalog compaction disable my-bucket my-namespace my-table&#10;</code></pre>
<p>For more details on managing compaction, refer to <a href="/r2-data-catalog/manage-catalogs/">Manage catalogs</a>.</p>
<h3 id="choose-the-right-target-file-size">Choose the right target file size</h3>
<p>You can configure the target file size for compaction. Currently, the minimum is 64 MB and the maximum is 512 MB.</p>
<p>Different compute engines have different optimal file sizes, so check their documentation.</p>
<p>Performance tradeoffs depend on your use case. For example, queries that return small amounts of data may perform better with smaller files, as larger files could result in reading unnecessary data.</p>
<ul>
<li>For workloads that are more latency sensitive, consider a smaller target file size (for example, 64 MB - 128 MB)</li>
<li>For streaming ingest workloads, consider medium file sizes (for example, 128 MB - 256 MB)</li>
<li>For OLAP style queries that need to scan a lot of data, consider larger file sizes (for example, 256 MB - 512 MB)</li>
</ul>
<h2 id="why-do-i-need-snapshot-expiration">Why do I need snapshot expiration?</h2>
<p>Every write to an Iceberg table—whether an insert, update, or delete—creates a new snapshot. Over time, these snapshots can accumulate and cause performance issues:</p>
<ul>
<li><strong>Metadata overhead</strong>: Each snapshot adds entries to the table's metadata files. As the number of snapshots grows, metadata files become larger, slowing down query planning and table operations</li>
<li><strong>Increased storage costs</strong>: Old snapshots reference data files that may no longer be needed. Without snapshot expiration, these files continue consuming unnecessary storage</li>
<li><strong>Slower table operations</strong>: Operations like listing snapshots or accessing table history become slower over time</li>
</ul>
<h2 id="r2-data-catalog-automatic-snapshot-expiration">R2 Data Catalog automatic snapshot expiration</h2>
<h3 id="configure-snapshot-expiration">Configure snapshot expiration</h3>
<p>Snapshot expiration uses two parameters to determine which snapshots to remove:</p>
<ul>
<li><code>--older-than-days</code>: Remove snapshots older than this many days (default: 30 days)</li>
<li><code>--retain-last</code>: Always keep this minimum number of recent snapshots (default: 5 snapshots)</li>
</ul>
<p>Both conditions must be met for a snapshot to be expired. This ensures you always retain recent snapshots even if they are older than the age threshold.</p>
<h3 id="examples-1">Examples</h3>
<pre tabindex="0"><code class="language-bash">&#35; Enable snapshot expiration for entire catalog&#10;&#35; Keep minimum 10 snapshots, expire those older than 7 days&#10;npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \&#10;  &#45;-token $R2_CATALOG_TOKEN \&#10;  &#45;-older-than-days 7 \&#10;  &#45;-retain-last 10&#10;&#10;&#35; Enable for specific table&#10;&#35; Keep minimum 5 snapshots, expire those older than 2 days&#10;npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket my-namespace my-table \&#10;  &#45;-token $R2_CATALOG_TOKEN \&#10;  &#45;-older-than-days 2 \&#10;  &#45;-retain-last 5&#10;&#10;&#35; Disable snapshot expiration for a catalog&#10;npx wrangler r2 bucket catalog snapshot-expiration disable my-bucket&#10;</code></pre>
<h3 id="choose-the-right-retention-policy">Choose the right retention policy</h3>
<p>Different workloads require different snapshot retention strategies:</p>
<ul>
<li><strong>Development/testing tables</strong>: Shorter retention (2-7 days, 5 snapshots) to minimize storage costs</li>
<li><strong>Production analytics tables</strong>: Medium retention (7-30 days, 10-20 snapshots) for debugging and analysis</li>
<li><strong>Compliance/audit tables</strong>: Longer retention (30-90 days, 50+ snapshots) to meet regulatory requirements</li>
<li><strong>High-frequency ingest</strong>: Higher minimum snapshot count to preserve more granular history</li>
</ul>
<p>These are generic recommendations, make sure to consider:</p>
<ul>
<li>Time travel requirements</li>
<li>Compliance requirements</li>
<li>Storage costs</li>
</ul>
<h2 id="current-limitations">Current limitations</h2>
<ul>
<li>Only data files stored in parquet format are currently supported with compaction.</li>
<li>Files that were not previously referenced by a snapshot will not be cleaned up (orphaned files).</li>
<li>Minimum target file size for compaction is 64 MB and maximum is 512 MB.</li>
</ul>
