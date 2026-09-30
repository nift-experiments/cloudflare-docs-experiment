---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/models/llava-1.5-7b-hf/
  description: '@cf/llava-hf/llava-1.5-7b-hf'
  full_title: '@cf/llava-hf/llava-1.5-7b-hf · Cloudflare Workers AI docs'
  head_html: <title>@cf/llava-hf/llava-1.5-7b-hf · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="@cf/llava-hf/llava-1.5-7b-hf"><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/models/llava-1.5-7b-hf/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="@cf/llava-hf/llava-1.5-7b-hf · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="@cf/llava-hf/llava-1.5-7b-hf"><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/models/llava-1.5-7b-hf/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/models/llava-1.5-7b-hf/#page","headline":"@cf/llava-hf/llava-1.5-7b-hf \u00b7 Cloudflare Workers AI docs","description":"@cf/llava-hf/llava-1.5-7b-hf","url":"https://developers.cloudflare.com/workers-ai/models/llava-1.5-7b-hf/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /workers-ai/models/llava-1.5-7b-hf/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="llava-1-5-7b-hf">llava-1.5-7b-hf</h1>

<p><code>@cf/llava-hf/llava-1.5-7b-hf</code></p>

LLaVA is an open-source chatbot trained by fine-tuning LLaMA/Vicuna on GPT-generated multimodal instruction-following data. It is an auto-regressive language model, based on the transformer architecture.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Image-to-Text</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">export default {
  async fetch(request, env) {
    const input = await request.json();
    const response = await env.AI.run(&quot;@cf/llava-hf/llava-1.5-7b-hf&quot;, input);
    return Response.json(response);
  },
} satisfies ExportedHandler&lt;Env&gt;;</code></pre>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/llava-hf/llava-1.5-7b-hf&quot;, { image_to_text: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/llava-hf/llava-1.5-7b-hf -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>array or string</td><td>Required.</td></tr><tr><td><code>temperature</code></td><td>number</td><td>Controls the randomness of the output; higher values produce more random results.</td></tr><tr><td><code>prompt</code></td><td>string</td><td>The input text prompt for the model to generate a response.</td></tr><tr><td><code>raw</code></td><td>boolean</td><td>If true, a chat template is not applied and you must adhere to the specific model's expected formatting. Default: False</td></tr><tr><td><code>top_p</code></td><td>number</td><td>Controls the creativity of the AI's responses by adjusting how many possible words it considers. Lower values make outputs more predictable; higher values allow for more varied and creative responses.</td></tr><tr><td><code>top_k</code></td><td>number</td><td>Limits the AI to choose from the top 'k' most probable words. Lower values make responses more focused; higher values introduce more variety and potential surprises.</td></tr><tr><td><code>seed</code></td><td>number</td><td>Random seed for reproducibility of the generation.</td></tr><tr><td><code>repetition_penalty</code></td><td>number</td><td>Penalty for repeated tokens; higher values discourage repetition.</td></tr><tr><td><code>frequency_penalty</code></td><td>number</td><td>Decreases the likelihood of the model repeating the same lines verbatim.</td></tr><tr><td><code>presence_penalty</code></td><td>number</td><td>Increases the likelihood of the model introducing new topics.</td></tr><tr><td><code>max_tokens</code></td><td>integer</td><td>The maximum number of tokens to generate in the response. Default: 512</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>description</code></td><td>string</td><td></td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/llava-1.5-7b-hf/schema-input.json)
- [Output schema](/workers-ai/models/llava-1.5-7b-hf/schema-output.json)

