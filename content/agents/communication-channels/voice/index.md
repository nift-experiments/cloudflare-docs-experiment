---
cp9:
  canonical: https://developers.cloudflare.com/agents/communication-channels/voice/
  description: Build real-time voice agents with speech-to-text, text-to-speech, and conversation persistence over WebSocket.
  full_title: Voice · Cloudflare Agents docs
  head_html: <title>Voice · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Build real-time voice agents with speech-to-text, text-to-speech, and conversation persistence over WebSocket."><link rel="canonical" href="https://developers.cloudflare.com/agents/communication-channels/voice/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/communication-channels/voice/index.md"><meta property="og:title" content="Voice · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build real-time voice agents with speech-to-text, text-to-speech, and conversation persistence over WebSocket."><meta property="og:url" content="https://developers.cloudflare.com/agents/communication-channels/voice/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/communication-channels/voice/#page","headline":"Voice \u00b7 Cloudflare Agents docs","description":"Build real-time voice agents with speech-to-text, text-to-speech, and conversation persistence over WebSocket.","url":"https://developers.cloudflare.com/agents/communication-channels/voice/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/communication-channels/voice/
  schema: 1
---
<p>Build real-time voice agents with speech-to-text, text-to-speech, and conversation persistence. Audio streams over WebSocket — no SFU or meeting infrastructure required. <span class="nb-badge">Beta</span></p>
<h2 id="overview">Overview</h2>
<p><code>@cloudflare/voice</code> provides two server-side mixins and matching client libraries:</p>
<table>
<thead>
<tr>
<th>Export</th>
<th>Import</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>withVoice</code></td>
<td><code>@cloudflare/voice</code></td>
<td>Full voice agent: STT, LLM, TTS, persistence</td>
</tr>
<tr>
<td><code>withVoiceInput</code></td>
<td><code>@cloudflare/voice</code></td>
<td>STT-only: transcription without response</td>
</tr>
<tr>
<td><code>useVoiceAgent</code></td>
<td><code>@cloudflare/voice/react</code></td>
<td>React hook for <code>withVoice</code> agents</td>
</tr>
<tr>
<td><code>useVoiceInput</code></td>
<td><code>@cloudflare/voice/react</code></td>
<td>React hook for <code>withVoiceInput</code> agents</td>
</tr>
<tr>
<td><code>VoiceClient</code></td>
<td><code>@cloudflare/voice/client</code></td>
<td>Framework-agnostic client</td>
</tr>
</tbody>
</table>
<p>Built on Cloudflare Durable Objects, you get:</p>
<ul>
<li><strong>Real-time audio</strong> — mic audio streams as binary WebSocket frames, TTS audio streams back</li>
<li><strong>Automatic conversation persistence</strong> — messages stored in SQLite, survive restarts</li>
<li><strong>Streaming TTS</strong> — LLM tokens are sentence-chunked and synthesized concurrently</li>
<li><strong>Interruption handling</strong> — user speech during playback cancels the current response</li>
<li><strong>Continuous STT</strong> — per-call transcriber session, model handles turn detection</li>
<li><strong>Pipeline hooks</strong> — intercept and transform text at every stage</li>
</ul>
<h2 id="quick-start">Quick start</h2>
<h3 id="install">Install</h3>
<pre tabindex="0"><code class="language-sh">npm install @cloudflare/voice agents&#10;</code></pre>
<h3 id="server">Server</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1963.md")
</div>
<h3 id="client-react">Client (React)</h3>
<pre tabindex="0"><code class="language-tsx">import { useVoiceAgent } from &quot;@cloudflare/voice/react&quot;;&#10;&#10;function VoiceUI() {&#10;	const {&#10;		status,&#10;		transcript,&#10;		interimTranscript,&#10;		audioLevel,&#10;		isMuted,&#10;		startCall,&#10;		endCall,&#10;		toggleMute,&#10;	} = useVoiceAgent({ agent: &quot;MyAgent&quot; });&#10;&#10;	return (&#10;		&lt;div&gt;&#10;			&lt;p&gt;Status: {status}&lt;/p&gt;&#10;&#10;			&lt;button onClick={status === &quot;idle&quot; ? startCall : endCall}&gt;&#10;				{status === &quot;idle&quot; ? &quot;Start Call&quot; : &quot;End Call&quot;}&#10;			&lt;/button&gt;&#10;&#10;			&lt;button onClick={toggleMute}&gt;{isMuted ? &quot;Unmute&quot; : &quot;Mute&quot;}&lt;/button&gt;&#10;&#10;			{interimTranscript &amp;&amp; (&#10;				&lt;p&gt;&#10;					&lt;em&gt;{interimTranscript}&lt;/em&gt;&#10;				&lt;/p&gt;&#10;			)}&#10;&#10;			{transcript.map((msg, i) =&gt; (&#10;				&lt;p key={i}&gt;&#10;					&lt;strong&gt;{msg.role}:&lt;/strong&gt; {msg.text}&#10;				&lt;/p&gt;&#10;			))}&#10;		&lt;/div&gt;&#10;	);&#10;}&#10;</code></pre>
<h3 id="wrangler-configuration">Wrangler configuration</h3>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1964.md")
</div>
<h2 id="how-it-works">How it works</h2>
<pre tabindex="0"><code class="language-txt">Browser                              Durable Object (withVoice)&#10;┌──────────┐                         ┌──────────────────────────┐&#10;│ Mic      │   binary PCM (16kHz)    │ Transcriber session      │&#10;│          │ ──────────────────────► │ (per-call, continuous)   │&#10;│          │                         │   ↓ model detects turn   │&#10;│          │   JSON: transcript      │ onTurn() → your LLM code │&#10;│          │ ◄────────────────────── │   ↓ (sentence chunking)  │&#10;│          │   binary: audio         │ TTS                      │&#10;│ Speaker  │ ◄────────────────────── │                          │&#10;└──────────┘                         └──────────────────────────┘&#10;</code></pre>
<ol>
<li>The client captures mic audio and sends it as binary WebSocket frames (16kHz mono 16-bit PCM).</li>
<li>Audio streams continuously to the transcriber session (created at <code>start_call</code>, lives for the entire call).</li>
<li>The STT model detects when the user finishes an utterance and fires <code>onUtterance</code>. All providers use <strong>model-driven turn detection</strong> — the client does not need to signal end-of-speech for STT.</li>
<li>Your <code>onTurn()</code> method runs — typically an LLM call.</li>
<li>The response is sentence-chunked and synthesized via TTS.</li>
<li>Audio streams back to the client for playback.</li>
</ol>
<p>The client receives <code>transcript_interim</code> messages with partial results as the user speaks, so you can show real-time feedback in the UI.</p>
<h2 id="server-api-withvoice">Server API: <code>withVoice</code></h2>
<p><code>withVoice(Agent)</code> adds the full voice pipeline to an Agent class.</p>
<h3 id="providers">Providers</h3>
<p>Set providers as class properties. Class field initializers run after <code>super()</code>, so <code>this.env</code> is available.</p>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>transcriber</code></td>
<td><code>Transcriber</code></td>
<td>Yes</td>
<td>Continuous per-call STT provider</td>
</tr>
<tr>
<td><code>tts</code></td>
<td><code>TTSProvider</code></td>
<td>Yes</td>
<td>Text-to-speech</td>
</tr>
</tbody>
</table>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1965.md")
</div>
<p>For runtime model switching (for example, a Flux vs Nova 3 dropdown), override <code>createTranscriber</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1966.md")
</div>
<h3 id="onturn-transcript-context"><code>onTurn(transcript, context)</code></h3>
<p><strong>Required.</strong> Called when the user finishes speaking and the transcript is ready. <code>context.messages</code> contains completed conversation history before this transcript. Append <code>transcript</code> exactly once when constructing an LLM message list.</p>
<p>Return a <code>string</code>, <code>AsyncIterable&lt;string&gt;</code>, or <code>ReadableStream</code> for streaming responses.</p>
<p><strong>Simple response:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1967.md")
</div>
<p><strong>Streaming response (recommended for LLM):</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1968.md")
</div>
<p>The <code>context</code> object provides:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>connection</code></td>
<td><code>Connection</code></td>
<td>The WebSocket connection</td>
</tr>
<tr>
<td><code>messages</code></td>
<td><code>Array&lt;{ role: string; content: string }&gt;</code></td>
<td>Completed history before the transcript</td>
</tr>
<tr>
<td><code>signal</code></td>
<td><code>AbortSignal</code></td>
<td>Aborted on interrupt or disconnect</td>
</tr>
</tbody>
</table>
<h3 id="lifecycle-hooks">Lifecycle hooks</h3>
<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>beforeCallStart(connection)</code></td>
<td>Return <code>false</code> to reject the call</td>
</tr>
<tr>
<td><code>onCallStart(connection)</code></td>
<td>Called after a call is accepted</td>
</tr>
<tr>
<td><code>onCallEnd(connection)</code></td>
<td>Called when a call ends</td>
</tr>
<tr>
<td><code>onInterrupt(connection)</code></td>
<td>Called when user interrupts during playback</td>
</tr>
</tbody>
</table>
<h3 id="pipeline-hooks">Pipeline hooks</h3>
<p>Intercept and transform data at each pipeline stage. Return <code>null</code> to skip the current utterance.</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Receives</th>
<th>Can skip?</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>afterTranscribe(transcript, connection)</code></td>
<td>STT text</td>
<td>Yes</td>
</tr>
<tr>
<td><code>beforeSynthesize(text, connection)</code></td>
<td>Text before TTS</td>
<td>Yes</td>
</tr>
<tr>
<td><code>afterSynthesize(audio, text, connection)</code></td>
<td>Audio after TTS</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1969.md")
</div>
<h3 id="convenience-methods">Convenience methods</h3>
<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>speak(connection, text)</code></td>
<td>Synthesize and send audio to one connection</td>
</tr>
<tr>
<td><code>speakAll(text)</code></td>
<td>Synthesize and send audio to all connections</td>
</tr>
<tr>
<td><code>forceEndCall(connection)</code></td>
<td>Programmatically end a call</td>
</tr>
<tr>
<td><code>saveMessage(role, text)</code></td>
<td>Persist a message to conversation history</td>
</tr>
<tr>
<td><code>getConversationHistory()</code></td>
<td>Retrieve conversation history from SQLite</td>
</tr>
</tbody>
</table>
<h3 id="configuration-options">Configuration options</h3>
<p>Pass options to <code>withVoice()</code> as the second argument:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1970.md")
</div>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>historyLimit</code></td>
<td><code>number</code></td>
<td><code>20</code></td>
<td>Max messages loaded for context</td>
</tr>
<tr>
<td><code>audioFormat</code></td>
<td><code>string</code></td>
<td><code>&quot;mp3&quot;</code></td>
<td>Audio format sent to client</td>
</tr>
<tr>
<td><code>maxMessageCount</code></td>
<td><code>number</code></td>
<td><code>1000</code></td>
<td>Max messages stored in SQLite</td>
</tr>
</tbody>
</table>
<h2 id="server-api-withvoiceinput">Server API: <code>withVoiceInput</code></h2>
<p><code>withVoiceInput(Agent)</code> adds STT-only voice input — no TTS, no LLM, no response generation. Use this for dictation, search-by-voice, or any UI where you need speech-to-text without a conversational agent.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1971.md")
</div>
<h3 id="ontranscript-text-connection"><code>onTranscript(text, connection)</code></h3>
<p>Called after each utterance is transcribed. Override this to process the transcript.</p>
<h3 id="hooks">Hooks</h3>
<p><code>withVoiceInput</code> supports the same lifecycle hooks as <code>withVoice</code>:</p>
<ul>
<li><code>beforeCallStart(connection)</code> — return <code>false</code> to reject</li>
<li><code>onCallStart(connection)</code>, <code>onCallEnd(connection)</code>, <code>onInterrupt(connection)</code></li>
<li><code>createTranscriber(connection)</code> — override for runtime model switching</li>
<li><code>afterTranscribe(transcript, connection)</code> — filter or transform transcripts</li>
</ul>
<p>It does <strong>not</strong> have TTS hooks (<code>beforeSynthesize</code>, <code>afterSynthesize</code>) or <code>onTurn</code>.</p>
<h2 id="client-api-react-hooks">Client API: React hooks</h2>
<h3 id="usevoiceagent"><code>useVoiceAgent</code></h3>
<p>Wraps <code>VoiceClient</code> for <code>withVoice</code> agents. Manages connection, mic capture, playback, silence detection, and interrupt detection.</p>
<pre tabindex="0"><code class="language-tsx">import { useVoiceAgent } from &quot;@cloudflare/voice/react&quot;;&#10;&#10;const selectedSpeakerId = &quot;default&quot;;&#10;&#10;const {&#10;	status, // &quot;idle&quot; | &quot;listening&quot; | &quot;thinking&quot; | &quot;speaking&quot;&#10;	transcript, // TranscriptMessage[] — conversation history&#10;	interimTranscript, // string | null — real-time partial transcript&#10;	metrics, // VoicePipelineMetrics | null&#10;	audioLevel, // number (0–1) — current mic RMS level&#10;	isMuted, // boolean&#10;	connected, // boolean — WebSocket connected&#10;	error, // string | null&#10;	outputDeviceError, // string | null — non-fatal speaker routing issue&#10;	startCall, // () =&gt; Promise&lt;void&gt;&#10;	endCall, // () =&gt; void&#10;	toggleMute, // () =&gt; void&#10;	sendText, // (text: string) =&gt; void — bypass STT&#10;	sendJSON, // (data: Record&lt;string, unknown&gt;) =&gt; void&#10;	lastCustomMessage, // unknown — last non-voice message from server&#10;} = useVoiceAgent({&#10;	agent: &quot;MyAgent&quot;,&#10;	name: &quot;default&quot;,&#10;	host: window.location.host,&#10;	outputDeviceId: selectedSpeakerId, // Optional audiooutput device ID&#10;	enabled: true,&#10;});&#10;</code></pre>
<p>Use <code>enabled: false</code> when the app must wait for async connection prerequisites, such as a user-scoped capability token. While disabled, the hook does not create or connect a <code>VoiceClient</code>, returns the idle disconnected state, and action callbacks such as <code>startCall()</code>, <code>sendText()</code>, and <code>sendJSON()</code> are safe no-ops.</p>
<p>When <code>enabled</code> changes to <code>true</code>, the hook connects with the current options. The first enable is treated as an initial connection, so <code>onReconnect</code> only fires for later connection identity changes while the hook remains enabled.</p>
<h4 id="output-device-selection">Output device selection</h4>
<p>Pass <code>outputDeviceId</code> to route assistant playback to a selected speaker when the browser supports <code>HTMLMediaElement.setSinkId()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1972.md")
</div>
<p>Use a <code>MediaDeviceInfo.deviceId</code> from <code>navigator.mediaDevices.enumerateDevices()</code> where <code>kind === &quot;audiooutput&quot;</code>. <code>&quot;default&quot;</code> and <code>undefined</code> use the system default output. Browsers without sink selection support continue playing through the default output and set <code>outputDeviceError</code> when a non-default output is requested. Device labels may be blank until the user grants microphone permission, so refresh device lists after <code>startCall()</code> if you show a speaker picker.</p>
<h4 id="tuning-options">Tuning options</h4>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>enabled</code></td>
<td><code>boolean</code></td>
<td><code>true</code></td>
<td>Delay client creation and connection when false</td>
</tr>
<tr>
<td><code>silenceThreshold</code></td>
<td><code>number</code></td>
<td><code>0.04</code></td>
<td>RMS below this is silence</td>
</tr>
<tr>
<td><code>silenceDurationMs</code></td>
<td><code>number</code></td>
<td><code>500</code></td>
<td>Silence duration before <code>end_of_speech</code> (ms)</td>
</tr>
<tr>
<td><code>interruptThreshold</code></td>
<td><code>number</code></td>
<td><code>0.05</code></td>
<td>RMS to detect speech during playback</td>
</tr>
<tr>
<td><code>interruptChunks</code></td>
<td><code>number</code></td>
<td><code>2</code></td>
<td>Consecutive high-RMS chunks to trigger interrupt</td>
</tr>
</tbody>
</table>
<p>Changing tuning options triggers a client reconnect (the connection key includes them).</p>
<h3 id="usevoiceinput"><code>useVoiceInput</code></h3>
<p>Lightweight hook for dictation and voice-to-text. Accumulates user transcripts into a single string.</p>
<pre tabindex="0"><code class="language-tsx">import { useVoiceInput } from &quot;@cloudflare/voice/react&quot;;&#10;&#10;function Dictation() {&#10;	const {&#10;		transcript, // string — accumulated text from all utterances&#10;		interimTranscript, // string | null — current partial transcript&#10;		isListening, // boolean&#10;		audioLevel, // number (0–1)&#10;		isMuted, // boolean&#10;		error, // string | null&#10;		start, // () =&gt; Promise&lt;void&gt;&#10;		stop, // () =&gt; void&#10;		toggleMute, // () =&gt; void&#10;		clear, // () =&gt; void — clear accumulated transcript&#10;	} = useVoiceInput({ agent: &quot;DictationAgent&quot; });&#10;&#10;	return (&#10;		&lt;div&gt;&#10;			&lt;textarea&#10;				value={transcript + (interimTranscript ? &quot; &quot; + interimTranscript : &quot;&quot;)}&#10;				readOnly&#10;			/&gt;&#10;			&lt;button onClick={isListening ? stop : start}&gt;&#10;				{isListening ? &quot;Stop&quot; : &quot;Dictate&quot;}&#10;			&lt;/button&gt;&#10;		&lt;/div&gt;&#10;	);&#10;}&#10;</code></pre>
<h2 id="client-api-voiceclient">Client API: <code>VoiceClient</code></h2>
<p>Framework-agnostic client for environments without React.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1973.md")
</div>
<h3 id="events">Events</h3>
<table>
<thead>
<tr>
<th>Event</th>
<th>Data type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>statuschange</code></td>
<td><code>VoiceStatus</code></td>
<td>Pipeline state changed</td>
</tr>
<tr>
<td><code>transcriptchange</code></td>
<td><code>TranscriptMessage[]</code></td>
<td>Transcript updated</td>
</tr>
<tr>
<td><code>interimtranscript</code></td>
<td><code>string | null</code></td>
<td>Interim transcript from streaming STT</td>
</tr>
<tr>
<td><code>metricschange</code></td>
<td><code>VoicePipelineMetrics</code></td>
<td>Pipeline timing metrics</td>
</tr>
<tr>
<td><code>audiolevelchange</code></td>
<td><code>number</code></td>
<td>Mic audio level (0–1)</td>
</tr>
<tr>
<td><code>connectionchange</code></td>
<td><code>boolean</code></td>
<td>WebSocket connected/disconnected</td>
</tr>
<tr>
<td><code>mutechange</code></td>
<td><code>boolean</code></td>
<td>Mute state changed</td>
</tr>
<tr>
<td><code>error</code></td>
<td><code>string | null</code></td>
<td>Error occurred</td>
</tr>
<tr>
<td><code>outputdeviceerror</code></td>
<td><code>string | null</code></td>
<td>Non-fatal speaker routing issue</td>
</tr>
<tr>
<td><code>custommessage</code></td>
<td><code>unknown</code></td>
<td>Non-voice message from server</td>
</tr>
</tbody>
</table>
<h3 id="advanced-options">Advanced options</h3>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>transport</code></td>
<td><code>VoiceTransport</code></td>
<td>Custom transport (default: WebSocket via PartySocket)</td>
</tr>
<tr>
<td><code>audioInput</code></td>
<td><code>VoiceAudioInput</code></td>
<td>Custom mic capture (default: built-in AudioWorklet)</td>
</tr>
<tr>
<td><code>preferredFormat</code></td>
<td><code>VoiceAudioFormat</code></td>
<td>Hint for server audio format (advisory only)</td>
</tr>
<tr>
<td><code>outputDeviceId</code></td>
<td><code>string</code></td>
<td>Preferred <code>audiooutput</code> device for assistant playback</td>
</tr>
</tbody>
</table>
<h2 id="providers-1">Providers</h2>
<h3 id="built-in-workers-ai">Built-in (Workers AI)</h3>
<p>No API keys required — use your Workers AI binding:</p>
<table>
<thead>
<tr>
<th>Class</th>
<th>Type</th>
<th>Default model</th>
<th>Recommended for</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>WorkersAIFluxSTT</code></td>
<td>Continuous STT</td>
<td><code>@cf/deepgram/flux</code></td>
<td><code>withVoice</code></td>
</tr>
<tr>
<td><code>WorkersAINova3STT</code></td>
<td>Continuous STT</td>
<td><code>@cf/deepgram/nova-3</code></td>
<td><code>withVoiceInput</code></td>
</tr>
<tr>
<td><code>WorkersAITTS</code></td>
<td>TTS</td>
<td><code>@cf/deepgram/aura-1</code></td>
<td>Both</td>
</tr>
</tbody>
</table>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1974.md")
</div>
<h3 id="third-party-providers">Third-party providers</h3>
<table>
<thead>
<tr>
<th>Package</th>
<th>Class</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cloudflare/voice-deepgram</code></td>
<td><code>DeepgramSTT</code></td>
<td>Continuous STT</td>
</tr>
<tr>
<td><code>@cloudflare/voice-elevenlabs</code></td>
<td><code>ElevenLabsTTS</code></td>
<td>High-quality TTS</td>
</tr>
<tr>
<td><code>@cloudflare/voice-telnyx</code></td>
<td><code>TelnyxSTT</code>, <code>TelnyxTTS</code></td>
<td>STT, TTS, and telephony</td>
</tr>
<tr>
<td><code>@cloudflare/voice-twilio</code></td>
<td><code>TwilioAdapter</code></td>
<td>Telephony (phone calls)</td>
</tr>
<tr>
<td><code>@cloudflare/voice-plivo</code></td>
<td><code>PlivoAdapter</code></td>
<td>Telephony (phone calls)</td>
</tr>
</tbody>
</table>
<p><strong>ElevenLabs TTS:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1975.md")
</div>
<p><strong>Deepgram STT:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1976.md")
</div>
<p><strong>Telnyx STT and TTS:</strong></p>
<p>Import from the <code>/stt</code> and <code>/tts</code> subpaths, which are server-safe:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1977.md")
</div>
<p><code>TelnyxTTS</code> defaults to <code>backend: &quot;rest&quot;</code>. Set <code>backend: &quot;websocket&quot;</code> for lower time-to-first-audio. That backend requires the Workers runtime.</p>
<h2 id="telephony">Telephony</h2>
<p>Telephony connects phone calls to the same <code>withVoice</code> agent that serves your browser clients. The call shares that agent instance's conversation history, state, tools, and schedules, so one agent can answer the phone and the web.</p>
<p>Providers take one of two approaches, which determines where call audio arrives and what you have to deploy:</p>
<table>
<thead>
<tr>
<th>Provider</th>
<th>Approach</th>
<th>Call audio arrives at</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td>Twilio</td>
<td>Server-side adapter in your Worker</td>
<td>Your Worker</td>
<td>Inbound numbers answered server-side</td>
</tr>
<tr>
<td>Plivo</td>
<td>Server-side adapter in your Worker</td>
<td>Your Worker</td>
<td>Inbound numbers answered server-side</td>
</tr>
<tr>
<td>Telnyx</td>
<td>Browser WebRTC bridge</td>
<td>The browser</td>
<td>Softphone and click-to-call in an app you ship</td>
</tr>
</tbody>
</table>
<h3 id="server-side-adapters-twilio-and-plivo">Server-side adapters (Twilio and Plivo)</h3>
<p>Install the adapter for your provider:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/voice-twilio</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/voice-twilio" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/voice-twilio</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/voice-twilio" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/voice-twilio</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/voice-twilio" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/voice-twilio</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/voice-twilio" aria-label="Copy to clipboard">Copy</button></div></div>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/voice-plivo</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/voice-plivo" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/voice-plivo</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/voice-plivo" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/voice-plivo</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/voice-plivo" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/voice-plivo</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/voice-plivo" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The adapter terminates the provider's audio WebSocket in your Worker and converts between the provider's 8 kHz mulaw audio and the agent's 16 kHz PCM protocol:</p>
<pre tabindex="0"><code class="language-txt">Phone → provider → WebSocket → adapter → WebSocket → VoiceAgent&#10;</code></pre>
<p>No browser is involved. Each adapter exposes a <code>handleRequest()</code> method that you call from your <code>fetch</code> handler for the provider's WebSocket path, and by default each call gets its own agent instance named after the provider's call identifier.</p>
<p>Beyond that path, the two providers differ in what they need from you. Twilio is configured with TwiML that points at your Worker. Plivo needs your auth ID, auth token, and phone number — deploying automatically provisions the Plivo application and points its answer URL at your Worker, so neither needs manual setup in the Plivo console.</p>
<h3 id="browser-webrtc-bridge-telnyx">Browser WebRTC bridge (Telnyx)</h3>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/voice-telnyx</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/voice-telnyx" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/voice-telnyx</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/voice-telnyx" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/voice-telnyx</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/voice-telnyx" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/voice-telnyx</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/voice-telnyx" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Telnyx bridges the PSTN call through WebRTC in the browser and reuses your existing voice client transport:</p>
<pre tabindex="0"><code class="language-txt">Phone ↔ Telnyx ↔ WebRTC ↔ browser bridge ↔ WebSocket → VoiceAgent&#10;</code></pre>
<p>Because the browser holds the WebRTC session, it needs a short-lived Telnyx credential — never your API key. <code>TelnyxJWTEndpoint</code> mints those tokens server-side and requires an <code>authorize</code> callback, so a public route cannot mint credentials for arbitrary callers. Telephony needs <code>TELNYX_CREDENTIAL_CONNECTION_ID</code> alongside <code>TELNYX_API_KEY</code>.</p>
<p>Telnyx also provides STT and TTS, so it can supply the whole pipeline. Refer to <a href="#third-party-providers">Third-party providers</a> for those.</p>
<h3 id="pcm-output-for-telephony">PCM output for telephony</h3>
<p><code>WorkersAITTS</code> returns MP3, which cannot be decoded to PCM in the Workers runtime. With the Twilio or Plivo adapter, use a TTS provider that outputs raw PCM — for example ElevenLabs with <code>outputFormat: &quot;pcm_16000&quot;</code>, or a Workers AI model called with <code>encoding: &quot;linear16&quot;</code> and <code>container: &quot;none&quot;</code>.</p>
<p>This constraint does not apply to Telnyx, where the browser decodes audio before playback.</p>
<h3 id="complete-examples">Complete examples</h3>
<p>Each adapter ships a runnable example with the Worker routes, provider configuration, and deployment steps:</p>
<div class="nb-card-grid">
@input("content/.markup/bodies/1978.md")
</div>
<h2 id="text-messages">Text messages</h2>
<p><code>withVoice</code> agents can also receive text messages, bypassing STT entirely. This is useful for chat-style input alongside voice.</p>
<pre tabindex="0"><code class="language-tsx">const { sendText } = useVoiceAgent({ agent: &quot;MyAgent&quot; });&#10;&#10;// Send text — goes straight to onTurn() without STT&#10;sendText(&quot;What is the weather like today?&quot;);&#10;</code></pre>
<p>Text messages work both during and outside of active calls. During a call, the response is spoken aloud via TTS. Outside a call, the response is sent as text-only transcript messages.</p>
<h2 id="custom-messages">Custom messages</h2>
<p>Send and receive application-level JSON messages alongside voice protocol messages. Non-voice messages pass through to your <code>onMessage</code> handler on the server and emit <code>custommessage</code> events on the client.</p>
<p><strong>Server:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1979.md")
</div>
<p><strong>Client:</strong></p>
<pre tabindex="0"><code class="language-tsx">const { sendJSON, lastCustomMessage } = useVoiceAgent({ agent: &quot;MyAgent&quot; });&#10;&#10;sendJSON({ type: &quot;kick_speaker&quot; });&#10;&#10;useEffect(() =&gt; {&#10;	if (lastCustomMessage) {&#10;		console.log(&quot;Custom message:&quot;, lastCustomMessage);&#10;	}&#10;}, [lastCustomMessage]);&#10;</code></pre>
<h2 id="single-speaker-enforcement">Single-speaker enforcement</h2>
<p>Use <code>beforeCallStart</code> to restrict who can start a call. This example enforces single-speaker — only one connection can be the active speaker at a time:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1980.md")
</div>
<h2 id="pipeline-metrics">Pipeline metrics</h2>
<p><code>withVoice</code> agents emit timing metrics after each turn:</p>
<pre tabindex="0"><code class="language-tsx">const { metrics } = useVoiceAgent({ agent: &quot;MyAgent&quot; });&#10;&#10;// metrics: {&#10;//   llm_ms: 850,&#10;//   tts_ms: 200,&#10;//   first_audio_ms: 950,&#10;//   total_ms: 1200,&#10;// }&#10;</code></pre>
<h2 id="conversation-history">Conversation history</h2>
<p><code>withVoice</code> automatically persists conversation messages to SQLite. In <code>onTurn()</code>, <code>context.messages</code> is a snapshot of the completed history before the current transcript. The pipeline persists the current transcript before invoking the hook. Therefore, a direct <code>getConversationHistory()</code> call inside <code>onTurn()</code> includes it.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1981.md")
</div>
<p>History survives Durable Object restarts and client reconnections. Voice agents use <code>keepAlive</code> to prevent eviction during active calls.</p>
