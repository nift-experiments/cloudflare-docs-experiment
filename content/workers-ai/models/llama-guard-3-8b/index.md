---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/models/llama-guard-3-8b/
  description: '@cf/meta/llama-guard-3-8b'
  full_title: '@cf/meta/llama-guard-3-8b · Cloudflare Workers AI docs'
  head_html: <title>@cf/meta/llama-guard-3-8b · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="@cf/meta/llama-guard-3-8b"><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/models/llama-guard-3-8b/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="@cf/meta/llama-guard-3-8b · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="@cf/meta/llama-guard-3-8b"><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/models/llama-guard-3-8b/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/models/llama-guard-3-8b/#page","headline":"@cf/meta/llama-guard-3-8b \u00b7 Cloudflare Workers AI docs","description":"@cf/meta/llama-guard-3-8b","url":"https://developers.cloudflare.com/workers-ai/models/llama-guard-3-8b/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /workers-ai/models/llama-guard-3-8b/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="llama-guard-3-8b">llama-guard-3-8b</h1>

<p><code>@cf/meta/llama-guard-3-8b</code></p>

Llama Guard 3 is a Llama-3.1-8B pretrained model, fine-tuned for content safety classification. Similar to previous versions, it can be used to classify content in both LLM inputs (prompt classification) and in LLM responses (response classification). It acts as an LLM – it generates text in its output that indicates whether a given prompt or response is safe or unsafe, and if unsafe, it also lists the content categories violated.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>131,072 tokens</td></tr>
<tr><th>Unit pricing</th><td>USD 0.484 per M input tokens, USD 0.03 per M output tokens</td></tr>
</tbody></table></div>

<h2 id="playground">Playground</h2>

Try this model with the Workers AI LLM Playground without additional setup or authentication.

<p><a class="nb-link-card" href="https://playground.ai.cloudflare.com/?model=@cf/meta/llama-guard-3-8b">Launch the LLM Playground</a></p>

<h2 id="usage">Usage</h2>

<div class="nb-tabs" data-nb-tabs><div role="tablist" data-nb-tabs-list></div><div data-nb-tabs-panels><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="Worker (Streaming)"><pre><code class="language-ts">export default {
  async fetch(request, env) {
    const stream = await env.AI.run(&quot;@cf/meta/llama-guard-3-8b&quot;, {
      messages: [{ role: &quot;user&quot;, content: &quot;Hello&quot; }], stream: true,
    });
    return new Response(stream, { headers: { &quot;content-type&quot;: &quot;text/event-stream&quot; } });
  },
};</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="TypeScript" hidden><pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/meta/llama-guard-3-8b&quot;, { messages });</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="Python" hidden><pre><code class="language-py">requests.post(f&quot;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/meta/llama-guard-3-8b&quot;, json={&quot;messages&quot;: messages})</code></pre></section><section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="curl" hidden><pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/meta/llama-guard-3-8b -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre></section></div></div>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>messages</code></td><td>array</td><td>Required. An array of message objects representing the conversation history.</td></tr><tr><td><code>messages[].role</code></td><td>object</td><td>Required. The role of the message sender must alternate between 'user' and 'assistant'. Values: user, assistant</td></tr><tr><td><code>messages[].content</code></td><td>string</td><td>Required. The content of the message as a string.</td></tr><tr><td><code>max_tokens</code></td><td>integer</td><td>The maximum number of tokens to generate in the response. Default: 256</td></tr><tr><td><code>temperature</code></td><td>number</td><td>Controls the randomness of the output; higher values produce more random results. Default: 0.6; Minimum: 0; Maximum: 5</td></tr><tr><td><code>response_format</code></td><td>object</td><td>Dictate the output format of the generated response.</td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Set to json_object to process and output generated text as JSON.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>response</code></td><td>string or object</td><td></td></tr><tr><td><code>response.safe</code></td><td>boolean</td><td>Whether the conversation is safe or not.</td></tr><tr><td><code>response.categories</code></td><td>array</td><td>A list of what hazard categories predicted for the conversation, if the conversation is deemed unsafe.</td></tr><tr><td><code>response.safe</code></td><td>boolean</td><td>Whether the conversation is safe or not.</td></tr><tr><td><code>response.categories</code></td><td>array</td><td>A list of what hazard categories predicted for the conversation, if the conversation is deemed unsafe.</td></tr><tr><td><code>usage</code></td><td>object</td><td>Usage statistics for the inference request</td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Total number of tokens in input Default: 0</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Total number of tokens in output Default: 0</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Total number of input and output tokens Default: 0</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/llama-guard-3-8b/schema-input.json)
- [Output schema](/workers-ai/models/llama-guard-3-8b/schema-output.json)

