<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 28, 2025</time><h2 id="post-title">Reranking and API-based system prompt configuration in AI Search</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports reranking for improved retrieval quality and allows you to set the system prompt directly in your API requests.</p>
<h4 id="rerank-for-more-relevant-results">Rerank for more relevant results</h4>
<p>You can now enable <a href="/ai-search/configuration/retrieval/reranking/">reranking</a> to reorder retrieved documents based on their semantic relevance to the user’s query. Reranking helps improve accuracy, especially for large or noisy datasets where vector similarity alone may not produce the optimal ordering.</p>
<p>You can enable and configure reranking in the dashboard or directly in your API requests:</p>
<pre><code class="language-javascript">const answer = await env.AI.autorag(&quot;my-autorag&quot;).aiSearch({&#10;	query: &quot;How do I train a llama to deliver coffee?&quot;,&#10;	model: &quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&#10;	reranking: {&#10;		enabled: true,&#10;		model: &quot;@cf/baai/bge-reranker-base&quot;,&#10;	},&#10;});&#10;</code></pre>
<h4 id="set-system-prompts-in-api">Set system prompts in API</h4>
<p>Previously, <a href="/ai-search/configuration/retrieval/system-prompt/">system prompts</a> could only be configured in the dashboard. You can now define them directly in your API requests, giving you per-query control over behavior. For example:</p>
<pre><code class="language-javascript">// Dynamically set query and system prompt in AI Search&#10;async function getAnswer(query, tone) {&#10;	const systemPrompt = `You are a ${tone} assistant.`;&#10;&#10;	const response = await env.AI.autorag(&quot;my-autorag&quot;).aiSearch({&#10;		query: query,&#10;		system_prompt: systemPrompt,&#10;	});&#10;&#10;	return response;&#10;}&#10;&#10;// Example usage&#10;const query = &quot;What is Cloudflare?&quot;;&#10;const tone = &quot;friendly&quot;;&#10;&#10;const answer = await getAnswer(query, tone);&#10;console.log(answer);&#10;</code></pre>
<p>Learn more about <a href="/ai-search/configuration/retrieval/reranking/">Reranking</a> and <a href="/ai-search/configuration/retrieval/system-prompt/">System Prompt</a> in AI Search.</p>
</div></article></div>
