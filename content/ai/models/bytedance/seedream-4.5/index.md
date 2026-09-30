<img src="/assets/upstream/images/workers-ai/bytedance.svg" alt="Bytedance logo" width="48" height="48">

<h1 id="seedream-4-5">Seedream 4.5</h1>

<p><code>bytedance/seedream-4.5</code></p>

Seedream 4.5 builds on 4.0 with multi-reference image support, batch generation, and sequential image generation.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.04</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-image generation

<section class="model-example"><strong>Simple Generation</strong>
<p>Basic text-to-image generation</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cozy reading nook with floor-to-ceiling bookshelves and a comfortable armchair&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/simple-generation-0.jpeg&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-5/0217764052077481386b9a8ed856c57501cfa946ce34c9865285c_0.jpeg&quot;
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-4.5&#x27;,
  { prompt: &#x27;A cozy reading nook with floor-to-ceiling bookshelves and a comfortable armchair&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-4.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cozy reading nook with floor-to-ceiling bookshelves and a comfortable armchair&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/simple-generation-0.jpeg" alt="Simple Generation">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>High Resolution</strong>
<p>4K quality image generation</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A hyperrealistic still life painting of fresh fruit on an antique wooden table with dramatic chiaroscuro lighting&quot;,
    &quot;aspect_ratio&quot;: &quot;4:3&quot;,
    &quot;size&quot;: &quot;4K&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/high-resolution-0.jpeg&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-5/0217764052077581386b9a8ed856c57501cfa946ce34c985dabe3_0.jpeg&quot;
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-4.5&#x27;,
  {
    prompt:
      &#x27;A hyperrealistic still life painting of fresh fruit on an antique wooden table with dramatic chiaroscuro lighting&#x27;,
    aspect_ratio: &#x27;4:3&#x27;,
    size: &#x27;4K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-4.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A hyperrealistic still life painting of fresh fruit on an antique wooden table with dramatic chiaroscuro lighting&quot;,
    &quot;aspect_ratio&quot;: &quot;4:3&quot;,
    &quot;size&quot;: &quot;4K&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/high-resolution-0.jpeg" alt="High Resolution">
</section>

<section class="model-example"><strong>Image-to-Image</strong>
<p>Edit using reference images</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Transform this scene into a winter wonderland with snow covering everything&quot;,
    &quot;aspect_ratio&quot;: &quot;match_input_image&quot;,
    &quot;image_input&quot;: [
      &quot;https://replicate.delivery/xezq/0lxxNQSg3NabCZrDiQVAPGVmjP1Q2dd7TgYCOTfI9LpyZaMLA/tmp89gopylq.jpg&quot;
    ]
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/image-to-image-0.jpeg&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-5/0217764052176861386b9a8ed856c57501cfa946ce34c98846458_0.jpeg&quot;
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-4.5&#x27;,
  {
    prompt: &#x27;Transform this scene into a winter wonderland with snow covering everything&#x27;,
    aspect_ratio: &#x27;match_input_image&#x27;,
    image_input: [
      &#x27;https://replicate.delivery/xezq/0lxxNQSg3NabCZrDiQVAPGVmjP1Q2dd7TgYCOTfI9LpyZaMLA/tmp89gopylq.jpg&#x27;,
    ],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-4.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Transform this scene into a winter wonderland with snow covering everything&quot;,
    &quot;aspect_ratio&quot;: &quot;match_input_image&quot;,
    &quot;image_input&quot;: [
      &quot;https://replicate.delivery/xezq/0lxxNQSg3NabCZrDiQVAPGVmjP1Q2dd7TgYCOTfI9LpyZaMLA/tmp89gopylq.jpg&quot;
    ]
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/image-to-image-0.jpeg" alt="Image-to-Image">
</section>

<section class="model-example"><strong>Sequential Generation</strong>
<p>Generate multiple related images</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A character design sheet for a fantasy warrior: front view, side view, and back view&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;max_images&quot;: 3,
    &quot;sequential_image_generation&quot;: &quot;auto&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/sequential-generation-0.jpeg&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-5/0217764052291261386b9a8ed856c57501cfa946ce34c98481db1_0.jpeg&quot;
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-4.5&#x27;,
  {
    prompt: &#x27;A character design sheet for a fantasy warrior: front view, side view, and back view&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    max_images: 3,
    sequential_image_generation: &#x27;auto&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-4.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A character design sheet for a fantasy warrior: front view, side view, and back view&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;max_images&quot;: 3,
    &quot;sequential_image_generation&quot;: &quot;auto&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/sequential-generation-0.jpeg" alt="Sequential Generation">
</section>

<section class="model-example"><strong>Multi-Image Edit</strong>
<p>Combine multiple reference images</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Combine the style of the first image with the subject from the second image&quot;,
    &quot;image_input&quot;: [
      &quot;https://replicate.delivery/xezq/TRYcLgNMrBpPJVq09ICKXWe4Z8d6olzpK5vtQPOB8O23ZaMLA/tmpaecga26m.jpg&quot;,
      &quot;https://replicate.delivery/xezq/1SbAc0aXYXbVD9doyrdCW78hYufVefMsaJXBrETN7Lu2npxsA/tmphvkx7emy.jpg&quot;
    ],
    &quot;size&quot;: &quot;2K&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/multi-image-edit-0.jpeg&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-5/0217764052323791386b9a8ed856c57501cfa946ce34c98b2f132_0.jpeg&quot;
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-4.5&#x27;,
  {
    prompt: &#x27;Combine the style of the first image with the subject from the second image&#x27;,
    image_input: [
      &#x27;https://replicate.delivery/xezq/TRYcLgNMrBpPJVq09ICKXWe4Z8d6olzpK5vtQPOB8O23ZaMLA/tmpaecga26m.jpg&#x27;,
      &#x27;https://replicate.delivery/xezq/1SbAc0aXYXbVD9doyrdCW78hYufVefMsaJXBrETN7Lu2npxsA/tmphvkx7emy.jpg&#x27;,
    ],
    size: &#x27;2K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-4.5&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Combine the style of the first image with the subject from the second image&quot;,
    &quot;image_input&quot;: [
      &quot;https://replicate.delivery/xezq/TRYcLgNMrBpPJVq09ICKXWe4Z8d6olzpK5vtQPOB8O23ZaMLA/tmpaecga26m.jpg&quot;,
      &quot;https://replicate.delivery/xezq/1SbAc0aXYXbVD9doyrdCW78hYufVefMsaJXBrETN7Lu2npxsA/tmphvkx7emy.jpg&quot;
    ],
    &quot;size&quot;: &quot;2K&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/multi-image-edit-0.jpeg" alt="Multi-Image Edit">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>image_input</code></td><td>array</td><td></td></tr><tr><td><code>size</code></td><td>string</td><td>Values: 2K, 4K</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Values: match_input_image, 1:1, 4:3, 3:4, 16:9, 9:16, 3:2, 2:3, 21:9</td></tr><tr><td><code>sequential_image_generation</code></td><td>string</td><td>Values: disabled, auto</td></tr><tr><td><code>max_images</code></td><td>integer</td><td>Minimum: 1; Maximum: 15</td></tr><tr><td><code>disable_safety_checker</code></td><td>boolean</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>images</code></td><td>array</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/bytedance/seedream-4.5/schema-input.json)
- [Output schema](/ai/models/bytedance/seedream-4.5/schema-output.json)

