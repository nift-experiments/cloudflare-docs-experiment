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
<pre><code class="language-js">const result = await orders.request({&#10;	path: &quot;/orders&quot;,&#10;	method: &quot;GET&quot;,&#10;	params: { status: &quot;processing&quot; },&#10;});&#10;</code></pre>
<p>Prefer derived operation methods when available. They provide discoverable descriptions and generated input types.</p>
<p><code>exposeSpec()</code> returns <code>false</code> by default. Override it to return <code>true</code> only when model-written code needs access to the raw OpenAPI document. Large documents can produce large results and durable log entries.</p>
