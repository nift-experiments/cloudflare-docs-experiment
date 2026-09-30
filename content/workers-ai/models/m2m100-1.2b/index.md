---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/
  description: '@cf/meta/m2m100-1.2b'
  full_title: '@cf/meta/m2m100-1.2b · Cloudflare Workers AI docs'
  head_html: <title>@cf/meta/m2m100-1.2b · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="@cf/meta/m2m100-1.2b"><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="@cf/meta/m2m100-1.2b · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="@cf/meta/m2m100-1.2b"><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/#page","headline":"@cf/meta/m2m100-1.2b \u00b7 Cloudflare Workers AI docs","description":"@cf/meta/m2m100-1.2b","url":"https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /workers-ai/models/m2m100-1.2b/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="m2m100-1-2b">m2m100-1.2b</h1>

<p><code>@cf/meta/m2m100-1.2b</code></p>

Multilingual encoder-decoder (seq-to-seq) model trained for Many-to-Many multilingual translation

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Translation</td></tr>
<tr><th>Asynchronous queue</th><td>Yes</td></tr>
<tr><th>More information</th><td><a href="https://github.com/facebookresearch/fairseq/tree/main/examples/m2m_100">Model details</a></td></tr>
<tr><th>Terms</th><td><a href="https://github.com/facebookresearch/fairseq/blob/main/LICENSE">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>USD 0.342 per M input tokens, USD 0.342 per M output tokens</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">export default {
  async fetch(request, env) {
    const input = await request.json();
    const response = await env.AI.run(&quot;@cf/meta/m2m100-1.2b&quot;, input);
    return Response.json(response);
  },
} satisfies ExportedHandler&lt;Env&gt;;</code></pre>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/meta/m2m100-1.2b&quot;, { translation: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/meta/m2m100-1.2b -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The text to be translated Minimum length: 1</td></tr><tr><td><code>source_lang</code></td><td>string</td><td>The language code of the source text (e.g., 'en' for English). Defaults to 'en' if not specified Default: en</td></tr><tr><td><code>target_lang</code></td><td>string</td><td>Required. The language code to translate the text into (e.g., 'es' for Spanish)</td></tr><tr><td><code>requests</code></td><td>array</td><td>Required. Batch of the embeddings requests to run using async-queue</td></tr><tr><td><code>requests[].text</code></td><td>string</td><td>Required. The text to be translated Minimum length: 1</td></tr><tr><td><code>requests[].source_lang</code></td><td>string</td><td>The language code of the source text (e.g., 'en' for English). Defaults to 'en' if not specified Default: en</td></tr><tr><td><code>requests[].target_lang</code></td><td>string</td><td>Required. The language code to translate the text into (e.g., 'es' for Spanish)</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>translated_text</code></td><td>string</td><td>The translated text in the target language</td></tr><tr><td><code>request_id</code></td><td>string</td><td>The async request id that can be used to obtain the results.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/m2m100-1.2b/schema-input.json)
- [Output schema](/workers-ai/models/m2m100-1.2b/schema-output.json)

