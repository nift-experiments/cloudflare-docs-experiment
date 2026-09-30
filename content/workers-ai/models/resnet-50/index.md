<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="resnet-50">resnet-50</h1>

<p><code>@cf/microsoft/resnet-50</code></p>

50 layers deep image classification CNN trained on more than 1M images from ImageNet

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Image Classification</td></tr>
<tr><th>More information</th><td><a href="https://www.microsoft.com/en-us/research/blog/microsoft-vision-model-resnet-50-combines-web-scale-data-and-multi-task-learning-to-achieve-state-of-the-art/">Model details</a></td></tr>
<tr><th>Unit pricing</th><td>USD 2.51e-06 per inference request</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">export default {
  async fetch(request, env) {
    const input = await request.json();
    const response = await env.AI.run(&quot;@cf/microsoft/resnet-50&quot;, input);
    return Response.json(response);
  },
} satisfies ExportedHandler&lt;Env&gt;;</code></pre>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/microsoft/resnet-50&quot;, { image_classification: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/microsoft/resnet-50 -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>array</td><td>Required. An array of integers that represent the image data constrained to 8-bit unsigned integer values</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<p>No parameters.</p>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/resnet-50/schema-input.json)
- [Output schema](/workers-ai/models/resnet-50/schema-output.json)

