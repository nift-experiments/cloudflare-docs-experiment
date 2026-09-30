<p>Build AI agents that persist, think, and act. Agents run on Cloudflare's global network, maintain state across requests, and connect to clients in real-time via WebSockets.</p>
<p><strong>What you will build:</strong> A counter agent with persistent state that syncs to a React frontend in real-time.</p>
<p><strong>Time:</strong> ~10 minutes</p>
<h2 id="create-a-new-project">Create a new project</h2>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- --template cloudflare/agents-starter</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- --template cloudflare/agents-starter" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare --template cloudflare/agents-starter</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare --template cloudflare/agents-starter" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest --template cloudflare/agents-starter</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest --template cloudflare/agents-starter" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Then install dependencies and start the dev server:</p>
<pre><code class="language-sh">cd agents-starter&#10;npm install&#10;npm run dev&#10;</code></pre>
<p>This creates a project with:</p>
<ul>
<li><code>src/server.ts</code> — Your agent code</li>
<li><code>src/client.tsx</code> — React frontend</li>
<li><code>wrangler.jsonc</code> — Cloudflare configuration</li>
<li><code>tsconfig.json</code> — Extends <code>agents/tsconfig</code> for correct decorator and module settings</li>
<li><code>vite.config.ts</code> — Includes the <code>agents/vite</code> plugin for decorator support</li>
</ul>
<p>The starter template includes two important SDK integrations. If you are setting up a project manually, add both:</p>
<p><strong>tsconfig.json</strong> — extends <code>agents/tsconfig</code>, which sets <code>target: &quot;ES2021&quot;</code> and other recommended options:</p>
<pre><code class="language-json">{&#10;	&quot;extends&quot;: &quot;agents/tsconfig&quot;&#10;}&#10;</code></pre>
<p><strong>vite.config.ts</strong> — includes the <code>agents()</code> plugin, which handles TC39 decorator transforms (required for <code>@callable()</code> in Vite 8):</p>
<pre><code class="language-ts">import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;import react from &quot;@vitejs/plugin-react&quot;;&#10;import agents from &quot;agents/vite&quot;;&#10;import { defineConfig } from &quot;vite&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [agents(), react(), cloudflare()],&#10;});&#10;</code></pre>
<p>Open <a href="http://localhost:5173">http://localhost:5173</a> to see your agent in action.</p>
<h2 id="your-first-agent">Your first agent</h2>
<p>Build a simple counter agent from scratch. Replace <code>src/server.ts</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1865.md")
</div>
<p>Update <code>wrangler.jsonc</code> to register the agent:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1866.md")
</div>
<p><strong>Key points:</strong></p>
<ul>
<li><code>name</code> in bindings becomes the property on <code>env</code> (for example, <code>env.CounterAgent</code>)</li>
<li><code>class_name</code> must exactly match your exported class name</li>
<li><code>new_sqlite_classes</code> enables SQLite storage for state persistence</li>
<li><code>nodejs_compat</code> flag is required for the agents package</li>
</ul>
<h2 id="connect-from-react">Connect from React</h2>
<p>Replace <code>src/client.tsx</code>:</p>
<pre><code class="language-tsx">import &quot;./styles.css&quot;;&#10;import { createRoot } from &quot;react-dom/client&quot;;&#10;import { useState } from &quot;react&quot;;&#10;import { useAgent } from &quot;agents/react&quot;;&#10;import type { CounterAgent, CounterState } from &quot;./server&quot;;&#10;&#10;export default function App() {&#10;	const [count, setCount] = useState(0);&#10;&#10;	// Connect to the Counter agent&#10;	const agent = useAgent&lt;CounterAgent, CounterState&gt;({&#10;		agent: &quot;CounterAgent&quot;,&#10;		onStateUpdate: (state) =&gt; setCount(state.count),&#10;	});&#10;&#10;	return (&#10;		&lt;div style={{ padding: &quot;2rem&quot;, fontFamily: &quot;system-ui&quot; }}&gt;&#10;			&lt;h1&gt;Counter Agent&lt;/h1&gt;&#10;			&lt;p style={{ fontSize: &quot;3rem&quot; }}&gt;{count}&lt;/p&gt;&#10;			&lt;div style={{ display: &quot;flex&quot;, gap: &quot;1rem&quot; }}&gt;&#10;				&lt;button onClick={() =&gt; agent.stub.decrement()}&gt;-&lt;/button&gt;&#10;				&lt;button onClick={() =&gt; agent.stub.reset()}&gt;Reset&lt;/button&gt;&#10;				&lt;button onClick={() =&gt; agent.stub.increment()}&gt;+&lt;/button&gt;&#10;			&lt;/div&gt;&#10;		&lt;/div&gt;&#10;	);&#10;}&#10;&#10;const root = createRoot(document.getElementById(&quot;root&quot;)!);&#10;root.render(&lt;App /&gt;);&#10;</code></pre>
<p>Key points:</p>
<ul>
<li><code>useAgent</code> connects to your agent via WebSocket</li>
<li><code>onStateUpdate</code> fires whenever the agent's state changes</li>
<li><code>agent.stub.methodName()</code> calls methods marked with <code>@callable()</code> on your agent</li>
</ul>
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
<h2 id="connect-from-vanilla-javascript">Connect from vanilla JavaScript</h2>
<p>If you are not using React:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1867.md")
</div>
<h2 id="deploy-to-cloudflare">Deploy to Cloudflare</h2>
<pre><code class="language-sh">npm run deploy&#10;</code></pre>
<p>Your agent is now live on Cloudflare's global network, running close to your users.</p>
<h2 id="common-integration-patterns">Common integration patterns</h2>
<h3 id="agents-behind-authentication">Agents behind authentication</h3>
<p>Check auth before routing to agents:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1868.md")
</div>
<h3 id="custom-agent-path-prefix">Custom agent path prefix</h3>
<p>By default, agents are routed at <code>/agents/{agent-name}/{instance-name}</code>. You can customize this:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1869.md")
</div>
<p>Refer to <a href="/agents/runtime/communication/routing/">Routing</a> for more options including CORS, custom instance naming, and location hints.</p>
<h3 id="accessing-agents-from-server-code">Accessing agents from server code</h3>
<p>You can interact with agents directly from your Worker code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1870.md")
</div>
<h3 id="adding-multiple-agents">Adding multiple agents</h3>
<p>Add more agents by extending the configuration:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1871.md")
</div>
<p>Update the Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1872.md")
</div>
<p>Export all agents from your entry point:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1873.md")
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
@markup("md", "content/.markup/bodies/1874.md")
</div>
<h3 id="websocket-connection-fails">WebSocket connection fails</h3>
<p>Ensure your routing passes the response unchanged:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1875.md")
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
@markup("md", "content/.markup/bodies/1876.md")
</div>
<h3 id="type-errors-with-agent-stub">Type errors with <code>agent.stub</code></h3>
<p>Add the agent and state type parameters:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1877.md")
</div>
<h3 id="syntaxerror-invalid-or-unexpected-token-with-callable"><code>SyntaxError: Invalid or unexpected token</code> with <code>@callable()</code></h3>
<p>If your dev server fails with <code>SyntaxError: Invalid or unexpected token</code>, set <code>&quot;target&quot;: &quot;ES2021&quot;</code> in your <code>tsconfig.json</code>. This ensures that Vite's esbuild transpiler downlevels TC39 decorators instead of passing them through as native syntax.</p>
<pre><code class="language-json">{&#10;	&quot;compilerOptions&quot;: {&#10;		&quot;target&quot;: &quot;ES2021&quot;&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/1864.md")
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
