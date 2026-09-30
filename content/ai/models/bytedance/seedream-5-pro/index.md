---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/
  description: bytedance/seedream-5-pro
  full_title: Seedream 5 Pro · Cloudflare AI docs
  head_html: <title>Seedream 5 Pro · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="bytedance/seedream-5-pro"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Seedream 5 Pro · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="bytedance/seedream-5-pro"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/#page","headline":"Seedream 5 Pro \u00b7 Cloudflare AI docs","description":"bytedance/seedream-5-pro","url":"https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/bytedance/seedream-5-pro/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/bytedance.svg" alt="Bytedance logo" width="48" height="48">

<h1 id="seedream-5-pro">Seedream 5 Pro</h1>

<p><code>bytedance/seedream-5-pro</code></p>

Seedream 5 Pro is ByteDance's high-quality image generation and editing model with text prompts, up to 10 reference images, and 1K, 2K, or explicit pixel-size output controls.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.045, Per input image: 0.03, Default (per second): 0.045</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Clean studio product render with precise materials and lighting.

<section class="model-example"><strong>Mechanical Watch</strong>
<p>Clean studio product render with precise materials and lighting.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Premium studio product render of a transparent mechanical wristwatch suspended above matte black stone, visible gears, sapphire reflections, razor-sharp lighting, luxury advertising style&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/mechanical-watch-0.jpeg&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/mechanical-watch-0.jpeg&quot;
      ]
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-5-pro&#x27;,
  {
    prompt:
      &#x27;Premium studio product render of a transparent mechanical wristwatch suspended above matte black stone, visible gears, sapphire reflections, razor-sharp lighting, luxury advertising style&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-5-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Premium studio product render of a transparent mechanical wristwatch suspended above matte black stone, visible gears, sapphire reflections, razor-sharp lighting, luxury advertising style&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/mechanical-watch-0.jpeg" alt="Mechanical Watch">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Red Panda Bakery</strong>
<p>Whimsical illustrated scene with a very different visual style.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cozy children&#x27;s book illustration of a red panda baker frosting moon-shaped cakes inside a tiny snowy mountain bakery, soft gouache texture, warm window light&quot;,
    &quot;size&quot;: &quot;1536x864&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/red-panda-bakery-0.jpeg&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/red-panda-bakery-0.jpeg&quot;
      ]
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-5-pro&#x27;,
  {
    prompt:
      &quot;A cozy children&#x27;s book illustration of a red panda baker frosting moon-shaped cakes inside a tiny snowy mountain bakery, soft gouache texture, warm window light&quot;,
    size: &#x27;1536x864&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-5-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A cozy children&#x27;\&#x27;&#x27;s book illustration of a red panda baker frosting moon-shaped cakes inside a tiny snowy mountain bakery, soft gouache texture, warm window light&quot;,
    &quot;size&quot;: &quot;1536x864&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/red-panda-bakery-0.jpeg" alt="Red Panda Bakery">
</section>

<section class="model-example"><strong>Claymation Reference</strong>
<p>Use a reference image for a claymation-style transformation.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg&quot;,
    &quot;prompt&quot;: &quot;Transform this reference into a handcrafted claymation diorama, rounded clay forms, visible fingerprints, miniature set lighting, playful stop-motion film look&quot;,
    &quot;size&quot;: &quot;1K&quot;
  },
  &quot;output&quot;: {
    &quot;images&quot;: [
      &quot;https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/claymation-reference-0.jpeg&quot;
    ]
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;images&quot;: [
        &quot;https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/claymation-reference-0.jpeg&quot;
      ]
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;bytedance/seedream-5-pro&#x27;,
  {
    image: &#x27;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg&#x27;,
    prompt:
      &#x27;Transform this reference into a handcrafted claymation diorama, rounded clay forms, visible fingerprints, miniature set lighting, playful stop-motion film look&#x27;,
    size: &#x27;1K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;bytedance/seedream-5-pro&quot;,
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg&quot;,
    &quot;prompt&quot;: &quot;Transform this reference into a handcrafted claymation diorama, rounded clay forms, visible fingerprints, miniature set lighting, playful stop-motion film look&quot;,
    &quot;size&quot;: &quot;1K&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/claymation-reference-0.jpeg" alt="Claymation Reference">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>image</code></td><td>string or array</td><td></td></tr><tr><td><code>size</code></td><td>string</td><td></td></tr><tr><td><code>watermark</code></td><td>boolean</td><td>Required. Whether to add an AI-generated watermark to the output image Default: False</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>images</code></td><td>array</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/bytedance/seedream-5-pro/schema-input.json)
- [Output schema](/ai/models/bytedance/seedream-5-pro/schema-output.json)

