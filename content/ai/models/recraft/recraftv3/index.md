---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/recraft/recraftv3/
  description: recraft/recraftv3
  full_title: Recraft V3 · Cloudflare AI docs
  head_html: <title>Recraft V3 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="recraft/recraftv3"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/recraft/recraftv3/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Recraft V3 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="recraft/recraftv3"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/recraft/recraftv3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/recraft/recraftv3/#page","headline":"Recraft V3 \u00b7 Cloudflare AI docs","description":"recraft/recraftv3","url":"https://developers.cloudflare.com/ai/models/recraft/recraftv3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/recraft/recraftv3/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/recraft.svg" alt="Recraft logo" width="48" height="48">

<h1 id="recraft-v3">Recraft V3</h1>

<p><code>recraft/recraftv3</code></p>

Recraft V3 is the previous-generation text-to-image model from Recraft, well-suited to design-quality compositions, brand-aware imagery, and accurate text rendering.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://www.recraft.ai/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.04</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-image with just a prompt

<section class="model-example"><strong>Simple Generation</strong>
<p>Basic text-to-image with just a prompt</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A minimalist logo of a mountain range with a sun rising behind it&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv3/simple-generation.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv3/simple-generation.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv3&#x27;,
  { prompt: &#x27;A minimalist logo of a mountain range with a sun rising behind it&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv3&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A minimalist logo of a mountain range with a sun rising behind it&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/recraft/recraftv3/simple-generation.png" alt="Simple Generation">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Scene Composition</strong>
<p>Generate a complex compositional scene</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cozy cabin in the woods surrounded by tall pine trees, smoke rising from the chimney&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv3/scene-composition.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv3/scene-composition.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv3&#x27;,
  {
    prompt: &#x27;A cozy cabin in the woods surrounded by tall pine trees, smoke rising from the chimney&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv3&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cozy cabin in the woods surrounded by tall pine trees, smoke rising from the chimney&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/recraft/recraftv3/scene-composition.png" alt="Scene Composition">
</section>

<section class="model-example"><strong>Custom Size</strong>
<p>Specify output dimensions</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A flat illustration of a workspace with a laptop, coffee cup, and potted plant&quot;,
    &quot;size&quot;: &quot;1024x1024&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv3/custom-size.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv3/custom-size.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv3&#x27;,
  {
    prompt: &#x27;A flat illustration of a workspace with a laptop, coffee cup, and potted plant&#x27;,
    size: &#x27;1024x1024&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv3&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A flat illustration of a workspace with a laptop, coffee cup, and potted plant&quot;,
    &quot;size&quot;: &quot;1024x1024&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/recraft/recraftv3/custom-size.png" alt="Custom Size">
</section>

<section class="model-example"><strong>With Color Controls</strong>
<p>Guide generation with specific brand colors</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An abstract geometric pattern suitable for a tech company brand identity&quot;,
    &quot;controls&quot;: {
      &quot;colors&quot;: [
        {
          &quot;rgb&quot;: [
            255,
            107,
            53
          ]
        },
        {
          &quot;rgb&quot;: [
            0,
            43,
            91
          ]
        }
      ]
    }
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv3/with-color-controls.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv3/with-color-controls.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv3&#x27;,
  {
    prompt: &#x27;An abstract geometric pattern suitable for a tech company brand identity&#x27;,
    controls: { colors: [{ rgb: [255, 107, 53] }, { rgb: [0, 43, 91] }] },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv3&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An abstract geometric pattern suitable for a tech company brand identity&quot;,
    &quot;controls&quot;: {
      &quot;colors&quot;: [
        {
          &quot;rgb&quot;: [
            255,
            107,
            53
          ]
        },
        {
          &quot;rgb&quot;: [
            0,
            43,
            91
          ]
        }
      ]
    }
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/recraft/recraftv3/with-color-controls.png" alt="With Color Controls">
</section>

<section class="model-example"><strong>Background Color</strong>
<p>Set a specific background color</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A clean icon of a lightning bolt&quot;,
    &quot;controls&quot;: {
      &quot;background_color&quot;: {
        &quot;rgb&quot;: [
          245,
          245,
          245
        ]
      }
    },
    &quot;size&quot;: &quot;1024x1024&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv3/background-color.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/recraft/recraftv3/background-color.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv3&#x27;,
  {
    prompt: &#x27;A clean icon of a lightning bolt&#x27;,
    controls: { background_color: { rgb: [245, 245, 245] } },
    size: &#x27;1024x1024&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv3&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A clean icon of a lightning bolt&quot;,
    &quot;controls&quot;: {
      &quot;background_color&quot;: {
        &quot;rgb&quot;: [
          245,
          245,
          245
        ]
      }
    },
    &quot;size&quot;: &quot;1024x1024&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/recraft/recraftv3/background-color.png" alt="Background Color">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>size</code></td><td>string</td><td></td></tr><tr><td><code>style</code></td><td>string</td><td></td></tr><tr><td><code>substyle</code></td><td>string</td><td></td></tr><tr><td><code>controls</code></td><td>object</td><td></td></tr><tr><td><code>controls.colors</code></td><td>array</td><td></td></tr><tr><td><code>controls.colors[].rgb</code></td><td>array</td><td>Required.</td></tr><tr><td><code>controls.background_color</code></td><td>object</td><td></td></tr><tr><td><code>controls.background_color.rgb</code></td><td>array</td><td>Required.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/recraft/recraftv3/schema-input.json)
- [Output schema](/ai/models/recraft/recraftv3/schema-output.json)

