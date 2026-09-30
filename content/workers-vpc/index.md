<div class="nb-description">
@markup("md", "content/.markup/bodies/47.md")
</div>
<div class="nb-plan">
<p>Available on Free and Paid plans</p>
</div>
<p>Workers VPC allows you to connect your Workers to your private APIs, services, and databases in external clouds (AWS, Azure, GCP, on-premise, and others) that are not accessible from the public Internet.</p>
<p><strong><a href="/workers-vpc/configuration/vpc-services/">VPC Services</a></strong> let you bind to a specific host and port in your private network. Connect a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> to your infrastructure, register each target as a VPC Service, and use the <a href="/workers-vpc/api/">binding API</a> from your Worker. VPC Services support HTTP and TCP (TCP databases through <a href="/hyperdrive/">Hyperdrive</a>).</p>
<p><strong><a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a></strong> give Workers broader access — bind to an entire <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>, <a href="/mesh/">Cloudflare Mesh</a> network, or <a href="/cloudflare-wan/">Cloudflare WAN</a> on-ramp (GRE, IPsec, CNI) without pre-registering individual hosts. The URL or address you pass at runtime determines the destination. VPC Networks support HTTP via <code>fetch()</code> and raw TCP via <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code></a> for non-HTTP services like Redis, MQTT, and custom protocols. The same binding can also egress to public Internet destinations through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>, with your Zero Trust policies and logs applied.</p>
<div class="nb-interactive-component" data-cf-component="WorkersVPCOverviewDiagram"></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/46.md")
</aside>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/50.md")
</div></div>
<h2 id="use-cases">Use cases</h2>
<h3 id="access-private-apis-from-workers-applications">Access private APIs from Workers applications</h3>
<p>Deploy APIs or full-stack applications to Workers that connect to private authentication services, CMS systems, internals APIs, and more. Your Workers applications run globally with optimized access to the backend services of your private network.</p>
<h3 id="api-gateway">API gateway</h3>
<p>Route requests to internal microservices in your private network based on URL paths. Centralize access control and load balancing for multiple private services on Workers.</p>
<h3 id="internal-tooling-agents-dashboards">Internal tooling, agents, dashboards</h3>
<p>Build employee-facing applications and MCP servers that aggregate data from multiple private services. Create unified dashboards, admin panels, and internal tools without exposing backend systems.</p>
<h3 id="apply-zero-trust-controls-to-worker-egress">Apply Zero Trust controls to Worker egress</h3>
<p>Route public Internet traffic from your Workers through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> so existing DNS, HTTP, Network, and egress policies — and the corresponding logs — apply to programmatic compute the same way they apply to your workforce. Stop a Worker from reaching unwanted destinations without writing custom proxy logic.</p>
<h2 id="get-started">Get started</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/55.md")
</div>
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/56.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/57.md")
</div>
