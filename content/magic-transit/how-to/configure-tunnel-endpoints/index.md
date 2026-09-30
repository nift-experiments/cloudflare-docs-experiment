<p>Cloudflare assigns an IPv4 anycast address to your account for use as the tunnel destination for your network's routers. You can find this address in the Cloudflare dashboard under <strong>Address Space</strong> &gt; <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space"><strong>Leased IPs</strong></a>. To request additional endpoint addresses, contact your account team.</p>
<p>Cloudflare handles failures on its network automatically by advertising your endpoint IP from multiple nodes across many globally distributed data centers. To handle failures on your network, configure two tunnels from separate routers.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Before creating a tunnel, make sure you have the following information:</p>
<ul>
<li><strong>Cloudflare endpoint address</strong>: The anycast IP address assigned to your account. You can find it in the Cloudflare dashboard under <strong>Address Space</strong> &gt; <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space"><strong>Leased IPs</strong></a>.</li>
<li><strong>Customer endpoint IP</strong>: A public Internet routable IP address outside of the prefixes Cloudflare will advertise on your behalf (typically provided by your ISP). Not required if using <a href="/network-interconnect/">Cloudflare Network Interconnect</a> or for <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/10662.md")
</div> tunnels (unless your router uses an <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/10663.md")
</div> ID of type `ID_IPV4_ADDR`).
- **Interface address**: A `/31` (recommended) or `/30` subnet from RFC 1918 private IP space (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) or `169.254.240.0/20`.
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10661.md")
</aside>
<h2 id="ways-to-onboard-traffic-to-cloudflare">Ways to onboard traffic to Cloudflare</h2>
<h3 id="gre-and-ipsec-tunnels">GRE and IPsec tunnels</h3>
<p>You can use GRE or IPsec tunnels to onboard your traffic to Magic Transit, and set them up through the Cloudflare dashboard or the API. If you use the API, you need your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> and <a href="/fundamentals/api/get-started/keys/#view-your-global-api-key">API key</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="anycast-routing">Anycast routing</h3>
@markup("md", "content/.markup/bodies/10660.md")
</aside>
<h4 id="choose-between-gre-and-ipsec">Choose between GRE and IPsec</h4>
<table>
<thead>
<tr>
<th>Feature</th>
<th>GRE</th>
<th>IPsec</th>
</tr>
</thead>
<tbody>
<tr>
<td>Encryption</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Authentication</td>
<td>No</td>
<td>Pre-shared key (PSK)</td>
</tr>
<tr>
<td>Setup complexity</td>
<td>Simpler</td>
<td>Requires PSK exchange</td>
</tr>
<tr>
<td>Best for</td>
<td>Trusted networks, CNI connections</td>
<td>Internet-facing connections requiring encryption</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/magic-transit/reference/gre-ipsec-tunnels/">Tunnels and encapsulation</a> to learn more about the technical requirements for both tunnel types.</p>
<h4 id="ipsec-supported-ciphers">IPsec supported ciphers</h4>
<p>Refer to <a href="/magic-transit/reference/gre-ipsec-tunnels/#supported-configuration-parameters">supported ciphers for IPsec</a> for a complete list. IPsec tunnels only support Internet Key Exchange version 2 (IKEv2).</p>
<h4 id="anti-replay-protection">Anti-replay protection</h4>
<p>If you use Magic Transit and <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10664.md")
</div> IPsec tunnels, we recommend disabling anti-replay protection. Cloudflare disables this setting by default. However, you can enable it through the API or the Cloudflare dashboard for devices that do not support disabling it, including Cisco Meraki, Velocloud, and AWS VPN Gateway.
<p>Refer to <a href="/magic-transit/reference/anti-replay-protection/">Anti-replay protection</a> for more information on this topic, or <a href="#add-ipsec-tunnel">Add IPsec tunnels</a> to learn how to enable this feature.</p>
<h3 id="network-interconnect-cni">Network Interconnect (CNI)</h3>
<p>Beyond GRE and IPsec tunnels, you can also use Network Interconnect (CNI) to onboard your traffic to Magic Transit. Refer to <a href="/magic-transit/network-interconnect/">Network Interconnect (CNI)</a> for more information.</p>
<h2 id="add-tunnels">Add tunnels</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10659.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10674.md")
</div></div>
<h2 id="bidirectional-vs-unidirectional-health-checks">Bidirectional vs unidirectional health checks</h2>
<p>To check for tunnel health, Cloudflare sends a <a href="/magic-transit/reference/tunnel-health-checks/">health check probe</a> consisting of ICMP (Internet Control Message Protocol) reply <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-packet/">packets</a> to your network. Cloudflare needs to receive these probes to know if your tunnel is healthy.</p>
<p>Cloudflare defaults to unidirectional health checks for Magic Transit (direct server return), and bidirectional health checks for Cloudflare WAN. However, routing unidirectional ICMP reply packets over the Internet to Cloudflare is sometimes subject to drops by intermediate network devices, such as stateful firewalls. Magic Transit customers with egress traffic can modify this setting to bidirectional.</p>
<p>If you are a Magic Transit customer with egress traffic, refer to <a href="/magic-transit/reference/egress/">Magic Transit egress traffic</a> for more information on the technical aspects you need to consider to create a successful connection to Cloudflare.</p>
<h3 id="legacy-bidirectional-health-checks">Legacy bidirectional health checks</h3>
<p>For customers using the legacy health check system with a public IP range, Cloudflare recommends:</p>
<ul>
<li>Configuring the tunnel health check target IP address to one within the <code>172.64.240.252/30</code> prefix range.</li>
<li>Applying a policy-based route that matches <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-packet/">packets</a> with a source IP address equal to the configured tunnel health check target (for example <code>172.64.240.253/32</code>), and route them over the tunnel back to Cloudflare.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<p>Now that you have set up your tunnel endpoints, you need to configure routes to direct your traffic through Cloudflare. You have two routing options:</p>
<ul>
<li><strong>Static routes</strong>: Best for simple, stable networks where routes rarely change. You manually define each route.</li>
<li><strong>BGP peering</strong>: Best for dynamic environments with frequently changing routes, multiple prefixes, or when you need automatic failover. Requires enabling BGP on your tunnel during creation.</li>
</ul>
<p>Refer to <a href="/magic-transit/how-to/configure-routes/">Configure routes</a> for detailed instructions on both options.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you experience issues with your tunnels:</p>
<ul>
<li>For tunnel health check problems, refer to <a href="/magic-transit/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a>.</li>
<li>For IPsec tunnel establishment issues, refer to <a href="/magic-transit/troubleshooting/ipsec-troubleshoot/">Troubleshoot with IPsec logs</a>.</li>
</ul>
