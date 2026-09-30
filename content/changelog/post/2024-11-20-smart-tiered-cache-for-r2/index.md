<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 20, 2024</time><h2 id="post-title">Smart Tiered Cache automatically optimizes R2 caching</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now reduce latency and lower R2 egress costs automatically when using <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> with <a href="/r2/">R2</a>. Cloudflare intelligently selects a tiered data center close to your R2 bucket location, creating an efficient caching topology without additional configuration.</p>
<h4 id="how-it-works">How it works</h4>
<p>When you enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> for zones using <a href="/r2/">R2</a> as an origin, Cloudflare automatically:</p>
<ol>
<li><strong>Identifies your R2 bucket location</strong>: Determines the geographical region where your R2 bucket is stored.</li>
<li><strong>Selects an optimal Upper Tier</strong>: Chooses a data center close to your bucket as the common Upper Tier cache.</li>
<li><strong>Routes requests efficiently</strong>: All cache misses in edge locations route through this Upper Tier before reaching R2.</li>
</ol>
<h4 id="benefits">Benefits</h4>
<ul>
<li><strong>Automatic optimization</strong>: No manual configuration required.</li>
<li><strong>Lower egress costs</strong>: Fewer requests to R2 reduce egress charges.</li>
<li><strong>Improved hit ratio</strong>: Common Upper Tier increases cache efficiency.</li>
<li><strong>Reduced latency</strong>: Upper Tier proximity to R2 minimizes fetch times.</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> on your zone using R2 as an origin.</p>
</div></article></div>
