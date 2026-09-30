<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="gpt-image-1-5">GPT Image 1.5</h1>

<p><code>openai/gpt-image-1.5</code></p>

OpenAI's image generation model that creates and edits images from text prompts, supporting multiple quality levels and output sizes.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 5, Input image tokens (per 1M): 8, Cached input tokens (per 1M): 1.25, Cached input image tokens (per 1M): 2, Output image tokens (per 1M): 32, Output tokens (per 1M): 10</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-image with just a prompt

<section class="model-example"><strong>Simple Generation</strong>
<p>Basic text-to-image with just a prompt</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever puppy playing in autumn leaves&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/simple-generation.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/simple-generation.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-1.5&#x27;,
  { prompt: &#x27;A golden retriever puppy playing in autumn leaves&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-1.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever puppy playing in autumn leaves&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/simple-generation.png" alt="Simple Generation">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>High Quality</strong>
<p>Generate a high-quality detailed image</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures&quot;,
    &quot;quality&quot;: &quot;high&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/high-quality.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/high-quality.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-1.5&#x27;,
  {
    prompt:
      &#x27;A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures&#x27;,
    quality: &#x27;high&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-1.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures&quot;,
    &quot;quality&quot;: &quot;high&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/high-quality.png" alt="High Quality">
</section>

<section class="model-example"><strong>Low Quality Draft</strong>
<p>Fast, rough draft for iteration</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A quiet Japanese garden in morning mist with a stone lantern and koi pond&quot;,
    &quot;quality&quot;: &quot;low&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/low-quality-draft.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/low-quality-draft.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-1.5&#x27;,
  {
    prompt: &#x27;A quiet Japanese garden in morning mist with a stone lantern and koi pond&#x27;,
    quality: &#x27;low&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-1.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A quiet Japanese garden in morning mist with a stone lantern and koi pond&quot;,
    &quot;quality&quot;: &quot;low&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/low-quality-draft.png" alt="Low Quality Draft">
</section>

<section class="model-example"><strong>Medium Quality</strong>
<p>Balanced quality for most uses</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A neon-lit cyberpunk figure standing in the rain beneath a holographic billboard, cinematic lighting&quot;,
    &quot;quality&quot;: &quot;medium&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/medium-quality.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/medium-quality.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-1.5&#x27;,
  {
    prompt:
      &#x27;A neon-lit cyberpunk figure standing in the rain beneath a holographic billboard, cinematic lighting&#x27;,
    quality: &#x27;medium&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-1.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A neon-lit cyberpunk figure standing in the rain beneath a holographic billboard, cinematic lighting&quot;,
    &quot;quality&quot;: &quot;medium&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/medium-quality.png" alt="Medium Quality">
</section>

<section class="model-example"><strong>Auto Quality</strong>
<p>Let the model pick an appropriate quality level</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A panoramic view of the northern lights over a snowy mountain range, vivid greens and purples dancing across the sky&quot;,
    &quot;quality&quot;: &quot;auto&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/auto-quality.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/auto-quality.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-1.5&#x27;,
  {
    prompt:
      &#x27;A panoramic view of the northern lights over a snowy mountain range, vivid greens and purples dancing across the sky&#x27;,
    quality: &#x27;auto&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-1.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A panoramic view of the northern lights over a snowy mountain range, vivid greens and purples dancing across the sky&quot;,
    &quot;quality&quot;: &quot;auto&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-1.5/auto-quality.png" alt="Auto Quality">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing the image to generate or edit</td></tr><tr><td><code>images</code></td><td>array</td><td>Input images for image editing, 1-16 entries. Each entry is base64-encoded (raw string or data:image/{png|jpeg|webp};base64,... URI).</td></tr><tr><td><code>quality</code></td><td>string</td><td>Quality of the generated image Values: low, medium, high, auto</td></tr><tr><td><code>size</code></td><td>string</td><td>Size of the generated image Values: 256x256, 512x512, 1024x1024, 1792x1024, 1024x1792</td></tr><tr><td><code>style</code></td><td>string</td><td>Style of the generated image Values: vivid, natural</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required. URL to the generated image</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/openai/gpt-image-1.5/schema-input.json)
- [Output schema](/ai/models/openai/gpt-image-1.5/schema-output.json)

