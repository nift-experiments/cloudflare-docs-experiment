---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/codemode/openapi/
  description: Turn OpenAPI operations into typed Code Mode connector methods while keeping authentication in the host Worker.
  full_title: Use an OpenAPI service with Code Mode · Cloudflare Agents docs
  head_html: <title>Use an OpenAPI service with Code Mode · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Turn OpenAPI operations into typed Code Mode connector methods while keeping authentication in the host Worker."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/codemode/openapi/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/codemode/openapi/index.md"><meta property="og:title" content="Use an OpenAPI service with Code Mode · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Turn OpenAPI operations into typed Code Mode connector methods while keeping authentication in the host Worker."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/codemode/openapi/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/tools/codemode/openapi/#page","headline":"Use an OpenAPI service with Code Mode \u00b7 Cloudflare Agents docs","description":"Turn OpenAPI operations into typed Code Mode connector methods while keeping authentication in the host Worker.","url":"https://developers.cloudflare.com/agents/tools/codemode/openapi/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/codemode/openapi/
  schema: 1
---
<p>Use <code>OpenApiConnector</code> to expose an OpenAPI service inside a durable Code Mode runtime. The connector derives one sandbox method for each operation in the OpenAPI document.</p>
<p>The model can discover methods with <code>codemode.search()</code> and request focused input types with <code>codemode.describe()</code>. The complete OpenAPI document does not need to enter the model context.</p>
<p>This page covers an Agent consuming an OpenAPI service. To publish an OpenAPI service to external MCP clients through <code>search</code> and <code>execute</code>, refer to <a href="/agents/model-context-protocol/guides/build-codemode-openapi-mcp-server/">Build a search and execute MCP server</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need a project with the <a href="/agents/tools/codemode/durable-runtime/">durable Code Mode runtime</a> configured. The runtime setup provides the Worker Loader binding and the <code>CodemodeRuntime</code> export used in this guide.</p>
<h2 id="create-an-openapi-connector">Create an OpenAPI connector</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2666.md")
</div>
<h2 id="derived-method-behavior">Derived method behavior</h2>
<p><code>OpenApiConnector</code> uses a sanitized <code>operationId</code> as the method name. If an operation has no <code>operationId</code>, it derives a name from the HTTP method and path. Define unique operation IDs to keep method names stable and avoid collisions.</p>
<p>Each generated method accepts one object:</p>
<ul>
<li>Path, query, and header parameters appear as top-level fields.</li>
<li>A JSON request body appears under <code>body</code>.</li>
<li>Required OpenAPI parameters become required TypeScript fields.</li>
<li>Local <code>$ref</code> values in input schemas are resolved before types are generated.</li>
</ul>
<p>The connector substitutes path parameters and passes a normalized <code>{ path, method, params, body, headers }</code> object to <code>request()</code>.</p>
<p>The current connector derives input types but does not derive response types from OpenAPI response schemas. Generated methods therefore return <code>unknown</code> unless your application provides more specific declarations through another connector implementation.</p>
<h2 id="request-escape-hatch">Request escape hatch</h2>
<p>Every OpenAPI connector also exposes a low-level <code>request()</code> sandbox method. Use it when the OpenAPI document does not describe an operation the model needs:</p>
<pre tabindex="0"><code class="language-js">const result = await orders.request({&#10;	path: &quot;/orders&quot;,&#10;	method: &quot;GET&quot;,&#10;	params: { status: &quot;processing&quot; },&#10;});&#10;</code></pre>
<p>Prefer derived operation methods when available. They provide discoverable descriptions and generated input types.</p>
<p><code>exposeSpec()</code> returns <code>false</code> by default. Override it to return <code>true</code> only when model-written code needs access to the raw OpenAPI document. Large documents can produce large results and durable log entries.</p>
