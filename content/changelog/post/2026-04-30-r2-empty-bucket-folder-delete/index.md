<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 30, 2026</time><h2 id="post-title">Empty buckets and delete folders from the R2 dashboard</h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p>You can now empty an entire <a href="/r2/">R2</a> bucket or delete folders directly from the dashboard. Emptying a bucket is required before you can delete it. Previously, this required scripting or configuring <a href="/r2/buckets/object-lifecycles/">lifecycle rules</a>. Now, the dashboard can handle it in a single action.</p>
<h4 id="empty-a-bucket">Empty a bucket</h4>
<p>Go to your bucket's <strong>Settings</strong> tab and select <strong>Empty</strong> under the <strong>Empty Bucket</strong> section. This deletes all objects in the bucket while preserving the bucket and its configuration. For large buckets, the operation runs in the background and the dashboard displays progress.</p>
<p>Emptying a bucket is also a prerequisite for deleting it. The dashboard now guides you through both steps in one place.</p>
<p><img src="/assets/upstream/images/r2/empty-bucket-changelog.png" alt="Empty Bucket and Delete Bucket sections in the R2 dashboard Settings tab" /></p>
<h4 id="delete-folders">Delete folders</h4>
<p>R2 uses a flat object structure. The dashboard groups objects that share a common prefix into folders when the <strong>View prefixes as directories</strong> checkbox is selected. Deleting a folder removes every object under that prefix.</p>
<p>From the <strong>Objects</strong> tab, you can select one or more folders and delete them alongside individual objects.</p>
<p>For step-by-step instructions, refer to <a href="/r2/buckets/delete-buckets/">Delete buckets</a> and <a href="/r2/objects/delete-objects/">Delete objects</a>.</p>
</div></article></div>
