<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="bge-m3">bge-m3</h1>

<p><code>@cf/baai/bge-m3</code></p>

Multi-Functionality, Multi-Linguality, and Multi-Granularity embeddings model.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Embeddings</td></tr>
<tr><th>Context window</th><td>60,000 tokens</td></tr>
<tr><th>Unit pricing</th><td>USD 0.0118 per M input tokens</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<div class="nb-tabs" data-nb-tabs><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="TypeScript"><pre><code class="language-ts">export default { async fetch(request, env) { const response = await env.AI.run("@cf/baai/bge-m3", { text: ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }); return Response.json(response); } } satisfies ExportedHandler&lt;Env&gt;;</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="Python"><pre><code class="language-py">output = requests.post("https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/baai/bge-m3", headers={"Authorization": "Bearer {API_KEY}"}, json={ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] })
print(output.json())</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="curl"><pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/baai/bge-m3 -X POST -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" -d '{ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }'</code></pre></section></div><aside class="nb-aside note"><p>Workers AI also supports OpenAI compatible API endpoints for <code>/v1/chat/completions</code> and <code>/v1/embeddings</code>. For more details, refer to <a href="/workers-ai/configuration/open-ai-compatibility/">Configurations</a>.</p></aside>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>query</code></td><td>string</td><td>A query you wish to perform against the provided contexts. If no query is provided the model with respond with embeddings for contexts Minimum length: 1</td></tr><tr><td><code>contexts</code></td><td>array</td><td>Required. List of provided contexts. Note that the index in this array is important, as the response will refer to it.</td></tr><tr><td><code>contexts[].text</code></td><td>string</td><td>One of the provided context content Minimum length: 1</td></tr><tr><td><code>truncate_inputs</code></td><td>boolean</td><td>When provided with too long context should the model error out or truncate the context to fit? Default: False</td></tr><tr><td><code>text</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>truncate_inputs</code></td><td>boolean</td><td>When provided with too long context should the model error out or truncate the context to fit? Default: False</td></tr><tr><td><code>requests</code></td><td>array</td><td>Required. Batch of the embeddings requests to run using async-queue</td></tr><tr><td><code>requests[].query</code></td><td>string</td><td>A query you wish to perform against the provided contexts. If no query is provided the model with respond with embeddings for contexts Minimum length: 1</td></tr><tr><td><code>requests[].contexts</code></td><td>array</td><td>Required. List of provided contexts. Note that the index in this array is important, as the response will refer to it.</td></tr><tr><td><code>requests[].contexts[].text</code></td><td>string</td><td>One of the provided context content Minimum length: 1</td></tr><tr><td><code>requests[].truncate_inputs</code></td><td>boolean</td><td>When provided with too long context should the model error out or truncate the context to fit? Default: False</td></tr><tr><td><code>requests[].text</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>requests[].truncate_inputs</code></td><td>boolean</td><td>When provided with too long context should the model error out or truncate the context to fit? Default: False</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>response</code></td><td>array</td><td></td></tr><tr><td><code>response[].id</code></td><td>integer</td><td>Index of the context in the request</td></tr><tr><td><code>response[].score</code></td><td>number</td><td>Score of the context under the index.</td></tr><tr><td><code>response</code></td><td>array</td><td></td></tr><tr><td><code>shape</code></td><td>array</td><td></td></tr><tr><td><code>pooling</code></td><td>string</td><td>The pooling method used in the embedding process. Values: mean, cls</td></tr><tr><td><code>shape</code></td><td>array</td><td></td></tr><tr><td><code>data</code></td><td>array</td><td>Embeddings of the requested text values</td></tr><tr><td><code>pooling</code></td><td>string</td><td>The pooling method used in the embedding process. Values: mean, cls</td></tr><tr><td><code>request_id</code></td><td>string</td><td>The async request id that can be used to obtain the results.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/bge-m3/schema-input.json)
- [Output schema](/workers-ai/models/bge-m3/schema-output.json)

