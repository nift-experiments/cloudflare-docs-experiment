<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 10, 2025</time><h2 id="post-title">R2 Data Catalog is a managed Apache Iceberg data catalog built directly into R2 buckets</h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p>Today, we are launching <a href="/r2-data-catalog/">R2 Data Catalog</a> in open beta, a managed Apache Iceberg catalog built directly into your <a href="/r2/">Cloudflare R2</a> bucket.</p>
<p>If you are not already familiar with it, <a href="https://iceberg.apache.org/">Apache Iceberg</a> is an open table format designed to handle large-scale analytics datasets stored in object storage, offering ACID transactions and schema evolution. R2 Data Catalog exposes a standard Iceberg REST catalog interface, so you can connect engines like <a href="/r2-data-catalog/config-examples/spark-scala/">Spark</a>, <a href="/r2-data-catalog/config-examples/snowflake/">Snowflake</a>, and <a href="/r2-data-catalog/config-examples/pyiceberg/">PyIceberg</a> to start querying your tables using the tools you already know.</p>
<p>To enable a data catalog on your R2 bucket, find <strong>R2 Data Catalog</strong> in your buckets settings in the dashboard, or run:</p>
<pre><code class="language-bash">npx wrangler r2 bucket catalog enable my-bucket&#10;</code></pre>
<p>And that's it. You'll get a catalog URI and warehouse you can plug into your favorite Iceberg engines.</p>
<p>Visit our <a href="/r2-data-catalog/get-started/">getting started guide</a> for step-by-step instructions on enabling R2 Data Catalog, creating tables, and running your first queries.</p>
</div></article></div>
