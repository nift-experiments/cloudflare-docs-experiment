---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/models/whisper/
  description: '@cf/openai/whisper'
  full_title: '@cf/openai/whisper · Cloudflare Workers AI docs'
  head_html: <title>@cf/openai/whisper · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="@cf/openai/whisper"><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/models/whisper/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="@cf/openai/whisper · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="@cf/openai/whisper"><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/models/whisper/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/models/whisper/#page","headline":"@cf/openai/whisper \u00b7 Cloudflare Workers AI docs","description":"@cf/openai/whisper","url":"https://developers.cloudflare.com/workers-ai/models/whisper/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /workers-ai/models/whisper/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="whisper">whisper</h1>

<p><code>@cf/openai/whisper</code></p>

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Automatic Speech Recognition</td></tr>
<tr><th>More information</th><td><a href="https://openai.com/research/whisper">Model details</a></td></tr>
<tr><th>Unit pricing</th><td>USD 0.000453 per audio minute</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">export default {
  async fetch(request, env) {
    const input = await request.json();
    const response = await env.AI.run(&quot;@cf/openai/whisper&quot;, input);
    return Response.json(response);
  },
} satisfies ExportedHandler&lt;Env&gt;;</code></pre>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/openai/whisper&quot;, { automatic_speech_recognition: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/openai/whisper -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>array</td><td>Required. An array of integers that represent the audio data constrained to 8-bit unsigned integer values</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The transcription</td></tr><tr><td><code>word_count</code></td><td>number</td><td></td></tr><tr><td><code>words</code></td><td>array</td><td></td></tr><tr><td><code>words[].word</code></td><td>string</td><td></td></tr><tr><td><code>words[].start</code></td><td>number</td><td>The second this word begins in the recording</td></tr><tr><td><code>words[].end</code></td><td>number</td><td>The ending second when the word completes</td></tr><tr><td><code>vtt</code></td><td>string</td><td></td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/whisper/schema-input.json)
- [Output schema](/workers-ai/models/whisper/schema-output.json)

