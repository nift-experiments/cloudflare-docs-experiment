<img src="/assets/upstream/images/workers-ai/xai.svg" alt="Xai logo" width="48" height="48">

<h1 id="grok-imagine-video-1-5-preview">Grok Imagine Video 1.5 Preview</h1>

<p><code>xai/grok-imagine-video-1.5-preview</code></p>

xAI's next-generation video generation model. Generates, edits, and extends videos from text and image inputs. Supports multiple aspect ratios and resolutions with improved quality over the previous generation.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Image-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://x.ai/legal/terms-of-service">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.08, @480p (per second): 0.08, @720p (per second): 0.14</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Image to video

<section class="model-example"><strong>Image to video</strong>
<p>Image to video</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Generate a slow and serene time-lapse&quot;,
    &quot;image&quot;: {
      &quot;url&quot;: &quot;https://docs.x.ai/assets/api-examples/video/milkyway-still.png&quot;
    },
    &quot;duration&quot;: 12
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-video-1.5-preview/image-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-video-1.5-preview/image-to-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-imagine-video-1.5-preview&#x27;,
  {
    prompt: &#x27;Generate a slow and serene time-lapse&#x27;,
    image: { url: &#x27;https://docs.x.ai/assets/api-examples/video/milkyway-still.png&#x27; },
    duration: 12,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-imagine-video-1.5-preview&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Generate a slow and serene time-lapse&quot;,
    &quot;image&quot;: {
      &quot;url&quot;: &quot;https://docs.x.ai/assets/api-examples/video/milkyway-still.png&quot;
    },
    &quot;duration&quot;: 12
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>_operation</code></td><td>string</td><td>Values: generate, edit, extend</td></tr><tr><td><code>prompt</code></td><td>string</td><td></td></tr><tr><td><code>duration</code></td><td>integer</td><td>Minimum: 1; Maximum: 15</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Values: 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Values: 480p, 720p</td></tr><tr><td><code>size</code></td><td>string</td><td>Values: 848x480, 1696x960, 1280x720, 1920x1080</td></tr><tr><td><code>image</code></td><td>object</td><td></td></tr><tr><td><code>image.url</code></td><td>string</td><td>Required.</td></tr><tr><td><code>video</code></td><td>object</td><td></td></tr><tr><td><code>video.url</code></td><td>string</td><td>Required.</td></tr><tr><td><code>reference_images</code></td><td>array</td><td></td></tr><tr><td><code>reference_images[].url</code></td><td>string</td><td>Required.</td></tr><tr><td><code>output</code></td><td>object</td><td></td></tr><tr><td><code>output.upload_url</code></td><td>string</td><td>Required.</td></tr><tr><td><code>user</code></td><td>string</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/xai/grok-imagine-video-1.5-preview/schema-input.json)
- [Output schema](/ai/models/xai/grok-imagine-video-1.5-preview/schema-output.json)

