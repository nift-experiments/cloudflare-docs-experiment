<p>This page provides an overview of the Agents SDK. For detailed documentation on each feature, refer to the linked reference pages.</p>
<h2 id="overview">Overview</h2>
<p>The Agents SDK provides two main APIs:</p>
<table>
<thead>
<tr>
<th>API</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Server-side</strong> <code>Agent</code> class</td>
<td>Encapsulates agent logic: connections, state, methods, AI models, error handling</td>
</tr>
<tr>
<td><strong>Client-side</strong> SDK</td>
<td><code>AgentClient</code>, <code>useAgent</code>, and <code>useAgentChat</code> for connecting from browsers</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1859.md")
</aside>
<h2 id="agent-class">Agent class</h2>
<p>An Agent is a class that extends the base <code>Agent</code> class:</p>
<pre><code class="language-ts">import { Agent, routeAgentRequest } from &quot;agents&quot;;&#10;&#10;export class MyAgent extends Agent&lt;Env, State&gt; {&#10;	// Your agent logic&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		return (&#10;			(await routeAgentRequest(request, env)) ||&#10;			new Response(&quot;Not found&quot;, { status: 404 })&#10;		);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Each Agent can have millions of instances. Each instance is a separate micro-server that runs independently, allowing horizontal scaling. Instances are addressed by a unique identifier (user ID, email, ticket number, etc.).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1858.md")
</aside>
<h2 id="lifecycle">Lifecycle</h2>
<pre><code class="language-mermaid">flowchart TD&#10;    A[&quot;onStart&lt;br/&gt;(instance wakes up)&quot;] --&gt; B[&quot;onRequest&lt;br/&gt;(HTTP)&quot;]&#10;    A --&gt; C[&quot;onConnect&lt;br/&gt;(WebSocket)&quot;]&#10;    A --&gt; D[&quot;onEmail&quot;]&#10;    C --&gt; E[&quot;onMessage ↔ send()&lt;br/&gt;onError (on failure)&quot;]&#10;    E --&gt; F[&quot;onClose&quot;]&#10;</code></pre>
<table>
<thead>
<tr>
<th>Method</th>
<th>When it runs</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>onStart(props?)</code></td>
<td>When the instance starts, or wakes from hibernation. Receives optional <a href="/agents/runtime/communication/routing/#props">initialization props</a> passed via <code>getAgentByName</code> or <code>routeAgentRequest</code>.</td>
</tr>
<tr>
<td><code>onRequest(request)</code></td>
<td>For each HTTP request to the instance</td>
</tr>
<tr>
<td><code>onConnect(connection, ctx)</code></td>
<td>When a WebSocket connection is established</td>
</tr>
<tr>
<td><code>onMessage(connection, message)</code></td>
<td>For each WebSocket message received</td>
</tr>
<tr>
<td><code>onError(connection, error)</code></td>
<td>When a WebSocket error occurs</td>
</tr>
<tr>
<td><code>onClose(connection, code, reason, wasClean)</code></td>
<td>When a WebSocket connection closes</td>
</tr>
<tr>
<td><code>onEmail(email)</code></td>
<td>When an email is routed to the instance</td>
</tr>
<tr>
<td><code>onStateChanged(state, source)</code></td>
<td>When state changes (from server or client)</td>
</tr>
</tbody>
</table>
<h2 id="core-properties">Core properties</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>this.env</code></td>
<td><code>Env</code></td>
<td>Environment variables and bindings</td>
</tr>
<tr>
<td><code>this.ctx</code></td>
<td><code>ExecutionContext</code></td>
<td>Execution context for the request</td>
</tr>
<tr>
<td><code>this.state</code></td>
<td><code>State</code></td>
<td>Current persisted state</td>
</tr>
<tr>
<td><code>this.sql</code></td>
<td>Function</td>
<td>Execute SQL queries on embedded SQLite</td>
</tr>
</tbody>
</table>
<h2 id="server-side-api-reference">Server-side API reference</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Methods</th>
<th>Documentation</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>State</strong></td>
<td><code>setState()</code>, <code>onStateChanged()</code>, <code>initialState</code></td>
<td><a href="/agents/runtime/lifecycle/state/">Store and sync state</a></td>
</tr>
<tr>
<td><strong>Callable methods</strong></td>
<td><code>@callable()</code> decorator</td>
<td><a href="/agents/runtime/lifecycle/callable-methods/">Callable methods</a></td>
</tr>
<tr>
<td><strong>Scheduling</strong></td>
<td><code>schedule()</code>, <code>scheduleEvery()</code>, <code>getScheduleById()</code>, <code>listSchedules()</code></td>
<td><a href="/agents/runtime/execution/schedule-tasks/">Schedule tasks</a></td>
</tr>
<tr>
<td><strong>Durable execution</strong></td>
<td><code>runFiber()</code>, <code>startFiber()</code>, <code>stash()</code>, <code>onFiberRecovered()</code>, <code>keepAlive()</code>, <code>keepAliveWhile()</code></td>
<td><a href="/agents/runtime/execution/durable-execution/">Durable execution</a></td>
</tr>
<tr>
<td><strong>Queue</strong></td>
<td><code>queue()</code>, <code>dequeue()</code>, <code>dequeueAll()</code>, <code>getQueue()</code></td>
<td><a href="/agents/runtime/execution/queue-tasks/">Queue tasks</a></td>
</tr>
<tr>
<td><strong>WebSockets</strong></td>
<td><code>onConnect()</code>, <code>onMessage()</code>, <code>onClose()</code>, <code>broadcast()</code></td>
<td><a href="/agents/runtime/communication/websockets/">WebSockets</a></td>
</tr>
<tr>
<td><strong>HTTP/SSE</strong></td>
<td><code>onRequest()</code></td>
<td><a href="/agents/runtime/communication/http-sse/">HTTP and SSE</a></td>
</tr>
<tr>
<td><strong>Email</strong></td>
<td><code>onEmail()</code>, <code>replyToEmail()</code></td>
<td><a href="/agents/communication-channels/email/">Email routing</a></td>
</tr>
<tr>
<td><strong>Workflows</strong></td>
<td><code>runWorkflow()</code>, <code>waitForApproval()</code></td>
<td><a href="/agents/runtime/execution/run-workflows/">Run Workflows</a></td>
</tr>
<tr>
<td><strong>MCP Client</strong></td>
<td><code>addMcpServer()</code>, <code>removeMcpServer()</code>, <code>getMcpServers()</code></td>
<td><a href="/agents/model-context-protocol/apis/client-api/">MCP Client API</a></td>
</tr>
<tr>
<td><strong>AI Models</strong></td>
<td>Workers AI, OpenAI, Anthropic bindings</td>
<td><a href="/agents/runtime/operations/using-ai-models/">Using AI models</a></td>
</tr>
<tr>
<td><strong>Protocol messages</strong></td>
<td><code>shouldSendProtocolMessages()</code>, <code>isConnectionProtocolEnabled()</code></td>
<td><a href="/agents/runtime/communication/protocol-messages/">Protocol messages</a></td>
</tr>
<tr>
<td><strong>Context</strong></td>
<td><code>getCurrentAgent()</code></td>
<td><a href="/agents/runtime/lifecycle/get-current-agent/">getCurrentAgent()</a></td>
</tr>
<tr>
<td><strong>Tracing</strong></td>
<td><code>wrapAISDK()</code></td>
<td><a href="/agents/runtime/operations/observability/tracing/">Tracing</a></td>
</tr>
<tr>
<td><strong>Diagnostics channels</strong></td>
<td><code>subscribe()</code>, diagnostics channels</td>
<td><a href="/agents/runtime/operations/observability/diagnostics-channels/">Diagnostics channels</a></td>
</tr>
<tr>
<td><strong>Sub-agents</strong></td>
<td><code>subAgent()</code>, <code>abortSubAgent()</code>, <code>deleteSubAgent()</code></td>
<td><a href="/agents/runtime/execution/sub-agents/">Sub-agents</a></td>
</tr>
<tr>
<td><strong>Agents as tools</strong></td>
<td><code>runAgentTool()</code>, <code>clearAgentToolRuns()</code>, <code>hasAgentToolRun()</code></td>
<td><a href="/agents/runtime/execution/agent-tools/">Agents as tools</a></td>
</tr>
<tr>
<td><strong>Agent Skills</strong></td>
<td><code>skills</code> registry, bundled skill sources, script runners</td>
<td><a href="/agents/runtime/execution/agent-skills/">Agent Skills</a></td>
</tr>
<tr>
<td><strong>Sessions</strong></td>
<td><code>Session.create()</code>, context blocks, compaction, search</td>
<td><a href="/agents/runtime/lifecycle/sessions/">Sessions</a></td>
</tr>
<tr>
<td><strong>Think</strong></td>
<td><code>Think</code> base class, workspace tools, lifecycle hooks, extensions</td>
<td><a href="/agents/harnesses/think/">Think</a></td>
</tr>
<tr>
<td><strong>Chat SDK</strong></td>
<td><code>createChatSdkState()</code>, <code>ChatSdkStateAgent</code></td>
<td><a href="/agents/runtime/communication/chat-sdk/">Chat SDK</a></td>
</tr>
</tbody>
</table>
<h2 id="sql-api">SQL API</h2>
<p>Each Agent instance has an embedded SQLite database accessed via <code>this.sql</code>:</p>
<pre><code class="language-ts">// Create tables&#10;this.sql`CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, name TEXT)`;&#10;&#10;// Insert data&#10;this.sql`INSERT INTO users (id, name) VALUES (${id}, ${name})`;&#10;&#10;// Query data&#10;const users = this.sql&lt;User&gt;`SELECT * FROM users WHERE id = ${id}`;&#10;</code></pre>
<p>For state that needs to sync with clients, use the <a href="/agents/runtime/lifecycle/state/">State API</a> instead.</p>
<h2 id="client-side-api-reference">Client-side API reference</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Methods</th>
<th>Documentation</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>WebSocket client</strong></td>
<td><code>AgentClient</code></td>
<td><a href="/agents/communication-channels/chat/client-sdk/">Client SDK</a></td>
</tr>
<tr>
<td><strong>HTTP client</strong></td>
<td><code>agentFetch()</code></td>
<td><a href="/agents/communication-channels/chat/client-sdk/#http-requests-with-agentfetch">Client SDK</a></td>
</tr>
<tr>
<td><strong>React hook</strong></td>
<td><code>useAgent()</code></td>
<td><a href="/agents/communication-channels/chat/client-sdk/#react">Client SDK</a></td>
</tr>
<tr>
<td><strong>Chat hook</strong></td>
<td><code>useAgentChat()</code></td>
<td><a href="/agents/communication-channels/chat/client-sdk/">Client SDK</a></td>
</tr>
<tr>
<td><strong>Agent tool events</strong></td>
<td><code>useAgentToolEvents()</code></td>
<td><a href="/agents/runtime/execution/agent-tools/#render-child-timelines-in-react">Agents as tools</a></td>
</tr>
</tbody>
</table>
<p>Module-level helper exports include <code>agentTool()</code> from <code>agents/agent-tools</code>, which converts a Think or <code>AIChatAgent</code> subclass into an AI SDK tool definition.</p>
<h3 id="quick-example">Quick example</h3>
<pre><code class="language-ts">import { useAgent } from &quot;agents/react&quot;;&#10;import type { MyAgent } from &quot;./server&quot;;&#10;&#10;function App() {&#10;	const agent = useAgent&lt;MyAgent, State&gt;({&#10;		agent: &quot;my-agent&quot;,&#10;		name: &quot;user-123&quot;,&#10;	});&#10;&#10;	// Call methods on the agent&#10;	agent.stub.someMethod();&#10;&#10;	// Update state (syncs to server and all clients)&#10;	agent.setState({ count: 1 });&#10;}&#10;</code></pre>
<h2 id="chat-agents">Chat agents</h2>
<p>For AI chat applications, extend <code>AIChatAgent</code> instead of <code>Agent</code>:</p>
<pre><code class="language-ts">import { AIChatAgent } from &quot;@cloudflare/ai-chat&quot;;&#10;&#10;class ChatAgent extends AIChatAgent {&#10;	async onChatMessage(onFinish) {&#10;		// this.messages contains the conversation history&#10;		// Return a streaming response&#10;	}&#10;}&#10;</code></pre>
<p>Features include:</p>
<ul>
<li>Built-in message persistence</li>
<li>Automatic resumable streaming (reconnect mid-stream)</li>
<li>Works with <code>useAgentChat</code> React hook</li>
</ul>
<p>Refer to <a href="/agents/examples/chat-agent/">Build a chat agent</a> for a complete tutorial.</p>
<h2 id="routing">Routing</h2>
<p>Agents are accessed via URL patterns:</p>
<pre><code class="language-txt">https://your-worker.workers.dev/agents/:agent-name/:instance-name&#10;</code></pre>
<p>Use <code>routeAgentRequest()</code> in your Worker to route requests:</p>
<pre><code class="language-ts">import { routeAgentRequest } from &quot;agents&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		return (&#10;			routeAgentRequest(request, env) ||&#10;			new Response(&quot;Not found&quot;, { status: 404 })&#10;		);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Refer to <a href="/agents/runtime/communication/routing/">Routing</a> for custom paths, CORS, and instance naming patterns.</p>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/getting-started/quick-start/"><h3 id="card-quick-start-agents-getting-started-quick-start">Quick start</h3><p>Build your first agent in about 10 minutes.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/operations/configuration/"><h3 id="card-configuration-agents-runtime-operations-configuration">Configuration</h3><p>Learn about wrangler.jsonc setup and deployment.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/communication/websockets/"><h3 id="card-websockets-agents-runtime-communication-websockets">WebSockets</h3><p>Real-time bidirectional communication with clients.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/examples/chat-agent/"><h3 id="card-build-a-chat-agent-agents-examples-chat-agent">Build a chat agent</h3><p>Build AI applications with AIChatAgent.</p></a></p>
