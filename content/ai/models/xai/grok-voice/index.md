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

