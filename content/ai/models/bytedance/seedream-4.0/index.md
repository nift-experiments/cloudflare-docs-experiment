---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/bytedance/seedream-4.0/
  description: bytedance/seedream-4.0
  full_title: Seedream 4.0 · Cloudflare AI docs
  head_html: <title>Seedream 4.0 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="bytedance/seedream-4.0"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/bytedance/seedream-4.0/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Seedream 4.0 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="bytedance/seedream-4.0"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/bytedance/seedream-4.0/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/bytedance/seedream-4.0/#page","headline":"Seedream 4.0 \u00b7 Cloudflare AI docs","description":"bytedance/seedream-4.0","url":"https://developers.cloudflare.com/ai/models/bytedance/seedream-4.0/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/bytedance/seedream-4.0/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/bytedance.svg" alt="Bytedance logo" width="48" height="48">

<h1 id="seedream-4-0">Seedream 4.0</h1>

<p><code>bytedance/seedream-4.0</code></p>

Seedream 4.0 is ByteDance's image creation model that combines text-to-image generation and image editing into a single architecture, offering fast, high-resolution output up to 4K.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.03</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-image generation

<section class="model-example"><strong>Simple Generation</strong>
<p>Basic text-to-image generation</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A serene mountain lake surrounded by pine trees at dawn&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.0/simple-generation.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-0/021776387438887c5f50319cb4d4388d7836967b82aebe5227f8d_0.jpeg&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-4.0&#x27;,
  { prompt: &#x27;A serene mountain lake surrounded by pine trees at dawn&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-4.0&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A serene mountain lake surrounded by pine trees at dawn&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.0/simple-generation.jpeg" alt="Simple Generation">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>High Resolution</strong>
<p>4K quality image generation</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed steampunk mechanical owl with brass gears and copper feathers, intricate clockwork visible&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;size&quot;: &quot;4K&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.0/high-resolution.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-0/021776387448153c5f50319cb4d4388d7836967b82aebe5807cbc_0.jpeg&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-4.0&#x27;,
  {
    prompt:
      &#x27;A detailed steampunk mechanical owl with brass gears and copper feathers, intricate clockwork visible&#x27;,
    aspect_ratio: &#x27;1:1&#x27;,
    size: &#x27;4K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-4.0&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed steampunk mechanical owl with brass gears and copper feathers, intricate clockwork visible&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;size&quot;: &quot;4K&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.0/high-resolution.jpeg" alt="High Resolution">
</section>

<section class="model-example"><strong>Widescreen Landscape</strong>
<p>Cinematic aspect ratio image</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A vast alien desert landscape with two suns setting on the horizon, ancient ruins in the foreground&quot;,
    &quot;aspect_ratio&quot;: &quot;21:9&quot;,
    &quot;size&quot;: &quot;2K&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.0/widescreen-landscape.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-0/021776387469085c5f50319cb4d4388d7836967b82aebe5dcf17e_0.jpeg&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-4.0&#x27;,
  {
    prompt:
      &#x27;A vast alien desert landscape with two suns setting on the horizon, ancient ruins in the foreground&#x27;,
    aspect_ratio: &#x27;21:9&#x27;,
    size: &#x27;2K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-4.0&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A vast alien desert landscape with two suns setting on the horizon, ancient ruins in the foreground&quot;,
    &quot;aspect_ratio&quot;: &quot;21:9&quot;,
    &quot;size&quot;: &quot;2K&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.0/widescreen-landscape.jpeg" alt="Widescreen Landscape">
</section>

<section class="model-example"><strong>Portrait Format</strong>
<p>Vertical image for portraits</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An elegant Art Deco poster featuring a jazz singer under a spotlight&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;enhance_prompt&quot;: true
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.0/portrait-format.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-0/021776387475078c5f50319cb4d4388d7836967b82aebe5e6ec81_0.jpeg&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-4.0&#x27;,
  {
    prompt: &#x27;An elegant Art Deco poster featuring a jazz singer under a spotlight&#x27;,
    aspect_ratio: &#x27;9:16&#x27;,
    enhance_prompt: true,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-4.0&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An elegant Art Deco poster featuring a jazz singer under a spotlight&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;,
    &quot;enhance_prompt&quot;: true
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.0/portrait-format.jpeg" alt="Portrait Format">
</section>

<section class="model-example"><strong>Detailed 4K</strong>
<p>High-resolution detailed botanical illustration</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed botanical illustration of exotic tropical flowers&quot;,
    &quot;aspect_ratio&quot;: &quot;3:4&quot;,
    &quot;size&quot;: &quot;4K&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.0/detailed-4k.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-0/021776441662380e1f2c28e220bf76d8a56e2a46eaa08e982d37f_0.jpeg&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-4.0&#x27;,
  {
    prompt: &#x27;A detailed botanical illustration of exotic tropical flowers&#x27;,
    aspect_ratio: &#x27;3:4&#x27;,
    size: &#x27;4K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-4.0&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed botanical illustration of exotic tropical flowers&quot;,
    &quot;aspect_ratio&quot;: &quot;3:4&quot;,
    &quot;size&quot;: &quot;4K&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.0/detailed-4k.jpeg" alt="Detailed 4K">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>size</code></td><td>string</td><td>Values: 1K, 2K, 4K, custom</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Values: match_input_image, 1:1, 4:3, 3:4, 16:9, 9:16, 3:2, 2:3, 21:9</td></tr><tr><td><code>width</code></td><td>integer</td><td>Minimum: 1024; Maximum: 4096</td></tr><tr><td><code>height</code></td><td>integer</td><td>Minimum: 1024; Maximum: 4096</td></tr><tr><td><code>enhance_prompt</code></td><td>boolean</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/bytedance/seedream-4.0/schema-input.json)
- [Output schema](/ai/models/bytedance/seedream-4.0/schema-output.json)

