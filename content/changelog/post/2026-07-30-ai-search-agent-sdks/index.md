<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 30, 2026</time><h2 id="post-title">Use AI Search with the Agents SDK, AI SDK, and LangChain</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>You can now use <a href="/ai-search/">AI Search</a> directly from popular agent frameworks, adding grounded retrieval to an existing app instead of calling the REST API by hand. The new <a href="/ai-search/agent-sdks/">Agents</a> section has guides for the <a href="/ai-search/agent-sdks/ai-sdk/">Vercel AI SDK</a>, <a href="/ai-search/agent-sdks/langchain/">LangChain</a>, and the <a href="/ai-search/agent-sdks/agents-sdk/">Cloudflare Agents SDK</a>. The AI SDK integration is a new package, and the LangChain integration is a new retriever in the existing <code>langchain-cloudflare</code> package.</p>
<h4 id="vercel-ai-sdk">Vercel AI SDK</h4>
<p>The <a href="https://www.npmjs.com/package/ai-search-provider"><code>ai-search-provider</code></a> package connects AI Search to the AI SDK, and targets AI SDK v6 (<code>ai@^6</code>). Pass <code>instance.chat()</code> to <code>generateText</code> or <code>streamText</code> to generate a response grounded in your indexed content, with the retrieved chunks returned as <code>sources</code>. You can also expose <code>instance.search()</code> as a tool for agent loops.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17688.md")</div>
<h4 id="langchain">LangChain</h4>
<p>The <code>langchain-cloudflare</code> package (<a href="https://pypi.org/project/langchain-cloudflare/">PyPI</a>, <a href="https://github.com/cloudflare/langchain-cloudflare">GitHub</a>) provides <code>CloudflareAISearchRetriever</code>, a standard LangChain retriever backed by AI Search. Use it on its own, wrap it with <code>create_retriever_tool</code> to give an agent a search tool, or drop it into a RAG chain. It works with REST credentials or a Worker binding inside a Python Worker.</p>
<pre><code class="language-python">from langchain_cloudflare import CloudflareAISearchRetriever&#10;&#10;retriever = CloudflareAISearchRetriever(&#10;    account_id=ACCOUNT_ID,&#10;    api_token=API_TOKEN,&#10;    instance_name=&quot;knowledge-base&quot;,&#10;    retrieval_type=&quot;hybrid&quot;,&#10;)&#10;&#10;docs = retriever.invoke(&quot;How do I configure Workers AI?&quot;)&#10;</code></pre>
<h4 id="cloudflare-agents-sdk">Cloudflare Agents SDK</h4>
<p>The <a href="/agents/">Cloudflare Agents SDK</a> could already reach AI Search through the Workers binding. The new <a href="/ai-search/agent-sdks/agents-sdk/">guide</a> walks through building a stateful chat agent that provisions its own instance, indexes content, and searches it from a tool.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17689.md")</div>
<p>For the full walkthroughs, including creating an instance and indexing content, refer to the <a href="/ai-search/agent-sdks/">Agents</a> guides.</p>
</div></article></div>
