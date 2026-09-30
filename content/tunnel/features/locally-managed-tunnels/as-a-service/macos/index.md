<p>You can install <code>cloudflared</code> as a system service on macOS.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you install Cloudflare Tunnel as a service on your OS, follow Steps 1 through 4 of the <a href="/tunnel/features/locally-managed-tunnels/create-local-tunnel/">Tunnel CLI setup guide</a>. At this point you should have a named tunnel and a <code>config.yml</code> file in your <code>$HOME/.cloudflared</code> directory.</p>
<h2 id="1-configure-cloudflared-as-a-service"><ol>
<li>Configure <code>cloudflared</code> as a service</li>
</ol></h2>
<p>By default, Cloudflare Tunnel expects all of the configuration to exist in the <code>$HOME/.cloudflared/config.yml</code> <a href="/tunnel/features/locally-managed-tunnels/configuration-file/">configuration file</a>. At a minimum you must specify the following arguments to run as a service:</p>
<table>
<thead>
<tr>
<th>Argument</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>tunnel</code></td>
<td>The UUID of your tunnel</td>
</tr>
<tr>
<td><code>credentials-file</code></td>
<td>The location of the credentials file for your tunnel</td>
</tr>
</tbody>
</table>
<h2 id="2-run-cloudflared-as-a-service"><ol start="2">
<li>Run <code>cloudflared</code> as a service</li>
</ol></h2>
<p>You can install the service to either run at login or at boot.</p>
<h3 id="run-at-login">Run at login</h3>
<p>Open a terminal window and run the following command:</p>
<pre><code class="language-sh">cloudflared service install&#10;</code></pre>
<p>Cloudflare Tunnel will be installed as a launch agent and start whenever you log in, using your local user configuration found in <code>~/.cloudflared/</code>.</p>
<h3 id="run-at-boot">Run at boot</h3>
<p>Open a terminal window and run the following command:</p>
<pre><code class="language-sh">sudo cloudflared service install&#10;</code></pre>
<p>Cloudflare Tunnel will be installed as a launch daemon and start whenever your system boots, using your configuration found in <code>/etc/cloudflared</code>.</p>
<h2 id="3-manually-start-the-service"><ol start="3">
<li>Manually start the service</li>
</ol></h2>
<p>Run the following command:</p>
<pre><code class="language-sh">sudo launchctl start com.cloudflare.cloudflared&#10;</code></pre>
<p>The output will be logged to <code>/Library/Logs/com.cloudflare.cloudflared.err.log</code> and <code>/Library/Logs/com.cloudflare.cloudflared.out.log</code>.</p>
<h2 id="next-steps">Next steps</h2>
<p>You can now <a href="/tunnel/features/locally-managed-tunnels/create-local-tunnel/#5-start-routing-traffic">route traffic through your tunnel</a>. If you add IP routes or otherwise change the configuration, restart the service to load the new configuration:</p>
<pre><code class="language-sh">sudo launchctl stop com.cloudflare.cloudflared&#10;sudo launchctl start com.cloudflare.cloudflared&#10;</code></pre>
