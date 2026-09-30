<img src="/assets/upstream/images/workers-ai/recraft.svg" alt="Recraft logo" width="48" height="48">

<h1 id="recraft-v4-1-utility-pro">Recraft V4.1 Utility Pro</h1>

<p><code>recraft/recraftv4-1-utility-pro</code></p>

Recraft V4.1 Utility Pro is a general-purpose text-to-image model producing high-resolution 2048px+ output for a wide range of production and print use cases.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://www.recraft.ai/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.25</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

High-resolution illustration for print

<section class="model-example"><strong>Print-Ready Illustration</strong>
<p>High-resolution illustration for print</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed illustrated map of an imaginary fantasy island with labeled landmarks, mountains, and forests&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/print-ready-illustration.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/print-ready-illustration.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-utility-pro&#x27;,
  {
    prompt:
      &#x27;A detailed illustrated map of an imaginary fantasy island with labeled landmarks, mountains, and forests&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-utility-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed illustrated map of an imaginary fantasy island with labeled landmarks, mountains, and forests&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/print-ready-illustration.png" alt="Print-Ready Illustration">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Large Format Art</strong>
<p>Large canvas general-purpose image</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A wide panoramic landscape of rolling green hills with a river winding through the valley under a bright blue sky&quot;,
    &quot;size&quot;: &quot;2048x2048&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/large-format-art.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/large-format-art.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-utility-pro&#x27;,
  {
    prompt:
      &#x27;A wide panoramic landscape of rolling green hills with a river winding through the valley under a bright blue sky&#x27;,
    size: &#x27;2048x2048&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-utility-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A wide panoramic landscape of rolling green hills with a river winding through the valley under a bright blue sky&quot;,
    &quot;size&quot;: &quot;2048x2048&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/large-format-art.png" alt="Large Format Art">
</section>

<section class="model-example"><strong>Marketing Asset</strong>
<p>High-resolution marketing visual with controlled colors</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A clean, modern banner illustration of a smartphone displaying a productivity app&quot;,
    &quot;controls&quot;: {
      &quot;background_color&quot;: {
        &quot;rgb&quot;: [
          250,
          250,
          255
        ]
      },
      &quot;colors&quot;: [
        {
          &quot;rgb&quot;: [
            100,
            200,
            150
          ]
        },
        {
          &quot;rgb&quot;: [
            20,
            20,
            60
          ]
        }
      ]
    },
    &quot;size&quot;: &quot;2048x2048&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/marketing-asset.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/marketing-asset.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-utility-pro&#x27;,
  {
    prompt: &#x27;A clean, modern banner illustration of a smartphone displaying a productivity app&#x27;,
    controls: {
      background_color: { rgb: [250, 250, 255] },
      colors: [{ rgb: [100, 200, 150] }, { rgb: [20, 20, 60] }],
    },
    size: &#x27;2048x2048&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-utility-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A clean, modern banner illustration of a smartphone displaying a productivity app&quot;,
    &quot;controls&quot;: {
      &quot;background_color&quot;: {
        &quot;rgb&quot;: [
          250,
          250,
          255
        ]
      },
      &quot;colors&quot;: [
        {
          &quot;rgb&quot;: [
            100,
            200,
            150
          ]
        },
        {
          &quot;rgb&quot;: [
            20,
            20,
            60
          ]
        }
      ]
    },
    &quot;size&quot;: &quot;2048x2048&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/marketing-asset.png" alt="Marketing Asset">
</section>

<section class="model-example"><strong>Technical Diagram</strong>
<p>High-resolution technical or infographic illustration</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A clean technical diagram showing the layers of a cloud computing architecture with labeled tiers&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/technical-diagram.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/technical-diagram.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-utility-pro&#x27;,
  {
    prompt:
      &#x27;A clean technical diagram showing the layers of a cloud computing architecture with labeled tiers&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-utility-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A clean technical diagram showing the layers of a cloud computing architecture with labeled tiers&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/technical-diagram.png" alt="Technical Diagram">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>size</code></td><td>string</td><td></td></tr><tr><td><code>style</code></td><td>string</td><td></td></tr><tr><td><code>substyle</code></td><td>string</td><td></td></tr><tr><td><code>controls</code></td><td>object</td><td></td></tr><tr><td><code>controls.colors</code></td><td>array</td><td></td></tr><tr><td><code>controls.colors[].rgb</code></td><td>array</td><td>Required.</td></tr><tr><td><code>controls.background_color</code></td><td>object</td><td></td></tr><tr><td><code>controls.background_color.rgb</code></td><td>array</td><td>Required.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/recraft/recraftv4-1-utility-pro/schema-input.json)
- [Output schema](/ai/models/recraft/recraftv4-1-utility-pro/schema-output.json)

