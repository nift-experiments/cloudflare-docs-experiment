---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-flare/
  description: openai/gpt-image-2.5-flare
  full_title: GPT Image 2.5 Flare · Cloudflare AI docs
  head_html: <title>GPT Image 2.5 Flare · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="openai/gpt-image-2.5-flare"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-flare/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="GPT Image 2.5 Flare · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="openai/gpt-image-2.5-flare"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-flare/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-flare/#page","headline":"GPT Image 2.5 Flare \u00b7 Cloudflare AI docs","description":"openai/gpt-image-2.5-flare","url":"https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-flare/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/openai/gpt-image-2.5-flare/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="gpt-image-2-5-flare">GPT Image 2.5 Flare</h1>

<p><code>openai/gpt-image-2.5-flare</code></p>

OpenAI's fastest high-quality everyday image generation model. It accepts text and image inputs and produces images with low, medium, high, xhigh, max, and auto quality settings.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Cached input image tokens (per 1M): 3, Cached input tokens (per 1M): 1.25, Input image tokens (per 1M): 8, Input tokens (per 1M): 5, Output image tokens (per 1M): 30</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Create a polished product scene with readable visual hierarchy

<section class="model-example"><strong>Commercial Product Scene</strong>
<p>Create a polished product scene with readable visual hierarchy</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A premium studio product photograph of a translucent orange mechanical keyboard on a cobalt blue acrylic pedestal, a few keys glowing amber, crisp reflections, bold geometric shadows, clean commercial art direction, no logos or readable words&quot;,
    &quot;quality&quot;: &quot;high&quot;,
    &quot;size&quot;: &quot;1024x1024&quot;,
    &quot;output_format&quot;: &quot;jpeg&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/commercial-product-scene.jpg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/commercial-product-scene.jpg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-2.5-flare&#x27;,
  {
    prompt:
      &#x27;A premium studio product photograph of a translucent orange mechanical keyboard on a cobalt blue acrylic pedestal, a few keys glowing amber, crisp reflections, bold geometric shadows, clean commercial art direction, no logos or readable words&#x27;,
    quality: &#x27;high&#x27;,
    size: &#x27;1024x1024&#x27;,
    output_format: &#x27;jpeg&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-2.5-flare&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A premium studio product photograph of a translucent orange mechanical keyboard on a cobalt blue acrylic pedestal, a few keys glowing amber, crisp reflections, bold geometric shadows, clean commercial art direction, no logos or readable words&quot;,
    &quot;quality&quot;: &quot;high&quot;,
    &quot;size&quot;: &quot;1024x1024&quot;,
    &quot;output_format&quot;: &quot;jpeg&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/commercial-product-scene.jpg" alt="Commercial Product Scene">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Environmental Concept Frame</strong>
<p>Generate a wide environmental concept frame</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A wide establishing shot of a hidden mountain library carved into basalt cliffs, tiny figures crossing rope bridges, waterfalls disappearing into mist, late afternoon sun, grounded fantasy concept art with realistic scale&quot;,
    &quot;quality&quot;: &quot;xhigh&quot;,
    &quot;size&quot;: &quot;1536x1024&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/environmental-concept-frame.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/environmental-concept-frame.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-2.5-flare&#x27;,
  {
    prompt:
      &#x27;A wide establishing shot of a hidden mountain library carved into basalt cliffs, tiny figures crossing rope bridges, waterfalls disappearing into mist, late afternoon sun, grounded fantasy concept art with realistic scale&#x27;,
    quality: &#x27;xhigh&#x27;,
    size: &#x27;1536x1024&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-2.5-flare&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A wide establishing shot of a hidden mountain library carved into basalt cliffs, tiny figures crossing rope bridges, waterfalls disappearing into mist, late afternoon sun, grounded fantasy concept art with realistic scale&quot;,
    &quot;quality&quot;: &quot;xhigh&quot;,
    &quot;size&quot;: &quot;1536x1024&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/environmental-concept-frame.png" alt="Environmental Concept Frame">
</section>

<section class="model-example"><strong>Poster Reference Edit</strong>
<p>Transform a reference sketch into a finished illustration</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Reimagine the reference as a vibrant risograph poster for a fictional night market. Keep the central market stall silhouette and hanging lantern arrangement, add layered coral, teal, and navy ink textures, imperfect registration, and a lively crowd rendered as abstract shapes&quot;,
    &quot;images&quot;: [
      &quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&quot;
    ],
    &quot;quality&quot;: &quot;medium&quot;,
    &quot;output_format&quot;: &quot;png&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/poster-reference-edit.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/poster-reference-edit.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-image-2.5-flare&#x27;,
  {
    prompt:
      &#x27;Reimagine the reference as a vibrant risograph poster for a fictional night market. Keep the central market stall silhouette and hanging lantern arrangement, add layered coral, teal, and navy ink textures, imperfect registration, and a lively crowd rendered as abstract shapes&#x27;,
    images: [
      &#x27;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&#x27;,
    ],
    quality: &#x27;medium&#x27;,
    output_format: &#x27;png&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-image-2.5-flare&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Reimagine the reference as a vibrant risograph poster for a fictional night market. Keep the central market stall silhouette and hanging lantern arrangement, add layered coral, teal, and navy ink textures, imperfect registration, and a lively crowd rendered as abstract shapes&quot;,
    &quot;images&quot;: [
      &quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=&quot;
    ],
    &quot;quality&quot;: &quot;medium&quot;,
    &quot;output_format&quot;: &quot;png&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/poster-reference-edit.png" alt="Poster Reference Edit">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing the image to generate or edit</td></tr><tr><td><code>images</code></td><td>array</td><td>Input images for image editing, 1-16 entries. Each entry is base64-encoded (raw string or data:image/{png|jpeg|webp};base64,... URI).</td></tr><tr><td><code>quality</code></td><td>string</td><td>Quality of the generated image Values: low, medium, high, xhigh, max, auto</td></tr><tr><td><code>size</code></td><td>string</td><td>Size of the generated image Values: 1024x1024, 1024x1536, 1536x1024, auto</td></tr><tr><td><code>background</code></td><td>string</td><td>Background transparency setting Values: transparent, opaque, auto</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Output format for the generated image Values: png, webp, jpeg</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required. URL to the generated image</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/openai/gpt-image-2.5-flare/schema-input.json)
- [Output schema](/ai/models/openai/gpt-image-2.5-flare/schema-output.json)

