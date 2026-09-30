<p>Using Cloudflare Tunnel's private networks, users can connect to arbitrary non-browser based TCP/UDP applications, like databases. You can set up network policies that implement zero trust controls to define who and what can access those applications using the Cloudflare One Client.</p>
<p>By the end of this tutorial, users that pass network policies will be able to access a remote MySQL database available through a Cloudflare Tunnel on TCP port 3306.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Make sure you have:</p>
<ul>
<li>A MySQL database listening for remote connections and configured with users that can connect remotely</li>
<li>(Optional)<a href="/cloudflare-one/traffic-policies/resolver-policies/">Resolver policies</a> enabled on your account</li>
</ul>
<h2 id="create-a-cloudflare-tunnel">Create a Cloudflare Tunnel</h2>
<p>Install <code>cloudflared</code> on a server in your private network. This server should have connectivity to the MySQL database.</p>
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
<h2 id="add-private-network-routes">Add private network routes</h2>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create route</strong> &gt; <strong>Tunnel CIDR</strong>. Select the tunnel you just created, enter the private IP/CIDR of your MySQL server (for example, <code>10.128.0.175/32</code>), and select <strong>Create route</strong>.</p>
</li>
<li>
<p>(Optional) Repeat to create a second route for the private IP/CIDR of your internal DNS server.</p>
</li>
</ol>
<p>The application and (optional) DNS server are now connected to Cloudflare.</p>
<h2 id="create-a-gateway-network-policy">Create a Gateway network policy</h2>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Network policies</strong>.</li>
<li>Add a <a href="/cloudflare-one/traffic-policies/network-policies/">network policy</a> that targets the private IP address and the port of the MySQL database (port 3306 by default). The following example allows access to the database to the users that enrolled into the Cloudflare One Client using an <code>@example.com</code> email address. The network policies can also take into consideration <a href="/cloudflare-one/reusable-components/posture-checks/">device posture checks</a>.</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination IP</td>
<td>in</td>
<td><code>10.128.0.175</code></td>
<td>And</td>
<td>Allow</td>
</tr>
<tr>
<td>Destination Port</td>
<td>in</td>
<td><code>3306</code></td>
<td>And</td>
<td></td>
</tr>
<tr>
<td>User Email</td>
<td>matches regex</td>
<td><code>.*example.com</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>In addition to the Allow rule above, Cloudflare recommends adding a <a href="/learning-paths/replace-vpn/build-policies/">catch-all block policy</a> to the bottom of your network policy list to enforce a default-deny model.</p>
<p>Allowed Cloudflare One Client users can now connect to the MySQL server at <code>10.128.0.175</code> using the MySQL client of their choice.</p>
<h2 id="optional-create-a-gateway-resolver-policy">(Optional) Create a Gateway resolver policy</h2>
<p>To allow users to access the MySQL database using an internal hostname instead of the private IP address, configure a Gateway resolver policy.</p>
<ol>
<li>
<p>Go to <strong>Traffic policies</strong> &gt; <strong>Resolver policies</strong>.</p>
</li>
<li>
<p>Select <strong>Add a policy</strong>.</p>
</li>
<li>
<p>Create an expression to match against the private <a href="/cloudflare-one/traffic-policies/resolver-policies/#domain">domain</a> or <a href="/cloudflare-one/traffic-policies/resolver-policies/#host">hostname</a> of the application, like in the following example:</p>
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
<td>Domain</td>
<td>in</td>
<td><code>internalrecord.com</code></td>
</tr>
</tbody>
</table>
<ol start="4">
<li>
<p>In <strong>Select DNS resolver</strong>, select <em>Configure custom DNS resolvers</em>.</p>
</li>
<li>
<p>Enter the private IP address of your DNS server.</p>
</li>
<li>
<p>In the dropdown menu, select <em><code>&lt;IP-address&gt; - Private</code></em>.</p>
</li>
<li>
<p>(Optional) Enter a custom port.</p>
</li>
<li>
<p>Select <strong>Create policy</strong>.</p>
</li>
</ol>
<p>If your internal DNS server has an <code>A</code> record for the MySQL database, users can connect to the server using this record. For example, assuming a BIND server that includes the entry:</p>
<p><code>mysql IN  A  10.128.0.175</code></p>
<p>Allowed Cloudflare One Client users can connect to the MySQL database at <code>mysql.internalrecord.com</code> using the MySQL client of their choice.</p>
