<img src="/assets/upstream/images/workers-ai/elevenlabs.svg" alt="Elevenlabs logo" width="48" height="48">

<h1 id="eleven-multilingual-v2">Eleven Multilingual v2</h1>

<p><code>elevenlabs/eleven-multilingual-v2</code></p>

ElevenLabs' multilingual text-to-speech model for generating natural speech across many languages with ElevenLabs voices.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Speech</td></tr>
<tr><th>Terms</th><td><a href="https://elevenlabs.io/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per character: 0.0001, Default (per second): 0.0001</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate multilingual speech about Cloudflare AI Gateway

<section class="model-example"><strong>French AI Gateway Speech</strong>
<p>Generate multilingual speech about Cloudflare AI Gateway</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Bonjour et bienvenue dans Cloudflare AI Gateway. Suivez vos requetes, vos couts et les performances de vos modeles depuis une seule interface.&quot;,
    &quot;voice_id&quot;: &quot;JBFqnCBsd6RMkjVDRZzb&quot;,
    &quot;language_code&quot;: &quot;fr&quot;,
    &quot;output_format&quot;: &quot;mp3_44100_128&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/elevenlabs/eleven-multilingual-v2/french-ai-gateway-speech.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/elevenlabs/eleven-multilingual-v2/french-ai-gateway-speech.mp3&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;elevenlabs/eleven-multilingual-v2&#x27;,
  {
    text: &#x27;Bonjour et bienvenue dans Cloudflare AI Gateway. Suivez vos requetes, vos couts et les performances de vos modeles depuis une seule interface.&#x27;,
    voice_id: &#x27;JBFqnCBsd6RMkjVDRZzb&#x27;,
    language_code: &#x27;fr&#x27;,
    output_format: &#x27;mp3_44100_128&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;elevenlabs/eleven-multilingual-v2&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Bonjour et bienvenue dans Cloudflare AI Gateway. Suivez vos requetes, vos couts et les performances de vos modeles depuis une seule interface.&quot;,
    &quot;voice_id&quot;: &quot;JBFqnCBsd6RMkjVDRZzb&quot;,
    &quot;language_code&quot;: &quot;fr&quot;,
    &quot;output_format&quot;: &quot;mp3_44100_128&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The text to convert into speech. Minimum length: 1</td></tr><tr><td><code>voice_id</code></td><td>string</td><td>Required. The ElevenLabs voice ID to use for generation. Minimum length: 1</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Values: mp3_22050_32, mp3_24000_48, mp3_44100_128, mp3_44100_192, mp3_44100_32, mp3_44100_64, mp3_44100_96, opus_48000_128, opus_48000_192, opus_48000_32, opus_48000_64, opus_48000_96</td></tr><tr><td><code>language_code</code></td><td>string</td><td>ISO 639-1 language code to enforce.</td></tr><tr><td><code>voice_settings</code></td><td>object</td><td></td></tr><tr><td><code>voice_settings.stability</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>voice_settings.similarity_boost</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>voice_settings.style</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>voice_settings.use_speaker_boost</code></td><td>boolean</td><td></td></tr><tr><td><code>voice_settings.speed</code></td><td>number</td><td>Minimum: 0.7; Maximum: 1.2</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Minimum: 0; Maximum: 4294967295</td></tr><tr><td><code>previous_text</code></td><td>string</td><td></td></tr><tr><td><code>next_text</code></td><td>string</td><td></td></tr><tr><td><code>apply_text_normalization</code></td><td>string</td><td>Values: auto, on, off</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>string</td><td>Required. URL to the generated audio file.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/elevenlabs/eleven-multilingual-v2/schema-input.json)
- [Output schema](/ai/models/elevenlabs/eleven-multilingual-v2/schema-output.json)

