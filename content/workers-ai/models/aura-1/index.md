---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/models/aura-1/
  description: '@cf/deepgram/aura-1'
  full_title: '@cf/deepgram/aura-1 · Cloudflare Workers AI docs'
  head_html: <title>@cf/deepgram/aura-1 · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="@cf/deepgram/aura-1"><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/models/aura-1/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="@cf/deepgram/aura-1 · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="@cf/deepgram/aura-1"><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/models/aura-1/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/models/aura-1/#page","headline":"@cf/deepgram/aura-1 \u00b7 Cloudflare Workers AI docs","description":"@cf/deepgram/aura-1","url":"https://developers.cloudflare.com/workers-ai/models/aura-1/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /workers-ai/models/aura-1/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="aura-1">aura-1</h1>

<p><code>@cf/deepgram/aura-1</code></p>

Aura is a context-aware text-to-speech (TTS) model that applies natural pacing, expressiveness, and fillers based on the context of the provided text. The quality of your text input directly impacts the naturalness of the audio output.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Speech</td></tr>
<tr><th>Asynchronous queue</th><td>Yes</td></tr>
<tr><th>Terms</th><td><a href="https://deepgram.com/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>USD 0.015 per 1k characters</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/deepgram/aura-1&quot;, { text_to_speech: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/deepgram/aura-1 -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>speaker</code></td><td>string</td><td>Speaker used to produce the audio. Default: angus; Values: angus, asteria, arcas, orion, orpheus, athena, luna, zeus, perseus, helios, hera, stella</td></tr><tr><td><code>encoding</code></td><td>string</td><td>Encoding of the output audio. Values: linear16, flac, mulaw, alaw, mp3, opus, aac</td></tr><tr><td><code>container</code></td><td>string</td><td>Container specifies the file format wrapper for the output audio. The available options depend on the encoding type.. Values: none, wav, ogg</td></tr><tr><td><code>text</code></td><td>string</td><td>Required. The text content to be converted to speech</td></tr><tr><td><code>sample_rate</code></td><td>number</td><td>Sample Rate specifies the sample rate for the output audio. Based on the encoding, different sample rates are supported. For some encodings, the sample rate is not configurable</td></tr><tr><td><code>bit_rate</code></td><td>number</td><td>The bitrate of the audio in bits per second. Choose from predefined ranges or specific values based on the encoding type.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<p>No parameters.</p>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/aura-1/schema-input.json)
- [Output schema](/workers-ai/models/aura-1/schema-output.json)

