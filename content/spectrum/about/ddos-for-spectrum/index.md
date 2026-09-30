<p>Spectrum provides DDoS Protection at layers 3-4 of the <a href="https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/">OSI model</a>, that is against TCP and UDP based DDoS attacks.</p>
<p>Spectrum works as a layer 4 reverse proxy, therefore a proper TCP connection must be first established before traffic is proxied to the origin. This moves any impact of SYN or SYN-ACK reflection attacks to the Cloudflare global network. Additionally, by using Spectrum in front of your application, your origin IP is concealed — preventing attackers from targeting your origin server directly. It is also recommended that you replace your origin IP address after moving to Cloudflare, and lock it down to only accept traffic from <a href="https://www.cloudflare.com/ips/">Cloudflare’s IP address range</a>.</p>
<p>Random or out-of-state TCP packets should not be passed to the origin if a legitimate TCP connection has not yet been established between the client and Cloudflare. Spectrum also <a href="https://blog.cloudflare.com/syn-packet-handling-in-the-wild/">leverages SYN cookie challenges as part of the Linux networking stack</a> to defend against floods.</p>
<p>Furthermore, if a flood of packets of an unspecified protocol target your application (for example, your Spectrum application is for TCP traffic, and a UDP flood targets your Spectrum application), the packets will be dropped. Similarly, if packets target a port or port range that you did not specify, they will also be dropped.</p>
<p>L3/4 DDoS attacks should be detected and mitigated by the <a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS Attack Protection managed ruleset</a> that is enabled by default. This ruleset detects and mitigates DDoS attacks by dynamically fingerprinting attacks based on packet header fields.</p>
<p>For protecting HTTP/S applications against L7 DDoS attacks and to benefit from caching and additional features, onboard your application to Cloudflare’s Web Application Firewall/Content Delivery Network service, which works in tandem with Cloudflare Spectrum.</p>
<p>Refer to <a href="/ddos-protection/">Cloudflare DDoS Protection</a> to learn more.</p>
<hr />
<h2 id="mitigation-reasons">Mitigation reasons</h2>
<p>The <strong>Mitigation reason</strong> field shown in the <strong>DDoS managed rules</strong> tab of <a href="/analytics/network-analytics/">Network Analytics</a> (<strong>Networking</strong> &gt; <strong>Insights</strong> &gt; <strong>Network Analytics</strong> in the dashboard) will contain more information on why a given packet was dropped by the Spectrum system.</p>
<p>The mitigation reasons are the following:</p>
<table>
<thead>
<tr>
<th>Reason</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Blocked</strong></td>
<td>Packet dropped because it matched a DDoS protection rule.</td>
</tr>
<tr>
<td><strong>Rate limited</strong></td>
<td>Packet dropped because it exceeded rate limits.</td>
</tr>
<tr>
<td><strong>Connection limited</strong></td>
<td>Packet dropped because it exceeded connection limits.</td>
</tr>
<tr>
<td><strong>Unexpected</strong></td>
<td>Packet dropped because it was not expected given the current state of the connection it was associated with.</td>
</tr>
<tr>
<td><strong>Not found</strong></td>
<td>Packet dropped because it does not match any configured Spectrum application on the destination IP address and port.</td>
</tr>
</tbody>
</table>
