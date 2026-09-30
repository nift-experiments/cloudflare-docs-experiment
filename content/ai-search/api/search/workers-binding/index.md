---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/api/search/workers-binding/
  description: Search and chat with AI Search instances from a Cloudflare Worker using the Workers binding.
  full_title: Workers binding · Cloudflare AI Search docs
  head_html: <title>Workers binding · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Search and chat with AI Search instances from a Cloudflare Worker using the Workers binding."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/api/search/workers-binding/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/api/search/workers-binding/index.md"><meta property="og:title" content="Workers binding · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Search and chat with AI Search instances from a Cloudflare Worker using the Workers binding."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/api/search/workers-binding/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/api/search/workers-binding/#page","headline":"Workers binding \u00b7 Cloudflare AI Search docs","description":"Search and chat with AI Search instances from a Cloudflare Worker using the Workers binding.","url":"https://developers.cloudflare.com/ai-search/api/search/workers-binding/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/api/search/workers-binding/
  schema: 1
---
<p><a href="/workers/">Workers</a> provides a serverless execution environment that allows you to create new applications or augment existing ones. Use a <a href="/workers/runtime-apis/bindings/">Workers binding</a> to search and chat with your AI Search instances from a Cloudflare Worker.</p>
<h2 id="configure-the-binding">Configure the binding</h2>
<p>To use AI Search with Workers, you must create an AI Search binding. You create bindings by updating your <a href="/workers/wrangler/configuration/">Wrangler configuration</a>. AI Search provides two types of bindings:</p>
<ul>
<li>Namespace binding: <code>ai_search_namespaces</code></li>
<li>Instance binding: <code>ai_search</code></li>
</ul>
<h3 id="namespace-binding">Namespace binding</h3>
<p>Access all instances within a <a href="/ai-search/concepts/namespaces/">namespace</a>. You can get, create, list, and delete instances at runtime.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3065.md")
</div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>binding</code></td>
<td>string</td>
<td>Yes</td>
<td>The variable name available on <code>env</code>. For example, <code>&quot;AI_SEARCH&quot;</code> makes it accessible as <code>env.AI_SEARCH</code>.</td>
</tr>
<tr>
<td><code>namespace</code></td>
<td>string</td>
<td>Yes</td>
<td>The <a href="/ai-search/concepts/namespaces/">namespace</a> to bind to. A <code>default</code> namespace is created automatically for every account. If the namespace does not exist, Wrangler creates it on deploy.</td>
</tr>
<tr>
<td><code>remote</code></td>
<td>boolean</td>
<td>No</td>
<td>Set to <code>true</code> for local development with <code>wrangler dev</code>.</td>
</tr>
</tbody>
</table>
<h3 id="instance-binding">Instance binding</h3>
<p>Bind directly to a single instance in the <code>default</code> namespace. Use this when you know which instance you need at deploy time.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3066.md")
</div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>binding</code></td>
<td>string</td>
<td>Yes</td>
<td>The variable name available on <code>env</code>. For example, <code>&quot;MY_SEARCH&quot;</code> makes it accessible as <code>env.MY_SEARCH</code>.</td>
</tr>
<tr>
<td><code>instance_name</code></td>
<td>string</td>
<td>Yes</td>
<td>The name of the AI Search instance. Must exist in the default namespace at deploy time.</td>
</tr>
<tr>
<td><code>remote</code></td>
<td>boolean</td>
<td>No</td>
<td>Set to <code>true</code> for local development with <code>wrangler dev</code>.</td>
</tr>
</tbody>
</table>
<h2 id="instance-methods">Instance methods</h2>
<p>The following methods are available on both the <code>ai_search_namespaces</code> and <code>ai_search</code> bindings. With the namespace binding, call methods on the handle returned by <code>get()</code>. With the instance binding, call methods directly on the binding (for example, <code>env.MY_SEARCH.search()</code>).</p>
<p>The examples below use the namespace binding.</p>
<h3 id="search"><code>search()</code></h3>
<p>Search for relevant content chunks from your indexed data source. Returns scored chunks with source references.</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;});&#10;</code></pre>
<h4 id="parameters">Parameters</h4>
<p><code>messages</code> <span class="nb-type">array</span> <span class="nb-metainfo">required</span></p>
<p>An array of message objects representing the conversation. Each message has a <code>role</code> and <code>content</code> field.</p>
<ul>
<li>
<p><code>role</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The role of the message sender. Valid values: <code>system</code>, <code>developer</code>, <code>user</code>, <code>assistant</code>, <code>tool</code>.</li>
</ul>
</li>
<li>
<p><code>content</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The content of the message.</li>
</ul>
</li>
</ul>
<hr />
<p><code>query</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>A simple text query string. Alternative to <code>messages</code>. Provide either <code>query</code> or <code>messages</code>, not both.</p>
<hr />
<p><code>ai_search_options</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<p>Configuration options for the search operation.</p>
<ul>
<li>
<p><code>retrieval</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p><code>retrieval_type</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The type of retrieval to perform. Valid values: <code>vector</code>, <code>keyword</code>, <code>hybrid</code>. Defaults to <code>hybrid</code>.</li>
</ul>
</li>
<li>
<p><code>match_threshold</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The minimum match score required for a result to be considered a match. Must be between <code>0</code> and <code>1</code>. Defaults to <code>0.4</code>.</li>
</ul>
</li>
<li>
<p><code>max_num_results</code> <span class="nb-type">integer</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The maximum number of results to return. Must be between <code>1</code> and <code>50</code>. Defaults to <code>10</code>.</li>
</ul>
</li>
<li>
<p><code>filters</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Filter search results based on metadata. Supports comparison filters (<code>eq</code>, <code>ne</code>, <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code>) and compound filters (<code>and</code>, <code>or</code>). For more details, refer to <a href="/ai-search/configuration/retrieval/filtering/">Metadata filtering</a>.</li>
</ul>
</li>
<li>
<p><code>context_expansion</code> <span class="nb-type">integer</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The number of surrounding chunks to include for additional context. Must be between <code>0</code> and <code>3</code>. Defaults to <code>0</code>.</li>
</ul>
</li>
<li>
<p><code>fusion_method</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Controls how vector and keyword scores are combined when using hybrid retrieval. Valid values: <code>rrf</code> (Reciprocal Rank Fusion), <code>max</code> (takes the maximum score). Defaults to the instance-level setting.</li>
</ul>
</li>
<li>
<p><code>keyword_match_mode</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Controls how keyword (BM25) matching selects candidate documents. <code>and</code> requires all terms to match. <code>or</code> requires any term to match. Defaults to <code>and</code>.</li>
</ul>
</li>
<li>
<p><code>boost_by</code> <span class="nb-type">array</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Boost results by metadata fields. Maximum 3 items. Each item has:
<ul>
<li><code>field</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span> - The metadata field name to boost by (for example, <code>timestamp</code>). Maximum 64 characters.</li>
<li><code>direction</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span> - The boost direction. Valid values: <code>asc</code>, <code>desc</code>, <code>exists</code>, <code>not_exists</code>. Defaults to <code>asc</code> for numeric fields and <code>exists</code> for text fields.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>metadata_only</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Return only metadata for each chunk without the text content.</li>
</ul>
</li>
<li>
<p><code>return_on_failure</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Whether to return partial results if some processing steps fail. Defaults to <code>true</code>.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>query_rewrite</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p><code>enabled</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Rewrites the query to improve retrieval accuracy. Defaults to <code>false</code>.</li>
</ul>
</li>
<li>
<p><code>model</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The model to use for query rewriting.</li>
</ul>
</li>
<li>
<p><code>rewrite_prompt</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A custom prompt to guide query rewriting.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>reranking</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p><code>enabled</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Reorders retrieved results based on semantic relevance using a reranking model. Defaults to <code>false</code>.</li>
</ul>
</li>
<li>
<p><code>model</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The reranking model to use. Valid value: <code>@cf/baai/bge-reranker-base</code>.</li>
</ul>
</li>
<li>
<p><code>match_threshold</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The minimum score for reranked results. Must be between <code>0</code> and <code>1</code>. Defaults to <code>0.4</code>.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>cache</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p><code>enabled</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Override the instance-level cache setting for this request.</li>
</ul>
</li>
<li>
<p><code>cache_threshold</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The similarity threshold for cache hits. Valid values: <code>super_strict_match</code>, <code>close_enough</code>, <code>flexible_friend</code>, <code>anything_goes</code>.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h4 id="response">Response</h4>
<p>The response contains the following fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>search_query</code></td>
<td>string</td>
<td>The query used for the search, which may be rewritten if query rewriting is enabled.</td>
</tr>
<tr>
<td><code>chunks</code></td>
<td>array</td>
<td>An array of matching content chunks.</td>
</tr>
<tr>
<td><code>chunks[].id</code></td>
<td>string</td>
<td>The unique identifier for the chunk.</td>
</tr>
<tr>
<td><code>chunks[].type</code></td>
<td>string</td>
<td>The type of content, typically <code>text</code>.</td>
</tr>
<tr>
<td><code>chunks[].score</code></td>
<td>number</td>
<td>The overall match score between 0 and 1.</td>
</tr>
<tr>
<td><code>chunks[].text</code></td>
<td>string</td>
<td>The text content of the chunk.</td>
</tr>
<tr>
<td><code>chunks[].item</code></td>
<td>object</td>
<td>Information about the source item.</td>
</tr>
<tr>
<td><code>chunks[].item.key</code></td>
<td>string</td>
<td>The file path or URL of the source document.</td>
</tr>
<tr>
<td><code>chunks[].item.timestamp</code></td>
<td>number</td>
<td>Unix timestamp of when the item was last modified.</td>
</tr>
<tr>
<td><code>chunks[].item.metadata</code></td>
<td>object</td>
<td>Custom metadata associated with the source item.</td>
</tr>
<tr>
<td><code>chunks[].scoring_details</code></td>
<td>object</td>
<td>Breakdown of how the chunk was scored.</td>
</tr>
<tr>
<td><code>chunks[].scoring_details.vector_score</code></td>
<td>number</td>
<td>The semantic similarity score (0 to 1).</td>
</tr>
<tr>
<td><code>chunks[].scoring_details.keyword_score</code></td>
<td>number</td>
<td>The keyword (BM25) match score. Present when using hybrid or keyword retrieval.</td>
</tr>
<tr>
<td><code>chunks[].scoring_details.keyword_rank</code></td>
<td>number</td>
<td>The keyword rank position.</td>
</tr>
<tr>
<td><code>chunks[].scoring_details.vector_rank</code></td>
<td>number</td>
<td>The vector rank position.</td>
</tr>
<tr>
<td><code>chunks[].scoring_details.reranking_score</code></td>
<td>number</td>
<td>The reranking score (0 to 1). Present when reranking is enabled.</td>
</tr>
<tr>
<td><code>chunks[].scoring_details.fusion_method</code></td>
<td>string</td>
<td>The fusion method used (<code>rrf</code> or <code>max</code>). Present when using hybrid retrieval.</td>
</tr>
</tbody>
</table>
<h3 id="chatcompletions"><code>chatCompletions()</code></h3>
<p>Generate chat completions using your AI Search instance as context. This method retrieves relevant content and uses it to generate a response.</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const response = await instance.chatCompletions({&#10;	messages: [&#10;		{ role: &quot;system&quot;, content: &quot;You are a helpful documentation assistant.&quot; },&#10;		{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; },&#10;	],&#10;	model: &quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&#10;	ai_search_options: {&#10;		retrieval: {&#10;			max_num_results: 5,&#10;		},&#10;		query_rewrite: {&#10;			enabled: true,&#10;		},&#10;	},&#10;});&#10;</code></pre>
<h4 id="stream-responses">Stream responses</h4>
<p>Set <code>stream: true</code> to receive responses as Server-Sent Events (SSE) as they are generated:</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const stream = await instance.chatCompletions({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	stream: true,&#10;});&#10;&#10;return new Response(stream, {&#10;	headers: {&#10;		&quot;content-type&quot;: &quot;text/event-stream&quot;,&#10;		&quot;cache-control&quot;: &quot;no-cache&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>When <code>stream</code> is enabled, the method returns a <code>ReadableStream</code> of SSE events. Each event contains a JSON object with <code>choices[0].delta.content</code> for incremental text. The stream ends with a <code>data: [DONE]</code> event.</p>
<h4 id="parameters-1">Parameters</h4>
<p><code>messages</code> <span class="nb-type">array</span> <span class="nb-metainfo">required</span></p>
<p>An array of message objects representing the conversation. Each message has a <code>role</code> and <code>content</code> field.</p>
<ul>
<li>
<p><code>role</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The role of the message sender. Valid values: <code>system</code>, <code>developer</code>, <code>user</code>, <code>assistant</code>, <code>tool</code>.</li>
</ul>
</li>
<li>
<p><code>content</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The content of the message.</li>
</ul>
</li>
</ul>
<hr />
<p><code>model</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>The text-generation model used to generate responses. Defaults to the generation model configured in the AI Search instance settings. For a list of supported models, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>
<hr />
<p><code>stream</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<p>Returns a stream of results as they are generated. When enabled, returns a <code>Response</code> object with a readable stream. Defaults to <code>false</code>.</p>
<hr />
<p><code>ai_search_options</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<p>Configuration options for the search and generation operation.</p>
<ul>
<li>
<p><code>retrieval</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p><code>retrieval_type</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The type of retrieval to perform. Valid values: <code>vector</code>, <code>keyword</code>, <code>hybrid</code>. Defaults to <code>hybrid</code>.</li>
</ul>
</li>
<li>
<p><code>match_threshold</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The minimum match score required for a result to be considered a match. Must be between <code>0</code> and <code>1</code>. Defaults to <code>0.4</code>.</li>
</ul>
</li>
<li>
<p><code>max_num_results</code> <span class="nb-type">integer</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The maximum number of results to return. Must be between <code>1</code> and <code>50</code>. Defaults to <code>10</code>.</li>
</ul>
</li>
<li>
<p><code>filters</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Filter search results based on metadata. Supports comparison filters (<code>eq</code>, <code>ne</code>, <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code>) and compound filters (<code>and</code>, <code>or</code>). For more details, refer to <a href="/ai-search/configuration/retrieval/filtering/">Metadata filtering</a>.</li>
</ul>
</li>
<li>
<p><code>context_expansion</code> <span class="nb-type">integer</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The number of surrounding chunks to include for additional context. Must be between <code>0</code> and <code>3</code>. Defaults to <code>0</code>.</li>
</ul>
</li>
<li>
<p><code>fusion_method</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Controls how vector and keyword scores are combined when using hybrid retrieval. Valid values: <code>rrf</code> (Reciprocal Rank Fusion), <code>max</code> (takes the maximum score). Defaults to the instance-level setting.</li>
</ul>
</li>
<li>
<p><code>keyword_match_mode</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Controls how keyword (BM25) matching selects candidate documents. <code>and</code> requires all terms to match. <code>or</code> requires any term to match. Defaults to <code>and</code>.</li>
</ul>
</li>
<li>
<p><code>boost_by</code> <span class="nb-type">array</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Boost results by metadata fields. Maximum 3 items. Each item has:
<ul>
<li><code>field</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span> - The metadata field name to boost by (for example, <code>timestamp</code>). Maximum 64 characters.</li>
<li><code>direction</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span> - The boost direction. Valid values: <code>asc</code>, <code>desc</code>, <code>exists</code>, <code>not_exists</code>. Defaults to <code>asc</code> for numeric fields and <code>exists</code> for text fields.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>metadata_only</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Return only metadata for each chunk without the text content.</li>
</ul>
</li>
<li>
<p><code>return_on_failure</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Whether to return partial results if some processing steps fail. Defaults to <code>true</code>.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>query_rewrite</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p><code>enabled</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Rewrites the query to improve retrieval accuracy. Defaults to <code>false</code>.</li>
</ul>
</li>
<li>
<p><code>model</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The model to use for query rewriting.</li>
</ul>
</li>
<li>
<p><code>rewrite_prompt</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A custom prompt to guide query rewriting.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>reranking</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p><code>enabled</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Reorders retrieved results based on semantic relevance using a reranking model. Defaults to <code>false</code>.</li>
</ul>
</li>
<li>
<p><code>model</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The reranking model to use. Valid value: <code>@cf/baai/bge-reranker-base</code>.</li>
</ul>
</li>
<li>
<p><code>match_threshold</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The minimum score for reranked results. Must be between <code>0</code> and <code>1</code>. Defaults to <code>0.4</code>.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>cache</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p><code>enabled</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Override the instance-level cache setting for this request.</li>
</ul>
</li>
<li>
<p><code>cache_threshold</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The similarity threshold for cache hits. Valid values: <code>super_strict_match</code>, <code>close_enough</code>, <code>flexible_friend</code>, <code>anything_goes</code>.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h4 id="response-non-streaming">Response (non-streaming)</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>string</td>
<td>Unique identifier for the completion.</td>
</tr>
<tr>
<td><code>object</code></td>
<td>string</td>
<td>Always <code>chat.completion</code>.</td>
</tr>
<tr>
<td><code>created</code></td>
<td>number</td>
<td>Unix timestamp of when the completion was created.</td>
</tr>
<tr>
<td><code>model</code></td>
<td>string</td>
<td>The model used to generate the response.</td>
</tr>
<tr>
<td><code>choices</code></td>
<td>array</td>
<td>Array of completion choices.</td>
</tr>
<tr>
<td><code>choices[].message.role</code></td>
<td>string</td>
<td>Always <code>assistant</code>.</td>
</tr>
<tr>
<td><code>choices[].message.content</code></td>
<td>string</td>
<td>The generated response text.</td>
</tr>
<tr>
<td><code>choices[].finish_reason</code></td>
<td>string</td>
<td>Why the model stopped generating. Typically <code>stop</code>.</td>
</tr>
<tr>
<td><code>usage.prompt_tokens</code></td>
<td>number</td>
<td>Number of tokens in the prompt.</td>
</tr>
<tr>
<td><code>usage.completion_tokens</code></td>
<td>number</td>
<td>Number of tokens in the generated response.</td>
</tr>
<tr>
<td><code>usage.total_tokens</code></td>
<td>number</td>
<td>Total tokens used.</td>
</tr>
<tr>
<td><code>chunks</code></td>
<td>array</td>
<td>The source chunks used as context. Same format as the <a href="#response">search response</a>.</td>
</tr>
</tbody>
</table>
<h4 id="response-streaming">Response (streaming)</h4>
<p>When <code>stream: true</code>, the method returns a <code>ReadableStream</code> of Server-Sent Events. The retrieved chunks are sent first as a <code>chunks</code> event, followed by the streamed response.</p>
<pre tabindex="0"><code class="language-txt">event: chunks&#10;data: [{&quot;id&quot;:&quot;chunk-001&quot;,&quot;type&quot;:&quot;text&quot;,&quot;score&quot;:0.85,&quot;text&quot;:&quot;...&quot;,&quot;item&quot;:{&quot;key&quot;:&quot;about-cloudflare.md&quot;,&quot;timestamp&quot;:1775925540000},&quot;scoring_details&quot;:{&quot;vector_score&quot;:0.85}}]&#10;&#10;data: {&quot;id&quot;:&quot;id-1776072781845&quot;,&quot;created&quot;:1776072781,&quot;model&quot;:&quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&quot;object&quot;:&quot;chat.completion.chunk&quot;,&quot;choices&quot;:[{&quot;index&quot;:0,&quot;delta&quot;:{&quot;content&quot;:&quot; document&quot;}}]}&#10;&#10;data: {&quot;id&quot;:&quot;id-1776072781845&quot;,&quot;created&quot;:1776072781,&quot;model&quot;:&quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&quot;object&quot;:&quot;chat.completion.chunk&quot;,&quot;choices&quot;:[{&quot;index&quot;:0,&quot;delta&quot;:{&quot;content&quot;:&quot; you provided doesn&quot;}}]}&#10;&#10;data: {&quot;id&quot;:&quot;id-1776072781845&quot;,&quot;created&quot;:1776072781,&quot;model&quot;:&quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&quot;object&quot;:&quot;chat.completion.chunk&quot;,&quot;choices&quot;:[{&quot;index&quot;:0,&quot;delta&quot;:{&quot;content&quot;:&quot;&#x27;t contain&quot;}}]}&#10;&#10;data: {&quot;id&quot;:&quot;id-1776072781845&quot;,&quot;created&quot;:1776072781,&quot;model&quot;:&quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&quot;object&quot;:&quot;chat.completion.chunk&quot;,&quot;choices&quot;:[{&quot;index&quot;:0,&quot;delta&quot;:{&quot;content&quot;:&quot; information&quot;}}]}&#10;&#10;data: [DONE]&#10;</code></pre>
<h2 id="namespace-methods">Namespace methods</h2>
<p>The following methods are only available when using the <code>ai_search_namespaces</code> binding. Search and chat across multiple instances in a single call using the namespace handle directly (<code>env.AI_SEARCH</code>).</p>
<h3 id="search-1"><code>search()</code></h3>
<p>Pass <code>instance_ids</code> in <code>ai_search_options</code> to specify which instances to query. Results are merged and ranked, and each chunk includes an <code>instance_id</code> field identifying which instance it came from.</p>
<pre tabindex="0"><code class="language-ts">const results = await env.AI_SEARCH.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		instance_ids: [&quot;product-docs&quot;, &quot;customer-abc123&quot;],&#10;	},&#10;});&#10;</code></pre>
<h4 id="parameters-2">Parameters</h4>
<p>Same as <a href="#parameters">instance-level search</a>, with one additional required field:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ai_search_options</code></td>
<td>object</td>
<td>Yes</td>
<td>Required for namespace-level search.</td>
</tr>
<tr>
<td><code>ai_search_options.instance_ids</code></td>
<td>array</td>
<td>Yes</td>
<td>Instance IDs to search across. Minimum 1, maximum 10.</td>
</tr>
</tbody>
</table>
<h4 id="response-1">Response</h4>
<p>Same as <a href="#response">instance-level search</a>, with additional fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>chunks[].instance_id</code></td>
<td>string</td>
<td>The instance this chunk came from.</td>
</tr>
<tr>
<td><code>errors</code></td>
<td>array</td>
<td>Per-instance errors if any instances failed. Each object has <code>instance_id</code> and <code>message</code>.</td>
</tr>
</tbody>
</table>
<h3 id="chatcompletions-1"><code>chatCompletions()</code></h3>
<p>Generate chat completions using context retrieved from multiple instances.</p>
<pre tabindex="0"><code class="language-ts">const response = await env.AI_SEARCH.chatCompletions({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		instance_ids: [&quot;product-docs&quot;, &quot;customer-abc123&quot;],&#10;	},&#10;});&#10;</code></pre>
<p>Streaming is supported with <code>stream: true</code>.</p>
<h4 id="parameters-3">Parameters</h4>
<p>Same as <a href="#parameters-1">instance-level chat completions</a>, with one additional required field:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ai_search_options</code></td>
<td>object</td>
<td>Yes</td>
<td>Required for namespace-level chat completions.</td>
</tr>
<tr>
<td><code>ai_search_options.instance_ids</code></td>
<td>array</td>
<td>Yes</td>
<td>Instance IDs to search across. Minimum 1, maximum 10.</td>
</tr>
</tbody>
</table>
<h4 id="response-2">Response</h4>
<p>Same as <a href="#response-non-streaming">instance-level chat completions</a>, with additional fields on each chunk:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>chunks[].instance_id</code></td>
<td>string</td>
<td>The instance this chunk came from.</td>
</tr>
<tr>
<td><code>errors</code></td>
<td>array</td>
<td>Per-instance errors if any instances failed. Each object has <code>instance_id</code> and <code>message</code>.</td>
</tr>
</tbody>
</table>
<h2 id="local-development">Local development</h2>
<p>Local development is supported by proxying requests to your deployed AI Search instance. Add <code>remote: true</code> to your binding configuration to enable local development with <code>wrangler dev</code>.</p>
<pre tabindex="0"><code class="language-jsonc">// wrangler.jsonc&#10;{&#10;	&quot;ai_search&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;MY_SEARCH&quot;,&#10;			&quot;instance_name&quot;: &quot;my-instance&quot;,&#10;			&quot;remote&quot;: true,&#10;		},&#10;	],&#10;}&#10;</code></pre>
