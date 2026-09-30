<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 20, 2026</time><h2 id="post-title">@cloudflare/codemode v0.1.0: a new runtime agnostic modular architecture</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The <a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a> package has been rewritten into a modular, runtime-agnostic SDK.</p>
<p><a href="https://blog.cloudflare.com/code-mode/">Code Mode</a> enables LLMs to write and execute code that orchestrates your tools, instead of calling them one at a time. This can (and does) yield significant token savings, reduces context window pressure and improves overall model performance on a task.</p>
<p>The new <code>Executor</code> interface is runtime agnostic and comes with a prebuilt <code>DynamicWorkerExecutor</code> to run generated code in a <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker Loader</a>.</p>
<h4 id="breaking-changes">Breaking changes</h4>
<ul>
<li>Removed <code>experimental_codemode()</code> and <code>CodeModeProxy</code> — the package no longer owns an LLM call or model choice</li>
<li>New import path: <code>createCodeTool()</code> is now exported from <code>@cloudflare/codemode/ai</code></li>
</ul>
<h4 id="new-features">New features</h4>
<ul>
<li><strong><code>createCodeTool()</code></strong> — Returns a standard AI SDK <code>Tool</code> to use in your AI agents.</li>
<li><strong><code>Executor</code> interface</strong> — Minimal <code>execute(code, fns)</code> contract. Implement for any code sandboxing primitive or runtime.</li>
</ul>
<h4 id="dynamicworkerexecutor"><code>DynamicWorkerExecutor</code></h4>
<p>Runs code in a <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a>. It comes with the following features:</p>
<ul>
<li><strong>Network isolation</strong> — <code>fetch()</code> and <code>connect()</code> blocked by default (<code>globalOutbound: null</code>) when using <code>DynamicWorkerExecutor</code></li>
<li><strong>Console capture</strong> — <code>console.log/warn/error</code> captured and returned in <code>ExecuteResult.logs</code></li>
<li><strong>Execution timeout</strong> — Configurable via <code>timeout</code> option (default 30s)</li>
</ul>
<h4 id="usage">Usage</h4>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17638.md")</div>
<h4 id="wrangler-configuration">Wrangler configuration</h4>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17639.md")</div>
<p>See the <a href="/agents/tools/codemode/">Code Mode documentation</a> for full API reference and examples.</p>
<h4 id="upgrade">Upgrade</h4>
<pre><code class="language-sh">npm i @cloudflare/codemode@latest&#10;</code></pre>
</div></article></div>
