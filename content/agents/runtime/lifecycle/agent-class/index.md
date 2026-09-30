<p>The core of the <code>agents</code> library is the <code>Agent</code> class. You extend it, override a few methods, and get state management, WebSockets, scheduling, RPC, and more for free. This page explains how <code>Agent</code> is built, layer by layer, so you understand what is happening under the hood.</p>
<p>The snippets shown here are illustrative and do not necessarily represent best practices. For the full API, refer to the <a href="/agents/runtime/">API reference</a> and the <a href="https://github.com/cloudflare/agents/blob/main/packages/agents/src/index.ts">source code</a>.</p>
<h2 id="what-is-the-agent">What is the Agent?</h2>
<p>The <code>Agent</code> class is an extension of <code>DurableObject</code> — agents <em>are</em> Durable Objects. If you are not familiar with Durable Objects, read <a href="/durable-objects/">What are Durable Objects</a> first. At their core, Durable Objects are globally addressable (each instance has a unique ID), single-threaded compute instances with long-term storage (key-value and SQLite).</p>
<p><code>Agent</code> does not extend <code>DurableObject</code> directly. It extends <code>Server</code> from the <a href="https://github.com/cloudflare/partykit/tree/main/packages/partyserver"><code>partyserver</code></a> package, which extends <code>DurableObject</code>. Think of it as layers: <strong>DurableObject</strong> &gt; <strong>Server</strong> &gt; <strong>Agent</strong>.</p>
<h2 id="layer-0-durable-object">Layer 0: Durable Object</h2>
<p>Let's briefly consider which primitives are exposed by Durable Objects so we understand how the outer layers make use of them. The Durable Object class comes with:</p>
<h3 id="constructor"><code>constructor</code></h3>
<pre><code class="language-ts">constructor(ctx: DurableObjectState, env: Env) {}&#10;</code></pre>
<p>The Workers runtime always calls the constructor to handle things internally. This means two things:</p>
<ol>
<li>While the constructor is called every time the Durable Object is initialized, the signature is fixed. Developers cannot add or update parameters from the constructor.</li>
<li>Instead of instantiating the class manually, developers must use the binding APIs and do it through the <a href="/durable-objects/api/namespace/">DurableObjectNamespace</a>.</li>
</ol>
<h3 id="rpc">RPC</h3>
<p>By writing a Durable Object class which inherits from the built-in type <code>DurableObject</code>, public methods are exposed as RPC methods, which developers can call using a <a href="/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/#invoking-methods-on-a-durable-object">DurableObjectStub from a Worker</a>.</p>
<pre><code class="language-ts">// This instance could&#x27;ve been active, hibernated,&#10;// not initialized or maybe had never even been created!&#10;const stub = env.MY_DO.getByName(&quot;foo&quot;);&#10;&#10;// We can call any public method on the class. The runtime&#10;// ensures the constructor is called if the instance was not active.&#10;await stub.bar();&#10;</code></pre>
<h3 id="fetch"><code>fetch()</code></h3>
<p>Durable Objects can take a <code>Request</code> from a Worker and send a <code>Response</code> back. This can only be done through the <a href="/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/#invoking-the-fetch-handler"><code>fetch</code></a> method (which the developer must implement).</p>
<h3 id="websockets">WebSockets</h3>
<p>Durable Objects include first-class support for <a href="/durable-objects/best-practices/websockets/">WebSockets</a>. A Durable Object can accept a WebSocket it receives from a <code>Request</code> in <code>fetch</code> and forget about it. The base class provides methods that developers can implement that are called as callbacks. They effectively replace the need for event listeners.</p>
<p>The base class provides <code>webSocketMessage(ws, message)</code>, <code>webSocketClose(ws, code, reason, wasClean)</code> and <code>webSocketError(ws , error)</code> (<a href="/workers/runtime-apis/websockets">API</a>).</p>
<pre><code class="language-ts">export class MyDurableObject extends DurableObject {&#10;	async fetch(request) {&#10;		// Creates two ends of a WebSocket connection.&#10;		const webSocketPair = new WebSocketPair();&#10;		const [client, server] = Object.values(webSocketPair);&#10;&#10;		// Calling `acceptWebSocket()` connects the WebSocket to the Durable Object, allowing the WebSocket to send and receive messages.&#10;		this.ctx.acceptWebSocket(server);&#10;&#10;		return new Response(null, {&#10;			status: 101,&#10;			webSocket: client,&#10;		});&#10;	}&#10;&#10;	async webSocketMessage(ws, message) {&#10;		ws.send(message);&#10;	}&#10;}&#10;</code></pre>
<h3 id="alarm"><code>alarm()</code></h3>
<p>HTTP and RPC requests are not the only entrypoints for a Durable Object. Alarms allow developers to schedule an event to trigger at a later time. Whenever the next alarm is due, the runtime will call the <code>alarm()</code> method, which is left to the developer to implement.</p>
<p>To schedule an alarm, you can use the <code>this.ctx.storage.setAlarm()</code> method. For more information, refer to <a href="/durable-objects/api/alarms/">Alarms</a>.</p>
<h3 id="this-ctx"><code>this.ctx</code></h3>
<p>The base <code>DurableObject</code> class sets the <a href="/durable-objects/api/state/">DurableObjectState</a> into <code>this.ctx</code>. There are a lot of interesting methods and properties, but we will focus on <code>this.ctx.storage</code>.</p>
<h3 id="this-ctx-storage"><code>this.ctx.storage</code></h3>
<p><a href="/durable-objects/api/sqlite-storage-api/">DurableObjectStorage</a> is the main interface with the Durable Object's persistence mechanisms, which include both a KV and SQLITE <strong>synchronous</strong> APIs.</p>
<pre><code class="language-ts">const sql = this.ctx.storage.sql;&#10;&#10;// Synchronous SQL query&#10;const rows = sql.exec(&quot;SELECT * FROM contacts WHERE country = ?&quot;, &quot;US&quot;);&#10;&#10;// Key-value storage&#10;const token = this.ctx.storage.get(&quot;someToken&quot;);&#10;</code></pre>
<h3 id="this-ctx-env"><code>this.ctx.env</code></h3>
<p>Lastly, it is worth mentioning that the Durable Object also has the Worker <code>Env</code> in <code>this.env</code>. Learn more in <a href="/workers/runtime-apis/bindings">Bindings</a>.</p>
<h2 id="layer-1-server-partyserver">Layer 1: <code>Server</code> (partyserver)</h2>
<p>Now that you have seen what Durable Objects provide out of the box, the <code>Server</code> class from <a href="https://github.com/cloudflare/partykit/tree/main/packages/partyserver"><code>partyserver</code></a> will make more sense. It is an opinionated <code>DurableObject</code> wrapper that replaces low-level primitives with developer-friendly callbacks.</p>
<p><code>Server</code> does not add any storage operations of its own — it only wraps the Durable Object lifecycle.</p>
<h3 id="addressing">Addressing</h3>
<p><code>partyserver</code> exposes helpers to address Durable Objects by name instead of going through bindings manually. This includes a URL routing scheme (<code>&lt;your-worker&gt;/servers/:durableClass/:durableName</code>) that the Agent layer builds on.</p>
<pre><code class="language-ts">// Note the await here!&#10;const stub = await getServerByName(env.MY_DO, &quot;foo&quot;);&#10;&#10;// We can still call RPC methods.&#10;await stub.bar();&#10;</code></pre>
<p>The URL scheme also enables a request router. In the Agent layer, this is re-exported as <code>routeAgentRequest</code>:</p>
<pre><code class="language-ts">  async fetch(request: Request, env: Env, ctx: ExecutionContext) {&#10;    const res = await routeAgentRequest(request, env);&#10;&#10;    if (res) return res;&#10;&#10;    return new Response(&quot;Not found&quot;, { status: 404 });&#10;  }&#10;</code></pre>
<h3 id="onstart"><code>onStart</code></h3>
<p>The addressing layer allows <code>Server</code> to expose an <code>onStart</code> callback that runs every time the Durable Object starts up (after eviction, hibernation, or first creation) and before any <code>fetch</code> or RPC call.</p>
<pre><code class="language-ts">class MyServer extends Server {&#10;	onStart() {&#10;		// Some initialization logic that you wish&#10;		// to run every time the DO is started up.&#10;		const sql = this.ctx.storage.sql;&#10;		sql.exec(`...`);&#10;	}&#10;}&#10;</code></pre>
<h3 id="onrequest-and-onconnect"><code>onRequest</code> and <code>onConnect</code></h3>
<p><code>Server</code> already implements <code>fetch</code> for the underlying Durable Object and exposes two different callbacks that developers can make use of, <code>onRequest</code> and <code>onConnect</code> for HTTP requests and incoming WS connections, respectively (WebSocket connections are accepted by default).</p>
<pre><code class="language-ts">class MyServer extends Server {&#10;	async onRequest(request: Request) {&#10;		const url = new URL(request.url);&#10;&#10;		return new Response(`Hello from ${url.origin}!`);&#10;	}&#10;&#10;	async onConnect(conn, ctx) {&#10;		const { request } = ctx;&#10;		const url = new URL(request.url);&#10;&#10;		// Connections are a WebSocket wrapper&#10;		conn.send(`Hello from ${url.origin}!`);&#10;	}&#10;}&#10;</code></pre>
<h3 id="websockets-1">WebSockets</h3>
<p>Just as <code>onConnect</code> is the callback for every new connection, <code>Server</code> also provides wrappers on top of the default callbacks from the <code>DurableObject</code> class: <code>onMessage</code>, <code>onClose</code> and <code>onError</code>.</p>
<p>There's also <code>this.broadcast</code> that sends a WS message to all connected clients (no magic, just a loop over <code>this.getConnections()</code>!).</p>
<h3 id="this-name"><code>this.name</code></h3>
<p>It is hard to get a Durable Object's <code>name</code> from within it. <code>partyserver</code> tries to make it available in <code>this.name</code> but it is not a perfect solution. Learn more about it in <a href="https://github.com/cloudflare/workerd/issues/2240">this GitHub issue</a>.</p>
<h2 id="layer-2-agent">Layer 2: Agent</h2>
<p>Now finally, the <code>Agent</code> class. <code>Agent</code> extends <code>Server</code> and provides opinionated primitives for stateful, schedulable, and observable agents that can communicate via RPC, WebSockets, and (even!) email.</p>
<h3 id="this-state-and-this-setstate"><code>this.state</code> and <code>this.setState()</code></h3>
<p>One of the core features of <code>Agent</code> is <strong>automatic state persistence</strong>. Developers define the shape of their state via the generic parameter and <code>initialState</code> (which is only used if no state exists in storage), and the Agent handles loading, saving, and broadcasting state changes (check <code>Server</code>'s <code>this.broadcast()</code> above).</p>
<p><code>this.state</code> is a getter that lazily loads state from storage (SQL). State is persisted across Durable Object evictions when it is updated with <code>this.setState()</code>, which automatically serializes the state and writes it back to storage.</p>
<p>There's also <code>this.onStateChanged</code> that you can override to react to state changes.</p>
<pre><code class="language-ts">class MyAgent extends Agent&lt;Env, { count: number }&gt; {&#10;	initialState = { count: 0 };&#10;&#10;	increment() {&#10;		this.setState({ count: this.state.count + 1 });&#10;	}&#10;&#10;	onStateChanged(state, source) {&#10;		console.log(&quot;State updated:&quot;, state);&#10;	}&#10;}&#10;</code></pre>
<p>State is stored in the <code>cf_agents_state</code> SQL table. State messages are sent with <code>type: &quot;cf_agent_state&quot;</code> (both from the client and the server). Since <code>agents</code> provides <a href="/agents/runtime/lifecycle/state/#synchronizing-state">JS and React clients</a>, real-time state updates are available out of the box.</p>
<h3 id="this-sql"><code>this.sql</code></h3>
<p>The Agent provides a convenient <code>sql</code> template tag for executing queries against the Durable Object's SQL storage. It constructs parameterized queries and executes them. This uses the <strong>synchronous</strong> SQL API from <code>this.ctx.storage.sql</code>.</p>
<pre><code class="language-ts">class MyAgent extends Agent {&#10;	onStart() {&#10;		this.sql`&#10;      CREATE TABLE IF NOT EXISTS users (&#10;        id TEXT PRIMARY KEY,&#10;        name TEXT&#10;      )&#10;    `;&#10;&#10;		const userId = &quot;1&quot;;&#10;		const userName = &quot;Alice&quot;;&#10;		this.sql`INSERT INTO users (id, name) VALUES (${userId}, ${userName})`;&#10;&#10;		const users = this.sql&lt;{ id: string; name: string }&gt;`&#10;      SELECT * FROM users WHERE id = ${userId}&#10;    `;&#10;		console.log(users); // [{ id: &quot;1&quot;, name: &quot;Alice&quot; }]&#10;	}&#10;}&#10;</code></pre>
<h3 id="rpc-and-callable-methods">RPC and Callable Methods</h3>
<p><code>agents</code> takes Durable Objects RPC one step further by implementing RPC through WebSockets, so clients can call methods on the Agent directly. To make a method callable through WebSocket, use the <code>@callable()</code> decorator. Methods can return a serializable value or a stream (when using <code>@callable({ streaming: true })</code>).</p>
<pre><code class="language-ts">class MyAgent extends Agent {&#10;	@callable({ description: &quot;Add two numbers&quot; })&#10;	async add(a: number, b: number) {&#10;		return a + b;&#10;	}&#10;}&#10;</code></pre>
<p>Clients can invoke this method by sending a WebSocket message:</p>
<pre><code class="language-json">{&#10;	&quot;type&quot;: &quot;rpc&quot;,&#10;	&quot;id&quot;: &quot;unique-request-id&quot;,&#10;	&quot;method&quot;: &quot;add&quot;,&#10;	&quot;args&quot;: [2, 3]&#10;}&#10;</code></pre>
<p>For example, with the provided <code>React</code> client, it is as easy as:</p>
<pre><code class="language-ts">const { stub } = useAgent({ name: &quot;my-agent&quot; });&#10;const result = await stub.add(2, 3);&#10;console.log(result); // 5&#10;</code></pre>
<h3 id="this-queue-and-friends"><code>this.queue</code> and friends</h3>
<p>Agents include a built-in task queue for deferred execution. This is useful for offloading work or retrying operations. The available methods are <code>this.queue</code>, <code>this.dequeue</code>, <code>this.dequeueAll</code>, <code>this.dequeueAllByCallback</code>, <code>this.getQueue</code>, and <code>this.getQueues</code>.</p>
<pre><code class="language-ts">class MyAgent extends Agent {&#10;	async onConnect() {&#10;		// Queue a task to be executed later&#10;		await this.queue(&quot;processTask&quot;, { userId: &quot;123&quot; });&#10;	}&#10;&#10;	async processTask(payload: { userId: string }, queueItem: QueueItem) {&#10;		console.log(&quot;Processing task for user:&quot;, payload.userId);&#10;	}&#10;}&#10;</code></pre>
<p>Tasks are stored in the <code>cf_agents_queues</code> SQL table and are automatically flushed in sequence. If a task succeeds, it is automatically dequeued.</p>
<h3 id="this-schedule-and-friends"><code>this.schedule</code> and friends</h3>
<p>Agents support scheduled execution of methods by wrapping the Durable Object's <code>alarm()</code>. The available methods are <code>this.schedule</code>, <code>this.getSchedule</code>, <code>this.getSchedules</code>, <code>this.cancelSchedule</code>. Schedules can be one-time, delayed, or recurring (using cron expressions).</p>
<p>Since Durable Objects only allow one alarm at a time, the <code>Agent</code> class works around this by managing multiple schedules in SQL and using a single alarm.</p>
<pre><code class="language-ts">class MyAgent extends Agent {&#10;	async foo() {&#10;		// Schedule at a specific time&#10;		await this.schedule(new Date(&quot;2025-12-25T00:00:00Z&quot;), &quot;sendGreeting&quot;, {&#10;			message: &quot;Merry Christmas!&quot;,&#10;		});&#10;&#10;		// Schedule with a delay (in seconds)&#10;		await this.schedule(60, &quot;checkStatus&quot;, { check: &quot;health&quot; });&#10;&#10;		// Schedule with a cron expression&#10;		await this.schedule(&quot;0 0 * * *&quot;, &quot;dailyTask&quot;, { type: &quot;cleanup&quot; });&#10;	}&#10;&#10;	async sendGreeting(payload: { message: string }) {&#10;		console.log(payload.message);&#10;	}&#10;&#10;	async checkStatus(payload: { check: string }) {&#10;		console.log(&quot;Running check:&quot;, payload.check);&#10;	}&#10;&#10;	async dailyTask(payload: { type: string }) {&#10;		console.log(&quot;Daily task:&quot;, payload.type);&#10;	}&#10;}&#10;</code></pre>
<p>Schedules are stored in the <code>cf_agents_schedules</code> SQL table. Cron schedules automatically reschedule themselves after execution, while one-time schedules are deleted.</p>
<h3 id="this-mcp-and-friends"><code>this.mcp</code> and friends</h3>
<p><code>Agent</code> includes a multi-server MCP client. This enables your Agent to interact with external services that expose MCP interfaces. The MCP client is properly documented in <a href="/agents/model-context-protocol/apis/client-api/">MCP client API</a>.</p>
<pre><code class="language-ts">class MyAgent extends Agent {&#10;	async onStart() {&#10;		// Add an HTTP MCP server (callbackHost only needed for OAuth servers)&#10;		await this.addMcpServer(&quot;GitHub&quot;, &quot;https://mcp.github.com/mcp&quot;, {&#10;			callbackHost: &quot;https://my-worker.example.workers.dev&quot;,&#10;		});&#10;&#10;		// Add an MCP server via RPC (Durable Object binding, no HTTP overhead)&#10;		await this.addMcpServer(&quot;internal-tools&quot;, this.env.MyMCP);&#10;	}&#10;}&#10;</code></pre>
<h3 id="email-handling">Email Handling</h3>
<p>Agents can receive and reply to emails using Cloudflare's <a href="/email-service/api/route-emails/email-handler/">Email Routing</a>.</p>
<pre><code class="language-ts">class MyAgent extends Agent {&#10;	async onEmail(email: AgentEmail) {&#10;		console.log(&quot;Received email from:&quot;, email.from);&#10;		console.log(&quot;Subject:&quot;, email.headers.get(&quot;subject&quot;));&#10;&#10;		const raw = await email.getRaw();&#10;		console.log(&quot;Raw email size:&quot;, raw.length);&#10;&#10;		// Reply to the email&#10;		await this.replyToEmail(email, {&#10;			fromName: &quot;My Agent&quot;,&#10;			subject: &quot;Re: &quot; + email.headers.get(&quot;subject&quot;),&#10;			body: &quot;Thanks for your email!&quot;,&#10;			contentType: &quot;text/plain&quot;,&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>To route emails to your Agent, use <code>routeAgentEmail</code> in your Worker's email handler:</p>
<pre><code class="language-ts">export default {&#10;	async email(message, env, ctx) {&#10;		await routeAgentEmail(message, env, {&#10;			resolver: createAddressBasedEmailResolver(&quot;my-agent&quot;),&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h3 id="context-management">Context Management</h3>
<p><code>agents</code> wraps all your methods with an <code>AsyncLocalStorage</code> to maintain context throughout the request lifecycle. This allows you to access the current agent, connection, request, or email (depending on what event is being handled) from anywhere in your code:</p>
<pre><code class="language-ts">import { getCurrentAgent } from &quot;agents&quot;;&#10;&#10;function someUtilityFunction() {&#10;	const { agent, connection, request, email } = getCurrentAgent();&#10;&#10;	if (agent) {&#10;		console.log(&quot;Current agent:&quot;, agent.name);&#10;	}&#10;&#10;	if (connection) {&#10;		console.log(&quot;WebSocket connection ID:&quot;, connection.id);&#10;	}&#10;}&#10;</code></pre>
<h3 id="this-onerror"><code>this.onError</code></h3>
<p><code>Agent</code> extends <code>Server</code>'s <code>onError</code> so it can be used to handle errors that are not necessarily WebSocket errors. It is called with a <code>Connection</code> or <code>unknown</code> error.</p>
<pre><code class="language-ts">class MyAgent extends Agent {&#10;	onError(connectionOrError: Connection | unknown, error?: unknown) {&#10;		if (error) {&#10;			// WebSocket connection error&#10;			console.error(&quot;Connection error:&quot;, error);&#10;		} else {&#10;			// Server error&#10;			console.error(&quot;Server error:&quot;, connectionOrError);&#10;		}&#10;&#10;		// Optionally throw to propagate the error&#10;		throw connectionOrError;&#10;	}&#10;}&#10;</code></pre>
<h3 id="this-destroy"><code>this.destroy</code></h3>
<p><code>this.destroy()</code> drops all tables, deletes alarms, clears storage, and aborts the context. To ensure that the Durable Object is fully evicted, <code>this.ctx.abort()</code> is called asynchronously using <code>setTimeout()</code> to allow any currently executing handlers (like scheduled tasks) to complete their cleanup operations before the context is aborted.</p>
<p>This means <code>this.ctx.abort()</code> throws an uncatchable error that will show up in your logs, but it does so after yielding to the event loop (read more about it in <a href="/durable-objects/api/state/#abort">abort()</a>).</p>
<p>The <code>destroy()</code> method can be safely called within scheduled tasks. When called from within a schedule callback, the Agent sets an internal flag to skip any remaining database updates, and yields <code>ctx.abort()</code> to the event loop to ensure the alarm handler completes cleanly before the Agent is evicted.</p>
<pre><code class="language-ts">class MyAgent extends Agent {&#10;	async onStart() {&#10;		console.log(&quot;Agent is starting up...&quot;);&#10;		// Initialize your agent&#10;	}&#10;&#10;	async cleanup() {&#10;		// This wipes everything!&#10;		await this.destroy();&#10;	}&#10;&#10;	async selfDestruct() {&#10;		// Safe to call from within a scheduled task&#10;		await this.schedule(60, &quot;destroyAfterDelay&quot;, {});&#10;	}&#10;&#10;	async destroyAfterDelay() {&#10;		// This will safely destroy the Agent even when&#10;		// called from within the alarm handler&#10;		await this.destroy();&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="using-destroy-in-scheduled-tasks">Using destroy() in scheduled tasks</h3>
@markup("md", "content/.markup/bodies/2435.md")
</aside>
<h3 id="static-options"><code>static options</code></h3>
<p>Configure agent behavior by overriding <code>static options</code> on your class. All fields are optional — defaults are applied at runtime.</p>
<pre><code class="language-ts">export class MyAgent extends Agent {&#10;	static options = {&#10;		hibernate: true,&#10;		sendIdentityOnConnect: false,&#10;		retry: { maxAttempts: 5, baseDelayMs: 200, maxDelayMs: 5000 },&#10;	};&#10;}&#10;</code></pre>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>hibernate</code></td>
<td><code>boolean</code></td>
<td><code>true</code></td>
<td>Whether the agent hibernates when inactive. WebSocket connections stay open while the DO sleeps</td>
</tr>
<tr>
<td><code>sendIdentityOnConnect</code></td>
<td><code>boolean</code></td>
<td><code>true</code></td>
<td>Send identity (agent name, instance name) to clients on WebSocket connect. Set to <code>false</code> to hide sensitive instance names</td>
</tr>
<tr>
<td><code>hungScheduleTimeoutSeconds</code></td>
<td><code>number</code></td>
<td><code>30</code></td>
<td>Timeout before a running interval schedule is considered hung and force-reset. Increase for long-running callbacks</td>
</tr>
<tr>
<td><code>keepAliveIntervalMs</code></td>
<td><code>number</code></td>
<td><code>30000</code></td>
<td>Interval in milliseconds for <code>keepAlive()</code> alarm heartbeats. Lower values mean faster recovery but more frequent alarms</td>
</tr>
<tr>
<td><code>retry</code></td>
<td><code>RetryOptions</code></td>
<td><code>{ maxAttempts: 3, baseDelayMs: 100, maxDelayMs: 3000 }</code></td>
<td>Default retry options for <code>schedule()</code>, <code>queue()</code>, and <code>this.retry()</code>. Per-task options override these defaults</td>
</tr>
</tbody>
</table>
<h3 id="this-keepalive-and-this-keepalivewhile"><code>this.keepAlive()</code> and <code>this.keepAliveWhile()</code></h3>
<p>Durable Objects are evicted after a period of inactivity (typically 70–140 seconds with no incoming requests, WebSocket messages, or alarms). During long-running operations — streaming LLM responses, waiting on external APIs, running multi-step computations — the agent can be evicted mid-flight.</p>
<p><code>keepAlive()</code> creates an alarm heartbeat that prevents eviction. <code>keepAliveWhile()</code> wraps an async function and guarantees cleanup.</p>
<pre><code class="language-ts">class MyAgent extends Agent {&#10;	async handleLongTask() {&#10;		// Option 1: manual dispose&#10;		const dispose = await this.keepAlive();&#10;		try {&#10;			await longRunningComputation();&#10;		} finally {&#10;			dispose();&#10;		}&#10;&#10;		// Option 2: automatic cleanup (recommended)&#10;		const result = await this.keepAliveWhile(async () =&gt; {&#10;			return await longRunningComputation();&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p><code>AIChatAgent</code> uses <code>keepAliveWhile</code> internally to keep the agent alive during streaming LLM responses. For more details, refer to <a href="/agents/runtime/execution/schedule-tasks/#keeping-the-agent-alive">Schedule tasks — Keeping the agent alive</a>.</p>
<h3 id="routing">Routing</h3>
<p>The <code>Agent</code> class re-exports the <a href="#addressing">addressing helpers</a> as <code>getAgentByName</code> and <code>routeAgentRequest</code>.</p>
<pre><code class="language-ts">const stub = await getAgentByName(env.MY_DO, &quot;foo&quot;);&#10;await stub.someMethod();&#10;&#10;const res = await routeAgentRequest(request, env);&#10;if (res) return res;&#10;&#10;return new Response(&quot;Not found&quot;, { status: 404 });&#10;</code></pre>
<h2 id="layer-3-aichatagent">Layer 3: <code>AIChatAgent</code></h2>
<p>The <a href="/agents/communication-channels/chat/chat-agents/"><code>AIChatAgent</code></a> class from <code>@cloudflare/ai-chat</code> extends <code>Agent</code> with an opinionated layer for AI chat. It adds automatic message persistence to SQLite, resumable streaming, tool support (server-side, client-side, and human-in-the-loop), and a React hook (<code>useAgentChat</code>) for building chat UIs.</p>
<p>The full hierarchy is: <strong>DurableObject</strong> &gt; <strong>Server</strong> &gt; <strong>Agent</strong> &gt; <strong>AIChatAgent</strong>.</p>
<p>If you are building a chat agent, start with <code>AIChatAgent</code>. If you need lower-level control or are not building a chat interface, use <code>Agent</code> directly.</p>
