---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-02-agents-sdk-v0.7.0/
  description: New updates and improvements at Cloudflare.
  full_title: 'Agents SDK v0.7.0: Observability rewrite, keepAlive, and waitForMcpConnections · Changelog'
  head_html: '<title>Agents SDK v0.7.0: Observability rewrite, keepAlive, and waitForMcpConnections · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-02-agents-sdk-v0.7.0/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Agents SDK v0.7.0: Observability rewrite, keepAlive, and waitForMcpConnections · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-02-agents-sdk-v0.7.0/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-02-agents-sdk-v0.7.0/#page","headline":"Agents SDK v0.7.0: Observability rewrite, keepAlive, and waitForMcpConnections \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-02-agents-sdk-v0.7.0/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>'
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-02-agents-sdk-v0.7.0/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 2, 2026</time><h2 id="post-title">Agents SDK v0.7.0: Observability rewrite, keepAlive, and waitForMcpConnections</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> rewrites observability from scratch with <code>diagnostics_channel</code>, adds <code>keepAlive()</code> to prevent Durable Object eviction during long-running work, and introduces <code>waitForMcpConnections</code> so MCP tools are always available when <code>onChatMessage</code> runs.</p>
<h4 id="observability-rewrite">Observability rewrite</h4>
<p>The previous observability system used <code>console.log()</code> with a custom <code>Observability.emit()</code> interface. v0.7.0 replaces it with structured events published to <a href="/workers/runtime-apis/nodejs/diagnostics-channel/">diagnostics channels</a> — silent by default, zero overhead when nobody is listening.</p>
<p>Every event has a <code>type</code>, <code>payload</code>, and <code>timestamp</code>. Events are routed to seven named channels:</p>
<table>
<thead>
<tr>
<th>Channel</th>
<th>Event types</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agents:state</code></td>
<td><code>state:update</code></td>
</tr>
<tr>
<td><code>agents:rpc</code></td>
<td><code>rpc</code>, <code>rpc:error</code></td>
</tr>
<tr>
<td><code>agents:message</code></td>
<td><code>message:request</code>, <code>message:response</code>, <code>message:clear</code>, <code>message:cancel</code>, <code>message:error</code>, <code>tool:result</code>, <code>tool:approval</code></td>
</tr>
<tr>
<td><code>agents:schedule</code></td>
<td><code>schedule:create</code>, <code>schedule:execute</code>, <code>schedule:cancel</code>, <code>schedule:retry</code>, <code>schedule:error</code>, <code>queue:retry</code>, <code>queue:error</code></td>
</tr>
<tr>
<td><code>agents:lifecycle</code></td>
<td><code>connect</code>, <code>destroy</code></td>
</tr>
<tr>
<td><code>agents:workflow</code></td>
<td><code>workflow:start</code>, <code>workflow:event</code>, <code>workflow:approved</code>, <code>workflow:rejected</code>, <code>workflow:terminated</code>, <code>workflow:paused</code>, <code>workflow:resumed</code>, <code>workflow:restarted</code></td>
</tr>
<tr>
<td><code>agents:mcp</code></td>
<td><code>mcp:client:preconnect</code>, <code>mcp:client:connect</code>, <code>mcp:client:authorize</code>, <code>mcp:client:discover</code></td>
</tr>
</tbody>
</table>
<p>Use the typed <code>subscribe()</code> helper from <code>agents/observability</code> for type-safe access:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17645.md")</div>
<p>In production, all diagnostics channel messages are automatically forwarded to <a href="/workers/observability/logs/tail-workers/">Tail Workers</a> — no subscription code needed in the agent itself:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17646.md")</div>
<p>The custom <code>Observability</code> override interface is still supported for users who need to filter or forward events to external services.</p>
<p>For the full event reference, refer to the <a href="/agents/runtime/operations/observability/diagnostics-channels/">Diagnostics channels documentation</a>.</p>
<h4 id="keepalive-and-keepalivewhile"><code>keepAlive()</code> and <code>keepAliveWhile()</code></h4>
<p>Durable Objects are evicted after a period of inactivity (typically 70-140 seconds with no incoming requests, WebSocket messages, or alarms). During long-running operations — streaming LLM responses, waiting on external APIs, running multi-step computations — the agent can be evicted mid-flight.</p>
<p><code>keepAlive()</code> prevents this by creating a 30-second heartbeat schedule. The alarm firing resets the inactivity timer. Returns a disposer function that cancels the heartbeat when called.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17647.md")</div>
<p><code>keepAliveWhile()</code> wraps an async function with automatic cleanup — the heartbeat starts before the function runs and stops when it completes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17648.md")</div>
<p>Key details:</p>
<ul>
<li><strong>Multiple concurrent callers</strong> — Each <code>keepAlive()</code> call returns an independent disposer. Disposing one does not affect others.</li>
<li><strong>AIChatAgent built-in</strong> — <code>AIChatAgent</code> automatically calls <code>keepAlive()</code> during streaming responses. You do not need to add it yourself.</li>
<li><strong>Uses the scheduling system</strong> — The heartbeat does not conflict with your own schedules. It shows up in <code>getSchedules()</code> if you need to inspect it.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17644.md")</aside>
<p>For the full API reference and when-to-use guidance, refer to <a href="/agents/runtime/execution/schedule-tasks/#keeping-the-agent-alive">Schedule tasks — Keeping the agent alive</a>.</p>
<h4 id="waitformcpconnections"><code>waitForMcpConnections</code></h4>
<p><code>AIChatAgent</code> now waits for MCP server connections to settle before calling <code>onChatMessage</code>. This ensures <code>this.mcp.getAITools()</code> returns the full set of tools, especially after Durable Object hibernation when connections are being restored in the background.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17649.md")</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>{ timeout: 10_000 }</code></td>
<td>Wait up to 10 seconds (default)</td>
</tr>
<tr>
<td><code>{ timeout: N }</code></td>
<td>Wait up to <code>N</code> milliseconds</td>
</tr>
<tr>
<td><code>true</code></td>
<td>Wait indefinitely until all connections ready</td>
</tr>
<tr>
<td><code>false</code></td>
<td>Do not wait (old behavior before 0.2.0)</td>
</tr>
</tbody>
</table>
<p>For lower-level control, call <code>this.mcp.waitForConnections()</code> directly inside <code>onChatMessage</code> instead.</p>
<h4 id="other-improvements">Other improvements</h4>
<ul>
<li><strong>MCP deduplication by name and URL</strong> — <code>addMcpServer</code> with HTTP transport now deduplicates on both server name and URL. Calling it with the same name but a different URL creates a new connection. URLs are normalized before comparison (trailing slashes, default ports, hostname case).</li>
<li><strong><code>callbackHost</code> optional for non-OAuth servers</strong> — <code>addMcpServer</code> no longer requires <code>callbackHost</code> when connecting to MCP servers that do not use OAuth.</li>
<li><strong>MCP URL security</strong> — Server URLs are validated before connection to prevent SSRF. Private IP ranges, loopback addresses, link-local addresses, and cloud metadata endpoints are blocked.</li>
<li><strong>Custom denial messages</strong> — <code>addToolOutput</code> now supports <code>state: &quot;output-error&quot;</code> with <code>errorText</code> for custom denial messages in human-in-the-loop tool approval flows.</li>
<li><strong><code>requestId</code> in chat options</strong> — <code>onChatMessage</code> options now include a <code>requestId</code> for logging and correlating events.</li>
</ul>
<h4 id="upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>
</div></article></div>
