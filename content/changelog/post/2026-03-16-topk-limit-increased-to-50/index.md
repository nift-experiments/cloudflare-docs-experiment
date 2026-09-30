<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 16, 2026</time><h2 id="post-title">Return up to 50 query results with values or metadata</h2>
<div class="changelog-badges"><span>vectorize</span></div><div class="changelog-body"><p>You can now set <code>topK</code> up to <code>50</code> when a Vectorize query returns values or full metadata. This raises the previous limit of <code>20</code> for queries that use <code>returnValues: true</code> or <code>returnMetadata: &quot;all&quot;</code>.</p>
<p>Use the higher limit when you need more matches in a single query response without dropping values or metadata. Refer to the <a href="/vectorize/reference/client-api/">Vectorize API reference</a> for query options and current <code>topK</code> limits.</p>
</div></article></div>
