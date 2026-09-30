<p>The <code>env.AI.autorag()</code> binding is the legacy API for AI Search. It will continue to work, but new projects should use the new AI Search bindings instead. For a step-by-step upgrade guide, refer to <a href="/ai-search/api/migration/workers-binding/">Workers binding migration</a>.</p>
<h3 id="aisearch"><code>aiSearch()</code></h3>
<p>This method searches for relevant results from your data source and generates a response using your default model and the retrieved context:</p>
<pre><code class="language-js">const answer = await env.AI.autorag(&quot;my-autorag&quot;).aiSearch({&#10;	query: &quot;How do I train a llama to deliver coffee?&quot;,&#10;	model: &quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&#10;	rewrite_query: true,&#10;	max_num_results: 2,&#10;	ranking_options: {&#10;		score_threshold: 0.3,&#10;	},&#10;	reranking: {&#10;		enabled: true,&#10;		model: &quot;@cf/baai/bge-reranker-base&quot;,&#10;	},&#10;	stream: true,&#10;});&#10;</code></pre>
<h4 id="parameters">Parameters</h4>
<p><code>query</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<p>The input query.</p>
<hr />
<p><code>model</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>The text-generation model used to generate the response for the query. For a list of valid options, check the AI Search generation model settings. Defaults to the generation model selected in the AI Search settings.</p>
<hr />
<p><code>system_prompt</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>The system prompt for generating the answer.</p>
<hr />
<p><code>rewrite_query</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<p>Rewrites the original query into a search optimized query to improve retrieval accuracy. Defaults to <code>false</code>.</p>
<hr />
<p><code>max_num_results</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<p>The maximum number of results that can be returned from the Vectorize database. Defaults to <code>10</code>. Must be between <code>1</code> and <code>50</code>.</p>
<hr />
<p><code>ranking_options</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<p>Configurations for customizing result ranking. Defaults to <code>{}</code>.</p>
<ul>
<li><code>score_threshold</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The minimum match score required for a result to be considered a match. Defaults to <code>0</code>. Must be between <code>0</code> and <code>1</code>.</li>
</ul>
</li>
</ul>
<p><code>reranking</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<p>Configurations for customizing reranking. Defaults to <code>{}</code>.</p>
<ul>
<li>
<p><code>enabled</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Enables or disables reranking, which reorders retrieved results based on semantic relevance using a reranking model. Defaults to <code>false</code>.</li>
</ul>
</li>
<li>
<p><code>model</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The reranking model to use when reranking is enabled.</li>
</ul>
</li>
</ul>
<p><code>stream</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<p>Returns a stream of results as they are available. Defaults to <code>false</code>.</p>
<p><code>filters</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<p>Narrow down search results based on metadata, like folder and date, so only relevant content is retrieved. For more details, refer to <a href="/ai-search/configuration/retrieval/filtering/">Metadata filtering</a>.</p>
<h4 id="response">Response</h4>
<p>This is the response structure without <code>stream</code> enabled.</p>
<pre><code class="language-json">{&#10;	&quot;object&quot;: &quot;vector_store.search_results.page&quot;,&#10;	&quot;search_query&quot;: &quot;How do I train a llama to deliver coffee?&quot;,&#10;	&quot;response&quot;: &quot;To train a llama to deliver coffee:\n\n1. **Build trust** — Llamas appreciate patience (and decaf).\n2. **Know limits** — Max 3 cups per llama, per `llama-logistics.md`.\n3. **Use voice commands** — Start with \&quot;Espresso Express!\&quot;\n4.&quot;,&#10;	&quot;data&quot;: [&#10;		{&#10;			&quot;file_id&quot;: &quot;llama001&quot;,&#10;			&quot;filename&quot;: &quot;llama/logistics/llama-logistics.md&quot;,&#10;			&quot;score&quot;: 0.45,&#10;			&quot;attributes&quot;: {&#10;				&quot;modified_date&quot;: 1735689600000,&#10;				&quot;folder&quot;: &quot;llama/logistics/&quot;&#10;			},&#10;			&quot;content&quot;: [&#10;				{&#10;					&quot;id&quot;: &quot;llama001&quot;,&#10;					&quot;type&quot;: &quot;text&quot;,&#10;					&quot;text&quot;: &quot;Llamas can carry 3 drinks max.&quot;&#10;				}&#10;			]&#10;		},&#10;		{&#10;			&quot;file_id&quot;: &quot;llama042&quot;,&#10;			&quot;filename&quot;: &quot;llama/llama-commands.md&quot;,&#10;			&quot;score&quot;: 0.4,&#10;			&quot;attributes&quot;: {&#10;				&quot;modified_date&quot;: 1735689600000,&#10;				&quot;folder&quot;: &quot;llama/&quot;&#10;			},&#10;			&quot;content&quot;: [&#10;				{&#10;					&quot;id&quot;: &quot;llama042&quot;,&#10;					&quot;type&quot;: &quot;text&quot;,&#10;					&quot;text&quot;: &quot;Start with basic commands like &#x27;Espresso Express!&#x27; Llamas love alliteration.&quot;&#10;				}&#10;			]&#10;		}&#10;	],&#10;	&quot;has_more&quot;: false,&#10;	&quot;next_page&quot;: null&#10;}&#10;</code></pre>
<h3 id="search"><code>search()</code></h3>
<p>This method searches for results from your corpus and returns the relevant results:</p>
<pre><code class="language-js">const answer = await env.AI.autorag(&quot;my-autorag&quot;).search({&#10;	query: &quot;How do I train a llama to deliver coffee?&quot;,&#10;	rewrite_query: true,&#10;	max_num_results: 2,&#10;	ranking_options: {&#10;		score_threshold: 0.3,&#10;	},&#10;	reranking: {&#10;		enabled: true,&#10;		model: &quot;@cf/baai/bge-reranker-base&quot;,&#10;	},&#10;});&#10;</code></pre>
<h4 id="parameters-1">Parameters</h4>
<p><code>messages</code> <span class="nb-type">array</span> <span class="nb-metainfo">required</span></p>
<p>An array of message objects. Each message has:</p>
<ul>
<li><code>content</code> <span class="nb-type">string</span> - The search query content.</li>
<li><code>role</code> <span class="nb-type">string</span> - The role: <code>user</code>, <code>system</code>, or <code>assistant</code>.</li>
</ul>
<hr />
<p><code>ai_search_options</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<p>Per-request overrides for retrieval and model behavior. Supports the following nested options:</p>
<ul>
<li><code>retrieval.filters</code> <span class="nb-type">object</span> - Narrow down search results based on metadata. Refer to <a href="/ai-search/configuration/retrieval/filtering/">Metadata filtering</a> for syntax and examples.</li>
<li><code>retrieval.max_num_results</code> <span class="nb-type">number</span> - Maximum number of chunks to return. Defaults to <code>10</code>, maximum <code>50</code>.</li>
<li><code>retrieval.retrieval_type</code> <span class="nb-type">string</span> - One of <code>vector</code>, <code>keyword</code>, or <code>hybrid</code>.</li>
<li><code>retrieval.match_threshold</code> <span class="nb-type">number</span> - Minimum similarity score (0-1). Defaults to <code>0.4</code>.</li>
<li><code>cache.enabled</code> <span class="nb-type">boolean</span> - Override the instance-level cache setting for this request.</li>
<li><code>reranking.enabled</code> <span class="nb-type">boolean</span> - Override the instance-level reranking setting for this request.</li>
</ul>
<hr />
<p>For the full list of optional parameters, refer to the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/search/">Search API reference</a>.</p>
<h4 id="response-1">Response</h4>
<pre><code class="language-json">{&#10;	&quot;object&quot;: &quot;vector_store.search_results.page&quot;,&#10;	&quot;search_query&quot;: &quot;How do I train a llama to deliver coffee?&quot;,&#10;	&quot;data&quot;: [&#10;		{&#10;			&quot;file_id&quot;: &quot;llama001&quot;,&#10;			&quot;filename&quot;: &quot;llama/logistics/llama-logistics.md&quot;,&#10;			&quot;score&quot;: 0.45,&#10;			&quot;attributes&quot;: {&#10;				&quot;modified_date&quot;: 1735689600000,&#10;				&quot;folder&quot;: &quot;llama/logistics/&quot;&#10;			},&#10;			&quot;content&quot;: [&#10;				{&#10;					&quot;id&quot;: &quot;llama001&quot;,&#10;					&quot;type&quot;: &quot;text&quot;,&#10;					&quot;text&quot;: &quot;Llamas can carry 3 drinks max.&quot;&#10;				}&#10;			]&#10;		},&#10;		{&#10;			&quot;file_id&quot;: &quot;llama042&quot;,&#10;			&quot;filename&quot;: &quot;llama/llama-commands.md&quot;,&#10;			&quot;score&quot;: 0.4,&#10;			&quot;attributes&quot;: {&#10;				&quot;modified_date&quot;: 1735689600000,&#10;				&quot;folder&quot;: &quot;llama/&quot;&#10;			},&#10;			&quot;content&quot;: [&#10;				{&#10;					&quot;id&quot;: &quot;llama042&quot;,&#10;					&quot;type&quot;: &quot;text&quot;,&#10;					&quot;text&quot;: &quot;Start with basic commands like &#x27;Espresso Express!&#x27; Llamas love alliteration.&quot;&#10;				}&#10;			]&#10;		}&#10;	],&#10;	&quot;has_more&quot;: false,&#10;	&quot;next_page&quot;: null&#10;}&#10;</code></pre>
