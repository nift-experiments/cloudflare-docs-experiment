<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="gpt-image-2-5-sunburst">GPT Image 2.5 Sunburst</h1>

<p><code>openai/gpt-image-2.5-sunburst</code></p>

OpenAI's most capable image generation and editing model. It accepts text and image inputs and produces images with low, medium, high, xhigh, max, and auto quality settings.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Cached input image tokens (per 1M): 3, Cached input tokens (per 1M): 1.25, Input image tokens (per 1M): 8, Input tokens (per 1M): 5, Output image tokens (per 1M): 30</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Create a detailed editorial illustration with the highest quality setting

<section class="model-example"><strong>Technical Editorial Illustration</strong>
<p>Create a detailed editorial illustration with the highest quality setting</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cutaway editorial illustration of a floating ocean research station during a storm, showing laboratories, hydroponic gardens, autonomous submersibles, and illuminated underwater cables, precise technical details, dramatic but realistic lighting&quot;,
    &quot;quality&quot;: &quot;max&quot;,
    &quot;size&quot;: &quot;1536x1024&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/technical-editorial-illustration.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/technical-editorial-illustration.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-2.5-sunburst&#x27;,
  {
    prompt:
      &#x27;A cutaway editorial illustration of a floating ocean research station during a storm, showing laboratories, hydroponic gardens, autonomous submersibles, and illuminated underwater cables, precise technical details, dramatic but realistic lighting&#x27;,
    quality: &#x27;max&#x27;,
    size: &#x27;1536x1024&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-2.5-sunburst&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cutaway editorial illustration of a floating ocean research station during a storm, showing laboratories, hydroponic gardens, autonomous submersibles, and illuminated underwater cables, precise technical details, dramatic but realistic lighting&quot;,
    &quot;quality&quot;: &quot;max&quot;,
    &quot;size&quot;: &quot;1536x1024&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/technical-editorial-illustration.png" alt="Technical Editorial Illustration">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Portrait WebP</strong>
<p>Generate a portrait composition in WebP format</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A fashion portrait of an astronaut botanist in a glass greenhouse on Mars, crimson dust visible through the windows, translucent fabric, delicate blue flowers in the foreground, soft rim light, sophisticated magazine photography&quot;,
    &quot;quality&quot;: &quot;xhigh&quot;,
    &quot;size&quot;: &quot;1024x1536&quot;,
    &quot;output_format&quot;: &quot;webp&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/portrait-webp.webp&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/portrait-webp.webp&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-2.5-sunburst&#x27;,
  {
    prompt:
      &#x27;A fashion portrait of an astronaut botanist in a glass greenhouse on Mars, crimson dust visible through the windows, translucent fabric, delicate blue flowers in the foreground, soft rim light, sophisticated magazine photography&#x27;,
    quality: &#x27;xhigh&#x27;,
    size: &#x27;1024x1536&#x27;,
    output_format: &#x27;webp&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-2.5-sunburst&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A fashion portrait of an astronaut botanist in a glass greenhouse on Mars, crimson dust visible through the windows, translucent fabric, delicate blue flowers in the foreground, soft rim light, sophisticated magazine photography&quot;,
    &quot;quality&quot;: &quot;xhigh&quot;,
    &quot;size&quot;: &quot;1024x1536&quot;,
    &quot;output_format&quot;: &quot;webp&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/portrait-webp.webp" alt="Portrait WebP">
</section>

<section class="model-example"><strong>Cinematic Reference Edit</strong>
<p>Edit a reference image into a cinematic scene while preserving its main subject</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Turn the reference drawing into a polished cinematic stop-motion scene. Preserve the character&#x27;s face and red scarf, add a miniature train platform at night, warm station lights, shallow depth of field, handcrafted felt and paper textures&quot;,
    &quot;images&quot;: [
      &quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&quot;
    ],
    &quot;quality&quot;: &quot;high&quot;,
    &quot;background&quot;: &quot;opaque&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/cinematic-reference-edit.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/cinematic-reference-edit.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-2.5-sunburst&#x27;,
  {
    prompt:
      &quot;Turn the reference drawing into a polished cinematic stop-motion scene. Preserve the character&#x27;s face and red scarf, add a miniature train platform at night, warm station lights, shallow depth of field, handcrafted felt and paper textures&quot;,
    images: [
      &#x27;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&#x27;,
    ],
    quality: &#x27;high&#x27;,
    background: &#x27;opaque&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-2.5-sunburst&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Turn the reference drawing into a polished cinematic stop-motion scene. Preserve the character&#x27;\&#x27;&#x27;s face and red scarf, add a miniature train platform at night, warm station lights, shallow depth of field, handcrafted felt and paper textures&quot;,
    &quot;images&quot;: [
      &quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&quot;
    ],
    &quot;quality&quot;: &quot;high&quot;,
    &quot;background&quot;: &quot;opaque&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/cinematic-reference-edit.png" alt="Cinematic Reference Edit">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing the image to generate or edit</td></tr><tr><td><code>images</code></td><td>array</td><td>Input images for image editing, 1-16 entries. Each entry is base64-encoded (raw string or data:image/{png|jpeg|webp};base64,... URI).</td></tr><tr><td><code>quality</code></td><td>string</td><td>Quality of the generated image Values: low, medium, high, xhigh, max, auto</td></tr><tr><td><code>size</code></td><td>string</td><td>Size of the generated image Values: 1024x1024, 1024x1536, 1536x1024, auto</td></tr><tr><td><code>background</code></td><td>string</td><td>Background transparency setting Values: transparent, opaque, auto</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Output format for the generated image Values: png, webp, jpeg</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required. URL to the generated image</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/openai/gpt-image-2.5-sunburst/schema-input.json)
- [Output schema](/ai/models/openai/gpt-image-2.5-sunburst/schema-output.json)

