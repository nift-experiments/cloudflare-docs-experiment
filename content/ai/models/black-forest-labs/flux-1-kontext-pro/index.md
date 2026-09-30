---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-pro/
  description: black-forest-labs/flux-1-kontext-pro
  full_title: FLUX.1 Kontext [pro] · Cloudflare AI docs
  head_html: <title>FLUX.1 Kontext [pro] · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="black-forest-labs/flux-1-kontext-pro"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-pro/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="FLUX.1 Kontext [pro] · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="black-forest-labs/flux-1-kontext-pro"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-pro/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-pro/#page","headline":"FLUX.1 Kontext [pro] \u00b7 Cloudflare AI docs","description":"black-forest-labs/flux-1-kontext-pro","url":"https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-pro/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/black-forest-labs/flux-1-kontext-pro/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/black-forest-labs.svg" alt="Black-Forest-Labs logo" width="48" height="48">

<h1 id="flux-1-kontext-pro">FLUX.1 Kontext [pro]</h1>

<p><code>black-forest-labs/flux-1-kontext-pro</code></p>

FLUX.1 Kontext [pro] creates and edits images from text prompts with strong character and style consistency.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://blackforestlabs.ai/terms-of-service/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.04</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Create an image from a detailed text prompt.

<section class="model-example"><strong>Text to Image</strong>
<p>Create an image from a detailed text prompt.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A small furry elephant pet looks out from a cat house&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-pro/text-to-image.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-pro/text-to-image.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-1-kontext-pro&#x27;,
  { prompt: &#x27;A small furry elephant pet looks out from a cat house&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-1-kontext-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A small furry elephant pet looks out from a cat house&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-pro/text-to-image.png" alt="Text to Image">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Wide Cinematic Image</strong>
<p>Generate a cinematic landscape using a wide aspect ratio.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A remote gas station swallowed by crimson fog, green glow from overhead lights staining the asphalt, cinematic wide shot&quot;,
    &quot;input_image&quot;: &quot;https://cdn.sanity.io/images/gsvmb6gz/production/3ae6ee032b85373b84934574f3ac3bb2fb792d64-2048x1365.jpg&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;output_format&quot;: &quot;jpeg&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-pro/wide-cinematic-image.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-pro/wide-cinematic-image.jpeg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-1-kontext-pro&#x27;,
  {
    prompt:
      &#x27;A remote gas station swallowed by crimson fog, green glow from overhead lights staining the asphalt, cinematic wide shot&#x27;,
    input_image:
      &#x27;https://cdn.sanity.io/images/gsvmb6gz/production/3ae6ee032b85373b84934574f3ac3bb2fb792d64-2048x1365.jpg&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    output_format: &#x27;jpeg&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-1-kontext-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A remote gas station swallowed by crimson fog, green glow from overhead lights staining the asphalt, cinematic wide shot&quot;,
    &quot;input_image&quot;: &quot;https://cdn.sanity.io/images/gsvmb6gz/production/3ae6ee032b85373b84934574f3ac3bb2fb792d64-2048x1365.jpg&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;output_format&quot;: &quot;jpeg&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-pro/wide-cinematic-image.jpeg" alt="Wide Cinematic Image">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt for image generation or editing.</td></tr><tr><td><code>input_image</code></td><td>['string', 'null']</td><td>Optional base64 encoded image or URL to edit.</td></tr><tr><td><code>aspect_ratio</code></td><td>['string', 'null']</td><td>Output aspect ratio, from 3:7 to 7:3. Defaults to 1:1.</td></tr><tr><td><code>seed</code></td><td>integer or null</td><td>Optional seed for reproducible generation.</td></tr><tr><td><code>prompt_upsampling</code></td><td>boolean</td><td>Whether to upsample the prompt. Defaults to false.</td></tr><tr><td><code>safety_tolerance</code></td><td>integer</td><td>Moderation tolerance. 0 is strictest and 6 is most permissive. Minimum: 0; Maximum: 6</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Output image format. Defaults to jpeg. Values: jpeg, png</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required. URL to the generated image</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/black-forest-labs/flux-1-kontext-pro/schema-input.json)
- [Output schema](/ai/models/black-forest-labs/flux-1-kontext-pro/schema-output.json)

