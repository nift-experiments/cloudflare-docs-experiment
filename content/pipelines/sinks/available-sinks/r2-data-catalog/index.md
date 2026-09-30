---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/sinks/available-sinks/r2-data-catalog/
  description: Write data as Apache Iceberg tables to R2 Data Catalog
  full_title: R2 Data Catalog · Cloudflare Pipelines Docs
  head_html: <title>R2 Data Catalog · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Write data as Apache Iceberg tables to R2 Data Catalog"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/sinks/available-sinks/r2-data-catalog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/sinks/available-sinks/r2-data-catalog/index.md"><meta property="og:title" content="R2 Data Catalog · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write data as Apache Iceberg tables to R2 Data Catalog"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/sinks/available-sinks/r2-data-catalog/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/sinks/available-sinks/r2-data-catalog/#page","headline":"R2 Data Catalog \u00b7 Cloudflare Pipelines Docs","description":"Write data as Apache Iceberg tables to R2 Data Catalog","url":"https://developers.cloudflare.com/pipelines/sinks/available-sinks/r2-data-catalog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/sinks/available-sinks/r2-data-catalog/
  schema: 1
---
<p>R2 Data Catalog sinks write processed data from pipelines as <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables to <a href="/r2-data-catalog/">R2 Data Catalog</a>. Iceberg tables provide ACID transactions, schema evolution, and time travel capabilities for analytics workloads.</p>
<p>To create an R2 Data Catalog sink, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-sinks-create"><code>pipelines sinks create</code></a> command and specify the sink type, target bucket, namespace, and table name:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines sinks create my-sink \&#10;  &#45;-type r2-data-catalog \&#10;  &#45;-bucket my-bucket \&#10;  &#45;-namespace my_namespace \&#10;  &#45;-table my_table \&#10;  &#45;-catalog-token YOUR_CATALOG_TOKEN&#10;</code></pre>
<p>The sink will create the specified namespace and table if they do not exist. Sinks cannot be created for existing Iceberg tables.</p>
<h2 id="format">Format</h2>
<p>R2 Data Catalog sinks only support Parquet format. JSON format is not supported for Iceberg tables.</p>
<h3 id="compression-options">Compression options</h3>
<p>Configure Parquet compression for optimal storage and query performance:</p>
<pre tabindex="0"><code class="language-bash">&#45;-compression zstd&#10;</code></pre>
<p><strong>Available compression options:</strong></p>
<ul>
<li><code>zstd</code> (default) - Best compression ratio</li>
<li><code>snappy</code> - Fastest compression</li>
<li><code>gzip</code> - Good compression, widely supported</li>
<li><code>lz4</code> - Fast compression with reasonable ratio</li>
<li><code>uncompressed</code> - No compression</li>
</ul>
<h3 id="row-group-size">Row group size</h3>
<p><a href="https://parquet.apache.org/docs/file-format/configurations/">Row groups</a> are sets of rows in a Parquet file that are stored together, affecting memory usage and query performance. Configure the target row group size in MB:</p>
<pre tabindex="0"><code class="language-bash">&#45;-target-row-group-size 256&#10;</code></pre>
<h2 id="batching-and-rolling-policy">Batching and rolling policy</h2>
<p>Control when data is written to Iceberg tables. Configure based on your needs:</p>
<ul>
<li><strong>Lower values</strong>: More frequent writes, smaller files, lower latency</li>
<li><strong>Higher values</strong>: Less frequent writes, larger files, better query performance</li>
</ul>
<h3 id="roll-interval">Roll interval</h3>
<p>Set how often files are written (default: 300 seconds, minimum: 60 seconds):</p>
<pre tabindex="0"><code class="language-bash">&#45;-roll-interval 60  # Write files every 60 seconds&#10;</code></pre>
<p>The minimum interval for R2 Data Catalog sinks is 60 seconds to prevent compaction issues. Iceberg tables require periodic compaction to merge small files into larger ones for optimal query performance. Writing too often creates merge conflicts with the compaction process.</p>
<h3 id="roll-size">Roll size</h3>
<p>Set maximum file size in MB before creating a new file:</p>
<pre tabindex="0"><code class="language-bash">&#45;-roll-size 100  # Create new file after 100MB&#10;</code></pre>
<h2 id="authentication">Authentication</h2>
<p>R2 Data Catalog sinks require an API token with <a href="/r2-data-catalog/manage-catalogs/#create-api-token-in-the-dashboard">R2 Admin Read &amp; Write permissions</a>. This permission grants the sink access to both R2 Data Catalog and R2 storage.</p>
<pre tabindex="0"><code class="language-bash">&#45;-catalog-token YOUR_CATALOG_TOKEN&#10;</code></pre>
