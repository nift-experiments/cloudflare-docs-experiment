<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 26, 2026</time><h2 id="post-title">Delete Log Explorer datasets</h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>Cloudflare Log Explorer customers can now permanently delete account and zone datasets from the Cloudflare dashboard or API.</p>
<p>Deletion protection is enabled by default to prevent accidental data loss. In the dashboard, go to <a href="/log-explorer/manage-datasets/">Manage datasets</a>, disable deletion protection for the dataset, select <strong>Delete</strong>, and enter the dataset name to confirm.</p>
<p>To delete a dataset through the API, first set <code>deletion_protection</code> to <code>false</code> with the <a href="/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/update/">Update an account or zone dataset</a> method. Then use the <a href="/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/delete/">Delete an account or zone dataset</a> method.</p>
<p>Dataset deletion is irreversible and runs asynchronously. You cannot recreate the same dataset while deletion is in progress.</p>
</div></article></div>
