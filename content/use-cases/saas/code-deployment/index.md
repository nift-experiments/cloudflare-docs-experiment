<p>SaaS platforms often need to let customers run their own code — custom logic, integrations, webhooks — without compromising tenant isolation or platform stability. Cloudflare Workers for Platforms runs each customer's code in a separate V8 isolate with dispatch routing based on hostname, path, or header.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="workers-for-platforms">Workers for Platforms</h3>
<p>Deploy isolated Workers execution environments for your customers. <a href="/cloudflare-for-platforms/workers-for-platforms/">Learn more about Workers for Platforms</a>.</p>
<ul>
<li><strong>Tenant isolation</strong> - Each customer's code runs in a separate V8 isolate with no shared memory between tenants</li>
<li><strong>Custom logic</strong> - Customers can deploy their own Workers to extend or customize your platform's behavior</li>
<li><strong>Dispatch routing</strong> - Route incoming requests to the correct customer Worker based on hostname, path, or header</li>
<li><strong>Observability</strong> - Tail Workers capture logs and errors across all tenant code from a single integration</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/get-started/">Workers for Platforms get started</a></li>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">Configure Dispatch Namespaces</a></li>
</ol>
