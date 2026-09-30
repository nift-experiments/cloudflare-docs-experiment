<p><a href="https://www.deepseek.com/">DeepSeek</a> helps you build quickly with DeepSeek's advanced AI models.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to DeepSeek, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active DeepSeek AI API token.</li>
<li>The name of the DeepSeek AI model you want to use.</li>
</ul>
<h2 id="url-structure">URL structure</h2>
<p>Your new base URL will use the data above in this structure:</p>
<p><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/</code>.</p>
<p>You can then append the endpoint you want to hit, for example: <code>chat/completions</code>.</p>
<p>So your final URL will come together as:</p>
<p><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions</code>.</p>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer DEEPSEEK_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;deepseek-chat&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<h3 id="use-deepseek-with-javascript">Use DeepSeek with JavaScript</h3>
<p>If you are using the OpenAI SDK, you can set your endpoint like this:</p>
<pre><code class="language-js">import OpenAI from &quot;openai&quot;;&#10;&#10;const openai = new OpenAI({&#10;	apiKey: env.DEEPSEEK_TOKEN,&#10;	baseURL:&#10;		&quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek&quot;,&#10;});&#10;&#10;try {&#10;	const chatCompletion = await openai.chat.completions.create({&#10;		model: &quot;deepseek-chat&quot;,&#10;		messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	});&#10;&#10;	const response = chatCompletion.choices[0].message;&#10;&#10;	return new Response(JSON.stringify(response));&#10;} catch (e) {&#10;	return new Response(e);&#10;}&#10;</code></pre>
<h2 id="openai-compatible-endpoint">OpenAI-Compatible Endpoint</h2>
<p>You can also access DeepSeek models using the OpenAI API schema through the <a href="/ai-gateway/usage/rest-api/">REST API</a>. Send your requests to:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions&#10;</code></pre>
<p>Specify:</p>
<pre><code class="language-json">{&#10;	&amp;quot;model&amp;quot;: &amp;quot;deepseek/{model}&amp;quot;&#10;}</code></pre>
