<p>These settings control how many results are returned and the minimum score required. To filter results by metadata attributes like folder or category, refer to <a href="/ai-search/configuration/retrieval/filtering/">Filtering</a>.</p>
<h2 id="match-threshold">Match threshold</h2>
<p>The <code>match_threshold</code> sets the minimum vector similarity score that a chunk must meet to be included in the results. Threshold values range from <code>0</code> to <code>1</code>. The threshold filters on the vector similarity score, not the fused score returned in the response.</p>
<ul>
<li>A higher threshold means stricter filtering, returning only highly similar matches.</li>
<li>A lower threshold allows broader matches, increasing recall but possibly reducing precision.</li>
</ul>
<h2 id="maximum-number-of-results">Maximum number of results</h2>
<p>The <code>max_num_results</code> setting controls the number of top-matching chunks returned. The maximum allowed value is 50.</p>
<ul>
<li>Use a higher value if you want to synthesize across multiple documents. However, providing more input to the model can increase latency and cost.</li>
<li>Use a lower value if you prefer concise answers with minimal context.</li>
</ul>
<h2 id="how-they-work-together">How they work together</h2>
<ol>
<li>Your query is embedded using the configured embedding model.</li>
<li>The search index is queried. For <a href="/ai-search/configuration/indexing/hybrid-search/">hybrid search</a>, vector and keyword results are fused into a single ranked list.</li>
<li>Chunks with a vector similarity score below <code>match_threshold</code> are filtered out.</li>
<li>The filtered results are limited to <code>max_num_results</code> and passed into the generation step as context.</li>
</ol>
<p>If no results meet the threshold, AI Search will not generate a response.</p>
<p>If <a href="/ai-search/configuration/retrieval/reranking/">reranking</a> is enabled, a separate <code>reranking.match_threshold</code> can be configured to filter chunks by their reranking score.</p>
<h2 id="per-request-override">Per-request override</h2>
<p>These values can be configured at the instance level or overridden per request:</p>
<pre><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			match_threshold: 0.5,&#10;			max_num_results: 10,&#10;		},&#10;	},&#10;});&#10;</code></pre>
