<img src="/assets/upstream/images/workers-ai/vidu.svg" alt="Vidu logo" width="48" height="48">

<h1 id="vidu-q3-turbo">Vidu Q3 Turbo</h1>

<p><code>vidu/q3-turbo</code></p>

Vidu Q3 Turbo is a faster version of Vidu Q3 optimized for lower latency video generation while maintaining audio support and up to 16-second clips.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://www.vidu.com/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.06, @540p (per second): 0.04, @720p (per second): 0.06, @1080p (per second): 0.07</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-video with just a prompt

<section class="model-example"><strong>Simple Text-to-Video</strong>
<p>Basic text-to-video with just a prompt</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cat lazily stretching on a sunlit windowsill&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/vidu/q3-turbo/simple-text-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://video.cf.vidu.com/infer_28/tasks/26/0417/05/942602832110972928/creation-01/video.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;vidu/q3-turbo&#x27;,
  { prompt: &#x27;A cat lazily stretching on a sunlit windowsill&#x27;, duration: 5, resolution: &#x27;720p&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;vidu/q3-turbo&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cat lazily stretching on a sunlit windowsill&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>High Resolution</strong>
<p>Generate at 1080p</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Close-up of a hummingbird feeding from a vibrant red flower, slow motion with soft bokeh background&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;1080p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/vidu/q3-turbo/high-resolution.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://video.cf.vidu.com/infer_44/tasks/26/0417/05/942602894400569344/creation-01/video.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;vidu/q3-turbo&#x27;,
  {
    prompt:
      &#x27;Close-up of a hummingbird feeding from a vibrant red flower, slow motion with soft bokeh background&#x27;,
    duration: 5,
    resolution: &#x27;1080p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;vidu/q3-turbo&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Close-up of a hummingbird feeding from a vibrant red flower, slow motion with soft bokeh background&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;1080p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Portrait Video</strong>
<p>Vertical video for mobile viewing</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A waterfall cascading down mossy rocks in a tropical jungle, mist rising&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/vidu/q3-turbo/portrait-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://video.cf.vidu.com/infer_48/tasks/26/0417/05/942603057143758848/creation-01/video.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;vidu/q3-turbo&#x27;,
  {
    prompt: &#x27;A waterfall cascading down mossy rocks in a tropical jungle, mist rising&#x27;,
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
  &quot;model&quot;: &quot;vidu/q3-turbo&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A waterfall cascading down mossy rocks in a tropical jungle, mist rising&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Extended Duration</strong>
<p>Longer video clip</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Timelapse of clouds rolling over a mountain peak from sunrise to sunset, dramatic lighting&quot;,
    &quot;duration&quot;: 16,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/vidu/q3-turbo/extended-duration.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://video.cf.vidu.com/infer_84/tasks/26/0417/06/942603162785705984/creation-01/video.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;vidu/q3-turbo&#x27;,
  {
    prompt:
      &#x27;Timelapse of clouds rolling over a mountain peak from sunrise to sunset, dramatic lighting&#x27;,
    duration: 16,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;vidu/q3-turbo&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Timelapse of clouds rolling over a mountain peak from sunrise to sunset, dramatic lighting&quot;,
    &quot;duration&quot;: 16,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Low Resolution Fast Preview</strong>
<p>Quick preview at 540p</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sailboat gliding across calm ocean waters at sunset&quot;,
    &quot;duration&quot;: 3,
    &quot;resolution&quot;: &quot;540p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/vidu/q3-turbo/low-resolution-fast-preview.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://video.cf.vidu.com/infer_68/tasks/26/0417/06/942603796612128768/creation-01/video.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;vidu/q3-turbo&#x27;,
  {
    prompt: &#x27;A sailboat gliding across calm ocean waters at sunset&#x27;,
    duration: 3,
    resolution: &#x27;540p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;vidu/q3-turbo&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sailboat gliding across calm ocean waters at sunset&quot;,
    &quot;duration&quot;: 3,
    &quot;resolution&quot;: &quot;540p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Text prompt describing what should appear in the video</td></tr><tr><td><code>start_image</code></td><td>string</td><td>Start image for video generation. Use alone for image-to-video, or with end_image for start/end-to-video. Accepts public URL or Base64 data URI (data:image/png;base64,...)</td></tr><tr><td><code>end_image</code></td><td>string</td><td>End image for start/end-to-video generation. Must be used together with start_image. Accepts public URL or Base64 data URI (data:image/png;base64,...)</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Required. Video duration in seconds (1-16) Default: 5; Minimum: 1; Maximum: 16</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Video resolution Default: 720p; Values: 540p, 720p, 1080p</td></tr><tr><td><code>audio</code></td><td>boolean</td><td>Enable audio-video synchronization. Default: true for Q3 models. When false, outputs silent video</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Video aspect ratio (text-to-video only). Default: 16:9 Values: 16:9, 9:16, 3:4, 4:3, 1:1</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. URL to the generated video</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/vidu/q3-turbo/schema-input.json)
- [Output schema](/ai/models/vidu/q3-turbo/schema-output.json)

