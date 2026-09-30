<img src="/assets/upstream/images/workers-ai/xai.svg" alt="Xai logo" width="48" height="48">

<h1 id="grok-imagine-image-2-0">Grok Imagine Image 2.0</h1>

<p><code>xai/grok-imagine-image-2.0</code></p>

xAI's Grok Imagine Image 2.0 is a precise image generation and editing model for creative work, with strong instruction following, typography, layout, and reference-image preservation.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://x.ai/legal/terms-of-service">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.04, Per input image: 0.01</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-image generation

<section class="model-example"><strong>Simple Generation</strong>
<p>Basic text-to-image generation</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A concert poster for a synthwave band, bold retro typography, sharp small print&quot;,
    &quot;response_format&quot;: &quot;b64_json&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/simple-generation.jpg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/simple-generation.jpg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-imagine-image-2.0&#x27;,
  { prompt: &#x27;A concert poster for a synthwave band, bold retro typography, sharp small print&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-imagine-image-2.0&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A concert poster for a synthwave band, bold retro typography, sharp small print&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/simple-generation.jpg" alt="Simple Generation">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Portrait 2K</strong>
<p>High-resolution image with a controlled aspect ratio</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;aspect_ratio&quot;: &quot;3:4&quot;,
    &quot;prompt&quot;: &quot;A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures&quot;,
    &quot;quality&quot;: &quot;medium&quot;,
    &quot;resolution&quot;: &quot;2k&quot;,
    &quot;response_format&quot;: &quot;b64_json&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/portrait-2k.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/portrait-2k.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-imagine-image-2.0&#x27;,
  {
    aspect_ratio: &#x27;3:4&#x27;,
    prompt:
      &#x27;A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures&#x27;,
    quality: &#x27;medium&#x27;,
    resolution: &#x27;2k&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-imagine-image-2.0&quot;,
  &quot;input&quot;: {
    &quot;aspect_ratio&quot;: &quot;3:4&quot;,
    &quot;prompt&quot;: &quot;A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures&quot;,
    &quot;quality&quot;: &quot;medium&quot;,
    &quot;resolution&quot;: &quot;2k&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/portrait-2k.png" alt="Portrait 2K">
</section>

<section class="model-example"><strong>Low Quality Draft</strong>
<p>Fast low-quality draft for iteration</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;prompt&quot;: &quot;A quiet Japanese garden in morning mist with a stone lantern and koi pond&quot;,
    &quot;quality&quot;: &quot;low&quot;,
    &quot;resolution&quot;: &quot;1k&quot;,
    &quot;response_format&quot;: &quot;b64_json&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/low-quality-draft.jpg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/low-quality-draft.jpg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-imagine-image-2.0&#x27;,
  {
    aspect_ratio: &#x27;1:1&#x27;,
    prompt: &#x27;A quiet Japanese garden in morning mist with a stone lantern and koi pond&#x27;,
    quality: &#x27;low&#x27;,
    resolution: &#x27;1k&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-imagine-image-2.0&quot;,
  &quot;input&quot;: {
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;prompt&quot;: &quot;A quiet Japanese garden in morning mist with a stone lantern and koi pond&quot;,
    &quot;quality&quot;: &quot;low&quot;,
    &quot;resolution&quot;: &quot;1k&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/low-quality-draft.jpg" alt="Low Quality Draft">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Values: 1:1, 3:4, 4:3, 9:16, 16:9, 2:3, 3:2, 9:19.5, 19.5:9, 9:20, 20:9, 1:2, 2:1, auto</td></tr><tr><td><code>quality</code></td><td>string</td><td>Values: low, medium</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Values: 1k, 2k</td></tr><tr><td><code>response_format</code></td><td>string</td><td>Values: url, b64_json</td></tr><tr><td><code>user</code></td><td>string</td><td></td></tr><tr><td><code>image</code></td><td>object</td><td></td></tr><tr><td><code>image.url</code></td><td>string</td><td>Required.</td></tr><tr><td><code>image.type</code></td><td>string</td><td></td></tr><tr><td><code>images</code></td><td>array</td><td></td></tr><tr><td><code>images[].url</code></td><td>string</td><td>Required.</td></tr><tr><td><code>images[].type</code></td><td>string</td><td></td></tr><tr><td><code>mask</code></td><td>object</td><td></td></tr><tr><td><code>mask.url</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required. Generated image. Either a base64 data URI (`data:image/png;base64,...`) or an `https://` URL, depending on the upstream `response_format`.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/xai/grok-imagine-image-2.0/schema-input.json)
- [Output schema](/ai/models/xai/grok-imagine-image-2.0/schema-output.json)

