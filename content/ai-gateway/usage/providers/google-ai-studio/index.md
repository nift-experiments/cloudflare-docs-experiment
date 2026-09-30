<p><a href="https://ai.google.dev/aistudio">Google AI Studio</a> helps you build quickly with Google Gemini models.</p>
<h2 id="endpoint">Endpoint</h2>
<p><strong>Base URL:</strong></p>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-ai-studio&#10;</code></pre>
<p>Then you can append the endpoint you want to hit, for example: <code>v1/models/{model}:{generative_ai_rest_resource}</code></p>
<p>So your final URL will come together as: <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-ai-studio/v1/models/{model}:{generative_ai_rest_resource}</code>.</p>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<details class="nb-details"><summary>With API Key in Request</summary><div class="nb-details-body">
@input("content/.markup/bodies/2973.md")
</div></details>
<details class="nb-details" open><summary>With Stored Keys (BYOK) / Unified Billing</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2974.md")
</div></details>
<h3 id="google-genai"><code>@google/genai</code></h3>
<p>If you are using the <code>@google/genai</code> package, you can set your endpoint like this:</p>
<details class="nb-details"><summary>With Key in Request</summary><div class="nb-details-body">
@input("content/.markup/bodies/2978.md")
</div></details>
<details class="nb-details" open><summary>With Stored Keys (BYOK) / Unified Billing</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2979.md")
</div></details>
<h2 id="openai-compatible-endpoint">OpenAI-Compatible Endpoint</h2>
<p>You can also access Google AI Studio models using the OpenAI API schema through the <a href="/ai-gateway/usage/rest-api/">REST API</a>. Send your requests to:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions&#10;</code></pre>
<p>Specify:</p>
<pre><code class="language-json">{&#10;	&amp;quot;model&amp;quot;: &amp;quot;google-ai-studio/{model}&amp;quot;&#10;}</code></pre>
