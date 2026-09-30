<h1 id="changelog">Changelog</h1>

<h2 id="new-metrics-view-in-autorag"><a href="/changelog/post/2025-09-19-autorag-metrics/">New Metrics View in AutoRAG</a></h2>
<p><em>2025-09-19</em></p>
<p><a href="/ai-search/">AutoRAG</a> now includes a <strong>Metrics</strong> tab that shows how your data is indexed and searched. Get a clear view of the health of your indexing pipeline, compare usage between <code>ai-search</code> and <code>search</code>, and see which files are retrieved most often.</p>
<p><img src="/assets/upstream/images/ai-search/metrics.png" alt="Metrics" /></p>
<p>You can find these metrics within each AutoRAG instance:</p>
<ul>
<li>Indexing: Track how files are ingested and see status changes over time.</li>
<li>Search breakdown: Compare usage between <code>ai-search</code> and <code>search</code> endpoints.</li>
<li>Top file retrievals: Identify which files are most frequently retrieved in a given period.</li>
</ul>
<p>Try it today in <a href="/ai-search/get-started/">AutoRAG</a>.</p>


<h2 id="faster-indexing-and-new-jobs-view-in-autorag"><a href="/changelog/post/2025-07-08-autorag-jobs-view/">Faster indexing and new Jobs view in AutoRAG</a></h2>
<p><em>2025-07-08</em></p>
<p>You can now expect <strong>3-5× faster indexing</strong> in AutoRAG, and with it, a brand new <strong>Jobs view</strong> to help you monitor indexing progress.</p>
<p>With each AutoRAG, indexing jobs are automatically triggered to sync your data source (i.e. R2 bucket) with your Vectorize index, ensuring new or updated files are reflected in your query results. You can also trigger jobs manually via the <a href="/api/resources/ai-search/subresources/rags/">Sync API</a> or by clicking “Sync index” in the dashboard.</p>
<p>With the new jobs observability, you can now:</p>
<ul>
<li>View the status, job ID, source, start time, duration and last sync time for each indexing job</li>
<li>Inspect real-time logs of job events (e.g. <code>Starting indexing data source...</code>)</li>
<li>See a history of past indexing jobs under the Jobs tab of your AutoRAG</li>
</ul>
<p>This makes it easier to understand what’s happening behind the scenes.</p>
<p><strong>Coming soon:</strong> We’re adding APIs to programmatically check indexing status, making it even easier to integrate AutoRAG into your workflows.</p>
<p>Try it out today on the <a href="https://dash.cloudflare.com/?to=/:account/ai/autorag">Cloudflare dashboard</a>.</p>


<h2 id="view-custom-metadata-in-responses-and-guide-ai-search-with-context-in-autorag"><a href="/changelog/post/2025-06-19-autorag-custom-metadata-and-context/">View custom metadata in responses and guide AI-search with context in AutoRAG</a></h2>
<p><em>2025-06-19</em></p>
<p>In <a href="/ai-search/">AutoRAG</a>, you can now view your object's custom metadata in the response from <a href="/ai-search/api/search/workers-binding/"><code>/search</code></a> and <a href="/ai-search/api/search/workers-binding/"><code>/ai-search</code></a>, and optionally add a <code>context</code> field in the custom metadata of an object to provide additional guidance for AI-generated answers.</p>
<p>You can add <a href="/r2/api/workers/workers-api-reference/#r2putoptions">custom metadata</a> to an object when uploading it to your R2 bucket.</p>
<h4 id="2025-06-19-autorag-custom-metadata-and-context-object-s-custom-metadata-in-search-responses">Object's custom metadata in search responses</h4>
<p>When you run a search, AutoRAG now returns any custom metadata associated with the object. This metadata appears in the response inside <code>attributes</code> then <code>file</code> , and can be used for downstream processing.</p>
<p>For example, the <code>attributes</code> section of your search response may look like:</p>
<pre><code class="language-json">{&#10;	&quot;attributes&quot;: {&#10;		&quot;timestamp&quot;: 1750001460000,&#10;		&quot;folder&quot;: &quot;docs/&quot;,&#10;		&quot;filename&quot;: &quot;launch-checklist.md&quot;,&#10;		&quot;file&quot;: {&#10;			&quot;url&quot;: &quot;https://wiki.company.com/docs/launch-checklist&quot;,&#10;			&quot;context&quot;: &quot;A checklist for internal launch readiness, including legal, engineering, and marketing steps.&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="2025-06-19-autorag-custom-metadata-and-context-add-a-context-field-to-guide-llm-answers">Add a <code>context</code> field to guide LLM answers</h4>
<p>When you include a custom metadata field named <code>context</code>, AutoRAG attaches that value to each chunk of the file. When you run an <code>/ai-search</code> query, this <code>context</code> is passed to the LLM and can be used as additional input when generating an answer.</p>
<p>We recommend using the <code>context</code> field to describe supplemental information you want the LLM to consider, such as a summary of the document or a source URL. If you have several different metadata attributes, you can join them together however you choose within the <code>context</code> string.</p>
<p>For example:</p>
<pre><code class="language-json">{&#10;	&quot;context&quot;: &quot;summary: &#x27;Checklist for internal product launch readiness, including legal, engineering, and marketing steps.&#x27;; url: &#x27;https://wiki.company.com/docs/launch-checklist&#x27;&quot;&#10;}&#10;</code></pre>
<p>This gives you more control over how your content is interpreted, without requiring you to modify the original contents of the file.</p>
<p>Learn more in AutoRAG's <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>


<h2 id="filter-your-autorag-search-by-file-name"><a href="/changelog/post/2025-06-19-autorag-filename-filter/">Filter your AutoRAG search by file name</a></h2>
<p><em>2025-06-19</em></p>
<p>In <a href="/ai-search/">AutoRAG</a>, you can now <a href="/ai-search/configuration/indexing/metadata/">filter</a> by an object's file name using the <code>filename</code> attribute, giving you more control over which files are searched for a given query.</p>
<p>This is useful when your application has already determined which files should be searched. For example, you might query a PostgreSQL database to get a list of files a user has access to based on their permissions, and then use that list to limit what AutoRAG retrieves.</p>
<p>For example, your search query may look like:</p>
<pre><code class="language-js">const response = await env.AI.autorag(&quot;my-autorag&quot;).search({&#10;	query: &quot;what is the project deadline?&quot;,&#10;	filters: {&#10;		type: &quot;eq&quot;,&#10;		key: &quot;filename&quot;,&#10;		value: &quot;project-alpha-roadmap.md&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>This allows you to connect your application logic with AutoRAG's retrieval process, making it easy to control what gets searched without needing to reindex or modify your data.</p>
<p>Learn more in AutoRAG's <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>


<h2 id="metadata-filtering-and-multitenancy-support-in-autorag"><a href="/changelog/post/2025-04-23-autorag-metadata-filtering/">Metadata filtering and multitenancy support in AutoRAG</a></h2>
<p><em>2025-04-23</em></p>
<p>You can now filter <a href="/ai-search/">AutoRAG</a> search results by <code>folder</code> and <code>timestamp</code> using <a href="/ai-search/configuration/indexing/metadata/">metadata filtering</a> to narrow down the scope of your query.</p>
<p>This makes it easy to build <a href="/ai-search/how-to/per-tenant-search/">multitenant experiences</a> where each user can only access their own data. By organizing your content into per-tenant folders and applying a <code>folder</code> filter at query time, you ensure that each tenant retrieves only their own documents.</p>
<p><strong>Example folder structure:</strong></p>
<pre><code class="language-bash">customer-a/logs/&#10;customer-a/contracts/&#10;customer-b/contracts/&#10;</code></pre>
<p><strong>Example query:</strong></p>
<pre><code class="language-js">const response = await env.AI.autorag(&quot;my-autorag&quot;).search({&#10;	query: &quot;When did I sign my agreement contract?&quot;,&#10;	filters: {&#10;		type: &quot;eq&quot;,&#10;		key: &quot;folder&quot;,&#10;		value: &quot;customer-a/contracts/&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>You can use metadata filtering by creating a new AutoRAG or reindexing existing data. To reindex all content in an existing AutoRAG, update any chunking setting and select <strong>Sync index</strong>. Metadata filtering is available for all data indexed on or after <strong>April 21, 2025</strong>.</p>
<p>If you are new to AutoRAG, get started with the <a href="/ai-search/get-started/">Get started AutoRAG guide</a>.</p>


<h2 id="create-fully-managed-rag-pipelines-for-your-ai-applications-with-autorag"><a href="/changelog/post/2025-04-07-autorag-open-beta/">Create fully-managed RAG pipelines for your AI applications with AutoRAG</a></h2>
<p><em>2025-04-07</em></p>
<p><a href="/ai-search/">AutoRAG</a> is now in open beta, making it easy for you to build fully-managed retrieval-augmented generation (RAG) pipelines without managing infrastructure. Just upload your docs to <a href="/r2/get-started/">R2</a>, and AutoRAG handles the rest: embeddings, indexing, retrieval, and response generation via API.</p>
<p>With AutoRAG, you can:</p>
<ul>
<li><strong>Customize your pipeline:</strong> Choose from <a href="/workers-ai">Workers AI</a> models, configure chunking strategies, edit system prompts, and more.</li>
<li><strong>Instant setup:</strong> AutoRAG provisions everything you need from <a href="/vectorize">Vectorize</a>, <a href="/ai-gateway">AI gateway</a>, to pipeline logic for you, so you can go from zero to a working RAG pipeline in seconds.</li>
<li><strong>Keep your index fresh:</strong> AutoRAG continuously syncs your index with your data source to ensure responses stay accurate and up to date.</li>
<li><strong>Ask questions:</strong> Query your data and receive grounded responses via a <a href="/ai-search/api/search/workers-binding/">Workers binding</a> or <a href="/ai-search/api/search/rest-api/">API</a>.</li>
</ul>
<p>Whether you're building internal tools, AI-powered search, or a support assistant, AutoRAG gets you from idea to deployment in minutes.</p>
<p>Get started in the <a href="https://dash.cloudflare.com/?to=/:account/ai/autorag">Cloudflare dashboard</a> or check out the <a href="/ai-search/get-started/">guide</a> for instructions on how to build your RAG pipeline today.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/ai-search/">Previous</a><span>Page 2 of 2</span></nav>
