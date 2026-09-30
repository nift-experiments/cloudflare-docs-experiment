---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/models/resnet-50/
  description: '@cf/microsoft/resnet-50'
  full_title: '@cf/microsoft/resnet-50 · Cloudflare Workers AI docs'
  head_html: <title>@cf/microsoft/resnet-50 · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="@cf/microsoft/resnet-50"><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/models/resnet-50/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="@cf/microsoft/resnet-50 · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="@cf/microsoft/resnet-50"><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/models/resnet-50/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/models/resnet-50/#page","headline":"@cf/microsoft/resnet-50 \u00b7 Cloudflare Workers AI docs","description":"@cf/microsoft/resnet-50","url":"https://developers.cloudflare.com/workers-ai/models/resnet-50/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /workers-ai/models/resnet-50/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="resnet-50">resnet-50</h1>

<p><code>@cf/microsoft/resnet-50</code></p>

50 layers deep image classification CNN trained on more than 1M images from ImageNet

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Image Classification</td></tr>
<tr><th>More information</th><td><a href="https://www.microsoft.com/en-us/research/blog/microsoft-vision-model-resnet-50-combines-web-scale-data-and-multi-task-learning-to-achieve-state-of-the-art/">Model details</a></td></tr>
<tr><th>Unit pricing</th><td>USD 2.51e-06 per inference request</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">export default {
  async fetch(request, env) {
    const input = await request.json();
    const response = await env.AI.run(&quot;@cf/microsoft/resnet-50&quot;, input);
    return Response.json(response);
  },
} satisfies ExportedHandler&lt;Env&gt;;</code></pre>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/microsoft/resnet-50&quot;, { image_classification: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/microsoft/resnet-50 -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>array</td><td>Required. An array of integers that represent the image data constrained to 8-bit unsigned integer values</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<p>No parameters.</p>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/resnet-50/schema-input.json)
- [Output schema](/workers-ai/models/resnet-50/schema-output.json)

