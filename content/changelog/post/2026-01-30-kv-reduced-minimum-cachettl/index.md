<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 30, 2026</time><h2 id="post-title">Reduced minimum cache TTL for Workers KV to 30 seconds</h2>
<div class="changelog-badges"><span>kv</span></div><div class="changelog-body"><p>The minimum <code>cacheTtl</code> parameter for Workers KV has been reduced from 60 seconds to 30 seconds. This change applies to both <code>get()</code> and <code>getWithMetadata()</code> methods.</p>
<p>This reduction allows you to maintain more up-to-date cached data and have finer-grained control over cache behavior. Applications requiring faster data refresh rates can now configure cache durations as low as 30 seconds instead of the previous 60-second minimum.</p>
<p>The <code>cacheTtl</code> parameter defines how long a KV result is cached at the global network location it is accessed from:</p>
<pre><code class="language-js">// Read with custom cache TTL&#10;const value = await env.NAMESPACE.get(&quot;my-key&quot;, {&#10;	cacheTtl: 30, // Cache for minimum 30 seconds (previously 60)&#10;});&#10;&#10;// getWithMetadata also supports the reduced cache TTL&#10;const valueWithMetadata = await env.NAMESPACE.getWithMetadata(&quot;my-key&quot;, {&#10;	cacheTtl: 30, // Cache for minimum 30 seconds&#10;});&#10;</code></pre>
<p>The default cache TTL remains unchanged at 60 seconds. Upgrade to the latest version of Wrangler to be able to use 30 seconds <code>cacheTtl</code>.</p>
<p>This change affects all KV read operations using the binding API. For more information, consult the <a href="/kv/api/read-key-value-pairs/#cachettl-parameter">Workers KV cache TTL documentation</a>.</p>
</div></article></div>
