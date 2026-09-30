---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/models/flux-1-schnell/
  description: '@cf/black-forest-labs/flux-1-schnell'
  full_title: '@cf/black-forest-labs/flux-1-schnell · Cloudflare Workers AI docs'
  head_html: <title>@cf/black-forest-labs/flux-1-schnell · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="@cf/black-forest-labs/flux-1-schnell"><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/models/flux-1-schnell/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="@cf/black-forest-labs/flux-1-schnell · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="@cf/black-forest-labs/flux-1-schnell"><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/models/flux-1-schnell/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/models/flux-1-schnell/#page","headline":"@cf/black-forest-labs/flux-1-schnell \u00b7 Cloudflare Workers AI docs","description":"@cf/black-forest-labs/flux-1-schnell","url":"https://developers.cloudflare.com/workers-ai/models/flux-1-schnell/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /workers-ai/models/flux-1-schnell/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="flux-1-schnell">flux-1-schnell</h1>

<p><code>@cf/black-forest-labs/flux-1-schnell</code></p>

FLUX.1 [schnell] is a 12 billion parameter rectified flow transformer capable of generating images from text descriptions. 

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://bfl.ai/legal/terms-of-service">Model terms</a></td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">export default {
  async fetch(request, env) {
    const response = await env.AI.run(&quot;@cf/black-forest-labs/flux-1-schnell&quot;, {
      prompt: &quot;a cyberpunk lizard&quot;,
      seed: Math.floor(Math.random() * 10),
    });
    const binaryString = atob(response.image);
    const bytes = Uint8Array.from(binaryString, (m) =&gt; m.codePointAt(0));
    return new Response(bytes, { headers: { &quot;content-type&quot;: &quot;image/jpeg&quot; } });
  },
} satisfies ExportedHandler&lt;Env&gt;;</code></pre>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/black-forest-labs/flux-1-schnell&quot;, { text_to_image: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/black-forest-labs/flux-1-schnell -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. A text description of the image you want to generate. Minimum length: 1</td></tr><tr><td><code>steps</code></td><td>integer</td><td>The number of diffusion steps; higher values can improve quality but take longer. Default is 4 Maximum: 8</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>The generated image in Base64 format.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/flux-1-schnell/schema-input.json)
- [Output schema](/workers-ai/models/flux-1-schnell/schema-output.json)

