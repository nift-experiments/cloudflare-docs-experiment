---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/
  description: New updates and improvements at Cloudflare.
  full_title: 'Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control · Changelog'
  head_html: '<title>Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/#page","headline":"Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>'
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-13-agents-sdk-v0.12.4/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 13, 2026</time><h2 id="post-title">Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings more reliable chat recovery, fixes Agent state synchronization during reconnects, adds durable submissions for Think, exposes routing retry configuration, and adds connection control for Voice agents.</p>
<h4 id="chat-recovery-improvements">Chat recovery improvements</h4>
<p><code>@cloudflare/ai-chat</code> now keeps server turns running when a browser or client stream is interrupted. This is useful for long-running AI responses where users refresh the page, close a tab, or temporarily lose connection. Calling <code>stop()</code> still cancels the server turn.</p>
<p>Set <code>cancelOnClientAbort: true</code> if browser or client aborts should also cancel the server turn:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17661.md")</div>
<p>Notable bug fixes:</p>
<ul>
<li>Chat stream resume negotiation no longer throws when replay races with a closed WebSocket connection.</li>
<li>Recovered chat continuations no longer leave <code>useAgentChat</code> stuck in a streaming state when the original socket disconnects before a terminal response.</li>
<li>Approval auto-continuation preserves reasoning parts and persists continuation reasoning in the final message.</li>
<li><code>isServerStreaming</code> now resets correctly when a resumed stream moves from the fallback observer path to a transport-owned stream.</li>
</ul>
<h4 id="agent-state-and-routing-fixes">Agent state and routing fixes</h4>
<p><code>agents@0.12.4</code> prevents duplicate initial state frames during WebSocket connection setup. This avoids stale initial state messages overwriting state updates already sent by the client.</p>
<p>Agent recovery is also more reliable when tool calls span a Durable Object restart. Recovery now defers user finish hooks until after agent startup and isolates hook failures, so one failed hook does not block other recovered runs from finalizing.</p>
<p><code>getAgentByName()</code> now supports <code>routingRetry</code> for transient Durable Object routing failures:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17662.md")</div>
<h4 id="durable-think-submissions">Durable Think submissions</h4>
<p><code>@cloudflare/think</code> now supports durable programmatic submissions. <code>submitMessages()</code> provides durable acceptance, idempotent retries, status inspection, cancellation, and cleanup for server-driven turns that should continue after the caller returns.</p>
<p><code>Think.chat()</code> RPC turns now run inside chat recovery fibers and persist their stream chunks. Interrupted sub-agent turns can recover partial output instead of starting over.</p>
<p><code>ChatOptions.tools</code> has been removed from the TypeScript API. Define durable tools on the child agent or use agent tools for orchestration. Runtime <code>options.tools</code> values passed by legacy callers are ignored with a warning.</p>
<h4 id="think-message-pruning-behavior-change">Think message pruning behavior change</h4>
<p><code>@cloudflare/think</code> no longer applies <code>pruneMessages({ toolCalls: &quot;before-last-2-messages&quot; })</code> to model context by default. The previous default could strip client-side tool results from longer multi-turn flows.</p>
<p><code>truncateOlderMessages</code> still runs as before, so context cost remains bounded. Subclasses that relied on the old aggressive pruning can opt back in from <code>beforeTurn</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17663.md")</div>
<h4 id="voice-agent-connection-control">Voice agent connection control</h4>
<p><code>@cloudflare/voice</code> adds an <code>enabled</code> option to <code>useVoiceAgent</code>. React apps can now delay creating and connecting a <code>VoiceClient</code> until prerequisites such as capability tokens are ready.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17664.md")</div>
<p>This release also fixes Workers AI speech-to-text session edge cases and <code>withVoice</code> text streaming from AI SDK <code>textStream</code> responses.</p>
<h4 id="other-improvements">Other improvements</h4>
<ul>
<li><strong>Streamable HTTP routing</strong> — Server-to-client requests now route through the originating POST stream when no standalone SSE stream is available.</li>
<li><strong>Structured tool output</strong> — Tool output shapes are preserved when truncating older messages or oversized persisted rows.</li>
<li><strong>Non-chat Think tool steps</strong> — Think agent-tool children can complete without emitting assistant text and can return structured output through <code>getAgentToolOutput</code>.</li>
<li><strong>Sub-agent schedules</strong> — Stale sub-agent schedule rows are pruned when their owning facet registry entry no longer exists.</li>
<li><strong><code>@cloudflare/codemode</code></strong> — Adds a browser-safe export with an iframe sandbox executor and resolves OpenAPI specs inside the sandbox to avoid Worker Loader RPC size limits.</li>
</ul>
<h4 id="upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/think@latest @cloudflare/voice@latest&#10;</code></pre>
<p>Refer to the <a href="/agents/runtime/">Agents API reference</a> and <a href="/agents/communication-channels/chat/chat-agents/">Chat agents documentation</a> for more information.</p>
</div></article></div>
