<p><a href="https://ideogram.ai/">Ideogram</a> provides advanced text-to-image generation models with exceptional text rendering capabilities and visual quality.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/ideogram&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Ideogram, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active Ideogram API key.</li>
<li>The name of the Ideogram model you want to use (e.g., <code>V_3</code>).</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/ideogram/v1/ideogram-v3/generate \&#10;  &#45;-header &#x27;Api-Key: {ideogram_api_key}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;prompt&quot;: &quot;A serene landscape with mountains and a lake at sunset&quot;,&#10;    &quot;model&quot;: &quot;V_3&quot;&#10;  }&#x27;&#10;</code></pre>
<h3 id="use-with-javascript">Use with JavaScript</h3>
<pre><code class="language-js">const accountId = &quot;{account_id}&quot;;&#10;const gatewayId = &quot;{gateway_id}&quot;;&#10;const ideogramApiKey = &quot;{ideogram_api_key}&quot;;&#10;const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/ideogram`;&#10;&#10;const response = await fetch(`${baseURL}/v1/ideogram-v3/generate`, {&#10;  method: &quot;POST&quot;,&#10;  headers: {&#10;    &quot;Api-Key&quot;: ideogramApiKey,&#10;    &quot;Content-Type&quot;: &quot;application/json&quot;,&#10;  },&#10;  body: JSON.stringify({&#10;    prompt: &quot;A serene landscape with mountains and a lake at sunset&quot;,&#10;    model: &quot;V_3&quot;,&#10;  }),&#10;});&#10;&#10;const result = await response.json();&#10;console.log(result);&#10;</code></pre>
