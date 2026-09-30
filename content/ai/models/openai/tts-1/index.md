<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="tts-1">TTS-1</h1>

<p><code>openai/tts-1</code></p>

OpenAI's text-to-speech model optimized for real-time use with low latency.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Speech</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per character: 1.5e-05</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate speech with default voice and settings

<section class="model-example"><strong>Simple Speech</strong>
<p>Generate speech with default voice and settings</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&quot;,
    &quot;voice&quot;: &quot;alloy&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/simple-speech.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/simple-speech.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/tts-1&#x27;,
  {
    response_format: &#x27;mp3&#x27;,
    speed: 1,
    text: &#x27;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&#x27;,
    voice: &#x27;alloy&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/tts-1&quot;,
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&quot;,
    &quot;voice&quot;: &quot;alloy&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Different Voice</strong>
<p>Use the Nova voice for a different tone</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;The weather today is sunny with a high of 72 degrees. Perfect for a walk in the park.&quot;,
    &quot;voice&quot;: &quot;nova&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/different-voice.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/different-voice.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/tts-1&#x27;,
  {
    response_format: &#x27;mp3&#x27;,
    speed: 1,
    text: &#x27;The weather today is sunny with a high of 72 degrees. Perfect for a walk in the park.&#x27;,
    voice: &#x27;nova&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/tts-1&quot;,
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;The weather today is sunny with a high of 72 degrees. Perfect for a walk in the park.&quot;,
    &quot;voice&quot;: &quot;nova&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Narration</strong>
<p>Slower narration style with the Onyx voice</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 0.85,
    &quot;text&quot;: &quot;In the beginning, the universe was a singularity of infinite density. Then, in a fraction of a second, it expanded into everything we know today.&quot;,
    &quot;voice&quot;: &quot;onyx&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/narration.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/narration.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/tts-1&#x27;,
  {
    response_format: &#x27;mp3&#x27;,
    speed: 0.85,
    text: &#x27;In the beginning, the universe was a singularity of infinite density. Then, in a fraction of a second, it expanded into everything we know today.&#x27;,
    voice: &#x27;onyx&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/tts-1&quot;,
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 0.85,
    &quot;text&quot;: &quot;In the beginning, the universe was a singularity of infinite density. Then, in a fraction of a second, it expanded into everything we know today.&quot;,
    &quot;voice&quot;: &quot;onyx&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Echo Voice</strong>
<p>Use the Echo voice for a deeper tone</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Welcome back to the podcast. Today we are going to talk about the future of artificial intelligence and its impact on creative work.&quot;,
    &quot;voice&quot;: &quot;echo&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/echo-voice.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/echo-voice.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/tts-1&#x27;,
  {
    response_format: &#x27;mp3&#x27;,
    speed: 1,
    text: &#x27;Welcome back to the podcast. Today we are going to talk about the future of artificial intelligence and its impact on creative work.&#x27;,
    voice: &#x27;echo&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/tts-1&quot;,
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Welcome back to the podcast. Today we are going to talk about the future of artificial intelligence and its impact on creative work.&quot;,
    &quot;voice&quot;: &quot;echo&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Fast Playback</strong>
<p>Speed up speech for quick listening</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1.5,
    &quot;text&quot;: &quot;This is a fast-paced summary of the key findings from the quarterly report. Revenue is up fifteen percent, user growth exceeded expectations, and infrastructure costs remain stable.&quot;,
    &quot;voice&quot;: &quot;shimmer&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/fast-playback.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/fast-playback.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/tts-1&#x27;,
  {
    response_format: &#x27;mp3&#x27;,
    speed: 1.5,
    text: &#x27;This is a fast-paced summary of the key findings from the quarterly report. Revenue is up fifteen percent, user growth exceeded expectations, and infrastructure costs remain stable.&#x27;,
    voice: &#x27;shimmer&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/tts-1&quot;,
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1.5,
    &quot;text&quot;: &quot;This is a fast-paced summary of the key findings from the quarterly report. Revenue is up fifteen percent, user growth exceeded expectations, and infrastructure costs remain stable.&quot;,
    &quot;voice&quot;: &quot;shimmer&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The text to generate audio for. Maximum length is 4096 characters.</td></tr><tr><td><code>voice</code></td><td>string</td><td>Required. The voice to use when generating the audio. Defaults to alloy. Default: alloy; Values: alloy, echo, fable, onyx, nova, shimmer</td></tr><tr><td><code>response_format</code></td><td>string</td><td>Required. The output format for the audio. Supported formats are mp3, opus, wav, aac and flac. Default: mp3; Values: mp3, opus, wav, aac, flac</td></tr><tr><td><code>speed</code></td><td>number</td><td>Required. The speed of the generated audio. Select a value from 0.25 to 4.0. 1.0 is the default. Default: 1; Minimum: 0.25; Maximum: 4</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>string</td><td>Required. URL to the generated audio file</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/openai/tts-1/schema-input.json)
- [Output schema](/ai/models/openai/tts-1/schema-output.json)

