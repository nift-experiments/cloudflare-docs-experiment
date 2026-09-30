<h2 id="introduction">Introduction</h2>
<p>Cloudflare helps organizations transform their networks by providing secure, high-performance connectivity for on-premises networks, virtual cloud networks and access to SaaS applications. As applications migrate to the cloud, <a href="https://www.cloudflare.com/zero-trust/">Cloudflare's SASE</a> platform enables businesses to replace traditional on-premise solutions, ensuring secure access, low latency, and automated scalability across distributed environments. This approach reduces reliance on legacy hardware, simplifies IT management, and improves user experience for cloud-based services.</p>
<p>Cloudflare One Appliance (formerly Magic WAN Connector) is a physical, or virtual (deployed as a VM on a hypervisor) device which, using <a href="https://en.wikipedia.org/wiki/Zero-touch_provisioning">Zero Touch Provisioning</a>, automatically on-ramps traffic for a local network to Cloudflare, and replaces existing, difficult to manage edge hardware.</p>
<p>Every organization and network is different, and as such there is no one-size-fits-all when it comes to how a Cloudflare One Appliance can be deployed. Therefore, the purpose of this document is to provide a high-level explanation of the deployment options that would make sense to most environments, while also describing the support of a few advanced use cases.</p>
<h2 id="deployment-locations">Deployment locations</h2>
<p>The first decision for a Cloudflare One Appliance deployment is its location in the network, and this relates to whether the organization wants to keep the existing Customer Premises Equipment (CPE, edge router or firewall at a site), and if so, for what reason. Experience shows that this decision usually leads to three different topologies:</p>
<ul>
<li>
<p><strong>Connector replacing the CPE</strong> (Figure 1a): When the link is an Internet connection and the organization does not have any real use of existing equipment since the Connector supports all the required networking features such as DHCP, DNS, NAT, Trunking (801.1Q), IP access lists, breakout traffic, etc. Examples could be:</p>
<ul>
<li>The transition from MPLS to Internet-based connectivity, where the MPLS router probably does not add any value in the deployment.</li>
<li>An Internet-facing CPE reaching, or already having exceeded, its end of life.</li>
<li>An Internet-facing CPE that is redundant with Cloudflare One Appliance and can be removed for simplicity's sake.</li>
</ul>
</li>
<li>
<p><strong>Connector north of the CPE</strong> (Figure 1b): This option might be preferred when the existing CPE is a firewall, and the organization wants to keep it for:</p>
<ul>
<li>Additional LAN protection as a result of a defense-in-depth approach.</li>
<li>Advanced segmentation requirements, for example allowing/blocking traffic between segments based on various Layer 3 to Layer 7 rules, since Cloudflare One Appliance supports segmentation only on layers 3 and 4 of the OSI model.</li>
</ul>
</li>
<li>
<p><strong>Connector south of the CPE</strong> (Figure 1c): Reasons for installing Cloudflare One Appliance south of an existing Internet-facing CPE might be:</p>
<ul>
<li>CPE cannot be replaced because it connects to a broadband service with a presentation (for example RJ-11) or protocol (for example PPPoE) that Cloudflare One Appliance does not support.</li>
<li>CPE cannot be replaced because it is part of a fiber service that only works with that specific hardware, such as an ISP-provided ONT (Optical Network Terminal).</li>
<li>CPE cannot be replaced (yet) because it is part of an active managed service.</li>
<li>CPE cannot be replaced because it is a firewall that the organization wants to keep in place for other reasons (technical or contractual).</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-appliance-deployment/figure01.svg" alt="Figure 1: Connector location options: (a) replacing CPE, (b) north of CPE , (c) south of CPE." title="Figure 1. Connector location options: (a) replacing CPE, (b) north of CPE , (c) south of CPE" /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<h2 id="high-availability">High availability</h2>
<p>In Wide Area Network (WAN) environments, where remote offices, data centers, and cloud services are interconnected, any downtime can lead to loss of access to critical applications, communication disruptions, and productivity losses. To avoid such downtimes, WAN networks are mostly designed with High Availability (HA) principles in mind. Deploying redundant hardware and uplink circuits, as well as failover mechanisms, ensures that if one component fails, another can immediately take over. This resilience is key to maintaining seamless connectivity, reliability, and service continuity in distributed networks.</p>
<h3 id="uplink-ha">Uplink HA</h3>
<p>Cloudflare One Appliance can use two or more WAN ports for uplinks, and therefore it can connect to multiple different ISPs for circuit resiliency. One option for a basic level of HA is to use a single Cloudflare One Appliance with two uplinks, while traffic can be load-balanced between them (Figure 2 below). This approach could be used for non-critical branches, small offices, and other similar types of locations, or as an intermediate step towards a full HA deployment.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-appliance-deployment/figure02.svg" alt="Figure 2. Uplink high-availability deployment." title="Figure 2. Uplink high-availability deployment." /></p>
<h3 id="full-ha">Full HA</h3>
<p>In this type of setup, a redundant device is configured to take over in case of a failure in the primary device, allowing seamless traffic failover and ensuring uninterrupted access to applications, data, and services. This approach enhances network resilience, improves service reliability, and helps maintain productivity by reducing the risk of single points of failure.</p>
<p>Figure 3 below illustrates the deployment topology where Cloudflare One Appliance supports full HA. Using an election process, one device becomes active and the other becomes passive. To achieve this, the two Connectors must connect to a LAN switch on the same Layer 2 domain (like a VLAN) for heartbeat messages to be sent between them. Active/passive means that the active Connector is the only device that propagates traffic at any point in time.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-appliance-deployment/figure03.svg" alt="Figure 3. Full HA with dual Connectors and dual uplinks." title="Figure 3. Full HA with dual Connectors and dual uplinks." /></p>
<p>Each Cloudflare One Appliance connects to the same two ISPs using dual uplinks, and automatically creates one IPsec tunnel per WAN port. This requires each ISP to support multiple ports on their on-site Network Termination Unit (or their CPE, if there is one present). In this HA deployment there are four tunnels in total, two per Connector, while traffic can be load-balanced between the two tunnels on the active device. When either the active Connector, or its IPsec tunnels go down, the other Connector takes over and propagates traffic, holding the active role until it fails (preemption is not used to avoid unnecessary failover delays).</p>
<h2 id="advanced-use-cases">Advanced use cases</h2>
<p>This section describes how the Cloudflare One Appliance can be deployed to support a few advanced use cases, that is, use cases beyond the typical scenarios where the Connector acts as a simple CPE that on-ramps traffic to Cloudflare for site-to-site, or site-to-Internet, connectivity and protection.</p>
<h3 id="protecting-local-internet-breakout-libo">Protecting local Internet breakout (LIBO)</h3>
<p>The main use case for this type of deployment is based on the fact that many organizations today require local Internet breakout to improve the performance of Cloud and SaaS applications, while they probably continue to use their private MPLS connectivity for self-hosted applications, or site-to-site connectivity, until they decide to further modernize their architectures at a later stage. Reasons behind such a decision might be:</p>
<ul>
<li>MPLS service is still in contract, but it is planned to be replaced by Internet connectivity everywhere when the term ends</li>
<li>Self-hosted applications might require low latency with agreed SLAs, so a hybrid MPLS/Internet architecture might be required</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-appliance-deployment/figure04.svg" alt="Figure 4. Hybrid MPLS/Internet use case." title="Figure 4. Hybrid MPLS/Internet use case." /></p>
<p>This type of hybrid architecture requires the MPLS Customer Edge router (CE) or some other L3 device in the LAN to route traffic via different interfaces depending on the destination. Traffic flows in this scenario as follows:</p>
<ol>
<li>Devices on the local network use the MPLS CE (or some other local L3 device) as their default gateway</li>
<li>Private traffic is sent towards the MPLS network. For example, the MPLS CE knows how to route these because it receives RFC1918 ranges via BGP from the MPLS network.</li>
<li>Internet traffic from the LAN network is forwarded towards the Cloudflare One Appliance (MPLS CE/L3 gateway points a static default route towards the Connector)</li>
</ol>
<p>All traffic towards internal locations and self-hosted applications follows the MPLS path, while traffic to cloud-based and SaaS applications follows the local Internet breakout path, protected by Cloudflare security services.</p>
<h3 id="split-tunneling">Split tunneling</h3>
<p>In some deployments, customers might want to protect only specific protocols using Cloudflare security services such as our <a href="/cloudflare-one/traffic-policies/">secure web gateway</a>, while the rest of the traffic routes through the existing edge device (router or firewall). Figure 5 illustrates such a use case.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-appliance-deployment/figure05.svg" alt="Figure 5. 'Split Tunneling' use case." title="Figure 5. 'Split Tunneling' use case." /></p>
<p>In this example, the organization wants Cloudflare to protect all Internet web traffic (HTTP/HTTPS), while the rest of the traffic flows out via the existing firewall. The latter could be traffic towards existing VPNs, or non-web traffic exiting the site, but protected by the on-premises firewall. This method could take advantage of local device policy-based routing (PBR) capabilities, for example:</p>
<ol>
<li>Local devices use the on-premises firewall as their default gateway</li>
<li>Firewall uses PBR to direct appropriate traffic to the right destination</li>
<li>Web traffic (TCP 80/443) is sent towards Cloudflare via the Cloudflare One Appliance</li>
<li>All other traffic exits via the on-premises firewall</li>
</ol>
<p>As long as PBR capability exists locally, and the ISP provides at least two public IP addresses to the organization, the possibilities of splitting traffic towards the Cloudflare One Appliance are endless, and really depend on each organization's unique environment and use cases.</p>
<h3 id="protecting-segments-segmentation">Protecting segments / segmentation</h3>
<p>Another advanced group of use cases that Cloudflare One Appliance can support is local segmentation, and protection of specific local networks. To achieve that, and depending on an organization's current architecture, line of business, security policies, and compliance requirements, Cloudflare One Appliance can be installed in any location south of the site edge device to provide more granular network security, as illustrated in figure 6 and described in the following paragraphs.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-appliance-deployment/figure06.svg" alt="Figure 6. Segmentation-related use cases." title="Figure 6. Segmentation-related use cases." /></p>
<p>In this example, the Cloudflare One Appliance will create an IPsec tunnel to Cloudflare through the on premises firewall and local Internet connection. Subnet A and B are both connected to the Cloudflare One Appliance, but have no direct connection with each other. This will enable a couple of use cases:</p>
<ul>
<li><strong>Internet security</strong>: Segment 1 adheres to Cloudflare security policies, bypassing the local firewall policy.</li>
<li><strong>Site-to-site connectivity</strong>: Segment 1 can connect to local segments in other locations (or entire sites, for example Site 2), depending on the organization's policy.</li>
</ul>
<p>The example also shows how Cloudflare One Appliance can be used to provide two types of local network segmentation:</p>
<ul>
<li><strong>Intra-segment</strong>: Traffic between LAN ports on the same Connector is blocked by default, hence, Subnet A and Subnet B in Segment 1 cannot talk to each other. The administrator would have to explicitly allow this traffic flow by using configuration logic similar to IP access lists. This ability to hairpin local traffic via the Connector's LAN ports, avoids traffic tromboning via the Cloudflare platform (that is, travel out and back in via the IPsec/GRE tunnel), which could result in those segments losing connectivity to each other in the event of Internet circuit outage. Therefore, this capability allows local nodes that do not necessarily require Internet access to function, for example printers, file servers, network attached storage (NAS) nodes, and various Internet of Things (IoT) devices, to continue being accessible by local hosts in different segments during Internet outages.</li>
<li><strong>Inter-segment</strong>: Cloudflare One Appliance does not allow any inbound traffic on its WAN ports. Therefore, Segments 1 and 2 cannot talk to each other.</li>
</ul>
<p>To summarize, Cloudflare One Appliance is a Zero-Touch Provisioning (ZTP) device that organizations can use to connect to Cloudflare and consume advanced security and connectivity services, while keeping operational costs low.</p>
<h2 id="related-resources">Related Resources</h2>
<ul>
<li><a href="https://www.cloudflare.com/en-gb/network-services/products/magic-wan/">Cloudflare WAN - Cloud-delivered enterprise networking</a></li>
<li><a href="https://blog.cloudflare.com/magic-wan-connector/">Announcing the Cloudflare One Appliance: the easiest on-ramp to your next generation network</a></li>
<li><a href="/cloudflare-wan/configuration/appliance/">Configuring Cloudflare One Appliance</a></li>
</ul>
