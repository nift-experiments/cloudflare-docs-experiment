<p><a href="https://huggingface.co/">HuggingFace</a> helps users build, deploy and train machine learning models.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface&#10;</code></pre>
<h2 id="url-structure">URL structure</h2>
<p>When making requests to HuggingFace Inference API, replace <code>https://api-inference.huggingface.co/models/</code> in the URL you're currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface</code>. Note that the model you're trying to access should come right after, for example <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface/bigcode/starcoder</code>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to HuggingFace, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active HuggingFace API token.</li>
<li>The name of the HuggingFace model you want to use.</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface/bigcode/starcoder \&#10;  &#45;-header &#x27;Authorization: Bearer {hf_api_token}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;inputs&quot;: &quot;console.log&quot;&#10;}&#x27;&#10;</code></pre>
<h3 id="use-huggingface-js-library-with-javascript">Use HuggingFace.js library with JavaScript</h3>
<p>If you are using the HuggingFace.js library, you can set your inference endpoint like this:</p>
<pre><code class="language-js">import { HfInferenceEndpoint } from &quot;@huggingface/inference&quot;;&#10;&#10;const accountId = &quot;{account_id}&quot;;&#10;const gatewayId = &quot;{gateway_id}&quot;;&#10;const model = &quot;gpt2&quot;;&#10;const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/huggingface/${model}`;&#10;const apiToken = env.HF_API_TOKEN;&#10;&#10;const hf = new HfInferenceEndpoint(baseURL, apiToken);&#10;</code></pre>
