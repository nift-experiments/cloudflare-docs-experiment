---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/
  description: New updates and improvements at Cloudflare.
  full_title: 'Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery() · Changelog'
  head_html: '<title>Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery() · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery() · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/#page","headline":"Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery() \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>'
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-03-agents-workflows-integration/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 3, 2026</time><h2 id="post-title">Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery()</h2>
<div class="changelog-badges"><span>agents</span><span>workflows</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings first-class support for <a href="/workflows/">Cloudflare Workflows</a>, synchronous state management, and new scheduling capabilities.</p>
<h4 id="cloudflare-workflows-integration">Cloudflare Workflows integration</h4>
<p>Agents excel at real-time communication and state management. Workflows excel at durable execution. Together, they enable powerful patterns where Agents handle WebSocket connections while Workflows handle long-running tasks, retries, and human-in-the-loop flows.</p>
<p>Use the new <code>AgentWorkflow</code> class to define workflows with typed access to your Agent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17624.md")</div>
<p>Start workflows from your Agent with <code>runWorkflow()</code> and handle lifecycle events:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17625.md")</div>
<p>Key workflow methods on your Agent:</p>
<ul>
<li><code>runWorkflow(workflowName, params, options?)</code> — Start a workflow with optional metadata</li>
<li><code>getWorkflow(workflowId)</code> / <code>getWorkflows(criteria?)</code> — Query workflows with cursor-based pagination</li>
<li><code>approveWorkflow(workflowId)</code> / <code>rejectWorkflow(workflowId)</code> — Human-in-the-loop approval flows</li>
<li><code>pauseWorkflow()</code>, <code>resumeWorkflow()</code>, <code>terminateWorkflow()</code> — Workflow control</li>
</ul>
<h4 id="synchronous-setstate">Synchronous setState()</h4>
<p>State updates are now synchronous with a new <code>validateStateChange()</code> validation hook:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17626.md")</div>
<h4 id="scheduleevery-for-recurring-tasks">scheduleEvery() for recurring tasks</h4>
<p>The new <code>scheduleEvery()</code> method enables fixed-interval recurring tasks with built-in overlap prevention:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17627.md")</div>
<h4 id="callable-system-improvements">Callable system improvements</h4>
<ul>
<li><strong>Client-side RPC timeout</strong> — Set timeouts on callable method invocations</li>
<li><strong><code>StreamingResponse.error(message)</code></strong> — Graceful stream error signaling</li>
<li><strong><code>getCallableMethods()</code></strong> — Introspection API for discovering callable methods</li>
<li><strong>Connection close handling</strong> — Pending calls are automatically rejected on disconnect</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17628.md")</div>
<h4 id="email-and-routing-enhancements">Email and routing enhancements</h4>
<p><strong>Secure email reply routing</strong> — Email replies are now secured with HMAC-SHA256 signed headers, preventing unauthorized routing of emails to agent instances.</p>
<p><strong>Routing improvements:</strong></p>
<ul>
<li><code>basePath</code> option to bypass default URL construction for custom routing</li>
<li>Server-sent identity — Agents send <code>name</code> and <code>agent</code> type on connect</li>
<li>New <code>onIdentity</code> and <code>onIdentityChange</code> callbacks on the client</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17629.md")</div>
<h4 id="upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest&#10;</code></pre>
<p>For the complete Workflows API reference and patterns, see <a href="/agents/runtime/execution/run-workflows/">Run Workflows</a>.</p>
</div></article></div>
