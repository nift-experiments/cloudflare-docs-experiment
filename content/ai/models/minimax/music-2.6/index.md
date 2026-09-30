<img src="/assets/upstream/images/workers-ai/minimax.svg" alt="Minimax logo" width="48" height="48">

<h1 id="minimax-music-2-6">MiniMax Music 2.6</h1>

<p><code>minimax/music-2.6</code></p>

MiniMax's music generation model that creates full-length songs with vocals from text prompts and lyrics, or instrumental tracks. Supports BPM/key control and auto-generated lyrics.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Music Generation</td></tr>
<tr><th>Terms</th><td><a href="https://www.minimaxi.com/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per track: 0.15, Per lyrics generation: 0.01</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate music from a style description with auto-generated lyrics

<section class="model-example"><strong>Simple Prompt</strong>
<p>Generate music from a style description with auto-generated lyrics</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An upbeat electronic dance track with a catchy synth melody and driving beat&quot;,
    &quot;is_instrumental&quot;: false,
    &quot;lyrics_optimizer&quot;: true
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__music-2.6/simple-prompt.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://minimax-algeng-chat-tts-us.oss-us-east-1.aliyuncs.com/music%2Fprod%2Ftts-20260417092034-QxSPMzdbiRxBSbDb.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/music-2.6&#x27;,
  {
    prompt: &#x27;An upbeat electronic dance track with a catchy synth melody and driving beat&#x27;,
    is_instrumental: false,
    lyrics_optimizer: true,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/music-2.6&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An upbeat electronic dance track with a catchy synth melody and driving beat&quot;,
    &quot;is_instrumental&quot;: false,
    &quot;lyrics_optimizer&quot;: true
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>With Lyrics</strong>
<p>Generate a song with custom lyrics</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A warm acoustic folk ballad with fingerpicked guitar and gentle vocals&quot;,
    &quot;is_instrumental&quot;: false,
    &quot;lyrics&quot;: &quot;Walking down a dusty road\nWith the sunset painting gold\nEvery step a story told\nOf the places I call home&quot;,
    &quot;lyrics_optimizer&quot;: false
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__music-2.6/with-lyrics.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://minimax-algeng-chat-tts-us.oss-us-east-1.aliyuncs.com/music%2Fprod%2Ftts-20260417091919-YiIxwmvIqXtREDcu.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/music-2.6&#x27;,
  {
    prompt: &#x27;A warm acoustic folk ballad with fingerpicked guitar and gentle vocals&#x27;,
    is_instrumental: false,
    lyrics:
      &#x27;Walking down a dusty road\nWith the sunset painting gold\nEvery step a story told\nOf the places I call home&#x27;,
    lyrics_optimizer: false,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/music-2.6&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A warm acoustic folk ballad with fingerpicked guitar and gentle vocals&quot;,
    &quot;is_instrumental&quot;: false,
    &quot;lyrics&quot;: &quot;Walking down a dusty road\nWith the sunset painting gold\nEvery step a story told\nOf the places I call home&quot;,
    &quot;lyrics_optimizer&quot;: false
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Instrumental</strong>
<p>Generate instrumental music without vocals</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A calm lo-fi hip hop instrumental with vinyl crackle and mellow piano chords&quot;,
    &quot;is_instrumental&quot;: true,
    &quot;lyrics_optimizer&quot;: false
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__music-2.6/instrumental.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://minimax-algeng-chat-tts-us.oss-us-east-1.aliyuncs.com/music%2Fprod%2Ftts-20260417092057-LOwvBOOdyGvAyHkQ.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/music-2.6&#x27;,
  {
    prompt: &#x27;A calm lo-fi hip hop instrumental with vinyl crackle and mellow piano chords&#x27;,
    is_instrumental: true,
    lyrics_optimizer: false,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/music-2.6&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A calm lo-fi hip hop instrumental with vinyl crackle and mellow piano chords&quot;,
    &quot;is_instrumental&quot;: true,
    &quot;lyrics_optimizer&quot;: false
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>High Quality Audio</strong>
<p>Specify audio format and sample rate</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An orchestral cinematic score building to an epic crescendo with full symphony&quot;,
    &quot;format&quot;: &quot;wav&quot;,
    &quot;is_instrumental&quot;: false,
    &quot;lyrics_optimizer&quot;: true,
    &quot;sample_rate&quot;: 44100
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__music-2.6/high-quality-audio.wav&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://minimax-algeng-chat-tts-us.oss-us-east-1.aliyuncs.com/music%2Fprod%2Ftts-20260417092208-UGTfqDggHaemCDAW.wav&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/music-2.6&#x27;,
  {
    prompt: &#x27;An orchestral cinematic score building to an epic crescendo with full symphony&#x27;,
    format: &#x27;wav&#x27;,
    is_instrumental: false,
    lyrics_optimizer: true,
    sample_rate: 44100,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/music-2.6&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An orchestral cinematic score building to an epic crescendo with full symphony&quot;,
    &quot;format&quot;: &quot;wav&quot;,
    &quot;is_instrumental&quot;: false,
    &quot;lyrics_optimizer&quot;: true,
    &quot;sample_rate&quot;: 44100
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Auto-Generated Lyrics</strong>
<p>Let the model generate lyrics from the prompt</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cheerful pop song about a summer road trip with friends&quot;,
    &quot;is_instrumental&quot;: false,
    &quot;lyrics_optimizer&quot;: true
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__music-2.6/auto-generated-lyrics.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://minimax-algeng-chat-tts-us.oss-us-east-1.aliyuncs.com/music%2Fprod%2Ftts-20260417092245-UlqOBbhqSXtRPopt.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/music-2.6&#x27;,
  {
    prompt: &#x27;A cheerful pop song about a summer road trip with friends&#x27;,
    is_instrumental: false,
    lyrics_optimizer: true,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/music-2.6&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cheerful pop song about a summer road trip with friends&quot;,
    &quot;is_instrumental&quot;: false,
    &quot;lyrics_optimizer&quot;: true
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Description of the music style, mood, and scenario</td></tr><tr><td><code>lyrics</code></td><td>string</td><td>Song lyrics, using \n to separate lines Minimum length: 1</td></tr><tr><td><code>sample_rate</code></td><td>number</td><td>Audio sample rate</td></tr><tr><td><code>bitrate</code></td><td>number</td><td>Audio bitrate</td></tr><tr><td><code>format</code></td><td>string</td><td>Audio format Values: mp3, wav</td></tr><tr><td><code>lyrics_optimizer</code></td><td>boolean</td><td>Required. Automatically generate lyrics based on the prompt description Default: False</td></tr><tr><td><code>is_instrumental</code></td><td>boolean</td><td>Required. Generate instrumental music (no vocals) Default: False</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>string</td><td>Required. URL to the generated audio file</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/minimax/music-2.6/schema-input.json)
- [Output schema](/ai/models/minimax/music-2.6/schema-output.json)

