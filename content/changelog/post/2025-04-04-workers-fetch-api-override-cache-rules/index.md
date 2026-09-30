<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 4, 2025</time><h2 id="post-title">Workers Fetch API can override Cache Rules</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now programmatically override Cache Rules using the <code>cf</code> object in the <code>fetch()</code> command. This feature gives you fine-grained control over caching behavior on a per-request basis, allowing Workers to customize cache settings dynamically based on request properties, user context, or business logic.</p>
<h4 id="how-it-works">How it works</h4>
<p>Using the <code>cf</code> object in <code>fetch()</code>, you can override specific Cache Rules settings by:</p>
<ol>
<li><strong>Setting custom cache options</strong>: Pass cache properties in the <code>cf</code> object as the second argument to <code>fetch()</code> to override default Cache Rules.</li>
<li><strong>Dynamic cache control</strong>: Apply different caching strategies based on request headers, cookies, or other runtime conditions.</li>
<li><strong>Per-request customization</strong>: Bypass or modify Cache Rules for individual requests while maintaining default behavior for others.</li>
<li><strong>Programmatic cache management</strong>: Implement complex caching logic that adapts to your application's needs.</li>
</ol>
<h4 id="what-can-be-configured">What can be configured</h4>
<p>Workers can override the following Cache Rules settings through the <code>cf</code> object:</p>
<ul>
<li><strong><code>cacheEverything</code></strong>: Treat all content as static and cache all file types beyond the default cached content.</li>
<li><strong><code>cacheTtl</code></strong>: Set custom time-to-live values in seconds for cached content at the edge, regardless of origin headers.</li>
<li><strong><code>cacheTtlByStatus</code></strong>: Set different TTLs based on the response status code (for example, <code>{ &quot;200-299&quot;: 86400, 404: 1, &quot;500-599&quot;: 0 }</code>).</li>
<li><strong><code>cacheKey</code></strong>: Customize cache keys to control which requests are treated as the same for caching purposes (Enterprise only).</li>
<li><strong><code>cacheTags</code></strong>: Append additional cache tags for targeted cache purging operations.</li>
</ul>
<h4 id="benefits">Benefits</h4>
<ul>
<li><strong>Enhanced flexibility</strong>: Customize cache behavior without modifying zone-level Cache Rules.</li>
<li><strong>Dynamic optimization</strong>: Adjust caching strategies in real-time based on request context.</li>
<li><strong>Simplified configuration</strong>: Reduce the number of Cache Rules needed by handling edge cases programmatically.</li>
<li><strong>Improved performance</strong>: Fine-tune cache behavior for specific use cases to maximize hit rates.</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>To get started, refer to the <a href="/workers/runtime-apis/fetch/">Workers Fetch API documentation</a> and the <a href="/workers/runtime-apis/request/#the-cf-property-requestinitcfproperties">cf object properties documentation</a>.</p>
</div></article></div>
