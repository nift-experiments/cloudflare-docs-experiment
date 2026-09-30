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
<pre><code class="language-sh">npm i agents@latest&#10;</code></pre>
<p>For the complete Workflows API reference and patterns, see <a href="/agents/runtime/execution/run-workflows/">Run Workflows</a>.</p>
</div></article></div>
