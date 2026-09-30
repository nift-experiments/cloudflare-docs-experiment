---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/models/plamo-embedding-1b/
  description: '@cf/pfnet/plamo-embedding-1b'
  full_title: '@cf/pfnet/plamo-embedding-1b · Cloudflare Workers AI docs'
  head_html: <title>@cf/pfnet/plamo-embedding-1b · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="@cf/pfnet/plamo-embedding-1b"><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/models/plamo-embedding-1b/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="@cf/pfnet/plamo-embedding-1b · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="@cf/pfnet/plamo-embedding-1b"><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/models/plamo-embedding-1b/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/models/plamo-embedding-1b/#page","headline":"@cf/pfnet/plamo-embedding-1b \u00b7 Cloudflare Workers AI docs","description":"@cf/pfnet/plamo-embedding-1b","url":"https://developers.cloudflare.com/workers-ai/models/plamo-embedding-1b/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /workers-ai/models/plamo-embedding-1b/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="plamo-embedding-1b">plamo-embedding-1b</h1>

<p><code>@cf/pfnet/plamo-embedding-1b</code></p>

PLaMo-Embedding-1B is a Japanese text embedding model developed by Preferred Networks, Inc.

It can convert Japanese text input into numerical vectors and can be used for a wide range of applications, including information retrieval, text classification, and clustering.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Embeddings</td></tr>
<tr><th>Unit pricing</th><td>USD 0.0186 per M input tokens</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<div class="nb-tabs" data-nb-tabs><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="TypeScript"><pre><code class="language-ts">export default { async fetch(request, env) { const response = await env.AI.run("@cf/pfnet/plamo-embedding-1b", { text: ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }); return Response.json(response); } } satisfies ExportedHandler&lt;Env&gt;;</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="Python"><pre><code class="language-py">output = requests.post("https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/pfnet/plamo-embedding-1b", headers={"Authorization": "Bearer {API_KEY}"}, json={ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] })
print(output.json())</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="curl"><pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/pfnet/plamo-embedding-1b -X POST -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" -d '{ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }'</code></pre></section></div><aside class="nb-aside note"><p>Workers AI also supports OpenAI compatible API endpoints for <code>/v1/chat/completions</code> and <code>/v1/embeddings</code>. For more details, refer to <a href="/workers-ai/configuration/open-ai-compatibility/">Configurations</a>.</p></aside>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string or array</td><td>Required. Input text to embed. Can be a single string or a list of strings.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>data</code></td><td>array</td><td>Required. Embedding vectors, where each vector is a list of floats.</td></tr><tr><td><code>shape</code></td><td>array</td><td>Required. Shape of the embedding data as [number_of_embeddings, embedding_dimension].</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/plamo-embedding-1b/schema-input.json)
- [Output schema](/workers-ai/models/plamo-embedding-1b/schema-output.json)

