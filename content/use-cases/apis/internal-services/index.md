<p>Internal services and microservices often need to communicate without exposing endpoints to the public Internet. Cloudflare Tunnel creates outbound-only connections with no inbound firewall rules, while Access enforces Zero Trust policies for every request between services.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="cloudflare-tunnel">Cloudflare Tunnel</h3>
<p>Connect infrastructure to Cloudflare without opening inbound firewall ports. <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Learn more about Cloudflare Tunnel</a>.</p>
<ul>
<li><strong>No public exposure</strong> - Internal Application Programming Interfaces (APIs) remain private; Tunnel establishes an outbound-only connection with no inbound firewall rules needed</li>
</ul>
<h3 id="access">Access</h3>
<p>Zero Trust access control for applications and infrastructure. <a href="/cloudflare-one/access-controls/policies/">Learn more about Access</a>.</p>
<ul>
<li><strong>Zero Trust policies</strong> - Verify identity and enforce per-service policies for every request between services</li>
<li><strong>Centralized policy management</strong> - Manage access rules for all internal services from a single control plane</li>
</ul>
<h3 id="service-tokens">Service Tokens</h3>
<p>Non-interactive credentials for machine-to-machine authentication. <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Learn more about Service Tokens</a>.</p>
<ul>
<li><strong>Service-to-service auth</strong> - Authenticate internal services with non-interactive credentials managed in Cloudflare One</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/">Create a Cloudflare Tunnel</a></li>
<li><a href="/cloudflare-one/access-controls/policies/">Cloudflare Access get started</a></li>
<li><a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Create service tokens</a></li>
</ol>
