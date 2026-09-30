<img src="/assets/upstream/images/workers-ai/vidu.svg" alt="Vidu logo" width="48" height="48">

<h1 id="vidu-q3-pro">Vidu Q3 Pro</h1>

<p><code>vidu/q3-pro</code></p>

Vidu Q3 Pro is a high-quality video generation model supporting text-to-video, image-to-video, and start/end-frame-to-video workflows with audio and up to 16-second clips.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://www.vidu.com/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.125, @540p (per second): 0.05, @720p (per second): 0.125, @1080p (per second): 0.15</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-video with just a prompt

<section class="model-example"><strong>Simple Text-to-Video</strong>
<p>Basic text-to-video with just a prompt</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever running through a sunlit meadow in slow motion&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/vidu__q3-pro/simple-text-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://video.cf.vidu.com/infer_64/tasks/26/0417/05/942597991691198464/creation-01/video.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;vidu/q3-pro&#x27;,
  {
    prompt: &#x27;A golden retriever running through a sunlit meadow in slow motion&#x27;,
    duration: 5,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;vidu/q3-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever running through a sunlit meadow in slow motion&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Portrait Aspect Ratio</strong>
<p>Vertical video for social media</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A busy street in Tokyo at night with neon signs reflecting on wet pavement, rain falling&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/vidu__q3-pro/portrait-aspect-ratio.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://video.cf.vidu.com/infer_88/tasks/26/0417/05/942598607041753088/creation-01/video.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;vidu/q3-pro&#x27;,
  {
    prompt:
      &#x27;A busy street in Tokyo at night with neon signs reflecting on wet pavement, rain falling&#x27;,
    aspect_ratio: &#x27;9:16&#x27;,
    duration: 5,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;vidu/q3-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A busy street in Tokyo at night with neon signs reflecting on wet pavement, rain falling&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Silent Video</strong>
<p>Generate video without audio</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;audio&quot;: false,
    &quot;prompt&quot;: &quot;Abstract paint swirls slowly mixing in water, vivid blues and golds&quot;,
    &quot;duration&quot;: 8,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/vidu__q3-pro/silent-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://video.cf.vidu.com/infer_76/tasks/26/0417/05/942599305355595776/creation-01/final_video.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;vidu/q3-pro&#x27;,
  {
    audio: false,
    prompt: &#x27;Abstract paint swirls slowly mixing in water, vivid blues and golds&#x27;,
    duration: 8,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;vidu/q3-pro&quot;,
  &quot;input&quot;: {
    &quot;audio&quot;: false,
    &quot;prompt&quot;: &quot;Abstract paint swirls slowly mixing in water, vivid blues and golds&quot;,
    &quot;duration&quot;: 8,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Square Format</strong>
<p>Square video for product demos or social posts</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sleek wireless headphone rotating on a pedestal with soft studio lighting and a white background&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/vidu__q3-pro/square-format.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://video.cf.vidu.com/infer_40/tasks/26/0417/05/942599364482723840/creation-01/video.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;vidu/q3-pro&#x27;,
  {
    prompt:
      &#x27;A sleek wireless headphone rotating on a pedestal with soft studio lighting and a white background&#x27;,
    aspect_ratio: &#x27;1:1&#x27;,
    duration: 5,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;vidu/q3-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sleek wireless headphone rotating on a pedestal with soft studio lighting and a white background&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Text prompt describing what should appear in the video</td></tr><tr><td><code>start_image</code></td><td>string</td><td>Start image for video generation. Use alone for image-to-video, or with end_image for start/end-to-video. Accepts public URL or Base64 data URI (data:image/png;base64,...)</td></tr><tr><td><code>end_image</code></td><td>string</td><td>End image for start/end-to-video generation. Must be used together with start_image. Accepts public URL or Base64 data URI (data:image/png;base64,...)</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Required. Video duration in seconds (1-16) Default: 5; Minimum: 1; Maximum: 16</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Video resolution Default: 720p; Values: 540p, 720p, 1080p</td></tr><tr><td><code>audio</code></td><td>boolean</td><td>Enable audio-video synchronization. Default: true for Q3 models. When false, outputs silent video</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Video aspect ratio (text-to-video only). Default: 16:9 Values: 16:9, 9:16, 3:4, 4:3, 1:1</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. URL to the generated video</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/vidu/q3-pro/schema-input.json)
- [Output schema](/ai/models/vidu/q3-pro/schema-output.json)

