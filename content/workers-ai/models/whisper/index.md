<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="whisper">whisper</h1>

<p><code>@cf/openai/whisper</code></p>

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Automatic Speech Recognition</td></tr>
<tr><th>More information</th><td><a href="https://openai.com/research/whisper">Model details</a></td></tr>
<tr><th>Unit pricing</th><td>USD 0.000453 per audio minute</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">export default {
  async fetch(request, env) {
    const input = await request.json();
    const response = await env.AI.run(&quot;@cf/openai/whisper&quot;, input);
    return Response.json(response);
  },
} satisfies ExportedHandler&lt;Env&gt;;</code></pre>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/openai/whisper&quot;, { automatic_speech_recognition: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/openai/whisper -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>array</td><td>Required. An array of integers that represent the audio data constrained to 8-bit unsigned integer values</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The transcription</td></tr><tr><td><code>word_count</code></td><td>number</td><td></td></tr><tr><td><code>words</code></td><td>array</td><td></td></tr><tr><td><code>words[].word</code></td><td>string</td><td></td></tr><tr><td><code>words[].start</code></td><td>number</td><td>The second this word begins in the recording</td></tr><tr><td><code>words[].end</code></td><td>number</td><td>The ending second when the word completes</td></tr><tr><td><code>vtt</code></td><td>string</td><td></td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/whisper/schema-input.json)
- [Output schema](/workers-ai/models/whisper/schema-output.json)

