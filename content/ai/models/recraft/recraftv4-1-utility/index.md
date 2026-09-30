---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility/
  description: recraft/recraftv4-1-utility
  full_title: Recraft V4.1 Utility · Cloudflare AI docs
  head_html: <title>Recraft V4.1 Utility · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="recraft/recraftv4-1-utility"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Recraft V4.1 Utility · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="recraft/recraftv4-1-utility"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility/#page","headline":"Recraft V4.1 Utility \u00b7 Cloudflare AI docs","description":"recraft/recraftv4-1-utility","url":"https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/recraft/recraftv4-1-utility/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/recraft.svg" alt="Recraft logo" width="48" height="48">

<h1 id="recraft-v4-1-utility">Recraft V4.1 Utility</h1>

<p><code>recraft/recraftv4-1-utility</code></p>

Recraft V4.1 Utility is a general-purpose text-to-image model balancing quality and flexibility for a wide range of everyday use cases at standard resolution.

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
    &quot;prompt&quot;: &quot;A friendly cartoon robot waving hello against a white background&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/simple-generation.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/simple-generation.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-utility&#x27;,
  { prompt: &#x27;A friendly cartoon robot waving hello against a white background&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-utility&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A friendly cartoon robot waving hello against a white background&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/simple-generation.png" alt="Simple Generation">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Product Mockup</strong>
<p>Generate a product concept image</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A clean product photo of a white ceramic coffee mug on a wooden table&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/product-mockup.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/product-mockup.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-utility&#x27;,
  { prompt: &#x27;A clean product photo of a white ceramic coffee mug on a wooden table&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-utility&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A clean product photo of a white ceramic coffee mug on a wooden table&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/product-mockup.png" alt="Product Mockup">
</section>

<section class="model-example"><strong>Custom Size</strong>
<p>Specify output dimensions</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A simple banner illustration with abstract shapes and warm colors&quot;,
    &quot;size&quot;: &quot;1024x1024&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/custom-size.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/custom-size.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-utility&#x27;,
  {
    prompt: &#x27;A simple banner illustration with abstract shapes and warm colors&#x27;,
    size: &#x27;1024x1024&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-utility&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A simple banner illustration with abstract shapes and warm colors&quot;,
    &quot;size&quot;: &quot;1024x1024&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/custom-size.png" alt="Custom Size">
</section>

<section class="model-example"><strong>With Color Controls</strong>
<p>Guide generation with specific colors</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A flat illustration of a globe with network connections&quot;,
    &quot;controls&quot;: {
      &quot;colors&quot;: [
        {
          &quot;rgb&quot;: [
            30,
            90,
            200
          ]
        },
        {
          &quot;rgb&quot;: [
            255,
            255,
            255
          ]
        }
      ]
    }
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/with-color-controls.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/with-color-controls.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-utility&#x27;,
  {
    prompt: &#x27;A flat illustration of a globe with network connections&#x27;,
    controls: { colors: [{ rgb: [30, 90, 200] }, { rgb: [255, 255, 255] }] },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-utility&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A flat illustration of a globe with network connections&quot;,
    &quot;controls&quot;: {
      &quot;colors&quot;: [
        {
          &quot;rgb&quot;: [
            30,
            90,
            200
          ]
        },
        {
          &quot;rgb&quot;: [
            255,
            255,
            255
          ]
        }
      ]
    }
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/with-color-controls.png" alt="With Color Controls">
</section>

<section class="model-example"><strong>Background Color</strong>
<p>Set a specific background color</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A simple icon of a checkmark inside a circle&quot;,
    &quot;controls&quot;: {
      &quot;background_color&quot;: {
        &quot;rgb&quot;: [
          240,
          248,
          255
        ]
      }
    },
    &quot;size&quot;: &quot;1024x1024&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/background-color.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/background-color.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-utility&#x27;,
  {
    prompt: &#x27;A simple icon of a checkmark inside a circle&#x27;,
    controls: { background_color: { rgb: [240, 248, 255] } },
    size: &#x27;1024x1024&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-utility&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A simple icon of a checkmark inside a circle&quot;,
    &quot;controls&quot;: {
      &quot;background_color&quot;: {
        &quot;rgb&quot;: [
          240,
          248,
          255
        ]
      }
    },
    &quot;size&quot;: &quot;1024x1024&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/background-color.png" alt="Background Color">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>size</code></td><td>string</td><td></td></tr><tr><td><code>style</code></td><td>string</td><td></td></tr><tr><td><code>substyle</code></td><td>string</td><td></td></tr><tr><td><code>controls</code></td><td>object</td><td></td></tr><tr><td><code>controls.colors</code></td><td>array</td><td></td></tr><tr><td><code>controls.colors[].rgb</code></td><td>array</td><td>Required.</td></tr><tr><td><code>controls.background_color</code></td><td>object</td><td></td></tr><tr><td><code>controls.background_color.rgb</code></td><td>array</td><td>Required.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/recraft/recraftv4-1-utility/schema-input.json)
- [Output schema](/ai/models/recraft/recraftv4-1-utility/schema-output.json)

