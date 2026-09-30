<img src="/assets/upstream/images/workers-ai/alibaba.svg" alt="Alibaba logo" width="48" height="48">

<h1 id="happyhorse-1-1-t2v">HappyHorse 1.1 T2V</h1>

<p><code>alibaba/hh1.1-t2v</code></p>

Alibaba's HappyHorse 1.1 text-to-video model. Generates videos from a text prompt with stronger dynamic expressiveness, better visual quality, and improved instruction following over 1.0. Configurable resolution, aspect ratio, and duration (3-15s).

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://www.alibabacloud.com/help/en/legal">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.18, @720p (per second): 0.14, @1080p (per second): 0.18</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate a short video from a text prompt

<section class="model-example"><strong>Simple Text-to-Video</strong>
<p>Generate a short video from a text prompt</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A little girl walking on the road&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/alibaba/hh1.1-t2v/simple-text-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/alibaba/hh1.1-t2v/simple-text-to-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/hh1.1-t2v&#x27;,
  { prompt: &#x27;A little girl walking on the road&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/hh1.1-t2v&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A little girl walking on the road&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Values: 720P, 1080P</td></tr><tr><td><code>ratio</code></td><td>string</td><td>Values: 16:9, 9:16, 1:1, 4:3, 3:4</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Minimum: 3; Maximum: 15</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Minimum: 0; Maximum: 2147483647</td></tr><tr><td><code>watermark</code></td><td>boolean</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/alibaba/hh1.1-t2v/schema-input.json)
- [Output schema](/ai/models/alibaba/hh1.1-t2v/schema-output.json)

