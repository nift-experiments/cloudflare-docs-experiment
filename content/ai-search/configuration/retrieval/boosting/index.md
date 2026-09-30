<p>Boosting lets you bias search results toward documents with specific metadata characteristics. For example, you can promote recent documents, surface higher-priority pages, or deprioritize drafts. Boosting re-ranks results without replacing semantic relevance.</p>
<h2 id="how-it-works">How it works</h2>
<p>Boosting applies after the initial retrieval step and before <a href="/ai-search/configuration/retrieval/reranking/">reranking</a> (if enabled):</p>
<ol>
<li><strong>Search</strong>: AI Search retrieves up to 50 candidate chunks using vector search, keyword search, or both.</li>
<li><strong>Boost</strong>: Each candidate is re-scored using the metadata fields you specify in <code>boost_by</code>. The boost is additive to the original retrieval score.</li>
<li><strong>Rerank</strong>: If reranking is enabled, the boosted results are reranked by a reranking model.</li>
<li><strong>Return</strong>: The top <code>max_num_results</code> are returned.</li>
</ol>
<p>Boosting can change the order of results within the candidate set, but cannot promote a chunk that the initial search step did not retrieve.</p>
<h2 id="supported-fields">Supported fields</h2>
<p>You can boost by the built-in <code>timestamp</code> field or by any field defined in your <a href="/ai-search/configuration/indexing/metadata/#define-a-schema">custom metadata schema</a>.</p>
<table>
<thead>
<tr>
<th>Field type</th>
<th>Supported directions</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>datetime</code></td>
<td><code>asc</code>, <code>desc</code>, <code>exists</code>, <code>not_exists</code></td>
</tr>
<tr>
<td><code>number</code></td>
<td><code>asc</code>, <code>desc</code>, <code>exists</code>, <code>not_exists</code></td>
</tr>
<tr>
<td><code>text</code></td>
<td><code>exists</code>, <code>not_exists</code> only</td>
</tr>
<tr>
<td><code>boolean</code></td>
<td><code>exists</code>, <code>not_exists</code> only</td>
</tr>
</tbody>
</table>
<h3 id="directions">Directions</h3>
<p>The direction controls how the field value affects the ranking of each result:</p>
<table>
<thead>
<tr>
<th>Direction</th>
<th>Effect</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>desc</code></td>
<td>Higher field values score higher (for example, most recent).</td>
</tr>
<tr>
<td><code>asc</code></td>
<td>Lower field values score higher (for example, lowest cost).</td>
</tr>
<tr>
<td><code>exists</code></td>
<td>Documents that have the field score higher.</td>
</tr>
<tr>
<td><code>not_exists</code></td>
<td>Documents that do not have the field score higher.</td>
</tr>
</tbody>
</table>
<p>If you omit <code>direction</code>, AI Search applies a default based on the field type:</p>
<table>
<thead>
<tr>
<th>Field type</th>
<th>Default direction</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>number</code>, <code>datetime</code>, <code>timestamp</code></td>
<td><code>asc</code></td>
</tr>
<tr>
<td><code>text</code>, <code>boolean</code></td>
<td><code>exists</code></td>
</tr>
</tbody>
</table>
<p>Using <code>asc</code> or <code>desc</code> on a <code>text</code> or <code>boolean</code> field returns an error.</p>
<h2 id="configuration">Configuration</h2>
<p>Specify <code>boost_by</code> as an array of up to 3 objects when creating or updating an instance. Each object must reference a unique field.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>field</code></td>
<td>string</td>
<td>Yes</td>
<td>Metadata field name or <code>timestamp</code>. Must match your schema. Case-insensitive.</td>
</tr>
<tr>
<td><code>direction</code></td>
<td>string</td>
<td>No</td>
<td>One of <code>asc</code>, <code>desc</code>, <code>exists</code>, <code>not_exists</code>. Defaults by type.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;	retrieval_options: {&#10;		boost_by: [&#10;			{ field: &quot;timestamp&quot;, direction: &quot;desc&quot; },&#10;			{ field: &quot;priority&quot;, direction: &quot;desc&quot; },&#10;		],&#10;	},&#10;});&#10;</code></pre>
<p>To remove boosting, set <code>boost_by</code> to an empty array when updating the instance.</p>
<h2 id="per-request-overrides">Per-request overrides</h2>
<p>You can override <code>boost_by</code> on individual requests using <code>ai_search_options.retrieval</code>. Per-request values fully replace the instance-level default.</p>
<pre><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			boost_by: [{ field: &quot;timestamp&quot;, direction: &quot;desc&quot; }],&#10;		},&#10;	},&#10;});&#10;</code></pre>
<p>To disable boosting for a single request, pass an empty array:</p>
<pre><code class="language-ts">const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			boost_by: [],&#10;		},&#10;	},&#10;});&#10;</code></pre>
<h2 id="common-patterns">Common patterns</h2>
<p>Here are some common ways to use relevance boosting:</p>
<table>
<thead>
<tr>
<th>Pattern</th>
<th>Configuration</th>
</tr>
</thead>
<tbody>
<tr>
<td>Prioritize recent documents</td>
<td><code>[{ &quot;field&quot;: &quot;timestamp&quot;, &quot;direction&quot;: &quot;desc&quot; }]</code></td>
</tr>
<tr>
<td>Promote by custom priority</td>
<td><code>[{ &quot;field&quot;: &quot;priority&quot;, &quot;direction&quot;: &quot;desc&quot; }]</code></td>
</tr>
<tr>
<td>Boost lower-cost options</td>
<td><code>[{ &quot;field&quot;: &quot;cost&quot;, &quot;direction&quot;: &quot;asc&quot; }]</code></td>
</tr>
<tr>
<td>Promote documents with an author</td>
<td><code>[{ &quot;field&quot;: &quot;author&quot;, &quot;direction&quot;: &quot;exists&quot; }]</code></td>
</tr>
<tr>
<td>Suppress drafts</td>
<td><code>[{ &quot;field&quot;: &quot;draft&quot;, &quot;direction&quot;: &quot;not_exists&quot; }]</code></td>
</tr>
<tr>
<td>Combine recency and priority</td>
<td><code>[{ &quot;field&quot;: &quot;timestamp&quot;, &quot;direction&quot;: &quot;desc&quot; }, { &quot;field&quot;: &quot;priority&quot;, &quot;direction&quot;: &quot;desc&quot; }]</code></td>
</tr>
</tbody>
</table>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Maximum of 3 boost fields per request.</li>
<li>Field names must match a field in your custom metadata schema or the built-in <code>timestamp</code> field.</li>
<li><code>text</code> and <code>boolean</code> fields only support <code>exists</code> and <code>not_exists</code> directions.</li>
<li>Boost fields within a single request must be unique.</li>
<li>Boosting re-ranks the candidate set from the initial search. It cannot surface documents that were not retrieved.</li>
</ul>
