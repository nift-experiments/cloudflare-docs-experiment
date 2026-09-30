<p>This guide covers how to enable secure remote access to private IP addresses using <code>cloudflared</code> and the Cloudflare One Client. You can connect an entire private network, a subnet, or an application defined by a static IP.</p>
<h2 id="1-connect-the-server-to-cloudflare"><ol>
<li>Connect the server to Cloudflare</li>
</ol></h2>
<p>To connect your infrastructure with Cloudflare Tunnel:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">Create a new tunnel</a> or edit an existing <code>cloudflared</code> tunnel.</p>
</li>
<li>
<p>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</p>
</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="4">
<li>
<p>Select <strong>Create route</strong> &gt; <strong>Tunnel CIDR</strong>.</p>
</li>
<li>
<p>Select the tunnel you just created, then enter the IP/CIDR range that you wish to route through the tunnel (for example, <code>10.0.0.1</code> or <code>10.0.0.0/8</code>).</p>
</li>
<li>
<p>(Optional) Select a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">virtual network</a> for this tunnel route. This step is only needed if the route's IP/CIDR range overlaps with another route in your account. If you do not select a virtual network, the IP route will be assigned to the <code>default</code> network.</p>
</li>
<li>
<p>Select <strong>Create route</strong>.</p>
</li>
</ol>
<h2 id="2-set-up-the-client"><ol start="2">
<li>Set up the client</li>
</ol></h2>
<p>To connect your devices to Cloudflare:</p>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">Deploy the Cloudflare One Client</a> on your devices in Traffic and DNS mode or <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">generate a proxy endpoint</a> and deploy a PAC file.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">Create device enrollment rules</a> to determine which devices can enroll to your Zero Trust organization.</li>
</ol>
<h2 id="3-route-private-network-ips-through-the-cloudflare-one-client"><ol start="3">
<li>Route private network IPs through the Cloudflare One Client</li>
</ol></h2>
<p>By default, WARP excludes traffic bound for <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918 space</a>, which are IP addresses typically used in private networks and not reachable from the Internet. In order for the Cloudflare One Client to send traffic to your <p>private network</p>
, you must configure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> so that the IP/CIDR of your <p>private network</p>
routes through the Cloudflare One Client.</p>
<ol>
<li>First, check whether your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#change-split-tunnels-mode">Split Tunnels mode</a> is set to <strong>Exclude</strong> or <strong>Include</strong> mode.</li>
<li>Edit your Split Tunnel routes depending on the mode:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5425.md")
</div></div>
<h2 id="4-recommended-filter-network-traffic-with-gateway"><ol start="4">
<li>(Recommended) Filter network traffic with Gateway</li>
</ol></h2>
<p>By default, all devices enrolled in your Zero Trust organization can connect to your private network through Cloudflare Tunnel. You can configure Gateway to inspect your network traffic and either block or allow access based on user identity and device posture. To learn more about policy design, refer to <a href="/learning-paths/replace-vpn/build-policies/create-policy/">Secure your first application</a>.</p>
<h3 id="enable-the-gateway-proxy">Enable the Gateway proxy</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5428.md")
</div></div>
<p>Cloudflare will now proxy traffic from enrolled devices, except for the traffic excluded in your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/#3-route-private-network-ips-through-the-cloudflare-one-client">split tunnel settings</a>. For more information on how Gateway forwards traffic, refer to <a href="/cloudflare-one/traffic-policies/proxy/">Gateway proxy</a>.</p>
<h3 id="zero-trust-policies">Zero Trust policies</h3>
<p>To prevent Cloudflare One Client users from accessing your entire private network, we recommend creating a <a href="/learning-paths/replace-vpn/build-policies/create-policy/#catch-all-policy">catch-all Gateway block policy</a> for your private IP space. You can then layer on higher priority Allow policies (in either Access or Gateway) which grant users access to specific applications or IPs.</p>
<p>If you have applications clearly defined by IPs or hostnames, we recommend <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">creating an Access application</a> and managing user access alongside your SaaS and other web apps. Alternatively, if you prefer to secure a private network using a traditional firewall model, you can build Gateway network and DNS policies for IP ranges and domains.</p>
<p>For more information on building Gateway policies, refer to <a href="/learning-paths/replace-vpn/build-policies/create-policy/">Secure your first application</a> and <a href="/cloudflare-one/traffic-policies/network-policies/common-policies/#restrict-access-to-private-networks">Common network policies</a>.</p>
<h2 id="5-connect-as-a-user"><ol start="5">
<li>Connect as a user</li>
</ol></h2>
<p>End users can now reach HTTP or TCP-based services on your network by visiting any IP address in the range you have specified.</p>
<p>To allow users to reach the service using its private hostname instead of its IP, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/private-dns/">Private DNS</a>.</p>
<p>To expose an IP from this range to public TCP or UDP traffic, refer to <a href="/spectrum/get-started/#create-a-spectrum-application-using-a-virtual-network-origin">Create a Spectrum application using a virtual network</a>.</p>
<h3 id="troubleshooting">Troubleshooting</h3>
<h4 id="device-configuration">Device configuration</h4>
<p>To check that their device is properly configured, the user can visit <code>https://help.teams.cloudflare.com/</code> to ensure that:</p>
<ul>
<li>The page returns <strong>Your network is fully protected</strong>.</li>
<li>In <strong>HTTP filtering</strong>, both <strong>WARP</strong> and <strong>Gateway Proxy</strong> are enabled.</li>
<li>The <strong>Team name</strong> matches the Zero Trust organization from which you created the tunnel.</li>
</ul>
<h4 id="router-configuration">Router configuration</h4>
<p>Check the local IP address of the device and ensure that it does not fall within the IP/CIDR range of your private network. For example, some home routers will make DHCP assignments in the <code>10.0.0.0/24</code> range, which overlaps with the <code>10.0.0.0/8</code> range used by most corporate private networks. When a user's home network shares the same IP addresses as the routes in your tunnel, their device will be unable to connect to your application.</p>
<p>To resolve the IP conflict, you can either:</p>
<ul>
<li>Reconfigure the user's router to use a non-overlapping IP range. Compatible routers typically use <code>192.168.1.0/24</code>, <code>192.168.0.0/24</code> or <code>172.16.0.0/24</code>.</li>
<li>Tighten the IP range in your Split Tunnel configuration to exclude the <code>10.0.0.0/24</code> range. This will only work if your private network does not have any hosts within <code>10.0.0.0/24</code>.</li>
<li>Change the IP/CIDR of your private network so that it does not overlap with a range commonly used by home networks.</li>
</ul>
