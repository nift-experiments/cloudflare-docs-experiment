<img src="/assets/upstream/images/workers-ai/bytedance.svg" alt="Bytedance logo" width="48" height="48">

<h1 id="seedance-2-0-fast">Seedance 2.0 Fast</h1>

<p><code>bytedance/seedance-2.0-fast</code></p>

Faster variant of ByteDance's Seedance 2.0 video model. Trades some quality for speed while sharing the same multimodal architecture. Supports text-to-video, image-to-video, native audio generation, multimodal references (images, videos, audio), video editing, and video extension.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.12, @480p video input (per second): 0.132, @720p video input (per second): 0.286, @480p non-video input (per second): 0.06, @720p non-video input (per second): 0.12</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Fast text-to-video with default settings

<section class="model-example"><strong>Quick Video</strong>
<p>Fast text-to-video with default settings</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever running through a field of sunflowers on a sunny day&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0-fast/quick-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0-fast/quick-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedance-2.0-fast&#x27;,
  {
    prompt: &#x27;A golden retriever running through a field of sunflowers on a sunny day&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: 5,
    resolution: &#x27;720p&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedance-2.0-fast&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever running through a field of sunflowers on a sunny day&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Portrait Video</strong>
<p>Vertical video for social media</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A barista pouring latte art in a cozy coffee shop, close-up with shallow depth of field&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0-fast/portrait-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0-fast/portrait-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedance-2.0-fast&#x27;,
  {
    prompt: &#x27;A barista pouring latte art in a cozy coffee shop, close-up with shallow depth of field&#x27;,
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
  &quot;model&quot;: &quot;bytedance/seedance-2.0-fast&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A barista pouring latte art in a cozy coffee shop, close-up with shallow depth of field&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Virtual Avatar Reference</strong>
<p>Use a virtual character avatar from the trusted asset library</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg&quot;,
    &quot;prompt&quot;: &quot;The scene gently animates with subtle motion&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;,
    &quot;use_virtual_avatar&quot;: true,
    &quot;generate_audio&quot;: false
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0-fast/virtual-avatar-reference.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/bytedance/seedance-2.0-fast/virtual-avatar-reference.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedance-2.0-fast&#x27;,
  {
    image: &#x27;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg&#x27;,
    prompt: &#x27;The scene gently animates with subtle motion&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    duration: 5,
    resolution: &#x27;720p&#x27;,
    use_virtual_avatar: true,
    generate_audio: false,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedance-2.0-fast&quot;,
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg&quot;,
    &quot;prompt&quot;: &quot;The scene gently animates with subtle motion&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;720p&quot;,
    &quot;use_virtual_avatar&quot;: true,
    &quot;generate_audio&quot;: false
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing the video to generate</td></tr><tr><td><code>image</code></td><td>string</td><td>Reference image (HTTP(S) URL or base64 data URI) for image-to-video</td></tr><tr><td><code>reference_video</code></td><td>string</td><td>Reference video (HTTP(S) URL or base64 data URI) for style/motion guidance</td></tr><tr><td><code>last_frame_image</code></td><td>string</td><td>Reference image (HTTP(S) URL or base64 data URI) for last-frame guidance. Only works if an image start frame is also given.</td></tr><tr><td><code>reference_images</code></td><td>array</td><td>Reference images (1-4, HTTP(S) URLs or base64 data URIs) to guide video generation for characters, avatars, clothing, or environments. Cannot be used with first/last frame images.</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Required. Video duration in seconds Default: 5; Minimum: 4; Maximum: 12</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Video resolution Default: 720p; Values: 480p, 720p</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Required. Video aspect ratio. Ignored if an image is used. Default: 16:9; Values: 16:9, 4:3, 1:1, 3:4, 9:16, 21:9, 9:21</td></tr><tr><td><code>fps</code></td><td>number</td><td>Required. Frame rate (frames per second) Default: 24</td></tr><tr><td><code>camera_fixed</code></td><td>boolean</td><td>Required. Whether to fix camera position Default: False</td></tr><tr><td><code>generate_audio</code></td><td>boolean</td><td>Whether to generate audio with the video</td></tr><tr><td><code>watermark</code></td><td>boolean</td><td>Required. Whether to add a watermark to the output video Default: False</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Random seed for reproducible generation Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>use_virtual_avatar</code></td><td>boolean</td><td>Required. Route image reference inputs (image, reference_images, last_frame_image) through ByteDance's trusted virtual avatar asset library before generation. Intended for AI-generated/virtual character avatars that would otherwise be blocked by face or deepfake detection Default: False</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. URL to the generated video</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/bytedance/seedance-2.0-fast/schema-input.json)
- [Output schema](/ai/models/bytedance/seedance-2.0-fast/schema-output.json)

