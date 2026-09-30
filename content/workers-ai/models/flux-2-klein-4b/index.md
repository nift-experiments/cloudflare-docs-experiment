---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/models/flux-2-klein-4b/
  description: '@cf/black-forest-labs/flux-2-klein-4b'
  full_title: '@cf/black-forest-labs/flux-2-klein-4b · Cloudflare Workers AI docs'
  head_html: <title>@cf/black-forest-labs/flux-2-klein-4b · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="@cf/black-forest-labs/flux-2-klein-4b"><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/models/flux-2-klein-4b/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="@cf/black-forest-labs/flux-2-klein-4b · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="@cf/black-forest-labs/flux-2-klein-4b"><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/models/flux-2-klein-4b/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/models/flux-2-klein-4b/#page","headline":"@cf/black-forest-labs/flux-2-klein-4b \u00b7 Cloudflare Workers AI docs","description":"@cf/black-forest-labs/flux-2-klein-4b","url":"https://developers.cloudflare.com/workers-ai/models/flux-2-klein-4b/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /workers-ai/models/flux-2-klein-4b/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="flux-2-klein-4b">flux-2-klein-4b</h1>

<p><code>@cf/black-forest-labs/flux-2-klein-4b</code></p>

FLUX.2 [klein] is an ultra-fast, distilled image model. It unifies image generation and editing in a single model, delivering state-of-the-art quality enabling interactive workflows, real-time previews, and latency-critical applications.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://bfl.ai/legal/terms-of-service">Model terms</a></td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-4b&quot;, { text_to_image: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/black-forest-labs/flux-2-klein-4b -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>multipart</code></td><td>object</td><td>Required.</td></tr><tr><td><code>multipart.body</code></td><td>object</td><td></td></tr><tr><td><code>multipart.contentType</code></td><td>string</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Generated image as Base64 string.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/flux-2-klein-4b/schema-input.json)
- [Output schema](/workers-ai/models/flux-2-klein-4b/schema-output.json)

