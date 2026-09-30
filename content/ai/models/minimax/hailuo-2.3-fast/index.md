<img src="/assets/upstream/images/workers-ai/minimax.svg" alt="Minimax logo" width="48" height="48">

<h1 id="minimax-hailuo-2-3-fast">MiniMax Hailuo 2.3 Fast</h1>

<p><code>minimax/hailuo-2.3-fast</code></p>

A lower-latency version of Hailuo 2.3 that preserves core motion quality, visual consistency, and stylization while enabling faster iteration.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://hailuoai.com/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.032, 6s @768p: 0.19, 10s @768p: 0.32, 6s @1080p: 0.33</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Animate a photo with default settings

<section class="model-example"><strong>Basic I2V</strong>
<p>Animate a photo with default settings</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Gentle movement and subtle animation, natural-looking motion&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: false,
    &quot;first_frame_image&quot;: &quot;https://replicate.delivery/xezq/MQpUhqkESIIQDlWUxtNcsznZLfUTmhEbCV3vdAZGHGPwwaMLA/tmpgl4gvv5n.jpeg&quot;,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;768P&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__hailuo-2.3-fast/basic-i2v.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;status&quot;: &quot;Success&quot;,
      &quot;task_id&quot;: &quot;388514752192863&quot;,
      &quot;video&quot;: &quot;https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/eff40703-0339-4d1d-b66a-db050e878038/output.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/hailuo-2.3-fast&#x27;,
  {
    prompt: &#x27;Gentle movement and subtle animation, natural-looking motion&#x27;,
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
  &quot;model&quot;: &quot;minimax/hailuo-2.3-fast&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Gentle movement and subtle animation, natural-looking motion&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: false,
    &quot;first_frame_image&quot;: &quot;https://replicate.delivery/xezq/MQpUhqkESIIQDlWUxtNcsznZLfUTmhEbCV3vdAZGHGPwwaMLA/tmpgl4gvv5n.jpeg&quot;,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;768P&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>High Resolution I2V</strong>
<p>Animate a photo in 1080P</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Camera slowly pans across the scene with cinematic depth of field&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: false,
    &quot;first_frame_image&quot;: &quot;https://replicate.delivery/xezq/IeNNble3XUqhpUZTd3CkYTUf8EgkFU1fl1Jnyive3B26MsGzC/tmp51dpln4i.jpeg&quot;,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;1080P&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__hailuo-2.3-fast/high-resolution-i2v.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;status&quot;: &quot;Success&quot;,
      &quot;task_id&quot;: &quot;388515984507205&quot;,
      &quot;video&quot;: &quot;https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/2b6251d2-d4ae-4d58-b12f-2609c50fadc2/output.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/hailuo-2.3-fast&#x27;,
  {
    prompt: &#x27;Camera slowly pans across the scene with cinematic depth of field&#x27;,
    duration: 6,
    fast_pretreatment: false,
    first_frame_image:
      &#x27;https://replicate.delivery/xezq/IeNNble3XUqhpUZTd3CkYTUf8EgkFU1fl1Jnyive3B26MsGzC/tmp51dpln4i.jpeg&#x27;,
    prompt_optimizer: true,
    resolution: &#x27;1080P&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/hailuo-2.3-fast&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Camera slowly pans across the scene with cinematic depth of field&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: false,
    &quot;first_frame_image&quot;: &quot;https://replicate.delivery/xezq/IeNNble3XUqhpUZTd3CkYTUf8EgkFU1fl1Jnyive3B26MsGzC/tmp51dpln4i.jpeg&quot;,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;1080P&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Fast Processing</strong>
<p>Quick I2V with fast pretreatment enabled</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Hair blowing in the wind, eyes blinking naturally&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: true,
    &quot;first_frame_image&quot;: &quot;https://replicate.delivery/xezq/jfh37lJpnDQhaKcAfCrxSCEh7HA7lv5cCWmJW284tYXwh1YWA/tmpw2i437qe.jpeg&quot;,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;768P&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__hailuo-2.3-fast/fast-processing.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;status&quot;: &quot;Success&quot;,
      &quot;task_id&quot;: &quot;388515980755024&quot;,
      &quot;video&quot;: &quot;https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/b64303a0-0227-4d42-983a-dcaec397b6b1/output.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/hailuo-2.3-fast&#x27;,
  {
    prompt: &#x27;Hair blowing in the wind, eyes blinking naturally&#x27;,
    duration: 6,
    fast_pretreatment: true,
    first_frame_image:
      &#x27;https://replicate.delivery/xezq/jfh37lJpnDQhaKcAfCrxSCEh7HA7lv5cCWmJW284tYXwh1YWA/tmpw2i437qe.jpeg&#x27;,
    prompt_optimizer: true,
    resolution: &#x27;768P&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/hailuo-2.3-fast&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Hair blowing in the wind, eyes blinking naturally&quot;,
    &quot;duration&quot;: 6,
    &quot;fast_pretreatment&quot;: true,
    &quot;first_frame_image&quot;: &quot;https://replicate.delivery/xezq/jfh37lJpnDQhaKcAfCrxSCEh7HA7lv5cCWmJW284tYXwh1YWA/tmpw2i437qe.jpeg&quot;,
    &quot;prompt_optimizer&quot;: true,
    &quot;resolution&quot;: &quot;768P&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>first_frame_image</code></td><td>string</td><td>Required. URL or base64 data URI of the first frame image</td></tr><tr><td><code>prompt</code></td><td>string</td><td></td></tr><tr><td><code>prompt_optimizer</code></td><td>boolean</td><td>Required. Default: True</td></tr><tr><td><code>fast_pretreatment</code></td><td>boolean</td><td>Required. Default: False</td></tr><tr><td><code>duration</code></td><td>number</td><td>Required. Default: 6</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Default: 768P; Values: 768P, 1080P</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td></td></tr><tr><td><code>task_id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>status</code></td><td>string</td><td>Values: Preparing, Queueing, Processing, Success, Fail</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/minimax/hailuo-2.3-fast/schema-input.json)
- [Output schema](/ai/models/minimax/hailuo-2.3-fast/schema-output.json)

