<p>Enable keyword search to match chunks that contain your query terms exactly. For an overview of search modes, refer to <a href="/ai-search/concepts/search-modes/">Search modes</a>.</p>
<h2 id="enable-keyword-search">Enable keyword search</h2>
<p>Set <code>index_method.keyword</code> to <code>true</code> when creating or updating an instance. You can use keyword search on its own or alongside vector search for <a href="/ai-search/configuration/indexing/hybrid-search/">hybrid search</a>.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>vector</code></td>
<td>boolean</td>
<td><code>true</code></td>
<td>Enable vector (semantic) search.</td>
</tr>
<tr>
<td><code>keyword</code></td>
<td>boolean</td>
<td><code>false</code></td>
<td>Enable keyword (BM25) search.</td>
</tr>
</tbody>
</table>
<p>At least one of <code>vector</code> or <code>keyword</code> must be <code>true</code>. Changing <code>index_method</code> triggers a full reindex of your content.</p>
<pre><code class="language-ts">const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;	index_method: {&#10;		vector: false,&#10;		keyword: true,&#10;	},&#10;});&#10;</code></pre>
<h2 id="keyword-tokenizer">Keyword tokenizer</h2>
<p>The <code>keyword_tokenizer</code> field (inside <code>indexing_options</code>) controls how text is split into tokens. Changing this triggers a full reindex.</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>porter</code></td>
<td>Yes</td>
<td>Applies Porter stemming. &quot;running&quot; matches &quot;run.&quot; Best for natural language.</td>
</tr>
<tr>
<td><code>trigram</code></td>
<td>No</td>
<td>Overlapping 3-character windows. &quot;config&quot; matches &quot;configuration.&quot; Best for code.</td>
</tr>
</tbody>
</table>
<h2 id="keyword-match-mode">Keyword match mode</h2>
<p>The <code>keyword_match_mode</code> field (inside <code>retrieval_options</code>) controls how multiple query terms are combined.</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>and</code></td>
<td>Yes</td>
<td>All query terms must appear. Higher precision, fewer results.</td>
</tr>
<tr>
<td><code>or</code></td>
<td>No</td>
<td>Any query term can match. Higher recall, more results.</td>
</tr>
</tbody>
</table>
<p>You can override <code>keyword_match_mode</code> per request:</p>
<pre><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			keyword_match_mode: &quot;or&quot;,&#10;		},&#10;	},&#10;});&#10;</code></pre>
<h2 id="limits">Limits</h2>
<p>Instances with keyword search enabled support up to 500,000 files per instance on the Workers Paid tier, compared to 1,000,000 for vector-only instances. Refer to <a href="/ai-search/platform/limits-pricing/">Limits and pricing</a> for the full list of limits.</p>
