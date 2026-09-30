<p>AI applications need specialized storage for vector embeddings, conversation history, training data, and cached responses. Cloudflare Vectorize stores and queries embeddings for Retrieval Augmented Generation (RAG), D1 provides SQL storage for structured data, R2 stores documents and assets, and KV caches frequent responses at the edge.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="vectorize">Vectorize</h3>
<p>Vector database for storing and querying embeddings. <a href="/vectorize/">Learn more about Vectorize</a>.</p>
<ul>
<li><strong>Vector search</strong> - Store embeddings and find semantically similar content for Retrieval Augmented Generation (RAG) and recommendation features</li>
</ul>
<h3 id="d1">D1</h3>
<p>Serverless SQL database built on SQLite, with global read replication. <a href="/d1/">Learn more about D1</a>.</p>
<ul>
<li><strong>Structured storage</strong> - Structured Query Language (SQL) database for conversation history, user data, and application metadata</li>
</ul>
<h3 id="r2">R2</h3>
<p>S3-compatible object storage with zero egress fees. <a href="/r2/">Learn more about R2</a>.</p>
<ul>
<li><strong>Object storage</strong> - Store documents, training data, and generated assets with no egress fees</li>
</ul>
<h3 id="kv">KV</h3>
<p>Globally distributed key-value storage for low-latency reads. <a href="/kv/">Learn more about KV</a>.</p>
<ul>
<li><strong>Edge caching</strong> - Cache frequent AI responses at the edge to reduce inference costs and latency</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/vectorize/get-started/">Vectorize get started</a></li>
<li><a href="/d1/get-started/">D1 get started</a></li>
<li><a href="/r2/get-started/">R2 get started</a></li>
</ol>
