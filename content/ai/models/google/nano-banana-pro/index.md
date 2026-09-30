<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="nano-banana-pro">Nano Banana Pro</h1>

<p><code>google/nano-banana-pro</code></p>

Google's higher-quality image generation model with improved detail and prompt adherence.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 2, Output tokens (per 1M): 120</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Professional product shot

<section class="model-example"><strong>Product Photography</strong>
<p>Professional product shot</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sleek modern wireless headphone on a minimalist white marble surface with soft studio lighting and subtle shadows&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;output_format&quot;: &quot;png&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/product-photography.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/product-photography.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana-pro&#x27;,
  {
    prompt:
      &#x27;A sleek modern wireless headphone on a minimalist white marble surface with soft studio lighting and subtle shadows&#x27;,
    aspect_ratio: &#x27;1:1&#x27;,
    output_format: &#x27;png&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sleek modern wireless headphone on a minimalist white marble surface with soft studio lighting and subtle shadows&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;output_format&quot;: &quot;png&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/product-photography.png" alt="Product Photography">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Fantasy Illustration</strong>
<p>Epic fantasy scene</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An epic fantasy illustration of a wizard casting a spell in an ancient library, magical runes floating in the air, dust motes catching golden light streaming through stained glass windows&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;image_size&quot;: &quot;2K&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/fantasy-illustration.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/fantasy-illustration.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana-pro&#x27;,
  {
    prompt:
      &#x27;An epic fantasy illustration of a wizard casting a spell in an ancient library, magical runes floating in the air, dust motes catching golden light streaming through stained glass windows&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    image_size: &#x27;2K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An epic fantasy illustration of a wizard casting a spell in an ancient library, magical runes floating in the air, dust motes catching golden light streaming through stained glass windows&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;image_size&quot;: &quot;2K&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/fantasy-illustration.png" alt="Fantasy Illustration">
</section>

<section class="model-example"><strong>Architectural Visualization</strong>
<p>Modern architecture render</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A photorealistic architectural visualization of a modern glass house perched on a cliff overlooking the ocean at sunset&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;image_size&quot;: &quot;4K&quot;,
    &quot;output_format&quot;: &quot;jpg&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/architectural-visualization.jpg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/architectural-visualization.jpg&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana-pro&#x27;,
  {
    prompt:
      &#x27;A photorealistic architectural visualization of a modern glass house perched on a cliff overlooking the ocean at sunset&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    image_size: &#x27;4K&#x27;,
    output_format: &#x27;jpg&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A photorealistic architectural visualization of a modern glass house perched on a cliff overlooking the ocean at sunset&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;image_size&quot;: &quot;4K&quot;,
    &quot;output_format&quot;: &quot;jpg&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/architectural-visualization.jpg" alt="Architectural Visualization">
</section>

<section class="model-example"><strong>Character Design</strong>
<p>Game character concept art</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed character design sheet for a steampunk inventor, showing front view, side view, and detail callouts for mechanical arm and goggles&quot;,
    &quot;aspect_ratio&quot;: &quot;3:2&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/character-design.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/character-design.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana-pro&#x27;,
  {
    prompt:
      &#x27;A detailed character design sheet for a steampunk inventor, showing front view, side view, and detail callouts for mechanical arm and goggles&#x27;,
    aspect_ratio: &#x27;3:2&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed character design sheet for a steampunk inventor, showing front view, side view, and detail callouts for mechanical arm and goggles&quot;,
    &quot;aspect_ratio&quot;: &quot;3:2&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/character-design.png" alt="Character Design">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>image_input</code></td><td>array</td><td></td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Values: 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Values: jpg, png, webp</td></tr><tr><td><code>image_size</code></td><td>string</td><td>Values: 1K, 2K, 4K</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/google/nano-banana-pro/schema-input.json)
- [Output schema](/ai/models/google/nano-banana-pro/schema-output.json)

