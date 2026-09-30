<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 24, 2026</time><h2 id="post-title">Dynamic Workers, now in open beta</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/dynamic-workers/">Dynamic Workers</a> are now in <a href="https://blog.cloudflare.com/dynamic-workers/">open beta</a> for all paid Workers users. You can now have a Worker spin up other Workers, called Dynamic Workers, at runtime to execute code on-demand in a secure, sandboxed environment. Dynamic Workers start in milliseconds, making them well suited for fast, secure code execution at scale.</p>
<h4 id="use-dynamic-workers-for">Use Dynamic Workers for</h4>
<ul>
<li><strong><a href="/agents/tools/codemode/">Code Mode</a></strong>: LLMs are trained to write code. Run tool-calling logic written in code instead of stepping through many tool calls, which can save up to 80% in inference tokens and cost.</li>
<li><strong>AI agents executing code</strong>: Run code for tasks like data analysis, file transformation, API calls, and chained actions.</li>
<li><strong>Running AI-generated code</strong>: Run generated code for prototypes, projects, and automations in a secure, isolated sandboxed environment.</li>
<li><strong>Fast development and previews</strong>: Load prototypes, previews, and playgrounds in milliseconds.</li>
<li><strong>Custom automations</strong>: Create custom tools on the fly that execute a task, call an integration, or automate a workflow.</li>
</ul>
<h4 id="executing-dynamic-workers">Executing Dynamic Workers</h4>
<p>Dynamic Workers support two loading modes:</p>
<ul>
<li><code>load(code)</code> — for one-time code execution (equivalent to calling <code>get()</code> with a null ID).</li>
<li><code>get(id, callback)</code> — caches a Dynamic Worker by ID so it can stay warm across requests. Use this when the same code will receive subsequent requests.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17801.md")</div>
<h4 id="helper-libraries-for-dynamic-workers">Helper libraries for Dynamic Workers</h4>
<p>Here are 3 new libraries to help you build with Dynamic Workers:</p>
<ul>
<li>
<p><strong><a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a></strong>: Replace individual tool calls with a single <code>code()</code> tool, so LLMs write and execute TypeScript that orchestrates multiple API calls in one pass.</p>
</li>
<li>
<p><strong><a href="https://www.npmjs.com/package/@cloudflare/worker-bundler"><code>@cloudflare/worker-bundler</code></a></strong>: Resolve npm dependencies and bundle source files into ready-to-load modules for Dynamic Workers, all at runtime.</p>
</li>
<li>
<p><strong><a href="https://www.npmjs.com/package/@cloudflare/shell"><code>@cloudflare/shell</code></a></strong>: Give your agent a virtual filesystem inside a Dynamic Worker with persistent storage backed by SQLite and R2.</p>
</li>
</ul>
<h4 id="try-it-out">Try it out</h4>
<p><strong>Dynamic Workers Starter</strong></p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>Use this <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers">starter</a> to deploy a Worker that can load and execute Dynamic Workers.</p>
<p><strong>Dynamic Workers Playground</strong></p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>Deploy the <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground">Dynamic Workers Playground</a> to write or import code, bundle it at runtime with <code>@cloudflare/worker-bundler</code>, execute it through a Dynamic Worker, and see real-time responses and execution logs.</p>
<p>For the full API reference and configuration options, refer to the <a href="/dynamic-workers/">Dynamic Workers documentation</a>.</p>
<h4 id="pricing">Pricing</h4>
<p>Dynamic Workers <a href="/dynamic-workers/pricing/">pricing</a> is based on three dimensions: Dynamic Workers created daily, requests, and CPU time.</p>
<table>
<thead>
<tr>
<th></th>
<th>Included</th>
<th>Additional usage</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Dynamic Workers created daily</strong></td>
<td>1,000 unique Dynamic Workers per month</td>
<td>+$0.002 per Dynamic Worker per day</td>
</tr>
<tr>
<td><strong>Requests</strong> ¹</td>
<td>10 million per month</td>
<td>+$0.30 per million requests</td>
</tr>
<tr>
<td><strong>CPU time</strong> ¹</td>
<td>30 million CPU milliseconds per month</td>
<td>+$0.02 per million CPU milliseconds</td>
</tr>
</tbody>
</table>
<p>¹ Uses <a href="/workers/platform/pricing/#workers">Workers Standard rates</a> and will appear as part of your existing Workers bill, not as separate Dynamic Workers charges.</p>
<p>Note: Dynamic Workers requests and CPU time are already billed as part of your Workers plan and will count toward your Workers requests and CPU usage. The Dynamic Workers created daily charge is not yet active — you will not be billed for the number of Dynamic Workers created at this time. Pricing information is shared in advance so you can estimate future costs.</p>
</div></article></div>
