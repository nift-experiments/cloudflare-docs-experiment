<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 9, 2026</time><h2 id="post-title">AI Gateway custom costs support cache tokens</h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway custom costs now support cache-read and cache-write token rates. This lets custom cost metrics reflect negotiated cache pricing across providers.</p>
<p>Add <code>per_cache_read_token</code> or <code>per_cache_write_token</code> to the <code>cf-aig-custom-cost</code> header:</p>
<pre><code class="language-json">{&#10;	&quot;per_token_in&quot;: 0.000001,&#10;	&quot;per_token_out&quot;: 0.000002,&#10;	&quot;per_cache_read_token&quot;: 0.0000001,&#10;	&quot;per_cache_write_token&quot;: 0.0000005&#10;}&#10;</code></pre>
<p>Cache-token pricing activates when either cache rate is present. An omitted cache rate defaults to <code>per_token_in</code>. If both cache rates are omitted, AI Gateway preserves the existing input and output calculation.</p>
<p>Providers can include cache tokens within input tokens or report them separately. AI Gateway automatically accounts for these differences and prevents double-counting.</p>
<p>For more information, refer to <a href="/ai-gateway/configuration/custom-costs/">Custom costs</a>.</p>
</div></article></div>
