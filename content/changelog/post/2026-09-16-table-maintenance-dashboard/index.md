<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 16, 2026</time><h2 id="post-title">R2 Data Catalog adds table maintenance visibility and manual queueing</h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p><a href="/r2-data-catalog/">R2 Data Catalog</a> now provides table-level maintenance visibility and manual compaction queueing in the Cloudflare dashboard. These updates make it easier to understand when maintenance is eligible to run, inspect completed operations, and request maintenance without leaving the table view.</p>
<p>To view table maintenance details:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17742.md")</div>
<p><img src="/assets/upstream/images/r2-data-catalog/table-maintenance-view.png" alt="Maintenance tab for an R2 Data Catalog table showing schedules and recent runs" /></p>
<p>The updated dashboard includes:</p>
<ul>
<li><strong>Maintenance tab</strong> — View compaction and snapshot expiration settings, schedules, and next eligibility alongside the table's <strong>Schema</strong> and <strong>Metadata</strong> tabs.</li>
<li><strong>Recent runs</strong> — Review a paginated audit log with job status, duration, and expandable details for manifest rewrites, compaction, and snapshot expiration. Expanded rows include operation metrics for each maintenance operation.</li>
<li><strong>Manual queueing</strong> — Select <strong>Queue maintenance</strong> to request compaction during normal scheduler polling. The dashboard checks permissions and explains when another maintenance job conflicts with the request or the daily accepted-request limit has been reached.</li>
<li><strong>Updated catalog layout</strong> — Find catalog metrics in the <strong>Metrics</strong> tab, use the renamed <strong>Explorer</strong> tab to browse data, and switch between table details using tabs instead of a scroll-to-section sidebar.</li>
<li><strong>Improved schema browser</strong> — For accounts with the schema browser enabled, select a namespace to open its tables in the right pane while also expanding the namespace tree. The tree can now be collapsed to provide more space for table details.</li>
</ul>
<p>For more information about compaction and snapshot expiration, refer to <a href="/r2-data-catalog/table-maintenance/">Table maintenance</a>.</p>
</div></article></div>
