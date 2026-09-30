---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/sinks/available-sinks/r2/
  description: Write data as JSON or Parquet files to R2 object storage
  full_title: R2 · Cloudflare Pipelines Docs
  head_html: <title>R2 · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Write data as JSON or Parquet files to R2 object storage"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/sinks/available-sinks/r2/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/sinks/available-sinks/r2/index.md"><meta property="og:title" content="R2 · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write data as JSON or Parquet files to R2 object storage"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/sinks/available-sinks/r2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/sinks/available-sinks/r2/#page","headline":"R2 \u00b7 Cloudflare Pipelines Docs","description":"Write data as JSON or Parquet files to R2 object storage","url":"https://developers.cloudflare.com/pipelines/sinks/available-sinks/r2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/sinks/available-sinks/r2/
  schema: 1
---
<p>R2 sinks write processed data from pipelines as raw files to <a href="/r2/">R2 object storage</a>. They currently support writing to JSON and Parquet formats.</p>
<p>To create an R2 sink, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-sinks-create"><code>pipelines sinks create</code></a> command and specify the sink type and target <a href="/r2/buckets/">bucket</a>:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines sinks create my-sink \&#10;  &#45;-type r2 \&#10;  &#45;-bucket my-bucket&#10;</code></pre>
<h2 id="format-options">Format options</h2>
<p>R2 sinks support two output formats:</p>
<h3 id="json-format">JSON format</h3>
<p>Write data as newline-delimited JSON files. JSON sinks support two compression modes: <code>uncompressed</code> (default) and <code>gzip</code>:</p>
<pre tabindex="0"><code class="language-bash">&#45;-format json --compression gzip&#10;</code></pre>
<h3 id="parquet-format">Parquet format</h3>
<p>Write data as Parquet files for better query performance and compression:</p>
<pre tabindex="0"><code class="language-bash">&#45;-format parquet --compression zstd&#10;</code></pre>
<p><strong>Compression options for Parquet:</strong></p>
<ul>
<li><code>zstd</code> (default) - Best compression ratio</li>
<li><code>snappy</code> - Fastest compression</li>
<li><code>gzip</code> - Good compression, widely supported</li>
<li><code>lz4</code> - Fast compression with reasonable ratio</li>
<li><code>uncompressed</code> - No compression</li>
</ul>
<p><strong>Row group size:</strong>
<a href="https://parquet.apache.org/docs/file-format/configurations/">Row groups</a> are sets of rows in a Parquet file that are stored together, affecting memory usage and query performance. Configure the target row group size in MB:</p>
<pre tabindex="0"><code class="language-bash">&#45;-target-row-group-size 256&#10;</code></pre>
<h2 id="file-organization">File organization</h2>
<p>Files are written with UUID names within the partitioned directory structure. For example, with path <code>analytics</code> and default partitioning:</p>
<pre tabindex="0"><code>analytics/year=2025/month=09/day=18/002507a5-d449-48e8-a484-b1bea916102f.parquet&#10;</code></pre>
<h3 id="path">Path</h3>
<p>Set a base directory in your bucket where files will be written:</p>
<pre tabindex="0"><code class="language-bash">&#45;-path analytics/events&#10;</code></pre>
<h3 id="partitioning">Partitioning</h3>
<p>R2 sinks automatically partition files by time using a configurable pattern. The default pattern is <code>year=%Y/month=%m/day=%d</code> (Hive-style partitioning).</p>
<pre tabindex="0"><code class="language-bash">&#45;-partitioning &quot;year=%Y/month=%m/day=%d/hour=%H&quot;&#10;</code></pre>
<p>For available format specifiers, refer to <a href="https://docs.rs/chrono/latest/chrono/format/strftime/index.html">strftime documentation</a>.</p>
<h2 id="batching-and-rolling-policy">Batching and rolling policy</h2>
<p>Control when files are written to R2. Configure based on your needs:</p>
<ul>
<li><strong>Lower values</strong>: More frequent writes, smaller files, lower latency</li>
<li><strong>Higher values</strong>: Less frequent writes, larger files, better query performance</li>
</ul>
<h3 id="roll-interval">Roll interval</h3>
<p>Set how often files are written (default: 300 seconds, minimum: 10 seconds):</p>
<pre tabindex="0"><code class="language-bash">&#45;-roll-interval 10  # Write files every 10 seconds&#10;</code></pre>
<h3 id="roll-size">Roll size</h3>
<p>Set maximum file size in MB before creating a new file:</p>
<pre tabindex="0"><code class="language-bash">&#45;-roll-size 100  # Create new file after 100MB&#10;</code></pre>
<h2 id="authentication">Authentication</h2>
<p>R2 sinks require an API credentials (Access Key ID and Secret Access Key) with <a href="/r2/api/tokens/#permissions">Object Read &amp; Write permissions</a> to write data to your bucket.</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines sinks create my-sink \&#10;  &#45;-type r2 \&#10;  &#45;-bucket my-bucket \&#10;  &#45;-access-key-id YOUR_ACCESS_KEY_ID \&#10;  &#45;-secret-access-key YOUR_SECRET_ACCESS_KEY&#10;</code></pre>
