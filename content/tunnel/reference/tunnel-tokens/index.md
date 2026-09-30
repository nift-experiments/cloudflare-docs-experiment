<p>A <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/14860.md")
</div> only requires a token to run. Anyone with the token can run the tunnel.
<h2 id="get-the-token">Get the token</h2>
<p>To get the token for a remotely-managed tunnel:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14863.md")
</div></div>
<h2 id="rotate-a-token">Rotate a token</h2>
<p>Rotate tokens regularly to reduce the risk of compromise. For tunnels with multiple <a href="/tunnel/configuration/#replicas-and-high-availability">replicas</a>, rotate outside working hours and update replicas in batches.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your tunnel.</li>
<li>Select <strong>Rotate token</strong>.
After rotating the token, <code>cloudflared</code> cannot establish new connections with the old token. Existing connectors remain active until restarted.</li>
<li>Select <strong>Add replica</strong> and copy the new <code>cloudflared</code> installation command.</li>
<li>On each replica, reinstall the <code>cloudflared</code> service using the new token:</li>
</ol>
<pre><code class="language-sh">sudo cloudflared service uninstall&#10;sudo cloudflared service install &lt;NEW_TOKEN&gt;&#10;</code></pre>
<details class="nb-details"><summary>Rotate a compromised token</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14864.md")
</div></details>
