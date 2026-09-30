<p>Sandboxes can access <a href="/workers/runtime-apis/bindings/">Workers bindings</a> — KV, R2, D1, Durable Objects, and others — through <a href="/sandbox/guides/outbound-traffic/#define-outbound-handlers">outbound handlers</a>. An outbound handler intercepts HTTP requests from the sandbox and runs inside the Workers runtime, where all of your configured bindings are available.</p>
<p>The sandbox makes a plain HTTP request to a virtual hostname (for example, <code>http://my.kv/some-key</code>), and the outbound handler resolves it using the bound resource. No SDK or client library is required inside the sandbox.</p>
<h2 id="use-bindings-in-outbound-handlers">Use bindings in outbound handlers</h2>
<p>Define an <code>outboundByHost</code> handler for each virtual hostname. The <code>env</code> argument gives you access to every binding declared in your Wrangler configuration.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13344.md")
</div>
<p>The sandbox calls <code>http://my.kv/some-key</code> and the handler resolves it using the KV binding. A call to <code>http://my.r2/file.png</code> reads from R2, scoped to the current sandbox instance.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13343.md")
</aside>
<h2 id="access-durable-object-state">Access Durable Object state</h2>
<p>The <code>ctx</code> argument exposes <code>containerId</code>, which lets you interact with the sandbox's own Durable Object from an outbound handler.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13345.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/guides/outbound-traffic/">Handle outbound traffic</a> — Block, allow, and intercept all outbound HTTP from a sandbox</li>
<li><a href="/sandbox/configuration/sandbox-options/">Sandbox options</a> — Configure sandbox behavior</li>
<li><a href="/sandbox/configuration/environment-variables/">Environment variables</a> — Configure secrets and environment variables</li>
</ul>
