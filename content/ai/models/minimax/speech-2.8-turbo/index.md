<img src="/assets/upstream/images/workers-ai/minimax.svg" alt="Minimax logo" width="48" height="48">

<h1 id="minimax-speech-2-8-turbo">MiniMax Speech 2.8 Turbo</h1>

<p><code>minimax/speech-2.8-turbo</code></p>

MiniMax Speech 2.8 Turbo turns text into natural, expressive speech with voice cloning, emotion control, and 40+ language support at faster speeds.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Speech</td></tr>
<tr><th>Terms</th><td><a href="https://www.minimaxi.com/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per character: 6e-05</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate speech with default settings

<section class="model-example"><strong>Simple Speech</strong>
<p>Generate speech with default settings</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-turbo/simple-speech.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-turbo/simple-speech.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/speech-2.8-turbo&#x27;,
  {
    format: &#x27;mp3&#x27;,
    pitch: 0,
    speed: 1,
    text: &#x27;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&#x27;,
    voice_id: &#x27;English_expressive_narrator&#x27;,
    volume: 1,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/speech-2.8-turbo&quot;,
  &quot;input&quot;: {
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Fast Narration</strong>
<p>Speed up narration for quick playback</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;speed&quot;: 1.5,
    &quot;text&quot;: &quot;This is a fast-paced summary of the key findings from the quarterly report. Revenue is up fifteen percent and user growth exceeded expectations.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-turbo/fast-narration.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-turbo/fast-narration.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/speech-2.8-turbo&#x27;,
  {
    format: &#x27;mp3&#x27;,
    pitch: 0,
    speed: 1.5,
    text: &#x27;This is a fast-paced summary of the key findings from the quarterly report. Revenue is up fifteen percent and user growth exceeded expectations.&#x27;,
    voice_id: &#x27;English_expressive_narrator&#x27;,
    volume: 1,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/speech-2.8-turbo&quot;,
  &quot;input&quot;: {
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;speed&quot;: 1.5,
    &quot;text&quot;: &quot;This is a fast-paced summary of the key findings from the quarterly report. Revenue is up fifteen percent and user growth exceeded expectations.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Calm Tone</strong>
<p>Calm and steady speech for meditation or relaxation</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;emotion&quot;: &quot;calm&quot;,
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;speed&quot;: 0.8,
    &quot;text&quot;: &quot;Take a deep breath in. Hold it for a moment. Now slowly exhale. Let your shoulders relax and release any tension.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-turbo/calm-tone.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-turbo/calm-tone.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/speech-2.8-turbo&#x27;,
  {
    emotion: &#x27;calm&#x27;,
    format: &#x27;mp3&#x27;,
    pitch: 0,
    speed: 0.8,
    text: &#x27;Take a deep breath in. Hold it for a moment. Now slowly exhale. Let your shoulders relax and release any tension.&#x27;,
    voice_id: &#x27;English_expressive_narrator&#x27;,
    volume: 1,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/speech-2.8-turbo&quot;,
  &quot;input&quot;: {
    &quot;emotion&quot;: &quot;calm&quot;,
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;speed&quot;: 0.8,
    &quot;text&quot;: &quot;Take a deep breath in. Hold it for a moment. Now slowly exhale. Let your shoulders relax and release any tension.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Adjusted Pitch</strong>
<p>Lower the pitch for a deeper voice</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: -6,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Good evening. Tonight we explore the mysteries of the deep ocean and the creatures that live in total darkness.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-turbo/adjusted-pitch.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-turbo/adjusted-pitch.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/speech-2.8-turbo&#x27;,
  {
    format: &#x27;mp3&#x27;,
    pitch: -6,
    speed: 1,
    text: &#x27;Good evening. Tonight we explore the mysteries of the deep ocean and the creatures that live in total darkness.&#x27;,
    voice_id: &#x27;English_expressive_narrator&#x27;,
    volume: 1,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/speech-2.8-turbo&quot;,
  &quot;input&quot;: {
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: -6,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Good evening. Tonight we explore the mysteries of the deep ocean and the creatures that live in total darkness.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The text to convert to speech. Maximum 10,000 characters.</td></tr><tr><td><code>voice_id</code></td><td>string</td><td>Required. The voice ID to use for synthesis Default: English_expressive_narrator</td></tr><tr><td><code>speed</code></td><td>number</td><td>Required. Speech speed (0.5 to 2) Default: 1; Minimum: 0.5; Maximum: 2</td></tr><tr><td><code>volume</code></td><td>number</td><td>Required. Speech volume (0 to 10) Default: 1; Minimum: 0; Maximum: 10</td></tr><tr><td><code>pitch</code></td><td>integer</td><td>Required. Pitch adjustment (-12 to 12) Default: 0; Minimum: -12; Maximum: 12</td></tr><tr><td><code>emotion</code></td><td>string</td><td>Emotion control for synthesized speech Values: happy, sad, angry, fearful, disgusted, surprised, calm, fluent</td></tr><tr><td><code>format</code></td><td>string</td><td>Required. Output audio format Default: mp3; Values: mp3, flac, wav</td></tr><tr><td><code>sample_rate</code></td><td>number</td><td>Audio sample rate</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>string</td><td>Required. URL to the generated audio file</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/minimax/speech-2.8-turbo/schema-input.json)
- [Output schema](/ai/models/minimax/speech-2.8-turbo/schema-output.json)

