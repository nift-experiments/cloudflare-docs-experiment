<p>AI Search is a managed search service. Connect a website, an R2 bucket, or upload your own documents, and AI Search indexes your content for natural language queries.</p>
<p>AI Search consists of two core processes:</p>
<ul>
<li><strong>Indexing:</strong> An asynchronous process that converts your content into vectors and keyword indexes for search. Indexing runs automatically when you connect a data source or upload files.</li>
<li><strong>Querying:</strong> A synchronous process triggered by user queries. It retrieves the most relevant content using vector search, keyword search, or both, and optionally generates a response.</li>
</ul>
<h2 id="how-indexing-works">How indexing works</h2>
<p>Indexing begins automatically when you connect a data source or upload files through the <a href="/ai-search/api/items/workers-binding/">Items API</a>.</p>
<div class="nb-interactive-component" data-cf-component="AiSearchIndexingDiagram"></div>
<p>Here is what happens during indexing:</p>
<ol>
<li><strong>Data ingestion:</strong> AI Search reads from your connected data source or receives files uploaded through the <a href="/ai-search/api/items/workers-binding/">Items API</a>.</li>
<li><strong>Markdown conversion:</strong> AI Search uses <a href="/workers-ai/features/markdown-conversion/">Workers AI's Markdown Conversion</a> to convert <a href="/ai-search/configuration/data-source/">supported data types</a> into structured Markdown. This ensures consistency across diverse file types. For images, Workers AI is used to perform object detection followed by vision-to-language transformation to convert images into Markdown text. Refer to <a href="/workers-ai/features/markdown-conversion/how-it-works/#images">how images are converted</a> for details.</li>
<li><strong>Chunking:</strong> The extracted text is <a href="/ai-search/configuration/indexing/chunking/">chunked</a> into smaller pieces to improve retrieval granularity.</li>
<li><strong>Embedding:</strong> Each chunk is embedded using Workers AI's embedding model to transform the content into vectors.</li>
<li><strong>Keyword indexing:</strong> When keyword search is enabled, each chunk is also indexed for BM25 keyword matching.</li>
<li><strong>Storage:</strong> The vectors, keyword index, and content are stored and ready for search.</li>
</ol>
<p>For instances with a connected data source, AI Search regularly checks for updates and indexes changes automatically. For instances using <a href="/ai-search/configuration/data-source/built-in-storage/">built-in storage</a>, new files are indexed as they are uploaded.</p>
<h2 id="how-querying-works">How querying works</h2>
<p>Once indexing is complete, AI Search is ready to respond to end-user queries in real time.</p>
<div class="nb-interactive-component" data-cf-component="AiSearchQueryingDiagram"></div>
<p>Here is how the querying pipeline works:</p>
<ol>
<li><strong>Receive query from AI Search API:</strong> The query workflow begins when you send a request to either the AI Search's <a href="/ai-search/api/search/rest-api/#chat-completions">Chat Completions</a> or <a href="/ai-search/api/search/rest-api/#search">Search</a> endpoints.</li>
<li><strong>Query rewriting (optional):</strong> AI Search provides the option to <a href="/ai-search/configuration/retrieval/query-rewriting/">rewrite the input query</a> using one of Workers AI's LLMs to improve retrieval quality by transforming the original query into a more effective search query.</li>
<li><strong>Embedding the query:</strong> The rewritten (or original) query is transformed into a vector using the same embedding model used to embed your data.</li>
<li><strong>Vector search:</strong> The query vector is matched against stored vectors to find semantically similar content.</li>
<li><strong>Keyword search (optional):</strong> When hybrid search is enabled, a BM25 keyword search runs in parallel with vector search.</li>
<li><strong>Fusion (optional):</strong> When using hybrid search, vector and keyword results are combined using the configured fusion method.</li>
<li><strong>Reranking (optional):</strong> A cross-encoder model re-scores results by evaluating the query and document together. Refer to <a href="/ai-search/configuration/retrieval/reranking/">Reranking</a> for details.</li>
<li><strong>Content retrieval:</strong> The most relevant chunks and their source content are returned. If you are using the Search endpoint, the content is returned at this point.</li>
<li><strong>Response generation:</strong> If you are using the Chat Completions endpoint, a text-generation model generates a response using the retrieved content. Refer to <a href="/ai-search/configuration/retrieval/system-prompt/">System prompt</a> for details.</li>
</ol>
<h2 id="when-to-use-ai-search-vs-vectorize">When to use AI Search vs. Vectorize</h2>
<p>AI Search is built on <a href="/vectorize/">Vectorize</a> and adds the rest of the search pipeline around it. Use Vectorize when you want to manage vectors yourself, and AI Search when you want managed search over your content.</p>
<table>
<thead>
<tr>
<th>Capability</th>
<th>AI Search</th>
<th>Vectorize</th>
</tr>
</thead>
<tbody>
<tr>
<td>What it is</td>
<td>Managed, end-to-end search over your content</td>
<td>A vector database you build on</td>
</tr>
<tr>
<td>You give it</td>
<td>Files, or a connected data source</td>
<td>Vectors you generate yourself</td>
</tr>
<tr>
<td>Chunking and embeddings</td>
<td>Handled for you</td>
<td>You generate and insert them</td>
</tr>
<tr>
<td>Indexing</td>
<td>Automatic, with continuous sync</td>
<td>You upsert and manage vectors</td>
</tr>
<tr>
<td>Retrieval</td>
<td>Vector and keyword (hybrid), reranking, metadata filtering</td>
<td>Vector similarity search with metadata filtering</td>
</tr>
<tr>
<td>Generated answers</td>
<td>Optional, built in</td>
<td>Not included</td>
</tr>
<tr>
<td>Best when</td>
<td>You want to add search or RAG quickly</td>
<td>You need full control of the retrieval pipeline</td>
</tr>
</tbody>
</table>
