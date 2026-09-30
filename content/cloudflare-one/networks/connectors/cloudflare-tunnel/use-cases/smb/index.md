<p>The Server Message Block (SMB) protocol allows users to read, write, and access shared resources on a network. Due to security risks, firewalls and ISPs usually block public connections to an SMB file share. With Cloudflare Tunnel, you can provide secure and simple SMB access to users outside of your network.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5258.md")
</aside>
<p>Cloudflare Zero Trust offers two solutions for connecting to SMB servers:</p>
<ul>
<li><a href="#connect-to-smb-server-with-the-cloudflare-one-client-to-tunnel">Private subnet routing with the Cloudflare One Client to Tunnel</a></li>
<li><a href="#connect-to-smb-server-with-cloudflared-access">Public hostname routing with <code>cloudflared access</code></a></li>
</ul>
<h2 id="set-up-an-smb-server-on-linux">Set up an SMB server on Linux</h2>
<p>While SMB was developed for Microsoft Windows, Samba provides SMB connectivity from UNIX-like and BSD systems. A Samba server can be set up using this <a href="https://ubuntu.com/tutorials/install-and-configure-samba#1-overview">guide</a> on an Ubuntu machine.</p>
<h2 id="connect-to-smb-server-with-the-cloudflare-one-client-to-tunnel">Connect to SMB server with the Cloudflare One Client to Tunnel</h2>
<p>You can use Cloudflare Tunnel to create a secure, outbound-only connection from your server to Cloudflare's global network. This requires running the <code>cloudflared</code> daemon on the server. Users reach the service by installing the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> on their device and enrolling in your Zero Trust organization. Remote devices will be able to connect as if they were on your private network. By default, all devices enrolled in your organization can access the service unless you build policies to allow or block specific users.</p>
<h3 id="1-connect-the-server-to-cloudflare"><ol>
<li>Connect the server to Cloudflare</li>
</ol></h3>
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
<li>Select <strong>Create route</strong> &gt; <strong>Tunnel CIDR</strong>. Select the tunnel you just created, enter the private IP or CIDR address of your server, and select <strong>Create route</strong>.</li>
<li>(Optional) <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/#4-recommended-filter-network-traffic-with-gateway">Set up Zero Trust policies</a> to fine-tune access to your server.</li>
</ol>
<h3 id="2-set-up-the-client"><ol start="2">
<li>Set up the client</li>
</ol></h3>
<p>To connect your devices to Cloudflare:</p>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">Deploy the Cloudflare One Client</a> on your devices in Traffic and DNS mode or <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">generate a proxy endpoint</a> and deploy a PAC file.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">Create device enrollment rules</a> to determine which devices can enroll to your Zero Trust organization.</li>
</ol>
<h3 id="3-route-private-network-ips-through-the-cloudflare-one-client"><ol start="3">
<li>Route private network IPs through the Cloudflare One Client</li>
</ol></h3>
<p>By default, WARP excludes traffic bound for <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918 space</a>, which are IP addresses typically used in private networks and not reachable from the Internet. In order for the Cloudflare One Client to send traffic to your <p>private network</p>
, you must configure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> so that the IP/CIDR of your <p>private network</p>
routes through the Cloudflare One Client.</p>
<ol>
<li>First, check whether your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#change-split-tunnels-mode">Split Tunnels mode</a> is set to <strong>Exclude</strong> or <strong>Include</strong> mode.</li>
<li>Edit your Split Tunnel routes depending on the mode:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5262.md")
</div></div>
<h3 id="4-connect-as-a-user"><ol start="4">
<li>Connect as a user</li>
</ol></h3>
<h4 id="macos">macOS</h4>
<ol>
<li>
<p>In the Finder menu, select <strong>Go</strong> &gt; <strong>Connect to Server</strong>.</p>
</li>
<li>
<p>Enter <code>smb://&lt;smb-server-ip-address&gt;/sambashare</code>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/connect-apps/use-cases/smb-connect.png" alt="Connect to SMB server in macOS" /></p>
<ol start="3">
<li>Sign in with the username and password created while setting up the server.</li>
</ol>
<h4 id="windows">Windows</h4>
<ol>
<li>Open File Explorer and right-click <strong>Network</strong> &gt; <strong>Map Network Drive</strong>.</li>
<li>For <strong>Folder</strong>, enter <code>\\&lt;server-private-ip&gt;\sambashare</code>.</li>
<li>Select <strong>Connect using different credentials</strong>.</li>
<li>Select <strong>Finish</strong>.</li>
<li>Sign in with the username and password created while setting up the server.</li>
</ol>
<h2 id="connect-to-smb-server-with-cloudflared-access">Connect to SMB server with <code>cloudflared access</code></h2>
<p>Cloudflare Tunnel can also route applications through a public hostname, which allows users to connect to the application without the Cloudflare One Client. This method requires having <code>cloudflared</code> installed on both the server machine and on the client machine, as well as an active zone on Cloudflare. The traffic is proxied over this connection, and the user logs in to the server with their Cloudflare Access credentials.</p>
<p>The public hostname method can be implemented in conjunction with routing over the Cloudflare One Client so that there are multiple ways to connect to the server. You can reuse the same tunnel for both the private network and public hostname routes.</p>
<h3 id="1-connect-the-server-to-cloudflare-1"><ol>
<li>Connect the server to Cloudflare</li>
</ol></h3>
<ol>
<li>
<p>Create a Cloudflare Tunnel by following our <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">dashboard setup guide</a>.</p>
</li>
<li>
<p>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong> and select your tunnel.</p>
</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>
<p>On the <strong>Routes</strong> tab, select <strong>Add route</strong>, then select <strong>Published application</strong>.</p>
</li>
<li>
<p>Choose a domain from the drop-down menu and specify any subdomain (for example, <code>smb.example.com</code>).</p>
</li>
<li>
<p>For <strong>Service</strong>, select <em>SMB</em> and enter the SMB listening port (for example, <code>localhost:445</code>). SMB drives listen on port <code>139</code> or <code>445</code> by default.</p>
</li>
<li>
<p>Select <strong>Add route</strong>.</p>
</li>
</ol>
<h3 id="2-recommended-create-an-access-application"><ol start="2">
<li>(Recommended) Create an Access application</li>
</ol></h3>
<p>By default, anyone on the Internet can connect to the server using the hostname of the published application. To allow or block specific users, create a <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application</a> in Cloudflare Access.</p>
<h3 id="3-connect-as-a-user"><ol start="3">
<li>Connect as a user</li>
</ol></h3>
<ol>
<li>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">Install <code>cloudflared</code></a> on the client machine.</p>
</li>
<li>
<p>Run the following command to open an SMB listening port. You can specify any available port on the client machine.</p>
</li>
</ol>
<pre><code class="language-sh">cloudflared access tcp --hostname smb.example.com --url localhost:8445&#10;</code></pre>
<p>This command can be wrapped as a desktop shortcut so that end users do not need to use the command line.</p>
<ol start="3">
<li>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/smb/#4-connect-as-a-user">Open your SMB client</a> and configure the client to point to <code>smb://localhost:8445/sambashare</code>. Do not input the hostname.</p>
</li>
<li>
<p>Sign in with the username and password created while setting up the server.</p>
</li>
</ol>
<h4 id="windows-specific-requirements">Windows-specific requirements</h4>
<p>If you are using a Windows machine and cannot specify the port for SMB, you might need to disable the local server. The local server on a client machine uses the same default port <code>445</code> for CIFS/SMB. By listening on that port, the local server can block the <code>cloudflare access</code> connection.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5257.md")
</aside>
<p>To disable the local server on a Windows machine:</p>
<ol>
<li>Select <strong>Win</strong>+<strong>R</strong> to open the Run window.</li>
<li>Type <code>services.msc</code> and select <strong>Enter</strong>.</li>
<li>Locate the local server process, likely called <code>Server</code>.</li>
<li>Stop the service and set <strong>Startup type</strong> to <em>Disabled</em>.</li>
<li>Repeat steps 3 and 4 for <code>TCP/IP NetBIOS Helper</code>.</li>
</ol>
