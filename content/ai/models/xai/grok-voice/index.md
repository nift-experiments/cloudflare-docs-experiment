---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/xai/grok-voice/
  description: xai/grok-voice
  full_title: Grok Voice · Cloudflare AI docs
  head_html: <title>Grok Voice · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="xai/grok-voice"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/xai/grok-voice/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Grok Voice · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="xai/grok-voice"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/xai/grok-voice/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/xai/grok-voice/#page","headline":"Grok Voice \u00b7 Cloudflare AI docs","description":"xai/grok-voice","url":"https://developers.cloudflare.com/ai/models/xai/grok-voice/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/xai/grok-voice/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/xai.svg" alt="Xai logo" width="48" height="48">

<h1 id="grok-voice">Grok Voice</h1>

<p><code>xai/grok-voice</code></p>

xAI's real-time voice conversation model with low-latency audio input and output streaming.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>websocket</td></tr>
<tr><th>Terms</th><td><a href="https://x.ai/legal/terms-of-service">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>total_audio_minutes: 0.05, input_text_messages: 0.004</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Real-time voice conversation using WebSocket connection. This model requires a GET request with WebSocket upgrade headers instead of a POST request. The connection provides low-latency bidirectional audio streaming with server-side voice activity detection (VAD).

<section class="model-example"><strong>WebSocket Voice Session</strong>
<p>Real-time voice conversation using WebSocket connection. This model requires a GET request with WebSocket upgrade headers instead of a POST request. The connection provides low-latency bidirectional audio streaming with server-side voice activity detection (VAD).</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;websocket&quot;: true
  },
  &quot;output&quot;: {
    &quot;url&quot;: &quot;wss://api.x.ai/v1/realtime?model=grok-voice-latest&quot;,
    &quot;headers&quot;: {
      &quot;Authorization&quot;: &quot;Bearer [ephemeral_token]&quot;
    }
  },
  &quot;raw_response&quot;: {
    &quot;websocket&quot;: {
      &quot;url&quot;: &quot;wss://api.x.ai/v1/realtime?model=grok-voice-latest&quot;,
      &quot;headers&quot;: {
        &quot;Authorization&quot;: &quot;Bearer [ephemeral_token]&quot;
      }
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">// Establish WebSocket connection
const response = await fetch(
  `https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run?model=xai/grok-voice`,
  {
    method: &#x27;GET&#x27;,
    headers: {
      &#x27;Authorization&#x27;: `Bearer $CLOUDFLARE_API_TOKEN`,
      &#x27;Upgrade&#x27;: &#x27;websocket&#x27;
    }
  }
)

const ws = response.webSocket
ws.accept()

// Send audio chunks
ws.send(JSON.stringify({
  type: &#x27;input_audio_buffer.append&#x27;,
  audio: audioBase64
}))

// Receive transcriptions and audio responses
ws.addEventListener(&#x27;message&#x27;, (event) =&gt; {
  const data = JSON.parse(event.data)
  console.log(data)
})</code></pre>
<pre><code class="language-bash"># Note: WebSocket connections require a WebSocket client
# curl does not support WebSocket upgrade
# Use wscat, websocat, or a programming language WebSocket library

wscat -c &#x27;wss://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run?model=xai/grok-voice&#x27; \
  -H &#x27;Authorization: Bearer $CLOUDFLARE_API_TOKEN&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>websocket</code></td><td>boolean</td><td>Enable real-time WebSocket connection for voice conversations. When true, establishes a bidirectional WebSocket for speech-to-speech interaction with Grok voice models.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>url</code></td><td>string</td><td>Required. WebSocket URL for the realtime connection (e.g., wss://...)</td></tr><tr><td><code>headers</code></td><td>object</td><td>Optional headers to include when establishing the WebSocket connection (e.g., Authorization)</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/xai/grok-voice/schema-input.json)
- [Output schema](/ai/models/xai/grok-voice/schema-output.json)

