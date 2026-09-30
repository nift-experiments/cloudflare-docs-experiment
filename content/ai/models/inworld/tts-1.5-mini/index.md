<img src="/assets/upstream/images/workers-ai/inworld.svg" alt="Inworld logo" width="48" height="48">

<h1 id="inworld-tts-1-5-mini">Inworld TTS 1.5 Mini</h1>

<p><code>inworld/tts-1.5-mini</code></p>

Ultra-fast, cost-efficient text-to-speech with approximately 120ms latency and 15-language support.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Speech</td></tr>
<tr><th>Terms</th><td><a href="https://inworld.ai/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per character: 1.5e-05</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate speech with default settings

<section class="model-example"><strong>Simple Speech</strong>
<p>Generate speech with default settings</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-mini/simple-speech.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-mini/simple-speech.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;inworld/tts-1.5-mini&#x27;,
  {
    output_format: &#x27;mp3&#x27;,
    temperature: 1,
    text: &#x27;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&#x27;,
    timestamp_type: &#x27;none&#x27;,
    voice_id: &#x27;Dennis&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;inworld/tts-1.5-mini&quot;,
  &quot;input&quot;: {
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Fast Speech</strong>
<p>Speed up speech for quick playback</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;speaking_rate&quot;: 1.4,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;This is a fast-paced summary of the key findings from the quarterly report. Revenue is up fifteen percent and user growth exceeded expectations.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-mini/fast-speech.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-mini/fast-speech.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;inworld/tts-1.5-mini&#x27;,
  {
    output_format: &#x27;mp3&#x27;,
    speaking_rate: 1.4,
    temperature: 1,
    text: &#x27;This is a fast-paced summary of the key findings from the quarterly report. Revenue is up fifteen percent and user growth exceeded expectations.&#x27;,
    timestamp_type: &#x27;none&#x27;,
    voice_id: &#x27;Dennis&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;inworld/tts-1.5-mini&quot;,
  &quot;input&quot;: {
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;speaking_rate&quot;: 1.4,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;This is a fast-paced summary of the key findings from the quarterly report. Revenue is up fifteen percent and user growth exceeded expectations.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Low Latency</strong>
<p>Minimize latency by disabling text normalization</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;apply_text_normalization&quot;: false,
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;Quick response needed. The server is ready.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-mini/low-latency.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-mini/low-latency.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;inworld/tts-1.5-mini&#x27;,
  {
    apply_text_normalization: false,
    output_format: &#x27;mp3&#x27;,
    temperature: 1,
    text: &#x27;Quick response needed. The server is ready.&#x27;,
    timestamp_type: &#x27;none&#x27;,
    voice_id: &#x27;Dennis&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;inworld/tts-1.5-mini&quot;,
  &quot;input&quot;: {
    &quot;apply_text_normalization&quot;: false,
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;Quick response needed. The server is ready.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The text to be synthesized into speech. Maximum input of 2,000 characters.</td></tr><tr><td><code>voice_id</code></td><td>string</td><td>Required. The ID of the voice to use for synthesizing speech. Defaults to Dennis. Default: Dennis; Values: Loretta, Darlene, Marlene, Hank, Evelyn, Celeste, Pippa, Tessa, Liam, Callum, Hamish, Abby, Graham, Rupert, Mortimer, Snik, Anjali, Saanvi, Arjun, Claire, Oliver, Simon, Elliot, James, Serena, Gareth, Vinny, Lauren, Jessica, Ethan, Tyler, Jason, Chloe, Veronica, Victoria, Miranda, Sebastian, Victor, Malcolm, Nate, Brian, Amina, Kelsey, Derek, Evan, Kayla, Jake, Grant, Tristan, Nadia, Selene, Marcus, Riley, Damon, Cedric, Mia, Naomi, Jonah, Levi, Avery, Brandon, Conrad, Bianca, Lucian, Trevor, Alex, Ashley, Craig, Deborah, Dennis, Edward, Elizabeth, Hades, Julia, Pixie, Mark, Olivia, Priya, Ronald, Sarah, Shaun, Theodore, Timothy, Wendy, Dominus, Hana, Clive, Carter, Blake, Luna, Reed, Duncan, Felix, Eleanor, Sophie</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Required. The output format for the audio. Supported formats are mp3, opus, wav, and flac. Defaults to mp3. Default: mp3; Values: mp3, opus, wav, flac</td></tr><tr><td><code>bit_rate</code></td><td>integer</td><td>Bits per second of the audio. Only for compressed audio formats (mp3, opus). The default is 128,000. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>sample_rate</code></td><td>integer</td><td>The synthesis sample rate in hertz. Accepts: 8000, 16000, 22050, 24000, 32000, 44100, 48000. The default is 48,000. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>speaking_rate</code></td><td>number</td><td>Speaking rate/speed, in the range [0.5, 1.5]. The default is 1.0. We recommend using values above 0.8 to ensure high quality. Minimum: 0.5; Maximum: 1.5</td></tr><tr><td><code>temperature</code></td><td>number</td><td>Required. Determines the degree of randomness when sampling audio tokens. Defaults to 1.0. Accepts values between 0 (exclusive) and 2 (inclusive). Higher values = more expressive, lower values = more deterministic. Default: 1; Minimum: 0.01; Maximum: 2</td></tr><tr><td><code>timestamp_type</code></td><td>string</td><td>Required. Controls timestamp metadata returned with the audio. "word" returns word-level timing, "character" returns character-level timing. Note: adds latency. Defaults to none. Default: none; Values: none, word, character</td></tr><tr><td><code>apply_text_normalization</code></td><td>boolean</td><td>When enabled, text normalization expands numbers, dates, times, and abbreviations before converting to speech. Turning this off may reduce latency.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>string</td><td>Required. URL to the generated audio file</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/inworld/tts-1.5-mini/schema-input.json)
- [Output schema](/ai/models/inworld/tts-1.5-mini/schema-output.json)

