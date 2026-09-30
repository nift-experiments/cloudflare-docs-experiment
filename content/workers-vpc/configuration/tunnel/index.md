<p>Cloudflare Tunnel creates secure connections from your infrastructure to Cloudflare's global network, providing the network connectivity that allows Workers to access your private resources.</p>
<p>When you create a VPC Service, you specify a tunnel ID and target service. Workers VPC then routes requests from your Worker to the specified tunnel, which establishes a connection to the specified hostname or IP address, such that the target service receives the request and returns a response back to your Worker.</p>
<p>To allow members to create VPC Services that represent a target service reachable via a tunnel, you must assign them the <strong>Connectivity Directory Admin</strong> role. Members with the <strong>Connectivity Directory Bind</strong> role can bind to existing VPC Services from Workers. Binding directly to a tunnel through a VPC Network binding requires the <strong>Connectivity Directory Admin</strong> role.</p>
<p>The tunnel maintains persistent connections to Cloudflare, eliminating the need for inbound firewall rules or public IP addresses.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15903.md")
</aside>
<h2 id="create-and-run-tunnel-cloudflared">Create and run tunnel (<code>cloudflared</code>)</h2>
<p>Cloudflare Tunnel requires the installation of a lightweight and highly scalable server-side daemon, <code>cloudflared</code>, to connect your infrastructure to Cloudflare.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="version-and-configuration">Version and Configuration</h3>
@markup("md", "content/.markup/bodies/15902.md")
</aside>
<p>Cloudflare Tunnels can be created one of two ways:</p>
<ol>
<li><strong>Remotely-managed tunnels (recommended):</strong> Remotely-managed configurations are stored on Cloudflare, allowing you to manage the tunnel from any machine using the dashboard, API, or Terraform.</li>
<li><strong>Locally-managed tunnels:</strong> A locally-managed tunnel is created by running <code>cloudflared tunnel create &lt;NAME&gt;</code> on the command line. Tunnel configuration is stored in your local cloudflared directory.</li>
</ol>
<p>For Workers VPC, we recommend creating a remotely-managed tunnel through the dashboard. Follow the <a href="/workers-vpc/get-started/">Tunnels for Workers VPC dashboard setup guide</a> to create your tunnel with provided installation commands shown in the dashboard.</p>
<p>For locally-managed tunnels, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/"><code>cloudflared</code> locally-managed tunnels</a> guide. For manual installation, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/"><code>cloudflared</code> downloads page</a> for platform-specific installation instructions.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/15901.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15900.md")
</aside>
<h2 id="cloud-platform-setup-guides">Cloud platform setup guides</h2>
<p>For platform-specific tunnel deployment instructions for production workloads:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/aws/">AWS</a> - Deploy tunnels in Amazon Web Services</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/azure/">Azure</a> - Deploy tunnels in Microsoft Azure</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/google-cloud-platform/">Google Cloud</a> - Deploy tunnels in Google Cloud Platform</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/kubernetes/">Kubernetes</a> - Deploy tunnels in Kubernetes clusters</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/terraform/">Terraform</a> - Deploy tunnels using Infrastructure as Code</li>
</ul>
<p>Refer to the full Cloudflare Tunnel documentation on <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">how to setup Tunnels for high availability and failover with replicas</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15899.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Configure <a href="/workers-vpc/configuration/vpc-services/">VPC Services</a> to connect your tunnels to Workers</li>
<li>Review <a href="/workers-vpc/configuration/tunnel/hardware-requirements/">hardware requirements</a> for capacity planning</li>
<li>Review the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">complete Cloudflare Tunnel documentation</a> for advanced features</li>
</ul>
