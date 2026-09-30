<div class="nb-description">
@markup("md", "content/.markup/bodies/1072.md")
</div>
<p>Dynamic Workers let you spin up an unlimited number of Workers to execute arbitrary code specified at runtime. Dynamic Workers can be used as a lightweight alternative to containers for securely sandboxing code you don't trust.</p>
<p>Dynamic Workers are the lowest-level primitive for spinning up a Worker, giving you full control over defining how the Worker is composed, which bindings it receives, whether it can reach the network, and more.</p>
<h3 id="get-started">Get started</h3>
<p>Deploy the <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground">Dynamic Workers Playground</a> to create and run Workers dynamically from code you write or import from GitHub, with real-time logs and observability.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/dinasaur404/dynamic-workers-playground"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<h2 id="use-dynamic-workers-for">Use Dynamic Workers for</h2>
<p>Use this pattern when code needs to run quickly in a secure, isolated environment.</p>
<ul>
<li><strong>AI Agent &quot;Code Mode&quot;</strong>: LLMs are trained to write code. Instead of supplying an agent with tool calls to perform tasks, give it an API and let it write and execute code. Save up to 80% in inference tokens and cost by allowing the agent to programmatically process data instead of sending it all through the LLM.</li>
<li><strong>AI-generated applications / &quot;Vibe Code&quot;</strong>: Run generated code for prototypes, projects, and automations in a secure, isolated sandboxed environment.</li>
<li><strong>Fast development and previews</strong>: Load prototypes, previews, and playgrounds in milliseconds.</li>
<li><strong>Custom automations</strong>: Create custom tools on the fly that execute a task, call an integration, or automate a workflow.</li>
<li><strong>Platforms</strong>: Run applications uploaded by your users.</li>
</ul>
<h2 id="features">Features</h2>
<p>Because you compose the Worker that runs the code at runtime, you control how that Worker is configured and what it can access.</p>
<ul>
<li><strong><a href="/dynamic-workers/usage/bindings/">Bindings</a></strong>: Decide which bindings and structured data the dynamic Worker receives.</li>
<li><strong><a href="/dynamic-workers/usage/observability/">Observability</a></strong>: Attach Tail Workers and capture logs for each run.</li>
<li><strong><a href="/dynamic-workers/usage/egress-control/">Network access</a></strong>: Intercept or block Internet access for outbound requests.</li>
<li><strong><a href="/dynamic-workers/usage/limits/">Limits</a></strong>: Enforce custom limits on the dynamic Worker's resource usage.</li>
<li><strong><a href="/dynamic-workers/usage/durable-object-facets/">Durable Object Facets</a></strong>: Run dynamically-loaded code as a Durable Object with its own isolated SQLite storage.</li>
</ul>
