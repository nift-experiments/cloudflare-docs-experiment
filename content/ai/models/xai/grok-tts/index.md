---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/xai/grok-tts/
  description: xai/grok-tts
  full_title: Grok TTS · Cloudflare AI docs
  head_html: <title>Grok TTS · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="xai/grok-tts"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/xai/grok-tts/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Grok TTS · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="xai/grok-tts"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/xai/grok-tts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/xai/grok-tts/#page","headline":"Grok TTS \u00b7 Cloudflare AI docs","description":"xai/grok-tts","url":"https://developers.cloudflare.com/ai/models/xai/grok-tts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/xai/grok-tts/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/xai.svg" alt="Xai logo" width="48" height="48">

<h1 id="grok-tts">Grok TTS</h1>

<p><code>xai/grok-tts</code></p>

xAI's Grok text-to-speech model. Generates high-fidelity spoken audio in 5 expressive voices (eve, ara, rex, sal, leo) with 20+ supported languages. Supports inline speech tags for laughter, whispers, and pauses.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Speech</td></tr>
<tr><th>Terms</th><td><a href="https://x.ai/legal/terms-of-service">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per character: 1.5e-05</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate speech with the default voice (eve) in English

<section class="model-example"><strong>Simple Generation</strong>
<p>Generate speech with the default voice (eve) in English</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Hello! Welcome to the xAI Text to Speech API.&quot;,
    &quot;language&quot;: &quot;en&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-tts/simple-generation.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-tts/simple-generation.mp3&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-tts&#x27;,
  { text: &#x27;Hello! Welcome to the xAI Text to Speech API.&#x27;, language: &#x27;en&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-tts&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Hello! Welcome to the xAI Text to Speech API.&quot;,
    &quot;language&quot;: &quot;en&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Different Voice</strong>
<p>Use the warm, conversational `ara` voice</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Thank you for calling. How can I help you today?&quot;,
    &quot;voice_id&quot;: &quot;ara&quot;,
    &quot;language&quot;: &quot;en&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-tts/different-voice.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-tts/different-voice.mp3&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-tts&#x27;,
  { text: &#x27;Thank you for calling. How can I help you today?&#x27;, voice_id: &#x27;ara&#x27;, language: &#x27;en&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-tts&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Thank you for calling. How can I help you today?&quot;,
    &quot;voice_id&quot;: &quot;ara&quot;,
    &quot;language&quot;: &quot;en&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>High-Fidelity MP3</strong>
<p>44.1 kHz / 192 kbps MP3 for production use</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Crystal clear audio at maximum quality.&quot;,
    &quot;voice_id&quot;: &quot;rex&quot;,
    &quot;language&quot;: &quot;en&quot;,
    &quot;output_format&quot;: {
      &quot;codec&quot;: &quot;mp3&quot;,
      &quot;sample_rate&quot;: 44100,
      &quot;bit_rate&quot;: 192000
    }
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-tts/high-fidelity-mp3.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-tts/high-fidelity-mp3.mp3&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-tts&#x27;,
  {
    text: &#x27;Crystal clear audio at maximum quality.&#x27;,
    voice_id: &#x27;rex&#x27;,
    language: &#x27;en&#x27;,
    output_format: { codec: &#x27;mp3&#x27;, sample_rate: 44100, bit_rate: 192000 },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-tts&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Crystal clear audio at maximum quality.&quot;,
    &quot;voice_id&quot;: &quot;rex&quot;,
    &quot;language&quot;: &quot;en&quot;,
    &quot;output_format&quot;: {
      &quot;codec&quot;: &quot;mp3&quot;,
      &quot;sample_rate&quot;: 44100,
      &quot;bit_rate&quot;: 192000
    }
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Telephony (mulaw)</strong>
<p>G.711 μ-law at 8 kHz for SIP / PSTN integration</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Hello, thank you for calling. How can I help you today?&quot;,
    &quot;voice_id&quot;: &quot;ara&quot;,
    &quot;language&quot;: &quot;en&quot;,
    &quot;output_format&quot;: {
      &quot;codec&quot;: &quot;mulaw&quot;,
      &quot;sample_rate&quot;: 8000
    }
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-tts/telephony-law.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-tts/telephony-law.mp3&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-tts&#x27;,
  {
    text: &#x27;Hello, thank you for calling. How can I help you today?&#x27;,
    voice_id: &#x27;ara&#x27;,
    language: &#x27;en&#x27;,
    output_format: { codec: &#x27;mulaw&#x27;, sample_rate: 8000 },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-tts&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;Hello, thank you for calling. How can I help you today?&quot;,
    &quot;voice_id&quot;: &quot;ara&quot;,
    &quot;language&quot;: &quot;en&quot;,
    &quot;output_format&quot;: {
      &quot;codec&quot;: &quot;mulaw&quot;,
      &quot;sample_rate&quot;: 8000
    }
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Expressive Delivery</strong>
<p>Inline speech tags for laughter, pauses, and whispers</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;So I walked in and [pause] there it was. [laugh] I honestly could not believe it! &lt;whisper&gt;It was a secret the whole time.&lt;/whisper&gt;&quot;,
    &quot;voice_id&quot;: &quot;eve&quot;,
    &quot;language&quot;: &quot;en&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-tts/expressive-delivery.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-tts/expressive-delivery.mp3&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-tts&#x27;,
  {
    text: &#x27;So I walked in and [pause] there it was. [laugh] I honestly could not believe it! &lt;whisper&gt;It was a secret the whole time.&lt;/whisper&gt;&#x27;,
    voice_id: &#x27;eve&#x27;,
    language: &#x27;en&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-tts&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;So I walked in and [pause] there it was. [laugh] I honestly could not believe it! &lt;whisper&gt;It was a secret the whole time.&lt;/whisper&gt;&quot;,
    &quot;voice_id&quot;: &quot;eve&quot;,
    &quot;language&quot;: &quot;en&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Text Normalization</strong>
<p>Convert written numbers and abbreviations to spoken form</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;text&quot;: &quot;The total is $1,234.56 and the meeting is at 3pm on Jan 15th.&quot;,
    &quot;voice_id&quot;: &quot;rex&quot;,
    &quot;language&quot;: &quot;en&quot;,
    &quot;text_normalization&quot;: true
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-tts/text-normalization.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/xai/grok-tts/text-normalization.mp3&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-tts&#x27;,
  {
    text: &#x27;The total is $1,234.56 and the meeting is at 3pm on Jan 15th.&#x27;,
    voice_id: &#x27;rex&#x27;,
    language: &#x27;en&#x27;,
    text_normalization: true,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-tts&quot;,
  &quot;input&quot;: {
    &quot;text&quot;: &quot;The total is $1,234.56 and the meeting is at 3pm on Jan 15th.&quot;,
    &quot;voice_id&quot;: &quot;rex&quot;,
    &quot;language&quot;: &quot;en&quot;,
    &quot;text_normalization&quot;: true
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Text to convert to speech. Maximum 15,000 characters. Supports inline speech tags: [pause], [laugh], &lt;whisper&gt;…&lt;/whisper&gt;, etc. Required for REST mode, mutually exclusive with websocket. Minimum length: 1</td></tr><tr><td><code>language</code></td><td>string</td><td>Required. BCP-47 language code (e.g. "en", "zh", "pt-BR") or "auto" for automatic language detection. Required for both REST and WebSocket modes. Supported codes: auto, en, ar-EG, ar-SA, ar-AE, bn, zh, fr, de, hi, id, it, ja, ko, pt-BR, pt-PT, ru, es-MX, es-ES, tr, vi.</td></tr><tr><td><code>websocket</code></td><td>boolean</td><td>Enable WebSocket streaming for text-to-speech. When true, establishes a bidirectional WebSocket connection. Mutually exclusive with text.</td></tr><tr><td><code>voice_id</code></td><td>string</td><td>Voice for synthesis. Defaults to "eve". Built-in voices: eve (energetic), ara (warm), rex (confident), sal (balanced), leo (authoritative). Custom voice IDs from /v1/tts/voices are also accepted. Case-insensitive — "Eve", "EVE", and "eve" are equivalent. Minimum length: 1</td></tr><tr><td><code>output_format</code></td><td>object</td><td>Output audio format. Defaults to MP3 at 24 kHz / 128 kbps when omitted.</td></tr><tr><td><code>output_format.codec</code></td><td>string</td><td>Audio codec. Defaults to "mp3". mp3 → audio/mpeg (general use); wav → audio/wav (lossless); pcm → audio/pcm (raw 16-bit LE, real-time pipelines); mulaw/ulaw → audio/basic (G.711 μ-law, telephony); alaw → audio/alaw (G.711 A-law, telephony). Values: mp3, wav, pcm, mulaw, ulaw, alaw</td></tr><tr><td><code>output_format.sample_rate</code></td><td>number</td><td>Sample rate in Hz. Defaults to 24000. Supported: 8000, 16000, 22050, 24000, 44100, 48000. Telephony codecs (mulaw, alaw) typically use 8000.</td></tr><tr><td><code>output_format.bit_rate</code></td><td>number</td><td>Bit rate in bps. MP3 only. Defaults to 128000. Supported: 32000, 64000, 96000, 128000, 192000.</td></tr><tr><td><code>optimize_streaming_latency</code></td><td>number</td><td>Latency optimization for streaming synthesis. 0 (default): no optimization, best audio quality. 1: reduced first-chunk size for lower time-to-first-audio with minor quality tradeoff.</td></tr><tr><td><code>text_normalization</code></td><td>boolean</td><td>When true, normalizes written-form text into spoken-form before synthesis (e.g. "Dr." → "Doctor", "100" → "one hundred"). Defaults to false.</td></tr><tr><td><code>speed</code></td><td>number</td><td>Speech speed multiplier. 1.0 is normal speed. Range: 0.7 to 1.5. Defaults to 1.0. Only used in WebSocket mode. Minimum: 0.7; Maximum: 1.5</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>string</td><td>Required. Presigned R2 URL for the generated audio file. MIME type reflects the requested codec (audio/mpeg for mp3, audio/wav for wav, etc.).</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/xai/grok-tts/schema-input.json)
- [Output schema](/ai/models/xai/grok-tts/schema-output.json)

