---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/models/distilbert-sst-2-int8/
  description: '@cf/huggingface/distilbert-sst-2-int8'
  full_title: '@cf/huggingface/distilbert-sst-2-int8 · Cloudflare Workers AI docs'
  head_html: <title>@cf/huggingface/distilbert-sst-2-int8 · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="@cf/huggingface/distilbert-sst-2-int8"><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/models/distilbert-sst-2-int8/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="@cf/huggingface/distilbert-sst-2-int8 · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="@cf/huggingface/distilbert-sst-2-int8"><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/models/distilbert-sst-2-int8/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/models/distilbert-sst-2-int8/#page","headline":"@cf/huggingface/distilbert-sst-2-int8 \u00b7 Cloudflare Workers AI docs","description":"@cf/huggingface/distilbert-sst-2-int8","url":"https://developers.cloudflare.com/workers-ai/models/distilbert-sst-2-int8/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /workers-ai/models/distilbert-sst-2-int8/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="distilbert-sst-2-int8">distilbert-sst-2-int8</h1>

<p><code>@cf/huggingface/distilbert-sst-2-int8</code></p>

Distilled BERT model that was finetuned on SST-2 for sentiment classification

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Classification</td></tr>
<tr><th>More information</th><td><a href="https://huggingface.co/Intel/distilbert-base-uncased-finetuned-sst-2-english-int8-static">Model details</a></td></tr>
<tr><th>Unit pricing</th><td>USD 0.0263 per M input tokens</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<div class="nb-tabs" data-nb-tabs><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="TypeScript"><pre><code class="language-ts">export default { async fetch(request, env) { const response = await env.AI.run("@cf/huggingface/distilbert-sst-2-int8", { text: "This pizza is great!" }); return Response.json(response); } } satisfies ExportedHandler&lt;Env&gt;;</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="Python"><pre><code class="language-py">output = requests.post("https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/huggingface/distilbert-sst-2-int8", headers={"Authorization": "Bearer {API_KEY}"}, json={ "text": "This pizza is great!" })
print(output.json())</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="curl"><pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/huggingface/distilbert-sst-2-int8 -X POST -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" -d '{ "text": "This pizza is great!" }'</code></pre></section></div>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The text that you want to classify Minimum length: 1</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<p>No parameters.</p>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/distilbert-sst-2-int8/schema-input.json)
- [Output schema](/workers-ai/models/distilbert-sst-2-int8/schema-output.json)

