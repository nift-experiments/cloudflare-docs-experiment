<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 6, 2025</time><h2 id="post-title">R2 Data Catalog table-level compaction</h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p>You can now enable compaction for individual <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a>, giving you fine-grained control over different workloads.</p>
<pre><code class="language-bash">&#35; Enable compaction for a specific table (no token required)&#10;npx wrangler r2 bucket catalog compaction enable &lt;BUCKET&gt; &lt;NAMESPACE&gt; &lt;TABLE&gt; --target-size 256&#10;</code></pre>
<p>This allows you to:</p>
<ul>
<li>Apply different target file sizes per table</li>
<li>Disable compaction for specific tables</li>
<li>Optimize based on table-specific access patterns</li>
</ul>
<p>Learn more at <a href="/r2-data-catalog/manage-catalogs/">Manage catalogs</a>.</p>
</div></article></div>
