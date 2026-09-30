<img src="/assets/upstream/images/workers-ai/black-forest-labs.svg" alt="Black-Forest-Labs logo" width="48" height="48">

<h1 id="flux-2-pro">FLUX.2 [pro]</h1>

<p><code>black-forest-labs/flux-2-pro-preview</code></p>

FLUX.2 [pro] Preview is Black Forest Labs' recommended default for production image generation and editing — tracks the latest [pro] weights with strong multi-reference support.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://blackforestlabs.ai/terms-of-service/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>First output megapixel: 0.03, Per additional output megapixel: 0.015, Per input megapixel: 0.015</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Standard text-to-image generation with the recommended FLUX.2 [pro] preview endpoint

<section class="model-example"><strong>Simple Prompt</strong>
<p>Standard text-to-image generation with the recommended FLUX.2 [pro] preview endpoint</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A serene mountain landscape at golden hour, soft diffused light filtering through clouds&quot;,
    &quot;height&quot;: 1024,
    &quot;width&quot;: 1024
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/simple-prompt.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/simple-prompt.jpeg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-2-pro-preview&#x27;,
  {
    prompt:
      &#x27;A serene mountain landscape at golden hour, soft diffused light filtering through clouds&#x27;,
    height: 1024,
    width: 1024,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-2-pro-preview&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A serene mountain landscape at golden hour, soft diffused light filtering through clouds&quot;,
    &quot;height&quot;: 1024,
    &quot;width&quot;: 1024
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/simple-prompt.jpeg" alt="Simple Prompt">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Multi-Reference Editing</strong>
<p>Multi-reference editing — combine two reference images in a single composition</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Combine the subjects of these images into a single editorial fashion scene&quot;,
    &quot;input_images&quot;: [
      &quot;https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg&quot;,
      &quot;https://replicate.delivery/xezq/0lxxNQSg3NabCZrDiQVAPGVmjP1Q2dd7TgYCOTfI9LpyZaMLA/tmp89gopylq.jpg&quot;
    ]
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/multi-reference-editing.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/multi-reference-editing.jpeg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-2-pro-preview&#x27;,
  {
    prompt: &#x27;Combine the subjects of these images into a single editorial fashion scene&#x27;,
    input_images: [
      &#x27;https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg&#x27;,
      &#x27;https://replicate.delivery/xezq/0lxxNQSg3NabCZrDiQVAPGVmjP1Q2dd7TgYCOTfI9LpyZaMLA/tmp89gopylq.jpg&#x27;,
    ],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-2-pro-preview&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Combine the subjects of these images into a single editorial fashion scene&quot;,
    &quot;input_images&quot;: [
      &quot;https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg&quot;,
      &quot;https://replicate.delivery/xezq/0lxxNQSg3NabCZrDiQVAPGVmjP1Q2dd7TgYCOTfI9LpyZaMLA/tmp89gopylq.jpg&quot;
    ]
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/multi-reference-editing.jpeg" alt="Multi-Reference Editing">
</section>

<section class="model-example"><strong>Reproducible PNG Output</strong>
<p>Seeded generation with PNG output for downstream editing pipelines</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A pastel watercolor of a koi pond at sunrise&quot;,
    &quot;output_format&quot;: &quot;png&quot;,
    &quot;seed&quot;: 1337
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/reproducible-png-output.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/reproducible-png-output.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-2-pro-preview&#x27;,
  { prompt: &#x27;A pastel watercolor of a koi pond at sunrise&#x27;, output_format: &#x27;png&#x27;, seed: 1337 },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-2-pro-preview&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A pastel watercolor of a koi pond at sunrise&quot;,
    &quot;output_format&quot;: &quot;png&quot;,
    &quot;seed&quot;: 1337
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/reproducible-png-output.png" alt="Reproducible PNG Output">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt for image generation or editing.</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Optional seed for reproducible generation. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>width</code></td><td>integer</td><td>Width of the generated image in pixels (minimum 64). Omit to let BFL pick. Minimum: 64; Maximum: 9007199254740991</td></tr><tr><td><code>height</code></td><td>integer</td><td>Height of the generated image in pixels (minimum 64). Omit to let BFL pick. Minimum: 64; Maximum: 9007199254740991</td></tr><tr><td><code>safety_tolerance</code></td><td>integer</td><td>Tolerance for input/output moderation. 0 is the strictest, 5 the most permissive. Defaults to 2. Minimum: 0; Maximum: 5</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Output image format. Defaults to jpeg. Values: jpeg, png, webp</td></tr><tr><td><code>input_images</code></td><td>array</td><td>Up to 8 reference images for editing or multi-image composition. Each entry is an HTTPS URL or a data:image/...;base64,... URI.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required. URL to the generated image</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/black-forest-labs/flux-2-pro-preview/schema-input.json)
- [Output schema](/ai/models/black-forest-labs/flux-2-pro-preview/schema-output.json)

