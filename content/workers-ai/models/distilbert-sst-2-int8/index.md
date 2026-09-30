<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="distilbert-sst-2-int8">distilbert-sst-2-int8</h1>

<p><code>@cf/huggingface/distilbert-sst-2-int8</code></p>

Distilled BERT model that was finetuned on SST-2 for sentiment classification

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Classification</td></tr>
<tr><th>More information</th><td><a href="https://huggingface.co/Intel/distilbert-base-uncased-finetuned-sst-2-english-int8-static">Model details</a></td></tr>
<tr><th>Unit pricing</th><td>USD 0.0263 per M input tokens</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<div class="nb-tabs" data-nb-tabs><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="TypeScript"><pre><code class="language-ts">export default { async fetch(request, env) { const response = await env.AI.run("@cf/huggingface/distilbert-sst-2-int8", { text: "This pizza is great!" }); return Response.json(response); } } satisfies ExportedHandler&lt;Env&gt;;</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="Python"><pre><code class="language-py">output = requests.post("https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/huggingface/distilbert-sst-2-int8", headers={"Authorization": "Bearer {API_KEY}"}, json={ "text": "This pizza is great!" })
print(output.json())</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="curl"><pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/huggingface/distilbert-sst-2-int8 -X POST -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" -d '{ "text": "This pizza is great!" }'</code></pre></section></div>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The text that you want to classify Minimum length: 1</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<p>No parameters.</p>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/distilbert-sst-2-int8/schema-input.json)
- [Output schema](/workers-ai/models/distilbert-sst-2-int8/schema-output.json)

