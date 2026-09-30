<p>Prompt caching (also called prefix caching) is a performance optimization that allows Workers AI to respond faster to requests with prompts that share common inputs. It reduces Time to First Token (TTFT) and increases Tokens Per Second (TPS) throughput by reusing previously computed input tensors instead of reprocessing them from scratch.</p>
<p>Cached input tokens are billed at a discounted rate compared to regular input tokens. Workers AI enables prefix caching by default for select models. Compatibility and pricing details are listed on each <a href="/workers-ai/models/">model page</a>.</p>
<h2 id="how-it-works">How it works</h2>
<p>When an LLM processes a request, it goes through two stages:</p>
<ol>
<li><strong>Prefill stage</strong> — processes input tokens (system prompts, tool definitions, conversation history).</li>
<li><strong>Output stage</strong> — generates output tokens.</li>
</ol>
<p>With prefix caching, Workers AI stores the computed input tensors from the prefill stage. On subsequent requests that share the same prefix, the model skips prefill for the cached portion and only processes the new input tokens. This saves significant compute time, especially for agentic workloads where consecutive requests share large amounts of context.</p>
<p>For example, when a coding agent sends a new prompt, it typically resends all previous prompts, tool definitions, and conversation history. The delta between consecutive requests is often just a few new lines. Prefix caching avoids redundant prefill on all the shared context.</p>
<h2 id="session-affinity-header">Session affinity header</h2>
<p>Prefix caching only works when a request routes to the same model instance that holds the cached tensors. To maximize cache hit rates, send the <code>x-session-affinity</code> header with a unique identifier for your session or agent. This routes requests with the same identifier to the same model instance, increasing the likelihood of a prefix cache hit.</p>
<h3 id="rest-api">REST API</h3>
<pre><code class="language-bash">curl -X POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/moonshotai/kimi-k2.5&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;x-session-affinity: ses_12345678&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;system&quot;,&#10;        &quot;content&quot;: &quot;You are a helpful assistant.&quot;&#10;      },&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is prefix caching and why does it matter?&quot;&#10;      }&#10;    ],&#10;    &quot;max_tokens&quot;: 2400,&#10;    &quot;stream&quot;: true&#10;  }&#x27;&#10;</code></pre>
<h3 id="workers-ai-binding">Workers AI binding</h3>
<pre><code class="language-js">const response = await env.AI.run(&#10;	&quot;@cf/moonshotai/kimi-k2.5&quot;,&#10;	{&#10;		messages: [&#10;			{ role: &quot;system&quot;, content: &quot;You are a helpful assistant.&quot; },&#10;			{ role: &quot;user&quot;, content: &quot;Explain prefix caching.&quot; },&#10;		],&#10;	},&#10;	{&#10;		extraHeaders: {&#10;			&quot;x-session-affinity&quot;: &quot;ses_12345678&quot;,&#10;		},&#10;	},&#10;);&#10;</code></pre>
<h2 id="structuring-prompts-for-caching">Structuring prompts for caching</h2>
<p>Prefix caching matches the exact token sequence from the start of the prompt. A single token difference invalidates the cache from that point onward.</p>
<p>To maximize cache hits:</p>
<ul>
<li><strong>Place static content first.</strong> System prompts, tool definitions, and shared instructions should appear at the beginning of the prompt. Put user-specific or dynamic content (timestamps, user queries) at the end.</li>
<li><strong>Avoid timestamps in system prompts.</strong> Including a timestamp at the start of a system prompt changes the prefix on every request, defeating the cache entirely. If time context is required, add it to the user message instead.</li>
<li><strong>Reuse tool definitions across requests.</strong> For function-calling agents, tools are part of the prompt prefix. Keeping tool definitions consistent across requests in the same session increases cache reuse.</li>
</ul>
<h2 id="monitoring-cached-tokens">Monitoring cached tokens</h2>
<p>Workers AI surfaces cached token counts in the response <code>usage</code> object. Use this to verify that prefix caching is working and to track cost savings. The first request will usually be cold, so it is expected that cached tokens are not returned on the first hit. Inputs need to be sufficiently large enough in order to be cached due to block size.
Cached tokens are billed at a lower rate than regular input tokens, which get totalled into your neuron count.</p>
