---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/lifecycle/state/
  description: Persist and sync Agent state across clients in real time using setState, SQL storage, and bidirectional updates.
  full_title: Store and sync state · Cloudflare Agents docs
  head_html: <title>Store and sync state · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Persist and sync Agent state across clients in real time using setState, SQL storage, and bidirectional updates."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/lifecycle/state/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/lifecycle/state/index.md"><meta property="og:title" content="Store and sync state · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Persist and sync Agent state across clients in real time using setState, SQL storage, and bidirectional updates."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/lifecycle/state/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/lifecycle/state/#page","headline":"Store and sync state \u00b7 Cloudflare Agents docs","description":"Persist and sync Agent state across clients in real time using setState, SQL storage, and bidirectional updates.","url":"https://developers.cloudflare.com/agents/runtime/lifecycle/state/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/lifecycle/state/
  schema: 1
---
<p>Agents provide built-in state management with automatic persistence and real-time synchronization across all connected clients.</p>
<h2 id="overview">Overview</h2>
<p>State within an Agent is:</p>
<ul>
<li><strong>Persistent</strong> - Automatically saves to SQLite, survives restarts and hibernation</li>
<li><strong>Synchronized</strong> - Changes are broadcast to all connected WebSocket clients instantly</li>
<li><strong>Bidirectional</strong> - Both server and clients can update state</li>
<li><strong>Type-safe</strong> - Full TypeScript support with generics</li>
<li><strong>Immediately consistent</strong> - Read your own writes</li>
<li><strong>Thread-safe</strong> - Safe for concurrent updates</li>
<li><strong>Fast</strong> - State is colocated wherever the Agent is running</li>
</ul>
<p>Agent state is stored in a SQL database embedded within each individual Agent instance. You can interact with it using the higher-level <code>this.setState</code> API (recommended), which allows you to sync state and trigger events on state changes, or by directly querying the database with <code>this.sql</code>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="state-vs-props">State vs Props</h3>
@markup("md", "content/.markup/bodies/2339.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2340.md")
</div>
<h2 id="defining-initial-state">Defining initial state</h2>
<p>Use the <code>initialState</code> property to define default values for new agent instances:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2341.md")
</div>
<h3 id="type-safety">Type safety</h3>
<p>The second generic parameter to <code>Agent</code> defines your state type:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2342.md")
</div>
<h3 id="when-initial-state-applies">When initial state applies</h3>
<p>Initial state is applied lazily on first access, not on every wake:</p>
<ol>
<li><strong>New agent</strong> - <code>initialState</code> is used and persisted</li>
<li><strong>Existing agent</strong> - Persisted state is loaded from SQLite</li>
<li><strong>No <code>initialState</code> defined</strong> - <code>this.state</code> is <code>undefined</code></li>
</ol>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2343.md")
</div>
<h2 id="reading-state">Reading state</h2>
<p>Access the current state via the <code>this.state</code> getter:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2344.md")
</div>
<h3 id="undefined-state">Undefined state</h3>
<p>If you do not define <code>initialState</code>, <code>this.state</code> returns <code>undefined</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2345.md")
</div>
<h2 id="updating-state">Updating state</h2>
<p>Use <code>setState()</code> to update state. This:</p>
<ol>
<li>Saves to SQLite (persistent)</li>
<li>Broadcasts to all connected clients (excluding connections where <a href="/agents/runtime/communication/protocol-messages/"><code>shouldSendProtocolMessages</code></a> returned <code>false</code>)</li>
<li>Triggers <code>onStateChanged()</code> (after broadcast; best-effort)</li>
</ol>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2346.md")
</div>
<h3 id="state-must-be-serializable">State must be serializable</h3>
<p>State is stored as JSON, so it must be serializable:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2347.md")
</div>
<h2 id="responding-to-state-changes">Responding to state changes</h2>
<p>Override <code>onStateChanged()</code> to react when state changes (notifications/side-effects):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2348.md")
</div>
<h3 id="the-source-parameter">The source parameter</h3>
<p>The <code>source</code> shows who triggered the update:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;server&quot;</code></td>
<td>Agent called <code>setState()</code></td>
</tr>
<tr>
<td><code>Connection</code></td>
<td>A client pushed state via WebSocket</td>
</tr>
</tbody>
</table>
<p>This is useful for:</p>
<ul>
<li>Avoiding infinite loops (do not react to your own updates)</li>
<li>Validating client input</li>
<li>Triggering side effects only on client actions</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2349.md")
</div>
<h3 id="common-pattern-client-driven-actions">Common pattern: Client-driven actions</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2350.md")
</div>
<h2 id="validating-state-updates">Validating state updates</h2>
<p>If you want to validate or reject state updates, override <code>validateStateChange()</code>:</p>
<ul>
<li>Runs before persistence and broadcast</li>
<li>Must be synchronous</li>
<li>Throwing aborts the update</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2351.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2338.md")
</aside>
<h2 id="client-side-state-sync">Client-side state sync</h2>
<p>State synchronizes automatically with connected clients.</p>
<h3 id="react-useagent">React (useAgent)</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2352.md")
</div>
<h3 id="vanilla-js-agentclient">Vanilla JS (AgentClient)</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2353.md")
</div>
<h3 id="state-flow">State flow</h3>
<pre tabindex="0"><code class="language-mermaid">flowchart TD&#10;    subgraph Agent&#10;        S[&quot;this.state&lt;br/&gt;(persisted in SQLite)&quot;]&#10;    end&#10;    subgraph Clients&#10;        C1[&quot;Client 1&quot;]&#10;        C2[&quot;Client 2&quot;]&#10;        C3[&quot;Client 3&quot;]&#10;    end&#10;    C1 &amp; C2 &amp; C3 --&gt;|setState| S&#10;    S --&gt;|broadcast via WebSocket| C1 &amp; C2 &amp; C3&#10;</code></pre>
<h2 id="state-from-workflows">State from Workflows</h2>
<p>When using <a href="/agents/runtime/execution/run-workflows/">Workflows</a>, you can update agent state from workflow steps:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2354.md")
</div>
<p>These are durable operations - they persist even if the workflow retries.</p>
<h2 id="sql-api">SQL API</h2>
<p>Every individual Agent instance has its own SQL (SQLite) database that runs within the same context as the Agent itself. This means that inserting or querying data within your Agent is effectively zero-latency: the Agent does not have to round-trip across a continent or the world to access its own data.</p>
<p>You can access the SQL API within any method on an Agent via <code>this.sql</code>. The SQL API accepts template literals:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2355.md")
</div>
<p>You can also supply a TypeScript type argument to the query, which will be used to infer the type of the result:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2356.md")
</div>
<p>You do not need to specify an array type (<code>User[]</code> or <code>Array&lt;User&gt;</code>), as <code>this.sql</code> will always return an array of the specified type.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2337.md")
</aside>
<p>The SQL API exposed to an Agent is similar to the one <a href="/durable-objects/api/sqlite-storage-api/#sql-api">within Durable Objects</a>. You can use the same SQL queries with the Agent's database. Create tables and query data, just as you would with Durable Objects or <a href="/d1/">D1</a>.</p>
<h2 id="best-practices">Best practices</h2>
<h3 id="keep-state-small">Keep state small</h3>
<p>State is broadcast to all clients on every change. For large data:</p>
<pre tabindex="0"><code class="language-ts">// Bad - storing large arrays in state&#10;initialState = {&#10;  allMessages: [] // Could grow to thousands of items&#10;};&#10;&#10;// Good - store in SQL, keep state light&#10;initialState = {&#10;  messageCount: 0,&#10;  lastMessageId: null&#10;};&#10;&#10;// Query SQL for full data&#10;async getMessages(limit = 50) {&#10;  return this.sql`SELECT * FROM messages ORDER BY created_at DESC LIMIT ${limit}`;&#10;}&#10;</code></pre>
<h3 id="optimistic-updates">Optimistic updates</h3>
<p>For responsive UIs, update client state immediately:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2357.md")
</div>
<h3 id="state-vs-sql">State vs SQL</h3>
<table>
<thead>
<tr>
<th>Use State For</th>
<th>Use SQL For</th>
</tr>
</thead>
<tbody>
<tr>
<td>UI state (loading, selected items)</td>
<td>Historical data</td>
</tr>
<tr>
<td>Real-time counters</td>
<td>Large collections</td>
</tr>
<tr>
<td>Active session data</td>
<td>Relationships</td>
</tr>
<tr>
<td>Configuration</td>
<td>Queryable data</td>
</tr>
</tbody>
</table>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2358.md")
</div>
<h3 id="avoid-infinite-loops">Avoid infinite loops</h3>
<p>Be careful not to trigger state updates in response to your own updates:</p>
<pre tabindex="0"><code class="language-ts">// Bad - infinite loop&#10;onStateChanged(state: State) {&#10;  this.setState({ ...state, lastUpdated: Date.now() });&#10;}&#10;&#10;// Good - check source&#10;onStateChanged(state: State, source: Connection | &quot;server&quot;) {&#10;  if (source === &quot;server&quot;) return; // Do not react to own updates&#10;  this.setState({ ...state, lastUpdated: Date.now() });&#10;}&#10;</code></pre>
<h2 id="use-agent-state-as-model-context">Use Agent state as model context</h2>
<p>You can combine the state and SQL APIs in your Agent with its ability to <a href="/agents/runtime/operations/using-ai-models/">call AI models</a> to include historical context within your prompts to a model. Modern Large Language Models (LLMs) often have very large context windows (up to millions of tokens), which allows you to pull relevant context into your prompt directly.</p>
<p>For example, you can use an Agent's built-in SQL database to pull history, query a model with it, and append to that history ahead of the next call to the model:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2359.md")
</div>
<p>This works because each instance of an Agent has its own database, and the state stored in that database is private to that Agent: whether it is acting on behalf of a single user, a room or channel, or a deep research tool. By default, you do not have to manage contention or reach out over the network to a centralized database to retrieve and store state.</p>
<h2 id="api-reference">API reference</h2>
<h3 id="properties">Properties</h3>
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
<td><code>state</code></td>
<td><code>State</code></td>
<td>Current state (getter)</td>
</tr>
<tr>
<td><code>initialState</code></td>
<td><code>State</code></td>
<td>Default state for new agents</td>
</tr>
</tbody>
</table>
<h3 id="methods">Methods</h3>
<table>
<thead>
<tr>
<th>Method</th>
<th>Signature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>setState</code></td>
<td><code>(state: State) =&gt; void</code></td>
<td>Update state, persist, and broadcast</td>
</tr>
<tr>
<td><code>onStateChanged</code></td>
<td><code>(state: State, source: Connection | &quot;server&quot;) =&gt; void</code></td>
<td>Called when state changes</td>
</tr>
<tr>
<td><code>validateStateChange</code></td>
<td><code>(nextState: State, source: Connection | &quot;server&quot;) =&gt; void</code></td>
<td>Validate before persistence (throw to reject)</td>
</tr>
</tbody>
</table>
<h3 id="workflow-step-methods">Workflow step methods</h3>
<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>step.updateAgentState(state)</code></td>
<td>Replace agent state from workflow</td>
</tr>
<tr>
<td><code>step.mergeAgentState(partial)</code></td>
<td>Merge partial state from workflow</td>
</tr>
<tr>
<td><code>step.resetAgentState()</code></td>
<td>Reset to <code>initialState</code> from workflow</td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-agents-api-agents-runtime-agents-api"><a href="/agents/runtime/agents-api/">Agents API</a></h3><p>Complete API reference for the Agents SDK.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-build-a-chat-agent-agents-examples-chat-agent"><a href="/agents/examples/chat-agent/">Build a chat agent</a></h3><p>Build and deploy an AI chat agent.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-websockets-agents-runtime-communication-websockets"><a href="/agents/runtime/communication/websockets/">WebSockets</a></h3><p>Build interactive agents with real-time data streaming.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-run-workflows-agents-runtime-execution-run-workflows"><a href="/agents/runtime/execution/run-workflows/">Run Workflows</a></h3><p>Orchestrate asynchronous workflows from your agent.</p></div>
