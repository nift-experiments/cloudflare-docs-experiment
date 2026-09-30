<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="nano-banana-2">Nano Banana 2</h1>

<p><code>google/nano-banana-2</code></p>

Google's second-generation image generation model with improved quality and speed.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 0.5, Output tokens (per 1M): 60</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Sci-fi cityscape with neon lights

<section class="model-example"><strong>Futuristic City</strong>
<p>Sci-fi cityscape with neon lights</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A futuristic cyberpunk city at night with towering skyscrapers, neon signs in Japanese and English, flying cars, and rain-slicked streets reflecting colorful lights&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/google/nano-banana-2/futuristic-city.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/google/nano-banana-2/futuristic-city.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana-2&#x27;,
  {
    prompt:
      &#x27;A futuristic cyberpunk city at night with towering skyscrapers, neon signs in Japanese and English, flying cars, and rain-slicked streets reflecting colorful lights&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A futuristic cyberpunk city at night with towering skyscrapers, neon signs in Japanese and English, flying cars, and rain-slicked streets reflecting colorful lights&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/google/nano-banana-2/futuristic-city.png" alt="Futuristic City">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Abstract Art</strong>
<p>Modern abstract expressionist painting</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An abstract expressionist painting with bold splashes of cobalt blue, crimson red, and gold leaf accents on a large canvas&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;output_format&quot;: &quot;jpg&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/google/nano-banana-2/abstract-art.jpg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/google/nano-banana-2/abstract-art.jpg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana-2&#x27;,
  {
    prompt:
      &#x27;An abstract expressionist painting with bold splashes of cobalt blue, crimson red, and gold leaf accents on a large canvas&#x27;,
    aspect_ratio: &#x27;1:1&#x27;,
    output_format: &#x27;jpg&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An abstract expressionist painting with bold splashes of cobalt blue, crimson red, and gold leaf accents on a large canvas&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;output_format&quot;: &quot;jpg&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/google/nano-banana-2/abstract-art.jpg" alt="Abstract Art">
</section>

<section class="model-example"><strong>With Google Search</strong>
<p>Use web search grounding for current events</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An illustration of the latest Mars rover exploring the Martian surface&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;google_search&quot;: true
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/google/nano-banana-2/with-google-search.jpg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/google/nano-banana-2/with-google-search.jpg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana-2&#x27;,
  {
    prompt: &#x27;An illustration of the latest Mars rover exploring the Martian surface&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    google_search: true,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An illustration of the latest Mars rover exploring the Martian surface&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;google_search&quot;: true
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/google/nano-banana-2/with-google-search.jpg" alt="With Google Search">
</section>

<section class="model-example"><strong>High Resolution Portrait</strong>
<p>4K portrait with specific aspect ratio</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A professional studio portrait of a woman with dramatic side lighting, wearing elegant jewelry&quot;,
    &quot;aspect_ratio&quot;: &quot;3:4&quot;,
    &quot;output_format&quot;: &quot;jpg&quot;,
    &quot;resolution&quot;: &quot;4K&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/google/nano-banana-2/high-resolution-portrait.jpg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/google/nano-banana-2/high-resolution-portrait.jpg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana-2&#x27;,
  {
    prompt:
      &#x27;A professional studio portrait of a woman with dramatic side lighting, wearing elegant jewelry&#x27;,
    aspect_ratio: &#x27;3:4&#x27;,
    output_format: &#x27;jpg&#x27;,
    resolution: &#x27;4K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A professional studio portrait of a woman with dramatic side lighting, wearing elegant jewelry&quot;,
    &quot;aspect_ratio&quot;: &quot;3:4&quot;,
    &quot;output_format&quot;: &quot;jpg&quot;,
    &quot;resolution&quot;: &quot;4K&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/google/nano-banana-2/high-resolution-portrait.jpg" alt="High Resolution Portrait">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>image_input</code></td><td>array</td><td></td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Values: match_input_image, 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Values: jpg, png</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Values: 1K, 2K, 4K</td></tr><tr><td><code>google_search</code></td><td>boolean</td><td></td></tr><tr><td><code>image_search</code></td><td>boolean</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/google/nano-banana-2/schema-input.json)
- [Output schema](/ai/models/google/nano-banana-2/schema-output.json)

