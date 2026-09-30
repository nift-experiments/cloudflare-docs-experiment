<h2 id="introduction">Introduction</h2>
<p>Network security teams have traditionally used various network firewalls or security appliances at the perimeter to protect their data center networks against both external and internal threats, for example, DDoS attacks, malware, ransomware, phishing, leaking of sensitive information, etc. In addition, the same or additional firewall or security appliances are deployed at the <a href="https://en.wikipedia.org/wiki/DMZ_(computing)">DMZ</a> or core layer of the data center networks to control and secure internal private network traffic routed between multiple data center sites across their wide-area network (WAN).</p>
<p>But these firewalls and security appliances are often expensive, complex to configure and manage, difficult to scale to handle large attacks, and require upgrades and patches to defend against newly discovered threats and vulnerabilities.</p>
<p><a href="/magic-transit/">Cloudflare Magic Transit</a>, <a href="/cloudflare-wan/">Cloudflare WAN</a> (formerly Magic WAN), <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> and <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> services running natively on <a href="https://www.cloudflare.com/network/">Cloudflare's massive global network</a> provide solutions to all the shortcomings described above and more. These services offer in-line, scalable and performant global protection for your data center networks, all from a single cloud network platform.</p>
<ul>
<li><a href="https://www.cloudflare.com/network-services/products/magic-transit/">Magic Transit</a> provides instant detection and mitigation against network-layer DDoS attacks on your public, Internet-facing networks.</li>
<li><a href="https://www.cloudflare.com/network-services/products/magic-wan/">Cloudflare WAN</a> provides any-to-any, hybrid/multi-cloud secure connectivity between your private, enterprise networks.</li>
<li><a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> is a cloud-native network firewall service that can be used to filter traffic that is routed to and from your networks that are protected by Magic Transit. It also supports functionalities such as <a href="/cloudflare-network-firewall/about/ids/">Intrusion Detection</a> (IDS) and <a href="/cloudflare-network-firewall/packet-captures/">packet capture</a>.</li>
<li><a href="https://www.cloudflare.com/zero-trust/products/gateway/">Gateway</a> is a secure web gateway (SWG) service that allows you to inspect and control both Internet-bound traffic that is originated from your networks, as well as private network-to-private network traffic (that is, east-west), by proxying such traffic through Cloudflare's global network while applying DNS, network and HTTP based <a href="/cloudflare-one/traffic-policies/">policies</a>.</li>
</ul>
<p>This document focuses specifically on the reference architectures of using Cloudflare Magic Transit, Cloudflare WAN, Cloudflare Network Firewall and Cloudflare Gateway services to protect both external and internal communications to your data center networks. For details of how Magic Transit, Cloudflare WAN, Cloudflare Network Firewall and Cloudflare Gateway works and how it can be architected for various use cases, see the linked resources at the end of the document.</p>
<p>To illustrate the architecture and how it works, the following diagrams visualize an example corporation with a set of data center networks that are either public-facing, connecting to users on the Internet or private, internal facing, used for communication within the enterprise. These networks are deployed at two on-premises locations. The prefixes of the public-facing networks are to be protected by Cloudflare Magic Transit.</p>
<table>
<thead>
<tr>
<th align="left">Data center 1</th>
<th align="left">Data center 2</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Public-facing network: <code>192.0.2.0/24</code></td>
<td align="left">Public-facing network: <code>203.0.113.0/24</code></td>
</tr>
<tr>
<td align="left">Private network: <code>192.168.1.0/24</code></td>
<td align="left">Private network: <code>172.16.2.0/24</code></td>
</tr>
</tbody>
</table>
<p>The edge router(s) at each data center is connected to Cloudflare network via two Direct <a href="/network-interconnect/">Cloudflare Network Interconnect</a> (CNI) connections, which are direct, private connections between your network and Cloudflare network. One of the Direct CNI connections is for carrying public-facing network traffic, while the other is for carrying private network traffic. Optionally, you can choose to carry both public and private network traffic over a single CNI connection but many organizations do desire to transport external and internal network traffic over separate connections in their security practice.</p>
<ul>
<li>For data center 1, CNI connection 1 is used to transport public-facing network traffic and connection 2 is used to transport private network traffic.</li>
<li>For data center 2, CNI connection 3 is used to transport public-facing network traffic and connection 4 is used to transport private network traffic.</li>
</ul>
<h2 id="protect-inbound-traffic-to-public-facing-networks">Protect inbound traffic to public-facing networks</h2>
<p>The reference architecture diagram below illustrates how Cloudflare Magic Transit and Cloudflare Network Firewall can be used to protect the data centers' public-facing networks from inbound traffic originating from the Internet.</p>
<p><img src="/assets/upstream/images/reference-architecture/protect-data-center-networks/figure1.svg" alt="Figure 1. Protect Public-facing Networks from Inbound Traffic." title="Figure 1. Protect Public-facing Networks from Inbound Traffic." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<ol>
<li>Using Border Gateway Protocol (<a href="https://www.cloudflare.com/learning/security/glossary/what-is-bgp/">BGP</a>) and <a href="https://www.cloudflare.com/learning/cdn/glossary/anycast-network/">IP anycast</a>, Cloudflare advertises the customer's protected IP prefixes to the Internet from all of <a href="https://www.cloudflare.com/network/">Cloudflare's global data centers</a>. At the same time, on-premises network(s) would stop advertising the same exact prefixes from their respective on-premises border routers. This ensures that all traffic passes through Cloudflare for Magic Transit DDoS protection and policy enforcement before being delivered to the customer's data center. Internet traffic destined to these protected IP prefixes will always be routed to the Cloudflare data center that is closest to the source of the traffic.
Optionally, you could advertise less-specific IP prefixes from the border routers to the Internet. This way, in the unlikely event of a Magic Transit service failure, traffic can be quickly re-routed directly to network locations from the Internet.</li>
<li>Traffic originating from the Internet and destined to the protected IP prefixes is ingested into the global Cloudflare network.</li>
<li>All DDoS attack traffic is mitigated in-line, close to the sources, at every Cloudflare data center using advanced and automated <a href="/ddos-protection/">DDoS mitigation</a> technologies.</li>
<li>Traffic that passes DDoS mitigation is subjected to additional network firewall filtering using <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a>.</li>
<li>Clean, filtered traffic is routed to the protected networks through Direct <a href="/network-interconnect/">Cloudflare Network Interconnect</a> (CNI) connections.</li>
<li>There are two ways to route server return traffic back to the clients. One way is to route it natively out of the data center and onto the Internet, bypassing Cloudflare network. This method is called Direct Server Return (DSR). It results in asymmetric routing for the bi-directional traffic, which may cause problems with network security and traffic filtering when there are stateful firewalls or NAT devices in the network path, either through other parts of the data center or between the data center and the Internet. Caution needs to be taken in ensuring such an issue does not exist in your network.
The other way is to symmetrically route server return traffic back through the Cloudflare network, over the same connection that carries the client-to-server traffic, using <a href="/magic-transit/reference/egress/">Magic Transit Egress</a>. This method is depicted in the diagram above, where the server return traffic is routed to the Cloudflare network via the same CNIs that transport public-facing network traffic from Cloudflare to the data center, using routing techniques such as policy-based routing (PBR) at your sites.</li>
<li>Magic Transit Egress traffic is subject to Cloudflare Network Firewall filtering before being routed out to the Internet towards the users.</li>
</ol>
<h2 id="protect-internet-access-from-public-facing-networks">Protect Internet access from public-facing networks</h2>
<p>The reference architecture diagram below illustrates how Cloudflare services - Magic Transit (Egress), Cloudflare Network Firewall, and Cloudflare Gateway can be used to protect outbound Internet traffic originating from the data centers' public-facing networks (that is, servers with public IP addresses).</p>
<p><img src="/assets/upstream/images/reference-architecture/protect-data-center-networks/figure2.svg" alt="Figure 2. Protect outbound traffic from public-facing networks." title="Figure 2. Protect outbound traffic from public-facing networks." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<ol>
<li>Each site network routes outbound Internet traffic originating from the public-facing networks to Cloudflare, via the same CNIs that inbound traffic traverses. This can be done at your site through routing techniques of your choice, such as policy based routing (PBR).</li>
<li>Upon entering the Cloudflare network, outbound Internet traffic is first routed through Cloudflare Network Firewall where it is subject to any configured network firewall policies.</li>
<li>Outbound Internet traffic is subsequently sent to <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>, our secure web gateway service where various <a href="/cloudflare-one/traffic-policies/">policies</a> enforce a comprehensive set of security and control measures on the outbound traffic, ensuring the utmost protection for your networks. For example, Gateway DNS and HTTP policies can both be configured to prevent your servers from connecting to questionable Internet sites and from downloading malware or other malicious content.</li>
<li>Once traffic clears inspection, Gateway proxies the outbound traffic to their destinations on the Internet. The source IP addresses of the outbound traffic are the Cloudflare owned IP addresses associated with the Gateway service, which if you want you can purchase and set your <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">own egress IP</a></li>
<li>Return traffic from the Internet, destined to Cloudflare's IP addresses linked to the Gateway service, is routed into Cloudflare's global network.</li>
<li>Traffic is inspected against Gateway policies.</li>
<li>Return traffic that passes Gateway inspection is routed to Cloudflare Network Firewall for further packet filtering.</li>
<li>Return traffic that passes Cloudflare Network Firewall filtering is routed from Cloudflare to your network locations via CNIs that transport public-facing network traffic.</li>
</ol>
<h2 id="protect-site-to-site-inter-data-center-private-network-traffic">Protect site-to-site, inter-data center, private network traffic</h2>
<p>The reference architecture diagrams below illustrate how Cloudflare services — Cloudflare WAN, Cloudflare Network Firewall and Cloudflare Gateway — can be used to protect site-to-site, inter-data center traffic between your private networks.</p>
<p><strong>Site to Site Private Network Traffic Connectivity</strong></p>
<p>First, let us examine the use case where you do not intend to subject site-to-site private network traffic to Cloudflare Gateway proxy firewall service and simply route it using Cloudflare WAN service.</p>
<p><img src="/assets/upstream/images/reference-architecture/protect-data-center-networks/figure3.1.svg" alt="Figure 3.1. Protect inter-data center non-gateway-proxied traffic between private networks." title="Figure 3.1. Protect inter-data center non-gateway-proxied traffic between private networks." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<ol>
<li>Each site routes site-to-site private network traffic, destined to the other data center location, to Cloudflare WAN via the corresponding CNI connections. This can be done at your site through routing techniques of your choice, such as policy based routing (PBR).</li>
<li>Upon entering the Cloudflare network, traffic is routed through Cloudflare Network Firewall.</li>
<li>Cloudflare Network Firewall subjects traffic to any configured network firewall policies.</li>
<li>Traffic that clears the Cloudflare Network Firewall rules and is not intended to be further proxied by Cloudflare Gateway service, is routed back to the destination network via the corresponding CNI.</li>
</ol>
<p><strong>Site to Site Private Network Traffic with Application Level Security Controls</strong></p>
<p>For the use case where you do want to apply application level policy for fine-grain control and security on certain private network traffic, you can route and proxy such traffic through Cloudflare WAN and Cloudflare Gateway service. The following diagram illustrates the architecture and packet flow of such use cases.</p>
<p><img src="/assets/upstream/images/reference-architecture/protect-data-center-networks/figure3.2.svg" alt="Figure 3.2: Figure 3.2. Protect inter-data center gateway-proxied traffic between private networks." title="Figure 3.2. Protect inter-data center gateway-proxied traffic between private networks." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<ol>
<li>Each site routes private network traffic destined to the other data center location to Cloudflare WAN via the corresponding CNI connections. This can be done at your site through routing techniques of your choice, such as policy based routing (PBR).</li>
<li>Upon entering the Cloudflare network, traffic is routed through Cloudflare Network Firewall where it is subject to any configured network firewall policies.</li>
<li>After clearing Cloudflare Network Firewall, traffic is subsequently routed to <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>, our secure web gateway service.</li>
<li>Cloudflare Gateway subjects traffic to any configured L3-7 <a href="/cloudflare-one/traffic-policies/">policies</a> that enforce a comprehensive set of security and control measures, ensuring the utmost protection for your networks. Once traffic clears inspection, Gateway proxies the traffic to its destination private network. The source IP addresses of the proxied traffic are the Cloudflare owned IP addresses associated with the Gateway service.</li>
<li>The proxied traffic, en-route to its destination private network, is routed through Cloudflare Network Firewall once again for further packet filtering.</li>
<li>Traffic that passes Cloudflare Network Firewall filtering is routed from Cloudflare to your network locations via the corresponding CNIs that transport private network traffic.</li>
</ol>
<h2 id="protect-outbound-internet-traffic-from-private-networks">Protect outbound Internet traffic from private networks</h2>
<p>The reference architecture diagram below illustrates how Cloudflare services — Cloudflare WAN, Cloudflare Network Firewall and Cloudflare Gateway — can be used to protect outbound Internet traffic originating from the data centers' private networks. The use cases and the protection provided to the servers on the private networks are very similar to those described in the previous section about protecting Internet access from public-facing networks. The differences are that the servers have private IP addresses and that Cloudflare WAN service is used in this section, as opposed to the previous section where servers are assigned with public IP addresses and Magic Transit server is used.</p>
<p><img src="/assets/upstream/images/reference-architecture/protect-data-center-networks/figure4.svg" alt="Figure 4. Protect outbound traffic from private networks." title="Figure 4. Protect outbound traffic from private networks." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<ol>
<li>Each site routes outbound Internet traffic originating from its private networks to Cloudflare WAN via the corresponding CNI connections. This can be done at your site through routing techniques of your choice, such as policy based routing (PBR).</li>
<li>Upon entering the Cloudflare network, outbound Internet traffic is first routed through Cloudflare Network Firewall where it is subject to any configured network firewall policies.</li>
<li>Traffic that clears Cloudflare Network Firewall is subsequently sent to <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>, our secure web gateway service where any configured L3-7 <a href="/cloudflare-one/traffic-policies/">policies</a> enforce a comprehensive set of security and control measures on the outbound traffic, ensuring the utmost protection for your networks.</li>
<li>Once traffic clears inspection, Gateway proxies the outbound traffic to their destinations on the Internet. The source IP addresses of the outbound traffic are the Cloudflare owned IP addresses associated with the Gateway service.</li>
<li>Return traffic from the Internet, destined to Cloudflare's IP addresses linked to the Gateway service, is routed into Cloudflare's global network.</li>
<li>Traffic is inspected against Gateway policies.</li>
<li>Return traffic that passes Gateway inspection is routed to Cloudflare Network Firewall for further packet filtering.</li>
<li>Return traffic that passes Cloudflare Network Firewall filtering is routed from Cloudflare to your network locations via CNIs that transport private network traffic.</li>
</ol>
<h2 id="related-resources">Related Resources</h2>
<ul>
<li><a href="/magic-transit/">Cloudflare Magic Transit</a></li>
<li><a href="/ddos-protection/">Cloudflare DDoS Protection</a></li>
<li><a href="/reference-architecture/architectures/magic-transit/">Magic Transit Reference Architecture</a></li>
<li><a href="/network-interconnect/">Cloudflare Network Interconnect</a></li>
<li><a href="/cloudflare-network-firewall/">Cloudflare Cloudflare Network Firewall</a></li>
<li><a href="/cloudflare-wan/">Cloudflare WAN</a></li>
<li><a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a></li>
<li><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Integration of Cloudflare Magic services and Cloudflare Gateway</a></li>
</ul>
