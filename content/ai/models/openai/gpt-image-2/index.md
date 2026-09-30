---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/openai/gpt-image-2/
  description: openai/gpt-image-2
  full_title: GPT Image 2 · Cloudflare AI docs
  head_html: <title>GPT Image 2 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="openai/gpt-image-2"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/openai/gpt-image-2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="GPT Image 2 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="openai/gpt-image-2"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/openai/gpt-image-2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/openai/gpt-image-2/#page","headline":"GPT Image 2 \u00b7 Cloudflare AI docs","description":"openai/gpt-image-2","url":"https://developers.cloudflare.com/ai/models/openai/gpt-image-2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/openai/gpt-image-2/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="gpt-image-2">GPT Image 2</h1>

<p><code>openai/gpt-image-2</code></p>

OpenAI's next-generation image model that creates and edits images from text prompts, with support for multiple quality levels, sizes, and output formats. Note: transparent backgrounds are not supported — use openai/gpt-image-1.5 for transparent PNGs.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Cached input image tokens (per 1M): 2, Cached input tokens (per 1M): 1.25, Input image tokens (per 1M): 8, Input tokens (per 1M): 5, Output image tokens (per 1M): 30, Output tokens (per 1M): 10</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-image with just a prompt

<section class="model-example"><strong>Simple Generation</strong>
<p>Basic text-to-image with just a prompt</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever puppy playing in autumn leaves&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/simple-generation.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/simple-generation.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-2&#x27;,
  { prompt: &#x27;A golden retriever puppy playing in autumn leaves&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever puppy playing in autumn leaves&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/simple-generation.png" alt="Simple Generation">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>High Quality</strong>
<p>Generate a high-quality detailed image</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures&quot;,
    &quot;quality&quot;: &quot;high&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/high-quality.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/high-quality.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-2&#x27;,
  {
    prompt:
      &#x27;A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures&#x27;,
    quality: &#x27;high&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures&quot;,
    &quot;quality&quot;: &quot;high&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/high-quality.png" alt="High Quality">
</section>

<section class="model-example"><strong>Custom Size</strong>
<p>Generate a portrait-oriented image</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A towering redwood forest with sunbeams filtering through the canopy, misty atmosphere&quot;,
    &quot;size&quot;: &quot;1024x1536&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/custom-size.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/custom-size.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-2&#x27;,
  {
    prompt: &#x27;A towering redwood forest with sunbeams filtering through the canopy, misty atmosphere&#x27;,
    size: &#x27;1024x1536&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A towering redwood forest with sunbeams filtering through the canopy, misty atmosphere&quot;,
    &quot;size&quot;: &quot;1024x1536&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/custom-size.png" alt="Custom Size">
</section>

<section class="model-example"><strong>WebP Output</strong>
<p>Generate an image in WebP format for smaller file size</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A neon-lit cyberpunk cityscape at night with rain-slicked streets and holographic billboards&quot;,
    &quot;output_format&quot;: &quot;webp&quot;,
    &quot;quality&quot;: &quot;high&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/webp-output.webp&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/webp-output.webp&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-2&#x27;,
  {
    prompt:
      &#x27;A neon-lit cyberpunk cityscape at night with rain-slicked streets and holographic billboards&#x27;,
    output_format: &#x27;webp&#x27;,
    quality: &#x27;high&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A neon-lit cyberpunk cityscape at night with rain-slicked streets and holographic billboards&quot;,
    &quot;output_format&quot;: &quot;webp&quot;,
    &quot;quality&quot;: &quot;high&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/webp-output.webp" alt="WebP Output">
</section>

<section class="model-example"><strong>Image Edit</strong>
<p>Edit an existing image by providing it in the images array as base64 (a raw string or a data:image/{png|jpeg|webp};base64,... URI). This routes the call to OpenAI's /v1/images/edits endpoint. The example uses a tiny 32x32 smiley-face PNG - real inputs are the full base64 encoding of your source image.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Transform this cartoon smiley into a photorealistic 3D clay sculpture sitting on a marble pedestal, studio lighting&quot;,
    &quot;images&quot;: [
      &quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&quot;
    ]
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/image-edit.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/image-edit.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-2&#x27;,
  {
    prompt:
      &#x27;Transform this cartoon smiley into a photorealistic 3D clay sculpture sitting on a marble pedestal, studio lighting&#x27;,
    images: [
      &#x27;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&#x27;,
    ],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Transform this cartoon smiley into a photorealistic 3D clay sculpture sitting on a marble pedestal, studio lighting&quot;,
    &quot;images&quot;: [
      &quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&quot;
    ]
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/image-edit.png" alt="Image Edit">
</section>

<section class="model-example"><strong>Multi-Image Edit</strong>
<p>Compose multiple input images by passing up to 16 base64 strings in the images array. The model blends the references; useful for combining subjects, styles, or reference shots. The example pairs a smiley-face PNG with a red ball PNG.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Combine these into a single photorealistic scene: a ceramic smiley-face mug next to a red rubber ball on a sunlit wooden table&quot;,
    &quot;images&quot;: [
      &quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&quot;,
      &quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAhklEQVR42u2XsRHAMAgDNY73nye7OG2KgGUnGCWH76j/oTACPfnhcwIA3AoTGIFXRTADPlqjakYEDJwFWyJLAk/hrAQi4YwEouEjiVuBt+FXCVcgqntvCtjVvTUF7OremkIJlEAJ6Aikf0QSX3H6MpJYx+mBRCKSSYRSiVgucZjInGa/vY5PvB72/7IdMuAAAAAASUVORK5CYII=&quot;
    ]
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/multi-image-edit.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/multi-image-edit.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-2&#x27;,
  {
    prompt:
      &#x27;Combine these into a single photorealistic scene: a ceramic smiley-face mug next to a red rubber ball on a sunlit wooden table&#x27;,
    images: [
      &#x27;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&#x27;,
      &#x27;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAhklEQVR42u2XsRHAMAgDNY73nye7OG2KgGUnGCWH76j/oTACPfnhcwIA3AoTGIFXRTADPlqjakYEDJwFWyJLAk/hrAQi4YwEouEjiVuBt+FXCVcgqntvCtjVvTUF7OremkIJlEAJ6Aikf0QSX3H6MpJYx+mBRCKSSYRSiVgucZjInGa/vY5PvB72/7IdMuAAAAAASUVORK5CYII=&#x27;,
    ],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Combine these into a single photorealistic scene: a ceramic smiley-face mug next to a red rubber ball on a sunlit wooden table&quot;,
    &quot;images&quot;: [
      &quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&quot;,
      &quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAhklEQVR42u2XsRHAMAgDNY73nye7OG2KgGUnGCWH76j/oTACPfnhcwIA3AoTGIFXRTADPlqjakYEDJwFWyJLAk/hrAQi4YwEouEjiVuBt+FXCVcgqntvCtjVvTUF7OremkIJlEAJ6Aikf0QSX3H6MpJYx+mBRCKSSYRSiVgucZjInGa/vY5PvB72/7IdMuAAAAAASUVORK5CYII=&quot;
    ]
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/multi-image-edit.png" alt="Multi-Image Edit">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing the image to generate or edit</td></tr><tr><td><code>images</code></td><td>array</td><td>Input images for image editing, 1-16 entries. Each entry is base64-encoded (raw string or data:image/{png|jpeg|webp};base64,... URI).</td></tr><tr><td><code>quality</code></td><td>string</td><td>Quality of the generated image Values: low, medium, high, auto</td></tr><tr><td><code>size</code></td><td>string</td><td>Size of the generated image Values: 1024x1024, 1024x1536, 1536x1024, auto</td></tr><tr><td><code>background</code></td><td>string</td><td>Background transparency setting. Use transparent for images with no background, opaque for a solid background, or auto to let the model decide. Values: transparent, opaque, auto</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Output format for the generated image Values: png, webp, jpeg</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required. URL to the generated image</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/openai/gpt-image-2/schema-input.json)
- [Output schema](/ai/models/openai/gpt-image-2/schema-output.json)

