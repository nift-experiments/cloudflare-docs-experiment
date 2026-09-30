<p>Query rewriting is an optional step in the AI Search pipeline that improves retrieval quality for follow-up queries. It applies to both <a href="/ai-search/api/search/workers-binding/#search">Search</a> and <a href="/ai-search/api/search/workers-binding/#chatcompletions">Chat Completions</a> requests.</p>
<h2 id="why-use-query-rewriting">Why use query rewriting?</h2>
<p>The wording of a user's question may not match how your documents are written. Query rewriting helps bridge this gap by:</p>
<ul>
<li>Rephrasing informal or vague queries into precise, information-dense terms</li>
<li>Adding synonyms or related keywords</li>
<li>Removing filler words or irrelevant details</li>
<li>Resolving follow-up queries that reference previous messages (for example, &quot;tell me more about that&quot; becomes a specific query based on conversation history)</li>
</ul>
<p>This leads to more relevant search matches, which improves the accuracy of results and generated responses.</p>
<h2 id="how-it-works">How it works</h2>
<p>Query rewriting requires the <code>messages</code> format and does not apply when using the <code>query</code> format. The first message is always used as-is. For follow-up queries, AI Search sends the conversation history, the latest user message, and the <a href="/ai-search/configuration/retrieval/system-prompt/">query rewrite system prompt</a> to the configured LLM. The rewritten query is then embedded and used to perform the search.</p>
<h2 id="example">Example</h2>
<p><strong>First message:</strong> <code>What is Cloudflare Workers?</code>
(used as-is, no rewriting)</p>
<p><strong>Follow-up message:</strong> <code>How do I deploy one?</code>
<strong>Rewritten query:</strong> <code>deploy Cloudflare Worker getting started</code></p>
<p>The follow-up &quot;How do I deploy one?&quot; is vague on its own. Query rewriting uses the conversation context to understand &quot;one&quot; refers to a Cloudflare Worker. How the query is rewritten depends on your <a href="/ai-search/configuration/retrieval/system-prompt/#query-rewriting-system-prompt">query rewrite system prompt</a>.</p>
<h2 id="considerations">Considerations</h2>
<p>Enabling query rewriting adds an extra LLM call to the query pipeline, which may increase latency.</p>
