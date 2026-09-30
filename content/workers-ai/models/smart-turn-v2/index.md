<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="smart-turn-v2">smart-turn-v2</h1>

<p><code>@cf/pipecat-ai/smart-turn-v2</code></p>

An open source, community-driven, native audio turn detection model in 2nd version

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Dumb Pipe</td></tr>
<tr><th>Asynchronous queue</th><td>Yes</td></tr>
<tr><th>Unit pricing</th><td>USD 0.000338 per audio minute</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">export default {
  async fetch(request, env) {
    const input = await request.json();
    const response = await env.AI.run(&quot;@cf/pipecat-ai/smart-turn-v2&quot;, input);
    return Response.json(response);
  },
} satisfies ExportedHandler&lt;Env&gt;;</code></pre>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/pipecat-ai/smart-turn-v2&quot;, { dumb_pipe: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/pipecat-ai/smart-turn-v2 -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>object</td><td>Required. readable stream with audio data and content-type specified for that data</td></tr><tr><td><code>audio.body</code></td><td>object</td><td>Required.</td></tr><tr><td><code>audio.contentType</code></td><td>string</td><td>Required.</td></tr><tr><td><code>dtype</code></td><td>string</td><td>type of data PCM data that's sent to the inference server as raw array Values: uint8, float32, float64</td></tr><tr><td><code>audio</code></td><td>string</td><td>Required. base64 encoded audio data</td></tr><tr><td><code>dtype</code></td><td>string</td><td>type of data PCM data that's sent to the inference server as raw array Values: uint8, float32, float64</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>is_complete</code></td><td>boolean</td><td>if true, end-of-turn was detected</td></tr><tr><td><code>probability</code></td><td>number</td><td>probability of the end-of-turn detection</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/smart-turn-v2/schema-input.json)
- [Output schema](/workers-ai/models/smart-turn-v2/schema-output.json)

