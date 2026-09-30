<p>If you want to manage your own SSH keys, you can use Cloudflare Tunnel to create a secure, outbound-only connection from your server to Cloudflare's global network. This requires running the <code>cloudflared</code> daemon on the server (or any other host machine within the private network). Users with SSH keys that are trusted by the SSH server can access the server by installing the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> on their device and enrolling in your Zero Trust organization. Users can SSH directly to the server's private hostname (for example, <code>ssh.internal.local</code>). You control access to the server using network-level Gateway policies instead of application-level Access policies.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5473.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Cloudflare Zero Trust organization</a></li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">Cloudflare One Client</a> installed on user devices.</li>
<li>Devices <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">enrolled</a> in your Zero Trust organization</li>
</ul>
<h2 id="1-create-an-example-ssh-server"><ol>
<li>Create an example SSH server</li>
</ol></h2>
<p>This example walks through how to set up an SSH server on a Google Cloud Platform (GCP) virtual machine (VM), but you can use any machine that supports SSH connections. If you already have an SSH server configured, you can skip to <a href="#2-connect-the-server-to-cloudflare">Step 2</a>.</p>
<h3 id="1-1-create-an-ssh-key-pair">1.1 Create an SSH key pair</h3>
<p>Before creating your VM instance you will need to create an SSH key pair.</p>
<ol>
<li>Open a terminal and type the following command:</li>
</ol>
<pre><code class="language-sh">ssh-keygen -t rsa -f ~/.ssh/gcp_ssh -C &lt;username in GCP&gt;&#10;</code></pre>
<ol start="2">
<li>
<p>Enter your passphrase when prompted. It will need to be entered twice.</p>
<p>Two files will be generated: <code>gcp_ssh</code> which contains the private key, and <code>gcp_ssh.pub</code> which contains the public key.</p>
</li>
<li>
<p>In the command line, enter:</p>
</li>
</ol>
<pre><code class="language-sh">cat ~/.ssh/gcp_ssh.pub&#10;</code></pre>
<ol start="4">
<li>Copy the output. This will be used when creating the VM instance in GCP.</li>
</ol>
<h3 id="1-2-create-a-vm-instance-in-gcp">1.2 Create a VM instance in GCP</h3>
<p>Now that the SSH key pair has been created, you can create a VM instance.</p>
<ol>
<li>In your <a href="https://console.cloud.google.com/">Google Cloud Console</a>, <a href="https://developers.google.com/workspace/guides/create-project">create a new project</a>.</li>
<li>Go to <strong>Compute Engine</strong> &gt; <strong>VM instances</strong>.</li>
<li>Select <strong>Create instance</strong>.</li>
<li>Name your VM instance, for example <code>ssh-server</code>.</li>
<li>Scroll down to <strong>Advanced options</strong> &gt; <strong>Security</strong> &gt; <strong>Manage Access</strong>.</li>
<li>Under <strong>Add manually generated SSH keys</strong>, select <strong>Add item</strong> and paste the public key that you have created.</li>
<li>Select <strong>Create</strong>.</li>
<li>Once your VM instance is running, open the dropdown next to <strong>SSH</strong> and select <em>Open in browser window</em>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5472.md")
</aside>
<h2 id="2-connect-the-server-to-cloudflare"><ol start="2">
<li>Connect the server to Cloudflare</li>
</ol></h2>
<p>This section covers how to create a new Cloudflare Tunnel for your SSH server. You can reuse the same tunnel for all services on a private network that are reachable from the <code>cloudflared</code> host.</p>
<ol>
<li>Log in to the Cloudflare dashboard and go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create a tunnel</strong>.</p>
</li>
<li>
<p>Enter a name for your tunnel. We suggest choosing a name that reflects the type of resources you want to connect through this tunnel (for example, <code>enterprise-VPC-01</code>).</p>
</li>
<li>
<p>Select <strong>Create Tunnel</strong>.</p>
</li>
<li>
<p>Choose your operating system, then copy the installation command and run it in a terminal on your origin server.</p>
</li>
<li>
<p>Wait for the tunnel to connect. Once the connection is established, select <strong>Continue</strong>.</p>
</li>
</ol>
<h2 id="3-use-hostname-routes"><ol start="3">
<li>Use hostname routes</li>
</ol></h2>
<p>Hostname routes allow you to SSH directly to <code>ssh.internal.local</code> without managing static IP routes.  Hostname routes are especially useful when your SSH server has an unknown or ephemeral IP address, such as dynamic infrastructure provisioned by cloud providers.</p>
   <details class="nb-details"><summary>How hostname routing works</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5475.md")
</div></details>
<p>If you do not have a private DNS resolver configured or would rather SSH to an IP address, skip to <a href="#4-optional-use-ip-routes">Step 4</a>.</p>
<h3 id="3-1-add-a-hostname-route">3.1 Add a hostname route</h3>
<p>To add a hostname route to your tunnel:</p>
<ol>
<li>Go to <strong>Networking</strong> &gt; <strong>Tunnels</strong> and select your tunnel.</li>
<li>On the <strong>Routes</strong> tab, select <strong>Add route</strong>, then select <strong>Private hostname</strong>.</li>
<li>Enter the hostname of your SSH server (for example, <code>ssh.internal.local</code>).</li>
</ol>
<details class="nb-details"><summary>Hostname format restrictions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5476.md")
</div></details>
<ol start="4">
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="3-2-configure-dns-resolution">3.2 Configure DNS resolution</h3>
<p>When Gateway receives a request for your private hostname, it must resolve the hostname to your SSH server's private IP address.</p>
<h4 id="scenario-a-use-the-system-resolver-default">Scenario A: Use the system resolver (Default)</h4>
<p>By default, <code>cloudflared</code> uses the private DNS resolver configured on its host machine (for example, in <code>/etc/resolv.conf</code> on Linux). If the machine running <code>cloudflared</code> can already resolve <code>ssh.internal.local</code> to its private IP using the local system resolver, no further configuration is required. You can skip to <a href="#33-configure-cloudflare-one-clients">Step 3.3</a>.</p>
<details class="nb-details"><summary>Verify local DNS resolution</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5477.md")
</div></details>
<h4 id="scenario-b-use-a-specific-private-dns-server-advanced">Scenario B: Use a specific private DNS server (Advanced)</h4>
<p>If you need <code>cloudflared</code> to use a specific internal DNS server that is different from the host's default resolver, you must explicitly connect that DNS server to Cloudflare via an <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">IP/CIDR route</a>. You will also need to configure a <a href="/cloudflare-one/traffic-policies/resolver-policies/">Gateway resolver policy</a> to route queries to this specific private DNS server.</p>
<ol>
<li>To create an IP/CIDR route for the DNS server:
<ol>
<li>Go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</li>
</ol>
</li>
</ol>
<div class="nb-dash-button"></div>
<pre><code>2. Select **Add CIDR route**.&#10;3. Enter the private IP address of your internal DNS resolver.&#10;4. Select the Cloudflare Tunnel that connects to the network where this DNS server resides.&#10;5. Select **Create**.&#10;</code></pre>
<ol start="2">
<li>To create a resolver policy:
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Resolver policies</strong>.</li>
<li>Select <strong>Create a policy</strong>.</li>
<li>Create an expression that matches the private hostname:</li>
</ol>
</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td>in</td>
<td><code>ssh.internal.local</code></td>
</tr>
</tbody>
</table>
    4. Under **Configure custom DNS resolvers**, enter the private IP address of your internal DNS server.
    5. From the dropdown menu, select the `- Private` routing option and the [virtual network](/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/) assigned to the tunnel you selected in the previous step.
    6. Select **Create policy**.
<h3 id="3-3-configure-cloudflare-one-clients">3.3 Configure Cloudflare One Clients</h3>
<p>To connect to private hostnames, Cloudflare One Clients must be configured to forward the following traffic to Cloudflare:</p>
<ul>
<li>
<p>Initial resolved IPs:</p>
</li>
<li>
<p><strong>IPv4</strong>: <code>172.64.128.0/20</code></p>
</li>
<li>
<p><strong>IPv6</strong>: <code>2606:4700:0cf1:4000::/64</code></p>
</li>
</ul>
<p>This is the default range. You can <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">configure a custom initial resolved IP range</a> for IPv4 if it conflicts with your existing network.</p>
<ul>
<li>DNS queries for your private hostname</li>
</ul>
<h4 id="3-3-1-configure-split-tunnels">3.3.1 Configure Split Tunnels</h4>
<p>In your WARP <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a>, configure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> such that the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5478.md")
</div> route through the WARP tunnel.  Configuration depends on your [Split Tunnels mode](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#change-split-tunnels-mode):
<ul>
<li>
<p><strong>Exclude mode</strong>: Delete <code>100.64.0.0/10</code> from your Split Tunnels list. We recommend <a href="/cloudflare-one/networks/routes/reserved-ips/#split-tunnel-configuration">adding back the IP ranges</a> that are not explicitly used for Cloudflare One services. This reduces the risk of conflicts with existing private network configurations that may use the CGNAT address space.</p>
</li>
<li>
<p><strong>Include mode</strong>: Add Split Tunnel entries for the following IP addresses:</p>
</li>
<li>
<p><strong>IPv4</strong>: <code>172.64.128.0/20</code></p>
</li>
<li>
<p><strong>IPv6</strong>: <code>2606:4700:0cf1:4000::/64</code></p>
</li>
</ul>
<p>This is the default range. You can <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">configure a custom initial resolved IP range</a> for IPv4 if it conflicts with your existing network.</p>
<h4 id="3-3-2-configure-local-domain-fallback">3.3.2 Configure Local Domain Fallback</h4>
<p>In <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a>, delete the top-level domain for your private hostname. This configures WARP to send the DNS query to Cloudflare Gateway for resolution.</p>
<p>For example, if your SSH hostname is <code>ssh.internal.local</code>, remove <code>internal.local</code> from Local Domain Fallback.</p>
<h2 id="4-optional-use-ip-routes"><ol start="4">
<li>(Optional) Use IP routes</li>
</ol></h2>
<h3 id="4-1-add-an-ip-route">4.1 Add an IP route</h3>
<p>To connect to the SSH server using its IP address (instead of a <a href="#3-use-hostname-routes">hostname</a>), <a href="/cloudflare-one/networks/routes/add-routes/#add-a-cidr-route">add a CIDR route</a> that includes the server's private IP address.</p>
<h3 id="4-2-configure-cloudflare-one-clients">4.2 Configure Cloudflare One Clients</h3>
<p>By default, WARP excludes traffic bound for <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918 space</a>, which are IP addresses typically used in private networks and not reachable from the Internet. In order for the Cloudflare One Client to send traffic to your <p>private network</p>
, you must configure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> so that the IP/CIDR of your <p>private network</p>
routes through the Cloudflare One Client.</p>
<ol>
<li>First, check whether your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#change-split-tunnels-mode">Split Tunnels mode</a> is set to <strong>Exclude</strong> or <strong>Include</strong> mode.</li>
<li>Edit your Split Tunnel routes depending on the mode:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5482.md")
</div></div>
<h2 id="5-optional-create-gateway-network-policies"><ol start="5">
<li>(Optional) Create Gateway network policies</li>
</ol></h2>
<p>By default, all devices enrolled in your organization can SSH to the server unless you build Gateway network policies to allow or block specific users. You can create policies based on user identity, device posture, location, and other criteria.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5485.md")
</div></div>
<p>Cloudflare will now proxy traffic from enrolled devices, except for the traffic excluded in your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/#3-route-private-network-ips-through-the-cloudflare-one-client">split tunnel settings</a>. For more information on how Gateway forwards traffic, refer to <a href="/cloudflare-one/traffic-policies/proxy/">Gateway proxy</a>.</p>
<h3 id="example-policies">Example policies</h3>
<p>The following example consists of two policies: the first allows specific users to reach your SSH server, and the second blocks all other traffic.</p>
<h4 id="policy-1-allow-authorized-users">Policy 1: Allow authorized users</h4>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>Network</strong>.</li>
<li>Select <strong>Create a policy</strong>.</li>
<li>Name your policy (for example, <code>Allow SSH to internal server</code>).</li>
<li>Create an expression to match your SSH hostname and authorized users:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>SNI</td>
<td>in</td>
<td><code>ssh.internal.local</code></td>
</tr>
<tr>
<td>User Email</td>
<td>in</td>
<td><code>admin@example.com</code>, <code>devops@example.com</code></td>
</tr>
</tbody>
</table>
<ol start="5">
<li>In <strong>Action</strong>, select <strong>Allow</strong>.</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<h4 id="policy-2-catch-all-block">Policy 2: Catch-all block</h4>
<p>To prevent Cloudflare One Client users from accessing your entire private network, we recommend creating a <a href="/learning-paths/replace-vpn/build-policies/create-policy/#catch-all-policy">catch-all Gateway block policy</a> for your private IP space. You can then layer on higher priority Allow policies (in either Access or Gateway) which grant users access to specific applications or IPs.</p>
<h3 id="additional-security-with-dns-policies">Additional security with DNS policies</h3>
<p>For an additional layer of protection, create a Gateway DNS policy to control DNS resolution:</p>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Firewall Policies</strong> &gt; <strong>DNS</strong>.</li>
<li>Select <strong>Create a policy</strong>.</li>
<li>Name your policy (for example, <code>Allow SSH hostname resolution</code>).</li>
<li>Create an expression:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td>in</td>
<td><code>ssh.internal.local</code></td>
</tr>
<tr>
<td>User Email</td>
<td>in</td>
<td><code>admin@example.com</code>, <code>devops@example.com</code></td>
</tr>
</tbody>
</table>
<ol start="5">
<li>In <strong>Action</strong>, select <strong>Allow</strong>.</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sni-selector-limitations">SNI selector limitations</h3>
@markup("md", "content/.markup/bodies/5471.md")
</aside>
<h2 id="6-connect-as-a-user"><ol start="6">
<li>Connect as a user</li>
</ol></h2>
<p>Once you have set up the tunnel route and the user device, the user can now SSH into the machine. If your SSH server requires an SSH key, the key should be included in the SSH command.</p>
<pre><code class="language-sh">ssh -i ~/.ssh/gcp_ssh &lt;username&gt;@ssh.internal.local&#10;</code></pre>
<p>The Cloudflare One Client must be connected to your Zero Trust organization. Users will be able to connect if they match the Gateway network policies you created.</p>
<h3 id="troubleshooting">Troubleshooting</h3>
<p>If you cannot connect, verify the following:</p>
<ol>
<li><strong>Confirm DNS resolution</strong> - From the device, confirm that you can successfully resolve the private hostname:</li>
</ol>
<pre><code class="language-sh">nslookup ssh.internal.local&#10;</code></pre>
<pre><code class="language-sh">Server:		127.0.2.2&#10;Address:	127.0.2.2#53&#10;&#10;Non-authoritative answer:&#10;Name:	ssh.internal.local&#10;Address: 172.64.128.48&#10;</code></pre>
<p>The query should resolve using <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#dns-traffic">WARP's DNS proxy</a> and return a Gateway <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5486.md")
</div>. If the query fails to resolve or returns a different IP, check your [Local Domain Fallback](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) configuration and [Gateway resolver policies](/cloudflare-one/traffic-policies/resolver-policies/).
<ol start="2">
<li>
<p><strong>Check Gateway logs</strong> - Review your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway network logs</a> to see if the connection is being blocked by a policy.</p>
</li>
<li>
<p><strong>Verify tunnel status</strong> - Confirm that your tunnel is healthy and connected by checking <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/">tunnel status</a>.</p>
</li>
<li>
<p><strong>Test connectivity to initial resolved IP</strong> - When you connect to the SSH server using its private hostname, the device should make a connection to the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
</li>
</ol>
@markup("md", "content/.markup/bodies/5487.md")
</div>:
<pre><code class="language-sh">ssh -v &lt;username&gt;@ssh.internal.local&#10;</code></pre>
<pre><code class="language-sh">...&#10;Authenticated to ssh.internal.local ([172.64.128.48]:22) using &quot;publickey&quot;.&#10;...&#10;</code></pre>
<pre><code>	Look for a line showing connection to an IP in your account's [initial resolved IP range](/cloudflare-one/networks/routes/reserved-ips/#gateway-initial-resolved-ips). If the request fails, confirm that the initial resolved IP [routes through the WARP tunnel](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/). You can also check your [tunnel logs](/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/) to confirm that requests are routing to the server's private IP.&#10;</code></pre>
