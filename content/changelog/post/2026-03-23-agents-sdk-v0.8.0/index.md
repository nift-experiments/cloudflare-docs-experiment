---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-23-agents-sdk-v0.8.0/
  description: New updates and improvements at Cloudflare.
  full_title: 'Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4 · Changelog'
  head_html: '<title>Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-23-agents-sdk-v0.8.0/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-23-agents-sdk-v0.8.0/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-23-agents-sdk-v0.8.0/#page","headline":"Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-23-agents-sdk-v0.8.0/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>'
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-23-agents-sdk-v0.8.0/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 23, 2026</time><h2 id="post-title">Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> exposes agent state as a readable property, prevents duplicate schedule rows across Durable Object restarts, brings full TypeScript inference to <code>AgentClient</code>, and migrates to Zod 4.</p>
<h4 id="readable-state-on-useagent-and-agentclient">Readable <code>state</code> on <code>useAgent</code> and <code>AgentClient</code></h4>
<p>Both <code>useAgent</code> (React) and <code>AgentClient</code> (vanilla JS) now expose a <code>state</code> property that reflects the current agent state. Previously, reading state required manually tracking it through the <code>onStateUpdate</code> callback.</p>
<p><strong>React (<code>useAgent</code>)</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17655.md")</div>
<p><code>agent.state</code> is reactive — the component re-renders when state changes from either the server or a client-side <code>setState()</code> call.</p>
<p><strong>Vanilla JS (<code>AgentClient</code>)</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17656.md")</div>
<p>State starts as <code>undefined</code> and is populated when the server sends the initial state on connect (from <code>initialState</code>) or when <code>setState()</code> is called. Use optional chaining (<code>agent.state?.field</code>) for safe access. The <code>onStateUpdate</code> callback continues to work as before — the new <code>state</code> property is additive.</p>
<h4 id="idempotent-schedule">Idempotent <code>schedule()</code></h4>
<p><code>schedule()</code> now supports an <code>idempotent</code> option that deduplicates by <code>(type, callback, payload)</code>, preventing duplicate rows from accumulating when called in places that run on every Durable Object restart such as <code>onStart()</code>.</p>
<p><strong>Cron schedules are idempotent by default.</strong> Calling <code>schedule(&quot;0 * * * *&quot;, &quot;tick&quot;)</code> multiple times with the same callback, expression, and payload returns the existing schedule row instead of creating a new one. Pass <code>{ idempotent: false }</code> to override.</p>
<p>Delayed and date-scheduled types support opt-in idempotency:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17657.md")</div>
<p>Two new warnings help catch common foot-guns:</p>
<ul>
<li>Calling <code>schedule()</code> inside <code>onStart()</code> without <code>{ idempotent: true }</code> emits a <code>console.warn</code> with actionable guidance (once per callback; skipped for cron and when <code>idempotent</code> is set explicitly).</li>
<li>If an alarm cycle processes 10 or more stale one-shot rows for the same callback, the SDK emits a <code>console.warn</code> and a <code>schedule:duplicate_warning</code> diagnostics channel event.</li>
</ul>
<h4 id="typed-agentclient-with-call-inference-and-stub-proxy">Typed <code>AgentClient</code> with <code>call</code> inference and <code>stub</code> proxy</h4>
<p><code>AgentClient</code> now accepts an optional agent type parameter for full type inference on RPC calls, matching the typed experience already available with <code>useAgent</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17658.md")</div>
<p>State is automatically inferred from the agent type, so <code>onStateUpdate</code> is also typed:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17659.md")</div>
<p>Existing untyped usage continues to work without changes. The RPC type utilities (<code>AgentMethods</code>, <code>AgentStub</code>, <code>RPCMethods</code>) are now exported from <code>agents/client</code> for advanced typing scenarios.
<code>agents</code>, <code>@cloudflare/ai-chat</code>, and <code>@cloudflare/codemode</code> now require <code>zod ^4.0.0</code>. Zod v3 is no longer supported.</p>
<h4 id="cloudflare-ai-chat-fixes"><code>@cloudflare/ai-chat</code> fixes</h4>
<ul>
<li><strong>Turn serialization</strong> — <code>onChatMessage()</code> and <code>_reply()</code> work is now queued so user requests, tool continuations, and <code>saveMessages()</code> never stream concurrently.</li>
<li><strong>Duplicate messages on stop</strong> — Clicking stop during an active stream no longer splits the assistant message into two entries.</li>
<li><strong>Duplicate messages after tool calls</strong> — Orphaned client IDs no longer leak into persistent storage.</li>
</ul>
<h4 id="keepalive-and-keepalivewhile-are-no-longer-experimental"><code>keepAlive()</code> and <code>keepAliveWhile()</code> are no longer experimental</h4>
<p><code>keepAlive()</code> now uses a lightweight in-memory ref count instead of schedule rows. Multiple concurrent callers share a single alarm cycle. The <code>@experimental</code> tag has been removed from both <code>keepAlive()</code> and <code>keepAliveWhile()</code>.</p>
<h4 id="cloudflare-codemode-tanstack-ai-integration"><code>@cloudflare/codemode</code>: TanStack AI integration</h4>
<p>A new entry point <code>@cloudflare/codemode/tanstack-ai</code> adds support for <a href="https://tanstack.com/ai">TanStack AI's</a> <code>chat()</code> as an alternative to the Vercel AI SDK's <code>streamText()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17660.md")</div>
<h4 id="upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>
</div></article></div>
