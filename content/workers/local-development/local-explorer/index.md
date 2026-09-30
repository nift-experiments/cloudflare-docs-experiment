---
cp9:
  canonical: https://developers.cloudflare.com/workers/local-development/local-explorer/
  description: Browse and edit local binding data from your browser during development.
  full_title: Local Explorer · Cloudflare Workers docs
  head_html: <title>Local Explorer · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Browse and edit local binding data from your browser during development."><link rel="canonical" href="https://developers.cloudflare.com/workers/local-development/local-explorer/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/local-development/local-explorer/index.md"><meta property="og:title" content="Local Explorer · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Browse and edit local binding data from your browser during development."><meta property="og:url" content="https://developers.cloudflare.com/workers/local-development/local-explorer/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/local-development/local-explorer/#page","headline":"Local Explorer \u00b7 Cloudflare Workers docs","description":"Browse and edit local binding data from your browser during development.","url":"https://developers.cloudflare.com/workers/local-development/local-explorer/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/local-development/local-explorer/
  schema: 1
---
<p>Local Explorer is a browser-based interface for viewing and editing the data in your local <a href="/workers/runtime-apis/bindings/">bindings</a> and debugging Worker invocations during development. It is available at <code>/cdn-cgi/local/explorer</code> on your local development server.</p>
<p>Instead of running CLI commands or writing throwaway code to inspect local state, you can open Local Explorer in your browser to work with your data, view traces, and search logs. This is useful when you want to seed test data, verify what your Worker wrote, debug a failing request, or run SQL queries against a local <a href="/d1/">D1</a> database.</p>
<p>Local Explorer works with both <a href="/workers/wrangler/">Wrangler</a> and the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Wrangler 4.118.0 or later, or <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> 1.50.0 or later</li>
</ul>
<h2 id="open-local-explorer">Open Local Explorer</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16267.md")
</div>
<p>Local Explorer is available by default and detects the bindings defined in your <a href="/workers/wrangler/configuration/">Wrangler configuration</a> automatically.</p>
<h2 id="supported-bindings">Supported bindings</h2>
<p>Local Explorer supports the following binding types:</p>
<table>
<thead>
<tr>
<th>Binding</th>
<th>View</th>
<th>Edit</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/kv/">KV</a></td>
<td>Browse keys, view values and metadata</td>
<td>Create, update, and delete key-value pairs</td>
</tr>
<tr>
<td><a href="/r2/">R2</a></td>
<td>List objects, view metadata</td>
<td>Upload and delete objects</td>
</tr>
<tr>
<td><a href="/d1/">D1</a></td>
<td>Browse tables and rows, run SQL queries</td>
<td>Insert, update, and delete rows through SQL</td>
</tr>
<tr>
<td><a href="/durable-objects/">Durable Objects</a> (SQLite storage)</td>
<td>Browse SQLite tables and rows, run SQL queries</td>
<td>Insert, update, and delete rows through SQL</td>
</tr>
<tr>
<td><a href="/workflows/">Workflows</a></td>
<td>List instances, view status and step history</td>
<td>Trigger new runs, retry failed instances</td>
</tr>
</tbody>
</table>
<h3 id="d1-and-durable-objects-sql-studio">D1 and Durable Objects SQL Studio</h3>
<p>For <a href="/d1/">D1</a> databases and <a href="/durable-objects/">Durable Objects</a> that use the <a href="/durable-objects/api/sqlite-storage-api/">SQLite storage API</a>, Local Explorer includes a SQL Studio. This is the same experience available in the Cloudflare dashboard for deployed D1 databases. It provides both a visual table browser with inline editing and a SQL query editor where you can run arbitrary queries.</p>
<h2 id="observability">Observability</h2>
<p>Local Explorer automatically captures traces and logs from every Worker invocation during <code>wrangler dev</code> without modifying your code. You get the same instrumentation as production <a href="/workers/observability/logs/workers-logs/">Workers Logs</a> and <a href="/workers/observability/traces/">Traces</a>, including invocation logs, binding operations, timing, and console output, directly in your browser during development.</p>
<h3 id="logs">Logs</h3>
<p>The <strong>Logs</strong> view captures all <code>console.*</code> output from your Worker. Filter by level (error, warn, info, log, debug) or search by text to find specific messages.</p>
<h3 id="traces">Traces</h3>
<p>Each Worker invocation appears as a trace. Select any trace to see every binding operation with timing, status, and error details.</p>
<p>Tracing also captures operations made through <a href="/workers/local-development/#remote-bindings">remote bindings</a>, so you can inspect calls from your locally running Worker to deployed resources.</p>
<p>For example, if a request makes two D1 calls and the second one fails, the trace shows you exactly which call succeeded and which errored without adding <code>console.log()</code> or try/catch blocks.</p>
<p><img src="/assets/upstream/images/workers/observability/local-trace-failed-request.png" alt="Trace view for POST /api/todos showing two D1 database spans: the first INSERT succeeded, the second failed with error &quot;no such table: audit_log&quot;" /></p>
<h2 id="api">API</h2>
<p>Local Explorer exposes an API at <code>/cdn-cgi/local/explorer/api</code> that provides programmatic access to the same operations available in the browser interface. The API serves an <a href="https://www.openapis.org/">OpenAPI specification</a> that describes all available endpoints, parameters, and response formats.</p>
<p>To retrieve the OpenAPI spec:</p>
<pre tabindex="0"><code class="language-sh">curl http://localhost:8787/cdn-cgi/local/explorer/api&#10;</code></pre>
<h3 id="use-with-ai-agents">Use with AI agents</h3>
<p>When Wrangler or the Cloudflare Vite plugin detects it is running inside an AI agent, it prints a hint with the Local Explorer API endpoint directly to the terminal. The agent can fetch the <a href="https://www.openapis.org/">OpenAPI specification</a> from that endpoint to discover all available operations, then make API calls to read or modify local data, query traces and logs, and debug your Worker.</p>
<p>The hint includes the API URL and relevant endpoints:</p>
<pre tabindex="0"><code class="language-txt">This dev session is running in an AI agent.&#10;&#10;The Local Explorer API is available at&#10;http://localhost:8787/cdn-cgi/local/explorer/api&#10;&#10;...&#10;&#10;Debug with traces:&#10;POST /cdn-cgi/local/explorer/api/local/observability/query -- query traces and logs with SQL&#10;</code></pre>
<p>This can be useful as an alternative to the CLI when you want an agent to:</p>
<ul>
<li>Populate test data in your local <a href="/kv/">KV</a> namespaces or <a href="/d1/">D1</a> databases</li>
<li>Inspect the state of a <a href="/durable-objects/">Durable Object</a> during debugging</li>
<li>Trigger or retry a <a href="/workflows/">Workflow</a> run with different input data</li>
<li>Upload test files to a local <a href="/r2/">R2</a> bucket</li>
<li>Find recent requests with errors and drill into failing spans</li>
</ul>
