---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-17-agents-sdk-v0.5.0/
  description: New updates and improvements at Cloudflare.
  full_title: 'Agents SDK v0.5.0: Protocol message control, retry utilities, data parts, and @cloudflare/ai-chat v0.1.0 · Changelog'
  head_html: '<title>Agents SDK v0.5.0: Protocol message control, retry utilities, data parts, and @cloudflare/ai-chat v0.1.0 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-17-agents-sdk-v0.5.0/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Agents SDK v0.5.0: Protocol message control, retry utilities, data parts, and @cloudflare/ai-chat v0.1.0 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-17-agents-sdk-v0.5.0/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-17-agents-sdk-v0.5.0/#page","headline":"Agents SDK v0.5.0: Protocol message control, retry utilities, data parts, and @cloudflare/ai-chat v0.1.0 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-17-agents-sdk-v0.5.0/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>'
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-17-agents-sdk-v0.5.0/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 17, 2026</time><h2 id="post-title">Agents SDK v0.5.0: Protocol message control, retry utilities, data parts, and @cloudflare/ai-chat v0.1.0</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> adds built-in retry utilities, per-connection protocol message control, and a fully rewritten <code>@cloudflare/ai-chat</code> with data parts, tool approval persistence, and zero breaking changes.</p>
<h4 id="retry-utilities">Retry utilities</h4>
<p>A new <code>this.retry()</code> method lets you retry any async operation with exponential backoff and jitter. You can pass an optional <code>shouldRetry</code> predicate to bail early on non-retryable errors.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17635.md")</div>
<p>Retry options are also available per-task on <code>queue()</code>, <code>schedule()</code>, <code>scheduleEvery()</code>, and <code>addMcpServer()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17636.md")</div>
<p>Retry options are validated eagerly at enqueue/schedule time, and invalid values throw immediately. Internal retries have also been added for workflow operations (<code>terminateWorkflow</code>, <code>pauseWorkflow</code>, and others) with Durable Object-aware error detection.</p>
<h4 id="per-connection-protocol-message-control">Per-connection protocol message control</h4>
<p>Agents automatically send JSON text frames (identity, state, MCP server lists) to every WebSocket connection. You can now suppress these per-connection for clients that cannot handle them — binary-only devices, MQTT clients, or lightweight embedded systems.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17637.md")</div>
<p>Connections with protocol messages disabled still fully participate in RPC and regular messaging. Use <code>isConnectionProtocolEnabled(connection)</code> to check a connection's status at any time. The flag persists across Durable Object hibernation.</p>
<p>See <a href="/agents/runtime/communication/protocol-messages/">Protocol messages</a> for full documentation.</p>
<h4 id="cloudflare-ai-chat-v0-1-0"><code>@cloudflare/ai-chat</code> v0.1.0</h4>
<p>The first stable release of <code>@cloudflare/ai-chat</code> ships alongside this release with a major refactor of <code>AIChatAgent</code> internals — new <code>ResumableStream</code> class, WebSocket <code>ChatTransport</code>, and simplified SSE parsing — with zero breaking changes. Existing code using <code>AIChatAgent</code> and <code>useAgentChat</code> works as-is.</p>
<p>Key new features:</p>
<ul>
<li><strong>Data parts</strong> — Attach typed JSON blobs (<code>data-*</code>) to messages alongside text. Supports reconciliation (type+id updates in-place), append, and transient parts (ephemeral via <code>onData</code> callback). See <a href="/agents/communication-channels/chat/chat-agents/#data-parts">Data parts</a>.</li>
<li><strong>Tool approval persistence</strong> — The <code>needsApproval</code> approval UI now survives page refresh and DO hibernation. The streaming message is persisted to SQLite when a tool enters <code>approval-requested</code> state.</li>
<li><strong><code>maxPersistedMessages</code></strong> — Cap SQLite message storage with automatic oldest-message deletion.</li>
<li><strong><code>body</code> option on <code>useAgentChat</code></strong> — Send custom data with every request (static or dynamic).</li>
<li><strong>Incremental persistence</strong> — Hash-based cache to skip redundant SQL writes.</li>
<li><strong>Row size guard</strong> — Automatic two-pass compaction when messages approach the SQLite 2 MB limit.</li>
<li><strong><code>autoContinueAfterToolResult</code> defaults to <code>true</code></strong> — Client-side tool results and tool approvals now automatically trigger a server continuation, matching server-executed tool behavior. Set <code>autoContinueAfterToolResult: false</code> in <code>useAgentChat</code> to restore the previous behavior.</li>
</ul>
<p>Notable bug fixes:</p>
<ul>
<li>Resolved stream resumption race conditions</li>
<li>Resolved an issue where <code>setMessages</code> functional updater sent empty arrays</li>
<li>Resolved an issue where client tool schemas were lost after DO hibernation</li>
<li>Resolved <code>InvalidPromptError</code> after tool approval (<code>approval.id</code> was dropped)</li>
<li>Resolved an issue where message metadata was not propagated on broadcast/resume paths</li>
<li>Resolved an issue where <code>clearAll()</code> did not clear in-memory chunk buffers</li>
<li>Resolved an issue where <code>reasoning-delta</code> silently dropped data when <code>reasoning-start</code> was missed during stream resumption</li>
</ul>
<h4 id="synchronous-queue-and-schedule-getters">Synchronous queue and schedule getters</h4>
<p><code>getQueue()</code>, <code>getQueues()</code>, <code>getSchedule()</code>, <code>dequeue()</code>, <code>dequeueAll()</code>, and <code>dequeueAllByCallback()</code> were unnecessarily <code>async</code> despite only performing synchronous SQL operations. They now return values directly instead of wrapping them in Promises. This is backward compatible — existing code using <code>await</code> on these methods will continue to work.</p>
<h4 id="other-improvements">Other improvements</h4>
<ul>
<li><strong>Fix TypeScript &quot;excessively deep&quot; error</strong> — A depth counter on <code>CanSerialize</code> and <code>IsSerializableParam</code> types bails out to <code>true</code> after 10 levels of recursion, preventing the &quot;Type instantiation is excessively deep&quot; error with deeply nested types like AI SDK <code>CoreMessage[]</code>.</li>
<li><strong>POST SSE keepalive</strong> — The POST SSE handler now sends <code>event: ping</code> every 30 seconds to keep the connection alive, matching the existing GET SSE handler behavior. This prevents POST response streams from being silently dropped by proxies during long-running tool calls.</li>
<li><strong>Widened peer dependency ranges</strong> — Peer dependency ranges across packages have been widened to prevent cascading major bumps during 0.x minor releases. <code>@cloudflare/ai-chat</code> and <code>@cloudflare/codemode</code> are now marked as optional peer dependencies.</li>
</ul>
<h4 id="upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>
</div></article></div>
