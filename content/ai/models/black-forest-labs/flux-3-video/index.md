<img src="/assets/upstream/images/workers-ai/black-forest-labs.svg" alt="Black-Forest-Labs logo" width="48" height="48">

<h1 id="flux-3-video">FLUX 3 Video</h1>

<p><code>black-forest-labs/flux-3-video</code></p>

FLUX 3 Video is Black Forest Labs' video generation model. It generates video from a text prompt (t2v), animates one or more reference images (i2v), or continues an existing clip (v2v), with synchronized audio, up to fhd resolution, and 5-20 second durations.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://blackforestlabs.ai/terms-of-service/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>hd: 0.17, fhd: 0.29, v2v_hd: 0.41, v2v_fhd: 0.53, hd_draft: 0.06, v2v_hd_draft: 0.12</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate a video from a text prompt alone (t2v), with synchronized ambient audio.

<section class="model-example"><strong>Text to Video</strong>
<p>Generate a video from a text prompt alone (t2v), with synchronized ambient audio.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;mode&quot;: &quot;t2v&quot;,
    &quot;prompt&quot;: &quot;A cozy ramen shop on a rainy Tokyo night, steam rising from the broth. Rain patter and quiet kitchen sounds.&quot;,
    &quot;resolution&quot;: &quot;hd&quot;,
    &quot;duration&quot;: 5,
    &quot;generate_audio&quot;: true
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-3-video/text-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-3-video/text-to-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-3-video&#x27;,
  {
    mode: &#x27;t2v&#x27;,
    prompt:
      &#x27;A cozy ramen shop on a rainy Tokyo night, steam rising from the broth. Rain patter and quiet kitchen sounds.&#x27;,
    resolution: &#x27;hd&#x27;,
    duration: 5,
    generate_audio: true,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-3-video&quot;,
  &quot;input&quot;: {
    &quot;mode&quot;: &quot;t2v&quot;,
    &quot;prompt&quot;: &quot;A cozy ramen shop on a rainy Tokyo night, steam rising from the broth. Rain patter and quiet kitchen sounds.&quot;,
    &quot;resolution&quot;: &quot;hd&quot;,
    &quot;duration&quot;: 5,
    &quot;generate_audio&quot;: true
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>mode</code></td><td>string</td><td></td></tr><tr><td><code>prompt</code></td><td>string</td><td></td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td></td></tr><tr><td><code>duration</code></td><td>integer or string</td><td></td></tr><tr><td><code>resolution</code></td><td>string</td><td></td></tr><tr><td><code>generate_audio</code></td><td>boolean</td><td></td></tr><tr><td><code>safety_tolerance</code></td><td>integer</td><td></td></tr><tr><td><code>draft</code></td><td>boolean</td><td></td></tr><tr><td><code>mode</code></td><td>string</td><td></td></tr><tr><td><code>prompt</code></td><td>string</td><td></td></tr><tr><td><code>keyframes</code></td><td>string or array</td><td></td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td></td></tr><tr><td><code>duration</code></td><td>integer or string</td><td></td></tr><tr><td><code>resolution</code></td><td>string</td><td></td></tr><tr><td><code>generate_audio</code></td><td>boolean</td><td></td></tr><tr><td><code>safety_tolerance</code></td><td>integer</td><td></td></tr><tr><td><code>draft</code></td><td>boolean</td><td></td></tr><tr><td><code>mode</code></td><td>string</td><td></td></tr><tr><td><code>prompt</code></td><td>string</td><td></td></tr><tr><td><code>start_video</code></td><td>string</td><td></td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td></td></tr><tr><td><code>duration</code></td><td>integer or string</td><td></td></tr><tr><td><code>resolution</code></td><td>string</td><td></td></tr><tr><td><code>generate_audio</code></td><td>boolean</td><td></td></tr><tr><td><code>safety_tolerance</code></td><td>integer</td><td></td></tr><tr><td><code>draft</code></td><td>boolean</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td></td></tr><tr><td><code>draft_cache</code></td><td>string</td><td></td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/black-forest-labs/flux-3-video/schema-input.json)
- [Output schema](/ai/models/black-forest-labs/flux-3-video/schema-output.json)

