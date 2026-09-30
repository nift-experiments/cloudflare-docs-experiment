<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 11, 2026</time><h2 id="post-title">Inspect Voice Agent turn latency and outcomes</h2>
<div class="changelog-badges"><span>agents</span></div><div class="changelog-body"><p><code>@cloudflare/voice</code> v0.4.0 now lets you inspect where each Voice Agent turn spends time and how it ends.</p>
<pre><code class="language-ts">client.addEventListener(&quot;turnmetrics&quot;, (turn) =&gt; {&#10;	console.log(turn.outcome, turn.turnTotalMs);&#10;});&#10;</code></pre>
<h4 id="about-the-voice-package">About the Voice package</h4>
<p>The <code>@cloudflare/voice</code> package lets you build real-time voice agents with Cloudflare Agents. It streams microphone audio to an Agent over WebSocket, transcribes speech, runs your model through <code>onTurn()</code>, converts the response to speech, and streams audio back to the caller.</p>
<p>A turn moves through several stages:</p>
<pre><code class="language-txt">User speaks -&gt; speech-to-text -&gt; model -&gt; text-to-speech -&gt; audio&#10;</code></pre>
<p>Previously, the package's four aggregate metrics covered successful, non-empty speech turns. They did not show how failed, aborted, empty, or text turns ended.</p>
<h4 id="turn-metrics">Turn metrics</h4>
<p>Each speech or text turn now produces a typed <code>VoiceTurnMetrics</code> summary with:</p>
<ul>
<li>A <code>turnId</code> for correlating events from the same turn.</li>
<li>A terminal outcome such as <code>completed</code>, <code>no_output</code>, <code>output_limit</code>, <code>content_filtered</code>, <code>model_error</code>, <code>tts_error</code>, or <code>aborted</code>.</li>
<li>Timings for important stages, including speech-to-final-transcript, model-to-first-text, TTS-to-first-audio, and total turn duration.</li>
</ul>
<p>These timings can overlap and are not additive. Timings for stages that a turn did not reach are omitted.</p>
<p>The latest summary is available through <code>VoiceClient</code>, <code>useVoiceAgent()</code>, and <code>useVoiceInput()</code>. Voice input includes only the speech and transcription timings it can measure.</p>
<p>If an agent produces no audio, you can now distinguish between the model returning no output, reaching an output limit, encountering content filtering, or failing.</p>
<h4 id="additional-diagnostics">Additional diagnostics</h4>
<p>For local debugging, you can forward server lifecycle events to the browser console:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17686.md")</div>
<p>The browser console combines server lifecycle events with local microphone, connection, and playback events, including model start, first model text, first audio, and playback start. Diagnostics are off by default, and their event names and fields can change.</p>
<p><code>VoiceClient</code> also exposes typed events for speech-to-text failures, connection errors, and model outcomes. The SDK removes known content fields and does not read arbitrary provider responses, but custom error messages must not contain sensitive data.</p>
<p>Install the release with a compatible Agents SDK version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/communication-channels/voice/#pipeline-metrics">Voice pipeline metrics</a> and <a href="https://github.com/cloudflare/agents/tree/main/examples/voice-agent">Voice Agent example</a> to get started.</p>
</div></article></div>
