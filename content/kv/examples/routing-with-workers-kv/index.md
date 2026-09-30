<p class="article-summary">Store routing data in Workers KV to route requests across various web servers with Workers</p>
<p>Using Workers KV to store routing data to route requests across various web servers with Workers is an ideal use case for Workers KV. Routing workloads can have high read volume, and Workers KV's low-latency reads can help ensure that routing decisions are made quickly and efficiently.</p>
<p>Routing can be helpful to route requests coming into a single Cloudflare Worker application to different web servers based on the request's path, hostname, or other request attributes.</p>
<p>In single-tenant applications, this can be used to route requests to various origin servers based on the business domain (for example, requests to <code>/admin</code> routed to administration server, <code>/store</code> routed to storefront server, <code>/api</code> routed to the API server).</p>
<p>In multi-tenant applications, requests can be routed to the tenant's respective origin resources (for example, requests to <code>tenantA.your-worker-hostname.com</code> routed to server for Tenant A, <code>tenantB.your-worker-hostname.com</code> routed to server for Tenant B).</p>
<p>Routing can also be used to implement <a href="/reference-architecture/diagrams/serverless/a-b-testing-using-workers/">A/B testing</a>, canary deployments, or <a href="https://en.wikipedia.org/wiki/Blue%E2%80%93green_deployment">blue-green deployments</a> for your own external applications.
If you are looking to implement canary or blue-green deployments of applications built fully on Cloudflare Workers, see <a href="/workers/versions-and-deployments/gradual-deployments/">Workers gradual deployments</a>.</p>
<h2 id="route-requests-with-workers-kv">Route requests with Workers KV</h2>
<p>In this example, a multi-tenant e-Commerce application is built on Cloudflare Workers. Each storefront is a different tenant and has its own external web server.
Our Cloudflare Worker is responsible for receiving all requests for all storefronts and routing requests to the correct origin web server according to the storefront ID.</p>
<p>For simplicity of demonstration, the storefront will be identified with a path element containing the storefront ID, where
<code>https://&lt;WORKER_HOSTNAME&gt;/&lt;STOREFRONT_ID&gt;/...</code> is the URL pattern for the storefront. You may prefer to use subdomains to identify storefronts in a real-world scenario.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9510.md")
</div></div>
<p>In this example, the Cloudflare Worker receives a request and extracts the storefront ID from the URL path.
The storefront ID is used to look up the origin server URL from Workers KV using the <code>get()</code> method.
The request is then forwarded to the origin server, and the response is modified to include custom headers before being returned to the client.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/languages/rust/">Rust support in Workers</a>.</li>
<li><a href="/kv/get-started/">Using KV in Workers</a>.</li>
</ul>
