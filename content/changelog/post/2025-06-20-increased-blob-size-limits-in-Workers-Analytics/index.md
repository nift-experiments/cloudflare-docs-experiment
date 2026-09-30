<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 20, 2025</time><h2 id="post-title">Increased blob size limits in Workers Analytics Engine</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We’ve increased the total allowed size of <a href="/analytics/analytics-engine/get-started/#2-write-data-points-from-your-worker"><code>blob</code></a> fields on data points written to <a href="/analytics/analytics-engine/">Workers Analytics Engine</a> from <strong>5 KB to 16 KB</strong>.</p>
<p>This change gives you more flexibility when logging rich observability data — such as base64-encoded payloads, AI inference traces, or custom metadata — without hitting request size limits.</p>
<p>You can find full details on limits for queries, filters, payloads, and more <a href="/analytics/analytics-engine/limits/">here in the Workers Analytics Engine limits documentation</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17779.md")</div>
</div></article></div>
