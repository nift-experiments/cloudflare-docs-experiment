<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 6, 2026</time><h2 id="post-title">Real-time transcription in RealtimeKit now supports 10 languages with regional variants</h2>
<div class="changelog-badges"><span>workers-ai</span><span>realtime</span></div><div class="changelog-body"><p><a href="/realtime/realtimekit/ai/transcription/">Real-time transcription</a> in RealtimeKit now supports 10 languages with regional variants, powered by <a href="/workers-ai/models/nova-3/">Deepgram Nova-3</a> running on <a href="/workers-ai/">Workers AI</a>.</p>
<p>During a meeting, participant audio is routed through <a href="/ai-gateway/">AI Gateway</a> to Nova-3 on Workers AI — so transcription runs on Cloudflare's network end-to-end, reducing latency compared to routing through external speech-to-text services.</p>
<p>Set the language when <a href="/realtime/realtimekit/concepts/meeting/">creating a meeting</a> via <code>ai_config.transcription.language</code>:</p>
<pre><code class="language-json">{&#10;	&quot;ai_config&quot;: {&#10;		&quot;transcription&quot;: {&#10;			&quot;language&quot;: &quot;fr&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Supported languages include English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch — with regional variants like <code>en-AU</code>, <code>en-GB</code>, <code>en-IN</code>, <code>en-NZ</code>, <code>es-419</code>, <code>fr-CA</code>, <code>de-CH</code>, <code>pt-BR</code>, and <code>pt-PT</code>. Use <code>multi</code> for automatic multilingual detection.</p>
<p>If you are building voice agents or real-time translation workflows, your agent can now transcribe in the caller's language natively — no extra services or routing logic needed.</p>
<ul>
<li><a href="/realtime/realtimekit/ai/transcription/">Transcription docs</a></li>
<li><a href="/workers-ai/models/nova-3/">Nova-3 model page</a></li>
<li><a href="/workers-ai/">Workers AI</a></li>
<li><a href="/ai-gateway/">AI Gateway</a></li>
</ul>
</div></article></div>
