<img src="/assets/upstream/images/workers-ai/minimax.svg" alt="Minimax logo" width="48" height="48">

<h1 id="minimax-hailuo-2-3">MiniMax Hailuo 2.3</h1>

<p><code>minimax/hailuo-2.3</code></p>

A high-fidelity video generation model optimized for realistic human motion, cinematic VFX, expressive characters, and strong prompt and style adherence across text-to-video and image-to-video workflows.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://hailuoai.com/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.047, 6s @768p: 0.28, 10s @768p: 0.56, 6s @1080p: 0.49</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-video with default settings

<section class="model-example"><strong>Simple Video</strong>
<p>Basic text-to-video with default settings</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever playing fetch on a sandy beach at sunset&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: false,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;768P&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/hailuo-2.3/simple-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;status&quot;: &quot;Success&quot;,
      &quot;task_id&quot;: &quot;388507504709991&quot;,
      &quot;video&quot;: &quot;https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/97d0c2d0-45ab-4ce8-a1f4-177401f43073/output.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/hailuo-2.3&#x27;,
  {
    prompt: &#x27;A golden retriever playing fetch on a sandy beach at sunset&#x27;,
    duration: 6,
    fast_pretreatment: false,
    prompt_optimizer: true,
    resolution: &#x27;768P&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/hailuo-2.3&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever playing fetch on a sandy beach at sunset&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: false,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;768P&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>High Resolution</strong>
<p>1080P video for higher quality output</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A professional chef preparing sushi in a traditional Japanese kitchen, detailed close-up shots&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: false,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;1080P&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/hailuo-2.3/high-resolution.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;status&quot;: &quot;Success&quot;,
      &quot;task_id&quot;: &quot;388510158565457&quot;,
      &quot;video&quot;: &quot;https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/1ee6a770-eb88-4b6a-86ea-61981f01ed65/output.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/hailuo-2.3&#x27;,
  {
    prompt:
      &#x27;A professional chef preparing sushi in a traditional Japanese kitchen, detailed close-up shots&#x27;,
    duration: 6,
    fast_pretreatment: false,
    prompt_optimizer: true,
    resolution: &#x27;1080P&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/hailuo-2.3&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A professional chef preparing sushi in a traditional Japanese kitchen, detailed close-up shots&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: false,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;1080P&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Image to Video</strong>
<p>Animate a still image with I2V</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Slowly zoom in with subtle parallax movement, gentle atmospheric motion&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: false,
    &quot;first_frame_image&quot;: &quot;https://replicate.delivery/xezq/MQpUhqkESIIQDlWUxtNcsznZLfUTmhEbCV3vdAZGHGPwwaMLA/tmpgl4gvv5n.jpeg&quot;,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;768P&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/hailuo-2.3/image-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;status&quot;: &quot;Success&quot;,
      &quot;task_id&quot;: &quot;388509844320343&quot;,
      &quot;video&quot;: &quot;https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/a19c7850-6f3b-47dd-b6f1-decb592a11ff/output.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/hailuo-2.3&#x27;,
  {
    prompt: &#x27;Slowly zoom in with subtle parallax movement, gentle atmospheric motion&#x27;,
    duration: 6,
    fast_pretreatment: false,
    first_frame_image:
      &#x27;https://replicate.delivery/xezq/MQpUhqkESIIQDlWUxtNcsznZLfUTmhEbCV3vdAZGHGPwwaMLA/tmpgl4gvv5n.jpeg&#x27;,
    prompt_optimizer: true,
    resolution: &#x27;768P&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/hailuo-2.3&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Slowly zoom in with subtle parallax movement, gentle atmospheric motion&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: false,
    &quot;first_frame_image&quot;: &quot;https://replicate.delivery/xezq/MQpUhqkESIIQDlWUxtNcsznZLfUTmhEbCV3vdAZGHGPwwaMLA/tmpgl4gvv5n.jpeg&quot;,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;768P&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Fast Processing</strong>
<p>Enable fast pretreatment for quicker results</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Fireworks exploding over a city skyline at night, colorful reflections on water&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: true,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;768P&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/hailuo-2.3/fast-processing.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;status&quot;: &quot;Success&quot;,
      &quot;task_id&quot;: &quot;388509805367378&quot;,
      &quot;video&quot;: &quot;https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/438b5433-5d32-4760-9564-c86da3d22aee/output.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/hailuo-2.3&#x27;,
  {
    prompt: &#x27;Fireworks exploding over a city skyline at night, colorful reflections on water&#x27;,
    duration: 6,
    fast_pretreatment: true,
    prompt_optimizer: true,
    resolution: &#x27;768P&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/hailuo-2.3&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Fireworks exploding over a city skyline at night, colorful reflections on water&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: true,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;768P&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td></td></tr><tr><td><code>first_frame_image</code></td><td>string</td><td></td></tr><tr><td><code>prompt_optimizer</code></td><td>boolean</td><td>Required. Default: True</td></tr><tr><td><code>fast_pretreatment</code></td><td>boolean</td><td>Required. Default: False</td></tr><tr><td><code>duration</code></td><td>number</td><td>Required. Default: 6</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Default: 768P; Values: 768P, 1080P</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td></td></tr><tr><td><code>task_id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>status</code></td><td>string</td><td>Values: Preparing, Queueing, Processing, Success, Fail</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/minimax/hailuo-2.3/schema-input.json)
- [Output schema](/ai/models/minimax/hailuo-2.3/schema-output.json)

