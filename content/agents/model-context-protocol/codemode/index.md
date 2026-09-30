---
cp9:
  canonical: https://developers.cloudflare.com/agents/model-context-protocol/codemode/
  description: Understand single-code-tool and search-and-execute patterns for exposing tools and large APIs through MCP.
  full_title: Code Mode MCP server patterns · Cloudflare Agents docs
  head_html: <title>Code Mode MCP server patterns · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand single-code-tool and search-and-execute patterns for exposing tools and large APIs through MCP."><link rel="canonical" href="https://developers.cloudflare.com/agents/model-context-protocol/codemode/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/model-context-protocol/codemode/index.md"><meta property="og:title" content="Code Mode MCP server patterns · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand single-code-tool and search-and-execute patterns for exposing tools and large APIs through MCP."><meta property="og:url" content="https://developers.cloudflare.com/agents/model-context-protocol/codemode/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="AI,MCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/model-context-protocol/codemode/#page","headline":"Code Mode MCP server patterns \u00b7 Cloudflare Agents docs","description":"Understand single-code-tool and search-and-execute patterns for exposing tools and large APIs through MCP.","url":"https://developers.cloudflare.com/agents/model-context-protocol/codemode/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI","MCP"]}</script>
  markdown: true
  noindex: false
  route: /agents/model-context-protocol/codemode/
  schema: 1
---
<p>A Code Mode MCP server lets any Model Context Protocol (MCP) client use model-written code without providing its own sandbox. The MCP server exposes code execution as its tool interface and runs generated JavaScript in an isolated Worker.</p>
<p>Code Mode MCP servers follow two patterns:</p>
<table>
<thead>
<tr>
<th>Pattern</th>
<th>MCP tools</th>
<th>Model-facing API</th>
<th>Use when</th>
</tr>
</thead>
<tbody>
<tr>
<td>Single code tool</td>
<td><code>code</code></td>
<td>Typed methods for every upstream tool</td>
<td>You already have an MCP server with a manageable set of tools.</td>
</tr>
<tr>
<td>Search and execute</td>
<td><code>search</code>, <code>execute</code></td>
<td>OpenAPI document and request function</td>
<td>You have a large API whose complete schema should stay out of context.</td>
</tr>
</tbody>
</table>
<p>Both patterns let generated code compose operations and keep intermediate results outside the model context. They differ in how the model discovers available operations.</p>
<h2 id="single-code-tool">Single code tool</h2>
<p>The single-tool pattern wraps an existing MCP server with <code>codeMcpServer()</code>. Instead of advertising each upstream tool separately, the server advertises one <code>code</code> tool.</p>
<p>The <code>code</code> tool description contains generated TypeScript definitions for every upstream tool. The model writes JavaScript against a <code>codemode</code> namespace:</p>
<pre tabindex="0"><code class="language-js">async () =&gt; {&#10;	const projects = await codemode.list_projects({ status: &quot;active&quot; });&#10;	const tasks = [];&#10;&#10;	for (const project of projects) {&#10;		tasks.push(...(await codemode.list_tasks({ projectId: project.id })));&#10;	}&#10;&#10;	return tasks.filter((task) =&gt; task.status === &quot;blocked&quot;);&#10;};&#10;</code></pre>
<p>The MCP client makes one outer tool call. Inside the sandbox, the code can make dependent upstream calls, filter intermediate data, and return only the final result.</p>
<p>This pattern works well when the generated type declarations fit comfortably in the <code>code</code> tool description. The model receives those declarations when it loads the MCP tool.</p>
<p>To implement this pattern, refer to <a href="/agents/model-context-protocol/guides/build-codemode-mcp-server/">Build a single-tool Code Mode MCP server</a>.</p>
<h2 id="search-and-execute">Search and execute</h2>
<p>A large API can have thousands of operations. Including every operation in one tool description would still consume substantial context. The search-and-execute pattern separates capability discovery from authenticated API calls.</p>
<p>The server exposes two MCP tools:</p>
<ul>
<li><code>search</code> runs generated code against an OpenAPI document. It returns only the operations, parameters, or schemas needed for the task.</li>
<li><code>execute</code> runs generated code with an authenticated request function. It can call the selected operations, compose responses, and return a focused result.</li>
</ul>
<p>The model first calls <code>search</code> with code such as:</p>
<pre tabindex="0"><code class="language-js">async () =&gt; {&#10;	const spec = await codemode.spec();&#10;	return Object.entries(spec.paths)&#10;		.filter(([path]) =&gt; path.includes(&quot;/rulesets&quot;))&#10;		.map(([path, operations]) =&gt; ({&#10;			path,&#10;			methods: Object.keys(operations),&#10;		}));&#10;};&#10;</code></pre>
<p>The complete OpenAPI document remains inside the sandbox. Only the returned subset enters the model context.</p>
<p>After selecting an operation, the model calls <code>execute</code>:</p>
<pre tabindex="0"><code class="language-js">async () =&gt; {&#10;	const response = await codemode.request({&#10;		method: &quot;GET&quot;,&#10;		path: `/zones/${zoneId}/rulesets`,&#10;	});&#10;&#10;	return response.result.map(({ id, name, phase }) =&gt; ({ id, name, phase }));&#10;};&#10;</code></pre>
<p>Authentication stays in the host request callback. The generated code receives a request function, not the credential.</p>
<p>The <a href="/agents/model-context-protocol/cloudflare/servers-for-cloudflare/">Cloudflare API MCP server</a> uses this pattern to expose the Cloudflare API through <code>search</code> and <code>execute</code>. For the design rationale and context savings, refer to <a href="https://blog.cloudflare.com/code-mode-mcp/">Code Mode: give agents an entire API in 1,000 tokens</a>.</p>
<p>To implement this pattern, refer to <a href="/agents/model-context-protocol/guides/build-codemode-openapi-mcp-server/">Build a search and execute MCP server</a>.</p>
<h2 id="sandbox-and-authorization-boundary">Sandbox and authorization boundary</h2>
<p>Model-written code runs in an isolated Worker. Direct outbound network access is blocked by default. Generated code reaches external systems only through upstream MCP tools or a host-provided request callback.</p>
<p>Code execution does not replace authorization. Enforce permissions and any required approval inside upstream tool handlers or the host request callback before applying side effects. Do not expose credentials through tool results or OpenAPI documents.</p>
<h2 id="choose-a-pattern">Choose a pattern</h2>
<p>Use <code>codeMcpServer()</code> when an existing MCP server already defines the operations and schemas the model needs. Use <code>openApiMcpServer()</code> when a large OpenAPI catalog needs progressive discovery and a fixed model-context footprint.</p>
<div class="nb-card-grid">
@input("content/.markup/bodies/1861.md")
</div>
