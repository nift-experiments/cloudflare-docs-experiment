<p><a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>, our comprehensive Secure Web Gateway, allows you to set up policies to inspect DNS, network, HTTP, and egress traffic.</p>
<p>You can apply network and HTTP Gateway policies alongside <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> policies (for L3/4 traffic filtering) to Internet-bound traffic or private traffic entering the Cloudflare network through Cloudflare WAN (formerly Magic WAN). Additionally, you can configure Gateway to <a href="#dns-filtering">resolve DNS queries</a> from Cloudflare WAN.</p>
<h2 id="https-filtering">HTTPS filtering</h2>
<p>To inspect HTTPS traffic, you need to install a Cloudflare root certificate on each client device. A certificate is required for Cloudflare to <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">decrypt TLS</a>.</p>
<h3 id="installing-certificates">Installing certificates</h3>
<p>You can use the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/zero-trust/cloudflare-one-client/">Cloudflare One Client</a> to <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/">automatically install a Cloudflare certificate</a> on supported devices. If your device or application does not support certificate installation through the Cloudflare One Client, you can <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/">manually install a certificate</a>.</p>
<h3 id="exempting-traffic-from-inspection">Exempting traffic from inspection</h3>
<p>If you cannot or do not want to install the certificate, you can create <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect</a> policies to exempt incompatible Cloudflare WAN traffic from inspection or to disable TLS decryption entirely.</p>
<p>Because Gateway cannot discern Cloudflare WAN traffic, you must use <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client checks</a> or the IP addresses associated with Cloudflare WAN to match traffic with Gateway policies.</p>
<p>For example, if your organization onboards devices to Cloudflare WAN using the Cloudflare One Client, you can exempt devices not running the Cloudflare One Client using <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/">OS version checks</a>:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Passed Device Posture Checks</td>
<td>not in</td>
<td>Windows (OS version)</td>
<td>Or</td>
<td>Do Not Inspect</td>
</tr>
<tr>
<td>Passed Device Posture Checks</td>
<td>not in</td>
<td>macOS (OS version)</td>
<td>Or</td>
<td>Do Not Inspect</td>
</tr>
<tr>
<td>Passed Device Posture Checks</td>
<td>not in</td>
<td>Linux (OS version)</td>
<td>Or</td>
<td>Do Not Inspect</td>
</tr>
<tr>
<td>Passed Device Posture Checks</td>
<td>not in</td>
<td>iOS (OS version)</td>
<td>Or</td>
<td>Do Not Inspect</td>
</tr>
<tr>
<td>Passed Device Posture Checks</td>
<td>not in</td>
<td>Android (OS version)</td>
<td></td>
<td>Do Not Inspect</td>
</tr>
</tbody>
</table>
<p>If your organization onboards users to Cloudflare WAN using an <a href="/cloudflare-one/networks/connectors/cloudflare-wan/on-ramps/">on-ramp other than the Cloudflare One Client</a>, you can exempt devices from inspection using the IP addresses for your IPsec tunnels:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source IP</td>
<td>in</td>
<td><code>203.0.113.0/24</code></td>
<td>Do Not Inspect</td>
</tr>
</tbody>
</table>
<h2 id="dns-filtering">DNS filtering</h2>
<p>You can configure the DNS resolver for your Cloudflare WAN networks to the shared IP addresses for the Gateway DNS resolver. The Gateway DNS resolver IPs are <code>172.64.36.1</code> and <code>172.64.36.2</code>.</p>
<p>When you resolve DNS queries from Cloudflare WAN through Gateway, Gateway will log the queries with the private source IP. You can use the private source IP to create <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> for queries intended for <a href="/cloudflare-one/traffic-policies/resolver-policies/#internal-dns">internal DNS records</a>.</p>
<p>The following diagram illustrates how DNS queries from Cloudflare WAN and Cloudflare Mesh flow through Gateway to your internal DNS:</p>
<pre class="mermaid">&#10;&#10;	{`&#10;flowchart LR&#10;accTitle: DNS query flow&#10;accDescr: Shows how DNS queries from Cloudflare WAN and Cloudflare Mesh flow through Gateway to internal DNS.&#10; subgraph subGraph0["Data center"]&#10;    direction TB&#10;        InternalDNS(["Internal DNS"])&#10;        ResolverPolicies["Resolver policies"]&#10;        CloudflareGatewayDNSResolver["Gateway DNS resolver"]&#10;  end&#10;    ResolverPolicies -- Retain and use</br>Source Internal IP --> InternalDNS&#10;    CloudflareGatewayDNSResolver -- <br> --> ResolverPolicies&#10;    WarpConnector["Cloudflare Mesh"] -- DHCP/DNS resolver --> IPSecTunnel["IPsec tunnel"]&#10;    CloudflareWAN[Cloudflare WAN] -- DHCP/DNS resolver --> IPSecTunnel&#10;    IPSecTunnel -- Shared IP endpoints --> CloudflareGatewayDNSResolver&#10;    ResolverPolicies@{ shape: proc}&#10;    WarpConnector@{ shape: in-out}&#10;    CloudflareWAN@{ shape: in-out}&#10;	`}&#10;&#10;</pre>
<h2 id="outbound-internet-traffic">Outbound Internet traffic</h2>
<p>By default, the following traffic routed through IPsec/GRE tunnels and destined to public IP addresses is proxied/filtered through Cloudflare Gateway:</p>
<ul>
<li>TCP, UDP, and ICMP traffic sourced from <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918</a> IPs or devices.</li>
<li>TCP and UDP traffic sourced from <a href="/byoip/">BYOIP</a> or <a href="/magic-transit/cloudflare-ips/">Leased IPs</a> and destined to a well-known port (<code>0</code>-<code>1023</code>).</li>
</ul>
<p>By default, traffic destined to public IPs will be routed over the public Internet. If you want to configure specific public IP ranges to be routed through your IPsec/GRE tunnels instead of over the public Internet after filtering, contact your account team.</p>
<p>This traffic will egress from Cloudflare according to the <a href="/cloudflare-one/traffic-policies/egress-policies/">egress policies</a> you define in Cloudflare Gateway. By default, it will egress from a shared Cloudflare public IP range.</p>
<h2 id="private-traffic">Private traffic</h2>
<p>By default, TCP, UDP, and ICMP traffic routed through IPsec/GRE tunnels and destined to routes behind <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> will be proxied/filtered through Cloudflare Gateway.</p>
<p>Contact your account team to enable Gateway filtering for traffic destined to routes behind IPsec/GRE tunnels.</p>
<h3 id="default-filtering-criteria">Default filtering criteria</h3>
<p>When enabled, TCP/UDP traffic meeting <strong>all</strong> the following criteria will be proxied and filtered by Cloudflare Gateway:</p>
<ul>
<li><strong>Source and destination IPs</strong>: Both must be part of <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC1918</a> space, <a href="/cloudflare-one/networks/connectors/cloudflare-wan/zero-trust/cloudflare-one-client/">WARP</a>, <a href="/byoip/">BYOIP</a>, or <a href="/magic-transit/cloudflare-ips/">Leased IPs</a>.</li>
<li><strong>Source port</strong>: Must be a client port strictly higher than <code>1023</code>.</li>
<li><strong>Destination port</strong>: Must be a well-known port (lower than <code>1024</code>).</li>
</ul>
<h3 id="custom-filtering-criteria">Custom filtering criteria</h3>
<p>You can specify more specific matches to override the default criteria:</p>
<ul>
<li><strong>Source IP prefix</strong>: A subset of RFC1918 space, <a href="/byoip/">BYOIP</a>, or <a href="/magic-transit/cloudflare-ips/">Leased IPs</a>.</li>
<li><strong>Destination IP prefix</strong>: A subset of RFC1918 space, <a href="/byoip/">BYOIP</a>, or <a href="/magic-transit/cloudflare-ips/">Leased IPs</a>.</li>
<li><strong>Destination port</strong>: Any port from <code>0</code> to <code>65535</code>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5533.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="run-traceroute">Run <code>traceroute</code></h3>
@markup("md", "content/.markup/bodies/5532.md")
</aside>
<h2 id="test-gateway-integration">Test Gateway integration</h2>
<p>To check if Gateway is working properly with your Cloudflare WAN connection, open a browser from a host behind your customer premise equipment, and browse to <code>https://ifconfig.me</code>.</p>
<p>If you are still testing Gateway and Cloudflare is not your default route, configure a policy-based route on your router to send traffic to Cloudflare Gateway first.</p>
<p>Confirm there is an entry for the test in <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#http-logs">HTTP Gateway Activity Logs</a>.</p>
<p>Verify the following details:</p>
<ul>
<li><strong>Destination IP</strong>: Should be the public IP address of <code>ifconfig.me</code>.</li>
<li><strong>Source IP</strong>: Should be the private (WAN) address of the host with the browser.</li>
<li><strong>Outbound connection</strong>: Should be sourced from a Cloudflare WAN IP address, not any public IP address that Cloudflare might be advertising on your behalf.</li>
</ul>
<p>This applies when using <a href="/reference-architecture/architectures/magic-transit/#magic-transit-with-egress-option-enabled">Magic Transit With Egress Option</a> as well.</p>
<p>Additionally, test both <code>http://ifconfig.me</code> (non-TLS) and <code>https://ifconfig.me</code> (TLS) to ensure that your <a href="/cloudflare-one/networks/connectors/cloudflare-wan/get-started/#set-maximum-segment-size">TCP maximum segment size (MSS Clamping)</a> has been set properly.</p>
<p>If the HTTPS query hangs or fails but HTTP works, the MSS value may be too high or not set. Reduce this value on your customer premise equipment to match the overhead introduced by your <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/gre-ipsec-tunnels/#supported-configuration-parameters">IKE</a> and <a href="https://en.wikipedia.org/wiki/IPsec#Encapsulating_Security_Payload">ESP</a> settings.</p>
