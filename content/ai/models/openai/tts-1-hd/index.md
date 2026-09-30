<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="tts-1-hd">TTS-1 HD</h1>

<p><code>openai/tts-1-hd</code></p>

OpenAI's high-definition text-to-speech model producing higher quality audio output.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Speech</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per character: 3e-05</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate high-definition speech with default settings

<section class="model-example"><strong>Simple Speech</strong>
<p>Generate high-definition speech with default settings</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&quot;,
    &quot;voice&quot;: &quot;alloy&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1-hd/simple-speech.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1-hd/simple-speech.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/tts-1-hd&#x27;,
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
  &quot;model&quot;: &quot;openai/tts-1-hd&quot;,
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&quot;,
    &quot;voice&quot;: &quot;alloy&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Storytelling</strong>
<p>HD narration with the Fable voice</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 0.9,
    &quot;text&quot;: &quot;Once upon a time, in a kingdom beyond the clouds, there lived a young inventor who dreamed of building machines that could think.&quot;,
    &quot;voice&quot;: &quot;fable&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1-hd/storytelling.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1-hd/storytelling.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/tts-1-hd&#x27;,
  {
    response_format: &#x27;mp3&#x27;,
    speed: 0.9,
    text: &#x27;Once upon a time, in a kingdom beyond the clouds, there lived a young inventor who dreamed of building machines that could think.&#x27;,
    voice: &#x27;fable&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/tts-1-hd&quot;,
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 0.9,
    &quot;text&quot;: &quot;Once upon a time, in a kingdom beyond the clouds, there lived a young inventor who dreamed of building machines that could think.&quot;,
    &quot;voice&quot;: &quot;fable&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Podcast Style</strong>
<p>Conversational podcast narration</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;So here&#x27;s the thing about large language models \u2014 they&#x27;re not actually thinking. They&#x27;re predicting the next token based on patterns in their training data. But the results can be surprisingly coherent.&quot;,
    &quot;voice&quot;: &quot;echo&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1-hd/podcast-style.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1-hd/podcast-style.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/tts-1-hd&#x27;,
  {
    response_format: &#x27;mp3&#x27;,
    speed: 1,
    text: &quot;So here&#x27;s the thing about large language models — they&#x27;re not actually thinking. They&#x27;re predicting the next token based on patterns in their training data. But the results can be surprisingly coherent.&quot;,
    voice: &#x27;echo&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/tts-1-hd&quot;,
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;So here&#x27;\&#x27;&#x27;s the thing about large language models — they&#x27;\&#x27;&#x27;re not actually thinking. They&#x27;\&#x27;&#x27;re predicting the next token based on patterns in their training data. But the results can be surprisingly coherent.&quot;,
    &quot;voice&quot;: &quot;echo&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Shimmer Voice</strong>
<p>Bright and expressive voice</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Breaking news: scientists have discovered a new species of deep-sea fish that produces its own light using bioluminescence.&quot;,
    &quot;voice&quot;: &quot;shimmer&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1-hd/shimmer-voice.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1-hd/shimmer-voice.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/tts-1-hd&#x27;,
  {
    response_format: &#x27;mp3&#x27;,
    speed: 1,
    text: &#x27;Breaking news: scientists have discovered a new species of deep-sea fish that produces its own light using bioluminescence.&#x27;,
    voice: &#x27;shimmer&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/tts-1-hd&quot;,
  &quot;input&quot;: {
    &quot;response_format&quot;: &quot;mp3&quot;,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Breaking news: scientists have discovered a new species of deep-sea fish that produces its own light using bioluminescence.&quot;,
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

- [Input schema](/ai/models/openai/tts-1-hd/schema-input.json)
- [Output schema](/ai/models/openai/tts-1-hd/schema-output.json)

