<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 17, 2025</time><h2 id="post-title">New models in Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>Workers AI is excited to add 4 new models to the catalog, including 2 brand new classes of models with a text-to-speech and reranker model. Introducing:</p>
<ul>
<li><a href="/workers-ai/models/bge-m3/">@cf/baai/bge-m3</a> - a multi-lingual embeddings model that supports over 100 languages. It can also simultaneously perform dense retrieval, multi-vector retrieval, and sparse retrieval, with the ability to process inputs of different granularities.</li>
<li><a href="/workers-ai/models/bge-reranker-base/">@cf/baai/bge-reranker-base</a> - our first reranker model! Rerankers are a type of text classification model that takes a query and context, and outputs a similarity score between the two. When used in RAG systems, you can use a reranker after the initial vector search to find the most relevant documents to return to a user by reranking the outputs.</li>
<li><a href="/workers-ai/models/whisper-large-v3-turbo/">@cf/openai/whisper-large-v3-turbo</a> - a faster, more accurate speech-to-text model. This model was added earlier but is graduating out of beta with pricing included today.</li>
<li><a href="/workers-ai/models/melotts/">@cf/myshell-ai/melotts</a> - our first text-to-speech model that allows users to generate an MP3 with voice audio from inputted text.</li>
</ul>
<p>Pricing is available for each of these models on the <a href="/workers-ai/platform/pricing/">Workers AI pricing page</a>.</p>
<p>This docs update includes a few minor bug fixes to the model schema for llama-guard, llama-3.2-1b, which you can review on the <a href="/workers-ai/changelog/">product changelog</a>.</p>
<p>Try it out and let us know what you think! Stay tuned for more models in the coming days.</p>
</div></article></div>
