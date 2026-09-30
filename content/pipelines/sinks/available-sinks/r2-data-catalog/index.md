<p>R2 Data Catalog sinks write processed data from pipelines as <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables to <a href="/r2-data-catalog/">R2 Data Catalog</a>. Iceberg tables provide ACID transactions, schema evolution, and time travel capabilities for analytics workloads.</p>
<p>To create an R2 Data Catalog sink, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-sinks-create"><code>pipelines sinks create</code></a> command and specify the sink type, target bucket, namespace, and table name:</p>
<pre><code class="language-bash">npx wrangler pipelines sinks create my-sink \&#10;  &#45;-type r2-data-catalog \&#10;  &#45;-bucket my-bucket \&#10;  &#45;-namespace my_namespace \&#10;  &#45;-table my_table \&#10;  &#45;-catalog-token YOUR_CATALOG_TOKEN&#10;</code></pre>
<p>The sink will create the specified namespace and table if they do not exist. Sinks cannot be created for existing Iceberg tables.</p>
<h2 id="format">Format</h2>
<p>R2 Data Catalog sinks only support Parquet format. JSON format is not supported for Iceberg tables.</p>
<h3 id="compression-options">Compression options</h3>
<p>Configure Parquet compression for optimal storage and query performance:</p>
<pre><code class="language-bash">&#45;-compression zstd&#10;</code></pre>
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
<pre><code class="language-bash">&#45;-target-row-group-size 256&#10;</code></pre>
<h2 id="batching-and-rolling-policy">Batching and rolling policy</h2>
<p>Control when data is written to Iceberg tables. Configure based on your needs:</p>
<ul>
<li><strong>Lower values</strong>: More frequent writes, smaller files, lower latency</li>
<li><strong>Higher values</strong>: Less frequent writes, larger files, better query performance</li>
</ul>
<h3 id="roll-interval">Roll interval</h3>
<p>Set how often files are written (default: 300 seconds, minimum: 60 seconds):</p>
<pre><code class="language-bash">&#45;-roll-interval 60  # Write files every 60 seconds&#10;</code></pre>
<p>The minimum interval for R2 Data Catalog sinks is 60 seconds to prevent compaction issues. Iceberg tables require periodic compaction to merge small files into larger ones for optimal query performance. Writing too often creates merge conflicts with the compaction process.</p>
<h3 id="roll-size">Roll size</h3>
<p>Set maximum file size in MB before creating a new file:</p>
<pre><code class="language-bash">&#45;-roll-size 100  # Create new file after 100MB&#10;</code></pre>
<h2 id="authentication">Authentication</h2>
<p>R2 Data Catalog sinks require an API token with <a href="/r2-data-catalog/manage-catalogs/#create-api-token-in-the-dashboard">R2 Admin Read &amp; Write permissions</a>. This permission grants the sink access to both R2 Data Catalog and R2 storage.</p>
<pre><code class="language-bash">&#45;-catalog-token YOUR_CATALOG_TOKEN&#10;</code></pre>
