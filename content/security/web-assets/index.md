<p>Web Assets automatically discovers operations in web applications proxied through Cloudflare. Operation context helps you define security protections against application-specific functionalities.</p>
<p>For example, discovering operations that receive LLM prompts so <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a> can help you define targeted protections such as deterring prompt injections.</p>
<p>To access Web Assets in the Cloudflare dashboard, go to the <strong>Web Assets</strong> page.</p>
<div class="nb-dash-button"></div>
<h2 id="definition-of-an-operation">Definition of an operation</h2>
<p>An operation is a group of HTTP requests that serve the same purpose in your application. Each operation is defined by:</p>
<ul>
<li>HTTP method</li>
<li>Hostname pattern</li>
<li>Path pattern</li>
</ul>
<p>For example, Web Assets can group requests to product detail pages into one operation:</p>
<pre><code class="language-txt">GET example.com/products/{var1}&#10;</code></pre>
<p>The operation can match requests such as:</p>
<pre><code class="language-txt">GET https://example.com/products/shoes&#10;GET https://example.com/products/hats&#10;GET https://example.com/products/jackets&#10;</code></pre>
<p>This lets Cloudflare identify requests that serve the same purpose in your application.</p>
<h2 id="how-cloudflare-identifies-operations">How Cloudflare identifies operations</h2>
<p>Operations can come from several sources:</p>
<ul>
<li><strong>Discovery</strong>: Web Assets continuously reviews proxied HTTP traffic and groups similar requests into operations using machine learning (for <a href="/api-shield/security/api-discovery/">API discovery</a>) and heuristics.</li>
<li><strong>Manual entry</strong>: You can add operations by method, hostname pattern, and path pattern.</li>
<li><strong>Schema upload</strong>: You can <a href="/api-shield/management-and-monitoring/endpoint-management/#add-endpoints-from-schema-validation">upload an OpenAPI schema</a> to create operations from an existing API definition.</li>
</ul>
<p>These sources contribute to the same operation inventory. You do not need to review every discovered operation before security detections can use operation context.</p>
<h2 id="operation-states-and-profile-learning">Operation states and profile learning</h2>
<p>Operations can be in the <code>candidate</code>, <code>shadow</code>, or <code>full</code> state. These states control operation matching and available features.</p>
<p>An operation state alone does not start profile learning. To learn a Schema Profile, select <strong>Learn profile</strong> from the operation overflow menu.</p>
<p>For the profile lifecycle, refer to <a href="/waf/detections/application-profiles/">Application Profiles</a>. For uploaded OpenAPI schemas, refer to <a href="/api-shield/security/schema-validation/">Schema Validation</a>.</p>
<h2 id="describe-operations-context">Describe operations context</h2>
<p><a href="/security/web-assets/label-operations/">Labels</a> describe what an operation does, such as a login flow, sign-up flow, AI-powered operation, or another use case.</p>
<p>Cloudflare defines managed labels. Some managed labels can be discovered automatically, but not every managed label is currently auto-discovered.</p>
<p>Custom labels let you organize operations for your own workflows. They do not replace managed labels for Cloudflare security detections.</p>
<h2 id="define-security-protections">Define security protections</h2>
<p>Security detections can use Web Assets to focus on the operations where their signals matter. For example, <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a> uses the <code>cf-llm</code> managed label to scan requests to AI-powered operations. For more information, refer to <a href="/security/web-assets/define-security-protections/">Define security protections</a>.</p>
<div class="nb-card"><h3 class="nb-component-title" id="related-api-shield-features">Related API Shield features</h3>
@markup("md", "content/.markup/bodies/13839.md")
</div>
