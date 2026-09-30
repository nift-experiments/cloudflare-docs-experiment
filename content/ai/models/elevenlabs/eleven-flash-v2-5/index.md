---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/elevenlabs/eleven-flash-v2-5/
  description: elevenlabs/eleven-flash-v2-5
  full_title: Eleven Flash v2.5 · Cloudflare AI docs
  head_html: <title>Eleven Flash v2.5 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="elevenlabs/eleven-flash-v2-5"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/elevenlabs/eleven-flash-v2-5/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Eleven Flash v2.5 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="elevenlabs/eleven-flash-v2-5"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/elevenlabs/eleven-flash-v2-5/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/elevenlabs/eleven-flash-v2-5/#page","headline":"Eleven Flash v2.5 \u00b7 Cloudflare AI docs","description":"elevenlabs/eleven-flash-v2-5","url":"https://developers.cloudflare.com/ai/models/elevenlabs/eleven-flash-v2-5/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/elevenlabs/eleven-flash-v2-5/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/elevenlabs.svg" alt="Elevenlabs logo" width="48" height="48">

<h1 id="eleven-flash-v2-5">Eleven Flash v2.5</h1>

<p><code>elevenlabs/eleven-flash-v2-5</code></p>

ElevenLabs' low-latency Flash v2.5 text-to-speech model for fast multilingual speech generation.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Speech</td></tr>
<tr><th>Terms</th><td><a href="https://elevenlabs.io/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per character: 5e-05, Default (per second): 5e-05</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate low-latency speech for an AI Gateway support assistant

<section class="model-example"><strong>AI Gateway Assistant</strong>
<p>Generate low-latency speech for an AI Gateway support assistant</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Thanks for contacting Cloudflare AI Gateway support. I can help you compare providers, review request logs, or troubleshoot model routing.&quot;,
    &quot;voice_id&quot;: &quot;JBFqnCBsd6RMkjVDRZzb&quot;,
    &quot;output_format&quot;: &quot;mp3_44100_128&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/elevenlabs/eleven-flash-v2-5/ai-gateway-assistant.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/elevenlabs/eleven-flash-v2-5/ai-gateway-assistant.mp3&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;elevenlabs/eleven-flash-v2-5&#x27;,
  {
    text: &#x27;Thanks for contacting Cloudflare AI Gateway support. I can help you compare providers, review request logs, or troubleshoot model routing.&#x27;,
    voice_id: &#x27;JBFqnCBsd6RMkjVDRZzb&#x27;,
    output_format: &#x27;mp3_44100_128&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;elevenlabs/eleven-flash-v2-5&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Thanks for contacting Cloudflare AI Gateway support. I can help you compare providers, review request logs, or troubleshoot model routing.&quot;,
    &quot;voice_id&quot;: &quot;JBFqnCBsd6RMkjVDRZzb&quot;,
    &quot;output_format&quot;: &quot;mp3_44100_128&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The text to convert into speech. Minimum length: 1</td></tr><tr><td><code>voice_id</code></td><td>string</td><td>Required. The ElevenLabs voice ID to use for generation. Minimum length: 1</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Values: mp3_22050_32, mp3_24000_48, mp3_44100_128, mp3_44100_192, mp3_44100_32, mp3_44100_64, mp3_44100_96, opus_48000_128, opus_48000_192, opus_48000_32, opus_48000_64, opus_48000_96</td></tr><tr><td><code>language_code</code></td><td>string</td><td>ISO 639-1 language code to enforce.</td></tr><tr><td><code>voice_settings</code></td><td>object</td><td></td></tr><tr><td><code>voice_settings.stability</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>voice_settings.similarity_boost</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>voice_settings.style</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>voice_settings.use_speaker_boost</code></td><td>boolean</td><td></td></tr><tr><td><code>voice_settings.speed</code></td><td>number</td><td>Minimum: 0.7; Maximum: 1.2</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Minimum: 0; Maximum: 4294967295</td></tr><tr><td><code>previous_text</code></td><td>string</td><td></td></tr><tr><td><code>next_text</code></td><td>string</td><td></td></tr><tr><td><code>apply_text_normalization</code></td><td>string</td><td>Values: auto, on, off</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>string</td><td>Required. URL to the generated audio file.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/elevenlabs/eleven-flash-v2-5/schema-input.json)
- [Output schema](/ai/models/elevenlabs/eleven-flash-v2-5/schema-output.json)

