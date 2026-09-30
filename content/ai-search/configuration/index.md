<p>You can customize how your AI Search instance indexes your data, retrieves results, and generates responses. Some settings can be updated after the instance is created, while others are fixed at creation time.</p>
<h2 id="data-source">Data source</h2>
<table>
<thead>
<tr>
<th>Configuration</th>
<th>Editable after creation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/ai-search/configuration/data-source/built-in-storage/">Built-in storage</a></td>
<td>n/a</td>
<td>Upload files directly to an instance</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/website/">Website</a></td>
<td>no</td>
<td>Connect a domain you own to index website pages</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/r2/">R2 Bucket</a></td>
<td>no</td>
<td>Connect a Cloudflare R2 bucket to index stored documents</td>
</tr>
</tbody>
</table>
<h2 id="indexing">Indexing</h2>
<table>
<thead>
<tr>
<th>Configuration</th>
<th>Editable after creation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/ai-search/configuration/indexing/vector-search/">Vector search</a></td>
<td>yes</td>
<td>Vector search and the built-in vector index</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/path-filtering/">Path filtering</a></td>
<td>yes</td>
<td>Include or exclude specific paths from indexing</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/chunking/">Chunking</a></td>
<td>yes</td>
<td>Number of tokens per chunk and overlap between chunks</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/syncing/">Syncing</a></td>
<td>yes</td>
<td>Sync jobs and indexing controls</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/keyword-search/">Keyword search</a></td>
<td>yes</td>
<td>Enable keyword (BM25) search for exact term matching</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/hybrid-search/">Hybrid search</a></td>
<td>yes</td>
<td>Combine vector and keyword search with configurable fusion</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/metadata/">Metadata attributes</a></td>
<td>yes</td>
<td>Define built-in and custom metadata fields</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/indexing/service-api-token/">Service API token</a></td>
<td>yes</td>
<td>API token that grants AI Search permission to access R2 buckets</td>
</tr>
</tbody>
</table>
<h2 id="retrieval">Retrieval</h2>
<table>
<thead>
<tr>
<th>Configuration</th>
<th>Editable after creation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/ai-search/configuration/retrieval/result-controls/">Result controls</a></td>
<td>yes</td>
<td>Match threshold and maximum number of results</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/filtering/">Filtering</a></td>
<td>yes</td>
<td>Filter results by metadata attributes</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/boosting/">Relevance boosting</a></td>
<td>yes</td>
<td>Bias results by metadata characteristics</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/reranking/">Reranking</a></td>
<td>yes</td>
<td>Reorder results by semantic relevance using a reranking model</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/query-rewriting/">Query rewriting</a></td>
<td>yes</td>
<td>Rewrite follow-up queries using conversation context</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/system-prompt/">System prompt</a></td>
<td>yes</td>
<td>Guide query rewriting and response generation behavior</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/cache/">Similarity caching</a></td>
<td>yes</td>
<td>Cache responses for similar prompts</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/public-endpoint/">Public endpoint</a></td>
<td>yes</td>
<td>Enable public access to search, chat, and MCP endpoints</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">Custom domains</a></td>
<td>yes</td>
<td>Serve a public endpoint from a hostname that you own</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a></td>
<td>yes</td>
<td>Require callers to authenticate before they can search</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">Namespace public endpoints</a></td>
<td>yes</td>
<td>Search across several instances from a single public endpoint</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/">UI snippets</a></td>
<td>yes</td>
<td>Embed pre-built search and chat components in your website</td>
</tr>
</tbody>
</table>
<h2 id="models">Models</h2>
<table>
<thead>
<tr>
<th>Configuration</th>
<th>Editable after creation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/ai-search/configuration/models/">Embedding model</a></td>
<td>no</td>
<td>Model used to generate vector embeddings</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/models/">Generation model</a></td>
<td>yes</td>
<td>Model used to generate the final response</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/models/">Query rewriting model</a></td>
<td>yes</td>
<td>Model used for query rewriting</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/models/">Reranking model</a></td>
<td>yes</td>
<td>Model used to reorder results by semantic relevance</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/models/ai-gateway/">AI Gateway</a></td>
<td>yes</td>
<td>Observe and control the model calls AI Search makes</td>
</tr>
</tbody>
</table>
