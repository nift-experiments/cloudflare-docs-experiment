<p>Use Workers AI with <a href="https://github.com/huggingface/chat-ui?tab=readme-ov-file#text-embedding-models">Chat UI</a>, an open-source chat interface offered by Hugging Face.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You will need the following:</p>
<ul>
<li>A <a href="https://dash.cloudflare.com">Cloudflare account</a></li>
<li>Your <a href="/fundamentals/account/find-account-and-zone-ids/">Account ID</a></li>
<li>An <a href="/workers-ai/get-started/rest-api/#1-get-api-token-and-account-id">API token</a> for Workers AI</li>
</ul>
<h2 id="setup">Setup</h2>
<p>First, decide how to reference your Account ID and API token (either directly in your <code>.env.local</code> using the <code>CLOUDFLARE_ACCOUNT_ID</code> and <code>CLOUDFLARE_API_TOKEN</code> variables or in the endpoint configuration).</p>
<p>Then, follow the rest of the setup instructions in the <a href="https://github.com/huggingface/chat-ui?tab=readme-ov-file#text-embedding-models">Chat UI GitHub repository</a>.</p>
<p>When setting up your models, specify the <code>cloudflare</code> endpoint.</p>
<pre><code class="language-json">{&#10;  &quot;name&quot; : &quot;nousresearch/hermes-2-pro-mistral-7b&quot;,&#10;  &quot;tokenizer&quot;: &quot;nousresearch/hermes-2-pro-mistral-7b&quot;,&#10;  &quot;parameters&quot;: {&#10;    &quot;stop&quot;: [&quot;&lt;|im_end|&gt;&quot;]&#10;  },&#10;  &quot;endpoints&quot; : [&#10;    {&#10;      &quot;type&quot;: &quot;cloudflare&quot;,&#10;      // optionally specify these if not included in .env.local&#10;      &quot;accountId&quot;: &quot;your-account-id&quot;,&#10;      &quot;apiToken&quot;: &quot;your-api-token&quot;&#10;      //&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h2 id="supported-models">Supported models</h2>
<p>This template works with any <a href="/workers-ai/models/">text generation models</a> that begin with the <code>@hf</code> parameter.</p>
