<p>Spectrum is available on all paid plans. Pro and Business support selected protocols only, whereas Enterprise supports all TCP and UDP based traffic. Refer to <a href="/spectrum/reference/configuration-options/">Configuration options</a> for more configuration details.</p>
<p>To create a Spectrum application, you can either use an IP address, a CNAME Record or a load balancer. Independently of the method you use, you can create the application through the dashboard or via <a href="/api/resources/spectrum/subresources/apps/methods/list/">API</a>.</p>
<p>Certain fields in Spectrum request and response bodies require an Enterprise plan. Refer to the <a href="/spectrum/reference/settings-by-plan/">Settings by plan</a> page for more details.</p>
<h2 id="create-a-spectrum-application-using-an-ip-address">Create a Spectrum application using an IP address</h2>
<p>To create a Spectrum application using an IP address, Cloudflare normally assigns you an arbitrary IP from Cloudflare’s IP pool to your application. If you want to use your own IP addresses, you can use <a href="/spectrum/about/byoip/">BYOIP</a> or you can also use a <a href="/spectrum/about/static-ip/">Static IP</a>. In these two last cases, you need to create your Spectrum application through the API, as these features are not available via dash. When using the API, the field <code>origin_direct</code> takes as input the IP address.</p>
<details class="nb-details"><summary>Add your application via Dashboard</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/338.md")
</div></details>
<details class="nb-details"><summary>Add your application via API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/339.md")
</div></details>
<h2 id="create-a-spectrum-application-using-a-cname-record">Create a Spectrum application using a CNAME record</h2>
<p>To create a Spectrum application using a CNAME record, you will need to create a <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/">CNAME record</a> on your Cloudflare hosted zone that points to your origin's hostname. This is required to resolve to your hostname origin. Refer to <a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">Create DNS records</a>, for more information. When using a CNAME as an origin, note that Cloudflare needs to be authoritative for that zone. When using the API, the <code>origin_dns</code> field takes as input the CNAME record.</p>
<details class="nb-details"><summary>Add your application via Dashboard</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/340.md")
</div></details>
<details class="nb-details"><summary>Add your application via API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/341.md")
</div></details>
<h2 id="create-a-spectrum-application-using-a-load-balancer">Create a Spectrum application using a load balancer</h2>
<p>To create a Spectrum application using a load balancer, you will need to generate a load balancer from the dashboard or via the API. Refer to the <a href="/load-balancing/additional-options/spectrum/#1-configure-your-load-balancer">Load Balancing documentation</a> for more details.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/337.md")
</aside>
<details class="nb-details"><summary>Add your application via Dashboard</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/342.md")
</div></details>
<details class="nb-details"><summary>Add your application via API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/343.md")
</div></details>
<h2 id="create-a-spectrum-application-using-a-virtual-network-origin">Create a Spectrum application using a virtual network origin</h2>
<p>To proxy TCP or UDP traffic to an origin on your private network, attach a Cloudflare Tunnel <a href="/cloudflare-one/networks/virtual-networks/">virtual network</a> to a Spectrum application. Spectrum routes traffic through the connector (Cloudflare Tunnel or Cloudflare WAN connection) associated with that virtual network. This provides an alternative to the previous pattern of putting a load balancer in front of a private origin.</p>
<p>Virtual network origins are only supported for TCP and UDP applications. The origin must be a single private IP routable within the specified virtual network. Port ranges, hostname origins (<code>origin_dns</code>), and multiple addresses in <code>origin_direct</code> are not supported. <a href="/spectrum/how-to/enable-proxy-protocol/">Proxy Protocol</a> is not currently supported, so <code>proxy_protocol</code> must be set to <code>off</code>. For details on validation errors, refer to <a href="/spectrum/reference/error-codes/">Error codes</a>.</p>
<p>For a primer on virtual networks, refer to <a href="/cloudflare-one/networks/virtual-networks/">Virtual networks</a>.</p>
<h3 id="before-you-begin">Before you begin</h3>
<p>Set up the virtual network and a route covering your origin IP before creating the Spectrum application:</p>
<ul>
<li>Create a virtual network and a Cloudflare Tunnel that carries it by following <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">Manage virtual networks</a>.</li>
<li>Attach a route covering your origin's private IP to the tunnel by following <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">Connect an IP/CIDR</a>.</li>
</ul>
<p>For Cloudflare WAN (formerly Magic WAN) as the connector, refer to <a href="/cloudflare-wan/get-started/">Get started with Cloudflare WAN</a> for setting up tunnel endpoints and routes.</p>
<details class="nb-details"><summary>Add your application via Dashboard</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/344.md")
</div></details>
<details class="nb-details"><summary>Add your application via API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/345.md")
</div></details>
<h2 id="view-traffic">View traffic</h2>
<p>You can now proxy traffic through Cloudflare without additional configuration. As you run traffic through Cloudflare, you will see the last minute of traffic from <strong>Spectrum</strong> in the dashboard.</p>
<p>If you have any feedback, please <a href="https://community.cloudflare.com/c/website-application-performance/spectrum/48">let us know</a>.</p>
