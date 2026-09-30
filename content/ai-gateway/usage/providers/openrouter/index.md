<p><a href="https://openrouter.ai/">OpenRouter</a> is a platform that provides a unified interface for accessing and using large language models (LLMs).</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openrouter&#10;</code></pre>
<h2 id="url-structure">URL structure</h2>
<p>When making requests to <a href="https://openrouter.ai/">OpenRouter</a>, replace <code>https://openrouter.ai/api/v1/chat/completions</code> in the URL you are currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openrouter/chat/completions</code>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to OpenRouter, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active OpenRouter API token or a token from the original model provider.</li>
<li>The name of the OpenRouter model you want to use.</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<pre><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openrouter/v1/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer OPENROUTER_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-5-mini&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<h3 id="use-openai-sdk-with-javascript">Use OpenAI SDK with JavaScript</h3>
<p>If you are using the OpenAI SDK with JavaScript, you can set your endpoint like this:</p>
<pre><code class="language-js">import OpenAI from &quot;openai&quot;;&#10;&#10;const openai = new OpenAI({&#10;	apiKey: env.OPENROUTER_TOKEN,&#10;	baseURL:&#10;		&quot;https://gateway.ai.cloudflare.com/v1/ACCOUNT_TAG/GATEWAY/openrouter&quot;,&#10;});&#10;&#10;try {&#10;	const chatCompletion = await openai.chat.completions.create({&#10;		model: &quot;openai/gpt-5-mini&quot;,&#10;		messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	});&#10;&#10;	const response = chatCompletion.choices[0].message;&#10;&#10;	return new Response(JSON.stringify(response));&#10;} catch (e) {&#10;	return new Response(e);&#10;}&#10;</code></pre>
