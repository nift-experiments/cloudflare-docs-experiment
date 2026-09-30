<p>This tutorial builds a voice agent that you can talk to and that answers out loud from your <a href="/ai-search/">AI Search</a> knowledge base. It uses the <a href="/agents/">Cloudflare Agents</a> <a href="/agents/communication-channels/voice/"><code>@cloudflare/voice</code></a> package for the speech pipeline, and AI Search as the agent's knowledge base, exposed as a retrieval tool the agent's model calls.</p>
<p><strong>What you will build:</strong> A voice agent that transcribes your speech, calls AI Search to retrieve relevant content from your indexed knowledge base, generates a grounded answer, and speaks it back.</p>
<h2 id="how-it-works">How it works</h2>
<p>The <code>@cloudflare/voice</code> package adds a full voice pipeline to a Cloudflare Agent: speech-to-text (STT), a &quot;turn&quot; handler where you produce a reply, and text-to-speech (TTS). The pipeline runs in a single Worker backed by a Durable Object, and the browser connects to it over a WebSocket.</p>
<p>The one method you write is <code>onTurn()</code>, which receives the user's transcript and returns the text to speak. This is where AI Search fits in: you run a language model and give it AI Search as a retrieval tool. The model decides when to search your knowledge base, grounds its reply in the results it gets back, and returns the answer text, which the pipeline speaks.</p>
<div class="nb-interactive-component" data-cf-component="AiSearchVoiceDiagram"></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2999.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3000.md")
</div></details>
<p>You also need an AI Search instance that already contains indexed content. This is the knowledge base you will speak to. To create one and add content, refer to <a href="/ai-search/get-started/">Get started</a>.</p>
<h2 id="1-create-the-voice-agent"><ol>
<li>Create the voice agent</li>
</ol></h2>
<p>Scaffold a Cloudflare Agents project with the voice starter template, which includes the Durable Object wiring and a React client:</p>
<pre><code class="language-sh">npm create cloudflare@latest voice-knowledge-base -- --template cloudflare/agents-starter&#10;cd voice-knowledge-base&#10;</code></pre>
<p>Install the voice package:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/voice</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/voice" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/voice</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/voice" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/voice</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/voice" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/voice</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/voice" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The <a href="/agents/communication-channels/voice/"><code>@cloudflare/voice</code></a> package provides the <code>withVoice</code> mixin and the Workers AI providers (<code>WorkersAIFluxSTT</code> and <code>WorkersAITTS</code>). For a full walkthrough of the voice agent itself, including the browser client, refer to the <a href="/agents/examples/voice-agent/">Voice agent example</a>.</p>
<h2 id="2-add-the-ai-search-binding"><ol start="2">
<li>Add the AI Search binding</li>
</ol></h2>
<p>Add an <a href="/ai-search/api/search/workers-binding/">AI Search binding</a> to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, alongside the Workers AI binding and the agent's Durable Object. Replace <code>my-instance</code> with the name of your instance.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3001.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2998.md")
</aside>
<p>Regenerate your binding types so <code>env.AI</code> and <code>env.AI_SEARCH</code> are typed:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler types" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="3-answer-from-your-knowledge-base"><ol start="3">
<li>Answer from your knowledge base</li>
</ol></h2>
<p>Update <code>src/server.ts</code>. Build the agent with the <code>withVoice</code> mixin, set the STT and TTS providers, and in <code>onTurn()</code> run a Workers AI model that calls AI Search as a retrieval tool.</p>
<p>The model is given a <code>searchKnowledgeBase</code> tool that calls AI Search's <code>search()</code> for retrieval. It calls the tool when it needs facts from your knowledge base, grounds its answer in the returned chunks, and you return the generated text for the pipeline to speak. The agent stores conversation history automatically, so you can pass <code>context.messages</code> for follow-up questions.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3002.md")
</div>
<p>Each chunk returned by <code>search()</code> includes its source item and a relevance score, so you can surface citations or log what the agent retrieved.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2997.md")
</aside>
<h2 id="4-build-the-client"><ol start="4">
<li>Build the client</li>
</ol></h2>
<p>Replace <code>src/client.tsx</code> with a React component that uses the <a href="/agents/communication-channels/voice/"><code>useVoiceAgent</code></a> hook. The hook manages the microphone, the WebSocket connection to your agent, audio playback, and interrupt detection, so the component only needs to render controls. Set <code>agent</code> to your agent class name, <code>TalkToDocs</code>.</p>
<pre><code class="language-tsx">import { useVoiceAgent } from &quot;@cloudflare/voice/react&quot;;&#10;&#10;function App() {&#10;	// useVoiceAgent connects to your agent over WebSocket, captures the&#10;	// microphone, plays the spoken response, and exposes the live call state.&#10;	// `agent` matches your Durable Object class name.&#10;	const {&#10;		// Pipeline state: &quot;idle&quot; | &quot;listening&quot; | &quot;thinking&quot; | &quot;speaking&quot;.&#10;		status,&#10;		// Finalized conversation turns (your speech and the agent&#x27;s replies).&#10;		transcript,&#10;		// Live partial transcription of what you are currently saying.&#10;		interimTranscript,&#10;		// Whether the WebSocket connection to the agent is open.&#10;		connected,&#10;		startCall,&#10;		endCall,&#10;		toggleMute,&#10;		isMuted,&#10;	} = useVoiceAgent({ agent: &quot;TalkToDocs&quot; });&#10;&#10;	const inCall = status !== &quot;idle&quot;;&#10;&#10;	return (&#10;		&lt;div&gt;&#10;			&lt;h1&gt;Talk to your knowledge base&lt;/h1&gt;&#10;&#10;			{/* Shows &quot;thinking&quot; while the agent searches the KB and generates a reply. */}&#10;			&lt;p&gt;Status: {status}&lt;/p&gt;&#10;&#10;			{/* Toggle the call. Disabled until the agent connection is open. */}&#10;			&lt;button&#10;				onClick={inCall ? endCall : startCall}&#10;				disabled={!connected &amp;&amp; !inCall}&#10;			&gt;&#10;				{!connected ? &quot;Connecting…&quot; : inCall ? &quot;End call&quot; : &quot;Start call&quot;}&#10;			&lt;/button&gt;&#10;&#10;			{/* Mute only applies once a call is active. */}&#10;			{inCall &amp;&amp; (&#10;				&lt;button onClick={toggleMute}&gt;{isMuted ? &quot;Unmute&quot; : &quot;Mute&quot;}&lt;/button&gt;&#10;			)}&#10;&#10;			{/* Lightweight loading state while the agent works on a reply. */}&#10;			{status === &quot;thinking&quot; &amp;&amp; &lt;p&gt;Thinking…&lt;/p&gt;}&#10;&#10;			{/* Live partial transcript, updated as you speak. */}&#10;			{interimTranscript &amp;&amp; (&#10;				&lt;p&gt;&#10;					&lt;em&gt;{interimTranscript}&lt;/em&gt;&#10;				&lt;/p&gt;&#10;			)}&#10;&#10;			{/* Finalized turns from both you and the agent. */}&#10;			{transcript.map((message, index) =&gt; (&#10;				&lt;p key={index}&gt;&#10;					&lt;strong&gt;{message.role}:&lt;/strong&gt; {message.text}&#10;				&lt;/p&gt;&#10;			))}&#10;		&lt;/div&gt;&#10;	);&#10;}&#10;&#10;export default App;&#10;</code></pre>
<p>The hook handles the microphone and playback, so there is no push-to-talk button. The model detects when you finish speaking, runs <code>onTurn()</code>, and plays the spoken answer back automatically.</p>
<h2 id="5-run-it-locally"><ol start="5">
<li>Run it locally</li>
</ol></h2>
<p>Start a local development server:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm run dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm run dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn run dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn run dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm run dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm run dev" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Open the app in your browser, select <strong>Start call</strong> and allow microphone access, then ask a question that your content can answer. You will see your words transcribed in real time, and the agent speaks its answer from your knowledge base. The <code>status</code> value moves through <code>listening</code>, <code>thinking</code>, and <code>speaking</code> as it works.</p>
<h2 id="6-deploy"><ol start="6">
<li>Deploy</li>
</ol></h2>
<p>Deploy your agent to make it available on the Internet:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deploy" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="talk-to-your-knowledge-base-with-multiple-people">Talk to your knowledge base with multiple people</h2>
<p>This tutorial builds a single-user voice agent. If you instead need several people in a live room talking to your knowledge base together, use <a href="/realtime/realtimekit/">RealtimeKit</a> for the multi-party audio and video layer, and keep this voice agent as the component that answers from AI Search. RealtimeKit provides the meeting room and transcription, but it does not host the answer engine.</p>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/communication-channels/voice/"><h3 id="card-voice-agents-api-reference-agents-communication-channels-voice">Voice agents API reference</h3><p>The @cloudflare/voice pipeline, providers, and onTurn contract.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/examples/voice-agent/"><h3 id="card-voice-agent-example-agents-examples-voice-agent">Voice agent example</h3><p>A full walkthrough of the voice agent and its browser client.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/api/search/workers-binding/"><h3 id="card-search-workers-binding-ai-search-api-search-workers-binding">Search Workers binding</h3><p>Full reference for chatCompletions() and search() from a Worker.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/how-to/bring-your-own-generation-model/"><h3 id="card-bring-your-own-generation-model-ai-search-how-to-bring-your-own-generation-model">Bring your own generation model</h3><p>Use a third-party model for generation while AI Search handles retrieval.</p></a></p>
