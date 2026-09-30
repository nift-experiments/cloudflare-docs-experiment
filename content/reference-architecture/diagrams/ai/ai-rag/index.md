<p>Retrieval-Augmented Generation (RAG) is an innovative approach in natural language processing that integrates retrieval mechanisms with generative models to enhance text generation.</p>
<p>By incorporating external knowledge from pre-existing sources, RAG addresses the challenge of generating contextually relevant and informative text. This integration enables RAG to overcome the limitations of traditional generative models by ensuring that the generated text is grounded in factual information and context. RAG aims to solve the problem of information overload by efficiently retrieving and incorporating only the most relevant information into the generated text, leading to improved coherence and accuracy. Overall, RAG represents a significant advancement in NLP, offering a more robust and contextually aware approach to text generation.</p>
<p>Examples for application of these technique includes for instance customer service chat bots that use a knowledge base to answer support requests.</p>
<p>In the context of Retrieval-Augmented Generation (RAG), knowledge seeding involves incorporating external information from pre-existing sources into the generative process, while querying refers to the mechanism of retrieving relevant knowledge from these sources to inform the generation of coherent and contextually accurate text. Both are shown below.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-a-managed-option">Looking for a managed option?</h3>
@markup("md", "content/.markup/bodies/12730.md")
</aside>
<h2 id="knowledge-seeding">Knowledge Seeding</h2>
<p><img src="/assets/upstream/images/reference-architecture/rag-ref-architecture-diagrams/rag-architecture-seeding.svg" alt="Figure 1: Knowledge seeding" title="Figure 1: Knowledge seeding" /></p>
<ol>
<li><strong>Client upload</strong>: Send POST request with documents to API endpoint.</li>
<li><strong>Input processing</strong>: Process incoming request using <a href="/workers/">Workers</a> and send messages to <a href="/queues/">Queues</a> to add processing backlog.</li>
<li><strong>Batch processing</strong>: Use <a href="/queues/">Queues</a> to trigger a <a href="/queues/reference/how-queues-works/#consumers">consumer</a> that process input documents in batches to prevent downstream overload.</li>
<li><strong>Embedding generation</strong>: Generate embedding vectors by calling <a href="/workers-ai/">Workers AI</a> <a href="/workers-ai/models/">text embedding models</a> for the documents.</li>
<li><strong>Vector storage</strong>: Insert the embedding vectors to <a href="/vectorize/">Vectorize</a>.</li>
<li><strong>Document storage</strong>: Insert documents to <a href="/d1/">D1</a> for persistent storage.</li>
<li><strong>Ack/Retry mechanism</strong>: Signal success/error by using the <a href="/queues/configuration/javascript-apis/#message">Queues Runtime API</a> in the consumer for each document. <a href="/queues/">Queues</a> will schedule retries, if needed.</li>
</ol>
<h2 id="knowledge-queries">Knowledge Queries</h2>
<p><img src="/assets/upstream/images/reference-architecture/rag-ref-architecture-diagrams/rag-architecture-query.svg" alt="Figure 2: Knowledge queries" title="Figure 2: Knowledge queries" /></p>
<ol>
<li><strong>Client query</strong>: Send GET request with query to API endpoint.</li>
<li><strong>Embedding generation</strong>: Generate embedding vectors by calling <a href="/workers-ai/">Workers AI</a> <a href="/workers-ai/models/">text embedding models</a> for the incoming query.</li>
<li><strong>Vector search</strong>: Query <a href="/vectorize/">Vectorize</a> using the vector representation of the query to retrieve related vectors.</li>
<li><strong>Document lookup</strong>: Retrieve related documents from <a href="/d1/">D1</a> based on search results from <a href="/vectorize/">Vectorize</a>.</li>
<li><strong>Text generation</strong>: Pass both the original query and the retrieved documents as context to <a href="/workers-ai/">Workers AI</a> <a href="/workers-ai/models/">text generation models</a> to generate a response.</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers-ai/guides/tutorials/build-a-retrieval-augmented-generation-ai/">Tutorial: Build a RAG AI</a></li>
<li><a href="/ai-search/get-started/">Get started with AI Search</a></li>
<li><a href="/workers-ai/models/">Workers AI: Text embedding models</a></li>
<li><a href="/workers-ai/models/">Workers AI: Text generation models</a></li>
</ul>
