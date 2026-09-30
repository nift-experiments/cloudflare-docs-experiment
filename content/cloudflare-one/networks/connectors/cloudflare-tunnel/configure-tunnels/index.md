<p>After <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/">creating your Cloudflare Tunnel</a>, you can configure various aspects of how <code>cloudflared</code> runs and connects your infrastructure to Cloudflare's network. This section covers advanced configuration options to optimize tunnel performance, security, and availability.</p>
<ul class="directory-listing"><li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Tunnel with firewall</a><p>Configure firewall rules to allow `cloudflared` egress traffic while blocking all ingress, implementing a positive security model.
</p></li><li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">Tunnel availability and failover</a><p>Deploy multiple `cloudflared` replicas for high availability and automatic failover across your infrastructure.
</p></li><li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/">Tunnel run parameters</a><p>Modify tunnel service parameters to control how `cloudflared` runs on your system, including logging, connection settings, and protocol options.
</p></li><li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/">Origin parameters</a><p>Reference information for Origin parameters in Zero Trust networking.</p></li><li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/">Tunnel permissions</a><p>Manage tunnel tokens and control who can run your remotely-managed tunnels.
</p></li><li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cipher-suites/">Cipher suites</a><p>Review the TLS cipher suites supported by `cloudflared` for secure connections between your origin and Cloudflare&#x27;s network.
</p></li></ul>
<h2 id="common-configuration-scenarios">Common configuration scenarios</h2>
<h3 id="optimize-for-production">Optimize for production</h3>
<p>For production deployments, consider the following steps:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/">Deploy replicas</a> - Run multiple <code>cloudflared</code> instances for redundancy.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#loglevel">Configure logging</a> - Set appropriate log levels for monitoring and troubleshooting.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/">Review system requirements</a> - Ensure your infrastructure meets performance needs.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Configure firewall rules</a> - Implement egress-only traffic patterns for security.</li>
</ul>
<h3 id="secure-your-tunnel">Secure your tunnel</h3>
<p>All tunnel connections between <code>cloudflared</code> and Cloudflare's network are secured with TLS 1.3 and post-quantum encryption by default, ensuring your traffic is protected against current and future cryptographic threats.</p>
<p>Enhance tunnel security with:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/">Tunnel token management</a> - Control access to your tunnel credentials.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Egress-only firewall rules</a> - Allow only necessary outbound connections.</li>
<li>Least privilege permissions - Run <code>cloudflared</code> as a non-root user with minimal permissions needed for tunnel operation.</li>
</ul>
<h3 id="improve-reliability">Improve reliability</h3>
<p>Maximize tunnel uptime with:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/#cloudflared-replicas">Multiple replicas</a> - Deploy <code>cloudflared</code> across different hosts.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications/">Health alerts</a> - Get notified when your tunnel is degraded or goes down.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#metrics">Health metrics</a> - Monitor tunnel resource usage to identify potential bottlenecks.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/#cloudflare-load-balancers/">Load balancing</a> - Distribute traffic across tunnel connections.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">Automatic failover</a> - Leverage built-in connection redundancy.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/">Monitor your tunnels</a> to track performance and troubleshoot issues.</li>
<li><a href="/cloudflare-one/networks/routes/add-routes/">Configure routes</a> to control how traffic reaches your applications.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">Set up private networks</a> for internal resource access.</li>
</ul>
