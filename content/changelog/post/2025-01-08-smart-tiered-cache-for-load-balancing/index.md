<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 8, 2025</time><h2 id="post-title">Smart Tiered Cache optimizes Load Balancing Pools</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now achieve higher cache hit rates and reduce origin load when using <a href="/load-balancing/">Load Balancing</a> with <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>. Cloudflare automatically selects a single, optimal tiered data center for all origins in your Load Balancing Pool.</p>
<h4 id="how-it-works">How it works</h4>
<p>When you use <a href="/load-balancing/">Load Balancing</a> with <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>, Cloudflare analyzes performance metrics across your pool's origins and automatically selects the optimal Upper Tier data center for the entire pool. This means:</p>
<ul>
<li><strong>Consistent cache location</strong>: All origins in the pool share the same Upper Tier cache.</li>
<li><strong>Higher HIT rates</strong>: Requests for the same content hit the cache more frequently.</li>
<li><strong>Reduced origin requests</strong>: Fewer requests reach your origin servers.</li>
<li><strong>Improved performance</strong>: Faster response times for cache HITs.</li>
</ul>
<h4 id="example-workflow">Example workflow</h4>
<pre><code class="language-txt">Load Balancing Pool: api-pool&#10;├── Origin 1: api-1.example.com&#10;├── Origin 2: api-2.example.com&#10;└── Origin 3: api-3.example.com&#10;    ↓&#10;Selected Upper Tier: [Optimal data center based on pool performance]&#10;</code></pre>
<h4 id="get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> on your zone and configure your <a href="/load-balancing/">Load Balancing Pool</a>.</p>
</div></article></div>
