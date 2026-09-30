<p><a href="https://www.baseten.co/">Baseten</a> provides infrastructure for building and deploying machine learning models at scale. Baseten offers access to various language models through a unified chat completions API.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/baseten&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Baseten, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active Baseten API token.</li>
<li>The name of the Baseten model you want to use.</li>
</ul>
<h2 id="openai-compatible-chat-completions-api">OpenAI-compatible chat completions API</h2>
<p>Baseten provides an OpenAI-compatible chat completions API for supported models.</p>
<h3 id="curl">cURL</h3>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/baseten/v1/chat/completions \&#10;  &#45;-header &#x27;Authorization: Bearer {baseten_api_token}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-oss-120b&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h3 id="use-openai-sdk-with-javascript">Use OpenAI SDK with JavaScript</h3>
<pre><code class="language-js">import OpenAI from &quot;openai&quot;;&#10;&#10;const apiKey = &quot;{baseten_api_token}&quot;;&#10;const accountId = &quot;{account_id}&quot;;&#10;const gatewayId = &quot;{gateway_id}&quot;;&#10;const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/baseten`;&#10;&#10;const openai = new OpenAI({&#10;  apiKey,&#10;  baseURL,&#10;});&#10;&#10;const model = &quot;openai/gpt-oss-120b&quot;;&#10;const messages = [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }];&#10;&#10;const chatCompletion = await openai.chat.completions.create({&#10;  model,&#10;  messages,&#10;});&#10;&#10;console.log(chatCompletion);&#10;</code></pre>
<h2 id="openai-compatible-endpoint">OpenAI-Compatible Endpoint</h2>
<p>You can also access Baseten models using the OpenAI API schema through the <a href="/ai-gateway/usage/rest-api/">REST API</a>. Send your requests to:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions&#10;</code></pre>
<p>Specify:</p>
<pre><code class="language-json">{&#10;  &amp;quot;model&amp;quot;: &amp;quot;baseten/{model}&amp;quot;&#10;}</code></pre>
<h2 id="model-specific-endpoints">Model-specific endpoints</h2>
<p>For models that don't use the OpenAI-compatible API, you can access them through their specific model endpoints.</p>
<h3 id="curl-1">cURL</h3>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/baseten/model/{model_id} \&#10;  &#45;-header &#x27;Authorization: Bearer {baseten_api_token}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;prompt&quot;: &quot;What is Cloudflare?&quot;,&#10;    &quot;max_tokens&quot;: 100&#10;  }&#x27;&#10;</code></pre>
<h3 id="use-with-javascript">Use with JavaScript</h3>
<pre><code class="language-js">const accountId = &quot;{account_id}&quot;;&#10;const gatewayId = &quot;{gateway_id}&quot;;&#10;const basetenApiToken = &quot;{baseten_api_token}&quot;;&#10;const modelId = &quot;{model_id}&quot;;&#10;const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/baseten`;&#10;&#10;const response = await fetch(`${baseURL}/model/${modelId}`, {&#10;  method: &quot;POST&quot;,&#10;  headers: {&#10;    &quot;Authorization&quot;: `Bearer ${basetenApiToken}`,&#10;    &quot;Content-Type&quot;: &quot;application/json&quot;,&#10;  },&#10;  body: JSON.stringify({&#10;    prompt: &quot;What is Cloudflare?&quot;,&#10;    max_tokens: 100,&#10;  }),&#10;});&#10;&#10;const result = await response.json();&#10;console.log(result);&#10;</code></pre>
