---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/lifecycle/callable-methods/
  description: Expose Agent methods to external clients over WebSocket RPC using the @callable() decorator.
  full_title: Callable methods · Cloudflare Agents docs
  head_html: <title>Callable methods · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Expose Agent methods to external clients over WebSocket RPC using the @callable() decorator."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/lifecycle/callable-methods/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/lifecycle/callable-methods/index.md"><meta property="og:title" content="Callable methods · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Expose Agent methods to external clients over WebSocket RPC using the @callable() decorator."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/lifecycle/callable-methods/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/lifecycle/callable-methods/#page","headline":"Callable methods \u00b7 Cloudflare Agents docs","description":"Expose Agent methods to external clients over WebSocket RPC using the @callable() decorator.","url":"https://developers.cloudflare.com/agents/runtime/lifecycle/callable-methods/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/lifecycle/callable-methods/
  schema: 1
---
<p>Callable methods let clients invoke agent methods over WebSocket using RPC (Remote Procedure Call). Mark methods with <code>@callable()</code> to expose them to external clients like browsers, mobile apps, or other services.</p>
<h2 id="overview">Overview</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2409.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2410.md")
</div>
<h3 id="how-it-works">How it works</h3>
<pre tabindex="0"><code class="language-mermaid">sequenceDiagram&#10;    participant Client&#10;    participant Agent&#10;    Client-&gt;&gt;Agent: agent.stub.greet(&quot;World&quot;)&#10;    Note right of Agent: Check @callable&lt;br/&gt;Execute method&#10;    Agent--&gt;&gt;Client: &quot;Hello, World!&quot;&#10;</code></pre>
<h3 id="when-to-use-callable">When to use <code>@callable()</code></h3>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Use</th>
</tr>
</thead>
<tbody>
<tr>
<td>Browser/mobile calling agent</td>
<td><code>@callable()</code></td>
</tr>
<tr>
<td>External service calling agent</td>
<td><code>@callable()</code></td>
</tr>
<tr>
<td>Worker calling agent (same codebase)</td>
<td>Durable Object RPC (no decorator needed)</td>
</tr>
<tr>
<td>Agent calling another agent</td>
<td>Durable Object RPC via <code>getAgentByName()</code></td>
</tr>
</tbody>
</table>
<p>The <code>@callable()</code> decorator is specifically for WebSocket-based RPC from external clients. When calling from within the same Worker or another agent, use standard <a href="/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/">Durable Object RPC</a> directly.</p>
<h2 id="basic-usage">Basic usage</h2>
<h3 id="defining-callable-methods">Defining callable methods</h3>
<p>Add the <code>@callable()</code> decorator to any method you want to expose:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2411.md")
</div>
<h3 id="calling-from-the-client">Calling from the client</h3>
<p>There are two ways to call methods from the client:</p>
<h4 id="using-agent-stub-recommended">Using <code>agent.stub</code> (recommended):</h4>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2412.md")
</div>
<h4 id="using-agent-call">Using <code>agent.call()</code>:</h4>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2413.md")
</div>
<p>The <code>stub</code> proxy provides better ergonomics and TypeScript support.</p>
<h2 id="method-signatures">Method signatures</h2>
<h3 id="serializable-types">Serializable types</h3>
<p>Arguments and return values must be JSON-serializable:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2414.md")
</div>
<h3 id="async-methods">Async methods</h3>
<p>Both sync and async methods work:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2415.md")
</div>
<h3 id="void-methods">Void methods</h3>
<p>Methods that do not return a value:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2416.md")
</div>
<p>On the client, these still return a Promise that resolves when the method completes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2417.md")
</div>
<h2 id="streaming-responses">Streaming responses</h2>
<p>For methods that produce data over time (like AI text generation), use streaming:</p>
<h3 id="defining-a-streaming-method">Defining a streaming method</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2418.md")
</div>
<h3 id="consuming-streams-on-the-client">Consuming streams on the client</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2419.md")
</div>
<h3 id="streamingresponse-api">StreamingResponse API</h3>
<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>send(chunk)</code></td>
<td>Send a chunk to the client</td>
</tr>
<tr>
<td><code>end(finalChunk?)</code></td>
<td>End the stream, optionally with a final value</td>
</tr>
<tr>
<td><code>error(message)</code></td>
<td>Send an error to the client and close the stream</td>
</tr>
</tbody>
</table>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2420.md")
</div>
<h2 id="typescript-integration">TypeScript integration</h2>
<h3 id="typed-client-calls">Typed client calls</h3>
<p>Pass your agent class as a type parameter for full type safety:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2421.md")
</div>
<h3 id="excluding-non-callable-methods">Excluding non-callable methods</h3>
<p>If you have methods that are not decorated with <code>@callable()</code>, you can exclude them from the type:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2422.md")
</div>
<h2 id="error-handling">Error handling</h2>
<h3 id="throwing-errors-in-callable-methods">Throwing errors in callable methods</h3>
<p>Errors thrown in callable methods are propagated to the client:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2423.md")
</div>
<h3 id="client-side-error-handling">Client-side error handling</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2424.md")
</div>
<h3 id="streaming-error-handling">Streaming error handling</h3>
<p>For streaming methods, use the <code>onError</code> callback:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2425.md")
</div>
<p>Server-side, you can use <code>stream.error()</code> to gracefully send an error mid-stream:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2426.md")
</div>
<h3 id="connection-errors">Connection errors</h3>
<p>If the WebSocket connection closes while RPC calls are pending, they automatically reject with a &quot;Connection closed&quot; error:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2427.md")
</div>
<h4 id="retrying-after-reconnection">Retrying after reconnection</h4>
<p>The client automatically reconnects after disconnection. To retry a failed call after reconnection, await <code>agent.ready</code> before retrying:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2428.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2408.md")
</aside>
<h2 id="when-not-to-use-callable">When NOT to use @callable</h2>
<h3 id="worker-to-agent-calls">Worker-to-Agent calls</h3>
<p>When calling an agent from the same Worker (for example, in your <code>fetch</code> handler), use Durable Object RPC directly:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2429.md")
</div>
<h3 id="agent-to-agent-calls">Agent-to-Agent calls</h3>
<p>When one agent needs to call another:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2430.md")
</div>
<h3 id="why-the-distinction">Why the distinction?</h3>
<table>
<thead>
<tr>
<th>RPC Type</th>
<th>Transport</th>
<th>Use Case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@callable</code></td>
<td>WebSocket</td>
<td>External clients (browsers, apps)</td>
</tr>
<tr>
<td>Durable Object RPC</td>
<td>Internal</td>
<td>Worker to Agent, Agent to Agent</td>
</tr>
</tbody>
</table>
<p>Durable Object RPC is more efficient for internal calls since it does not go through WebSocket serialization. The <code>@callable</code> decorator adds the necessary WebSocket RPC handling for external clients.</p>
<h2 id="api-reference">API reference</h2>
<h3 id="callable-metadata-decorator">@callable(metadata?) decorator</h3>
<p>Marks a method as callable from external clients.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2431.md")
</div>
<h3 id="callablemetadata-type">CallableMetadata type</h3>
<pre tabindex="0"><code class="language-ts">type CallableMetadata = {&#10;	/** Optional description of what the method does */&#10;	description?: string;&#10;	/** Whether the method supports streaming responses */&#10;	streaming?: boolean;&#10;};&#10;</code></pre>
<h3 id="streamingresponse-class">StreamingResponse class</h3>
<p>Used in streaming callable methods to send data to the client.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2432.md")
</div>
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
<td><code>send</code></td>
<td><code>(chunk: unknown) =&gt; void</code></td>
<td>Send a chunk to the client</td>
</tr>
<tr>
<td><code>end</code></td>
<td><code>(finalChunk?: unknown) =&gt; void</code></td>
<td>End the stream</td>
</tr>
<tr>
<td><code>error</code></td>
<td><code>(message: string) =&gt; void</code></td>
<td>Send an error and close the stream</td>
</tr>
</tbody>
</table>
<h3 id="client-methods">Client methods</h3>
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
<td><code>agent.call</code></td>
<td><code>(method, args?, options?) =&gt; Promise</code></td>
<td>Call a method by name</td>
</tr>
<tr>
<td><code>agent.stub</code></td>
<td><code>Proxy</code></td>
<td>Typed method calls</td>
</tr>
</tbody>
</table>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2433.md")
</div>
<h3 id="calloptions-type">CallOptions type</h3>
<pre tabindex="0"><code class="language-ts">type CallOptions = {&#10;	/** Timeout in milliseconds. Rejects if call does not complete in time. */&#10;	timeout?: number;&#10;	/** Streaming options */&#10;	stream?: {&#10;		onChunk?: (chunk: unknown) =&gt; void;&#10;		onDone?: (finalChunk: unknown) =&gt; void;&#10;		onError?: (error: string) =&gt; void;&#10;	};&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2407.md")
</aside>
<h3 id="getcallablemethods-method">getCallableMethods() method</h3>
<p>Returns a map of all callable methods on the agent with their metadata. Useful for introspection and automatic documentation.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2434.md")
</div>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="syntaxerror-invalid-or-unexpected-token"><code>SyntaxError: Invalid or unexpected token</code></h3>
<p>If your dev server fails with <code>SyntaxError: Invalid or unexpected token</code> when using <code>@callable()</code>, you need two things:</p>
<p><strong>1. Add the <code>agents/vite</code> plugin</strong> — Vite 8 uses Oxc for transpilation, which does not yet support TC39 decorators. The plugin adds the required transform:</p>
<pre tabindex="0"><code class="language-ts">import agents from &quot;agents/vite&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [agents(), react(), cloudflare()],&#10;});&#10;</code></pre>
<p><strong>2. Extend <code>agents/tsconfig</code></strong> — this sets <code>&quot;target&quot;: &quot;ES2021&quot;</code> and all other recommended compiler options:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;extends&quot;: &quot;agents/tsconfig&quot;&#10;}&#10;</code></pre>
<p>If you cannot extend the shared config, set <code>&quot;target&quot;: &quot;ES2021&quot;</code> manually in your <code>tsconfig.json</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2406.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-agents-api-agents-runtime-agents-api"><a href="/agents/runtime/agents-api/">Agents API</a></h3><p>Complete API reference for the Agents SDK.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-websockets-agents-runtime-communication-websockets"><a href="/agents/runtime/communication/websockets/">WebSockets</a></h3><p>Real-time bidirectional communication with clients.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-state-management-agents-runtime-lifecycle-state"><a href="/agents/runtime/lifecycle/state/">State management</a></h3><p>Sync state between agents and clients.</p></div>
