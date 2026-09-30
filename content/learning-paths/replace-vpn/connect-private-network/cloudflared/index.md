<p>Cloudflare Tunnel is an outbound-only daemon service that can run on nearly any host machine and proxies local traffic once validated from the Cloudflare network. User traffic initiated from the Cloudflare One Client onramps to Cloudflare, passes down your Cloudflare Tunnel connections, and terminates automatically in your local network. Traffic reaching your internal applications or services will carry the local source IP address of the host machine running the <code>cloudflared</code> daemon.</p>
<h2 id="create-a-tunnel">Create a tunnel</h2>
<p>To connect your private network:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9904.md")
</div></div>
<p>All internal applications and services in this IP range are now connected to Cloudflare.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9894.md")
</aside>
<h2 id="best-practices">Best practices</h2>
<ul>
<li>Segregate production and staging traffic among different Cloudflare tunnels.</li>
<li>Add a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/"><code>cloudflared</code> replica</a> to another host machine for an additional point of availability.</li>
<li>Distribute access to critical services (for example, private DNS, Active Directory, and other critical systems) across different tunnels for blast-radius reduction in the event of a server-side outage.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications/">Enable notifications</a> in the Cloudflare dashboard to monitor tunnel health.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/">Monitor performance metrics</a> to identify potential bottlenecks.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/update-cloudflared/">Update <code>cloudflared</code></a> regularly.</li>
</ul>
