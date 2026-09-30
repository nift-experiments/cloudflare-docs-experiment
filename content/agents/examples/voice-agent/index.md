<p>Build a voice agent that listens to users, thinks with an LLM, and speaks back — all in real-time over WebSocket. <span class="nb-badge">Beta</span></p>
<p>By the end of this guide you will have:</p>
<ul>
<li>A server-side voice agent with speech-to-text and text-to-speech</li>
<li>An LLM-powered <code>onTurn</code> handler that streams responses</li>
<li>Tools that the agent can call during conversation</li>
<li>A React client with a push-to-talk style UI</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A Cloudflare account with <a href="/workers-ai/">Workers AI</a> access</li>
<li>Node.js 18+</li>
</ul>
<h2 id="1-create-the-project"><ol>
<li>Create the project</li>
</ol></h2>
<p>Scaffold a new Workers project with Vite and React, then add the voice dependencies:</p>
<pre><code class="language-sh">npm create cloudflare@latest voice-agent -- --template cloudflare/agents-starter&#10;cd voice-agent&#10;npm install @cloudflare/voice&#10;</code></pre>
<p>The starter gives you a working Vite + React + Cloudflare Workers setup. You will replace the server and client code in the following steps.</p>
<h2 id="2-configure-wrangler"><ol start="2">
<li>Configure wrangler</li>
</ol></h2>
<p>Update <code>wrangler.jsonc</code> to include a Workers AI binding and a Durable Object for your voice agent:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1899.md")
</div>
<h2 id="3-build-the-server"><ol start="3">
<li>Build the server</li>
</ol></h2>
<p>Replace <code>src/server.ts</code> with the following. The <code>withVoice</code> mixin adds the full voice pipeline — STT, sentence chunking, TTS, and conversation persistence — to a standard <code>Agent</code> class.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1900.md")
</div>
<p>Key points:</p>
<ul>
<li><code>WorkersAIFluxSTT</code> handles continuous speech-to-text — the model detects when the user finishes speaking.</li>
<li><code>WorkersAITTS</code> converts the LLM response to audio, sentence by sentence.</li>
<li><code>onTurn</code> receives the transcript and returns a stream. The mixin handles chunking the stream into sentences and synthesizing each one.</li>
<li><code>onCallStart</code> sends a greeting when the user connects.</li>
<li><code>context.messages</code> contains completed conversation history before the current transcript.</li>
<li><code>context.signal</code> is aborted if the user interrupts or disconnects.</li>
</ul>
<h2 id="4-build-the-client"><ol start="4">
<li>Build the client</li>
</ol></h2>
<p>Replace <code>src/client.tsx</code> with a React component using the <code>useVoiceAgent</code> hook. The hook manages the WebSocket connection, mic capture, audio playback, and interrupt detection.</p>
<pre><code class="language-tsx">import { useVoiceAgent } from &quot;@cloudflare/voice/react&quot;;&#10;&#10;function App() {&#10;	const {&#10;		status,&#10;		transcript,&#10;		interimTranscript,&#10;		metrics,&#10;		audioLevel,&#10;		isMuted,&#10;		startCall,&#10;		endCall,&#10;		toggleMute,&#10;	} = useVoiceAgent({ agent: &quot;MyVoiceAgent&quot; });&#10;&#10;	return (&#10;		&lt;div&gt;&#10;			&lt;h1&gt;Voice Agent&lt;/h1&gt;&#10;			&lt;p&gt;Status: {status}&lt;/p&gt;&#10;&#10;			&lt;div&gt;&#10;				&lt;button onClick={status === &quot;idle&quot; ? startCall : endCall}&gt;&#10;					{status === &quot;idle&quot; ? &quot;Start Call&quot; : &quot;End Call&quot;}&#10;				&lt;/button&gt;&#10;				{status !== &quot;idle&quot; &amp;&amp; (&#10;					&lt;button onClick={toggleMute}&gt;{isMuted ? &quot;Unmute&quot; : &quot;Mute&quot;}&lt;/button&gt;&#10;				)}&#10;			&lt;/div&gt;&#10;&#10;			{interimTranscript &amp;&amp; (&#10;				&lt;p&gt;&#10;					&lt;em&gt;{interimTranscript}&lt;/em&gt;&#10;				&lt;/p&gt;&#10;			)}&#10;&#10;			{transcript.map((msg, i) =&gt; (&#10;				&lt;p key={i}&gt;&#10;					&lt;strong&gt;{msg.role}:&lt;/strong&gt; {msg.text}&#10;				&lt;/p&gt;&#10;			))}&#10;&#10;			{metrics &amp;&amp; (&#10;				&lt;p&gt;&#10;					LLM: {metrics.llm_ms}ms | TTS: {metrics.tts_ms}ms | First audio:{&quot; &quot;}&#10;					{metrics.first_audio_ms}ms&#10;				&lt;/p&gt;&#10;			)}&#10;		&lt;/div&gt;&#10;	);&#10;}&#10;</code></pre>
<p>The <code>status</code> field cycles through <code>&quot;idle&quot;</code> → <code>&quot;listening&quot;</code> → <code>&quot;thinking&quot;</code> → <code>&quot;speaking&quot;</code> → <code>&quot;listening&quot;</code>, giving you everything you need to build a responsive UI.</p>
<h2 id="5-run-it"><ol start="5">
<li>Run it</li>
</ol></h2>
<pre><code class="language-sh">npm run dev&#10;</code></pre>
<p>Open the app in your browser, select <strong>Start Call</strong>, and speak. You will see the transcript appear in real time, and the agent's response will play through your speakers.</p>
<h2 id="adding-pipeline-hooks">Adding pipeline hooks</h2>
<p>You can intercept and transform data at each stage of the pipeline. For example, filter out short transcripts (noise) and adjust pronunciation before TTS:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1901.md")
</div>
<p>Returning <code>null</code> from <code>afterTranscribe</code> drops the utterance entirely — useful for filtering noise or very short transcripts.</p>
<h2 id="using-third-party-providers">Using third-party providers</h2>
<p>Swap in third-party STT or TTS providers without changing your agent logic:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1902.md")
</div>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/communication-channels/voice/"><h3 id="card-voice-agents-api-reference-agents-communication-channels-voice">Voice agents API reference</h3><p>Full reference for withVoice, withVoiceInput, React hooks, VoiceClient, and all providers.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/communication-channels/chat/chat-agents/"><h3 id="card-chat-agents-agents-communication-channels-chat-chat-agents">Chat agents</h3><p>Build text-based AI chat with AIChatAgent and useAgentChat.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/operations/using-ai-models/"><h3 id="card-using-ai-models-agents-runtime-operations-using-ai-models">Using AI models</h3><p>Use Workers AI, OpenAI, Anthropic, Gemini, or any provider with your agents.</p></a></p>
