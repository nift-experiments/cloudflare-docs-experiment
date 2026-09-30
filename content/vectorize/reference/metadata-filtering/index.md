<p>In addition to providing an input vector to your query, you can also filter by <a href="/vectorize/best-practices/insert-vectors/#metadata">vector metadata</a> associated with every vector. Query results will only include vectors that match the <code>filter</code> criteria, meaning that <code>filter</code> is applied first, and the <code>topK</code> results are taken from the filtered set.</p>
<p>By using metadata filtering to limit the scope of a query, you can filter by specific customer IDs, tenant, product category or any other metadata you associate with your vectors.</p>
<h2 id="metadata-indexes">Metadata indexes</h2>
<p>Vectorize supports <a href="/vectorize/best-practices/insert-vectors/#namespaces">namespace</a> filtering by default, but to filter on another metadata property of your vectors, you'll need to create a metadata index. You can create up to 10 metadata indexes per Vectorize index.</p>
<p>Metadata indexes for properties of type <code>string</code>, <code>number</code> and <code>boolean</code> are supported. Please refer to <a href="/vectorize/get-started/intro/#4-optional-create-metadata-indexes">Create metadata indexes</a> for details.</p>
<p>You can store up to 10KiB of metadata per vector. See <a href="/vectorize/platform/limits/">Vectorize Limits</a> for a complete list of limits.</p>
<p>For metadata indexes of type <code>number</code>, the indexed number precision is that of float64.</p>
<p>For metadata indexes of type <code>string</code>, each vector indexes the first 64B of the string data truncated on UTF-8 character boundaries to the longest well-formed UTF-8 substring within that limit, so vectors are filterable on the first 64B of their value for each indexed property.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="enable-metadata-filtering">Enable metadata filtering</h3>
@markup("md", "content/.markup/bodies/15253.md")
</aside>
<h2 id="supported-operations">Supported operations</h2>
<p>An optional <code>filter</code> property on <code>query()</code> method specifies metadata filters:</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>$eq</code></td>
<td>Equals</td>
</tr>
<tr>
<td><code>$ne</code></td>
<td>Not equals</td>
</tr>
<tr>
<td><code>$in</code></td>
<td>In</td>
</tr>
<tr>
<td><code>$nin</code></td>
<td>Not in</td>
</tr>
<tr>
<td><code>$lt</code></td>
<td>Less than</td>
</tr>
<tr>
<td><code>$lte</code></td>
<td>Less than or equal to</td>
</tr>
<tr>
<td><code>$gt</code></td>
<td>Greater than</td>
</tr>
<tr>
<td><code>$gte</code></td>
<td>Greater than or equal to</td>
</tr>
</tbody>
</table>
<ul>
<li><code>filter</code> must be non-empty object whose compact JSON representation must be less than 2048 bytes.</li>
<li><code>filter</code> object keys cannot be empty, contain <code>&quot; | .</code> (dot is reserved for nesting), start with <code>$</code>, or be longer than 512 characters.</li>
<li>For <code>$eq</code> and <code>$ne</code>, <code>filter</code> object non-nested values can be <code>string</code>, <code>number</code>, <code>boolean</code>, or <code>null</code> values.</li>
<li>For <code>$in</code> and <code>$nin</code>, <code>filter</code> object values can be arrays of <code>string</code>, <code>number</code>, <code>boolean</code>, or <code>null</code> values.</li>
<li>Upper-bound range queries (i.e. <code>$lt</code> and <code>$lte</code>) can be combined with lower-bound range queries (i.e. <code>$gt</code> and <code>$gte</code>) within the same filter. Other combinations are not allowed.</li>
<li>For range queries (i.e. <code>$lt</code>, <code>$lte</code>, <code>$gt</code>, <code>$gte</code>), <code>filter</code> object non-nested values can be <code>string</code> or <code>number</code> values. Strings are ordered lexicographically.</li>
<li>Range queries involving a large number of vectors (~10M and above) may experience reduced accuracy.</li>
</ul>
<h3 id="namespace-versus-metadata-filtering">Namespace versus metadata filtering</h3>
<p>Both <a href="/vectorize/best-practices/insert-vectors/#namespaces">namespaces</a> and metadata filtering narrow the vector search space for a query. Consider the following when evaluating both filter types:</p>
<ul>
<li>A namespace filter is applied before metadata filter(s).</li>
<li>A vector can only be part of a single namespace with the documented <a href="/vectorize/platform/limits/">limits</a>. Vector metadata can contain multiple key-value pairs up to <a href="/vectorize/platform/limits/">metadata per vector limits</a>. Metadata values support different types (<code>string</code>, <code>boolean</code>, and others), therefore offering more flexibility.</li>
</ul>
<h3 id="valid-filter-examples">Valid <code>filter</code> examples</h3>
<h4 id="implicit-eq-operator">Implicit <code>$eq</code> operator</h4>
<pre><code class="language-json">{ &quot;streaming_platform&quot;: &quot;netflix&quot; }&#10;</code></pre>
<h4 id="explicit-operator">Explicit operator</h4>
<pre><code class="language-json">{ &quot;someKey&quot;: { &quot;$ne&quot;: &quot;hbo&quot; } }&#10;</code></pre>
<h4 id="in-operator"><code>$in</code> operator</h4>
<pre><code class="language-json">{ &quot;someKey&quot;: { &quot;$in&quot;: [&quot;hbo&quot;, &quot;netflix&quot;] } }&#10;</code></pre>
<h4 id="nin-operator"><code>$nin</code> operator</h4>
<pre><code class="language-json">{ &quot;someKey&quot;: { &quot;$nin&quot;: [&quot;hbo&quot;, &quot;netflix&quot;] } }&#10;</code></pre>
<h4 id="range-query-involving-numbers">Range query involving numbers</h4>
<pre><code class="language-json">{ &quot;timestamp&quot;: { &quot;$gte&quot;: 1734242400, &quot;$lt&quot;: 1734328800 } }&#10;</code></pre>
<h4 id="range-query-involving-strings">Range query involving strings</h4>
<p>Range queries can implement <strong>prefix searching</strong> on string metadata fields. This is also like a <strong>starts_with</strong> filter.</p>
<p>For example, the following filter matches all values starting with &quot;net&quot;:</p>
<pre><code class="language-json">{ &quot;someKey&quot;: { &quot;$gte&quot;: &quot;net&quot;, &quot;$lt&quot;: &quot;neu&quot; } }&#10;</code></pre>
<h4 id="implicit-logical-and-with-multiple-keys">Implicit logical <code>AND</code> with multiple keys</h4>
<pre><code class="language-json">{ &quot;pandas.nice&quot;: 42, &quot;someKey&quot;: { &quot;$ne&quot;: &quot;someValue&quot; } }&#10;</code></pre>
<h4 id="keys-define-nesting-with-dot">Keys define nesting with <code>.</code> (dot)</h4>
<pre><code class="language-json">{ &quot;pandas.nice&quot;: 42 }&#10;&#10;// looks for { &quot;pandas&quot;: { &quot;nice&quot;: 42 } }&#10;</code></pre>
<h2 id="examples">Examples</h2>
<h3 id="add-metadata">Add metadata</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="using-legacy-vectorize-v1-indexes">Using legacy Vectorize (V1) indexes?</h3>
@markup("md", "content/.markup/bodies/15252.md")
</aside>
<p>With the following index definition:</p>
<pre><code class="language-sh">npx wrangler vectorize create tutorial-index --dimensions=32 --metric=cosine&#10;</code></pre>
<p>Create metadata indexes:</p>
<pre><code class="language-sh">npx wrangler vectorize create-metadata-index tutorial-index --property-name=url --type=string&#10;</code></pre>
<pre><code class="language-sh">npx wrangler vectorize create-metadata-index tutorial-index --property-name=streaming_platform --type=string&#10;</code></pre>
<p>Metadata can be added when <a href="/vectorize/best-practices/insert-vectors/#examples">inserting or upserting vectors</a>.</p>
<pre><code class="language-ts">const newMetadataVectors: Array&lt;VectorizeVector&gt; = [&#10;	{&#10;		id: &quot;1&quot;,&#10;		values: [32.4, 74.1, 3.2, ...],&#10;		metadata: { url: &quot;/products/sku/13913913&quot;, streaming_platform: &quot;netflix&quot; },&#10;	},&#10;	{&#10;		id: &quot;2&quot;,&#10;		values: [15.1, 19.2, 15.8, ...],&#10;		metadata: { url: &quot;/products/sku/10148191&quot;, streaming_platform: &quot;hbo&quot; },&#10;	},&#10;	{&#10;		id: &quot;3&quot;,&#10;		values: [0.16, 1.2, 3.8, ...],&#10;		metadata: { url: &quot;/products/sku/97913813&quot;, streaming_platform: &quot;amazon&quot; },&#10;	},&#10;	{&#10;		id: &quot;4&quot;,&#10;		values: [75.1, 67.1, 29.9, ...],&#10;		metadata: { url: &quot;/products/sku/418313&quot;, streaming_platform: &quot;netflix&quot; },&#10;	},&#10;	{&#10;		id: &quot;5&quot;,&#10;		values: [58.8, 6.7, 3.4, ...],&#10;		metadata: { url: &quot;/products/sku/55519183&quot;, streaming_platform: &quot;hbo&quot; },&#10;	},&#10;];&#10;&#10;// Upsert vectors with added metadata, returning a count of the vectors upserted and their vector IDs&#10;let upserted = await env.YOUR_INDEX.upsert(newMetadataVectors);&#10;</code></pre>
<h3 id="query-examples">Query examples</h3>
<p>Use the <code>query()</code> method:</p>
<pre><code class="language-ts">let queryVector: Array&lt;number&gt; = [54.8, 5.5, 3.1, ...];&#10;let originalMatches = await env.YOUR_INDEX.query(queryVector, {&#10;	topK: 3,&#10;	returnValues: true,&#10;	returnMetadata: &#x27;all&#x27;,&#10;});&#10;</code></pre>
<p>Results without metadata filtering:</p>
<pre><code class="language-json">{&#10;	&quot;count&quot;: 3,&#10;	&quot;matches&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;5&quot;,&#10;			&quot;score&quot;: 0.999909486,&#10;			&quot;values&quot;: [58.79999923706055, 6.699999809265137, 3.4000000953674316],&#10;			&quot;metadata&quot;: {&#10;				&quot;url&quot;: &quot;/products/sku/55519183&quot;,&#10;				&quot;streaming_platform&quot;: &quot;hbo&quot;&#10;			}&#10;		},&#10;		{&#10;			&quot;id&quot;: &quot;4&quot;,&#10;			&quot;score&quot;: 0.789848214,&#10;			&quot;values&quot;: [75.0999984741211, 67.0999984741211, 29.899999618530273],&#10;			&quot;metadata&quot;: {&#10;				&quot;url&quot;: &quot;/products/sku/418313&quot;,&#10;				&quot;streaming_platform&quot;: &quot;netflix&quot;&#10;			}&#10;		},&#10;		{&#10;			&quot;id&quot;: &quot;2&quot;,&#10;			&quot;score&quot;: 0.611976262,&#10;			&quot;values&quot;: [15.100000381469727, 19.200000762939453, 15.800000190734863],&#10;			&quot;metadata&quot;: {&#10;				&quot;url&quot;: &quot;/products/sku/10148191&quot;,&#10;				&quot;streaming_platform&quot;: &quot;hbo&quot;&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>The same <code>query()</code> method with a <code>filter</code> property supports metadata filtering.</p>
<pre><code class="language-ts">let queryVector: Array&lt;number&gt; = [54.8, 5.5, 3.1, ...];&#10;let metadataMatches = await env.YOUR_INDEX.query(queryVector, {&#10;	topK: 3,&#10;	filter: { streaming_platform: &quot;netflix&quot; },&#10;	returnValues: true,&#10;	returnMetadata: &#x27;all&#x27;,&#10;});&#10;</code></pre>
<p>Results with metadata filtering:</p>
<pre><code class="language-json">{&#10;	&quot;count&quot;: 2,&#10;	&quot;matches&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;4&quot;,&#10;			&quot;score&quot;: 0.789848214,&#10;			&quot;values&quot;: [75.0999984741211, 67.0999984741211, 29.899999618530273],&#10;			&quot;metadata&quot;: {&#10;				&quot;url&quot;: &quot;/products/sku/418313&quot;,&#10;				&quot;streaming_platform&quot;: &quot;netflix&quot;&#10;			}&#10;		},&#10;		{&#10;			&quot;id&quot;: &quot;1&quot;,&#10;			&quot;score&quot;: 0.491185264,&#10;			&quot;values&quot;: [32.400001525878906, 74.0999984741211, 3.200000047683716],&#10;			&quot;metadata&quot;: {&#10;				&quot;url&quot;: &quot;/products/sku/13913913&quot;,&#10;				&quot;streaming_platform&quot;: &quot;netflix&quot;&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<ul>
<li>As of now, metadata indexes need to be created for Vectorize indexes <em>before</em> vectors can be inserted to support metadata filtering.</li>
<li>Only indexes created on or after 2023-12-06 support metadata filtering. Previously created indexes cannot be migrated to support metadata filtering.</li>
</ul>
