<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="embeddinggemma-300m">embeddinggemma-300m</h1>

<p><code>@cf/google/embeddinggemma-300m</code></p>

EmbeddingGemma is a 300M parameter, state-of-the-art for its size, open embedding model from Google, built from Gemma 3 (with T5Gemma initialization) and the same research and technology used to create Gemini models. EmbeddingGemma produces vector representations of text, making it well-suited for search and retrieval tasks, including classification, clustering, and semantic similarity search. This model was trained with data in 100+ spoken languages.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Embeddings</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<div class="nb-tabs" data-nb-tabs><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="TypeScript"><pre><code class="language-ts">export default { async fetch(request, env) { const response = await env.AI.run("@cf/google/embeddinggemma-300m", { text: ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }); return Response.json(response); } } satisfies ExportedHandler&lt;Env&gt;;</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="Python"><pre><code class="language-py">output = requests.post("https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/google/embeddinggemma-300m", headers={"Authorization": "Bearer {API_KEY}"}, json={ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] })
print(output.json())</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="curl"><pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/google/embeddinggemma-300m -X POST -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" -d '{ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }'</code></pre></section></div><aside class="nb-aside note"><p>Workers AI also supports OpenAI compatible API endpoints for <code>/v1/chat/completions</code> and <code>/v1/embeddings</code>. For more details, refer to <a href="/workers-ai/configuration/open-ai-compatibility/">Configurations</a>.</p></aside>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string or array</td><td>Required.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>shape</code></td><td>array</td><td></td></tr><tr><td><code>data</code></td><td>array</td><td>Embeddings of the requested text values</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/embeddinggemma-300m/schema-input.json)
- [Output schema](/workers-ai/models/embeddinggemma-300m/schema-output.json)

