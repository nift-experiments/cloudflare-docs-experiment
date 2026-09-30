---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/google/gemini-3.1-flash-tts/
  description: google/gemini-3.1-flash-tts
  full_title: Gemini 3.1 Flash TTS · Cloudflare AI docs
  head_html: <title>Gemini 3.1 Flash TTS · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="google/gemini-3.1-flash-tts"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/google/gemini-3.1-flash-tts/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Gemini 3.1 Flash TTS · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="google/gemini-3.1-flash-tts"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/google/gemini-3.1-flash-tts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/google/gemini-3.1-flash-tts/#page","headline":"Gemini 3.1 Flash TTS \u00b7 Cloudflare AI docs","description":"google/gemini-3.1-flash-tts","url":"https://developers.cloudflare.com/ai/models/google/gemini-3.1-flash-tts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/google/gemini-3.1-flash-tts/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="gemini-3-1-flash-tts">Gemini 3.1 Flash TTS</h1>

<p><code>google/gemini-3.1-flash-tts</code></p>

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Speech</td></tr>
<tr><th>Unit pricing</th><td>Input audio tokens (per 1M): 3, Input text tokens (per 1M): 0.75, output_audio_tokens: 12, output_text_tokens: 4.5</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Convert text to speech with default voice

<section class="model-example"><strong>Simple Text-to-Speech</strong>
<p>Convert text to speech with default voice</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Hello, welcome to Cloudflare AI Gateway!&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__gemini-3.1-flash-tts/simple-text-to-speech.wav&quot;
  },
  &quot;raw_response&quot;: {
    &quot;audio&quot;: &quot;data:audio/l16;base64,...&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.1-flash-tts&#x27;,
  { text: &#x27;Hello, welcome to Cloudflare AI Gateway!&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.1-flash-tts&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Hello, welcome to Cloudflare AI Gateway!&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Custom Voice</strong>
<p>Generate speech with a specific voice</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;The quick brown fox jumps over the lazy dog.&quot;,
    &quot;voice&quot;: &quot;Puck&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__gemini-3.1-flash-tts/custom-voice.wav&quot;
  },
  &quot;raw_response&quot;: {
    &quot;audio&quot;: &quot;data:audio/l16;base64,...&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.1-flash-tts&#x27;,
  { text: &#x27;The quick brown fox jumps over the lazy dog.&#x27;, voice: &#x27;Puck&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.1-flash-tts&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;The quick brown fox jumps over the lazy dog.&quot;,
    &quot;voice&quot;: &quot;Puck&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Longer Text</strong>
<p>Convert longer text to speech</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Artificial intelligence has transformed the way we interact with technology. From voice assistants to autonomous vehicles, AI is reshaping our daily lives and creating new possibilities for innovation.&quot;,
    &quot;voice&quot;: &quot;Charon&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__gemini-3.1-flash-tts/longer-text.wav&quot;
  },
  &quot;raw_response&quot;: {
    &quot;audio&quot;: &quot;data:audio/l16;base64,...&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.1-flash-tts&#x27;,
  {
    text: &#x27;Artificial intelligence has transformed the way we interact with technology. From voice assistants to autonomous vehicles, AI is reshaping our daily lives and creating new possibilities for innovation.&#x27;,
    voice: &#x27;Charon&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.1-flash-tts&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Artificial intelligence has transformed the way we interact with technology. From voice assistants to autonomous vehicles, AI is reshaping our daily lives and creating new possibilities for innovation.&quot;,
    &quot;voice&quot;: &quot;Charon&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Narrative Voice</strong>
<p>Generate speech with a narrative voice style</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Once upon a time, in a kingdom far away, there lived a brave knight who sought to protect the realm from all dangers.&quot;,
    &quot;voice&quot;: &quot;Kore&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__gemini-3.1-flash-tts/narrative-voice.wav&quot;
  },
  &quot;raw_response&quot;: {
    &quot;audio&quot;: &quot;data:audio/l16;base64,...&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.1-flash-tts&#x27;,
  {
    text: &#x27;Once upon a time, in a kingdom far away, there lived a brave knight who sought to protect the realm from all dangers.&#x27;,
    voice: &#x27;Kore&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.1-flash-tts&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Once upon a time, in a kingdom far away, there lived a brave knight who sought to protect the realm from all dangers.&quot;,
    &quot;voice&quot;: &quot;Kore&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The text to convert to speech. Maximum 10,000 characters.</td></tr><tr><td><code>voice</code></td><td>string</td><td>The voice to use for speech synthesis Values: Zephyr, Puck, Charon, Kore, Fenrir, Leda, Orus, Aoede, Callirrhoe, Autonoe, Enceladus, Iapetus, Umbriel, Algieba, Despina, Erinome, Algenib, Rasalgethi, Laomedeia, Achernar, Alnilam, Schedar, Gacrux, Pulcherrima, Achird, Zubenelgenubi, Vindemiatrix, Sadachbia, Sadaltager, Sulafat</td></tr><tr><td><code>temperature</code></td><td>number</td><td>Controls randomness in generation (0-2) Minimum: 0; Maximum: 2</td></tr><tr><td><code>topP</code></td><td>number</td><td>Nucleus sampling threshold (0-1). Tokens with cumulative probability up to topP are considered Minimum: 0; Maximum: 1</td></tr><tr><td><code>topK</code></td><td>integer</td><td>Only sample from the top K tokens. Smaller K = more focused, larger K = more diverse Maximum: 9007199254740991</td></tr><tr><td><code>maxOutputTokens</code></td><td>integer</td><td>Maximum number of tokens to generate Maximum: 9007199254740991</td></tr><tr><td><code>stopSequences</code></td><td>array</td><td>Sequences where the model will stop generating further tokens</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>string</td><td>Required. Base64-encoded audio data (WAV format)</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/google/gemini-3.1-flash-tts/schema-input.json)
- [Output schema](/ai/models/google/gemini-3.1-flash-tts/schema-output.json)

