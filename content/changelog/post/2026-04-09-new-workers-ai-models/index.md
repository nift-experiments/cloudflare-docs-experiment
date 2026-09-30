<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 8, 2026</time><h2 id="post-title">New Workers AI models for text generation and embedding in AI Search</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports four additional <a href="/workers-ai/">Workers AI</a> models across text generation and embedding.</p>
<h4 id="text-generation">Text generation</h4>
<table>
<thead>
<tr>
<th>Model</th>
<th>Context window (tokens)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/zai-org/glm-4.7-flash</code></td>
<td>131,072</td>
</tr>
<tr>
<td><code>@cf/qwen/qwen3-30b-a3b-fp8</code></td>
<td>32,000</td>
</tr>
</tbody>
</table>
<p>GLM-4.7-Flash is a lightweight model from Zhipu AI with a 131,072 token context window, suitable for long-document summarization and retrieval tasks. Qwen3-30B-A3B is a mixture-of-experts model from Alibaba that activates only 3 billion parameters per forward pass, keeping inference fast while maintaining strong response quality.</p>
<h4 id="embedding">Embedding</h4>
<table>
<thead>
<tr>
<th>Model</th>
<th>Vector dims</th>
<th>Input tokens</th>
<th>Metric</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/qwen/qwen3-embedding-0.6b</code></td>
<td>1,024</td>
<td>4,096</td>
<td>cosine</td>
</tr>
<tr>
<td><code>@cf/google/embeddinggemma-300m</code></td>
<td>768</td>
<td>512</td>
<td>cosine</td>
</tr>
</tbody>
</table>
<p>Qwen3-Embedding-0.6B supports up to 4,096 input tokens, making it a good fit for indexing longer text chunks. EmbeddingGemma-300M from Google produces 768-dimension vectors and is optimized for low-latency embedding workloads.</p>
<p>All four models are available without additional provider keys since they run on Workers AI. Select them when creating or updating an AI Search instance in the dashboard or through the API.</p>
<p>For the full list of supported models, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>
</div></article></div>
