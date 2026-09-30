<p><a href="https://azure.microsoft.com/en-gb/products/ai-services/openai-service/">Azure OpenAI</a> allows you apply natural language algorithms on your data.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/azure-openai/{resource_name}/{deployment_name}&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Azure OpenAI, you will need:</p>
<ul>
<li>AI Gateway account ID</li>
<li>AI Gateway gateway name</li>
<li>Azure OpenAI API key</li>
<li>Azure OpenAI resource name</li>
<li>Azure OpenAI deployment name (aka model name)</li>
</ul>
<h2 id="url-structure">URL structure</h2>
<p>Your new base URL will use the data above in this structure: <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/azure-openai/{resource_name}/{deployment_name}</code>. Then, you can append your endpoint and api-version at the end of the base URL, like <code>.../chat/completions?api-version=2023-05-15</code>.</p>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<pre><code class="language-bash">curl &#x27;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway}/azure-openai/{resource_name}/{deployment_name}/chat/completions?api-version=2023-05-15&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;api-key: {azure_api_key}&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;messages&quot;: [&#10;    {&#10;      &quot;role&quot;: &quot;user&quot;,&#10;      &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<h3 id="use-openai-javascript-sdk">Use <code>openai</code> JavaScript SDK</h3>
<pre><code class="language-js">import { AzureOpenAI } from &quot;openai&quot;;&#10;&#10;const azure_openai = new AzureOpenAI({&#10;  apiKey: &quot;{azure_api_key}&quot;,&#10;  baseURL: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway}/azure-openai/{resource_name}/`,&#10;  apiVersion: &quot;2023-05-15&quot;,&#10;  defaultHeaders: { &quot;cf-aig-authorization&quot;: &quot;{cf-api-token}&quot; }, // if authenticated&#10;});&#10;&#10;const result = await azure_openai.chat.completions.create({&#10;  model: &#x27;{deployment_name}&#x27;,&#10;  messages: [{ role: &quot;user&quot;, content: &quot;Hello&quot; }],&#10;});&#10;</code></pre>
