---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/bytedance/seedream-5-lite/
  description: bytedance/seedream-5-lite
  full_title: Seedream 5 Lite · Cloudflare AI docs
  head_html: <title>Seedream 5 Lite · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="bytedance/seedream-5-lite"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/bytedance/seedream-5-lite/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Seedream 5 Lite · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="bytedance/seedream-5-lite"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/bytedance/seedream-5-lite/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/bytedance/seedream-5-lite/#page","headline":"Seedream 5 Lite \u00b7 Cloudflare AI docs","description":"bytedance/seedream-5-lite","url":"https://developers.cloudflare.com/ai/models/bytedance/seedream-5-lite/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/bytedance/seedream-5-lite/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/bytedance.svg" alt="Bytedance logo" width="48" height="48">

<h1 id="seedream-5-lite">Seedream 5 Lite</h1>

<p><code>bytedance/seedream-5-lite</code></p>

Seedream 5 Lite is a lighter, faster version of the Seedream 5 family with multi-reference and batch generation support.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.035</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-image generation

<section class="model-example"><strong>Simple Generation</strong>
<p>Basic text-to-image generation</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cute robot watering plants in a sunny greenhouse&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/simple-generation-0.jpeg&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://ark-acg-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-5-0/021776405291656e8ad6f8fac80a9b78040141fa10ae51dc262e8_0.jpeg&quot;
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-5-lite&#x27;,
  { prompt: &#x27;A cute robot watering plants in a sunny greenhouse&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-5-lite&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cute robot watering plants in a sunny greenhouse&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/simple-generation-0.jpeg" alt="Simple Generation">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>High Resolution PNG</strong>
<p>3K quality with PNG output</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed technical blueprint of a futuristic spacecraft with annotations and measurements&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;output_format&quot;: &quot;png&quot;,
    &quot;size&quot;: &quot;3K&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/high-resolution-png-0.png&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://ark-acg-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-5-0/021776405293188e8ad6f8fac80a9b78040141fa10ae51d8ac521_0.png&quot;
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-5-lite&#x27;,
  {
    prompt:
      &#x27;A detailed technical blueprint of a futuristic spacecraft with annotations and measurements&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    output_format: &#x27;png&#x27;,
    size: &#x27;3K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-5-lite&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed technical blueprint of a futuristic spacecraft with annotations and measurements&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;output_format&quot;: &quot;png&quot;,
    &quot;size&quot;: &quot;3K&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/high-resolution-png-0.png" alt="High Resolution PNG">
</section>

<section class="model-example"><strong>Portrait Photo</strong>
<p>JPEG output for photographs</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A professional headshot portrait with soft studio lighting and a neutral gray background&quot;,
    &quot;aspect_ratio&quot;: &quot;3:4&quot;,
    &quot;output_format&quot;: &quot;jpeg&quot;,
    &quot;size&quot;: &quot;2K&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/portrait-photo-0.jpeg&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://ark-acg-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-5-0/021776405322247e8ad6f8fac80a9b78040141fa10ae51db518ee_0.jpeg&quot;
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-5-lite&#x27;,
  {
    prompt:
      &#x27;A professional headshot portrait with soft studio lighting and a neutral gray background&#x27;,
    aspect_ratio: &#x27;3:4&#x27;,
    output_format: &#x27;jpeg&#x27;,
    size: &#x27;2K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-5-lite&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A professional headshot portrait with soft studio lighting and a neutral gray background&quot;,
    &quot;aspect_ratio&quot;: &quot;3:4&quot;,
    &quot;output_format&quot;: &quot;jpeg&quot;,
    &quot;size&quot;: &quot;2K&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/portrait-photo-0.jpeg" alt="Portrait Photo">
</section>

<section class="model-example"><strong>Sequential Comic</strong>
<p>Generate sequential comic panels</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A four-panel comic strip showing a cat discovering a cardboard box and deciding to sit in it&quot;,
    &quot;aspect_ratio&quot;: &quot;4:3&quot;,
    &quot;max_images&quot;: 4,
    &quot;sequential_image_generation&quot;: &quot;auto&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/sequential-comic-0.jpeg&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://ark-acg-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-5-0/0217764053440971386b9a8ed856c57501cfa946ce34c987bb335_0.jpeg&quot;
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-5-lite&#x27;,
  {
    prompt:
      &#x27;A four-panel comic strip showing a cat discovering a cardboard box and deciding to sit in it&#x27;,
    aspect_ratio: &#x27;4:3&#x27;,
    max_images: 4,
    sequential_image_generation: &#x27;auto&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-5-lite&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A four-panel comic strip showing a cat discovering a cardboard box and deciding to sit in it&quot;,
    &quot;aspect_ratio&quot;: &quot;4:3&quot;,
    &quot;max_images&quot;: 4,
    &quot;sequential_image_generation&quot;: &quot;auto&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/sequential-comic-0.jpeg" alt="Sequential Comic">
</section>

<section class="model-example"><strong>Image Variation</strong>
<p>Create variation from reference</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Create a variation of this image in a watercolor painting style&quot;,
    &quot;aspect_ratio&quot;: &quot;match_input_image&quot;,
    &quot;image_input&quot;: [
      &quot;https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg&quot;
    ],
    &quot;size&quot;: &quot;2K&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/image-variation-0.jpeg&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://ark-acg-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-5-0/0217764053505731386b9a8ed856c57501cfa946ce34c989ba40c_0.jpeg&quot;
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-5-lite&#x27;,
  {
    prompt: &#x27;Create a variation of this image in a watercolor painting style&#x27;,
    aspect_ratio: &#x27;match_input_image&#x27;,
    image_input: [
      &#x27;https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg&#x27;,
    ],
    size: &#x27;2K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-5-lite&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Create a variation of this image in a watercolor painting style&quot;,
    &quot;aspect_ratio&quot;: &quot;match_input_image&quot;,
    &quot;image_input&quot;: [
      &quot;https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg&quot;
    ],
    &quot;size&quot;: &quot;2K&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/image-variation-0.jpeg" alt="Image Variation">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>image_input</code></td><td>array</td><td></td></tr><tr><td><code>size</code></td><td>string</td><td>Values: 2K, 3K</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Values: match_input_image, 1:1, 4:3, 3:4, 16:9, 9:16, 3:2, 2:3, 21:9</td></tr><tr><td><code>sequential_image_generation</code></td><td>string</td><td>Values: disabled, auto</td></tr><tr><td><code>max_images</code></td><td>integer</td><td>Minimum: 1; Maximum: 15</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Values: png, jpeg</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>images</code></td><td>array</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/bytedance/seedream-5-lite/schema-input.json)
- [Output schema](/ai/models/bytedance/seedream-5-lite/schema-output.json)

