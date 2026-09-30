<p>This guide helps you diagnose and resolve common tunnel health issues with Cloudflare WAN. Tunnel health checks monitor your GRE and IPsec tunnel endpoints (also called connectors in the Cloudflare dashboard) and steer traffic to the best available routes.</p>
<h2 id="quick-diagnostic-checklist">Quick diagnostic checklist</h2>
<p>Use the following table to match your symptom to the most likely cause and first action:</p>
<table>
<thead>
<tr>
<th align="left">Symptom</th>
<th align="left">Most likely cause</th>
<th align="left">First action</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Tunnel shows Down, never becomes healthy</td>
<td align="left">Configuration mismatch or firewall blocking IKE</td>
<td align="left">Check IPsec parameters and firewall rules. Refer to <a href="#ipsec-tunnel-establishment-failures">IPsec tunnel establishment failures</a>.</td>
</tr>
<tr>
<td align="left">Dashboard shows &quot;100% degraded&quot; for some colos</td>
<td align="left">Normal — this is a state indicator, not packet loss</td>
<td align="left">Check if affected colos carry your traffic. Refer to <a href="#understanding-degraded-status-in-the-dashboard">Understanding degraded status</a>.</td>
</tr>
<tr>
<td align="left">Tunnel flaps between healthy and unhealthy</td>
<td align="left">Anti-replay protection or rekey disruption</td>
<td align="left">Disable anti-replay protection on your router. Refer to <a href="#ipsec-tunnel-instability-or-packet-drops">IPsec tunnel instability</a>.</td>
</tr>
<tr>
<td align="left">Health checks fail but traffic flows normally</td>
<td align="left">Stateful firewall dropping health check probes</td>
<td align="left">Change health check type from <em>Reply</em> to <em>Request</em>. Refer to <a href="#tunnel-shows-down-but-traffic-is-flowing">Tunnel shows Down but traffic is flowing</a>.</td>
</tr>
<tr>
<td align="left">Health checks fail on policy-based VPN tunnels</td>
<td align="left">Reply health checks fall outside tunnel traffic selectors</td>
<td align="left">Use Request-style health checks with a loopback target. Refer to <a href="#policy-based-vpn-health-check-failures">Policy-based VPN health check failures</a>.</td>
</tr>
<tr>
<td align="left">All tunnels degraded or down in a specific region</td>
<td align="left">Network path issue between that region and your network</td>
<td align="left">Check ISP connectivity. Use traceroute or MTR from your tunnel endpoint toward Cloudflare.</td>
</tr>
<tr>
<td align="left">All tunnels degraded or down globally</td>
<td align="left">Issue at your network edge</td>
<td align="left">Check your tunnel endpoint router and upstream connectivity.</td>
</tr>
</tbody>
</table>
<h3 id="what-you-can-check">What you can check</h3>
<ul>
<li><strong>Dashboard</strong>: Tunnel health status per data center and traffic volume per tunnel (Go to <strong>Insights</strong> &gt; <strong>Network health</strong> &gt; <strong>Network health</strong>)</li>
<li><strong>API</strong>: Tunnel health status via the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/tunnel-health-checks/">Cloudflare WAN tunnel health API</a></li>
<li><strong>Network Analytics</strong>: Traffic volume, packet counts, and protocol distribution through <a href="/cloudflare-one/networks/connectors/cloudflare-wan/analytics/network-analytics/">Network Analytics</a></li>
<li><strong>From your network</strong>: Traceroute and MTR from your tunnel endpoint toward Cloudflare. Since Cloudflare endpoints use anycast, this tests the path to the nearest data center only. To test specific regions, use the <a href="/api/resources/diagnostics/subresources/traceroutes/methods/create/">Cloudflare Traceroute API</a> to run traceroutes from specific Cloudflare locations to your network.</li>
</ul>
<h3 id="what-you-cannot-check-current-limitations">What you cannot check (current limitations)</h3>
<ul>
<li>Correlation between tunnel health events and Cloudflare network incidents</li>
<li>Per-packet forwarding decisions (which data center forwarded which packet through which tunnel)</li>
<li>Historical health check probe data beyond the dashboard retention period</li>
</ul>
<h3 id="common-fixes-checklist">Common fixes checklist</h3>
<p>If you are experiencing tunnel health issues, check these items first:</p>
<ol>
<li><strong>Health check type</strong>: If using a stateful firewall (such as Palo Alto Networks, Check Point, Cisco, or Fortinet), change health check type from <em>Reply</em> to <em>Request</em>.</li>
<li><strong>Anti-replay protection</strong>: Disable anti-replay protection on your router, or set the replay window to <code>0</code>.</li>
<li><strong>MTU settings</strong>: Verify MTU is set correctly (typically <code>1476</code> for GRE, <code>1400</code>-<code>1450</code> for IPsec).</li>
<li><strong>IPsec parameters</strong>: Confirm your cryptographic parameters match <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/gre-ipsec-tunnels/#supported-configuration-parameters">Cloudflare's supported configuration</a>.</li>
<li><strong>Health check direction</strong>: Cloudflare WAN defaults to <p><em>Bidirectional</em></p>
.</li>
<li><strong>Cloudflare Network Firewall rules (less common)</strong>: Ensure ICMP traffic from <a href="https://cloudflare.com/ips/">Cloudflare IP addresses</a> is allowed.</li>
</ol>
<hr />
<h2 id="tunnel-health-states">Tunnel health states</h2>
<p>The <a href="https://dash.cloudflare.com/?to=/:account/networking-insights/health">Network health</a> page in the Cloudflare dashboard displays three tunnel health states:</p>
<table>
<thead>
<tr>
<th align="left">State</th>
<th align="left">Dashboard display</th>
<th align="left">Technical threshold</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Healthy</strong></td>
<td align="left">More than 80% of health checks pass</td>
<td align="left">Less than 0.1% failure rate</td>
</tr>
<tr>
<td align="left"><strong>Degraded</strong></td>
<td align="left">Between 40% and 80% of health checks pass</td>
<td align="left">At least 0.1% failures in last five minutes (minimum two failures)</td>
</tr>
<tr>
<td align="left"><strong>Down</strong></td>
<td align="left">Less than 40% of health checks pass</td>
<td align="left">All health checks failed (at least three samples in last second)</td>
</tr>
</tbody>
</table>
<p>The dashboard shows tunnel health as measured from each Cloudflare data center where your traffic lands. It is normal to see some locations reporting degraded status due to Internet path issues. Focus on locations that show traffic in the <strong>Traffic volume (1h)</strong> column.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="probe-retry-behavior">Probe retry behavior</h3>
@markup("md", "content/.markup/bodies/6728.md")
</aside>
<h3 id="understanding-degraded-status-in-the-dashboard">Understanding degraded status in the dashboard</h3>
<p>The tunnel health dashboard reports health state per data center per tunnel. Each Cloudflare data center independently tracks the health of each tunnel.</p>
<p>A common source of confusion is seeing &quot;100% degraded&quot; in the dashboard and misinterpreting it as 100% packet loss. Note that these are different.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="100-degraded-is-a-state-not-a-packet-loss-percentage">100% degraded is a state, not a packet loss percentage</h3>
@markup("md", "content/.markup/bodies/6727.md")
</aside>
<p><strong>How degraded state is triggered:</strong></p>
<p>When a health check probe fails, Cloudflare sends two additional probes. If some probes succeed and some fail, the tunnel enters degraded state for that data center. A few seconds of intermittent packet loss is enough to trigger this transition.</p>
<p><strong>What to check:</strong></p>
<p>Focus on data centers that show traffic in the <strong>Traffic volume (1h)</strong> column. A data center showing degraded status with zero or minimal traffic is informational — it indicates a path issue between that specific Cloudflare data center and your network, but it does not affect your traffic if no traffic routes through that data center.</p>
<p><strong>Recovery timing:</strong></p>
<p>Tunnels remain in degraded state for at least five minutes, even if health checks start succeeding immediately. Recovery from degraded to healthy requires consistently passing health checks over a sustained period and can take up to 30 minutes. For details on how tunnels transition between states, refer to <a href="#recovery-behavior">Recovery behavior</a> below.</p>
<h3 id="routing-priority-penalties">Routing priority penalties</h3>
<p>When a tunnel becomes unhealthy, Cloudflare applies priority penalties to routes through that tunnel:</p>
<ul>
<li><strong>Degraded</strong>: Adds <code>500,000</code> to route priority</li>
<li><strong>Down</strong>: Adds <code>1,000,000</code> to route priority</li>
</ul>
<p>These penalties shift traffic to healthier tunnels while maintaining redundancy. Cloudflare never completely removes routes, preserving failover options even when all tunnels are unhealthy.</p>
<h3 id="recovery-behavior">Recovery behavior</h3>
<p>Tunnels transition between states asymmetrically to prevent flapping:</p>
<ul>
<li><strong>Healthy to Degraded/Down</strong>: Transitions quickly when failures are detected. A tunnel can go directly from Healthy to Down if all probe retries fail.</li>
<li><strong>Down to Degraded</strong>: Requires three consecutive successful health check probes.</li>
<li><strong>Degraded to Healthy</strong>: Requires failure rate below 0.1% over 30 consecutive probes.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="minimum-state-duration">Minimum state duration</h3>
@markup("md", "content/.markup/bodies/6726.md")
</aside>
<p>For instructions on monitoring tunnel status, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/">Check tunnel health in the dashboard</a>.</p>
<h3 id="health-check-types-and-directions">Health check types and directions</h3>
<p><strong>Health check type:</strong></p>
<table>
<thead>
<tr>
<th align="left">Type</th>
<th align="left">Behavior</th>
<th align="left">When to use</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Reply</strong> (default)</td>
<td align="left">Cloudflare sends an ICMP reply packet</td>
<td align="left">Simple networks without stateful firewalls</td>
</tr>
<tr>
<td align="left"><strong>Request</strong></td>
<td align="left">Cloudflare sends an ICMP echo request</td>
<td align="left">Networks with stateful firewalls (recommended for most deployments)</td>
</tr>
</tbody>
</table>
<p><strong>Health check direction:</strong></p>
<table>
<thead>
<tr>
<th align="left">Direction</th>
<th align="left">Behavior</th>
<th align="left">Default for</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Bidirectional</strong></td>
<td align="left">Probe and response both traverse the tunnel</td>
<td align="left">Cloudflare WAN (formerly Magic WAN)</td>
</tr>
<tr>
<td align="left"><strong>Unidirectional</strong></td>
<td align="left">Probe traverses tunnel; response returns via Internet</td>
<td align="left">Magic Transit (direct server return)</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6725.md")
</aside>
<hr />
<h2 id="resolve-common-issues">Resolve common issues</h2>
<h3 id="tunnel-shows-down-but-traffic-is-flowing">Tunnel shows <code>Down</code> but traffic is flowing</h3>
<h4 id="symptoms">Symptoms</h4>
<ul>
<li>Dashboard shows tunnel as <code>Down</code> or <code>Degraded</code></li>
<li>Actual user traffic passes through the tunnel successfully</li>
<li>Health check failure rate is 100% despite working connectivity</li>
</ul>
<h4 id="cause">Cause</h4>
<p>Stateful firewalls (such as Palo Alto Networks, Check Point, Cisco, and Fortinet) drop the health check packets. By default, Cloudflare sends ICMP <em>Reply</em> packets as health check probes.</p>
<p>Stateful firewalls inspect these packets and look for a matching ICMP <em>Request</em> in their session table. When no matching request exists, firewalls drop the reply as &quot;out-of-state&quot;.</p>
<h4 id="solution">Solution</h4>
<p>Change the health check type from <em>Reply</em> to <em>Request</em>:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>IPsec/GRE tunnels</strong>, select <strong>Edit</strong> on the affected tunnel.</li>
<li>Under <strong>Health check type</strong>, change from <em>Reply</em> to <em>Request</em>.</li>
<li>Select <strong>Update tunnel</strong>.</li>
</ol>
<p>When you use <em>Request</em> style health checks, Cloudflare sends an ICMP echo request. Your firewall's stateful inspection engine recognizes this as a legitimate request and automatically permits the ICMP reply response.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6724.md")
</aside>
<hr />
<h3 id="health-check-failures-with-cloudflare-network-firewall">Health check failures with Cloudflare Network Firewall</h3>
<h4 id="symptoms-1">Symptoms</h4>
<ul>
<li>Tunnels were healthy before enabling Cloudflare Network Firewall</li>
<li>After adding Cloudflare Network Firewall rules, health checks fail</li>
<li>Blocking ICMP traffic causes immediate health check failures</li>
</ul>
<h4 id="cause-1">Cause</h4>
<p>Cloudflare Network Firewall processes all traffic, including Cloudflare's health check probes. If you create a rule that blocks ICMP traffic, you also block the health check packets that Cloudflare sends to monitor tunnel status.</p>
<h4 id="solution-1">Solution</h4>
<p>Add an allow rule for ICMP traffic from Cloudflare IP addresses <em>before</em> any block rules:</p>
<ol>
<li>Go to the <strong>Firewall policies</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Create a new policy with the following parameters:</li>
</ol>
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Action</strong></td>
<td align="left">Allow</td>
</tr>
<tr>
<td align="left"><strong>Protocol</strong></td>
<td align="left">ICMP</td>
</tr>
<tr>
<td align="left"><strong>Source</strong></td>
<td align="left"><a href="https://cloudflare.com/ips/">Cloudflare IP ranges</a></td>
</tr>
</tbody>
</table>
<ol start="3">
<li>Position this rule <em>before</em> any rules that block ICMP traffic.</li>
</ol>
<p>For more information, refer to <a href="/cloudflare-network-firewall/about/ruleset-logic/#cloudflare-network-firewall-rules-and-magic-transit-endpoint-health-checks">Cloudflare Network Firewall rules and endpoint health checks</a>.</p>
<hr />
<h3 id="ipsec-tunnel-instability-or-packet-drops">IPsec tunnel instability or packet drops</h3>
<h4 id="symptoms-2">Symptoms</h4>
<ul>
<li>IPsec tunnel frequently flaps between healthy and down states</li>
<li>Intermittent packet loss on the tunnel</li>
<li>Traffic works for a period then stops without configuration changes</li>
<li>Router logs show packets dropped due to:
<ul>
<li>&quot;replay check failed&quot;</li>
<li>&quot;invalid sequence number&quot;</li>
<li>&quot;invalid SPI&quot; (Security Parameter Index)</li>
</ul>
</li>
</ul>
<h4 id="cause-2">Cause</h4>
<p>Anti-replay protection is enabled on your router. IPsec anti-replay protection expects packets to arrive in sequence from a single sender.</p>
<p>Cloudflare's anycast architecture means your tunnel traffic can originate from thousands of servers across hundreds of data centers. Each server maintains its own sequence counter, causing packets to arrive out-of-order from your router's perspective.</p>
<h4 id="solution-2">Solution</h4>
<p>Disable anti-replay protection on your router:</p>
<p><strong>For most routers:</strong></p>
<p>Locate the anti-replay or replay protection setting in your IPsec configuration and disable it.</p>
<p><strong>If you can only set a replay window size:</strong></p>
<p>Set the replay window to <code>0</code> to effectively disable the check.</p>
<p><strong>For devices that do not support disabling anti-replay:</strong></p>
<p>Enable replay protection in the Cloudflare dashboard. This routes all tunnel traffic through a single server, maintaining proper sequence numbers at the cost of losing anycast benefits.</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>IPsec/GRE tunnels</strong>, select <strong>Edit</strong> on your IPsec tunnel.</li>
<li>Enable <strong>Replay protection</strong>.</li>
<li>Select <strong>Update tunnel</strong>.</li>
</ol>
<p><strong>For Cisco IOS/IOS-XE routers experiencing &quot;invalid SPI&quot; errors:</strong></p>
<p>Enable ISAKMP invalid SPI recovery to help the router resynchronize Security Associations:</p>
<pre><code class="language-txt">configure terminal&#10;crypto isakmp invalid-spi-recovery&#10;exit&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6723.md")
</aside>
<p>For a detailed explanation of why this setting is necessary, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/anti-replay-protection/">Anti-replay protection</a>.</p>
<hr />
<h3 id="tunnel-degraded-after-rekey-events">Tunnel degraded after rekey events</h3>
<h4 id="symptoms-3">Symptoms</h4>
<ul>
<li>Tunnel health drops to <code>Degraded</code> or <code>Down</code> periodically</li>
<li>Issues coincide with IPsec rekey intervals (typically every few hours)</li>
<li>Tunnel recovers automatically after 1-3 minutes</li>
<li>Router logs show successful rekey completion</li>
</ul>
<h4 id="cause-3">Cause</h4>
<p>When your tunnel endpoint initiates an IPsec rekey, new Security Associations (SAs) must propagate across Cloudflare's network. Rekey propagation delays have been significantly reduced and are uncommon in most deployments. However, brief tunnel degradation during rekeys can still occur in some configurations.</p>
<p>Cloudflare never initiates rekey — only responds. All rekey attempts must come from your tunnel endpoint. If your device receives a TEMPORARY_FAILURE response during rekey, it must re-establish the IKE session to recover.</p>
<h4 id="solution-3">Solution</h4>
<p>This behavior is expected and the tunnel will automatically recover. To minimize impact:</p>
<ol>
<li>
<p><strong>Configure Dead Peer Detection (DPD) with restart</strong>: Set your tunnel endpoint's DPD action to &quot;restart&quot; so it automatically re-establishes the IKE session if a rekey fails with TEMPORARY_FAILURE. Without DPD restart, the device can get stuck in a loop of failed rekeys.</p>
</li>
<li>
<p><strong>Increase rekey intervals</strong>: Configure longer SA lifetimes on your tunnel endpoint to reduce rekey frequency. Common values are 8-24 hours for IKE SA and 1-8 hours for IPsec SA.</p>
</li>
<li>
<p><strong>Adjust health check sensitivity</strong>: If brief degradation during rekeys triggers alerts, consider lowering the health check rate:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>In <strong>IPsec/GRE tunnels</strong>, select <strong>Edit</strong> on the tunnel.</p>
</li>
<li>
<p>Change <strong>Health check rate</strong> to <em>Low</em>.</p>
</li>
<li>
<p><strong>Stagger rekey times</strong>: If you have multiple tunnels, configure different SA lifetimes so they do not rekey simultaneously.</p>
</li>
</ol>
<hr />
<h3 id="bidirectional-health-check-failures">Bidirectional health check failures</h3>
<h4 id="symptoms-4">Symptoms</h4>
<ul>
<li>Health checks configured as bidirectional fail consistently</li>
<li>Unidirectional health checks work correctly</li>
<li>Traffic flows through the tunnel normally</li>
</ul>
<h4 id="cause-4">Cause</h4>
<p>Bidirectional health checks require both the probe and response to traverse the tunnel. Your router must:</p>
<ol>
<li>Accept ICMP packets destined for the tunnel interface IP addresses</li>
<li>Route the ICMP response back through the tunnel to Cloudflare</li>
</ol>
<p>If traffic selectors or firewall rules do not permit this traffic, bidirectional health checks fail.</p>
<h4 id="solution-4">Solution</h4>
<p><strong>For IPsec tunnels:</strong></p>
<p>Configure traffic selectors to accept packets for the tunnel interface addresses. For example, if your tunnel interface address is <code>10.252.2.27/31</code>:</p>
<ul>
<li>Permit traffic to/from <code>10.252.2.26</code> (Cloudflare side)</li>
<li>Permit traffic to/from <code>10.252.2.27</code> (your side)</li>
</ul>
<p><strong>For all tunnel types:</strong></p>
<p>Ensure your firewall permits ICMP traffic on the tunnel interface. Many firewalls require explicit rules to allow management traffic (including ping) on tunnel interfaces.</p>
<p>For detailed information on how bidirectional health checks work, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/tunnel-health-checks/">Tunnel health checks</a>.</p>
<hr />
<h3 id="ipsec-tunnel-establishment-failures">IPsec tunnel establishment failures</h3>
<h4 id="symptoms-5">Symptoms</h4>
<ul>
<li>Tunnel status shows <code>Down</code> and never becomes healthy</li>
<li>No traffic passes through the tunnel</li>
<li>Router logs show IKE negotiation failures</li>
</ul>
<h4 id="cause-5">Cause</h4>
<p>IPsec tunnel establishment can fail due to several configuration mismatches:</p>
<table>
<thead>
<tr>
<th align="left">Issue</th>
<th align="left">Symptom</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Crypto parameter mismatch</strong></td>
<td align="left">IKE negotiation fails with &quot;no proposal chosen&quot;</td>
</tr>
<tr>
<td align="left"><strong>Incorrect PSK</strong></td>
<td align="left">Authentication failures in Phase 1</td>
</tr>
<tr>
<td align="left"><strong>Wrong IKE ID format</strong></td>
<td align="left">Authentication failures despite correct PSK</td>
</tr>
<tr>
<td align="left"><strong>Firewall blocking IKE</strong></td>
<td align="left">No IKE traffic reaches Cloudflare</td>
</tr>
</tbody>
</table>
<h4 id="solution-5">Solution</h4>
<ol>
<li>
<p><strong>Verify crypto parameters match Cloudflare's supported configuration:</strong></p>
<p><strong>Phase 1 (IKE)</strong></p>
</li>
</ol>
<table>
<thead>
<tr>
<th align="left">Parameter</th>
<th align="left">Supported values</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">IKE version</td>
<td align="left">IKEv2 only</td>
</tr>
<tr>
<td align="left">Encryption</td>
<td align="left">AES-GCM-16, AES-CBC-256</td>
</tr>
<tr>
<td align="left">Authentication</td>
<td align="left">SHA-256, SHA-384, SHA-512</td>
</tr>
<tr>
<td align="left">DH Group</td>
<td align="left">DH group 14, 15, 16, 19, 20</td>
</tr>
</tbody>
</table>
<p><strong>Phase 2 (IPsec)</strong></p>
<table>
<thead>
<tr>
<th align="left">Parameter</th>
<th align="left">Supported values</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Encryption</td>
<td align="left">AES-GCM-16, AES-CBC-256</td>
</tr>
<tr>
<td align="left">Authentication</td>
<td align="left">SHA-256, SHA-512</td>
</tr>
<tr>
<td align="left">PFS Group</td>
<td align="left">DH group 14, 15, 16, 19, 20</td>
</tr>
</tbody>
</table>
<ol start="2">
<li>
<p><strong>Verify the Pre-Shared Key (PSK):</strong></p>
<ul>
<li>Regenerate the PSK in the Cloudflare dashboard</li>
<li>Copy the new PSK exactly (no extra spaces or characters)</li>
<li>Update your router with the new PSK</li>
</ul>
</li>
<li>
<p><strong>Check the IKE ID format:</strong> Cloudflare uses FQDN format for the IKE ID. Ensure your router is configured to accept an FQDN peer identity. The FQDN is displayed in the tunnel details in the Cloudflare dashboard.</p>
</li>
<li>
<p><strong>Verify firewall rules:</strong> Ensure your edge firewall permits:</p>
<ul>
<li>UDP port <code>500</code> (IKE)</li>
<li>UDP port <code>4500</code> (IKE NAT-T)</li>
<li>IP protocol <code>50</code> (ESP)</li>
</ul>
</li>
</ol>
<p>For the complete list of supported parameters, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/gre-ipsec-tunnels/#supported-configuration-parameters">Supported configuration parameters</a>.</p>
<hr />
<h3 id="policy-based-vpn-health-check-failures">Policy-based VPN health check failures</h3>
<h4 id="symptoms-6">Symptoms</h4>
<ul>
<li>Health checks fail consistently on policy-based IPsec tunnels</li>
<li>Traffic matching the tunnel's traffic selectors (encryption domain) flows normally</li>
<li>Route-based tunnels on the same device work correctly</li>
</ul>
<h4 id="cause-6">Cause</h4>
<p>Policy-based IPsec tunnels use traffic selectors to define which prefixes are permitted in the tunnel. Reply-style health checks are self-addressed to Cloudflare IP addresses. These addresses fall outside the tunnel's traffic selectors (which only permit customer network destinations), so the tunnel endpoint drops the health check packets.</p>
<p>Additionally, some firewalls (such as Check Point) may flag Reply-style health check packets as spoofed due to their self-addressed nature, even on route-based tunnels.</p>
<h4 id="solution-6">Solution</h4>
<ol>
<li>Change the health check type from <em>Reply</em> to <em>Request</em>.</li>
<li>Configure a loopback address on your tunnel endpoint as the health check target. The target must be:
<ul>
<li>Routable from the tunnel endpoint</li>
<li>Covered by the tunnel's traffic selectors (encryption domain)</li>
</ul>
</li>
<li>For bidirectional health checks, ensure the health check source (the tunnel Interface Address configured in the Cloudflare dashboard) is also covered by a traffic selector.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6722.md")
</aside>
<hr />
<h2 id="vendor-specific-guidance">Vendor-specific guidance</h2>
<h3 id="common-vendor-specific-issues">Common vendor-specific issues</h3>
<table>
<thead>
<tr>
<th align="left">Vendor</th>
<th align="left">Common issue</th>
<th align="left">Solution</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Palo Alto Networks</strong></td>
<td align="left">Health checks fail with default settings</td>
<td align="left">Change health check type to <em>Request</em>; disable anti-replay</td>
</tr>
<tr>
<td align="left"><strong>Cisco Meraki</strong></td>
<td align="left">Cannot disable anti-replay</td>
<td align="left">Enable replay protection in Cloudflare dashboard</td>
</tr>
<tr>
<td align="left"><strong>AWS VPN Gateway</strong></td>
<td align="left">Cannot disable anti-replay</td>
<td align="left">Enable replay protection in Cloudflare dashboard</td>
</tr>
<tr>
<td align="left"><strong>VeloCloud</strong></td>
<td align="left">Cannot disable anti-replay</td>
<td align="left">Enable replay protection in Cloudflare dashboard</td>
</tr>
<tr>
<td align="left"><strong>Check Point</strong></td>
<td align="left">Out-of-state packet drops</td>
<td align="left">Change health check type to <em>Request</em></td>
</tr>
</tbody>
</table>
<hr />
<h2 id="gather-information-for-support">Gather information for support</h2>
<p>If you have worked through this guide and still experience tunnel health issues, gather the following information before contacting Cloudflare support:</p>
<h3 id="required-information">Required information</h3>
<ol>
<li><strong>Account ID</strong> and <strong>Tunnel name(s)</strong> affected</li>
<li><strong>Timestamps</strong> (in UTC) when the issue occurred</li>
<li><strong>Tunnel configuration details:</strong>
<ul>
<li>Tunnel type (GRE or IPsec)</li>
<li>Health check type (Request or Reply)</li>
<li>Health check direction (Bidirectional or Unidirectional)</li>
<li>Health check rate (Low, Medium, or High)</li>
</ul>
</li>
<li><strong>Router information:</strong>
<ul>
<li>Vendor and model</li>
<li>Firmware/software version</li>
<li>IPsec configuration (sanitized to remove PSK)</li>
</ul>
</li>
<li><strong>Symptoms observed:</strong>
<ul>
<li>Dashboard tunnel health status</li>
<li>Whether user traffic is affected</li>
<li>Error messages from router logs</li>
</ul>
</li>
</ol>
<h3 id="helpful-diagnostic-data">Helpful diagnostic data</h3>
<ul>
<li><strong>Packet captures</strong> from your router showing tunnel traffic</li>
<li><strong>Router logs</strong> covering the time period of the issue</li>
<li><strong>Traceroute</strong> results from your network to Cloudflare endpoints</li>
<li><strong>Screenshots</strong> of the tunnel health dashboard</li>
<li><strong>Distributed traceroutes</strong> using tools like <a href="https://ping.pe">ping.pe</a> to test reachability from multiple global locations</li>
</ul>
<h3 id="router-diagnostic-commands">Router diagnostic commands</h3>
<p>Collect output from these commands (syntax varies by vendor):</p>
<ul>
<li>IPsec SA status: <code>show crypto ipsec sa</code></li>
<li>IKE SA status: <code>show crypto isakmp sa</code></li>
<li>Tunnel interface status: <code>show interface tunnel &lt;number&gt;</code></li>
<li>Routing table: <code>show ip route</code></li>
</ul>
<hr />
<h2 id="resources">Resources</h2>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/tunnel-health-checks/">Tunnel health checks</a>: Technical details on health check behavior</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/anti-replay-protection/">Anti-replay protection</a>: Why anti-replay must be disabled</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a>: Tunnel setup instructions</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/">Check tunnel health in the dashboard</a>: Dashboard navigation guide</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/analytics/network-analytics/">Network Analytics</a>: Traffic analysis tools</li>
</ul>
<hr />
<h2 id="more-wan-resources">More WAN resources</h2>
<p>For more information, refer to the full Cloudflare WAN documentation.</p>
<p><a class="nb-link-button" href="/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/tunnel-health/">Full tunnel health guide ❯</a></p>
