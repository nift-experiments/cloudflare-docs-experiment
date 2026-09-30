<img src="/assets/upstream/images/workers-ai/recraft.svg" alt="Recraft logo" width="48" height="48">

<h1 id="recraft-v4-pro-svg">Recraft V4 Pro SVG</h1>

<p><code>recraft/recraftv4-pro-vector</code></p>

Generate detailed, production-ready SVG vector graphics from text prompts with fine geometry, scalable to any size for print and design work.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://www.recraft.ai/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.3</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate a scalable vector logo

<section class="model-example"><strong>Logo Design</strong>
<p>Generate a scalable vector logo</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A modern minimalist logo for a cloud computing company, clean geometric shapes&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/logo-design.svg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/logo-design.svg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-pro-vector&#x27;,
  { prompt: &#x27;A modern minimalist logo for a cloud computing company, clean geometric shapes&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-pro-vector&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A modern minimalist logo for a cloud computing company, clean geometric shapes&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/logo-design.svg" alt="Logo Design">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Icon Set</strong>
<p>Generate a vector icon</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A flat design icon of a rocket launching, suitable for a mobile app&quot;,
    &quot;size&quot;: &quot;2048x2048&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/icon-set.svg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/icon-set.svg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-pro-vector&#x27;,
  {
    prompt: &#x27;A flat design icon of a rocket launching, suitable for a mobile app&#x27;,
    size: &#x27;2048x2048&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-pro-vector&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A flat design icon of a rocket launching, suitable for a mobile app&quot;,
    &quot;size&quot;: &quot;2048x2048&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/icon-set.svg" alt="Icon Set">
</section>

<section class="model-example"><strong>Print-Ready Vector</strong>
<p>High-resolution vector for large-format print</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An intricate mandala pattern with floral and geometric elements, highly detailed and symmetrical&quot;,
    &quot;size&quot;: &quot;2048x2048&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/print-ready-vector.svg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/print-ready-vector.svg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-pro-vector&#x27;,
  {
    prompt:
      &#x27;An intricate mandala pattern with floral and geometric elements, highly detailed and symmetrical&#x27;,
    size: &#x27;2048x2048&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-pro-vector&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An intricate mandala pattern with floral and geometric elements, highly detailed and symmetrical&quot;,
    &quot;size&quot;: &quot;2048x2048&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/print-ready-vector.svg" alt="Print-Ready Vector">
</section>

<section class="model-example"><strong>Brand Illustration</strong>
<p>Vector illustration with brand colors</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A vector illustration of a cityscape skyline at sunset with clean lines and flat colors&quot;,
    &quot;controls&quot;: {
      &quot;colors&quot;: [
        {
          &quot;rgb&quot;: [
            255,
            87,
            51
          ]
        },
        {
          &quot;rgb&quot;: [
            41,
            50,
            65
          ]
        },
        {
          &quot;rgb&quot;: [
            239,
            239,
            239
          ]
        }
      ]
    }
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/brand-illustration.svg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/brand-illustration.svg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-pro-vector&#x27;,
  {
    prompt: &#x27;A vector illustration of a cityscape skyline at sunset with clean lines and flat colors&#x27;,
    controls: { colors: [{ rgb: [255, 87, 51] }, { rgb: [41, 50, 65] }, { rgb: [239, 239, 239] }] },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-pro-vector&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A vector illustration of a cityscape skyline at sunset with clean lines and flat colors&quot;,
    &quot;controls&quot;: {
      &quot;colors&quot;: [
        {
          &quot;rgb&quot;: [
            255,
            87,
            51
          ]
        },
        {
          &quot;rgb&quot;: [
            41,
            50,
            65
          ]
        },
        {
          &quot;rgb&quot;: [
            239,
            239,
            239
          ]
        }
      ]
    }
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/brand-illustration.svg" alt="Brand Illustration">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>size</code></td><td>string</td><td></td></tr><tr><td><code>style</code></td><td>string</td><td></td></tr><tr><td><code>substyle</code></td><td>string</td><td></td></tr><tr><td><code>controls</code></td><td>object</td><td></td></tr><tr><td><code>controls.colors</code></td><td>array</td><td></td></tr><tr><td><code>controls.colors[].rgb</code></td><td>array</td><td>Required.</td></tr><tr><td><code>controls.background_color</code></td><td>object</td><td></td></tr><tr><td><code>controls.background_color.rgb</code></td><td>array</td><td>Required.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/recraft/recraftv4-pro-vector/schema-input.json)
- [Output schema](/ai/models/recraft/recraftv4-pro-vector/schema-output.json)

