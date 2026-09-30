---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/xai/grok-imagine-image/
  description: xai/grok-imagine-image
  full_title: Grok Imagine Image · Cloudflare AI docs
  head_html: <title>Grok Imagine Image · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="xai/grok-imagine-image"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/xai/grok-imagine-image/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Grok Imagine Image · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="xai/grok-imagine-image"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/xai/grok-imagine-image/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/xai/grok-imagine-image/#page","headline":"Grok Imagine Image \u00b7 Cloudflare AI docs","description":"xai/grok-imagine-image","url":"https://developers.cloudflare.com/ai/models/xai/grok-imagine-image/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/xai/grok-imagine-image/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/xai.svg" alt="Xai logo" width="48" height="48">

<h1 id="grok-imagine-image">Grok Imagine Image</h1>

<p><code>xai/grok-imagine-image</code></p>

xAI's Grok Imagine image model. Generates and edits images from text and reference-image inputs with configurable aspect ratio and resolution.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://x.ai/legal/terms-of-service">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.02, Per input image: 0.002</td></tr>
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
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-image/simple-generation.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-image/simple-generation.jpeg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-imagine-image&#x27;,
  { prompt: &#x27;A golden retriever puppy playing in autumn leaves&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-imagine-image&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever puppy playing in autumn leaves&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/xai/grok-imagine-image/simple-generation.jpeg" alt="Simple Generation">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Custom Aspect Ratio</strong>
<p>Portrait orientation render at 2K resolution</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures&quot;,
    &quot;aspect_ratio&quot;: &quot;3:4&quot;,
    &quot;resolution&quot;: &quot;2k&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-image/custom-aspect-ratio.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-image/custom-aspect-ratio.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-imagine-image&#x27;,
  {
    prompt:
      &#x27;A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures&#x27;,
    aspect_ratio: &#x27;3:4&#x27;,
    resolution: &#x27;2k&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-imagine-image&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures&quot;,
    &quot;aspect_ratio&quot;: &quot;3:4&quot;,
    &quot;resolution&quot;: &quot;2k&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/xai/grok-imagine-image/custom-aspect-ratio.png" alt="Custom Aspect Ratio">
</section>

<section class="model-example"><strong>Cinematic Landscape</strong>
<p>Widescreen landscape at 2K resolution</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A neon-lit cyberpunk figure standing in the rain beneath a holographic billboard, cinematic lighting&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;2k&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-image/cinematic-landscape.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-imagine-image/cinematic-landscape.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-imagine-image&#x27;,
  {
    prompt:
      &#x27;A neon-lit cyberpunk figure standing in the rain beneath a holographic billboard, cinematic lighting&#x27;,
    aspect_ratio: &#x27;16:9&#x27;,
    resolution: &#x27;2k&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-imagine-image&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A neon-lit cyberpunk figure standing in the rain beneath a holographic billboard, cinematic lighting&quot;,
    &quot;aspect_ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;2k&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/xai/grok-imagine-image/cinematic-landscape.png" alt="Cinematic Landscape">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>n</code></td><td>integer</td><td>Minimum: 1; Maximum: 10</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Values: 1:1, 3:4, 4:3, 9:16, 16:9, 2:3, 3:2, 9:19.5, 19.5:9, 9:20, 20:9, 1:2, 2:1, auto</td></tr><tr><td><code>quality</code></td><td>string</td><td>Values: low, medium, high</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Values: 1k, 2k</td></tr><tr><td><code>response_format</code></td><td>string</td><td>Values: url, b64_json</td></tr><tr><td><code>user</code></td><td>string</td><td></td></tr><tr><td><code>image</code></td><td>object</td><td></td></tr><tr><td><code>image.url</code></td><td>string</td><td>Required.</td></tr><tr><td><code>image.type</code></td><td>string</td><td></td></tr><tr><td><code>images</code></td><td>array</td><td></td></tr><tr><td><code>images[].url</code></td><td>string</td><td>Required.</td></tr><tr><td><code>images[].type</code></td><td>string</td><td></td></tr><tr><td><code>mask</code></td><td>object</td><td></td></tr><tr><td><code>mask.url</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/xai/grok-imagine-image/schema-input.json)
- [Output schema](/ai/models/xai/grok-imagine-image/schema-output.json)

