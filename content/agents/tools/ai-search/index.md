<p>Agents can use <a href="/ai-search/">AI Search</a> to retrieve relevant information from indexed content and use it to augment <a href="/agents/runtime/operations/using-ai-models/">calls to AI models</a>. AI Search manages the retrieval pipeline for you, including indexing, search, and optional chat completions over your content.</p>
<p>Use AI Search when you want an agent to:</p>
<ul>
<li>Search product docs, support content, user files, or internal knowledge bases.</li>
<li>Retrieve relevant chunks before calling a model.</li>
<li>Use managed indexing instead of building retrieval infrastructure yourself.</li>
<li>Query content from an R2 bucket, website, or uploaded files.</li>
</ul>
<h2 id="basic-pattern">Basic pattern</h2>
<p>Bind AI Search to your Worker, then query an instance from an agent method.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1855.md")
</div>
<p>For answer generation, use <code>chatCompletions()</code> to retrieve relevant content and generate a response in one call.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1856.md")
</div>
<h2 id="configuration">Configuration</h2>
<p>Use an <code>ai_search_namespaces</code> binding when the agent needs to access AI Search instances by name.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1857.md")
</div>
<p>Use <code>remote: true</code> to query deployed AI Search instances during local development with <code>wrangler dev</code>.</p>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="/ai-search/"><h3 id="card-ai-search-ai-search">AI Search</h3><p>Create managed retrieval pipelines over websites, R2 buckets, and uploaded files.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/api/search/workers-binding/"><h3 id="card-workers-binding-ai-search-api-search-workers-binding">Workers binding</h3><p>Query AI Search directly from Workers code.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/get-started/"><h3 id="card-create-an-ai-search-instance-ai-search-get-started">Create an AI Search instance</h3><p>Create your first AI Search instance and run your first query.</p></a></p>
