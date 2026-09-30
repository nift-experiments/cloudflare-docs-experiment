---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/lifecycle/get-current-agent/
  description: Access the current Agent context from external utility functions using getCurrentAgent() in the Agents SDK.
  full_title: getCurrentAgent() · Cloudflare Agents docs
  head_html: <title>getCurrentAgent() · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Access the current Agent context from external utility functions using getCurrentAgent() in the Agents SDK."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/lifecycle/get-current-agent/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/lifecycle/get-current-agent/index.md"><meta property="og:title" content="getCurrentAgent() · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Access the current Agent context from external utility functions using getCurrentAgent() in the Agents SDK."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/lifecycle/get-current-agent/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/lifecycle/get-current-agent/#page","headline":"getCurrentAgent() \u00b7 Cloudflare Agents docs","description":"Access the current Agent context from external utility functions using getCurrentAgent() in the Agents SDK.","url":"https://developers.cloudflare.com/agents/runtime/lifecycle/get-current-agent/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/lifecycle/get-current-agent/
  schema: 1
---
<p>The <code>getCurrentAgent()</code> function allows you to access the current agent context from anywhere in your code, including external utility functions and libraries. This is useful when you need agent information in functions that do not have direct access to <code>this</code>.</p>
<h2 id="automatic-context-for-custom-methods">Automatic context for custom methods</h2>
<p>The framework detects and wraps custom Agent methods during initialization so <code>getCurrentAgent()</code> can resolve the active agent inside them and the functions they call.</p>
<h2 id="how-it-works">How it works</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2395.md")
</div>
<p>No configuration is required. The framework automatically:</p>
<ol>
<li>Scans your agent class for custom methods.</li>
<li>Wraps them with agent context during initialization.</li>
<li>Ensures <code>getCurrentAgent()</code> works in all external functions called from your methods.</li>
</ol>
<h2 id="real-world-example">Real-world example</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2396.md")
</div>
<h3 id="built-in-vs-custom-methods">Built-in vs custom methods</h3>
<ul>
<li><strong>Built-in methods</strong> (<code>onRequest</code>, <code>onEmail</code>, <code>onStateChanged</code>): Already have context.</li>
<li><strong>Custom methods</strong> (your methods): Automatically wrapped during initialization.</li>
<li><strong>External functions</strong>: Access context through <code>getCurrentAgent()</code>.</li>
</ul>
<h3 id="the-context-flow">The context flow</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2397.md")
</div>
<h2 id="common-use-cases">Common use cases</h2>
<h3 id="working-with-ai-sdk-tools">Working with AI SDK tools</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2398.md")
</div>
<h3 id="calling-external-libraries">Calling external libraries</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2399.md")
</div>
<h3 id="accessing-request-and-connection-context">Accessing request and connection context</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2400.md")
</div>
<h2 id="when-context-is-lost">When context is lost</h2>
<p>The agent context only propagates along the call tree of the original invocation. Code reached outside that call tree starts with an empty context, so <code>getCurrentAgent()</code> returns an object whose fields are <code>undefined</code>. Common cases include:</p>
<ul>
<li>a host callback invoked through RPC from a Worker Loader child isolate, such as sandboxed Codemode execution;</li>
<li>a service binding or Durable Object RPC entrypoint;</li>
<li>a queue consumer or another entrypoint that retains an agent reference.</li>
</ul>
<p>Route the callback through a public method on the agent. Custom methods are wrapped automatically, so calling <code>agent.someMethod()</code> re-enters that agent's context:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2401.md")
</div>
<p>Context restored this way has <code>connection</code>, <code>request</code>, and <code>email</code> unset. It is not tied to live client I/O.</p>
<p>Server-initiated MCP requests (<code>elicitInput</code>, <code>createMessage</code>, and <code>listRoots</code>) on <code>McpAgent</code> do not require this indirection because the MCP transport retains its owning agent.</p>
<h2 id="api-reference">API reference</h2>
<h3 id="getcurrentagent"><code>getCurrentAgent()</code></h3>
<p>Gets the current agent from any context where it is available.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2402.md")
</div>
<h4 id="returns">Returns:</h4>
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
<td><code>agent</code></td>
<td><code>T | undefined</code></td>
<td>The current agent instance</td>
</tr>
<tr>
<td><code>connection</code></td>
<td><code>Connection | undefined</code></td>
<td>The WebSocket connection (if called from a WebSocket handler)</td>
</tr>
<tr>
<td><code>request</code></td>
<td><code>Request | undefined</code></td>
<td>The HTTP request (if called from a request handler)</td>
</tr>
<tr>
<td><code>email</code></td>
<td><code>AgentEmail | undefined</code></td>
<td>The email (if called from an email handler)</td>
</tr>
</tbody>
</table>
<h4 id="usage">Usage:</h4>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2403.md")
</div>
<h3 id="context-availability">Context availability</h3>
<p>The context available depends on how the method was invoked:</p>
<table>
<thead>
<tr>
<th>Invocation</th>
<th><code>agent</code></th>
<th><code>connection</code></th>
<th><code>request</code></th>
<th><code>email</code></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>onRequest()</code></td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td><code>onConnect()</code></td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td><code>onMessage()</code></td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<td><code>onEmail()</code></td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Custom method (via RPC)</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<td>Scheduled task</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<td>Queue callback</td>
<td>Yes</td>
<td>Depends</td>
<td>Depends</td>
<td>Depends</td>
</tr>
</tbody>
</table>
<h2 id="best-practices">Best practices</h2>
<ol>
<li>
<p><strong>Use <code>this</code> when possible</strong>: Inside agent methods, prefer <code>this.name</code>, <code>this.state</code>, etc. over <code>getCurrentAgent()</code>.</p>
</li>
<li>
<p><strong>Use <code>getCurrentAgent()</code> in external functions</strong>: When you need agent context in utility functions or libraries that do not have access to <code>this</code>.</p>
</li>
<li>
<p><strong>Check for undefined</strong>: The returned values may be <code>undefined</code> if called outside an agent context.</p>
</li>
</ol>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2404.md")
</div>
<ol start="4">
<li><strong>Type the agent</strong>: Pass your agent class as a type parameter for proper typing.</li>
</ol>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2405.md")
</div>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-agents-api-agents-runtime-agents-api"><a href="/agents/runtime/agents-api/">Agents API</a></h3><p>Complete API reference for the Agents SDK.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-callable-methods-agents-runtime-lifecycle-callable-methods"><a href="/agents/runtime/lifecycle/callable-methods/">Callable methods</a></h3><p>Expose methods to clients via RPC.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-state-management-agents-runtime-lifecycle-state"><a href="/agents/runtime/lifecycle/state/">State management</a></h3><p>Manage and sync agent state.</p></div>
