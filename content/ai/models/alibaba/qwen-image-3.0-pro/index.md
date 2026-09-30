---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/
  description: alibaba/qwen-image-3.0-pro
  full_title: Qwen Image 3.0 Pro · Cloudflare AI docs
  head_html: <title>Qwen Image 3.0 Pro · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="alibaba/qwen-image-3.0-pro"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Qwen Image 3.0 Pro · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="alibaba/qwen-image-3.0-pro"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/#page","headline":"Qwen Image 3.0 Pro \u00b7 Cloudflare AI docs","description":"alibaba/qwen-image-3.0-pro","url":"https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/alibaba/qwen-image-3.0-pro/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/alibaba.svg" alt="Alibaba logo" width="48" height="48">

<h1 id="qwen-image-3-0-pro">Qwen Image 3.0 Pro</h1>

<p><code>alibaba/qwen-image-3.0-pro</code></p>

Alibaba's Qwen Image 3.0 Pro generates images from text prompts with a focus on complex layout generation, small-text precision, and multilingual font rendering. Supports up to 6 image variants per call, negative prompts, seed control, and optional prompt rewriting.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://www.alibabacloud.com/help/en/legal">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.04, output_size_1k: 0.04, output_size_2k: 0.07, Default (per second): 0.04</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-image generation

<section class="model-example"><strong>Simple Generation</strong>
<p>Basic text-to-image generation</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever puppy playing in autumn leaves&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/simple-generation.png&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/simple-generation.png&quot;
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/qwen-image-3.0-pro&#x27;,
  { prompt: &#x27;A golden retriever puppy playing in autumn leaves&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/qwen-image-3.0-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever puppy playing in autumn leaves&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/simple-generation.png" alt="Simple Generation">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Multiple Variants</strong>
<p>Generate several image variants from a single call</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A minimalist logo for a coffee roastery, line art style, single color&quot;,
    &quot;n&quot;: 4
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-0.png&quot;,
      &quot;https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-1.png&quot;,
      &quot;https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-2.png&quot;,
      &quot;https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-3.png&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-0.png&quot;,
        &quot;https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-1.png&quot;,
        &quot;https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-2.png&quot;,
        &quot;https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-3.png&quot;
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/qwen-image-3.0-pro&#x27;,
  { prompt: &#x27;A minimalist logo for a coffee roastery, line art style, single color&#x27;, n: 4 },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/qwen-image-3.0-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A minimalist logo for a coffee roastery, line art style, single color&quot;,
    &quot;n&quot;: 4
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-0.png" alt="Multiple Variants">
<img src="https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-1.png" alt="Multiple Variants">
<img src="https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-2.png" alt="Multiple Variants">
<img src="https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-3.png" alt="Multiple Variants">
</section>

<section class="model-example"><strong>Negative Prompt</strong>
<p>Guide generation away from unwanted elements</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar&quot;,
    &quot;negative_prompt&quot;: &quot;modern clothing, photograph, blurry, low quality&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/negative-prompt.png&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/negative-prompt.png&quot;
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/qwen-image-3.0-pro&#x27;,
  {
    prompt: &#x27;A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar&#x27;,
    negative_prompt: &#x27;modern clothing, photograph, blurry, low quality&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/qwen-image-3.0-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar&quot;,
    &quot;negative_prompt&quot;: &quot;modern clothing, photograph, blurry, low quality&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/negative-prompt.png" alt="Negative Prompt">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>size</code></td><td>string</td><td>Required. Default: 1024x1024</td></tr><tr><td><code>negative_prompt</code></td><td>string</td><td></td></tr><tr><td><code>n</code></td><td>integer</td><td>Minimum: 1; Maximum: 6</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Minimum: 0; Maximum: 2147483647</td></tr><tr><td><code>watermark</code></td><td>boolean</td><td></td></tr><tr><td><code>prompt_extend</code></td><td>boolean</td><td></td></tr><tr><td><code>prompt_extend_mode</code></td><td>string</td><td>Values: direct, agent</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>images</code></td><td>array</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/alibaba/qwen-image-3.0-pro/schema-input.json)
- [Output schema](/ai/models/alibaba/qwen-image-3.0-pro/schema-output.json)

