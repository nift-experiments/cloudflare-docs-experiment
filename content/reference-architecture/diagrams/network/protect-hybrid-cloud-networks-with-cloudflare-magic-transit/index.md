<h2 id="introduction">Introduction</h2>
<p>Protecting network infrastructure from DDoS attacks demands a unique combination of strength and speed. Volumetric attacks can easily overwhelm on-premise hardware-based DDoS protection appliances and their bandwidth-constrained Internet links.</p>
<p>A cloud-based DDoS protection solution is more agile, efficient and scalable but most solutions on the market lack the global network footprint and scrubbing center density required to maintain good network performance. DDoS protection solutions with such shortcomings require redirecting customer traffic through sparsely located scrubbing centers that are often thousands of miles away from where the traffic was originally ingested into the network, adding significant latency that inevitably impacts the end-to-end network performance and throughput.</p>
<p>Cloudflare Magic Transit provides cloud-native, in-line DDoS protection and traffic acceleration for all your Internet-facing networks that serve incoming user traffic from the Internet, regardless of where they are deployed, whether on-premise, in the cloud, or a combination of the two (that is, hybrid architecture). With data centers spanning hundreds of cities and with hundreds of Tbps in DDoS mitigation capacity, Magic Transit can detect and mitigate attacks close to their source of origin in under 3 seconds globally.</p>
<p>The details of how Magic Transit works and how it can be architected for various use cases are documented in the related resources at the end of this document - <a href="/magic-transit/">Cloudflare Magic Transit</a> and <a href="/reference-architecture/architectures/magic-transit/">Magic Transit Reference Architecture</a>.</p>
<p>This document will focus specifically on, for a few common scenarios, the reference architectures of using Magic Transit to protect a hybrid cloud based network infrastructure.</p>
<h2 id="scenario-1-customer-byoip-for-both-on-premise-and-cloud-network-deployments">Scenario 1 - Customer BYOIP for both on-premise and cloud network deployments</h2>
<p>In this scenario, there are multiple /24 or larger network prefixes that need to be protected by Magic Transit. These networks are deployed at on-premise locations as well as across multiple cloud providers’ regions.</p>
<p>For illustration purposes, below is an example list of the locations of Internet-facing networks and their respective IP prefixes.</p>
<pre><code class="language-txt">AWS VPC: 192.0.2.0/24&#10;GCP VPC: 198.51.100.0/24&#10;Azure vNet: 203.0.113.0/26&#10;On-premise data center 1: 203.0.113.64/26&#10;On-premise data center 2: 203.0.113.128/25&#10;</code></pre>
<p><img src="/assets/upstream/images/reference-architecture/protect-hybrid-cloud-networks-with-cloudflare-magic-transit/figure-1.svg" alt="Figure 1: Customer BYOIP for all Cloud and on-premises networks." title="Figure 1: Customer BYOIP for all Cloud and on-premises networks." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<ol>
<li>Using Border Gateway Protocol (<a href="https://www.cloudflare.com/learning/security/glossary/what-is-bgp/">BGP</a>), Cloudflare advertises customer’s protected IP prefixes to the Internet from all of Cloudflare’s global data centers, enabling <a href="https://www.cloudflare.com/learning/cdn/glossary/anycast-network/">IP Anycast</a>, so that Internet traffic destined to these protected IP prefixes will always be routed to the Cloudflare data center that is closest to the source of the traffic.</li>
</ol>
<p>At the same time, on-premise network(s) and cloud provider network(s) would stop advertising the same exact prefixes from their respective on-premises border routers and cloud border routers. This ensures all Internet traffic destined to the Magic Transit protected IP prefixes will be routed through the Cloudflare network.</p>
<p>You can instead advertise less-specific IP prefixes from their border routers to the Internet. This way, if the Magic Transit service ever experiences a failure in a very unlikely event, traffic can be quickly re-routed directly to network locations from the Internet.</p>
<ol start="2">
<li>Traffic originated from the Internet and destined to the protected IP prefixes is ingested into Cloudflare network globally.</li>
<li>All traffic is scrubbed, that is, DDoS attack traffic is removed and mitigated in-line at every Cloudflare data center using advanced and automated <a href="/ddos-protection/">DDoS mitigation</a> technologies.</li>
<li>Traffic that passes DDoS mitigation is subjected to additional network firewall filtering using the included <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> service.</li>
<li>Clean, filtered traffic is routed to the protected networks either through private connections called <a href="/network-interconnect/">Cloudflare Network Interconnect</a> (CNI), or through the public Internet using standard IP tunnels such as GRE or IPsec tunnels. More specific details on Magic Transit IP tunnels can be found in the <a href="/magic-transit/reference/gre-ipsec-tunnels/">Magic Transit Tunnels and Encapsulation documentation</a>.</li>
<li>The server return traffic from protected IP prefixes to the Internet users are routed directly over the Internet from the hybrid cloud locations, bypassing the Cloudflare network. This is called direct server return (DSR). Note you must have BYOIP with your Cloud Service Provider to use DSR.</li>
</ol>
<p>With Magic Transit service being the single, consolidated cloud-native network protection solution running globally on the Cloudflare network, your global, hybrid cloud based Internet-facing networks are well protected from DDoS and other malicious attacks, regardless where and what environments they are deployed in.</p>
<p>One other added benefit of using such consolidated, cloud-native network protection solutions is that you can easily migrate or relocate Internet-facing networks between the various hybrid cloud environments without ever losing protection to these networks. They can do so by simply changing routes in the Magic Transit configuration to route traffic to the new location.</p>
<h2 id="scenario-2-customer-lease-ip-address-from-cloudflare-for-both-on-premise-and-cloud-network-deployments">Scenario 2 - Customer lease IP address from Cloudflare for both on-premise and cloud network deployments</h2>
<p>In the case where you do not own any network prefixes that are equal to or larger than /24, but would still like to use Magic Transit to protect their networks, you can <a href="/magic-transit/cloudflare-ips/">lease IPs</a> from Cloudflare to assign to these smaller networks. The following diagram illustrates the architecture of such a deployment. Similar to the previous scenario, these customer networks are deployed at on-premise locations as well as across multiple cloud providers’ regions.</p>
<p>For illustration purposes, below is an example list of the locations of Internet-facing networks and their respective IP prefixes.</p>
<pre><code class="language-txt">AWS VPC: 192.0.2.0/28&#10;GCP VPC: 192.0.2.16/28&#10;Azure vNet: 192.0.2.32/28&#10;On-premise data center 1: 192.0.2.48/28&#10;On-premise data center 2: 192.0.2.64/28&#10;</code></pre>
<p><img src="/assets/upstream/images/reference-architecture/protect-hybrid-cloud-networks-with-cloudflare-magic-transit/figure-2.svg" alt="Figure 2: Customer lease IPs from Cloudflare for both on-premise and cloud network deployments." title="Figure 2: Customer lease IPs from Cloudflare for both on-premise and cloud network deployments." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<ol>
<li>Using Border Gateway Protocol (BGP), Cloudflare advertises its owned IP prefixes to the Internet, which includes the IP addresses that you lease.</li>
</ol>
<p>[Steps 2 through 5 are the same as those of scenario 1 above]</p>
<ol start="6">
<li>The server return traffic, with leased Cloudflare IP addresses as their source IP addresses, cannot be routed to the Internet directly via the various sites’ border routers. This traffic has to be routed back through Cloudflare network to reach the Internet, using <a href="/magic-transit/reference/egress/">Magic Transit Egress</a> functionality. It can be sent to the Cloudflare network via the same CNIs or IP tunnels that the Ingress traffic traversed, using routing techniques such as policy-based routing (PBR) at your sites.</li>
<li>Magic Transit Egress traffic is subject to Network Firewall filtering before being routed out to the Internet towards the users.</li>
</ol>
<h2 id="scenario-3-customer-byoip-for-on-premise-networks-and-lease-ip-address-from-cloudflare-for-cloud-network-deployments">Scenario 3 - Customer BYOIP for on-premise networks and lease IP address from Cloudflare for cloud network deployments</h2>
<p>In this scenario, you can deploy larger on-premise networks and smaller cloud-based networks. You assign your own /24 IP prefixes to the on-premise networks while leasing IPs from Cloudflare for your cloud-based networks.</p>
<p>For illustration purposes, below is an example list of the locations of Internet-facing networks and their respective IP prefixes.</p>
<pre><code class="language-txt">AWS VPC: 192.0.2.0/28&#10;GCP VPC: 192.0.2.16/28&#10;Azure vNet: 192.0.2.32/28&#10;On-premise data center 1: 198.51.100.0/24&#10;On-premise data center 2: 203.0.113.0/24&#10;</code></pre>
<p><img src="/assets/upstream/images/reference-architecture/protect-hybrid-cloud-networks-with-cloudflare-magic-transit/figure-3.svg" alt="Figure 3: Customer BYOIP for on-premise networks and lease IP from Cloudflare for cloud network deployments." title="Figure 3: Customer BYOIP for on-premise networks and lease IP from Cloudflare for cloud network deployments." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<ol>
<li>Using Border Gateway Protocol (BGP), Cloudflare advertises both customer-owned and Cloudflare-owned IP prefixes to the Internet.</li>
</ol>
<p>[Steps 2 through 5 are the same as those of scenario 1 above]</p>
<ol start="6">
<li>The server return traffic from your cloud-based networks is routed back through Cloudflare network to reach the Internet, using Magic Transit Egress functionality. It can be sent to the Cloudflare network via the same CNIs or IP tunnels that the Ingress traffic traversed, using routing techniques such as policy-based routing (PBR) at your physical sites.</li>
<li>This Magic Transit Egress traffic is subject to Network Firewall filtering before being routed out to the Internet towards the users.</li>
<li>The server return traffic from on-premises networks to the Internet users are direct server returned (DSR), bypassing the Cloudflare network.</li>
</ol>
<p><em>Note</em>: Alternatively, customers can choose to also route the on-premise networks’ server return traffic through Cloudflare via policy-based routing and Magic Transit Egress functionality. This adds an additional layer of security and control for the egress traffic with Network Firewall filtering. For example, it can block traffic destined to questionable IP addresses and sites, prohibited destinations, or countries.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/reference-architecture/architectures/magic-transit/">Magic Transit Reference Architecture</a></li>
<li><a href="/magic-transit/">Cloudflare Magic Transit</a></li>
<li><a href="/network-interconnect/">Cloudflare Network Interconnect</a></li>
<li><a href="/ddos-protection/">Cloudflare DDoS Protection</a></li>
<li><a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a></li>
<li><a href="/cloudflare-wan/reference/device-compatibility/">Cloudflare IPsec Device Compatibility Matrix</a></li>
<li><a href="/magic-transit/cloudflare-ips/">Cloudflare Magic Transit Leased IP</a></li>
</ul>
