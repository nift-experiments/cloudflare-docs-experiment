<p>This guide shows how to add agents to an existing Cloudflare Workers project. If you are starting fresh, refer to <a href="/agents/examples/chat-agent/">Building a chat agent</a> instead.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An existing Cloudflare Workers project with a Wrangler configuration file</li>
<li>Node.js 18 or newer</li>
</ul>
<h2 id="1-install-the-package"><ol>
<li>Install the package</li>
</ol></h2>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For React applications, no additional packages are needed — React bindings are included.</p>
<p>For Hono applications:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents hono-agents</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents hono-agents" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents hono-agents</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents hono-agents" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents hono-agents</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents hono-agents" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents hono-agents</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents hono-agents" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="2-create-an-agent"><ol start="2">
<li>Create an Agent</li>
</ol></h2>
<p>Create a new file for your agent (for example, <code>src/agents/counter.ts</code>):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1879.md")
</div>
<h2 id="3-update-wrangler-configuration"><ol start="3">
<li>Update Wrangler configuration</li>
</ol></h2>
<p>Add the Durable Object binding and migration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1880.md")
</div>
<p><strong>Key points:</strong></p>
<ul>
<li><code>name</code> in bindings becomes the property on <code>env</code> (for example, <code>env.CounterAgent</code>)</li>
<li><code>class_name</code> must exactly match your exported class name</li>
<li><code>new_sqlite_classes</code> enables SQLite storage for state persistence</li>
<li><code>nodejs_compat</code> flag is required for the agents package</li>
</ul>
<h2 id="4-configure-typescript-and-vite"><ol start="4">
<li>Configure TypeScript and Vite</li>
</ol></h2>
<p>If you use <code>@callable()</code> decorators (as in the example above), you need two build configurations.</p>
<p><strong>tsconfig.json</strong> — extend <code>agents/tsconfig</code> (or set <code>&quot;target&quot;: &quot;ES2021&quot;</code> manually):</p>
<pre><code class="language-json">{&#10;	&quot;extends&quot;: &quot;agents/tsconfig&quot;&#10;}&#10;</code></pre>
<p>If you have an existing <code>tsconfig.json</code> with custom settings, you can extend and override:</p>
<pre><code class="language-json">{&#10;	&quot;extends&quot;: &quot;agents/tsconfig&quot;,&#10;	&quot;compilerOptions&quot;: {&#10;		&quot;paths&quot;: { &quot;~/*&quot;: [&quot;./src/*&quot;] }&#10;	}&#10;}&#10;</code></pre>
<p><strong>vite.config.ts</strong> — add the <code>agents()</code> plugin (handles TC39 decorator transforms for Vite 8):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1881.md")
</div>
<p>If your project does not use Vite, the <code>tsconfig.json</code> change alone is sufficient — your bundler must support TC39 decorators (stage 3, version <code>2023-11</code>).</p>
<p>For more details, refer to the <a href="/agents/runtime/operations/configuration/#typescript-configuration">TypeScript configuration</a> and <a href="/agents/runtime/operations/configuration/#vite-configuration">Vite configuration</a> reference.</p>
<h2 id="5-export-the-agent-class"><ol start="5">
<li>Export the Agent class</li>
</ol></h2>
<p>Your agent class must be exported from your main entry point. Update your <code>src/index.ts</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1882.md")
</div>
<h2 id="6-wire-up-routing"><ol start="6">
<li>Wire up routing</li>
</ol></h2>
<p>Choose the approach that matches your project structure:</p>
<h3 id="plain-workers-fetch-handler">Plain Workers (fetch handler)</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1883.md")
</div>
<h3 id="hono">Hono</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1884.md")
</div>
<h3 id="with-static-assets">With static assets</h3>
<p>If you are serving static assets alongside agents, static assets are served first by default. Your Worker code only runs for paths that do not match a static asset:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1885.md")
</div>
<p>Configure assets in the Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1886.md")
</div>
<h2 id="7-generate-typescript-types"><ol start="7">
<li>Generate TypeScript types</li>
</ol></h2>
<p>Do not hand-write your <code>Env</code> interface. Run <a href="/workers/wrangler/commands/general/#types"><code>wrangler types</code></a> to generate a type definition file that matches your Wrangler configuration. This catches mismatches between your config and code at compile time instead of at deploy time.</p>
<p>Re-run <code>wrangler types</code> whenever you add or rename a binding.</p>
<pre><code class="language-sh">npx wrangler types&#10;</code></pre>
<p>This creates a type definition file with all your bindings typed, including your agent Durable Object namespaces. The <code>Agent</code> class defaults to using the generated <code>Env</code> type, so you do not need to pass it as a type parameter — <code>extends Agent</code> is sufficient unless you need to pass a second type parameter for state (for example, <code>Agent&lt;Env, CounterState&gt;</code>).</p>
<p>Refer to <a href="/agents/runtime/operations/configuration/#generating-types">Configuration</a> for more details on type generation.</p>
<h2 id="8-connect-from-the-frontend"><ol start="8">
<li>Connect from the frontend</li>
</ol></h2>
<h3 id="react">React</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1887.md")
</div>
<p>Key points:</p>
<ul>
<li><code>useAgent</code> connects to your agent via WebSocket</li>
<li><code>onStateUpdate</code> fires whenever the agent's state changes</li>
<li><code>agent.stub.methodName()</code> calls methods marked with <code>@callable()</code> on your agent</li>
</ul>
<h3 id="vanilla-javascript">Vanilla JavaScript</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1888.md")
</div>
<h2 id="how-it-works">How it works</h2>
<p>When you clicked the button:</p>
<ol>
<li><strong>Client</strong> called <code>agent.stub.increment()</code> over WebSocket</li>
<li><strong>Agent</strong> ran <code>increment()</code>, updated state with <code>setState()</code></li>
<li><strong>State</strong> persisted to SQLite automatically</li>
<li><strong>Broadcast</strong> sent to all connected clients</li>
<li><strong>React</strong> updated via <code>onStateUpdate</code></li>
</ol>
<pre><code class="language-mermaid">flowchart LR&#10;    A[&quot;Browser&lt;br/&gt;(React)&quot;] &lt;--&gt;|WebSocket| B[&quot;Agent&lt;br/&gt;(Counter)&quot;]&#10;    B --&gt; C[&quot;SQLite&lt;br/&gt;(State)&quot;]&#10;</code></pre>
<h3 id="key-concepts">Key concepts</h3>
<table>
<thead>
<tr>
<th>Concept</th>
<th>What it means</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Agent instance</strong></td>
<td>Each unique name gets its own agent. <code>CounterAgent:user-123</code> is separate from <code>CounterAgent:user-456</code></td>
</tr>
<tr>
<td><strong>Persistent state</strong></td>
<td>State survives restarts, deploys, and hibernation. It is stored in SQLite</td>
</tr>
<tr>
<td><strong>Real-time sync</strong></td>
<td>All clients connected to the same agent receive state updates instantly</td>
</tr>
<tr>
<td><strong>Hibernation</strong></td>
<td>When no clients are connected, the agent hibernates (no cost). It wakes on the next request</td>
</tr>
</tbody>
</table>
<h2 id="deploy-to-cloudflare">Deploy to Cloudflare</h2>
<pre><code class="language-sh">npm run deploy&#10;</code></pre>
<p>Your agent is now live on Cloudflare's global network, running close to your users.</p>
<h2 id="common-integration-patterns">Common integration patterns</h2>
<h3 id="agents-behind-authentication">Agents behind authentication</h3>
<p>Check auth before routing to agents:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1889.md")
</div>
<h3 id="custom-agent-path-prefix">Custom agent path prefix</h3>
<p>By default, agents are routed at <code>/agents/{agent-name}/{instance-name}</code>. You can customize this:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1890.md")
</div>
<p>Refer to <a href="/agents/runtime/communication/routing/">Routing</a> for more options including CORS, custom instance naming, and location hints.</p>
<h3 id="accessing-agents-from-server-code">Accessing agents from server code</h3>
<p>You can interact with agents directly from your Worker code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1891.md")
</div>
<h3 id="adding-multiple-agents">Adding multiple agents</h3>
<p>Add more agents by extending the configuration:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1892.md")
</div>
<p>Update the Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1893.md")
</div>
<p>Export all agents from your entry point:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1894.md")
</div>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="agent-not-found-or-404-errors">Agent not found, or 404 errors</h3>
<ol>
<li><strong>Check the export</strong> - Agent class must be exported from your main entry point.</li>
<li><strong>Check the binding</strong> - <code>class_name</code> in the Wrangler configuration file must exactly match the exported class name.</li>
<li><strong>Check the route</strong> - Default route is <code>/agents/{'{agent-name}'}/{'{instance-name}'}</code>. Agent name in client matches the class name (case-insensitive).</li>
</ol>
<h3 id="no-such-durable-object-class-error">No such Durable Object class error</h3>
<p>Add the migration to the Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1895.md")
</div>
<h3 id="websocket-connection-fails">WebSocket connection fails</h3>
<p>Ensure your routing passes the response unchanged:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1896.md")
</div>
<h3 id="state-not-persisting">State not persisting</h3>
<p>Check that:</p>
<ol>
<li>You are calling <code>this.setState()</code>, not mutating <code>this.state</code> directly.</li>
<li>The agent class is in <code>new_sqlite_classes</code> in migrations.</li>
<li>You are connecting to the same agent instance name.</li>
<li>The <code>onStateUpdate</code> callback is wired up in your client.</li>
<li>WebSocket connection is established (check browser dev tools).</li>
</ol>
<h3 id="method-x-is-not-callable-errors">&quot;Method X is not callable&quot; errors</h3>
<p>Make sure your methods are decorated with <code>@callable()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1897.md")
</div>
<h3 id="type-errors-with-agent-stub">Type errors with <code>agent.stub</code></h3>
<p>Add the agent and state type parameters:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1898.md")
</div>
<h3 id="syntaxerror-invalid-or-unexpected-token-with-callable"><code>SyntaxError: Invalid or unexpected token</code> with <code>@callable()</code></h3>
<p>If your dev server fails with <code>SyntaxError: Invalid or unexpected token</code>, set <code>&quot;target&quot;: &quot;ES2021&quot;</code> in your <code>tsconfig.json</code>. This ensures that Vite's esbuild transpiler downlevels TC39 decorators instead of passing them through as native syntax.</p>
<pre><code class="language-json">{&#10;	&quot;compilerOptions&quot;: {&#10;		&quot;target&quot;: &quot;ES2021&quot;&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/1878.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<p>Now that you have a working agent, explore these topics:</p>
<h3 id="common-next-steps">Common next steps</h3>
<table>
<thead>
<tr>
<th>Learn how to</th>
<th>Refer to</th>
</tr>
</thead>
<tbody>
<tr>
<td>Add AI/LLM capabilities</td>
<td><a href="/agents/runtime/operations/using-ai-models/">Using AI models</a></td>
</tr>
<tr>
<td>Expose tools via MCP</td>
<td><a href="/agents/model-context-protocol/apis/agent-api/">MCP servers</a></td>
</tr>
<tr>
<td>Run background tasks</td>
<td><a href="/agents/runtime/execution/schedule-tasks/">Schedule tasks</a></td>
</tr>
<tr>
<td>Handle emails</td>
<td><a href="/agents/communication-channels/email/">Email routing</a></td>
</tr>
<tr>
<td>Use Cloudflare Workflows</td>
<td><a href="/agents/runtime/execution/run-workflows/">Run Workflows</a></td>
</tr>
</tbody>
</table>
<h3 id="explore-more">Explore more</h3>
<p><a class="nb-card nb-link-card" href="/agents/runtime/lifecycle/state/"><h3 id="card-state-management-agents-runtime-lifecycle-state">State management</h3><p>Deep dive into setState(), initialState, and onStateChanged().</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/communication-channels/chat/client-sdk/"><h3 id="card-client-sdk-agents-communication-channels-chat-client-sdk">Client SDK</h3><p>Full useAgent and AgentClient API reference.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/lifecycle/callable-methods/"><h3 id="card-callable-methods-agents-runtime-lifecycle-callable-methods">Callable methods</h3><p>Expose methods to clients with @callable().</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/execution/schedule-tasks/"><h3 id="card-schedule-tasks-agents-runtime-execution-schedule-tasks">Schedule tasks</h3><p>Run tasks on a delay, schedule, or cron.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/lifecycle/agent-class/"><h3 id="card-agent-class-internals-agents-runtime-lifecycle-agent-class">Agent class internals</h3><p>Full lifecycle and methods reference.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/agents-api/"><h3 id="card-agents-api-agents-runtime-agents-api">Agents API</h3><p>Complete API reference for the Agents SDK.</p></a></p>
