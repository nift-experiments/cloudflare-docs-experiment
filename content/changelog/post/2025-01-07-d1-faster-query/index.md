<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 7, 2025</time><h2 id="post-title">40-60% Faster D1 Worker API Requests</h2>
<div class="changelog-badges"><span>d1</span></div><div class="changelog-body"><p>Users making <a href="/d1/">D1</a> requests via the <a href="/d1/worker-api/">Workers API</a> can see up to a 60% end-to-end latency improvement due to the removal of redundant network round trips needed for each request to a D1 database.</p>
<p><img src="/images/d1/faster-d1-worker-api.png" alt="D1 Worker API latency" /></p>
<p><em>p50, p90, and p95 request latency aggregated across entire D1 service. These latencies are a reference point and should not be viewed as your exact workload improvement.</em></p>
<p>This performance improvement benefits all D1 Worker API traffic, especially cross-region requests where network latency is an outsized latency factor. For example, a user in Europe talking to a database in North America. D1 <a href="/d1/configuration/data-location/#provide-a-location-hint">location hints</a> can be used to influence the geographic location of a database.</p>
<p>For more details on how D1 removed redundant round trips, see the D1 specific release note <a href="/d1/platform/release-notes/#2025-01-07">entry</a>.</p>
</div></article></div>
