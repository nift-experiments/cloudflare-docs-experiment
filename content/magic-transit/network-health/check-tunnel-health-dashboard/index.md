<p>The Cloudflare dashboard monitors the health of all <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10649.md")
</div> tunnels on your account that route traffic from Cloudflare to your origin network.
<p>The dashboard shows the global view of tunnel health as measured from all Cloudflare locations. If the tunnels are healthy on your side, you will see the majority of servers reporting an <strong>up</strong> status. It is normal for a subset of these locations to report tunnel status as degraded or unhealthy, since the Internet is not homogeneous and intermediary path issues between Cloudflare and your network can cause interruptions for specific paths.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10648.md")
</aside>
<p>Not all data centers are relevant to you at all times. You can refer to the <strong>Traffic volume (1 hour)</strong> column to understand if a given data center is receiving traffic for your network, and if its health status is relevant to you.</p>
<h2 id="check-tunnel-health">Check tunnel health</h2>
<ol>
<li>Go to the <strong>Network health</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Connector health</strong> tab.</li>
<li>In this view you can access a list of your tunnels and their current health status. You can also check the amount of health checks passed in the last hour as well as traffic volume for each tunnel.</li>
<li>Find the tunnel you want to inspect, select the three dots next to it, and select:
<ul>
<li><strong>Create alert</strong>: Opens the <a href="/magic-transit/network-health/configure-tunnel-health-alerts/">notifications wizard</a> so you can create specific alerts for that tunnel when specific conditions are met.</li>
<li><strong>Network Analytics</strong>: Opens the Analytics section of the dash, prefiltered with the tunnel you want to inspect.</li>
</ul>
</li>
<li>Alternatively, from the list of tunnels, select the tunnel you want to inspect to access details about it.</li>
</ol>
<h2 id="check-tunnel-health-for-a-specific-tunnel">Check tunnel health for a specific tunnel</h2>
<p>You can drill down into a specific tunnel to check its health status and other information.</p>
<ol>
<li>Go to the <strong>Network health</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select the <strong>Connector health</strong> tab.</p>
</li>
<li>
<p>Find and select the tunnel you want to inspect.</p>
</li>
</ol>
<p>The next view displays detailed information about the tunnel, including:</p>
<ul>
<li>Status information
<ul>
<li>Up: More than 80% of health checks pass.</li>
<li>Degraded: More than 40% of health checks pass.</li>
<li>Down: Less than 40% of health checks pass.</li>
</ul>
</li>
<li>Health checks passed in the last hour</li>
<li>Traffic volume in the last hour</li>
</ul>
<p>If you select the three dots in front of the tunnel you want to inspect, you have access to the following tools:</p>
<ul>
<li>Packet captures: Collect <a href="/cloudflare-network-firewall/packet-captures/">packet level data for your traffic</a></li>
<li>Network Analytics: Leverage real-time insights into <a href="/magic-transit/analytics/network-analytics/">network analytics</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10647.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you received a tunnel health alert but are unsure whether it affects your traffic, refer to <a href="/magic-transit/troubleshooting/connectivity/">Troubleshoot connectivity</a> to determine whether the alert is relevant.</p>
<p>If your tunnels show as unhealthy or degraded, refer to <a href="/magic-transit/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a> for common issues and solutions.</p>
