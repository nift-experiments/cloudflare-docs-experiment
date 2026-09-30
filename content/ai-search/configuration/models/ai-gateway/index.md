<p>Every AI Search instance is connected to a Cloudflare <a href="/ai-gateway/">AI Gateway</a>. The model calls that AI Search makes for embedding, query rewriting, reranking, and response generation run through this gateway. By configuring the connected gateway, you can observe and control those model calls.</p>
<p>To choose or change which gateway your instance uses, see <a href="/ai-search/configuration/models/">Models</a>.</p>
<h2 id="observe-your-model-calls">Observe your model calls</h2>
<p>AI Gateway records the model requests that run through it, so you can see what your instance is doing.</p>
<ul>
<li><strong><a href="/ai-gateway/observability/analytics/">Analytics</a>:</strong> Track the number of requests, tokens used, cost, latency, and errors across your model calls.</li>
<li><strong><a href="/ai-gateway/observability/logging/">Logs</a>:</strong> Inspect individual requests and responses, including the effective <a href="/ai-search/configuration/retrieval/system-prompt/">system prompt</a>, rewritten queries, and generated answers.</li>
</ul>
<h2 id="use-models-from-other-providers">Use models from other providers</h2>
<p>By default, AI Search uses <a href="/workers-ai/">Workers AI</a> models. To use models from other providers, such as OpenAI or Anthropic, add your provider keys to AI Gateway and select those models in AI Search.</p>
<ol>
<li>Add your provider keys with <a href="/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Keys</a>.</li>
<li>Connect the gateway and select the models in your AI Search settings. For details, see <a href="/ai-search/configuration/models/">Models</a>.</li>
</ol>
<h2 id="guard-against-unsafe-content">Guard against unsafe content</h2>
<p>Use AI Gateway <a href="/ai-gateway/features/guardrails/">Guardrails</a> to screen the prompts and responses that flow through your instance and block content that is unsafe or inappropriate. To detect and handle sensitive information, such as personal or financial data, use <a href="/ai-gateway/features/dlp/">Data Loss Prevention (DLP)</a>.</p>
<h2 id="improve-resilience">Improve resilience</h2>
<p>Configure <a href="/ai-gateway/configuration/fallbacks/">request retries and model fallbacks</a> so that a model call can automatically retry or fall back to another model when a provider returns an error.</p>
<h2 id="caching-and-rate-limiting">Caching and rate limiting</h2>
<p>Some AI Gateway features act on every request that passes through the gateway. Because your AI Search instance shares this gateway for its internal model calls, a few features can interfere with indexing and querying.</p>
<p>Do not turn on <a href="/ai-gateway/features/caching/">AI Gateway caching</a> for the gateway connected to your AI Search instance. This matters most for embedding requests. AI Search relies on fresh embeddings to build its vector index and to match each query against it, so serving cached embeddings can store or return incorrect vectors and quietly degrade the accuracy of your search results. To cache search results, use AI Search's own <a href="/ai-search/configuration/retrieval/cache/">Similarity cache</a> instead.</p>
<p>Similarly, avoid setting <a href="/ai-gateway/features/rate-limiting/">rate limiting</a> on this gateway. Rate limits apply to AI Search's own model calls, including the many embedding requests made while indexing, and can interrupt indexing and querying.</p>
