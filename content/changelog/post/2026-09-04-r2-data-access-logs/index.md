<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 4, 2026</time><h2 id="post-title">R2 Data Access Logs</h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p>R2 Data Access Logs are now generally available. Turn on logging for a bucket to record object read, write, list, multipart upload, and delete operations with response status codes below <code>400</code>.</p>
<p>Data Access Logs cover requests made through the S3-compatible API, Cloudflare API and dashboard, Workers bindings, and public buckets through <code>r2.dev</code> or custom domains. Events are available in Workers Observability, where you can filter by bucket, operation, interface, actor, and other request fields.</p>
<p>Log delivery is asynchronous and best effort. Events may be delayed or omitted, so do not rely on Data Access Logs as a complete record of bucket activity.</p>
<p>Data Access Logs are available for non-jurisdictional buckets. For setup instructions, supported operations, and the event field reference, refer to <a href="/r2/buckets/data-access-logs/">R2 Data Access Logs</a>.</p>
</div></article></div>
