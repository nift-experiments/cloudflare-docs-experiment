---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/google/nano-banana/
  description: google/nano-banana
  full_title: Nano Banana · Cloudflare AI docs
  head_html: <title>Nano Banana · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="google/nano-banana"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/google/nano-banana/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Nano Banana · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="google/nano-banana"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/google/nano-banana/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/google/nano-banana/#page","headline":"Nano Banana \u00b7 Cloudflare AI docs","description":"google/nano-banana","url":"https://developers.cloudflare.com/ai/models/google/nano-banana/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/google/nano-banana/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="nano-banana">Nano Banana</h1>

<p><code>google/nano-banana</code></p>

Google's fast image generation model producing high-quality images from text prompts.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 0.3, Output tokens (per 1M): 30, Cached input tokens (per 1M): 0.03, Cache creation tokens (per 1M): 0.083333</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Interior scene with warm lighting and a cat

<section class="model-example"><strong>Cozy Coffee Shop</strong>
<p>Interior scene with warm lighting and a cat</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cozy coffee shop interior with warm lighting, plants hanging from the ceiling, and a cat sleeping on a velvet armchair by the window&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/cozy-coffee-shop.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/cozy-coffee-shop.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana&#x27;,
  {
    prompt:
      &#x27;A cozy coffee shop interior with warm lighting, plants hanging from the ceiling, and a cat sleeping on a velvet armchair by the window&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cozy coffee shop interior with warm lighting, plants hanging from the ceiling, and a cat sleeping on a velvet armchair by the window&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/cozy-coffee-shop.png" alt="Cozy Coffee Shop">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Vintage Tokyo Poster</strong>
<p>Retro travel poster style illustration</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A vintage travel poster for Tokyo, Japan in the style of 1960s airline advertisements, with Mount Fuji in the background and cherry blossoms framing the scene&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/vintage-tokyo-poster.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/vintage-tokyo-poster.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana&#x27;,
  {
    prompt:
      &#x27;A vintage travel poster for Tokyo, Japan in the style of 1960s airline advertisements, with Mount Fuji in the background and cherry blossoms framing the scene&#x27;,
    aspect_ratio: &#x27;9:16&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A vintage travel poster for Tokyo, Japan in the style of 1960s airline advertisements, with Mount Fuji in the background and cherry blossoms framing the scene&quot;,
    &quot;aspect_ratio&quot;: &quot;9:16&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/vintage-tokyo-poster.png" alt="Vintage Tokyo Poster">
</section>

<section class="model-example"><strong>Dewdrops Macro</strong>
<p>Photorealistic macro photography</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A photorealistic macro shot of dewdrops on a spider web at sunrise, with rainbow light refracting through each droplet&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/dewdrops-macro.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/dewdrops-macro.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana&#x27;,
  {
    prompt:
      &#x27;A photorealistic macro shot of dewdrops on a spider web at sunrise, with rainbow light refracting through each droplet&#x27;,
    aspect_ratio: &#x27;1:1&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A photorealistic macro shot of dewdrops on a spider web at sunrise, with rainbow light refracting through each droplet&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/dewdrops-macro.png" alt="Dewdrops Macro">
</section>

<section class="model-example"><strong>Pixel Art Marketplace</strong>
<p>Isometric pixel art scene</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An isometric pixel art scene of a bustling medieval marketplace with merchants, knights, and a dragon perched on the town hall roof&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/pixel-art-marketplace.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/pixel-art-marketplace.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana&#x27;,
  {
    prompt:
      &#x27;An isometric pixel art scene of a bustling medieval marketplace with merchants, knights, and a dragon perched on the town hall roof&#x27;,
    aspect_ratio: &#x27;1:1&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An isometric pixel art scene of a bustling medieval marketplace with merchants, knights, and a dragon perched on the town hall roof&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/pixel-art-marketplace.png" alt="Pixel Art Marketplace">
</section>

<section class="model-example"><strong>High Resolution Landscape</strong>
<p>Generate a high-resolution 4K landscape image</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A dramatic mountain landscape at golden hour with snow-capped peaks and a crystal clear alpine lake&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;image_size&quot;: &quot;4K&quot;,
    &quot;output_format&quot;: &quot;png&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/high-resolution-landscape.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/high-resolution-landscape.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/nano-banana&#x27;,
  {
    prompt:
      &#x27;A dramatic mountain landscape at golden hour with snow-capped peaks and a crystal clear alpine lake&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    image_size: &#x27;4K&#x27;,
    output_format: &#x27;png&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/nano-banana&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A dramatic mountain landscape at golden hour with snow-capped peaks and a crystal clear alpine lake&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;image_size&quot;: &quot;4K&quot;,
    &quot;output_format&quot;: &quot;png&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana/high-resolution-landscape.png" alt="High Resolution Landscape">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>image_input</code></td><td>array</td><td></td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Values: 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Values: jpg, png, webp</td></tr><tr><td><code>image_size</code></td><td>string</td><td>Values: 1K, 2K, 4K</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/google/nano-banana/schema-input.json)
- [Output schema](/ai/models/google/nano-banana/schema-output.json)

