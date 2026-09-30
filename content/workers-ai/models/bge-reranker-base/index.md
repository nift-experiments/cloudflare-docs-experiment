---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/models/bge-reranker-base/
  description: '@cf/baai/bge-reranker-base'
  full_title: '@cf/baai/bge-reranker-base · Cloudflare Workers AI docs'
  head_html: <title>@cf/baai/bge-reranker-base · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="@cf/baai/bge-reranker-base"><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/models/bge-reranker-base/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="@cf/baai/bge-reranker-base · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="@cf/baai/bge-reranker-base"><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/models/bge-reranker-base/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/models/bge-reranker-base/#page","headline":"@cf/baai/bge-reranker-base \u00b7 Cloudflare Workers AI docs","description":"@cf/baai/bge-reranker-base","url":"https://developers.cloudflare.com/workers-ai/models/bge-reranker-base/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /workers-ai/models/bge-reranker-base/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="bge-reranker-base">bge-reranker-base</h1>

<p><code>@cf/baai/bge-reranker-base</code></p>

Different from embedding model, reranker uses question and document as input and directly output similarity instead of embedding. You can get a relevance score by inputting query and passage to the reranker. And the score can be mapped to a float value in [0,1] by sigmoid function.



<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Classification</td></tr>
<tr><th>Unit pricing</th><td>USD 0.00311 per M input tokens</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<div class="nb-tabs" data-nb-tabs><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="TypeScript"><pre><code class="language-ts">export default { async fetch(request, env) { const response = await env.AI.run("@cf/baai/bge-reranker-base", { text: "This pizza is great!" }); return Response.json(response); } } satisfies ExportedHandler&lt;Env&gt;;</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="Python"><pre><code class="language-py">output = requests.post("https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/baai/bge-reranker-base", headers={"Authorization": "Bearer {API_KEY}"}, json={ "text": "This pizza is great!" })
print(output.json())</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="curl"><pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/baai/bge-reranker-base -X POST -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" -d '{ "text": "This pizza is great!" }'</code></pre></section></div>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>query</code></td><td>string</td><td>Required. A query you wish to perform against the provided contexts. Minimum length: 1</td></tr><tr><td><code>top_k</code></td><td>integer</td><td>Number of returned results starting with the best score. Minimum: 1</td></tr><tr><td><code>contexts</code></td><td>array</td><td>Required. List of provided contexts. Note that the index in this array is important, as the response will refer to it.</td></tr><tr><td><code>contexts[].text</code></td><td>string</td><td>One of the provided context content Minimum length: 1</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>response</code></td><td>array</td><td></td></tr><tr><td><code>response[].id</code></td><td>integer</td><td>Index of the context in the request</td></tr><tr><td><code>response[].score</code></td><td>number</td><td>Score of the context under the index.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/bge-reranker-base/schema-input.json)
- [Output schema](/workers-ai/models/bge-reranker-base/schema-output.json)

