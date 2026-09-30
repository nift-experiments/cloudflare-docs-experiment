<p>A route maps an IP address or hostname to a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/#connectors">Cloudflare One connector</a> installed on your private network. When a user connects to that IP or hostname through Cloudflare's network, Cloudflare will route their traffic down a secure tunnel to the corresponding resource in your private network.</p>
<p>The dashboard <strong>Routes</strong> page is the single place to view and manage the routes for all of your connectors — Cloudflare Tunnel, Cloudflare Mesh, Cloudflare WAN, and Magic Transit — in one table. When you create a route, you choose its type, which determines the connector it uses.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5129.md")
</aside>
<h2 id="add-a-cidr-route">Add a CIDR route</h2>
<p>CIDR routes define the IP network segments (such as <code>10.0.0.0/24</code>) that are reachable via a Cloudflare Tunnel or a Cloudflare Mesh node.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisites">Prerequisites</h3>
@markup("md", "content/.markup/bodies/5128.md")
</aside>
<p>To add a CIDR route:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>From the <strong>Routes</strong> tab, select <strong>Create route</strong>, then choose <strong>Tunnel CIDR</strong> (for a <code>cloudflared</code> tunnel) or <strong>Mesh CIDR</strong> (for a Cloudflare Mesh node) as the route type.</li>
<li>For the connector, select the Cloudflare Tunnel or Cloudflare Mesh node that connects your private network to Cloudflare.</li>
<li>Enter the IP address or CIDR range that you wish to route through the connector (for example, <code>10.0.0.1</code> or <code>10.0.0.0/24</code>). This can be a private or public IP.</li>
<li>(Optional) Select a <a href="/cloudflare-one/networks/virtual-networks/">virtual network</a> for this route. A virtual network is a private routing domain that provides routing isolation within your account. This step is only needed if the route's IP/CIDR range overlaps with another route in your account. If you do not select a virtual network, the route will be assigned to the <code>default</code> network.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5127.md")
</aside>
6. Select **Create route**.
<p>Cloudflare will now route requests to your private network. However, the route does not automatically capture traffic from end users. To enable client-side connectivity, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">cloudflared</a> or
<a href="/mesh/features/routes/">Cloudflare Mesh</a> setup guides.</p>
<h2 id="add-a-hostname-route">Add a hostname route</h2>
<p>Hostname routes steer traffic for a public or private hostname down a Cloudflare Tunnel. This allows users to access internal resources using familiar URLs (such as <code>wiki.internal.local</code>) rather than IP addresses.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisites-1">Prerequisites</h3>
@markup("md", "content/.markup/bodies/5126.md")
</aside>
<p>To add a hostname route:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>From the <strong>Routes</strong> tab, select <strong>Create route</strong>, then choose <strong>Tunnel Hostname</strong> as the route type.</li>
<li>For the connector, select the Cloudflare Tunnel that connects your private network to Cloudflare.</li>
<li>In <strong>Hostname</strong>, enter the private or public hostname that represents your application (for example, <code>wiki.internal.local</code> or <code>app.bank.com</code>).</li>
<li>Select <strong>Create route</strong>.</li>
</ol>
<p>Cloudflare will now route requests to your private network. However, the route does not automatically capture traffic from end users. To enable client-side connectivity, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostname</a> or <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/#3-route-network-traffic-through-the-cloudflare-one-client">public hostname</a> setup guides.</p>
<h2 id="add-a-published-application-route">Add a published application route</h2>
<p>Published application routes expose applications to the Internet via a domain that you have connected to Cloudflare. This allows users to access your applications without needing a VPN or specialized client software.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisites-2">Prerequisites</h3>
@markup("md", "content/.markup/bodies/5125.md")
</aside>
<p>To add a published application route to an existing tunnel:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>, then select your tunnel.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>On the <strong>Routes</strong> tab, select <strong>Add route</strong>, then select <strong>Published application</strong>.</p>
</li>
<li>
<p>Enter a subdomain and select a <strong>Domain</strong> from the drop-down menu. Specify any subdomain or path information.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5124.md")
</aside>
<ol start="4">
<li>
<p>In <strong>Service URL</strong>, enter the protocol and address of your application (for example, <code>http://localhost:8000</code>). Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/">supported protocols</a> for available options.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>Anyone on the Internet can now access the application at the specified hostname. To allow or block specific users, <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">create an Access application</a>.</p>
<h2 id="add-a-wan-route">Add a WAN route</h2>
<p>WAN routes define the IP network segments (such as <code>10.0.0.0/24</code>) that are reachable via a GRE or IPsec tunnel. To add a WAN route, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-routes/">WAN Connectors documentation</a>.</p>
