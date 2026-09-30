<p><a href="https://www.perplexity.ai/">Perplexity</a> is an AI powered answer engine.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/perplexity-ai&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Perplexity, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active Perplexity API token.</li>
<li>The name of the Perplexity model you want to use.</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/perplexity-ai/chat/completions \&#10;     &#45;-header &#x27;accept: application/json&#x27; \&#10;     &#45;-header &#x27;content-type: application/json&#x27; \&#10;     &#45;-header &#x27;Authorization: Bearer {perplexity_token}&#x27; \&#10;     &#45;-data &#x27;{&#10;      &quot;model&quot;: &quot;mistral-7b-instruct&quot;,&#10;      &quot;messages&quot;: [&#10;        {&#10;          &quot;role&quot;: &quot;user&quot;,&#10;          &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;      ]&#10;    }&#x27;&#10;</code></pre>
<h3 id="use-perplexity-through-openai-sdk-with-javascript">Use Perplexity through OpenAI SDK with JavaScript</h3>
<p>Perplexity does not have their own SDK, but they have compatibility with the OpenAI SDK. You can use the OpenAI SDK to make a Perplexity call through AI Gateway as follows:</p>
<pre><code class="language-js">import OpenAI from &quot;openai&quot;;&#10;&#10;const apiKey = env.PERPLEXITY_API_KEY;&#10;const accountId = &quot;{account_id}&quot;;&#10;const gatewayId = &quot;{gateway_id}&quot;;&#10;const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/perplexity-ai`;&#10;&#10;const perplexity = new OpenAI({&#10;	apiKey,&#10;	baseURL,&#10;});&#10;&#10;const model = &quot;mistral-7b-instruct&quot;;&#10;const messages = [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }];&#10;const maxTokens = 20;&#10;&#10;const chatCompletion = await perplexity.chat.completions.create({&#10;	model,&#10;	messages,&#10;	max_tokens: maxTokens,&#10;});&#10;</code></pre>
<h2 id="openai-compatible-endpoint">OpenAI-Compatible Endpoint</h2>
<p>You can also access Perplexity models using the OpenAI API schema through the <a href="/ai-gateway/usage/rest-api/">REST API</a>. Send your requests to:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions&#10;</code></pre>
<p>Specify:</p>
<pre><code class="language-json">{&#10;	&amp;quot;model&amp;quot;: &amp;quot;perplexity/{model}&amp;quot;&#10;}</code></pre>
