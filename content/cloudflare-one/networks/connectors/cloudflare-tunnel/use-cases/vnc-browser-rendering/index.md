<p>A Virtual Network Computer (VNC) server provides users with remote access to a computer's desktop environment. Cloudflare can render a VNC terminal in the browser without any client-side software or configuration.</p>
<p>Browser-rendered VNC requires connecting the VNC server to Cloudflare and routing traffic through a public hostname. To access the VNC server, users go to the public hostname URL and log in through Cloudflare Access using your configured identity provider. Cloudflare will apply your <a href="/cloudflare-one/access-controls/policies/">Access policies</a> and, when a user is allowed, render a VNC client in their browser.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5256.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/fundamentals/manage-domains/add-site/">active domain on Cloudflare</a>.</li>
<li>The domain uses either a <a href="/dns/zone-setups/full-setup/">full setup</a> or a <a href="/dns/zone-setups/partial-setup/">partial (<code>CNAME</code>) setup</a>.</li>
</ul>
<h2 id="1-set-up-a-vnc-server"><ol>
<li>Set up a VNC server</li>
</ol></h2>
<p>For demonstration purposes, we will create a TightVNC server on an Ubuntu virtual machine (VM) hosted in Google Cloud Project (GCP). We will configure the VNC server to run XFCE, a lightweight desktop environment suitable for remote access. If you already have a VNC server installed, you can skip this step and <a href="#2-connect-the-server-to-cloudflare">go to Step 2</a>.</p>
<ol>
<li>
<p>Open a terminal window for your Ubuntu VM.</p>
</li>
<li>
<p>Install XFCE and TightVNC by running the following command:</p>
</li>
</ol>
<pre><code class="language-sh">sudo apt update&#10;sudo apt install xfce4 xfce4-goodies dbus-x11 tightvncserver -y&#10;</code></pre>
<pre><code>	This command installs the desktop, some helpful utilities, and the VNC server software.&#10;</code></pre>
<ol start="3">
<li>
<p>To initialize the VNC server:</p>
<ol>
<li>Create a VNC server instance:</li>
</ol>
</li>
</ol>
<pre><code class="language-sh">vncserver&#10;</code></pre>
<pre><code>2. You will be prompted to set a password. This password will be used to connect to your VNC server. It is limited to 8 characters.&#10;&#10;	TightVNC will now create configuration files and start a VNC session on display `:1` (which uses port `5901`).&#10;&#10;3. You will be asked if you want to create a view-only password. You can press `n` for no.&#10;&#10;4. Kill this initial session so that you can edit its configuration:&#10;</code></pre>
<pre><code class="language-sh">vncserver -kill :1&#10;</code></pre>
<ol start="4">
<li>
<p>Configure VNC to launch the XFCE desktop:</p>
<ol>
<li>Create a VNC configuration directory if it is missing:</li>
</ol>
</li>
</ol>
<pre><code class="language-sh">mkdir -p ~/.vnc&#10;</code></pre>
<pre><code>2. Open the `xstartup` file using a text editor. For example,&#10;</code></pre>
<pre><code class="language-sh">vim ~/.vnc/xstartup&#10;</code></pre>
<pre><code>3. Update the file to the following configuration:&#10;</code></pre>
<pre><code class="language-bash">&#35;!/bin/sh&#10;unset SESSION_MANAGER&#10;unset DBUS_SESSION_BUS_ADDRESS&#10;startxfce4&#10;</code></pre>
<pre><code>4. Make the file executable:&#10;</code></pre>
<pre><code class="language-sh">chmod +x ~/.vnc/xstartup&#10;</code></pre>
<ol start="5">
<li>Start the VNC server again:</li>
</ol>
<pre><code class="language-sh">vncserver -localhost :1&#10;</code></pre>
<pre><code>The `-localhost` flag ensures the VNC server only listens for connections from the VM itself, not from the public Internet. Your VNC server is now running on port `5901`, but it is only accessible from `localhost` (`127.0.0.1`) inside the VM.&#10;</code></pre>
<ol start="6">
<li>
<p>(Recommended) Test the VNC server with an existing VNC client to verify any missing packages or configuration changes. For example, to test a VNC server hosted on GCP:</p>
<ol>
<li>
<p>Open a terminal on the client machine.</p>
</li>
<li>
<p>Connect to the VNC server over SSH, forwarding your local port <code>5901</code> to the VNC server's listening port:</p>
</li>
</ol>
</li>
</ol>
<pre><code class="language-sh">gcloud compute ssh [YOUR_VM_NAME] --zone=[YOUR_ZONE] -- -L 5901:localhost:5901&#10;</code></pre>
<pre><code>3. Open your preferred VNC viewer application.&#10;&#10;4. In the VNC viewer, connect to the address `localhost:5901` and enter your VNC server password.&#10;&#10;You should see the Ubuntu VM desktop.&#10;</code></pre>
<ol start="7">
<li>
<p>(Optional) Configure the VNC server to start on boot:</p>
<ol>
<li>Find the full path to the <code>vncserver</code> command:</li>
</ol>
</li>
</ol>
<pre><code class="language-sh">which vncserver&#10;</code></pre>
<pre><code class="language-sh">/usr/bin/vncserver&#10;</code></pre>
<pre><code>2. Create a new service configuration file:&#10;</code></pre>
<pre><code class="language-sh">sudo vim /etc/systemd/system/vncserver@.service&#10;</code></pre>
<pre><code>3. Copy and paste the following content. Replace `[YOUR_USERNAME]` with the VNC server user. If needed, update `/usr/bin/vncserver` to your `vncserver` path.&#10;</code></pre>
<pre><code class="language-toml">[Unit]&#10;Description=Start TightVNC server at startup&#10;After=syslog.target network.target&#10;&#10;[Service]&#10;Type=forking&#10;User=[YOUR_USERNAME]&#10;WorkingDirectory=/home/[YOUR_USERNAME]&#10;&#10;PIDFile=/home/[YOUR_USERNAME]/.vnc/%H:%i.pid&#10;&#10;ExecStartPre=-/usr/bin/vncserver -kill :%i &gt; /dev/null 2&gt;&amp;1&#10;ExecStart=/usr/bin/vncserver -localhost :%i&#10;ExecStop=/usr/bin/vncserver -kill :%i&#10;&#10;[Install]&#10;WantedBy=multi-user.target&#10;</code></pre>
<pre><code>	4. Reload `systemd` to read in the new service file:&#10;</code></pre>
<pre><code class="language-sh">sudo systemctl daemon-reload&#10;</code></pre>
<pre><code>	5. Enable the service to start at boot:&#10;</code></pre>
<pre><code class="language-sh">sudo systemctl enable vncserver@1.service&#10;</code></pre>
<pre><code>	The `1` variable configures the VNC service to use display `:1` (which runs on port `5901`).&#10;&#10;	6. By default, `systemd` user services only run when that user is logged in. To allow your VNC service to start on boot (before you log in), enable user linger for your user:&#10;</code></pre>
<pre><code class="language-sh">sudo loginctl enable-linger [YOUR_USERNAME]&#10;</code></pre>
<pre><code>	7. Start the service:&#10;</code></pre>
<pre><code class="language-sh">sudo systemctl start vncserver@1.service&#10;</code></pre>
<pre><code>	8. Check its status:&#10;</code></pre>
<pre><code class="language-sh">sudo systemctl status vncserver@1.service&#10;</code></pre>
<pre><code>	The VNC server will now start automatically every time the VM boots.&#10;</code></pre>
<h2 id="2-connect-the-server-to-cloudflare"><ol start="2">
<li>Connect the server to Cloudflare</li>
</ol></h2>
<ol>
<li>
<p>Create a Cloudflare Tunnel by following the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">dashboard setup guide</a>.</p>
</li>
<li>
<p>Go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>, then select your tunnel.</p>
</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>
<p>On the <strong>Routes</strong> tab, select <strong>Add route</strong>, then select <strong>Published application</strong>.</p>
</li>
<li>
<p>Choose a domain from the drop-down menu and specify any subdomain (for example, <code>vnc.example.com</code>).</p>
</li>
<li>
<p>For <strong>Service</strong>, select <em>TCP</em> and enter <code>localhost:&lt;5901&gt;</code>. If the VNC server is on a different machine from where you installed the tunnel, enter <code>&lt;SERVER_IP&gt;:5901</code>.</p>
<p>Replace <code>5901</code> with your VNC server's listening port. To determine your VNC listening port, run <code>sudo ss -lnpt</code> and look for <code>vnc</code> in the list of processes.</p>
</li>
<li>
<p>Save the route.</p>
</li>
</ol>
<p>Your VNC server is now ready to accept inbound requests from Cloudflare.</p>
<h2 id="3-create-an-access-application-for-vnc"><ol start="3">
<li>Create an Access application for VNC</li>
</ol></h2>
<p>Create a Cloudflare Access application that users can access through their browser:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Create new application</strong>.</p>
</li>
<li>
<p>Select <strong>Self-hosted and private</strong>.</p>
</li>
<li>
<p>Select <strong>Add public hostname</strong> and enter your published application hostname (<code>vnc.example.com</code>).</p>
</li>
<li>
<p>Turn on <strong>Allow access through browser-based RDP, SSH, or VNC sessions</strong>, then select <em>VNC</em>.</p>
</li>
<li></li>
</ol>
<p>Under <strong>Access policies</strong>, add an existing policy or <a href="/cloudflare-one/access-controls/policies/policy-management/">create a new policy</a> to control who can connect to your application. All Access applications are deny by default -- a user must match an Allow policy before they are granted access.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5255.md")
</aside>
<ol start="7">
<li>Select <strong>Create</strong>.</li>
</ol>
<h2 id="4-connect-as-a-user"><ol start="4">
<li>Connect as a user</li>
</ol></h2>
<p>Users can now access the remote desktop environment directly in their web browser without installing any VNC client software.</p>
<p>To connect to the VNC server:</p>
<ol>
<li>Open a browser and go to the public hostname URL (for example, <code>https://vnc.example.com</code>).</li>
<li>Log in to Cloudflare Access with your configured identity provider.</li>
<li>Enter the VNC server password.</li>
</ol>
<p>You should see the remote VNC server desktop rendered in your browser. All connections are secured through Cloudflare's network, and access is controlled by your Access policies.</p>
