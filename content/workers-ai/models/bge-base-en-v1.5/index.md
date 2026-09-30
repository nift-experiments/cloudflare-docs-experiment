<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="bge-base-en-v1-5">bge-base-en-v1.5</h1>

<p><code>@cf/baai/bge-base-en-v1.5</code></p>

BAAI general embedding (Base) model that transforms any given text into a 768-dimensional vector

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Embeddings</td></tr>
<tr><th>Context window</th><td>153,600 tokens</td></tr>
<tr><th>Maximum input tokens</th><td>512 tokens</td></tr>
<tr><th>Output dimensions</th><td>768</td></tr>
<tr><th>Asynchronous queue</th><td>Yes</td></tr>
<tr><th>More information</th><td><a href="https://huggingface.co/BAAI/bge-base-en-v1.5">Model details</a></td></tr>
<tr><th>Unit pricing</th><td>USD 0.0666 per M input tokens</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<div class="nb-tabs" data-nb-tabs><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="TypeScript"><pre><code class="language-ts">export default { async fetch(request, env) { const response = await env.AI.run("@cf/baai/bge-base-en-v1.5", { text: ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }); return Response.json(response); } } satisfies ExportedHandler&lt;Env&gt;;</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="Python"><pre><code class="language-py">output = requests.post("https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/baai/bge-base-en-v1.5", headers={"Authorization": "Bearer {API_KEY}"}, json={ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] })
print(output.json())</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="curl"><pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/baai/bge-base-en-v1.5 -X POST -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" -d '{ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }'</code></pre></section></div><aside class="nb-aside note"><p>Workers AI also supports OpenAI compatible API endpoints for <code>/v1/chat/completions</code> and <code>/v1/embeddings</code>. For more details, refer to <a href="/workers-ai/configuration/open-ai-compatibility/">Configurations</a>.</p></aside>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>pooling</code></td><td>string</td><td>The pooling method used in the embedding process. `cls` pooling will generate more accurate embeddings on larger inputs - however, embeddings created with cls pooling are not compatible with embeddings generated with mean pooling. The default pooling method is `mean` in order for this to not be a breaking change, but we highly suggest using the new `cls` pooling for better accuracy. Default: mean; Values: mean, cls</td></tr><tr><td><code>requests</code></td><td>array</td><td>Required. Batch of the embeddings requests to run using async-queue</td></tr><tr><td><code>requests[].text</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>requests[].pooling</code></td><td>string</td><td>The pooling method used in the embedding process. `cls` pooling will generate more accurate embeddings on larger inputs - however, embeddings created with cls pooling are not compatible with embeddings generated with mean pooling. The default pooling method is `mean` in order for this to not be a breaking change, but we highly suggest using the new `cls` pooling for better accuracy. Default: mean; Values: mean, cls</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>shape</code></td><td>array</td><td></td></tr><tr><td><code>data</code></td><td>array</td><td>Embeddings of the requested text values</td></tr><tr><td><code>pooling</code></td><td>string</td><td>The pooling method used in the embedding process. Values: mean, cls</td></tr><tr><td><code>request_id</code></td><td>string</td><td>The async request id that can be used to obtain the results.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/bge-base-en-v1.5/schema-input.json)
- [Output schema](/workers-ai/models/bge-base-en-v1.5/schema-output.json)

