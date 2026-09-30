<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="gemini-omni-flash">Gemini Omni Flash</h1>

<p><code>google/gemini-omni-flash</code></p>

Preview high-performance multimodal video generation and editing model with conversational controls and generated audio.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input text tokens (per 1M): 1.5, Input image tokens (per 1M): 1.5, Input audio tokens (per 1M): 1.5, Input video tokens (per 1M): 1.5, output_text_tokens: 9, Reasoning tokens (per 1M): 9, output_video_tokens: 17.5, Default (per second): 1.5</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate an underwater landscape video

<section class="model-example"><strong>Underwater reef</strong>
<p>Generate an underwater landscape video</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;A school of silver fish moving through a sunlit coral reef, slow cinematic tracking shot with drifting particles.&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/google/gemini-omni-flash/underwater-reef.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/google/gemini-omni-flash/underwater-reef.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-omni-flash&#x27;,
  {
    text: &#x27;A school of silver fish moving through a sunlit coral reef, slow cinematic tracking shot with drifting particles.&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-omni-flash&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;A school of silver fish moving through a sunlit coral reef, slow cinematic tracking shot with drifting particles.&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Breakfast robot</strong>
<p>Generate a portrait-format character scene</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;A friendly home robot preparing breakfast in a bright modern kitchen, gentle handheld camera movement.&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/google/gemini-omni-flash/breakfast-robot.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/google/gemini-omni-flash/breakfast-robot.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-omni-flash&#x27;,
  {
    text: &#x27;A friendly home robot preparing breakfast in a bright modern kitchen, gentle handheld camera movement.&#x27;,
    aspect_ratio: &#x27;9:16&#x27;,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-omni-flash&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;A friendly home robot preparing breakfast in a bright modern kitchen, gentle handheld camera movement.&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Desert train</strong>
<p>Generate a high-resolution desert scene</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;A vintage train crossing a vast desert at golden hour, dust glowing in the sunset as the camera sweeps alongside.&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;1080p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/google/gemini-omni-flash/desert-train.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/google/gemini-omni-flash/desert-train.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-omni-flash&#x27;,
  {
    text: &#x27;A vintage train crossing a vast desert at golden hour, dust glowing in the sunset as the camera sweeps alongside.&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    resolution: &#x27;1080p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-omni-flash&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;A vintage train crossing a vast desert at golden hour, dust glowing in the sunset as the camera sweeps alongside.&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;1080p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Northern lights</strong>
<p>Generate a low-resolution night landscape</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Colorful northern lights dancing above a frozen lake, a small cabin glowing warmly in the foreground.&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;360p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/google/gemini-omni-flash/northern-lights.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/google/gemini-omni-flash/northern-lights.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-omni-flash&#x27;,
  {
    text: &#x27;Colorful northern lights dancing above a frozen lake, a small cabin glowing warmly in the foreground.&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    resolution: &#x27;360p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-omni-flash&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Colorful northern lights dancing above a frozen lake, a small cabin glowing warmly in the foreground.&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;360p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Text prompt or editing instruction</td></tr><tr><td><code>image</code></td><td>string</td><td>First-frame or primary reference image</td></tr><tr><td><code>last_frame</code></td><td>string</td><td>Last-frame reference image</td></tr><tr><td><code>reference_images</code></td><td>array</td><td></td></tr><tr><td><code>video</code></td><td>string</td><td>Reference video for editing or extension</td></tr><tr><td><code>audio</code></td><td>string</td><td>Reference audio input</td></tr><tr><td><code>previous_interaction_id</code></td><td>string</td><td></td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Values: 16:9, 9:16</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Values: 360p, 720p, 1080p, 4k</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/google/gemini-omni-flash/schema-input.json)
- [Output schema](/ai/models/google/gemini-omni-flash/schema-output.json)

