<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 25, 2025</time><h2 id="post-title">R2 Data Catalog now supports compaction</h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p>You can now enable automatic compaction for <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a> to improve query performance.</p>
<p>Compaction is the process of taking a group of small files and combining them into fewer larger files. This is an important maintenance operation as it helps ensure that query performance remains consistent by reducing the number of files that needs to be scanned.</p>
<p>To enable automatic compaction in R2 Data Catalog, find it under <strong>R2 Data Catalog</strong> in your R2 bucket settings in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/r2/compaction.png" alt="compaction-dash" /></p>
<p>Or with <a href="/workers/wrangler/">Wrangler</a>, run:</p>
<pre><code class="language-bash">npx wrangler r2 bucket catalog compaction enable &lt;BUCKET_NAME&gt;  --target-size 128 --token &lt;API_TOKEN&gt;&#10;</code></pre>
<p>To get started with compaction, check out <a href="/r2-data-catalog/manage-catalogs/">manage catalogs</a>. For best practices and limitations, refer to <a href="/r2-data-catalog/table-maintenance/">about compaction</a>.</p>
</div></article></div>
