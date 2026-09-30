<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 7, 2026</time><h2 id="post-title">R2 Data Catalog warns before you delete data manually</h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> catalog built directly into your R2 bucket. Iceberg tracks your data through a tree of metadata files, so every insert, update, and delete must go through a catalog transaction. Manually adding, modifying, or deleting objects outside the catalog can leave pointers referencing files that no longer exist, corrupting the table into an inconsistent state that is difficult to recover from.</p>
<p>To help prevent this, the R2 dashboard and Wrangler now warn you when you attempt a manual delete operation on a Data Catalog-enabled bucket.</p>
<h4 id="dashboard">Dashboard</h4>
<p>When you try to delete objects from a bucket that has R2 Data Catalog enabled, the dashboard displays a warning explaining that the operation could leave the catalog in an invalid state, with a link to the documentation for deleting data correctly. You can cancel the operation or choose to proceed anyway.</p>
<p><img src="/assets/upstream/images/r2-data-catalog/data-catalog-delete-warning.png" alt="R2 dashboard warning shown before deleting objects from a Data Catalog-enabled bucket" /></p>
<h4 id="wrangler">Wrangler</h4>
<p>Wrangler now checks whether a bucket is Data Catalog-enabled before running a delete and warns you before continuing:</p>
<pre><code class="language-txt">Data Catalog is enabled for this bucket. &#10;Proceeding may leave the data catalog in an invalid state. Continue?&#10;</code></pre>
<p>To learn how to safely manage and delete data in your tables, refer to the <a href="/r2-data-catalog/">R2 Data Catalog documentation</a>.</p>
</div></article></div>
