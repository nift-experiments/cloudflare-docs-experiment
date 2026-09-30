<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="m2m100-1-2b">m2m100-1.2b</h1>

<p><code>@cf/meta/m2m100-1.2b</code></p>

Multilingual encoder-decoder (seq-to-seq) model trained for Many-to-Many multilingual translation

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Translation</td></tr>
<tr><th>Asynchronous queue</th><td>Yes</td></tr>
<tr><th>More information</th><td><a href="https://github.com/facebookresearch/fairseq/tree/main/examples/m2m_100">Model details</a></td></tr>
<tr><th>Terms</th><td><a href="https://github.com/facebookresearch/fairseq/blob/main/LICENSE">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>USD 0.342 per M input tokens, USD 0.342 per M output tokens</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">export default {
  async fetch(request, env) {
    const input = await request.json();
    const response = await env.AI.run(&quot;@cf/meta/m2m100-1.2b&quot;, input);
    return Response.json(response);
  },
} satisfies ExportedHandler&lt;Env&gt;;</code></pre>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/meta/m2m100-1.2b&quot;, { translation: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/meta/m2m100-1.2b -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The text to be translated Minimum length: 1</td></tr><tr><td><code>source_lang</code></td><td>string</td><td>The language code of the source text (e.g., 'en' for English). Defaults to 'en' if not specified Default: en</td></tr><tr><td><code>target_lang</code></td><td>string</td><td>Required. The language code to translate the text into (e.g., 'es' for Spanish)</td></tr><tr><td><code>requests</code></td><td>array</td><td>Required. Batch of the embeddings requests to run using async-queue</td></tr><tr><td><code>requests[].text</code></td><td>string</td><td>Required. The text to be translated Minimum length: 1</td></tr><tr><td><code>requests[].source_lang</code></td><td>string</td><td>The language code of the source text (e.g., 'en' for English). Defaults to 'en' if not specified Default: en</td></tr><tr><td><code>requests[].target_lang</code></td><td>string</td><td>Required. The language code to translate the text into (e.g., 'es' for Spanish)</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>translated_text</code></td><td>string</td><td>The translated text in the target language</td></tr><tr><td><code>request_id</code></td><td>string</td><td>The async request id that can be used to obtain the results.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/m2m100-1.2b/schema-input.json)
- [Output schema](/workers-ai/models/m2m100-1.2b/schema-output.json)

