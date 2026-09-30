<p>Agents can use <a href="/sandbox/">Sandbox</a> to run code in isolated container environments. Use Sandbox when an agent needs a real filesystem, shell commands, language runtimes, package installation, or long-lived project state that should not run inside the agent's own Worker isolate.</p>
<p>Sandbox is built on <a href="/containers/">Cloudflare Containers</a> and exposes a TypeScript API for command execution, file operations, background processes, and service previews.</p>
<h2 id="when-to-use-sandbox">When to use Sandbox</h2>
<p>Use Sandbox for agents that need to:</p>
<ul>
<li>Run untrusted or model-generated code in isolation.</li>
<li>Execute Python, Node.js, shell commands, or package managers.</li>
<li>Read, write, and manage project files.</li>
<li>Run tests, linters, build tools, or data analysis scripts.</li>
<li>Maintain a workspace across multiple agent turns.</li>
</ul>
<h2 id="basic-pattern">Basic pattern</h2>
<p>Bind the Sandbox Durable Object to your Worker, then access a sandbox from your agent methods with <code>getSandbox()</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1841.md")
</div>
<h2 id="configuration">Configuration</h2>
<p>Configure the Sandbox container, Durable Object binding, and migration in <code>wrangler.jsonc</code>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1842.md")
</div>
<h2 id="sandbox-and-agent-state">Sandbox and agent state</h2>
<p>Use agent state for user-visible progress and small metadata. Use the sandbox filesystem for workspace files, generated code, package installs, logs, and artifacts.</p>
<p>For long-running sandbox work, pair Sandbox with <a href="/agents/runtime/execution/durable-execution/">durable execution with fibers</a> or <a href="/agents/runtime/execution/run-workflows/">Workflows</a> so the agent can recover or report progress if work outlives a single request.</p>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="/sandbox/"><h3 id="card-sandbox-sdk-sandbox">Sandbox SDK</h3><p>Full Sandbox documentation for commands, files, sessions, and deployment.</p></a></p>
<p><a class="nb-card nb-link-card" href="/sandbox/guides/execute-commands/"><h3 id="card-execute-commands-sandbox-guides-execute-commands">Execute commands</h3><p>Run shell commands in a sandbox environment.</p></a></p>
<p><a class="nb-card nb-link-card" href="/sandbox/guides/manage-files/"><h3 id="card-manage-files-sandbox-guides-manage-files">Manage files</h3><p>Read, write, upload, and download sandbox files.</p></a></p>
