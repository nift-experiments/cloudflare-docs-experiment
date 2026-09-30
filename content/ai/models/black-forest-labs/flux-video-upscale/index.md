<img src="/assets/upstream/images/workers-ai/black-forest-labs.svg" alt="Black-Forest-Labs logo" width="48" height="48">

<h1 id="flux-video-upscale">FLUX Video Upscale</h1>

<p><code>black-forest-labs/flux-video-upscale</code></p>

FLUX Video Upscale increases video resolution with a precise mode for source-faithful results and a creative mode for stronger detail enhancement. It accepts clips up to 20 seconds and preserves audio.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>video-to-video</td></tr>
<tr><th>Terms</th><td><a href="https://blackforestlabs.ai/terms-of-service/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Precise (per megapixel-second): 0.07, Creative (per megapixel-second): 0.1</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Upscale a source clip while preserving its identity and original detail.

<section class="model-example"><strong>Precise Video Upscale</strong>
<p>Upscale a source clip while preserving its identity and original detail.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input_video&quot;: &quot;https://replicate.delivery/pbxt/PetLEVcclEkT5H9A3tYETZyAMT5GE2Sa4m6sQqPDpj8vgHga/animatediff.B572L3lv.mp4&quot;,
    &quot;upscale_factor&quot;: 2,
    &quot;creativity&quot;: 0
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-video-upscale/precise-video-upscale.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-video-upscale/precise-video-upscale.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-video-upscale&#x27;,
  {
    input_video: &#x27;https://replicate.delivery/pbxt/PetLEVcclEkT5H9A3tYETZyAMT5GE2Sa4m6sQqPDpj8vgHga/animatediff.B572L3lv.mp4&#x27;,
    upscale_factor: 2,
    creativity: 0,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-video-upscale&quot;,
  &quot;input&quot;: {
    &quot;input_video&quot;: &quot;https://replicate.delivery/pbxt/PetLEVcclEkT5H9A3tYETZyAMT5GE2Sa4m6sQqPDpj8vgHga/animatediff.B572L3lv.mp4&quot;,
    &quot;upscale_factor&quot;: 2,
    &quot;creativity&quot;: 0
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Creative Video Upscale</strong>
<p>Enhance fine detail in a source clip using creative mode.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input_video&quot;: &quot;https://replicate.delivery/xezq/q1XccP3m8V4HMBNDY3LBkaiKjPdJ6e7t74ICqq2wbfWHJNFXA/tmpq8inl7pd.mp4&quot;,
    &quot;upscale_factor&quot;: 2,
    &quot;creativity&quot;: 1,
    &quot;prompt&quot;: &quot;A cinematic travel video with detailed natural scenery and crisp texture&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-video-upscale/creative-video-upscale.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-video-upscale/creative-video-upscale.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-video-upscale&#x27;,
  {
    input_video: &#x27;https://replicate.delivery/xezq/q1XccP3m8V4HMBNDY3LBkaiKjPdJ6e7t74ICqq2wbfWHJNFXA/tmpq8inl7pd.mp4&#x27;,
    upscale_factor: 2,
    creativity: 1,
    prompt: &#x27;A cinematic travel video with detailed natural scenery and crisp texture&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-video-upscale&quot;,
  &quot;input&quot;: {
    &quot;input_video&quot;: &quot;https://replicate.delivery/xezq/q1XccP3m8V4HMBNDY3LBkaiKjPdJ6e7t74ICqq2wbfWHJNFXA/tmpq8inl7pd.mp4&quot;,
    &quot;upscale_factor&quot;: 2,
    &quot;creativity&quot;: 1,
    &quot;prompt&quot;: &quot;A cinematic travel video with detailed natural scenery and crisp texture&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>input_video</code></td><td>string</td><td>Required. HTTP(S) URL or base64-encoded MP4 video, up to 20 seconds and 50MB.</td></tr><tr><td><code>upscale_factor</code></td><td>number</td><td>Output scale relative to the source resolution, from 1.5x to 3x. Minimum: 1.5; Maximum: 3</td></tr><tr><td><code>creativity</code></td><td>number</td><td>0 preserves the source precisely; 1 enhances fine detail creatively.</td></tr><tr><td><code>prompt</code></td><td>string</td><td>Optional description of the clip to guide creative detail enhancement.</td></tr><tr><td><code>safety_tolerance</code></td><td>integer</td><td>Moderation strictness, from 0 (strictest) to 4. Minimum: 0; Maximum: 4</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required. Signed URL to the upscaled MP4. Download promptly before it expires.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/black-forest-labs/flux-video-upscale/schema-input.json)
- [Output schema](/ai/models/black-forest-labs/flux-video-upscale/schema-output.json)

