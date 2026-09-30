---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/execution/sub-agents/
  description: Spawn child agents with isolated storage and typed RPC using subAgent(), abortSubAgent(), and deleteSubAgent().
  full_title: Sub-agents · Cloudflare Agents docs
  head_html: <title>Sub-agents · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Spawn child agents with isolated storage and typed RPC using subAgent(), abortSubAgent(), and deleteSubAgent()."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/execution/sub-agents/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/execution/sub-agents/index.md"><meta property="og:title" content="Sub-agents · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Spawn child agents with isolated storage and typed RPC using subAgent(), abortSubAgent(), and deleteSubAgent()."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/execution/sub-agents/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/execution/sub-agents/#page","headline":"Sub-agents \u00b7 Cloudflare Agents docs","description":"Spawn child agents with isolated storage and typed RPC using subAgent(), abortSubAgent(), and deleteSubAgent().","url":"https://developers.cloudflare.com/agents/runtime/execution/sub-agents/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/execution/sub-agents/
  schema: 1
---
<p>Spawn child agents as co-located Durable Objects with their own isolated SQLite storage. The parent gets a typed RPC stub for calling methods on the child — every public method on the child class is callable as a remote procedure call with Promise-wrapped return types.</p>
<p>Use sub-agents when a single user or entity owns an open-ended set of long-lived agents, such as chats, documents, sessions, shards, or projects. Each sub-agent runs in parallel with its own state while the parent coordinates discovery, access control, and lifecycle.</p>
<p>If you want a parent chat agent to dispatch another chat-capable agent during a single turn and render that child's progress inline, use <a href="/agents/runtime/execution/agent-tools/">Agents as tools</a>. Agents as tools are built on sub-agents, but add a parent-side run registry, streaming <code>agent-tool-event</code> frames, replay, cancellation, and cleanup.</p>
<h2 id="quick-start">Quick start</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2436.md")
</div>
<p>Both classes must be exported from the worker entry point. No separate Durable Object bindings are needed for child-only classes — child classes are discovered automatically via <code>ctx.exports</code>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2437.md")
</div>
<p>Only the top-level parent agent needs a Durable Object binding and migration. Child agents are created as facets of the parent — they share the same machine but have fully isolated SQLite storage.</p>
<h2 id="subagent">subAgent</h2>
<p>Get or create a named sub-agent. The first call for a given name triggers the child's <code>onStart()</code>. Subsequent calls return the existing instance.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2438.md")
</div>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cls</code></td>
<td><code>SubAgentClass&lt;T&gt;</code></td>
<td>The Agent subclass. Must be exported from the worker entry point, and the export name must match the class name.</td>
</tr>
<tr>
<td><code>name</code></td>
<td><code>string</code></td>
<td>Unique name for this child instance. The same name always returns the same child.</td>
</tr>
</tbody>
</table>
<p>Returns a <code>SubAgentStub&lt;T&gt;</code> — a typed RPC stub where every user-defined method on <code>T</code> is available as a Promise-returning remote call.</p>
<h3 id="subagentstub">SubAgentStub</h3>
<p>The stub exposes all public instance methods you define on the child class. Methods inherited from <code>Agent</code> (lifecycle hooks, <code>setState</code>, <code>broadcast</code>, <code>sql</code>, and so on) are excluded — only your custom methods appear on the stub.</p>
<p>Return types are automatically wrapped in <code>Promise</code> if they are not already:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2439.md")
</div>
<h3 id="requirements">Requirements</h3>
<ul>
<li>The child class must extend <code>Agent</code></li>
<li>The child class must be exported from the worker entry point (<code>export class MyChild extends Agent</code>)</li>
<li>The export name must match the class name — <code>export { Foo as Bar }</code> is not supported</li>
<li>The top-level parent class must be bound as a Durable Object namespace in <code>wrangler.jsonc</code></li>
<li>A facet-only child class does not need to be registered under <code>new_sqlite_classes</code> unless the same class is also bound as a top-level Durable Object elsewhere</li>
<li>Nested facet parents do not need their own top-level Durable Object bindings; the runtime resolves nested children through the root parent namespace</li>
<li>The child class name cannot be <code>Sub</code>, because <code>/sub/</code> is reserved as the URL separator for nested routes</li>
</ul>
<h3 id="notes-for-testing">Notes for testing</h3>
<p>Tests that use <code>@cloudflare/vitest-plugin</code> may need to list facet classes as test-only Durable Object bindings so <code>ctx.exports</code> provides a facet-compatible class value. Keep those facet classes out of <code>new_sqlite_classes</code>; the extra binding belongs only in test <code>wrangler.jsonc</code> files and is not a production Worker requirement.</p>
<h2 id="abortsubagent">abortSubAgent</h2>
<p>Forcefully stop a running sub-agent. The child stops executing immediately and restarts on the next <code>subAgent()</code> call. Storage is preserved — only the running instance is killed.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2440.md")
</div>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cls</code></td>
<td><code>SubAgentClass</code></td>
<td>The Agent subclass used when creating the child</td>
</tr>
<tr>
<td><code>name</code></td>
<td><code>string</code></td>
<td>Name of the child to abort</td>
</tr>
<tr>
<td><code>reason</code></td>
<td><code>unknown</code></td>
<td>Error thrown to any pending or future RPC callers</td>
</tr>
</tbody>
</table>
<p>Abort is transitive — if the child has its own sub-agents, they are also aborted.</p>
<h2 id="deletesubagent">deleteSubAgent</h2>
<p>Abort the child (if running) and permanently wipe its storage. The next <code>subAgent()</code> call creates a fresh instance with empty SQLite.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2441.md")
</div>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cls</code></td>
<td><code>SubAgentClass</code></td>
<td>The Agent subclass used when creating the child</td>
</tr>
<tr>
<td><code>name</code></td>
<td><code>string</code></td>
<td>Name of the child to delete</td>
</tr>
</tbody>
</table>
<p>Deletion is transitive — the child's own sub-agents are also deleted.</p>
<h2 id="introspection-and-access-control">Introspection and access control</h2>
<h3 id="hassubagent"><code>hasSubAgent</code></h3>
<p>Check whether a child has been spawned and not deleted. This is backed by a framework-maintained SQLite registry.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2442.md")
</div>
<h3 id="listsubagents"><code>listSubAgents</code></h3>
<p>List spawned sub-agents, optionally filtered by class. Rows are returned in creation order.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2443.md")
</div>
<h3 id="onbeforesubagent"><code>onBeforeSubAgent</code></h3>
<p>Override this middleware hook on the parent to gate, mutate, or short-circuit incoming <code>/sub/</code> requests before the framework wakes the child. It mirrors <code>onBeforeConnect</code> and <code>onBeforeRequest</code>.</p>
<p>The hook can return:</p>
<table>
<thead>
<tr>
<th>Return value</th>
<th>Effect</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>void</code></td>
<td>Forward the original request to the child</td>
</tr>
<tr>
<td><code>Request</code></td>
<td>Forward a modified request</td>
</tr>
<tr>
<td><code>Response</code></td>
<td>Short-circuit and do not wake the child</td>
</tr>
</tbody>
</table>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2444.md")
</div>
<p>WebSocket upgrade requests flow through this hook the same way as plain HTTP requests. If you return a modified <code>Request</code>, preserve the original WebSocket upgrade headers.</p>
<h2 id="parent-and-child-identity">Parent and child identity</h2>
<p>Sub-agents know who their parent is through <code>this.parentPath</code> and <code>this.selfPath</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2445.md")
</div>
<p><code>parentPath</code> is root-first, so the direct parent is always <code>parentPath.at(-1)</code>. Top-level agents have <code>parentPath === []</code>.</p>
<p>Use <code>parentAgent(Cls)</code> from a sub-agent to get a typed RPC stub to its immediate parent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2446.md")
</div>
<p><code>parentAgent()</code> resolves the direct parent even when that parent is itself a facet-only sub-agent, using a root-side RPC bridge under the hood. This gives you typed method calls to the immediate parent without requiring every nested parent class to be bound as a top-level Durable Object.</p>
<p>For grandparents and further ancestors, iterate <code>this.parentPath</code> and call <code>getAgentByName()</code> directly. If the binding name does not match the class name, call <code>getAgentByName(env.MY_BINDING, this.parentPath.at(-1)!.name)</code> instead of <code>parentAgent()</code>.</p>
<h2 id="client-routing">Client routing</h2>
<h3 id="useagent-sub"><code>useAgent({ sub })</code></h3>
<p>Extend any <code>useAgent</code> call with a <code>sub</code> chain to connect to a descendant facet:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2447.md")
</div>
<p>The hook builds a URL like <code>/agents/inbox/user-123/sub/chat/chat-abc</code> and opens a direct WebSocket to the <code>Chat</code> child. Every other <code>useAgent</code> feature works as usual: state sync, <code>stub</code> calls, <code>@callable</code> RPC, and <code>useAgentChat</code> on top of the returned socket.</p>
<h3 id="direct-http-and-websocket-urls">Direct HTTP and WebSocket URLs</h3>
<p>Use <code>buildAgentPath()</code> to create a canonical pathname for an Agent identity. The same pathname supports HTTP requests and WebSocket connections.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2448.md")
</div>
<p>Inside an Agent, pass <code>this.selfPath</code> directly. If the root Durable Object binding name differs from its class name, also pass <code>rootBinding</code> in the options. Use <code>buildAgentUrl()</code> to add a public origin for callbacks, webhooks, approvals, or asynchronous job completion.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2449.md")
</div>
<p>Pass the incoming request to <code>routeAgentRequest()</code>. Each ancestor runs <code>onBeforeSubAgent</code> before the destination receives the request. For a sub-agent destination, routing removes the nested <code>/sub/</code> segments, so its pathname is the <code>leafPath</code> suffix.</p>
<p><code>buildAgentUrl()</code> accepts an HTTP(S) or WS(S) origin. The origin cannot contain credentials, a pathname, a query, or a fragment. Add callback query parameters through the returned URL <code>searchParams</code> property.</p>
<p>Root Agent names must already be valid pathname segments. The <code>sub</code> segment is reserved in routing prefixes, class and binding names, and root Agent names. The helper URL-encodes descendant names, including spaces, Unicode characters, <code>/</code>, and other URL-reserved characters.</p>
<h3 id="custom-http-routing">Custom HTTP routing</h3>
<p>For fetch handlers that do their own top-level URL parsing, use <code>routeSubAgentRequest()</code> to dispatch a request into a sub-agent from an already-resolved parent stub:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2450.md")
</div>
<p><code>fromPath</code> takes any pathname that contains a sub-agent tail, such as <code>/sub/chat/chat-abc</code>. You can pass the result of <code>buildAgentPath()</code> directly. The helper parses it, runs the parent <code>onBeforeSubAgent</code> hook, and forwards the request into the facet.</p>
<h3 id="external-typed-rpc">External typed RPC</h3>
<p>From inside the parent Durable Object, <code>this.subAgent(Cls, name)</code> returns a typed stub. From outside the parent, use <code>getSubAgentByName()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2451.md")
</div>
<p><code>getSubAgentByName()</code> returns an RPC-only proxy. Method calls work, but <code>.fetch()</code> throws. Use <code>routeSubAgentRequest()</code> for HTTP and WebSocket forwarding.</p>
<h2 id="storage-isolation">Storage isolation</h2>
<p>Each sub-agent has its own SQLite database, completely isolated from the parent and from other sub-agents. A parent writing to <code>this.sql</code> and a child writing to <code>this.sql</code> operate on different databases:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2452.md")
</div>
<h2 id="naming-and-identity">Naming and identity</h2>
<p>Two different classes can share the same user-facing name — they are resolved independently. The internal key is a composite of class name and facet name:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2453.md")
</div>
<p>The child's <code>this.name</code> property returns the facet name (not the parent's name):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2454.md")
</div>
<h2 id="patterns">Patterns</h2>
<h3 id="parallel-sub-agents">Parallel sub-agents</h3>
<p>Run multiple sub-agents concurrently:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2455.md")
</div>
<h3 id="nested-sub-agents">Nested sub-agents</h3>
<p>Sub-agents can spawn their own sub-agents, forming a tree:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2456.md")
</div>
<h3 id="callback-streaming">Callback streaming</h3>
<p>Pass an <code>RpcTarget</code> callback to stream results from a sub-agent back to the parent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2457.md")
</div>
<h2 id="scheduling-and-durable-work">Scheduling and durable work</h2>
<p>Sub-agents can schedule their own callbacks and run durable fibers:</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Behavior in sub-agent</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>schedule()</code> / <code>scheduleEvery()</code></td>
<td>Work normally and run callbacks inside the sub-agent</td>
</tr>
<tr>
<td><code>cancelSchedule()</code></td>
<td>Works for schedules owned by the calling sub-agent</td>
</tr>
<tr>
<td><code>getScheduleById()</code> / <code>listSchedules()</code></td>
<td>Work and return schedules scoped to the calling sub-agent</td>
</tr>
<tr>
<td><code>keepAlive()</code> / <code>keepAliveWhile()</code></td>
<td>Work by delegating the heartbeat to the top-level parent</td>
</tr>
<tr>
<td><code>runFiber()</code></td>
<td>Works, with fiber rows and snapshots stored in the child's SQLite database</td>
</tr>
<tr>
<td><code>setState()</code></td>
<td>Works normally and writes to the child's own storage</td>
</tr>
<tr>
<td><code>this.sql</code></td>
<td>Works normally and points at the child's own SQLite database</td>
</tr>
<tr>
<td><code>subAgent()</code></td>
<td>Works, so sub-agents can spawn their own children</td>
</tr>
</tbody>
</table>
<p>The top-level parent still owns the physical Durable Object alarm because facets do not have independent alarm slots. The Agents SDK records which child owns each scheduled callback or recovery check, wakes the parent, and routes the work back into the child. The callback still runs with the sub-agent as <code>this</code>, so it uses the child's state, SQLite storage, and <code>getCurrentAgent()</code> context.</p>
<p>The older synchronous <code>getSchedule()</code> and <code>getSchedules()</code> APIs throw inside sub-agents because scheduled rows are stored on the top-level parent. Use <code>getScheduleById()</code> and <code>listSchedules()</code> instead.</p>
<p>Calling <code>this.destroy()</code> inside a sub-agent delegates cleanup to the parent. The parent cancels that sub-agent's schedules, removes recovery metadata for the sub-agent and its descendants, removes the registry entry, and asks the runtime to wipe the child storage. Treat <code>this.destroy()</code> as fire-and-forget because deleting the sub-agent can abort its isolate before the method returns cleanly.</p>
<h3 id="workflows-from-sub-agents">Workflows from sub-agents</h3>
<p>Sub-agents can also start <a href="/agents/runtime/execution/run-workflows/">Workflows</a> with <code>this.runWorkflow()</code>. Workflow tracking is local to the sub-agent's SQLite database, and <code>AgentWorkflow.agent</code> routes RPC, callbacks, state updates, and broadcasts back to the originating sub-agent. Parent agents do not automatically list or control child-started workflows.</p>
<p>Because <code>SubAgentStub&lt;T&gt;</code> only exposes user-defined child methods, add child wrapper methods for controls such as <code>getWorkflow()</code>, <code>approveWorkflow()</code>, or <code>terminateWorkflow()</code>, then call those wrappers through <code>await this.subAgent(Child, name)</code>. If you pass <code>runWorkflow(..., { agentBinding })</code> from a sub-agent, use the root Agent binding name, not a child binding name.</p>
<p>For sub-agent workflow origins, <code>AgentWorkflow.agent</code> is RPC-only. Use it to call Agent methods, but use <code>routeSubAgentRequest()</code> or the nested <code>/agents/{parent}/{name}/sub/{child}/{name}</code> URL shape for external HTTP or WebSocket routing instead of <code>this.agent.fetch()</code>.</p>
<h2 id="example">Example</h2>
<div class="nb-card nb-link-card"><h3 id="card-multi-session-chat-example-https-github-com-cloudflare-agents-tree-main-examples-multi-ai-chat"><a href="https://github.com/cloudflare/agents/tree/main/examples/multi-ai-chat">Multi-session chat example</a></h3><p>Build an inbox where each chat is an AIChatAgent sub-agent with isolated state and direct client routing.</p></div>
<h2 id="related">Related</h2>
<ul>
<li><a href="/agents/harnesses/think/">Think</a> — <code>chat()</code> method for streaming AI turns through sub-agents</li>
<li><a href="/agents/concepts/agentic-patterns/long-running-agents/">Long-running agents</a> — sub-agent delegation in the context of multi-week agent lifetimes</li>
<li><a href="/agents/runtime/lifecycle/callable-methods/">Callable methods</a> — RPC via <code>@callable</code> and service bindings</li>
<li><a href="/agents/runtime/execution/agent-tools/">Agents as tools</a> — run Think or <code>AIChatAgent</code> sub-agents as retained, streaming tools</li>
<li><a href="/agents/runtime/execution/schedule-tasks/">Schedule tasks</a> — scheduling primitives for top-level agents and sub-agents</li>
</ul>
