<img src="/assets/upstream/images/workers-ai/alibaba.svg" alt="Alibaba logo" width="48" height="48">

<h1 id="wan-3-0-video">Wan 3.0 Video</h1>

<p><code>alibaba/wan-3.0</code></p>

Alibaba's Wan 3.0 text-to-video model. Generates cinematic videos from text prompts with adaptive aspect ratio, 480P, 720P, or 1080P resolution, and configurable duration.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://www.alibabacloud.com/help/en/legal">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.05, @480p (per second): 0.05, @720p (per second): 0.1, @1080p (per second): 0.2</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate a 5-second 480P video with adaptive aspect ratio

<section class="model-example"><strong>Adaptive 480P Text-to-Video</strong>
<p>Generate a 5-second 480P video with adaptive aspect ratio</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A kitten running across a rooftop under the moonlight, city neon lights flickering in the distance, cinematic quality, smooth camera movement.&quot;,
    &quot;resolution&quot;: &quot;480P&quot;,
    &quot;ratio&quot;: &quot;adaptive&quot;,
    &quot;duration&quot;: 5
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/alibaba/wan-3.0/adaptive-480p-text-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/alibaba/wan-3.0/adaptive-480p-text-to-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/wan-3.0&#x27;,
  {
    prompt:
      &#x27;A kitten running across a rooftop under the moonlight, city neon lights flickering in the distance, cinematic quality, smooth camera movement.&#x27;,
    resolution: &#x27;480P&#x27;,
    ratio: &#x27;adaptive&#x27;,
    duration: 5,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/wan-3.0&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A kitten running across a rooftop under the moonlight, city neon lights flickering in the distance, cinematic quality, smooth camera movement.&quot;,
    &quot;resolution&quot;: &quot;480P&quot;,
    &quot;ratio&quot;: &quot;adaptive&quot;,
    &quot;duration&quot;: 5
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Values: 480P, 720P, 1080P</td></tr><tr><td><code>ratio</code></td><td>string</td><td>Values: adaptive, 16:9, 9:16, 1:1, 4:3, 3:4</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Minimum: 1; Maximum: 15</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/alibaba/wan-3.0/schema-input.json)
- [Output schema](/ai/models/alibaba/wan-3.0/schema-output.json)

