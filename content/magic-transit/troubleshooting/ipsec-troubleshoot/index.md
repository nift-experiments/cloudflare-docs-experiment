<p>This guide helps you diagnose IPsec tunnel issues (also called connectors in the Cloudflare dashboard), from initial establishment through ongoing operation. Use the following sections to identify your symptom and find the appropriate solution.</p>
<h2 id="tunnel-never-establishes-ike-negotiation-fails">Tunnel never establishes (IKE negotiation fails)</h2>
<h3 id="symptoms">Symptoms</h3>
<ul>
<li>Tunnel status shows <code>Down</code> and never becomes healthy</li>
<li>No traffic passes through the tunnel</li>
<li>Tunnel endpoint logs show IKE negotiation errors or retransmissions</li>
</ul>
<h3 id="possible-causes-and-solutions">Possible causes and solutions</h3>
<h4 id="firewall-blocking-ike-traffic">Firewall blocking IKE traffic</h4>
<p>Your edge firewall may be blocking the traffic required for IPsec tunnel establishment. Verify your firewall permits:</p>
<ul>
<li>UDP port <code>500</code> (IKE)</li>
<li>UDP port <code>4500</code> (IKE NAT-T)</li>
<li>IP protocol <code>50</code> (ESP)</li>
</ul>
<h4 id="crypto-parameter-mismatch">Crypto parameter mismatch</h4>
<p>IKE negotiation fails when Phase 1 (IKE) or Phase 2 (IPsec) parameters do not match between your tunnel endpoint and Cloudflare. Common symptoms include &quot;no proposal chosen&quot; errors in your device logs.</p>
<p>Verify your parameters match Cloudflare's supported values. For the complete list, refer to <a href="/magic-transit/reference/gre-ipsec-tunnels/#supported-configuration-parameters">Supported configuration parameters</a>.</p>
<h4 id="pre-shared-key-psk-mismatch">Pre-shared key (PSK) mismatch</h4>
<p>Authentication failures in Phase 1 indicate a PSK mismatch. To resolve:</p>
<ol>
<li>Go to <strong>Connectors</strong> and select your tunnel.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Generate new PSK</strong>.</li>
<li>Copy the new PSK exactly — do not add extra spaces or characters.</li>
<li>Update your tunnel endpoint with the new PSK.</li>
</ol>
<h4 id="ike-id-format-mismatch">IKE ID format mismatch</h4>
<p>Cloudflare uses FQDN format for the IKE ID. If your tunnel endpoint expects a different peer identity format (such as an IP address), authentication fails even when the PSK is correct.</p>
<p>Ensure your tunnel endpoint is configured to accept an FQDN peer identity. To find your tunnel's FQDN, go to <strong>Connectors</strong>, select your tunnel, and check the tunnel details.</p>
<hr />
<h2 id="tunnel-establishes-but-health-checks-fail">Tunnel establishes but health checks fail</h2>
<h3 id="symptoms-1">Symptoms</h3>
<ul>
<li>IKE negotiation completes successfully</li>
<li>Tunnel shows <code>Down</code> or <code>Degraded</code> in the dashboard</li>
<li>User traffic may still pass through the tunnel</li>
</ul>
<h3 id="possible-causes-and-solutions-1">Possible causes and solutions</h3>
<h4 id="anti-replay-protection-enabled-on-tunnel-endpoint">Anti-replay protection enabled on tunnel endpoint</h4>
<p>This is the most common IPsec issue. Anti-replay protection expects packets to arrive in sequence from a single sender. Cloudflare's anycast architecture means tunnel traffic originates from thousands of servers, each with its own sequence counter. This causes your tunnel endpoint to drop packets as out-of-order.</p>
<p>Disable anti-replay protection on your tunnel endpoint, or set the replay window to <code>0</code>. For a detailed explanation, refer to <a href="/magic-transit/reference/anti-replay-protection/">Anti-replay protection</a>.</p>
<h4 id="health-check-type-incompatible-with-stateful-firewall">Health check type incompatible with stateful firewall</h4>
<p>Stateful firewalls (such as Palo Alto Networks, Check Point, Cisco, and Fortinet) drop the default <em>Reply</em> health check packets because no matching ICMP request exists in their session table.</p>
<p>Change the health check type from <em>Reply</em> to <em>Request</em>. For detailed steps, refer to <a href="/magic-transit/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a>.</p>
<h4 id="isp-blocking-health-check-return-path">ISP blocking health check return path</h4>
<p>With unidirectional health checks, Cloudflare sends probes through the tunnel, but responses return via the public internet (direct server return). If your ISP blocks ICMP reply packets destined for Cloudflare, health checks fail even though tunnel traffic works normally.</p>
<p>If you have egress traffic enabled, consider switching to bidirectional health checks so that both the probe and response traverse the tunnel. For configuration details, refer to <a href="/magic-transit/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a>.</p>
<h4 id="policy-based-vpn-health-check-failures">Policy-based VPN health check failures</h4>
<p>If you use a policy-based VPN (where traffic selectors define specific prefixes rather than <code>0.0.0.0/0</code>), Reply-style health checks do not work. Reply health checks are self-addressed to Cloudflare IP addresses, which fall outside your tunnel's traffic selectors.</p>
<p>Use Request-style health checks instead. Configure a loopback address on your tunnel endpoint as the health check target. The target must be routable and covered by the tunnel's traffic selectors (encryption domain). For more details, refer to <a href="/magic-transit/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a>.</p>
<hr />
<h2 id="tunnel-works-intermittently-flapping">Tunnel works intermittently (flapping)</h2>
<h3 id="symptoms-2">Symptoms</h3>
<ul>
<li>Tunnel alternates between healthy and unhealthy states</li>
<li>Intermittent packet loss on the tunnel</li>
<li>Traffic works for a period then stops without configuration changes</li>
</ul>
<h3 id="possible-causes-and-solutions-2">Possible causes and solutions</h3>
<h4 id="anti-replay-protection-dropping-out-of-order-packets">Anti-replay protection dropping out-of-order packets</h4>
<p>Cloudflare's anycast architecture means packets arrive from many servers with different sequence counters. Anti-replay protection interprets this as a replay attack and drops packets intermittently.</p>
<p>Disable anti-replay protection on your tunnel endpoint, or set the replay window to <code>0</code>. For a detailed explanation, refer to <a href="/magic-transit/reference/anti-replay-protection/">Anti-replay protection</a>.</p>
<h4 id="rekey-events-causing-brief-disruption">Rekey events causing brief disruption</h4>
<p>When your tunnel endpoint initiates an IPsec rekey, new Security Associations (SAs) must propagate across Cloudflare's network. Rekey propagation delays have been significantly reduced and are uncommon in most deployments. However, brief tunnel degradation during rekeys can still occur in some configurations.</p>
<p>Cloudflare never initiates rekey — only responds. All rekey attempts must come from your tunnel endpoint. If your device receives a TEMPORARY_FAILURE response during rekey, configure Dead Peer Detection (DPD) with a &quot;restart&quot; action so the device re-establishes the IKE session automatically. Without DPD restart, the device can get stuck in a loop of failed rekeys.</p>
<p>To minimize any impact from rekeys, increase SA lifetimes on your tunnel endpoint to reduce rekey frequency. Common values are 8-24 hours for IKE SA and 1-8 hours for IPsec SA. For more details, refer to <a href="/magic-transit/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a>.</p>
<h4 id="mtu-issues">MTU issues</h4>
<p>Packets exceeding the tunnel MTU are fragmented or dropped, causing intermittent connectivity issues. Verify MTU is set correctly — typically <code>1476</code> for GRE tunnels and <code>1400</code>-<code>1450</code> for IPsec tunnels. For detailed guidance, refer to <a href="/magic-transit/reference/mtu-mss/">MTU and MSS</a>.</p>
<hr />
<h2 id="monitor-with-ipsec-logs">Monitor with IPsec logs</h2>
<p>Use IPsec logs to monitor tunnel activity during the key-exchange phase of the IPsec negotiation. Configure a Logpush job to forward these logs to your preferred storage service for analysis.</p>
<h3 id="set-up-an-ipsec-logpush-job">Set up an IPsec Logpush job</h3>
<ol>
<li>Go to the <strong>Logpush</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create a Logpush job</strong>.</li>
<li>Select <strong>IPsec logs</strong> as your dataset.</li>
</ol>
<p>Refer to the <a href="/logs/logpush/">Logpush documentation</a> for more information about features, including the <a href="/logs/logpush/logpush-job/datasets/account/ipsec_logs/">available fields</a> in the dataset.</p>
<h2 id="anti-replay-protection">Anti-replay protection</h2>
<p>Some customer routers cannot fully disable IPsec anti-replay protection, which is required for optimal Magic Transit operation (packet reordering at the Cloudflare edge can otherwise trigger false drops).</p>
<p><strong>If your router does not support disabling anti-replay:</strong></p>
<ol>
<li>Check whether your router supports configuring a <strong>replay window size</strong>. Setting this to <code>0</code> is equivalent to disabling anti-replay protection.</li>
<li>If neither disabling anti-replay nor setting the window size to <code>0</code> is supported, <strong>the router cannot be used as a Magic Transit IPsec on-ramp</strong>. Consider using a GRE tunnel or Cloudflare Network Interconnect (CNI) instead.</li>
</ol>
<h2 id="health-check-failures-when-using-ipsec">Health check failures when using IPsec</h2>
<p>In the default unidirectional (DSR) configuration, Magic Transit health check responses travel over the public internet back to Cloudflare, not through the IPsec tunnel. This means your ISP or upstream network must allow the health check response packets from your prefix to reach <a href="https://www.cloudflare.com/ips/">Cloudflare's IP ranges</a>.</p>
<p>If your ISP is blocking these response packets, health checks will fail even when the IPsec tunnel and data plane are working correctly.</p>
<p><strong>Symptom:</strong> Health checks fail but application traffic flows normally through the tunnel.</p>
<p><strong>Resolution:</strong> Switch to bidirectional health checks, which send both the probe and the response through the tunnel. Bidirectional health checks require egress traffic to be turned on for your Magic Transit configuration. For more information, refer to <a href="/magic-transit/reference/tunnel-health-checks/">Tunnel health checks</a>.</p>
