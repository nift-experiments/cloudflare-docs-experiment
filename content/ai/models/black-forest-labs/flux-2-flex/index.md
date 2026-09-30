---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-flex/
  description: black-forest-labs/flux-2-flex
  full_title: FLUX.2 [flex] · Cloudflare AI docs
  head_html: <title>FLUX.2 [flex] · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="black-forest-labs/flux-2-flex"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-flex/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="FLUX.2 [flex] · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="black-forest-labs/flux-2-flex"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-flex/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-flex/#page","headline":"FLUX.2 [flex] \u00b7 Cloudflare AI docs","description":"black-forest-labs/flux-2-flex","url":"https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-flex/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/black-forest-labs/flux-2-flex/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/black-forest-labs.svg" alt="Black-Forest-Labs logo" width="48" height="48">

<h1 id="flux-2-flex">FLUX.2 [flex]</h1>

<p><code>black-forest-labs/flux-2-flex</code></p>

FLUX.2 [flex] is Black Forest Labs' fine-grained control variant of FLUX.2 — exposes tunable inference steps, guidance, and prompt upsampling for typography-heavy and production workflows.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://blackforestlabs.ai/terms-of-service/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>First output megapixel: 0.05, Per additional output megapixel: 0.05, Per input megapixel: 0.05</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Typography-heavy advertising layout — flex is tuned for crisp text rendering

<section class="model-example"><strong>Typography &amp; Design</strong>
<p>Typography-heavy advertising layout — flex is tuned for crisp text rendering</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Samsung Galaxy S25 Ultra product advertisement, &#x27;Ultra-strong titanium&#x27; headline, close-up of phone edge showing titanium frame, dark gradient background, clean minimalist tech aesthetic&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/typography-design.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/typography-design.jpeg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-2-flex&#x27;,
  {
    prompt:
      &quot;Samsung Galaxy S25 Ultra product advertisement, &#x27;Ultra-strong titanium&#x27; headline, close-up of phone edge showing titanium frame, dark gradient background, clean minimalist tech aesthetic&quot;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-2-flex&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Samsung Galaxy S25 Ultra product advertisement, &#x27;\&#x27;&#x27;Ultra-strong titanium&#x27;\&#x27;&#x27; headline, close-up of phone edge showing titanium frame, dark gradient background, clean minimalist tech aesthetic&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/typography-design.jpeg" alt="Typography &amp; Design">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>High Detail Generation</strong>
<p>Crank steps and guidance for maximum detail when latency is not the priority</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar&quot;,
    &quot;guidance&quot;: 7.5,
    &quot;steps&quot;: 50
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/high-detail-generation.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/high-detail-generation.jpeg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-2-flex&#x27;,
  {
    prompt: &#x27;A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar&#x27;,
    guidance: 7.5,
    steps: 50,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-2-flex&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar&quot;,
    &quot;guidance&quot;: 7.5,
    &quot;steps&quot;: 50
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/high-detail-generation.jpeg" alt="High Detail Generation">
</section>

<section class="model-example"><strong>Fast Draft</strong>
<p>Fast draft with prompt upsampling disabled — preserves the literal prompt</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A simple line sketch of a mountain landscape&quot;,
    &quot;prompt_upsampling&quot;: false,
    &quot;steps&quot;: 10
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/fast-draft.jpeg&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/fast-draft.jpeg&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;black-forest-labs/flux-2-flex&#x27;,
  { prompt: &#x27;A simple line sketch of a mountain landscape&#x27;, prompt_upsampling: false, steps: 10 },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;black-forest-labs/flux-2-flex&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A simple line sketch of a mountain landscape&quot;,
    &quot;prompt_upsampling&quot;: false,
    &quot;steps&quot;: 10
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/fast-draft.jpeg" alt="Fast Draft">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt for image generation or editing.</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Optional seed for reproducible generation. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>width</code></td><td>integer</td><td>Width of the generated image in pixels (minimum 64). Omit to let BFL pick. Minimum: 64; Maximum: 9007199254740991</td></tr><tr><td><code>height</code></td><td>integer</td><td>Height of the generated image in pixels (minimum 64). Omit to let BFL pick. Minimum: 64; Maximum: 9007199254740991</td></tr><tr><td><code>safety_tolerance</code></td><td>integer</td><td>Tolerance for input/output moderation. 0 is the strictest, 5 the most permissive. Defaults to 2. Minimum: 0; Maximum: 5</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Output image format. Defaults to jpeg. Values: jpeg, png, webp</td></tr><tr><td><code>input_images</code></td><td>array</td><td>Up to 8 reference images for editing or multi-image composition. Each entry is an HTTPS URL or a data:image/...;base64,... URI.</td></tr><tr><td><code>prompt_upsampling</code></td><td>boolean</td><td>Whether BFL should expand short prompts before generation. Defaults to true on flex.</td></tr><tr><td><code>guidance</code></td><td>number</td><td>Classifier-free guidance scale (1.5–10). Higher values follow the prompt more strictly at the cost of realism. Minimum: 1.5; Maximum: 10</td></tr><tr><td><code>steps</code></td><td>integer</td><td>Number of denoising steps (1–50). Higher steps yield more detail at the cost of latency. Minimum: 1; Maximum: 50</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required. URL to the generated image</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/black-forest-labs/flux-2-flex/schema-input.json)
- [Output schema](/ai/models/black-forest-labs/flux-2-flex/schema-output.json)

