<p>End users can connect to an RDP server without the Cloudflare One Client by authenticating through <code>cloudflared</code> in their native terminal. This method requires having <code>cloudflared</code> installed on both the server machine and on the client machine, as well as an active zone on Cloudflare. The traffic is proxied over this connection, and the user logs in to the server with their Cloudflare Access credentials.</p>
<p>Client-side <code>cloudflared</code> can be used in conjunction with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-device-client/">the Cloudflare One Client</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Browser-based RDP</a> so that there are multiple ways to connect to the server. You can reuse the same Cloudflare Tunnel when configuring each connection method.</p>
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
<p>Choose a domain from the drop-down menu and specify any subdomain (for example, <code>rdp.example.com</code>).</p>
</li>
<li>
<p>For <strong>Service</strong>, select <em>RDP</em> and enter the <a href="https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/change-listening-port">RDP listening port</a> of your server (for example, <code>localhost:3389</code>). It will likely be port <code>3389</code>.</p>
</li>
<li>
<p>Select <strong>Add route</strong>.</p>
</li>
</ol>
<h2 id="2-recommended-create-an-access-application"><ol start="2">
<li>(Recommended) Create an Access application</li>
</ol></h2>
<p>By default, anyone on the Internet can connect to the server using the hostname of the published application. To allow or block specific users, create a <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application</a> in Cloudflare Access.</p>
<h2 id="3-connect-as-a-user"><ol start="3">
<li>Connect as a user</li>
</ol></h2>
<ol>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">Install <code>cloudflared</code></a> on the client machine.</li>
<li>Run this command to open an RDP listening port:</li>
</ol>
<pre><code class="language-sh">cloudflared access rdp --hostname rdp.example.com --url rdp://localhost:3389&#10;</code></pre>
<p>This process will need to be configured to stay alive and autostart. If the process is killed, users will not be able to connect.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5498.md")
</aside>
<ol start="3">
<li>While <code>cloudflared access</code> is running, connect from an RDP client such as Microsoft Remote Desktop:
<ol>
<li>Open Microsoft Remote Desktop and select <strong>Add a PC</strong>.</li>
<li>For <strong>PC name</strong>, enter <code>localhost:3389</code>.</li>
<li>For <strong>User account</strong>, enter your RDP server username and password.</li>
<li>Double-click the newly added PC.</li>
<li>When asked if you want to continue, select <strong>Continue</strong>.</li>
</ol>
</li>
</ol>
<p>When the client launches, a browser window will open and prompt the user to authenticate with Cloudflare Access.</p>
