<img src="/assets/upstream/images/workers-ai/alibaba.svg" alt="Alibaba logo" width="48" height="48">

<h1 id="happyhorse-1-1-r2v">HappyHorse 1.1 R2V</h1>

<p><code>alibaba/hh1.1-r2v</code></p>

Alibaba's HappyHorse 1.1 reference-to-video model. Takes 1-9 reference images (characters and scenes) and a prompt that choreographs them into a single video, keeping each subject's identity consistent. Supports 720P and 1080P output with durations from 3 to 15 seconds.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Image-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://www.alibabacloud.com/help/en/legal">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.18, @720p (per second): 0.14, @1080p (per second): 0.18</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Compose three distinct references (person, scene, person) into one shot at 1080P

<section class="model-example"><strong>Multi-Image Reference</strong>
<p>Compose three distinct references (person, scene, person) into one shot at 1080P</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;The person in image 1 walks through the futuristic city in image 2 and meets the person in image 3.&quot;,
    &quot;images&quot;: [
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/portrait-photo-0.jpeg&quot;,
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-2/futuristic-city.png&quot;,
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-2/high-resolution-portrait.jpg&quot;
    ],
    &quot;duration&quot;: 8,
    &quot;ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;1080P&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/alibaba/hh1.1-r2v/multi-image-reference.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/alibaba/hh1.1-r2v/multi-image-reference.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/hh1.1-r2v&#x27;,
  {
    prompt:
      &#x27;The person in image 1 walks through the futuristic city in image 2 and meets the person in image 3.&#x27;,
    images: [
      &#x27;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/portrait-photo-0.jpeg&#x27;,
      &#x27;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-2/futuristic-city.png&#x27;,
      &#x27;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-2/high-resolution-portrait.jpg&#x27;,
    ],
    duration: 8,
    ratio: &#x27;16:9&#x27;,
    resolution: &#x27;1080P&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/hh1.1-r2v&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;The person in image 1 walks through the futuristic city in image 2 and meets the person in image 3.&quot;,
    &quot;images&quot;: [
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/portrait-photo-0.jpeg&quot;,
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-2/futuristic-city.png&quot;,
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-2/high-resolution-portrait.jpg&quot;
    ],
    &quot;duration&quot;: 8,
    &quot;ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;1080P&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>images</code></td><td>array</td><td>Required.</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Values: 720P, 1080P</td></tr><tr><td><code>ratio</code></td><td>string</td><td>Values: 16:9, 9:16, 3:4, 4:3, 1:1, 21:9, 9:21, 5:4, 4:5</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Minimum: 3; Maximum: 15</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Minimum: 0; Maximum: 2147483647</td></tr><tr><td><code>watermark</code></td><td>boolean</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/alibaba/hh1.1-r2v/schema-input.json)
- [Output schema](/ai/models/alibaba/hh1.1-r2v/schema-output.json)

