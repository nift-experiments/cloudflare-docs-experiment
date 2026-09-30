<img src="/assets/upstream/images/workers-ai/recraft.svg" alt="Recraft logo" width="48" height="48">

<h1 id="recraft-v4-1-svg">Recraft V4.1 SVG</h1>

<p><code>recraft/recraftv4-1-vector</code></p>

Generate production-ready SVG vector graphics from text prompts with high aesthetic quality, clean geometry, structured layers, and editable paths.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://www.recraft.ai/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.08</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate a basic vector icon

<section class="model-example"><strong>Simple Icon</strong>
<p>Generate a basic vector icon</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A simple flat icon of a coffee cup with steam rising&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-vector/simple-icon.jpg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-vector/simple-icon.jpg&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-vector&#x27;,
  { prompt: &#x27;A simple flat icon of a coffee cup with steam rising&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-vector&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A simple flat icon of a coffee cup with steam rising&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-vector/simple-icon.jpg" alt="Simple Icon">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>App Icon</strong>
<p>Mobile app icon in vector format</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A colorful gradient app icon featuring a chat bubble with a sparkle effect&quot;,
    &quot;size&quot;: &quot;1024x1024&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-vector/app-icon.jpg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-vector/app-icon.jpg&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-vector&#x27;,
  {
    prompt: &#x27;A colorful gradient app icon featuring a chat bubble with a sparkle effect&#x27;,
    size: &#x27;1024x1024&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-vector&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A colorful gradient app icon featuring a chat bubble with a sparkle effect&quot;,
    &quot;size&quot;: &quot;1024x1024&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-vector/app-icon.jpg" alt="App Icon">
</section>

<section class="model-example"><strong>Illustration</strong>
<p>Vector illustration for web use</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A flat vector illustration of a person working at a desk with a computer, plants, and a window showing a city view&quot;,
    &quot;size&quot;: &quot;1024x1024&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-vector/illustration.jpg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-vector/illustration.jpg&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-vector&#x27;,
  {
    prompt:
      &#x27;A flat vector illustration of a person working at a desk with a computer, plants, and a window showing a city view&#x27;,
    size: &#x27;1024x1024&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-vector&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A flat vector illustration of a person working at a desk with a computer, plants, and a window showing a city view&quot;,
    &quot;size&quot;: &quot;1024x1024&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-vector/illustration.jpg" alt="Illustration">
</section>

<section class="model-example"><strong>With Brand Colors</strong>
<p>Vector with specific color palette</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A badge or seal design with a star in the center, suitable for a certification mark&quot;,
    &quot;controls&quot;: {
      &quot;background_color&quot;: {
        &quot;rgb&quot;: [
          255,
          255,
          255
        ]
      },
      &quot;colors&quot;: [
        {
          &quot;rgb&quot;: [
            0,
            119,
            182
          ]
        },
        {
          &quot;rgb&quot;: [
            255,
            209,
            102
          ]
        }
      ]
    }
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-vector/with-brand-colors.jpg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-vector/with-brand-colors.jpg&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-vector&#x27;,
  {
    prompt: &#x27;A badge or seal design with a star in the center, suitable for a certification mark&#x27;,
    controls: {
      background_color: { rgb: [255, 255, 255] },
      colors: [{ rgb: [0, 119, 182] }, { rgb: [255, 209, 102] }],
    },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-vector&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A badge or seal design with a star in the center, suitable for a certification mark&quot;,
    &quot;controls&quot;: {
      &quot;background_color&quot;: {
        &quot;rgb&quot;: [
          255,
          255,
          255
        ]
      },
      &quot;colors&quot;: [
        {
          &quot;rgb&quot;: [
            0,
            119,
            182
          ]
        },
        {
          &quot;rgb&quot;: [
            255,
            209,
            102
          ]
        }
      ]
    }
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-vector/with-brand-colors.jpg" alt="With Brand Colors">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>size</code></td><td>string</td><td></td></tr><tr><td><code>style</code></td><td>string</td><td></td></tr><tr><td><code>substyle</code></td><td>string</td><td></td></tr><tr><td><code>controls</code></td><td>object</td><td></td></tr><tr><td><code>controls.colors</code></td><td>array</td><td></td></tr><tr><td><code>controls.colors[].rgb</code></td><td>array</td><td>Required.</td></tr><tr><td><code>controls.background_color</code></td><td>object</td><td></td></tr><tr><td><code>controls.background_color.rgb</code></td><td>array</td><td>Required.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/recraft/recraftv4-1-vector/schema-input.json)
- [Output schema](/ai/models/recraft/recraftv4-1-vector/schema-output.json)

