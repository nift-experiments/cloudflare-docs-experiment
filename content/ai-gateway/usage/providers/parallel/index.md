<p><a href="https://parallel.ai/">Parallel</a> is a web API purpose-built for AIs, providing production-ready outputs with minimal hallucination and evidence-based results.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/parallel&#10;</code></pre>
<h2 id="url-structure">URL structure</h2>
<p>When making requests to Parallel, you can route to any Parallel endpoint through AI Gateway by appending the path after <code>parallel</code>. For example, to access the Tasks API at <code>/v1/tasks/runs</code>, use:</p>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/parallel/v1/tasks/runs&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Parallel, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active Parallel API key.</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="tasks-api">Tasks API</h3>
<p>The <a href="https://docs.parallel.ai/task-api/task-quickstart">Tasks API</a> allows you to create comprehensive research and analysis tasks.</p>
<h4 id="curl-example">cURL example</h4>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/parallel/v1/tasks/runs \&#10;  &#45;-header &#x27;x-api-key: {parallel_api_key}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;input&quot;: &quot;Create a comprehensive market research report on the HVAC industry in the USA including an analysis of recent M&amp;A activity and other relevant details.&quot;,&#10;    &quot;processor&quot;: &quot;ultra&quot;&#10;  }&#x27;&#10;</code></pre>
<h3 id="search-api">Search API</h3>
<p>The <a href="https://docs.parallel.ai/search-api/search-quickstart">Search API</a> enables advanced search with configurable parameters.</p>
<h4 id="curl-example-1">cURL example</h4>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/parallel/v1beta/search \&#10;  &#45;-header &#x27;x-api-key: {parallel_api_key}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;objective&quot;: &quot;When was the United Nations established? Prefer UN&#x27;\&#x27;&#x27;s websites.&quot;,&#10;    &quot;search_queries&quot;: [&#10;      &quot;Founding year UN&quot;,&#10;      &quot;Year of founding United Nations&quot;&#10;    ],&#10;    &quot;processor&quot;: &quot;base&quot;,&#10;    &quot;max_results&quot;: 10,&#10;    &quot;max_chars_per_result&quot;: 6000&#10;  }&#x27;&#10;</code></pre>
<h2 id="chat-api">Chat API</h2>
<p>The <a href="https://docs.parallel.ai/chat-api/chat-quickstart">Chat API</a> is supported through AI Gateway's Unified Chat Completions API. See below for more details:</p>
<h2 id="openai-compatible-endpoint">OpenAI-Compatible Endpoint</h2>
<p>You can also access Parallel models using the OpenAI API schema through the <a href="/ai-gateway/usage/rest-api/">REST API</a>. Send your requests to:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions&#10;</code></pre>
<p>Specify:</p>
<pre><code class="language-json">{&#10;	&amp;quot;model&amp;quot;: &amp;quot;parallel/{model}&amp;quot;&#10;}</code></pre>
<h4 id="javascript-sdk-example">JavaScript SDK example</h4>
<pre><code class="language-js">import OpenAI from &quot;openai&quot;;&#10;&#10;const apiKey = &quot;{parallel_api_key}&quot;;&#10;const accountId = &quot;{account_id}&quot;;&#10;const gatewayId = &quot;{gateway_id}&quot;;&#10;const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/compat`;&#10;&#10;const client = new OpenAI({&#10;	apiKey,&#10;	baseURL,&#10;});&#10;&#10;try {&#10;	const model = &quot;parallel/speed&quot;;&#10;	const messages = [{ role: &quot;user&quot;, content: &quot;Hello!&quot; }];&#10;	const chatCompletion = await client.chat.completions.create({&#10;		model,&#10;		messages,&#10;	});&#10;	const response = chatCompletion.choices[0].message;&#10;	console.log(response);&#10;} catch (e) {&#10;	console.error(e);&#10;}&#10;</code></pre>
<h3 id="findall-api">FindAll API</h3>
<p>The <a href="https://docs.parallel.ai/findall-api/findall-quickstart">FindAll API</a> enables structured data extraction from complex queries.</p>
<h4 id="curl-example-2">cURL example</h4>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/parallel/v1beta/findall/ingest \&#10;  &#45;-header &#x27;x-api-key: {parallel_api_key}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;query&quot;: &quot;Find all AI companies that recently raised money and get their website, CEO name, and CTO name.&quot;&#10;  }&#x27;&#10;</code></pre>
