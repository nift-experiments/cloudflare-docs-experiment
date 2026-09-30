<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 22, 2025</time><h2 id="post-title">Workers KV completes hybrid storage provider rollout for improved performance, fault-tolerance</h2>
<div class="changelog-badges"><span>kv</span></div><div class="changelog-body"><p>Workers KV has completed rolling out performance improvements across all KV namespaces, providing a significant latency reduction on read operations for all KV users. This is due to architectural changes to KV's underlying storage infrastructure, which introduces a new metadata later and substantially improves redundancy.</p>
<p><img src="/assets/upstream/images/kv/changelog/kv-hybrid-providers-performance-improvements.png" alt="Workers KV latency improvements showing P95 and P99 performance gains in Europe, Asia, Africa and Middle East regions as measured within KV's internal storage gateway worker." /></p>
<h4 id="performance-improvements">Performance improvements</h4>
<p>The new hybrid architecture delivers substantial latency reductions throughout Europe, Asia, Middle East, Africa regions. Over the past 2 weeks, we have observed the following:</p>
<ul>
<li><strong>p95 latency</strong>: Reduced from ~150ms to ~50ms (67% decrease)</li>
<li><strong>p99 latency</strong>: Reduced from ~350ms to ~250ms (29% decrease)</li>
</ul>
</div></article></div>
