<p>Follow this step-by-step guide to get your first tunnel up and running using the CLI.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/5381.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you start, make sure you:</p>
<ul>
<li><a href="/fundamentals/manage-domains/add-site/">Add a website to Cloudflare</a>.</li>
<li><a href="/dns/zone-setups/full-setup/setup/">Change your domain nameservers to Cloudflare</a>.</li>
</ul>
<h2 id="1-download-and-install-cloudflared"><ol>
<li>Download and install <code>cloudflared</code></li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5386.md")
</div></div>
<h2 id="2-authenticate-cloudflared"><ol start="2">
<li>Authenticate <code>cloudflared</code></li>
</ol></h2>
<pre><code class="language-sh">cloudflared tunnel login&#10;</code></pre>
<p>Running this command will:</p>
<ul>
<li>Open a browser window and prompt you to log in to your Cloudflare account. After logging in to your account, select your hostname.</li>
<li>Generate an account certificate, the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/local-tunnel-terms/#certpem">cert.pem file</a>, in the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/local-tunnel-terms/#default-cloudflared-directory">default <code>cloudflared</code> directory</a>.</li>
</ul>
<h2 id="3-create-a-tunnel-and-give-it-a-name"><ol start="3">
<li>Create a tunnel and give it a name</li>
</ol></h2>
<pre><code class="language-sh">cloudflared tunnel create &lt;NAME&gt;&#10;</code></pre>
<p>Running this command will:</p>
<ul>
<li>Create a tunnel by establishing a persistent relationship between the name you provide and a UUID for your tunnel. At this point, no connection is active within the tunnel yet.</li>
<li>Generate a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/local-tunnel-terms/#credentials-file">tunnel credentials file</a> in the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/local-tunnel-terms/#default-cloudflared-directory">default <code>cloudflared</code> directory</a>.</li>
<li>Create a subdomain of <code>.cfargotunnel.com</code>.</li>
</ul>
<p>From the output of the command, take note of the tunnel's UUID and the path to your tunnel's credentials file.</p>
<p>Confirm that the tunnel has been successfully created by running:</p>
<pre><code class="language-sh">cloudflared tunnel list&#10;</code></pre>
<h2 id="4-create-a-configuration-file"><ol start="4">
<li>Create a configuration file</li>
</ol></h2>
<ol>
<li>
<p>In your <code>.cloudflared</code> directory, create a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/"><code>config.yml</code> file</a> using any text editor. This file will configure the tunnel to route traffic from a given origin to the hostname of your choice.</p>
</li>
<li>
<p>Add the following fields to the file:</p>
<p>If you are connecting a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">published application</a>:</p>
</li>
</ol>
<pre><code class="language-yml">url: http://localhost:8000&#10;tunnel: &lt;Tunnel-UUID&gt;&#10;credentials-file: /root/.cloudflared/&lt;Tunnel-UUID&gt;.json&#10;</code></pre>
<pre><code>If you are connecting a &lt;a href=&quot;/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/&quot;&gt;private network&lt;/a&gt;:&#10;&#10;&lt;pre&gt;&lt;code class=&quot;language-yml&quot;&gt;`tunnel: &lt;Tunnel-UUID&gt;\ncredentials-file: /root/.cloudflared/&lt;Tunnel-UUID&gt;.json\nwarp-routing:\n  enabled: true`&lt;/code&gt;&lt;/pre&gt;&#10;</code></pre>
<ol start="3">
<li>Confirm that the configuration file has been successfully created by running:</li>
</ol>
<pre><code class="language-sh">cat config.yml&#10;</code></pre>
<h2 id="5-start-routing-traffic"><ol start="5">
<li>Start routing traffic</li>
</ol></h2>
<ol>
<li>To route a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">published application</a> through the tunnel:</li>
</ol>
<pre><code class="language-sh">cloudflared tunnel route dns &lt;UUID or NAME&gt; &lt;hostname&gt;&#10;</code></pre>
<pre><code> This command will create a `CNAME` record pointing to `&lt;UUID&gt;.cfargotunnel.com`.&#10;</code></pre>
<p>2. If you are connecting a private network, route a private IP address or CIDR through the tunnel:</p>
<pre><code class="language-sh">cloudflared tunnel route ip add &lt;IP/CIDR&gt; &lt;UUID or NAME&gt;</code></pre>
<p>3. Confirm that the route has been successfully established:</p>
<pre><code class="language-sh">cloudflared tunnel route ip show</code></pre>
<h2 id="6-run-the-tunnel"><ol start="6">
<li>Run the tunnel</li>
</ol></h2>
<p>Run the tunnel to proxy incoming traffic from the tunnel to any number of services running locally on your origin.</p>
<pre><code class="language-sh">cloudflared tunnel run &lt;UUID or NAME&gt;&#10;</code></pre>
<p>If your configuration file has a custom name or is not in the <code>.cloudflared</code> directory, add the <code>--config</code> flag and specify the path.</p>
<pre><code class="language-sh">cloudflared tunnel --config /path/your-config-file.yml run &lt;UUID or NAME&gt;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5380.md")
</aside>
<h2 id="7-check-the-tunnel"><ol start="7">
<li>Check the tunnel</li>
</ol></h2>
<p>To get information on the tunnel you just created, run:</p>
<pre><code class="language-sh">cloudflared tunnel info &lt;UUID or NAME&gt;&#10;</code></pre>
