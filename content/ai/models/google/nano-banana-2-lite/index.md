<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="nano-banana-2-lite">Nano Banana 2 Lite</h1>

<p><code>google/nano-banana-2-lite</code></p>

Google's fastest Gemini image generation model for rapid image creation and iteration.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Context window</th><td>65,536 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 0.25, Output tokens (per 1M): 30</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate a fast concept illustration

<section class="model-example"><strong>Concept Sketch</strong>
<p>Generate a fast concept illustration</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A playful concept sketch of a compact solar-powered delivery robot rolling through a leafy neighborhood, bright morning light, clean product design&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/google/nano-banana-2-lite/concept-sketch.jpg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/google/nano-banana-2-lite/concept-sketch.jpg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana-2-lite&#x27;,
  {
    prompt:
      &#x27;A playful concept sketch of a compact solar-powered delivery robot rolling through a leafy neighborhood, bright morning light, clean product design&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana-2-lite&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A playful concept sketch of a compact solar-powered delivery robot rolling through a leafy neighborhood, bright morning light, clean product design&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/google/nano-banana-2-lite/concept-sketch.jpg" alt="Concept Sketch">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Product Render</strong>
<p>Create a square PNG product image</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A studio product render of translucent wireless earbuds in a frosted glass charging case, soft gradient background, premium advertising style&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;output_format&quot;: &quot;png&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/google/nano-banana-2-lite/product-render.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/google/nano-banana-2-lite/product-render.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana-2-lite&#x27;,
  {
    prompt:
      &#x27;A studio product render of translucent wireless earbuds in a frosted glass charging case, soft gradient background, premium advertising style&#x27;,
    aspect_ratio: &#x27;1:1&#x27;,
    output_format: &#x27;png&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana-2-lite&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A studio product render of translucent wireless earbuds in a frosted glass charging case, soft gradient background, premium advertising style&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;output_format&quot;: &quot;png&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/google/nano-banana-2-lite/product-render.png" alt="Product Render">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>image_input</code></td><td>array</td><td></td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Values: match_input_image, 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Values: jpg, png</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Values: 1K, 2K, 4K</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/google/nano-banana-2-lite/schema-input.json)
- [Output schema](/ai/models/google/nano-banana-2-lite/schema-output.json)

