<img src="/assets/upstream/images/workers-ai/black-forest-labs.svg" alt="Black-Forest-Labs logo" width="48" height="48">

<h1 id="flux-2-max">FLUX.2 [max]</h1>

<p><code>black-forest-labs/flux-2-max</code></p>

FLUX.2 [max] is Black Forest Labs' highest-quality image model — top editing consistency, strongest prompt following, and grounding search for visualizations of real-time information.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://blackforestlabs.ai/terms-of-service/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>First output megapixel: 0.07, Per additional output megapixel: 0.03, Per input megapixel: 0.03</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Text-to-image generation at near-4MP resolution using FLUX.2's highest-quality endpoint

<section class="model-example"><strong>High Resolution Scene</strong>
<p>Text-to-image generation at near-4MP resolution using FLUX.2's highest-quality endpoint</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cat on its back legs running like a human is holding a big silver fish with its arms. The cat is running away from the shop owner and has a panicked look on his face. The scene is situated in a crowded market.&quot;,
    &quot;height&quot;: 2048,
    &quot;width&quot;: 1440
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/high-resolution-scene.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/high-resolution-scene.jpeg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-2-max&#x27;,
  {
    prompt:
      &#x27;A cat on its back legs running like a human is holding a big silver fish with its arms. The cat is running away from the shop owner and has a panicked look on his face. The scene is situated in a crowded market.&#x27;,
    height: 2048,
    width: 1440,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-2-max&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cat on its back legs running like a human is holding a big silver fish with its arms. The cat is running away from the shop owner and has a panicked look on his face. The scene is situated in a crowded market.&quot;,
    &quot;height&quot;: 2048,
    &quot;width&quot;: 1440
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/high-resolution-scene.jpeg" alt="High Resolution Scene">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Hex Color Control</strong>
<p>Exact color control via hex codes — useful for brand-consistent imagery</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A vase on a table in living room, the color of the vase is a gradient of color, starting with color #02eb3c and finishing with color #edfa3c. The flowers inside the vase have the color #ff0088&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/hex-color-control.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/hex-color-control.jpeg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-2-max&#x27;,
  {
    prompt:
      &#x27;A vase on a table in living room, the color of the vase is a gradient of color, starting with color #02eb3c and finishing with color #edfa3c. The flowers inside the vase have the color #ff0088&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-2-max&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A vase on a table in living room, the color of the vase is a gradient of color, starting with color #02eb3c and finishing with color #edfa3c. The flowers inside the vase have the color #ff0088&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/hex-color-control.jpeg" alt="Hex Color Control">
</section>

<section class="model-example"><strong>Image Editing</strong>
<p>Single-reference image editing — relight or restage a product photo</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Place this product onto a minimalist marble countertop with soft window light&quot;,
    &quot;input_images&quot;: [
      &quot;https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg&quot;
    ]
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/image-editing.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/image-editing.jpeg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-2-max&#x27;,
  {
    prompt: &#x27;Place this product onto a minimalist marble countertop with soft window light&#x27;,
    input_images: [
      &#x27;https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg&#x27;,
    ],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-2-max&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Place this product onto a minimalist marble countertop with soft window light&quot;,
    &quot;input_images&quot;: [
      &quot;https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg&quot;
    ]
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/image-editing.jpeg" alt="Image Editing">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt for image generation or editing.</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Optional seed for reproducible generation. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>width</code></td><td>integer</td><td>Width of the generated image in pixels (minimum 64). Omit to let BFL pick. Minimum: 64; Maximum: 9007199254740991</td></tr><tr><td><code>height</code></td><td>integer</td><td>Height of the generated image in pixels (minimum 64). Omit to let BFL pick. Minimum: 64; Maximum: 9007199254740991</td></tr><tr><td><code>safety_tolerance</code></td><td>integer</td><td>Tolerance for input/output moderation. 0 is the strictest, 5 the most permissive. Defaults to 2. Minimum: 0; Maximum: 5</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Output image format. Defaults to jpeg. Values: jpeg, png, webp</td></tr><tr><td><code>input_images</code></td><td>array</td><td>Up to 8 reference images for editing or multi-image composition. Each entry is an HTTPS URL or a data:image/...;base64,... URI.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required. URL to the generated image</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/black-forest-labs/flux-2-max/schema-input.json)
- [Output schema](/ai/models/black-forest-labs/flux-2-max/schema-output.json)

