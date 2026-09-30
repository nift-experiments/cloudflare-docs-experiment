<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 16, 2026</time><h2 id="post-title">AI Search now has hybrid search and relevance boosting</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports hybrid search and relevance boosting, giving you more control over how results are found and ranked.</p>
<h4 id="hybrid-search">Hybrid search</h4>
<p>Hybrid search combines vector (semantic) search with BM25 keyword search in a single query. Vector search finds chunks with similar meaning, even when the exact words differ. Keyword search matches chunks that contain your query terms exactly. When you enable hybrid search, both run in parallel and the results are fused into a single ranked list.</p>
<p>You can configure the tokenizer (<code>porter</code> for natural language, <code>trigram</code> for code), keyword match mode (<code>and</code> for precision, <code>or</code> for recall), and fusion method (<code>rrf</code> or <code>max</code>) per instance:</p>
<pre><code class="language-ts">const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;	index_method: { vector: true, keyword: true },&#10;	fusion_method: &quot;rrf&quot;,&#10;	indexing_options: { keyword_tokenizer: &quot;porter&quot; },&#10;	retrieval_options: { keyword_match_mode: &quot;and&quot; },&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/concepts/search-modes/">Search modes</a> for an overview and <a href="/ai-search/configuration/indexing/hybrid-search/">Hybrid search</a> for configuration details.</p>
<h4 id="relevance-boosting">Relevance boosting</h4>
<p>Relevance boosting lets you nudge search rankings based on document metadata. For example, you can prioritize recent documents by boosting on <code>timestamp</code>, or surface high-priority content by boosting on a custom metadata field like <code>priority</code>.</p>
<p>Configure up to 3 boost fields per instance or override them per request:</p>
<pre><code class="language-ts">const results = await env.AI_SEARCH.get(&quot;my-instance&quot;).search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;deployment guide&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			boost_by: [&#10;				{ field: &quot;timestamp&quot;, direction: &quot;desc&quot; },&#10;				{ field: &quot;priority&quot;, direction: &quot;desc&quot; },&#10;			],&#10;		},&#10;	},&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/configuration/retrieval/boosting/">Relevance boosting</a> for configuration details.</p>
</div></article></div>
