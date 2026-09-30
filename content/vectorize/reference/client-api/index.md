<p>This page covers the Vectorize API available within <a href="/workers/">Cloudflare Workers</a>, including usage examples.</p>
<h2 id="operations">Operations</h2>
<h3 id="insert-vectors">Insert vectors</h3>
<pre><code class="language-ts">let vectorsToInsert = [&#10;	{ id: &quot;123&quot;, values: [32.4, 6.5, 11.2, 10.3, 87.9] },&#10;	{ id: &quot;456&quot;, values: [2.5, 7.8, 9.1, 76.9, 8.5] },&#10;];&#10;let inserted = await env.YOUR_INDEX.insert(vectorsToInsert);&#10;</code></pre>
<p>Inserts vectors into the index. Vectorize inserts are asynchronous and the insert operation returns a mutation identifier unique for that operation. It typically takes a few seconds for inserted vectors to be available for querying in a Vectorize index.</p>
<p>If vectors with the same vector ID already exist in the index, only the vectors with new IDs will be inserted.</p>
<p>If you need to update existing vectors, use the <a href="#upsert-vectors">upsert</a> operation.</p>
<h3 id="upsert-vectors">Upsert vectors</h3>
<pre><code class="language-ts">let vectorsToUpsert = [&#10;	{ id: &quot;123&quot;, values: [32.4, 6.5, 11.2, 10.3, 87.9] },&#10;	{ id: &quot;456&quot;, values: [2.5, 7.8, 9.1, 76.9, 8.5] },&#10;	{ id: &quot;768&quot;, values: [29.1, 5.7, 12.9, 15.4, 1.1] },&#10;];&#10;let upserted = await env.YOUR_INDEX.upsert(vectorsToUpsert);&#10;</code></pre>
<p>Upserts vectors into an index. Vectorize upserts are asynchronous and the upsert operation returns a mutation identifier unique for that operation. It typically takes a few seconds for upserted vectors to be available for querying in a Vectorize index.</p>
<p>An upsert operation will insert vectors into the index if vectors with the same ID do not exist, and overwrite vectors with the same ID.</p>
<p>Upserting does not merge or combine the values or metadata of an existing vector with the upserted vector: the upserted vector replaces the existing vector in full.</p>
<h3 id="query-vectors">Query vectors</h3>
<pre><code class="language-ts">let queryVector = [32.4, 6.55, 11.2, 10.3, 87.9];&#10;let matches = await env.YOUR_INDEX.query(queryVector);&#10;</code></pre>
<p>Query an index with the provided vector, returning the score(s) of the closest vectors based on the configured distance metric.</p>
<ul>
<li>Configure the number of returned matches by setting <code>topK</code> (default: 5)</li>
<li>Return vector values by setting <code>returnValues: true</code> (default: false)</li>
<li>Return vector metadata by setting <code>returnMetadata: 'indexed'</code> or <code>returnMetadata: 'all'</code> (default: 'none')</li>
</ul>
<pre><code class="language-ts">let matches = await env.YOUR_INDEX.query(queryVector, {&#10;	topK: 5,&#10;	returnValues: true,&#10;	returnMetadata: &quot;all&quot;,&#10;});&#10;</code></pre>
<h4 id="topk">topK</h4>
<p>The <code>topK</code> can be configured to specify the number of matches returned by the query operation. Vectorize now supports an upper limit of <code>100</code> for the <code>topK</code> value. However, for a query operation with <code>returnValues</code> set to <code>true</code> or <code>returnMetadata</code> set to <code>all</code>, <code>topK</code> is limited to a maximum value of <code>50</code>.</p>
<h4 id="returnmetadata">returnMetadata</h4>
<p>The <code>returnMetadata</code> field provides three ways to fetch vector metadata while querying:</p>
<ol>
<li><code>none</code>: Do not fetch metadata.</li>
<li><code>indexed</code>: Fetched metadata only for the indexed metadata fields. There is no latency overhead with this option, but long text fields may be truncated.</li>
<li><code>all</code>: Fetch all metadata associated with a vector. Queries may run slower with this option, and <code>topK</code> is limited to 50.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="topk-and-returnmetadata-for-legacy-vectorize-indexes">`topK` and `returnMetadata` for legacy Vectorize indexes</h3>
@markup("md", "content/.markup/bodies/15259.md")
</aside>
<h3 id="query-vectors-by-id">Query vectors by ID</h3>
<pre><code class="language-ts">let matches = await env.YOUR_INDEX.queryById(&quot;some-vector-id&quot;);&#10;</code></pre>
<p>Query an index using a vector that is already present in the index.</p>
<p>Query options remain the same as the query operation described above.</p>
<pre><code class="language-ts">let matches = await env.YOUR_INDEX.queryById(&quot;some-vector-id&quot;, {&#10;	topK: 5,&#10;	returnValues: true,&#10;	returnMetadata: &quot;all&quot;,&#10;});&#10;</code></pre>
<h3 id="get-vectors-by-id">Get vectors by ID</h3>
<pre><code class="language-ts">let ids = [&quot;11&quot;, &quot;22&quot;, &quot;33&quot;, &quot;44&quot;];&#10;const vectors = await env.YOUR_INDEX.getByIds(ids);&#10;</code></pre>
<p>Retrieves the specified vectors by their ID, including values and metadata.</p>
<h3 id="delete-vectors-by-id">Delete vectors by ID</h3>
<pre><code class="language-ts">let idsToDelete = [&quot;11&quot;, &quot;22&quot;, &quot;33&quot;, &quot;44&quot;];&#10;const deleted = await env.YOUR_INDEX.deleteByIds(idsToDelete);&#10;</code></pre>
<p>Deletes the vector IDs provided from the current index. Vectorize deletes are asynchronous and the delete operation returns a mutation identifier unique for that operation. It typically takes a few seconds for vectors to be removed from the Vectorize index.</p>
<h3 id="retrieve-index-details">Retrieve index details</h3>
<pre><code class="language-ts">const details = await env.YOUR_INDEX.describe();&#10;</code></pre>
<p>Retrieves the configuration of a given index directly, including its configured <code>dimensions</code> and distance <code>metric</code>.</p>
<h3 id="list-vectors">List Vectors</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="python-sdk-availability">Python SDK availability</h3>
@markup("md", "content/.markup/bodies/15258.md")
</aside>
<p>List all vector identifiers in an index using paginated requests, returning up to 1000 vector identifiers per page.</p>
<pre><code class="language-sh">wrangler vectorize list-vectors &lt;index-name&gt; [--count=&lt;number&gt;] [--cursor=&lt;cursor-string&gt;]&#10;</code></pre>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>&lt;index-name&gt;</code> - The name of your Vectorize index</li>
<li><code>--count</code> (optional) - Number of vector IDs to return per page. Must be between 1 and 1000 (default: 100)</li>
<li><code>--cursor</code> (optional) - Pagination cursor from the previous response to continue listing from that position</li>
</ul>
<p>For detailed guidance on pagination behavior and best practices, refer to <a href="/vectorize/best-practices/list-vectors/">List vectors best practices</a>.</p>
<h3 id="create-metadata-index">Create Metadata Index</h3>
<p>Enable metadata filtering on the specified property. Limited to 10 properties.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wrangler-version-3-71-0-required">Wrangler version 3.71.0 required</h3>
@markup("md", "content/.markup/bodies/15257.md")
</aside>
<p>Run the following <code>wrangler vectorize</code> command:</p>
<pre><code class="language-sh">wrangler vectorize create-metadata-index &lt;index-name&gt; --property-name=&#x27;some-prop&#x27; --type=&#x27;string&#x27;&#10;</code></pre>
<h3 id="delete-metadata-index">Delete Metadata Index</h3>
<p>Allow Vectorize to delete the specified metadata index.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wrangler-version-3-71-0-required-1">Wrangler version 3.71.0 required</h3>
@markup("md", "content/.markup/bodies/15256.md")
</aside>
<p>Run the following <code>wrangler vectorize</code> command:</p>
<pre><code class="language-sh">wrangler vectorize delete-metadata-index &lt;index-name&gt; --property-name=&#x27;some-prop&#x27;&#10;</code></pre>
<h3 id="list-metadata-indexes">List Metadata Indexes</h3>
<p>List metadata properties on which metadata filtering is enabled.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wrangler-version-3-71-0-required-2">Wrangler version 3.71.0 required</h3>
@markup("md", "content/.markup/bodies/15255.md")
</aside>
<p>Run the following <code>wrangler vectorize</code> command:</p>
<pre><code class="language-sh">wrangler vectorize list-metadata-index &lt;index-name&gt;&#10;</code></pre>
<h3 id="get-index-info">Get Index Info</h3>
<p>Get additional details about the index.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wrangler-version-3-71-0-required-3">Wrangler version 3.71.0 required</h3>
@markup("md", "content/.markup/bodies/15254.md")
</aside>
<p>Run the following <code>wrangler vectorize</code> command:</p>
<pre><code class="language-sh">wrangler vectorize info &lt;index-name&gt;&#10;</code></pre>
<h2 id="vectors">Vectors</h2>
<p>A vector represents the vector embedding output from a machine learning model.</p>
<ul>
<li><code>id</code> - a unique <code>string</code> identifying the vector in the index. This should map back to the ID of the document, object or database identifier that the vector values were generated from.</li>
<li><code>namespace</code> - an optional partition key within a index. Operations are performed per-namespace, so this can be used to create isolated segments within a larger index.</li>
<li><code>values</code> - an array of <code>number</code>, <code>Float32Array</code>, or <code>Float64Array</code> as the vector embedding itself. This must be a dense array, and the length of this array must match the <code>dimensions</code> configured on the index.</li>
<li><code>metadata</code> - an optional set of key-value pairs that can be used to store additional metadata alongside a vector.</li>
</ul>
<pre><code class="language-ts">let vectorExample = {&#10;	id: &quot;12345&quot;,&#10;	values: [32.4, 6.55, 11.2, 10.3, 87.9],&#10;	metadata: {&#10;		key: &quot;value&quot;,&#10;		hello: &quot;world&quot;,&#10;		url: &quot;r2://bucket/some/object.json&quot;,&#10;	},&#10;};&#10;</code></pre>
<h2 id="binding-to-a-worker">Binding to a Worker</h2>
<p><a href="/workers/runtime-apis/bindings/">Bindings</a> allow you to attach resources, including Vectorize indexes or R2 buckets, to your Worker.</p>
<p>Bindings are defined in either the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> associated with your Workers project, or via the Cloudflare dashboard for your project.</p>
<p>Vectorize indexes are bound by name. A binding for an index named <code>production-doc-search</code> would resemble the below:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15260.md")
</div>
<p>Refer to the <a href="/workers/wrangler/configuration/#vectorize-indexes">bindings documentation</a> for more details.</p>
<h2 id="typescript-types">TypeScript Types</h2>
<p>If you're using TypeScript, run <a href="/workers/wrangler/commands/general/#types"><code>wrangler types</code></a> whenever you modify your Wrangler configuration file. This generates types for the <code>env</code> object based on your bindings, as well as <a href="/workers/languages/typescript/">runtime types</a>.</p>
