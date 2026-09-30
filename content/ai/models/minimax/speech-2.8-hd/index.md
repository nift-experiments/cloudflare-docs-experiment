---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/minimax/speech-2.8-hd/
  description: minimax/speech-2.8-hd
  full_title: MiniMax Speech 2.8 HD · Cloudflare AI docs
  head_html: <title>MiniMax Speech 2.8 HD · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="minimax/speech-2.8-hd"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/minimax/speech-2.8-hd/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="MiniMax Speech 2.8 HD · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="minimax/speech-2.8-hd"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/minimax/speech-2.8-hd/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/minimax/speech-2.8-hd/#page","headline":"MiniMax Speech 2.8 HD \u00b7 Cloudflare AI docs","description":"minimax/speech-2.8-hd","url":"https://developers.cloudflare.com/ai/models/minimax/speech-2.8-hd/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/minimax/speech-2.8-hd/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/minimax.svg" alt="Minimax logo" width="48" height="48">

<h1 id="minimax-speech-2-8-hd">MiniMax Speech 2.8 HD</h1>

<p><code>minimax/speech-2.8-hd</code></p>

MiniMax Speech 2.8 HD focuses on studio-grade audio generation with emotion control, multilingual support (40+ languages), and voice cloning.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Speech</td></tr>
<tr><th>Terms</th><td><a href="https://www.minimaxi.com/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per character: 0.0001</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate speech with default settings

<section class="model-example"><strong>Simple Speech</strong>
<p>Generate speech with default settings</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-hd/simple-speech.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-hd/simple-speech.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/speech-2.8-hd&#x27;,
  {
    format: &#x27;mp3&#x27;,
    pitch: 0,
    speed: 1,
    text: &#x27;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&#x27;,
    voice_id: &#x27;English_expressive_narrator&#x27;,
    volume: 1,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/speech-2.8-hd&quot;,
  &quot;input&quot;: {
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Custom Voice</strong>
<p>Use a specific voice and adjust speed</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;speed&quot;: 0.9,
    &quot;text&quot;: &quot;The weather today is sunny with a high of 72 degrees. Perfect for a walk in the park.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-hd/custom-voice.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-hd/custom-voice.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/speech-2.8-hd&#x27;,
  {
    format: &#x27;mp3&#x27;,
    pitch: 0,
    speed: 0.9,
    text: &#x27;The weather today is sunny with a high of 72 degrees. Perfect for a walk in the park.&#x27;,
    voice_id: &#x27;English_expressive_narrator&#x27;,
    volume: 1,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/speech-2.8-hd&quot;,
  &quot;input&quot;: {
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;speed&quot;: 0.9,
    &quot;text&quot;: &quot;The weather today is sunny with a high of 72 degrees. Perfect for a walk in the park.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>With Emotion</strong>
<p>Apply emotional tone to speech</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;emotion&quot;: &quot;happy&quot;,
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Congratulations! You&#x27;ve just won the grand prize! This is absolutely incredible news!&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-hd/with-emotion.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-hd/with-emotion.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/speech-2.8-hd&#x27;,
  {
    emotion: &#x27;happy&#x27;,
    format: &#x27;mp3&#x27;,
    pitch: 0,
    speed: 1,
    text: &quot;Congratulations! You&#x27;ve just won the grand prize! This is absolutely incredible news!&quot;,
    voice_id: &#x27;English_expressive_narrator&#x27;,
    volume: 1,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/speech-2.8-hd&quot;,
  &quot;input&quot;: {
    &quot;emotion&quot;: &quot;happy&quot;,
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;Congratulations! You&#x27;\&#x27;&#x27;ve just won the grand prize! This is absolutely incredible news!&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>High Sample Rate</strong>
<p>Studio quality at 44.1kHz sample rate</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;sample_rate&quot;: 44100,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;This recording is generated at studio quality sample rate for the highest possible audio fidelity.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-hd/high-sample-rate.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-hd/high-sample-rate.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/speech-2.8-hd&#x27;,
  {
    format: &#x27;mp3&#x27;,
    pitch: 0,
    sample_rate: 44100,
    speed: 1,
    text: &#x27;This recording is generated at studio quality sample rate for the highest possible audio fidelity.&#x27;,
    voice_id: &#x27;English_expressive_narrator&#x27;,
    volume: 1,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/speech-2.8-hd&quot;,
  &quot;input&quot;: {
    &quot;format&quot;: &quot;mp3&quot;,
    &quot;pitch&quot;: 0,
    &quot;sample_rate&quot;: 44100,
    &quot;speed&quot;: 1,
    &quot;text&quot;: &quot;This recording is generated at studio quality sample rate for the highest possible audio fidelity.&quot;,
    &quot;voice_id&quot;: &quot;English_expressive_narrator&quot;,
    &quot;volume&quot;: 1
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The text to convert to speech. Maximum 10,000 characters.</td></tr><tr><td><code>voice_id</code></td><td>string</td><td>Required. The voice ID to use for synthesis Default: English_expressive_narrator</td></tr><tr><td><code>speed</code></td><td>number</td><td>Required. Speech speed (0.5 to 2) Default: 1; Minimum: 0.5; Maximum: 2</td></tr><tr><td><code>volume</code></td><td>number</td><td>Required. Speech volume (0 to 10) Default: 1; Minimum: 0; Maximum: 10</td></tr><tr><td><code>pitch</code></td><td>integer</td><td>Required. Pitch adjustment (-12 to 12) Default: 0; Minimum: -12; Maximum: 12</td></tr><tr><td><code>emotion</code></td><td>string</td><td>Emotion control for synthesized speech Values: happy, sad, angry, fearful, disgusted, surprised, calm, fluent</td></tr><tr><td><code>format</code></td><td>string</td><td>Required. Output audio format Default: mp3; Values: mp3, flac, wav</td></tr><tr><td><code>sample_rate</code></td><td>number</td><td>Audio sample rate</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>string</td><td>Required. URL to the generated audio file</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/minimax/speech-2.8-hd/schema-input.json)
- [Output schema](/ai/models/minimax/speech-2.8-hd/schema-output.json)

