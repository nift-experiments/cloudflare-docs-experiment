---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/communication/readonly-connections/
  description: Restrict WebSocket clients to view-only access so they receive state updates without modifying Agent state.
  full_title: Readonly connections · Cloudflare Agents docs
  head_html: <title>Readonly connections · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Restrict WebSocket clients to view-only access so they receive state updates without modifying Agent state."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/communication/readonly-connections/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/communication/readonly-connections/index.md"><meta property="og:title" content="Readonly connections · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Restrict WebSocket clients to view-only access so they receive state updates without modifying Agent state."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/communication/readonly-connections/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/communication/readonly-connections/#page","headline":"Readonly connections \u00b7 Cloudflare Agents docs","description":"Restrict WebSocket clients to view-only access so they receive state updates without modifying Agent state.","url":"https://developers.cloudflare.com/agents/runtime/communication/readonly-connections/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/communication/readonly-connections/
  schema: 1
---
<p>Readonly connections restrict certain WebSocket clients from modifying agent state while still letting them receive state updates and call non-mutating RPC methods.</p>
<h2 id="overview">Overview</h2>
<p>When a connection is marked as readonly:</p>
<ul>
<li>It <strong>receives</strong> state updates from the server</li>
<li>It <strong>can call</strong> RPC methods that do not modify state</li>
<li>It <strong>cannot</strong> call <code>this.setState()</code> — neither via client-side <code>setState()</code> nor via a <code>@callable()</code> method that calls <code>this.setState()</code> internally</li>
</ul>
<p>This is useful for scenarios like:</p>
<ul>
<li><strong>View-only modes</strong>: Users who should only observe but not modify</li>
<li><strong>Role-based access</strong>: Restricting state modifications based on user roles</li>
<li><strong>Multi-tenant scenarios</strong>: Some tenants have read-only access</li>
<li><strong>Audit and monitoring connections</strong>: Observers that should not affect the system</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2612.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2613.md")
</div>
<h2 id="marking-connections-as-readonly">Marking connections as readonly</h2>
<h3 id="on-connect">On connect</h3>
<p>Override <code>shouldConnectionBeReadonly</code> to evaluate each connection when it first connects. Return <code>true</code> to mark it readonly.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2614.md")
</div>
<p>This hook runs before the initial state is sent to the client, so the connection is readonly from the very first message.</p>
<h3 id="at-any-time">At any time</h3>
<p>Use <code>setConnectionReadonly</code> to change a connection's readonly status dynamically:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2615.md")
</div>
<h3 id="letting-a-connection-toggle-its-own-status">Letting a connection toggle its own status</h3>
<p>A connection can toggle its own readonly status via a callable. This is useful for lock/unlock UIs where viewers can opt into editing mode:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2616.md")
</div>
<p>On the client:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2617.md")
</div>
<h3 id="checking-status">Checking status</h3>
<p>Use <code>isConnectionReadonly</code> to check a connection's current status:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2618.md")
</div>
<h2 id="handling-errors-on-the-client">Handling errors on the client</h2>
<p>Errors surface in two ways depending on how the write was attempted:</p>
<ul>
<li><strong>Client-side <code>setState()</code></strong> — the server sends a <code>cf_agent_state_error</code> message. Handle it with the <code>onStateUpdateError</code> callback.</li>
<li><strong><code>@callable()</code> methods</strong> — the RPC call rejects with an error. Handle it with a <code>try</code>/<code>catch</code> around <code>agent.call()</code>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2611.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2619.md")
</div>
<p>To avoid showing errors in the first place, check permissions before rendering edit controls:</p>
<pre tabindex="0"><code class="language-tsx">function Editor() {&#10;	const [canEdit, setCanEdit] = useState(false);&#10;	const agent = useAgent({ agent: &quot;MyAgent&quot;, name: &quot;instance&quot; });&#10;&#10;	useEffect(() =&gt; {&#10;		agent.call(&quot;getPermissions&quot;).then((p) =&gt; setCanEdit(p.canEdit));&#10;	}, []);&#10;&#10;	return &lt;button disabled={!canEdit}&gt;{canEdit ? &quot;Edit&quot; : &quot;View Only&quot;}&lt;/button&gt;;&#10;}&#10;</code></pre>
<h2 id="api-reference">API reference</h2>
<h3 id="shouldconnectionbereadonly"><code>shouldConnectionBeReadonly</code></h3>
<p>An overridable hook that determines if a connection should be marked as readonly when it connects.</p>
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
<td><code>connection</code></td>
<td><code>Connection</code></td>
<td>The connecting client</td>
</tr>
<tr>
<td><code>ctx</code></td>
<td><code>ConnectionContext</code></td>
<td>Contains the upgrade request</td>
</tr>
<tr>
<td><strong>Returns</strong></td>
<td><code>boolean</code></td>
<td><code>true</code> to mark as readonly</td>
</tr>
</tbody>
</table>
<p>Default: returns <code>false</code> (all connections are writable).</p>
<h3 id="setconnectionreadonly"><code>setConnectionReadonly</code></h3>
<p>Mark or unmark a connection as readonly. Can be called at any time.</p>
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
<td><code>connection</code></td>
<td><code>Connection</code></td>
<td>The connection to update</td>
</tr>
<tr>
<td><code>readonly</code></td>
<td><code>boolean</code></td>
<td><code>true</code> to make readonly (default: <code>true</code>)</td>
</tr>
</tbody>
</table>
<h3 id="isconnectionreadonly"><code>isConnectionReadonly</code></h3>
<p>Check if a connection is currently readonly.</p>
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
<td><code>connection</code></td>
<td><code>Connection</code></td>
<td>The connection to check</td>
</tr>
<tr>
<td><strong>Returns</strong></td>
<td><code>boolean</code></td>
<td><code>true</code> if readonly</td>
</tr>
</tbody>
</table>
<h3 id="onstateupdateerror-client"><code>onStateUpdateError</code> (client)</h3>
<p>Callback on <code>AgentClient</code> and <code>useAgent</code> options. Called when the server rejects a state update.</p>
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
<td><code>error</code></td>
<td><code>string</code></td>
<td>Error message from the server</td>
</tr>
</tbody>
</table>
<h2 id="examples">Examples</h2>
<h3 id="query-parameter-based-access">Query parameter based access</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2620.md")
</div>
<h3 id="role-based-access-control">Role-based access control</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2621.md")
</div>
<h3 id="admin-dashboard">Admin dashboard</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2622.md")
</div>
<h3 id="dynamic-permission-changes">Dynamic permission changes</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2623.md")
</div>
<p>Client-side React component:</p>
<pre tabindex="0"><code class="language-tsx">function GameComponent() {&#10;	const [canEdit, setCanEdit] = useState(false);&#10;&#10;	const agent = useAgent({&#10;		agent: &quot;GameAgent&quot;,&#10;		name: &quot;game-123&quot;,&#10;		onStateUpdateError: (error) =&gt; {&#10;			toast.error(&quot;Cannot modify game state in spectator mode&quot;);&#10;		},&#10;	});&#10;&#10;	useEffect(() =&gt; {&#10;		agent.call(&quot;getMyPermissions&quot;).then((perms) =&gt; {&#10;			setCanEdit(perms?.canEdit ?? false);&#10;		});&#10;	}, [agent]);&#10;&#10;	return (&#10;		&lt;div&gt;&#10;			&lt;button onClick={() =&gt; agent.call(&quot;joinAsPlayer&quot;)} disabled={canEdit}&gt;&#10;				Join as Player&#10;			&lt;/button&gt;&#10;&#10;			&lt;button&#10;				onClick={() =&gt; agent.call(&quot;startSpectatorMode&quot;)}&#10;				disabled={!canEdit}&#10;			&gt;&#10;				Switch to Spectator&#10;			&lt;/button&gt;&#10;&#10;			&lt;div&gt;{canEdit ? &quot;You can modify the game&quot; : &quot;You are spectating&quot;}&lt;/div&gt;&#10;		&lt;/div&gt;&#10;	);&#10;}&#10;</code></pre>
<h2 id="how-it-works">How it works</h2>
<p>Readonly status is stored in the connection's WebSocket attachment, which persists through the WebSocket Hibernation API. The flag is namespaced internally so it cannot be accidentally overwritten by <code>connection.setState()</code>. The same mechanism is used by <a href="/agents/runtime/communication/protocol-messages/">protocol message control</a> — both flag coexist safely in the attachment. This means:</p>
<ul>
<li><strong>Survives hibernation</strong> — the flag is serialized and restored when the agent wakes up</li>
<li><strong>No cleanup needed</strong> — connection state is automatically discarded when the connection closes</li>
<li><strong>Zero overhead</strong> — no database tables or queries, just the connection's built-in attachment</li>
<li><strong>Safe from user code</strong> — <code>connection.state</code> and <code>connection.setState()</code> never expose or overwrite the readonly flag</li>
</ul>
<p>When a readonly connection tries to modify state, the server blocks it — regardless of whether the write comes from client-side <code>setState()</code> or from a <code>@callable()</code> method:</p>
<pre tabindex="0"><code>Client (readonly)                     Agent&#10;       │                                │&#10;       │  setState({ count: 1 })        │&#10;       │ ─────────────────────────────▶ │  Check readonly → blocked&#10;       │  ◀───────────────────────────  │&#10;       │  cf_agent_state_error          │&#10;       │                                │&#10;       │  call(&quot;increment&quot;)             │&#10;       │ ─────────────────────────────▶ │  increment() calls this.setState()&#10;       │                                │  Check readonly → throw&#10;       │  ◀───────────────────────────  │&#10;       │  RPC error: &quot;Connection is     │&#10;       │              readonly&quot;         │&#10;       │                                │&#10;       │  call(&quot;getPermissions&quot;)        │&#10;       │ ─────────────────────────────▶ │  getPermissions() — no setState()&#10;       │  ◀───────────────────────────  │&#10;       │  RPC result: { canEdit: false }│&#10;</code></pre>
<h3 id="what-readonly-does-and-does-not-restrict">What readonly does and does not restrict</h3>
<table>
<thead>
<tr>
<th>Action</th>
<th>Allowed?</th>
</tr>
</thead>
<tbody>
<tr>
<td>Receive state broadcasts</td>
<td>Yes</td>
</tr>
<tr>
<td>Call <code>@callable()</code> methods that do not write state</td>
<td>Yes</td>
</tr>
<tr>
<td>Call <code>@callable()</code> methods that call <code>this.setState()</code></td>
<td><strong>No</strong></td>
</tr>
<tr>
<td>Send state updates via client-side <code>setState()</code></td>
<td><strong>No</strong></td>
</tr>
</tbody>
</table>
<p>The enforcement happens inside <code>setState()</code> itself. When a <code>@callable()</code> method tries to call <code>this.setState()</code> and the current connection context is readonly, the framework throws an <code>Error(&quot;Connection is readonly&quot;)</code>. This means you do not need manual permission checks in your RPC methods — any callable that writes state is automatically blocked for readonly connections.</p>
<h2 id="caveats">Caveats</h2>
<h3 id="side-effects-in-callables-still-run">Side effects in callables still run</h3>
<p>The readonly check happens inside <code>this.setState()</code>, not at the start of the callable. If your method has side effects before the state write, those will still execute:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2624.md")
</div>
<p>To avoid this, either check permissions before side effects or structure your code so the state write comes first:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2625.md")
</div>
<h2 id="best-practices">Best practices</h2>
<h3 id="combine-with-authentication">Combine with authentication</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2626.md")
</div>
<h3 id="provide-clear-user-feedback">Provide clear user feedback</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2627.md")
</div>
<h3 id="check-permissions-before-ui-actions">Check permissions before UI actions</h3>
<pre tabindex="0"><code class="language-tsx">function EditButton() {&#10;	const [canEdit, setCanEdit] = useState(false);&#10;	const agent = useAgent({&#10;		/* ... */&#10;	});&#10;&#10;	useEffect(() =&gt; {&#10;		agent.call(&quot;checkPermissions&quot;).then((perms) =&gt; {&#10;			setCanEdit(perms.canEdit);&#10;		});&#10;	}, []);&#10;&#10;	return &lt;button disabled={!canEdit}&gt;{canEdit ? &quot;Edit&quot; : &quot;View Only&quot;}&lt;/button&gt;;&#10;}&#10;</code></pre>
<h3 id="log-access-attempts">Log access attempts</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2628.md")
</div>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Readonly status only applies to state updates using <code>setState()</code></li>
<li>RPC methods can still be called (implement your own checks if needed)</li>
<li>Readonly is a per-connection flag, not tied to user identity</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/agents/runtime/lifecycle/state/">Store and sync state</a></li>
<li><a href="/agents/runtime/communication/protocol-messages/">Protocol messages</a> — suppress JSON protocol frames for binary-only clients (can be combined with readonly)</li>
<li><a href="/agents/runtime/communication/websockets/">WebSockets</a></li>
<li><a href="/agents/runtime/lifecycle/callable-methods/">Callable methods</a></li>
</ul>
