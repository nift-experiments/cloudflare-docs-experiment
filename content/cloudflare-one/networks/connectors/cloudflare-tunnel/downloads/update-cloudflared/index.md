<p>Updates will cause <code>cloudflared</code> to restart which will impact traffic currently being served. You can perform zero-downtime upgrades by using Cloudflare's <a href="#update-with-cloudflare-load-balancer">Load Balancer product</a> or by using <a href="#update-with-multiple-cloudflared-instances">multiple <code>cloudflared</code> instances</a>.</p>
<h2 id="update-the-cloudflared-service">Update the <code>cloudflared</code> service</h2>
<p>Refer to the following commands to update <code>cloudflared</code> for a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5306.md")
</div> or a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/5307.md")
</div>. Locally-managed tunnels must be set up to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/">run as a service</a> for the following commands to execute successfully.
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5314.md")
</div></div>
<h2 id="update-with-cloudflare-load-balancer">Update with Cloudflare Load Balancer</h2>
<p>You can update <code>cloudflared</code> without downtime by using Cloudflare's Load Balancer product with your Cloudflare Tunnel deployment.</p>
<ol>
<li>Install a new instance of <code>cloudflared</code> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/">create</a> a new Tunnel.</li>
<li>Configure the instance to point traffic to the same locally-available service as your current, active instance of <code>cloudflared</code>.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/public-load-balancers/">Add the address</a> of the new instance of <code>cloudflared</code> into your Load Balancer pool as priority 2.</li>
<li>Swap the priority such that the new instance is now priority 1 and monitor to confirm traffic is being served.</li>
<li>Once confirmed, you can remove the older version from the Load Balancer pool.</li>
</ol>
<h2 id="update-with-multiple-cloudflared-instances">Update with multiple <code>cloudflared</code> instances</h2>
<p>If you are not using Cloudflare's Load Balancer, you can use multiple instances of <code>cloudflared</code> to update without the risk of downtime.</p>
<ol>
<li>Install a new instance of <code>cloudflared</code> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/">create</a> a new Tunnel.</li>
<li>Configure the instance to point traffic to the same locally-available service as your current, active instance of <code>cloudflared</code>.</li>
<li>In the Cloudflare DNS dashboard, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/dns/">replace</a> the address of the current instance of <code>cloudflared</code> with the address of the new instance. Save the record.</li>
<li>Remove the now-inactive instance of <code>cloudflared</code>.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="traffic-handling">Traffic handling</h3>
@markup("md", "content/.markup/bodies/5304.md")
</aside>
<h3 id="run-multiple-instances-in-windows">Run multiple instances in Windows</h3>
<p>Windows systems require services to have a unique name and display name. You can run multiple instances of <code>cloudflared</code> by creating <code>cloudflared</code> services with unique names.</p>
<ol>
<li>Install and configure <code>cloudflared</code>.</li>
<li>Next, create a service with a unique name and point to the <code>cloudflared</code> executable and configuration file.</li>
</ol>
<pre><code class="language-powershell">sc.exe create &lt;unique-name&gt; binPath=&#x27;&lt;path-to-exe&gt;&#x27; --config &#x27;&lt;path-to-config&gt;&#x27; displayname=&quot;Unique Name&quot;&#10;</code></pre>
<ol start="3">
<li>
<p>Proceed to create additional services with unique names.</p>
</li>
<li>
<p>You can now start each unique service.</p>
</li>
</ol>
<pre><code class="language-powershell">sc.exe start &lt;unique-name&gt;&#10;</code></pre>
