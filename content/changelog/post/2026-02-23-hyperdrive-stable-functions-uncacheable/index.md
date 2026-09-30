<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 23, 2026</time><h2 id="post-title">Hyperdrive no longer caches queries using STABLE PostgreSQL functions</h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Hyperdrive now treats queries containing PostgreSQL <code>STABLE</code> functions as uncacheable, in addition to <code>VOLATILE</code> functions.</p>
<p>Previously, only functions <a href="https://www.postgresql.org/docs/current/xfunc-volatility.html">that PostgreSQL categorizes</a> as <code>VOLATILE</code> (for example, <code>RANDOM()</code>, <code>LASTVAL()</code>) were detected as uncacheable. <code>STABLE</code> functions (for example, <code>NOW()</code>, <code>CURRENT_TIMESTAMP</code>, <code>CURRENT_DATE</code>) were incorrectly allowed to be cached.</p>
<p>Because <code>STABLE</code> functions can return different results across different SQL statements within the same transaction, caching their results could serve stale or incorrect data. This change aligns Hyperdrive's caching behavior with PostgreSQL's function volatility semantics.</p>
<p>If your queries use <code>STABLE</code> functions, and you were relying on them being cached, move the function call to your application code and pass the result as a query parameter. For example, instead of <code>WHERE created_at &gt; NOW()</code>, compute the timestamp in your Worker and pass it as <code>WHERE created_at &gt; $1</code>.</p>
<p>Hyperdrive uses text-based pattern matching to detect uncacheable functions. References to function names like <code>NOW()</code> in SQL comments also cause the query to be marked as uncacheable.</p>
<p>For more information, refer to <a href="/hyperdrive/concepts/query-caching/">Query caching</a> and <a href="/hyperdrive/observability/troubleshooting/">Troubleshoot and debug</a>.</p>
</div></article></div>
