<p><a href="/workers/">Workers</a> provides a serverless execution environment that allows you to create new applications or augment existing ones. Use a <a href="/workers/runtime-apis/bindings/">Workers binding</a> to create, list, update, and delete AI Search instances from a Cloudflare Worker. You can also check instance configuration and monitor indexing progress.</p>
<h2 id="configure-the-binding">Configure the binding</h2>
<p>To use AI Search with Workers, you must create an AI Search binding. You create bindings by updating your <a href="/workers/wrangler/configuration/">Wrangler configuration</a>. AI Search provides two types of bindings:</p>
<ul>
<li>Namespace binding: <code>ai_search_namespaces</code></li>
<li>Instance binding: <code>ai_search</code></li>
</ul>
<h3 id="namespace-binding">Namespace binding</h3>
<p>Access all instances within a <a href="/ai-search/concepts/namespaces/">namespace</a>. You can get, create, list, and delete instances at runtime.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3075.md")
</div>
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
<td><code>binding</code></td>
<td>string</td>
<td>Yes</td>
<td>The variable name available on <code>env</code>. For example, <code>&quot;AI_SEARCH&quot;</code> makes it accessible as <code>env.AI_SEARCH</code>.</td>
</tr>
<tr>
<td><code>namespace</code></td>
<td>string</td>
<td>Yes</td>
<td>The <a href="/ai-search/concepts/namespaces/">namespace</a> to bind to. A <code>default</code> namespace is created automatically for every account. If the namespace does not exist, Wrangler creates it on deploy.</td>
</tr>
<tr>
<td><code>remote</code></td>
<td>boolean</td>
<td>No</td>
<td>Set to <code>true</code> for local development with <code>wrangler dev</code>.</td>
</tr>
</tbody>
</table>
<h3 id="instance-binding">Instance binding</h3>
<p>Bind directly to a single instance in the <code>default</code> namespace. Use this when you know which instance you need at deploy time.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3076.md")
</div>
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
<td><code>binding</code></td>
<td>string</td>
<td>Yes</td>
<td>The variable name available on <code>env</code>. For example, <code>&quot;MY_SEARCH&quot;</code> makes it accessible as <code>env.MY_SEARCH</code>.</td>
</tr>
<tr>
<td><code>instance_name</code></td>
<td>string</td>
<td>Yes</td>
<td>The name of the AI Search instance. Must exist in the default namespace at deploy time.</td>
</tr>
<tr>
<td><code>remote</code></td>
<td>boolean</td>
<td>No</td>
<td>Set to <code>true</code> for local development with <code>wrangler dev</code>.</td>
</tr>
</tbody>
</table>
<h2 id="namespace-methods">Namespace methods</h2>
<p>The following methods are only available when using the <code>ai_search_namespaces</code> binding. The namespace handle (<code>env.AI_SEARCH</code>) exposes methods for working with instances within a <a href="/ai-search/concepts/namespaces/">namespace</a>.</p>
<h3 id="get"><code>get()</code></h3>
<p>Returns a handle to a specific instance. This is <strong>synchronous</strong> and does not make a network call. The instance is resolved lazily when you call methods like <code>search()</code> or <code>info()</code>.</p>
<pre><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;});&#10;</code></pre>
<h4 id="parameters">Parameters</h4>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td>string</td>
<td>Yes</td>
<td>The name of the instance to get a handle to.</td>
</tr>
</tbody>
</table>
<h3 id="list"><code>list()</code></h3>
<p>Returns all instances within the namespace.</p>
<pre><code class="language-ts">const { result, result_info } = await env.AI_SEARCH.list();&#10;&#10;for (const instance of result) {&#10;	console.log(`${instance.id} (${instance.type}) - ${instance.status}`);&#10;}&#10;// result_info.total_count contains the total number of instances&#10;</code></pre>
<h4 id="parameters-1">Parameters</h4>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>page</code></td>
<td>number</td>
<td>No</td>
<td>The page number to return. Defaults to <code>1</code>.</td>
</tr>
<tr>
<td><code>per_page</code></td>
<td>number</td>
<td>No</td>
<td>The number of instances per page. Defaults to <code>20</code>. Maximum <code>100</code>.</td>
</tr>
<tr>
<td><code>search</code></td>
<td>string</td>
<td>No</td>
<td>Search instances by ID.</td>
</tr>
<tr>
<td><code>order_by</code></td>
<td>string</td>
<td>No</td>
<td>Sort column. Valid value: <code>created_at</code>. Defaults to <code>created_at</code>.</td>
</tr>
<tr>
<td><code>order_by_direction</code></td>
<td>string</td>
<td>No</td>
<td>Sort direction. Valid values: <code>asc</code>, <code>desc</code>. Defaults to <code>desc</code>.</td>
</tr>
</tbody>
</table>
<h4 id="response">Response</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>result</code></td>
<td>array</td>
<td>Array of instance objects.</td>
</tr>
<tr>
<td><code>result[].id</code></td>
<td>string</td>
<td>The instance identifier.</td>
</tr>
<tr>
<td><code>result[].type</code></td>
<td>string</td>
<td>The data source type (<code>r2</code>, <code>web-crawler</code>, or <code>null</code> for empty instances).</td>
</tr>
<tr>
<td><code>result[].source</code></td>
<td>string</td>
<td>The data source location.</td>
</tr>
<tr>
<td><code>result[].status</code></td>
<td>string</td>
<td>The instance status (<code>active</code>, <code>waiting</code>, <code>indexing</code>).</td>
</tr>
<tr>
<td><code>result[].enable</code></td>
<td>boolean</td>
<td>Whether the instance is enabled.</td>
</tr>
<tr>
<td><code>result[].namespace</code></td>
<td>string</td>
<td>The namespace the instance belongs to.</td>
</tr>
<tr>
<td><code>result[].created_at</code></td>
<td>string</td>
<td>ISO 8601 timestamp of when the instance was created.</td>
</tr>
<tr>
<td><code>result[].modified_at</code></td>
<td>string</td>
<td>ISO 8601 timestamp of the last modification.</td>
</tr>
<tr>
<td><code>result_info</code></td>
<td>object</td>
<td>Pagination metadata.</td>
</tr>
<tr>
<td><code>result_info.total_count</code></td>
<td>number</td>
<td>Total number of instances in the namespace.</td>
</tr>
</tbody>
</table>
<h3 id="create"><code>create()</code></h3>
<p>Creates a new instance and returns a handle to it. You can create instances backed by a data source or create empty instances for use with the <a href="/ai-search/api/items/workers-binding/">Items API</a>.</p>
<p><strong>Create an empty instance for file uploads:</strong></p>
<p>AI Search instances come with <a href="/ai-search/configuration/data-source/built-in-storage/">built-in storage</a> where you can upload documents directly.</p>
<pre><code class="language-ts">const instance = await env.AI_SEARCH.create({&#10;	id: &quot;knowledge-base&quot;,&#10;});&#10;&#10;// Upload documents using the Items API&#10;await instance.items.upload(&quot;guide.pdf&quot;, pdfArrayBuffer);&#10;</code></pre>
<p><strong>Create a web-crawler instance:</strong></p>
<p>Automatically crawl and index a website that you own. For more configuration options, refer to <a href="/ai-search/configuration/data-source/website/">Website data source</a>.</p>
<pre><code class="language-ts">const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-docs&quot;,&#10;	type: &quot;web-crawler&quot;,&#10;	source: &quot;developers.cloudflare.com&quot;,&#10;});&#10;</code></pre>
<p><strong>Create an R2-backed instance:</strong></p>
<p>Index documents stored in an <a href="/r2/">R2</a> bucket. For more configuration options, refer to <a href="/ai-search/configuration/data-source/r2/">R2 data source</a>.</p>
<pre><code class="language-ts">const instance = await env.AI_SEARCH.create({&#10;	id: &quot;internal-docs&quot;,&#10;	type: &quot;r2&quot;,&#10;	source: &quot;my-docs-bucket&quot;,&#10;});&#10;</code></pre>
<h4 id="parameters-2">Parameters</h4>
<p><code>id</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<p>The unique identifier for the AI Search instance. Must be 1-64 characters and match the pattern <code>^[a-z0-9_]+(?:-[a-z0-9_]+)*$</code>.</p>
<hr />
<p><code>type</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>The type of data source. Valid values: <code>r2</code>, <code>web-crawler</code>. Required when creating an instance with a data source. Omit when creating an empty instance for use with the <a href="/ai-search/api/items/workers-binding/">Items API</a>.</p>
<hr />
<p><code>source</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>The data source location. For <code>r2</code> type, this is the R2 bucket name. For <code>web-crawler</code> type, this is the website domain. Required when <code>type</code> is specified.</p>
<hr />
<p><code>source_params</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<p>Additional parameters for the data source.</p>
<ul>
<li><code>prefix</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>For R2 sources, limits indexing to objects with this key prefix.</li>
</ul>
</li>
<li><code>r2_jurisdiction</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The jurisdiction for the R2 bucket, for example <code>eu</code>.</li>
</ul>
</li>
<li><code>include_items</code> <span class="nb-type">array</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Glob patterns for paths to include in indexing. For example: <code>[&quot;/blog/**&quot;, &quot;/docs/**/*.html&quot;]</code>.</li>
</ul>
</li>
<li><code>exclude_items</code> <span class="nb-type">array</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Glob patterns for paths to exclude from indexing. For example: <code>[&quot;/admin/**&quot;, &quot;/private/**&quot;]</code>.</li>
</ul>
</li>
<li><code>web_crawler</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Configuration for web crawler sources.</li>
<li><code>parse_type</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>How pages are discovered. Valid values: <code>sitemap</code> (reads XML sitemaps), <code>discover</code> (starts at the source URL and, by default, uses both sitemaps and links found on crawled pages). Defaults to <code>sitemap</code>. Refer to <a href="/ai-search/configuration/data-source/website/parse-types/">Parse types</a>.</li>
</ul>
</li>
<li><code>parse_options</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li><code>include_headers</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Custom HTTP headers to include when crawling.</li>
</ul>
</li>
<li><code>include_images</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Whether to include images in the index.</li>
</ul>
</li>
<li><code>specific_sitemaps</code> <span class="nb-type">array</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Specific sitemap URLs to crawl. For example: <code>[&quot;https://example.com/sitemap.xml&quot;]</code>. Only valid when <code>parse_type</code> is <code>sitemap</code>.</li>
</ul>
</li>
<li><code>use_browser_rendering</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Use Browser Run (formerly Browser Rendering) to crawl JavaScript-rendered pages.</li>
</ul>
</li>
</ul>
</li>
<li><code>discover_options</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Crawl settings that apply when <code>parse_type</code> is <code>discover</code>.</li>
<li><code>source</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Where the crawler looks for candidate URLs. Valid values: <code>all</code>, <code>sitemaps</code>, <code>links</code>. Defaults to <code>all</code>.</li>
</ul>
</li>
<li><code>limit</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Maximum number of pages to crawl. Valid values: <code>1</code> to <code>100000</code>. Defaults to <code>100000</code>.</li>
</ul>
</li>
<li><code>depth</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Maximum number of link hops to follow from the source URL. Valid values: <code>1</code> to <code>100000</code>. Defaults to <code>5</code>.</li>
</ul>
</li>
<li><code>max_age</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>How long, in seconds, the crawler reuses cached page content before it re-fetches from the origin. Valid values: <code>0</code> to <code>604800</code>. Defaults to <code>86400</code>.</li>
</ul>
</li>
<li><code>include_external_links</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Whether to follow links that point to other domains. Defaults to <code>false</code>.</li>
</ul>
</li>
<li><code>include_subdomains</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Whether to follow links that point to subdomains of the source URL. Defaults to <code>false</code>.</li>
</ul>
</li>
</ul>
</li>
<li><code>store_options</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li><code>storage_type</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The storage type. Valid value: <code>r2</code>.</li>
</ul>
</li>
<li><code>storage_id</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The storage bucket ID.</li>
</ul>
</li>
<li><code>r2_jurisdiction</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The jurisdiction for the storage bucket.</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<p><code>index_method</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<p>Configures which indexing methods are enabled for the instance. Determines whether vector (semantic) search, keyword search, or both are available. At least one must be <code>true</code>.</p>
<ul>
<li><code>vector</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Enable vector-based semantic search. Defaults to <code>true</code>.</li>
</ul>
</li>
<li><code>keyword</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Enable keyword-based search. Defaults to <code>false</code>.</li>
</ul>
</li>
</ul>
<p>Set both to <code>true</code> for hybrid search.</p>
<hr />
<p><code>fusion_method</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>Controls how vector and keyword scores are combined when using hybrid search. Valid values: <code>rrf</code> (Reciprocal Rank Fusion), <code>max</code> (takes the maximum score). Defaults to <code>rrf</code>.</p>
<hr />
<p><code>indexing_options</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<p>Configuration for how content is indexed.</p>
<ul>
<li><code>keyword_tokenizer</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The tokenizer used for keyword search indexing. Valid values: <code>porter</code> (stemming-based), <code>trigram</code> (character n-gram). Defaults to <code>porter</code>.</li>
</ul>
</li>
</ul>
<hr />
<p><code>retrieval_options</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<p>Default retrieval configuration for the instance. These defaults can be overridden per-request using <code>ai_search_options</code>.</p>
<ul>
<li><code>keyword_match_mode</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Controls how keyword (BM25) matching selects candidate documents. <code>and</code> requires all terms to match. <code>or</code> requires any term to match. Defaults to <code>and</code>.</li>
</ul>
</li>
<li><code>boost_by</code> <span class="nb-type">array</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Default boost fields applied to all search queries. Maximum 3 items. Each item has:
<ul>
<li><code>field</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span> - The metadata field name to boost by. Maximum 64 characters.</li>
<li><code>direction</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span> - The boost direction. Valid values: <code>asc</code>, <code>desc</code>, <code>exists</code>, <code>not_exists</code>.</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<p><code>sync_interval</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<p>Seconds between automatic data source syncs. Valid values: <code>3600</code>, <code>7200</code>, <code>14400</code>, <code>21600</code>, <code>43200</code>, <code>86400</code>. Defaults to <code>21600</code> (6 hours).</p>
<hr />
<p><code>token_id</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>The UUID of the <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a> to use for this instance. Only required if you have never created an AI Search instance before. Refer to the <a href="/ai-search/get-started/api/">API get started guide</a> for how to create and register a service token.</p>
<hr />
<p><code>ai_gateway_id</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>The AI Gateway ID to route requests through for logging and analytics.</p>
<hr />
<p><code>embedding_model</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>The embedding model to use for vectorizing content.</p>
<hr />
<p><code>ai_search_model</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>The text-generation model to use for generating responses.</p>
<hr />
<p><code>rewrite_query</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<p>Enable query rewriting to improve retrieval accuracy. Defaults to <code>false</code>.</p>
<hr />
<p><code>rewrite_model</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>The model to use for query rewriting.</p>
<hr />
<p><code>reranking</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<p>Enable reranking to reorder retrieved results by semantic relevance. Defaults to <code>false</code>.</p>
<hr />
<p><code>reranking_model</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>The reranking model to use. Valid value: <code>@cf/baai/bge-reranker-base</code>.</p>
<hr />
<p><code>chunk_size</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<p>The size of chunks when splitting documents. Minimum value: <code>64</code>.</p>
<hr />
<p><code>chunk_overlap</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<p>The overlap between chunks. Minimum value: <code>0</code>.</p>
<hr />
<p><code>max_num_results</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<p>The default maximum number of results to return. Minimum value: <code>1</code>.</p>
<hr />
<p><code>score_threshold</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<p>The default minimum score threshold for results. Minimum value: <code>0</code>.</p>
<hr />
<p><code>cache</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<p>Enable response caching. Defaults to <code>true</code>.</p>
<hr />
<p><code>cache_threshold</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>The cache matching threshold. Valid values: <code>super_strict_match</code>, <code>close_enough</code>, <code>flexible_friend</code>, <code>anything_goes</code>. Defaults to <code>close_enough</code>.</p>
<hr />
<p><code>cache_ttl</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<p>The cache entry TTL in seconds. Valid values are <code>600</code>, <code>1800</code>, <code>3600</code>, <code>7200</code>, <code>21600</code>, <code>43200</code>, <code>86400</code>, <code>172800</code>, <code>259200</code>, and <code>518400</code>. Defaults to <code>172800</code>.</p>
<hr />
<p><code>custom_metadata</code> <span class="nb-type">array</span> <span class="nb-metainfo">optional</span></p>
<p>Custom metadata fields to extract and index from documents.</p>
<ul>
<li><code>field_name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the metadata field.</li>
</ul>
</li>
<li><code>data_type</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The data type of the field. Valid values: <code>text</code>, <code>number</code>, <code>boolean</code>, <code>datetime</code>.</li>
</ul>
</li>
</ul>
<hr />
<p><code>enable</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<p>Whether the instance is enabled. Defaults to <code>true</code>.</p>
<h4 id="response-1">Response</h4>
<p>Returns an <code>AiSearchInstance</code> handle that is immediately usable for calling methods like <code>search()</code>, <code>info()</code>, <code>stats()</code>, and <code>items.upload()</code>. Call <code>info()</code> on the handle to get the instance configuration.</p>
<h3 id="delete"><code>delete()</code></h3>
<p>Permanently deletes an instance and all its indexed content. This action cannot be undone.</p>
<pre><code class="language-ts">await env.AI_SEARCH.delete(&quot;old-docs&quot;);&#10;</code></pre>
<h4 id="parameters-3">Parameters</h4>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td>string</td>
<td>Yes</td>
<td>The name of the instance to delete.</td>
</tr>
</tbody>
</table>
<h4 id="response-2">Response</h4>
<p>Returns <code>void</code>. Throws an error if the instance does not exist.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3074.md")
</aside>
<h2 id="instance-methods">Instance methods</h2>
<p>The following methods are available on both the <code>ai_search_namespaces</code> and <code>ai_search</code> bindings. With the namespace binding, call methods on the handle returned by <code>get()</code>. With the instance binding, call methods directly on the binding (for example, <code>env.MY_SEARCH.info()</code>).</p>
<p>The examples below use the namespace binding.</p>
<h3 id="update"><code>update()</code></h3>
<p>Partially updates the instance configuration. Only the fields you pass are modified.</p>
<pre><code class="language-ts">const updated = await env.AI_SEARCH.get(&quot;my-instance&quot;).update({&#10;	ai_search_model: &quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&#10;	reranking: true,&#10;});&#10;</code></pre>
<h4 id="parameters-4">Parameters</h4>
<p>Accepts a partial version of the <a href="#parameters">create parameters</a>. Only the fields you include are updated.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ai_search_model</code></td>
<td>string</td>
<td>The text-generation model.</td>
</tr>
<tr>
<td><code>embedding_model</code></td>
<td>string</td>
<td>The embedding model.</td>
</tr>
<tr>
<td><code>index_method</code></td>
<td>object</td>
<td>Indexing methods: <code>\{ vector: boolean, keyword: boolean \}</code>.</td>
</tr>
<tr>
<td><code>fusion_method</code></td>
<td>string</td>
<td>How vector and keyword scores are combined (<code>rrf</code> or <code>max</code>).</td>
</tr>
<tr>
<td><code>indexing_options</code></td>
<td>object</td>
<td>Indexing configuration including <code>keyword_tokenizer</code>.</td>
</tr>
<tr>
<td><code>retrieval_options</code></td>
<td>object</td>
<td>Retrieval configuration including <code>keyword_match_mode</code> and <code>boost_by</code>.</td>
</tr>
<tr>
<td><code>reranking</code></td>
<td>boolean</td>
<td>Turn on or off reranking.</td>
</tr>
<tr>
<td><code>reranking_model</code></td>
<td>string</td>
<td>The reranking model.</td>
</tr>
<tr>
<td><code>rewrite_query</code></td>
<td>boolean</td>
<td>Turn on or off query rewriting.</td>
</tr>
<tr>
<td><code>rewrite_model</code></td>
<td>string</td>
<td>The query rewriting model.</td>
</tr>
<tr>
<td><code>source</code></td>
<td>string</td>
<td>Update the data source location.</td>
</tr>
<tr>
<td><code>cache</code></td>
<td>boolean</td>
<td>Turn on or off response caching.</td>
</tr>
<tr>
<td><code>chunk_size</code></td>
<td>number</td>
<td>Token size of each chunk.</td>
</tr>
<tr>
<td><code>chunk_overlap</code></td>
<td>number</td>
<td>Token overlap between chunks.</td>
</tr>
<tr>
<td><code>score_threshold</code></td>
<td>number</td>
<td>Minimum score threshold for results.</td>
</tr>
<tr>
<td><code>max_num_results</code></td>
<td>number</td>
<td>Maximum number of results per query.</td>
</tr>
<tr>
<td><code>custom_metadata</code></td>
<td>array</td>
<td>Custom metadata field definitions.</td>
</tr>
<tr>
<td><code>sync_interval</code></td>
<td>number</td>
<td>Seconds between automatic data source syncs.</td>
</tr>
</tbody>
</table>
<h4 id="response-3">Response</h4>
<p>Returns the updated instance configuration. Same shape as <a href="#response-2">info()</a>.</p>
<h3 id="info"><code>info()</code></h3>
<p>Returns the current configuration and metadata for the instance.</p>
<pre><code class="language-ts">const info = await env.AI_SEARCH.get(&quot;my-instance&quot;).info();&#10;</code></pre>
<h4 id="response-4">Response</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>string</td>
<td>The instance identifier.</td>
</tr>
<tr>
<td><code>type</code></td>
<td>string</td>
<td>The data source type (<code>r2</code>, <code>web-crawler</code>, or <code>null</code>).</td>
</tr>
<tr>
<td><code>source</code></td>
<td>string</td>
<td>The data source location.</td>
</tr>
<tr>
<td><code>namespace</code></td>
<td>string</td>
<td>The namespace the instance belongs to.</td>
</tr>
<tr>
<td><code>status</code></td>
<td>string</td>
<td>The instance status (<code>active</code>, <code>waiting</code>, <code>indexing</code>).</td>
</tr>
<tr>
<td><code>enable</code></td>
<td>boolean</td>
<td>Whether the instance is enabled.</td>
</tr>
<tr>
<td><code>created_at</code></td>
<td>string</td>
<td>Timestamp of when the instance was created.</td>
</tr>
<tr>
<td><code>modified_at</code></td>
<td>string</td>
<td>Timestamp of the last modification.</td>
</tr>
<tr>
<td><code>ai_search_model</code></td>
<td>string</td>
<td>The text-generation model.</td>
</tr>
<tr>
<td><code>embedding_model</code></td>
<td>string</td>
<td>The embedding model.</td>
</tr>
<tr>
<td><code>reranking</code></td>
<td>boolean</td>
<td>Whether reranking is enabled.</td>
</tr>
<tr>
<td><code>reranking_model</code></td>
<td>string</td>
<td>The reranking model.</td>
</tr>
<tr>
<td><code>rewrite_query</code></td>
<td>boolean</td>
<td>Whether query rewriting is enabled.</td>
</tr>
<tr>
<td><code>rewrite_model</code></td>
<td>string</td>
<td>The query rewriting model.</td>
</tr>
<tr>
<td><code>cache</code></td>
<td>boolean</td>
<td>Whether response caching is enabled.</td>
</tr>
<tr>
<td><code>cache_threshold</code></td>
<td>string</td>
<td>The similarity threshold for cache hits.</td>
</tr>
<tr>
<td><code>index_method</code></td>
<td>object</td>
<td>Which indexing methods are enabled (<code>vector</code>, <code>keyword</code>).</td>
</tr>
<tr>
<td><code>fusion_method</code></td>
<td>string</td>
<td>How vector and keyword scores are combined (<code>rrf</code> or <code>max</code>).</td>
</tr>
<tr>
<td><code>indexing_options</code></td>
<td>object</td>
<td>Indexing configuration including <code>keyword_tokenizer</code>.</td>
</tr>
<tr>
<td><code>retrieval_options</code></td>
<td>object</td>
<td>Retrieval configuration including <code>keyword_match_mode</code> and <code>boost_by</code>.</td>
</tr>
<tr>
<td><code>chunk_size</code></td>
<td>number</td>
<td>Token size of each chunk.</td>
</tr>
<tr>
<td><code>chunk_overlap</code></td>
<td>number</td>
<td>Token overlap between chunks.</td>
</tr>
<tr>
<td><code>score_threshold</code></td>
<td>number</td>
<td>Minimum score threshold for results.</td>
</tr>
<tr>
<td><code>max_num_results</code></td>
<td>number</td>
<td>Maximum number of results per query.</td>
</tr>
<tr>
<td><code>sync_interval</code></td>
<td>number</td>
<td>Seconds between automatic data source syncs.</td>
</tr>
<tr>
<td><code>custom_metadata</code></td>
<td>array</td>
<td>Custom metadata field definitions.</td>
</tr>
<tr>
<td><code>last_activity</code></td>
<td>string</td>
<td>Timestamp of the last indexing activity.</td>
</tr>
</tbody>
</table>
<h3 id="stats"><code>stats()</code></h3>
<p>Returns the current indexing progress for the instance. Use this to poll for completion after creating an instance or uploading files.</p>
<pre><code class="language-ts">const stats = await env.AI_SEARCH.get(&quot;my-instance&quot;).stats();&#10;</code></pre>
<h4 id="response-5">Response</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>queued</code></td>
<td>number</td>
<td>Items waiting to be processed.</td>
</tr>
<tr>
<td><code>running</code></td>
<td>number</td>
<td>Items currently being processed.</td>
</tr>
<tr>
<td><code>completed</code></td>
<td>number</td>
<td>Items successfully indexed.</td>
</tr>
<tr>
<td><code>error</code></td>
<td>number</td>
<td>Items that failed to index.</td>
</tr>
<tr>
<td><code>skipped</code></td>
<td>number</td>
<td>Items skipped during indexing.</td>
</tr>
<tr>
<td><code>outdated</code></td>
<td>number</td>
<td>Items that need re-indexing.</td>
</tr>
<tr>
<td><code>last_activity</code></td>
<td>string</td>
<td>ISO 8601 timestamp of the last indexing activity.</td>
</tr>
<tr>
<td><code>file_embed_errors</code></td>
<td>object</td>
<td>Map of file IDs to embedding error details.</td>
</tr>
<tr>
<td><code>engine.vectorize.vectorsCount</code></td>
<td>number</td>
<td>Total number of vectors stored.</td>
</tr>
<tr>
<td><code>engine.vectorize.dimensions</code></td>
<td>number</td>
<td>Dimensions of the vector embeddings.</td>
</tr>
<tr>
<td><code>engine.r2.payloadSizeBytes</code></td>
<td>number</td>
<td>Total size of stored payloads in bytes.</td>
</tr>
<tr>
<td><code>engine.r2.metadataSizeBytes</code></td>
<td>number</td>
<td>Total size of stored metadata in bytes.</td>
</tr>
<tr>
<td><code>engine.r2.objectCount</code></td>
<td>number</td>
<td>Total number of objects in storage.</td>
</tr>
</tbody>
</table>
<h2 id="local-development">Local development</h2>
<p>Local development is supported by proxying requests to your deployed AI Search instance. Add <code>remote: true</code> to your binding configuration to enable local development with <code>wrangler dev</code>.</p>
<pre><code class="language-jsonc">// wrangler.jsonc&#10;{&#10;	&quot;ai_search&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;MY_SEARCH&quot;,&#10;			&quot;instance_name&quot;: &quot;my-instance&quot;,&#10;			&quot;remote&quot;: true,&#10;		},&#10;	],&#10;}&#10;</code></pre>
