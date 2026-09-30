<h2 id="error-1002-dns-points-to-prohibited-ip">Error 1002: DNS points to prohibited IP</h2>
<p>This error occurs when you proxy a private IP address without the necessary entitlement. Contact your account team to request access.</p>
<h2 id="setting-seems-off-but-traffic-routes-through-tunnel">Setting seems off but traffic routes through tunnel</h2>
<p>Check for other records on the same name.</p>
<p>Private network routing applies per name, not per record. If you have multiple <code>A</code> or <code>AAAA</code> records on the same name and at least one of them has private network routing enabled, all records on that name will use private network routing.</p>
<h2 id="traffic-not-reaching-origin">Traffic not reaching origin</h2>
<p>If traffic is not reaching your private origin:</p>
<ol>
<li>Verify your tunnel is active and healthy in the Cloudflare dashboard.</li>
<li>Confirm the origin IP is routable within your private network.</li>
<li>Check that <code>private_routing</code> is set to <code>true</code> on the DNS record.</li>
<li>Verify the record has proxy status enabled.</li>
</ol>
<h2 id="connection-timeouts-from-clients">Connection timeouts from clients</h2>
<p>Cloudflare Source IP is set to a public range. Set it to a private <code>/12</code>. Refer to <a href="/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">Configure Cloudflare source IPs</a>.</p>
<h2 id="request-times-out-with-no-response-on-the-origin">Request times out with no response on the origin</h2>
<p>The network where your origin lives has no return route for the Cloudflare Source IP range. Add a route that sends that range back through the tunnel.</p>
<h2 id="tunnel-shows-ike-established-but-health-checks-fail">Tunnel shows IKE established but health checks fail</h2>
<p>ICMP is blocked on the path or the health check is misconfigured. Allow ICMP between the tunnel endpoints and confirm the health check direction is <code>bidirectional</code> and type is <code>reply</code>.</p>
<h2 id="traffic-tries-to-route-over-the-public-internet">Traffic tries to route over the public Internet</h2>
<p>The <strong>Use private network routing</strong> toggle is not turned on for the DNS record. Edit the record and turn the toggle on. Refer to <a href="/dns/private-origins/private-network-routing/">Private network routing</a> for dashboard and API steps.</p>
