---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/retrieval/system-prompt/
  description: Guide AI Search query rewriting and response generation behavior with custom system prompts.
  full_title: System prompt · Cloudflare AI Search docs
  head_html: <title>System prompt · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Guide AI Search query rewriting and response generation behavior with custom system prompts."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/retrieval/system-prompt/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/retrieval/system-prompt/index.md"><meta property="og:title" content="System prompt · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Guide AI Search query rewriting and response generation behavior with custom system prompts."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/retrieval/system-prompt/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/retrieval/system-prompt/#page","headline":"System prompt \u00b7 Cloudflare AI Search docs","description":"Guide AI Search query rewriting and response generation behavior with custom system prompts.","url":"https://developers.cloudflare.com/ai-search/configuration/retrieval/system-prompt/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/retrieval/system-prompt/
  schema: 1
---
<p>System prompts allow you to guide the behavior of the text-generation models used by AI Search at query time. AI Search supports system prompt configuration in two steps:</p>
<ul>
<li><strong>Query rewriting</strong>: Reformulates the original user query to improve semantic retrieval. A system prompt can guide how the model interprets and rewrites the query.</li>
<li><strong>Generation</strong>: Generates the final response from retrieved context. A system prompt can help define how the model should format, filter, or prioritize information when constructing the answer.</li>
</ul>
<h2 id="what-is-a-system-prompt">What is a system prompt?</h2>
<p>A system prompt is a special instruction sent to a large language model (LLM) that guides how it behaves during inference. The system prompt defines the model's role, context, or rules it should follow.</p>
<p>System prompts are particularly useful for:</p>
<ul>
<li>Enforcing specific response formats</li>
<li>Constraining behavior (for example, it only responds based on the provided content)</li>
<li>Applying domain-specific tone or terminology</li>
<li>Encouraging consistent, high-quality output</li>
</ul>
<h2 id="system-prompt-configuration">System prompt configuration</h2>
<h3 id="default-system-prompt">Default system prompt</h3>
<p>When configuring your AI Search instance, you can provide your own system prompts. If you do not provide a system prompt, AI Search will use the <strong>default system prompt</strong> provided by Cloudflare.</p>
<p>You can view the effective system prompt used for any AI Search's model call through AI Gateway logs, where model inputs and outputs are recorded.</p>
<h3 id="configure-via-api">Configure via API</h3>
<p>When you make a <code>/chat/completions</code> request using the <a href="/ai-search/api/search/workers-binding/">Workers binding</a> or <a href="/ai-search/api/search/rest-api/">REST API</a>, you can set the system prompt programmatically.</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const response = await instance.chatCompletions({&#10;	messages: [&#10;		{ role: &quot;system&quot;, content: &quot;You are a helpful assistant.&quot; },&#10;		{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; },&#10;	],&#10;	model: &quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&#10;});&#10;</code></pre>
<h2 id="generation-system-prompt">Generation system prompt</h2>
<p>If you are using the Chat Completions endpoint, you can use the system prompt to influence how the LLM responds to the final user query using the retrieved results. At this step, the model receives:</p>
<ul>
<li>The user's original query</li>
<li>Retrieved document chunks (with metadata)</li>
<li>The generation system prompt</li>
</ul>
<p>The model uses these inputs to generate a context-aware response.</p>
<h3 id="example">Example</h3>
<pre tabindex="0"><code class="language-text">You are a helpful AI assistant specialized in answering questions using retrieved documents.&#10;Your task is to provide accurate, relevant answers based on the matched content provided.&#10;For each query, you will receive:&#10;User&#x27;s question/query&#10;A set of matched documents, each containing:&#10;  &#45; File name&#10;  &#45; File content&#10;&#10;You should:&#10;1. Analyze the relevance of matched documents&#10;2. Synthesize information from multiple sources when applicable&#10;3. Acknowledge if the available documents don&#x27;t fully answer the query&#10;4. Format the response in a way that maximizes readability, in Markdown format&#10;&#10;Answer only with direct reply to the user question, be concise, omit everything which is not directly relevant, focus on answering the question directly and do not redirect the user to read the content.&#10;&#10;If the available documents don&#x27;t contain enough information to fully answer the query, explicitly state this and provide an answer based on what is available.&#10;&#10;Important:&#10;&#45; Cite which document(s) you&#x27;re drawing information from&#10;&#45; Present information in order of relevance&#10;&#45; If documents contradict each other, note this and explain your reasoning for the chosen answer&#10;&#45; Do not repeat the instructions&#10;</code></pre>
<h2 id="query-rewriting-system-prompt">Query rewriting system prompt</h2>
<p>If query rewriting is enabled, you can provide a custom system prompt to control how the model rewrites user queries. In this step, the model receives:</p>
<ul>
<li>The query rewrite system prompt</li>
<li>The original user query</li>
</ul>
<p>The model outputs a rewritten query optimized for semantic retrieval.</p>
<h3 id="example-1">Example</h3>
<pre tabindex="0"><code class="language-text">You are a search query optimizer for vector database searches. Your task is to reformulate user queries into more effective search terms.&#10;&#10;Given a user&#x27;s search query, you must:&#10;1. Identify the core concepts and intent&#10;2. Add relevant synonyms and related terms&#10;3. Remove irrelevant filler words&#10;4. Structure the query to emphasize key terms&#10;5. Include technical or domain-specific terminology if applicable&#10;&#10;Provide only the optimized search query without any explanations, greetings, or additional commentary.&#10;&#10;Example input: &quot;how to fix a bike tire that&#x27;s gone flat&quot;&#10;Example output: &quot;bicycle tire repair puncture fix patch inflate maintenance flat tire inner tube replacement&quot;&#10;&#10;Constraints:&#10;&#45; Output only the enhanced search terms&#10;&#45; Keep focus on searchable concepts&#10;&#45; Include both specific and general related terms&#10;&#45; Maintain all important meaning from original query&#10;</code></pre>
