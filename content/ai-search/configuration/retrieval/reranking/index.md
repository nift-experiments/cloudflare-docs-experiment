<p>Reranking can help improve the quality of AI Search results by reordering retrieved documents based on semantic relevance to the user's query. It applies a secondary model after retrieval to rerank the top results before they are returned.</p>
<h2 id="how-it-works">How it works</h2>
<p>By default, reranking is <strong>disabled</strong> for all AI Search instances. You can enable it during creation or later from the settings page.</p>
<p>When enabled, AI Search will:</p>
<ol>
<li>Retrieve a set of relevant results from your index, constrained by your <code>max_num_results</code> and <code>score_threshold</code> parameters.</li>
<li>Pass those results through a <a href="/ai-search/configuration/models/supported-models/">reranking model</a>.</li>
<li>Return the reranked results, which the text generation model can use for answer generation.</li>
</ol>
<p>Reranking helps improve accuracy, especially for large or noisy datasets where vector similarity alone may not produce the optimal ordering.</p>
<h2 id="configuration">Configuration</h2>
<p>When you make a <code>/search</code> or <code>/chat/completions</code> request using the <a href="/ai-search/api/search/workers-binding/">Workers binding</a> or <a href="/ai-search/api/search/rest-api/">REST API</a>, you can enable or disable reranking per request and specify the reranking model.</p>
<pre><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		reranking: {&#10;			enabled: true,&#10;			model: &quot;@cf/baai/bge-reranker-base&quot;,&#10;		},&#10;	},&#10;});&#10;</code></pre>
<h3 id="considerations">Considerations</h3>
<p>Adding reranking will include an additional step to the query request. As a result, there may be an increase in the latency of the request.</p>
