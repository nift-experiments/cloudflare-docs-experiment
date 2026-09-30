<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="bge-reranker-base">bge-reranker-base</h1>

<p><code>@cf/baai/bge-reranker-base</code></p>

Different from embedding model, reranker uses question and document as input and directly output similarity instead of embedding. You can get a relevance score by inputting query and passage to the reranker. And the score can be mapped to a float value in [0,1] by sigmoid function.



<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Classification</td></tr>
<tr><th>Unit pricing</th><td>USD 0.00311 per M input tokens</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<div class="nb-tabs" data-nb-tabs><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="TypeScript"><pre><code class="language-ts">export default { async fetch(request, env) { const response = await env.AI.run("@cf/baai/bge-reranker-base", { text: "This pizza is great!" }); return Response.json(response); } } satisfies ExportedHandler&lt;Env&gt;;</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="Python"><pre><code class="language-py">output = requests.post("https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/baai/bge-reranker-base", headers={"Authorization": "Bearer {API_KEY}"}, json={ "text": "This pizza is great!" })
print(output.json())</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="curl"><pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/baai/bge-reranker-base -X POST -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" -d '{ "text": "This pizza is great!" }'</code></pre></section></div>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>query</code></td><td>string</td><td>Required. A query you wish to perform against the provided contexts. Minimum length: 1</td></tr><tr><td><code>top_k</code></td><td>integer</td><td>Number of returned results starting with the best score. Minimum: 1</td></tr><tr><td><code>contexts</code></td><td>array</td><td>Required. List of provided contexts. Note that the index in this array is important, as the response will refer to it.</td></tr><tr><td><code>contexts[].text</code></td><td>string</td><td>One of the provided context content Minimum length: 1</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>response</code></td><td>array</td><td></td></tr><tr><td><code>response[].id</code></td><td>integer</td><td>Index of the context in the request</td></tr><tr><td><code>response[].score</code></td><td>number</td><td>Score of the context under the index.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/bge-reranker-base/schema-input.json)
- [Output schema](/workers-ai/models/bge-reranker-base/schema-output.json)

