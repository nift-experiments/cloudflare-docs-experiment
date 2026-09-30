---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/communication/routing/
  description: Route HTTP and WebSocket requests to Agents SDK instances using routeAgentRequest() and getAgentByName().
  full_title: Routing · Cloudflare Agents docs
  head_html: <title>Routing · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Route HTTP and WebSocket requests to Agents SDK instances using routeAgentRequest() and getAgentByName()."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/communication/routing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/communication/routing/index.md"><meta property="og:title" content="Routing · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route HTTP and WebSocket requests to Agents SDK instances using routeAgentRequest() and getAgentByName()."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/communication/routing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/communication/routing/#page","headline":"Routing \u00b7 Cloudflare Agents docs","description":"Route HTTP and WebSocket requests to Agents SDK instances using routeAgentRequest() and getAgentByName().","url":"https://developers.cloudflare.com/agents/runtime/communication/routing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/communication/routing/
  schema: 1
---
<p>This guide explains how requests are routed to agents, how naming works, and patterns for organizing your agents.</p>
<h2 id="how-routing-works">How routing works</h2>
<p>When a request comes in, <code>routeAgentRequest()</code> examines the URL and routes it to the appropriate agent instance:</p>
<pre tabindex="0"><code class="language-txt">https://your-worker.dev/agents/{agent-name}/{instance-name}&#10;                               └────┬────┘   └─────┬─────┘&#10;                               Class name     Unique instance ID&#10;                              (kebab-case)&#10;</code></pre>
<p><strong>Example URLs:</strong></p>
<table>
<thead>
<tr>
<th>URL</th>
<th>Agent Class</th>
<th>Instance</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/agents/counter/user-123</code></td>
<td><code>Counter</code></td>
<td><code>user-123</code></td>
</tr>
<tr>
<td><code>/agents/chat-room/lobby</code></td>
<td><code>ChatRoom</code></td>
<td><code>lobby</code></td>
</tr>
<tr>
<td><code>/agents/my-agent/default</code></td>
<td><code>MyAgent</code></td>
<td><code>default</code></td>
</tr>
</tbody>
</table>
<h2 id="name-resolution">Name resolution</h2>
<p>Agent class names are automatically converted to kebab-case for URLs:</p>
<table>
<thead>
<tr>
<th>Class Name</th>
<th>URL Path</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Counter</code></td>
<td><code>/agents/counter/...</code></td>
</tr>
<tr>
<td><code>MyAgent</code></td>
<td><code>/agents/my-agent/...</code></td>
</tr>
<tr>
<td><code>ChatRoom</code></td>
<td><code>/agents/chat-room/...</code></td>
</tr>
<tr>
<td><code>AIAssistant</code></td>
<td><code>/agents/ai-assistant/...</code></td>
</tr>
</tbody>
</table>
<p>The router matches both the original name and kebab-case version, so you can use either:</p>
<ul>
<li><code>useAgent({ agent: &quot;Counter&quot; })</code> → <code>/agents/counter/...</code></li>
<li><code>useAgent({ agent: &quot;counter&quot; })</code> → <code>/agents/counter/...</code></li>
</ul>
<h2 id="using-routeagentrequest">Using routeAgentRequest()</h2>
<p>The <code>routeAgentRequest()</code> function is the main entry point for agent routing:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2581.md")
</div>
<h2 id="build-agent-urls">Build Agent URLs</h2>
<p>Use <code>buildAgentPath()</code> to create a pathname for a known Agent identity. The function handles the root route and each nested <code>/sub/</code> route.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2582.md")
</div>
<p>Inside an Agent, <code>this.selfPath</code> provides the required root-first identity. If the root Durable Object binding name differs from its class name, pass the binding name as <code>rootBinding</code>. The pathname supports both HTTP requests and WebSocket connections.</p>
<p>For a custom route prefix, pass the same <code>prefix</code> to <code>buildAgentPath()</code> and <code>routeAgentRequest()</code>. Refer to <a href="/agents/runtime/execution/sub-agents/#direct-http-and-websocket-urls">Sub-agents</a> for callback and webhook examples.</p>
<h2 id="instance-naming-patterns">Instance naming patterns</h2>
<p>The instance name (the last part of the URL) determines which agent instance handles the request. Each unique name gets its own isolated agent with its own state.</p>
<h3 id="per-user-agents">Per-user agents</h3>
<p>Each user gets their own agent instance:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2583.md")
</div>
<pre tabindex="0"><code class="language-txt">/agents/user-profile/user-abc123 → User abc123&#x27;s agent&#10;/agents/user-profile/user-xyz789 → User xyz789&#x27;s agent (separate instance)&#10;</code></pre>
<h3 id="shared-rooms">Shared rooms</h3>
<p>Multiple users share the same agent instance:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2584.md")
</div>
<pre tabindex="0"><code class="language-txt">/agents/chat-room/general → All users in &quot;general&quot; share this agent&#10;</code></pre>
<h3 id="global-singleton">Global singleton</h3>
<p>A single instance for the entire application:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2585.md")
</div>
<h3 id="dynamic-naming">Dynamic naming</h3>
<p>Generate instance names based on context:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2586.md")
</div>
<h2 id="custom-url-routing">Custom URL routing</h2>
<p>For advanced use cases where you need control over the URL structure, you can bypass the default <code>/agents/{agent}/{name}</code> pattern.</p>
<h3 id="using-basepath-client-side">Using basePath (client-side)</h3>
<p>The <code>basePath</code> option lets clients connect to any URL path:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2587.md")
</div>
<p>This is useful when:</p>
<ul>
<li>You want clean URLs without the <code>/agents/</code> prefix</li>
<li>The instance name is determined server-side (for example, from auth/session)</li>
<li>You are integrating with an existing URL structure</li>
</ul>
<h3 id="server-side-instance-selection">Server-side instance selection</h3>
<p>When using <code>basePath</code>, the server must handle routing. Use <code>getAgentByName()</code> to get the agent instance, then forward the request with <code>fetch()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2588.md")
</div>
<h3 id="custom-path-with-dynamic-instance">Custom path with dynamic instance</h3>
<p>Route different paths to different instances:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2589.md")
</div>
<h3 id="receiving-the-instance-identity-client-side">Receiving the instance identity (client-side)</h3>
<p>When using <code>basePath</code>, the client does not know which instance it connected to until the server returns this information. The agent automatically sends its identity on connection:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2590.md")
</div>
<p>For <code>AgentClient</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2591.md")
</div>
<h3 id="handling-identity-changes-on-reconnect">Handling identity changes on reconnect</h3>
<p>If the identity changes on reconnect (for example, session expired and user logs in as someone else), you can handle it with <code>onIdentityChange</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2592.md")
</div>
<p>If <code>onIdentityChange</code> is not provided and identity changes, a warning is logged to help catch unexpected session changes.</p>
<h3 id="disabling-identity-for-security">Disabling identity for security</h3>
<p>If your instance names contain sensitive data (session IDs, internal user IDs), you can disable identity sending:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2593.md")
</div>
<p>When identity is disabled:</p>
<ul>
<li><code>agent.identified</code> stays <code>false</code></li>
<li><code>agent.ready</code> never resolves (use state updates instead)</li>
<li><code>onIdentity</code> and <code>onIdentityChange</code> are never called</li>
</ul>
<h3 id="when-to-use-custom-routing">When to use custom routing</h3>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Approach</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard agent access</td>
<td>Default <code>/agents/{agent}/{name}</code></td>
</tr>
<tr>
<td>Instance from auth/session</td>
<td><code>basePath</code> + <code>getAgentByName</code> + <code>fetch</code></td>
</tr>
<tr>
<td>Clean URLs (no <code>/agents/</code> prefix)</td>
<td><code>basePath</code> + custom routing</td>
</tr>
<tr>
<td>Legacy URL structure</td>
<td><code>basePath</code> + custom routing</td>
</tr>
<tr>
<td>Complex routing logic</td>
<td>Custom routing in Worker</td>
</tr>
</tbody>
</table>
<h2 id="routing-options">Routing options</h2>
<p>Both <code>routeAgentRequest()</code> and <code>getAgentByName()</code> accept options for customizing routing behavior.</p>
<h3 id="cors">CORS</h3>
<p>For cross-origin requests (common when your frontend is on a different domain):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2594.md")
</div>
<p>Or with custom CORS headers:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2595.md")
</div>
<h3 id="location-hints">Location hints</h3>
<p>For latency-sensitive applications, hint where the agent should run:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2596.md")
</div>
<p>Available location hints: <code>wnam</code>, <code>enam</code>, <code>sam</code>, <code>weur</code>, <code>eeur</code>, <code>apac</code>, <code>oc</code>, <code>afr</code>, <code>me</code></p>
<h3 id="jurisdiction">Jurisdiction</h3>
<p>For data residency requirements:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2597.md")
</div>
<h3 id="props">Props</h3>
<p>Since agents are instantiated by the runtime rather than constructed directly, <code>props</code> provides a way to pass initialization arguments:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2598.md")
</div>
<p>Props are passed to the agent's <code>onStart</code> lifecycle method:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2599.md")
</div>
<p>When using <code>props</code> with <code>routeAgentRequest</code>, the same props are passed to whichever agent matches the URL. This works well for universal context like authentication:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2600.md")
</div>
<p>For agent-specific initialization, use <code>getAgentByName</code> instead where you control exactly which agent receives the props.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2580.md")
</aside>
<h3 id="routing-retry">Routing retry</h3>
<p>Use <code>routingRetry</code> with <code>getAgentByName()</code> when server-side code should retry transient Durable Object routing failures:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2601.md")
</div>
<p>This option is useful for request forwarding and RPC paths where a short-lived routing failure should be retried before returning an error to the caller.</p>
<h3 id="hooks">Hooks</h3>
<p><code>routeAgentRequest</code> supports hooks for intercepting requests before they reach agents:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2602.md")
</div>
<p>These hooks are useful for authentication and validation. Refer to <a href="/agents/runtime/operations/cross-domain-authentication/">Cross-domain authentication</a> for detailed examples.</p>
<h2 id="server-side-agent-access">Server-side agent access</h2>
<p>You can access agents from your Worker code using <code>getAgentByName()</code> for RPC calls:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2603.md")
</div>
<p>For options like <code>locationHint</code>, <code>jurisdiction</code>, and <code>props</code>, refer to <a href="#routing-options">Routing options</a>.</p>
<h2 id="sub-paths-and-http-methods">Sub-paths and HTTP methods</h2>
<p>Requests can include sub-paths after the instance name. These are passed to your agent's <code>onRequest()</code> handler:</p>
<pre tabindex="0"><code class="language-txt">/agents/api/v1/users     → agent: &quot;api&quot;, instance: &quot;v1&quot;, path: &quot;/users&quot;&#10;/agents/api/v1/users/123 → agent: &quot;api&quot;, instance: &quot;v1&quot;, path: &quot;/users/123&quot;&#10;</code></pre>
<p>Handle sub-paths in your agent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2604.md")
</div>
<h2 id="multiple-agents">Multiple agents</h2>
<p>You can have multiple agent classes in one project. Each gets its own namespace:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2605.md")
</div>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2606.md")
</div>
<p>Each agent is accessed via its own path:</p>
<pre tabindex="0"><code class="language-txt">/agents/counter/...&#10;/agents/chat-room/...&#10;/agents/user-profile/...&#10;</code></pre>
<h2 id="request-flow">Request flow</h2>
<p>Here is how a request flows through the system:</p>
<pre tabindex="0"><code class="language-mermaid">flowchart TD&#10;    A[&quot;HTTP Request&lt;br/&gt;or WebSocket&quot;] --&gt; B[&quot;routeAgentRequest&lt;br/&gt;Parse URL path&quot;]&#10;    B --&gt; C[&quot;Find binding in&lt;br/&gt;env by name&quot;]&#10;    C --&gt; D[&quot;Get/create DO&lt;br/&gt;by instance ID&quot;]&#10;    D --&gt; E[&quot;Agent Instance&quot;]&#10;    E --&gt; F{&quot;Protocol?&quot;}&#10;    F --&gt;|WebSocket| G[&quot;onConnect(), onMessage&quot;]&#10;    F --&gt;|HTTP| H[&quot;onRequest()&quot;]&#10;</code></pre>
<h2 id="routing-with-authentication">Routing with authentication</h2>
<p>There are several ways to authenticate requests before they reach your agent.</p>
<h3 id="using-authentication-hooks">Using authentication hooks</h3>
<p>The <code>routeAgentRequest()</code> function provides <code>onBeforeConnect</code> and <code>onBeforeRequest</code> hooks for authentication:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2607.md")
</div>
<h3 id="manual-authentication">Manual authentication</h3>
<p>Check authentication before calling <code>routeAgentRequest()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2608.md")
</div>
<h3 id="using-a-framework-hono">Using a framework (Hono)</h3>
<p>If you are using a framework like <a href="https://hono.dev/">Hono</a>, authenticate in middleware before calling the agent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2609.md")
</div>
<p>For WebSocket authentication patterns (tokens in URLs, JWT refresh), refer to <a href="/agents/runtime/operations/cross-domain-authentication/">Cross-domain authentication</a>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="agent-namespace-not-found">Agent namespace not found</h3>
<p>The error message lists available agents. Check:</p>
<ol>
<li>Agent class is exported from your entry point.</li>
<li>Class name in code matches <code>class_name</code> in <code>wrangler.jsonc</code>.</li>
<li>URL uses correct kebab-case name.</li>
</ol>
<h3 id="request-returns-404">Request returns 404</h3>
<ol>
<li>Verify the URL pattern: <code>/agents/{agent-name}/{instance-name}</code>.</li>
<li>Check that <code>routeAgentRequest()</code> is called before your 404 handler.</li>
<li>Ensure the response from <code>routeAgentRequest()</code> is returned (not just called).</li>
</ol>
<h3 id="websocket-connection-fails">WebSocket connection fails</h3>
<ol>
<li>Do not modify the response from <code>routeAgentRequest()</code> for WebSocket upgrades.</li>
<li>Ensure CORS is enabled if connecting from a different origin.</li>
<li>Check browser dev tools for the actual error.</li>
</ol>
<h3 id="basepath-not-working"><code>basePath</code> not working</h3>
<ol>
<li>Ensure your Worker handles the custom path and forwards to the agent.</li>
<li>Use <code>getAgentByName()</code> + <code>agent.fetch(request)</code> to forward requests.</li>
<li>The <code>agent</code> parameter is still required but ignored when <code>basePath</code> is set.</li>
<li>Check that the server-side route matches the client's <code>basePath</code>.</li>
</ol>
<h2 id="api-reference">API reference</h2>
<h3 id="routeagentrequest-request-env-options"><code>routeAgentRequest(request, env, options?)</code></h3>
<p>Routes a request to the appropriate agent.</p>
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
<td><code>request</code></td>
<td><code>Request</code></td>
<td>The incoming request</td>
</tr>
<tr>
<td><code>env</code></td>
<td><code>Env</code></td>
<td>Environment with agent bindings</td>
</tr>
<tr>
<td><code>options.cors</code></td>
<td><code>boolean | HeadersInit</code></td>
<td>Enable CORS headers</td>
</tr>
<tr>
<td><code>options.props</code></td>
<td><code>Record&lt;string, unknown&gt;</code></td>
<td>Props passed to whichever agent handles request</td>
</tr>
<tr>
<td><code>options.locationHint</code></td>
<td><code>string</code></td>
<td>Preferred location for agent instances</td>
</tr>
<tr>
<td><code>options.jurisdiction</code></td>
<td><code>string</code></td>
<td>Data jurisdiction for agent instances</td>
</tr>
<tr>
<td><code>options.onBeforeConnect</code></td>
<td><code>Function</code></td>
<td>Callback before WebSocket connections</td>
</tr>
<tr>
<td><code>options.onBeforeRequest</code></td>
<td><code>Function</code></td>
<td>Callback before HTTP requests</td>
</tr>
</tbody>
</table>
<p><strong>Returns:</strong> <code>Promise&lt;Response | undefined&gt;</code> - Response if matched, undefined if no agent route.</p>
<h3 id="getagentbyname-namespace-name-options"><code>getAgentByName(namespace, name, options?)</code></h3>
<p>Get an agent instance by name for server-side RPC or request forwarding.</p>
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
<td><code>namespace</code></td>
<td><code>DurableObjectNamespace&lt;T&gt;</code></td>
<td>Agent binding from env</td>
</tr>
<tr>
<td><code>name</code></td>
<td><code>string</code></td>
<td>Instance name</td>
</tr>
<tr>
<td><code>options.locationHint</code></td>
<td><code>string</code></td>
<td>Preferred location</td>
</tr>
<tr>
<td><code>options.jurisdiction</code></td>
<td><code>string</code></td>
<td>Data jurisdiction</td>
</tr>
<tr>
<td><code>options.props</code></td>
<td><code>Record&lt;string, unknown&gt;</code></td>
<td>Initialization properties for onStart</td>
</tr>
<tr>
<td><code>options.routingRetry</code></td>
<td><code>object</code></td>
<td>Retry configuration for transient Durable Object routing failures</td>
</tr>
</tbody>
</table>
<p><strong>Returns:</strong> <code>Promise&lt;DurableObjectStub&lt;T&gt;&gt;</code> - Typed stub for calling agent methods or forwarding requests.</p>
<h3 id="useagent-options-agentclient-options"><code>useAgent(options)</code> / <code>AgentClient</code> options</h3>
<p>Client connection options for custom routing:</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agent</code></td>
<td><code>string</code></td>
<td>Agent class name (required)</td>
</tr>
<tr>
<td><code>name</code></td>
<td><code>string</code></td>
<td>Instance name (default: <code>&quot;default&quot;</code>)</td>
</tr>
<tr>
<td><code>basePath</code></td>
<td><code>string</code></td>
<td>Full URL path - bypasses agent/name URL construction</td>
</tr>
<tr>
<td><code>path</code></td>
<td><code>string</code></td>
<td>Additional path to append to the URL</td>
</tr>
<tr>
<td><code>onIdentity</code></td>
<td><code>(name, agent) =&gt; void</code></td>
<td>Called when server sends identity</td>
</tr>
<tr>
<td><code>onIdentityChange</code></td>
<td><code>(oldName, newName, oldAgent, newAgent) =&gt; void</code></td>
<td>Called when identity changes on reconnect</td>
</tr>
</tbody>
</table>
<p><strong>Return value properties (React hook):</strong></p>
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
<td><code>name</code></td>
<td><code>string</code></td>
<td>Current instance name (reactive)</td>
</tr>
<tr>
<td><code>agent</code></td>
<td><code>string</code></td>
<td>Current agent class name (reactive)</td>
</tr>
<tr>
<td><code>identified</code></td>
<td><code>boolean</code></td>
<td>Whether identity has been received (reactive)</td>
</tr>
<tr>
<td><code>ready</code></td>
<td><code>Promise&lt;void&gt;</code></td>
<td>Resolves when identity is received</td>
</tr>
</tbody>
</table>
<h3 id="agent-options-server"><code>Agent.options</code> (server)</h3>
<p>Static options for agent configuration:</p>
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
<td>Whether the agent should hibernate when inactive</td>
</tr>
<tr>
<td><code>sendIdentityOnConnect</code></td>
<td><code>boolean</code></td>
<td><code>true</code></td>
<td>Whether to send identity to clients on connect</td>
</tr>
<tr>
<td><code>hungScheduleTimeoutSeconds</code></td>
<td><code>number</code></td>
<td><code>30</code></td>
<td>Timeout before a running schedule is considered hung</td>
</tr>
</tbody>
</table>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2610.md")
</div>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-client-sdk-agents-communication-channels-chat-client-sdk"><a href="/agents/communication-channels/chat/client-sdk/">Client SDK</a></h3><p>Connect from browsers with useAgent and AgentClient.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-cross-domain-authentication-agents-runtime-operations-cross-domain-authentication"><a href="/agents/runtime/operations/cross-domain-authentication/">Cross-domain authentication</a></h3><p>WebSocket authentication patterns.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-callable-methods-agents-runtime-lifecycle-callable-methods"><a href="/agents/runtime/lifecycle/callable-methods/">Callable methods</a></h3><p>RPC from clients over WebSocket.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-configuration-agents-runtime-operations-configuration"><a href="/agents/runtime/operations/configuration/">Configuration</a></h3><p>Set up agent bindings in wrangler.jsonc.</p></div>
