<p>You can install <code>cloudflared</code> as a system service on Linux.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you install Cloudflare Tunnel as a service on Linux, follow Steps 1 through 4 of the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/">Tunnel CLI setup guide</a>. At this point you should have a named tunnel and a <code>config.yml</code> file in your <code>.cloudflared</code> directory.</p>
<h2 id="1-configure-cloudflared-as-a-service"><ol>
<li>Configure <code>cloudflared</code> as a service</li>
</ol></h2>
<p>By default, Cloudflare Tunnel expects all of the configuration to exist in the <code>$HOME/.cloudflared/config.yml</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/">configuration file</a>. At a minimum you must specify the following arguments to run as a service:</p>
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
<td>The location of the credentials file for your Tunnel</td>
</tr>
</tbody>
</table>
<h2 id="2-run-cloudflared-as-a-service"><ol start="2">
<li>Run <code>cloudflared</code> as a service</li>
</ol></h2>
<ol>
<li>Install the <code>cloudflared</code> service.</li>
</ol>
<pre><code class="language-sh">cloudflared service install&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5390.md")
</aside>
<ol start="2">
<li>Start the service.</li>
</ol>
<pre><code class="language-sh">systemctl start cloudflared&#10;</code></pre>
<ol start="3">
<li>(Optional) View the status of the service.</li>
</ol>
<pre><code class="language-sh">systemctl status cloudflared&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>You can now <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/#5-start-routing-traffic">route traffic through your tunnel</a>. If you add IP routes or otherwise change the configuration, restart the service to load the new configuration:</p>
<pre><code class="language-sh">systemctl restart cloudflared&#10;</code></pre>
