<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 28, 2026</time><h2 id="post-title">Durable Objects can use up to ten Dynamic Workers concurrently</h2>
<div class="changelog-badges"><span>workers</span><span>durable-objects</span></div><div class="changelog-body"><p><a href="/durable-objects/">Durable Objects</a> can have up to ten distinct <a href="/dynamic-workers/">Dynamic Workers</a> with in-flight requests, increased from four. This limit applies across all concurrent requests to the same Durable Object because they share an input/output (I/O) context. Other Workers can have up to four distinct Dynamic Workers with in-flight requests per request.</p>
<p>Multiple in-flight requests to the same Dynamic Worker count as one toward this limit.</p>
<p>For more information, refer to <a href="/dynamic-workers/platform/limits/">Dynamic Workers limits</a>.</p>
</div></article></div>
