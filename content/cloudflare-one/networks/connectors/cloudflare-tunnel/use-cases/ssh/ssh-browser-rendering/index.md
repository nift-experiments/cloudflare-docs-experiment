<p>Cloudflare's browser-based terminal allows end users to connect to an SSH server without managing SSH keys or installing the Cloudflare One Client.</p>
<p>This method requires routing SSH access to the server through a public hostname. The traffic is proxied over this connection, and the user logs in to the server with their Cloudflare Access credentials.</p>
<p>The browser-based terminal can be used in conjunction with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-device-client/">the Cloudflare One Client</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Access for Infrastructure</a> so that there are multiple ways to connect to the server. You can reuse the same Cloudflare Tunnel when configuring each connection method.</p>
<h2 id="1-connect-the-server-to-cloudflare"><ol>
<li>Connect the server to Cloudflare</li>
</ol></h2>
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
<p>Choose a domain from the drop-down menu and specify any subdomain (for example, <code>ssh.example.com</code>).</p>
</li>
<li>
<p>For <strong>Service</strong>, select <em>SSH</em> and enter <code>localhost:22</code>. If the SSH server is on a different machine from where you installed the tunnel, enter <code>&lt;server IP&gt;:22</code>.</p>
</li>
<li>
<p>Select <strong>Add route</strong>.</p>
</li>
<li>
<p>(Recommended) Add a <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application</a> to Cloudflare Access in order to manage access to your server.</p>
</li>
</ol>
<h2 id="2-connect-as-a-user"><ol start="2">
<li>Connect as a user</li>
</ol></h2>
<p>To enable browser-rendering for SSH, refer to <a href="/cloudflare-one/access-controls/applications/non-http/browser-rendering/">Browser-rendered terminal</a>.</p>
<p>When users visit the public hostname URL (for example, <code>https://ssh.example.com</code>) and log in with their Access credentials, Cloudflare will render a terminal in their browser.</p>
