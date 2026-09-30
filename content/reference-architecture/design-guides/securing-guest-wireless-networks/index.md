<h2 id="introduction">Introduction</h2>
<p>Many organizations and businesses offer free wireless Internet access to their customers, clients, patients, students, and visitors. In industries like hospitality, providing guest Wi-Fi is often essential. For colleges and universities, having a reliable and secure Wi-Fi service can be a significant factor in attracting potential students and visitors.</p>
<p>Offering free wireless Internet access brings several benefits. Businesses use guest Wi-Fi to enhance customer engagement by directing users to landing pages for marketing campaigns or offering coupons. Additionally, many guest Wi-Fi systems collect valuable user analytics, such as email addresses, browsing behavior, and even dwell time in specific locations. This data can help influence decisions like product placement in stores or drive follow-up email marketing campaigns.</p>
<p>However, providing guest Wi-Fi also introduces risks. Malicious users could exploit your network for illegal activities, such as accessing prohibited content, purchasing contraband, or engaging in cybercrime. In some cases, businesses like hotels, cafes, and libraries have faced lawsuits for allegedly enabling illegal downloads through their guest Wi-Fi. These lawsuits, often filed by copyright holders, claim that businesses facilitated piracy by failing to monitor or control the content accessed or downloaded by their guests.</p>
<p><img src="/assets/upstream/images/reference-architecture/securing-guest-wireless-networks/figure1.svg" alt="Figure 1: Guest networks are often directly connected to the Internet with little security." title="Figure 1: Guest networks are often directly connected to the Internet with little security." /></p>
<p>While it may be unlikely that your organization could face criminal charges, your organization could become part of lengthy investigations, potentially resulting in legal expenses and reputation damage. In this guide, you will learn how Cloudflare can help minimize risk, provide visibility into guest Internet activity and <a href="https://www.cloudflare.com/zero-trust/solutions/secure-guest-wifi/">better secure your guest wireless network</a>.</p>
<h3 id="who-is-this-document-for-and-what-will-you-learn">Who is this document for and what will you learn?</h3>
<p>This reference architecture is designed for IT or security professionals who are looking at Cloudflare to help secure their guest wireless networks. To build a stronger baseline understanding of Cloudflare, we recommend the following resources:</p>
<ul>
<li>What is Cloudflare? | <a href="https://www.cloudflare.com/what-is-cloudflare/">Website</a> (5 minute read) or <a href="https://www.youtube.com/watch?v=XHvmX3FhTwU">video</a> (2 minutes)</li>
<li>Cloudflare Zero Trust | <a href="https://www.cloudflare.com/zero-trust/">https://www.cloudflare.com/zero-trust/</a></li>
<li>SASE Architecture with Cloudflare | <a href="/reference-architecture/architectures/sase/">/reference-architecture/architectures/sase/</a></li>
</ul>
<p>This reference architecture guide will help readers understand:</p>
<ol>
<li><strong>Cloudflare Gateway DNS</strong>: Learn how to integrate Cloudflare Gateway DNS policies into common guest wireless deployment scenarios.</li>
<li><strong>Best practices for DNS policies</strong>: Discover effective methods for building guest wireless DNS policies to enforce your acceptable use policy and prevent malicious activities.</li>
<li><strong>Enhanced visibility and security</strong>:</li>
</ol>
<ul>
<li>Use the Cloudflare Zero Trust dashboard to access detailed logs and analytics, offering insights into DNS queries, traffic patterns, and potential security threats.</li>
<li>Enable <strong>Logpush</strong> to export logs to external storage solutions for long-term analysis or compliance purposes.</li>
<li>Integrate with your SIEM (Security Information and Event Management) platform to correlate Cloudflare logs with other security data, streamlining incident detection and response.</li>
</ul>
<h3 id="gateway-dns">Gateway DNS</h3>
<p>Cloudflare offers an enhanced, protected DNS resolver service for Zero Trust customers. This service utilizes Anycast, a routing technology that enables multiple servers or data centers to share the same IP address. When a request is sent to an Anycast IP address, routers use the Border Gateway Protocol (BGP) to direct the request to the nearest server. As a result, DNS queries are always routed to the closest Cloudflare data center based on your location. With data centers in <div class="nb-data-component" data-cf-component="PublicStats"></div>, Cloudflare operates one of the <a href="https://www.cloudflare.com/network/">largest global networks</a>. This service can also strengthen your organization's security by enabling the creation of policies to filter DNS resolutions for potentially malicious, questionable, or inappropriate destinations. This guide explains how to enable this service and configure your environment to secure guest wireless networks, reducing risks to your organization.</p>
<h3 id="dns-locations">DNS locations</h3>
<p>Cloudflare <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations</a> are a collection of DNS endpoints which can be mapped to physical entities such as offices, homes or data centers. <a href="/cloudflare-one/traffic-policies/">Gateway</a> identifies locations differently depending on the DNS query protocol. IPv4 traffic is identified from the source IP address from which a DNS query originated. IPv6 traffic can be identified by the unique IPv6 resolver address created in the Cloudflare dashboard. The following sections describe how to ensure DNS queries are appropriately mapped to your physical locations depending on the network environment and protocols being used. Later in this document you will learn how to use the location's IP address as an attribute which you can apply to Gateway DNS policies.</p>
<p>The goal is to have DNS requests from your Wi-Fi networks be sent via Cloudflare's secure DNS and secure web gateway service, where your DNS policies can filter requests and block those you deem risky. This guide walks through the different possible network architectures you might have for guest networks and gives guidance on how to implement Cloudflare to protect devices on those guest Wi-Fi networks.</p>
<h2 id="securing-guest-traffic-sourced-from-a-basic-wireless-router">Securing guest traffic sourced from a basic wireless router</h2>
<h3 id="using-business-internet-and-a-static-ipv4-address">Using business Internet and a static IPv4 address</h3>
<p>A common method for providing guest wireless access is to set up a completely separate network from the corporate or production network. For example, a branch office or retail store might use a single wireless router to achieve this. The router would broadcast a guest wireless Service Set Identifier (SSID), assign IP addresses to connected devices, and provide Internet connectivity. The public static IPv4 address assigned to the router can then serve as a DNS location attribute in the Cloudflare Zero Trust dashboard. If the router's IP address is dynamically assigned by your ISP refer to the section &quot;Dedicated DNS resolver IPv4 and IPv6 addresses&quot;.</p>
<p>To route all DNS queries through Cloudflare, update your router's DNS settings in the WAN interface to use Cloudflare's resolver IP addresses. The specific resolver IPs for Zero Trust can be found in the DNS location settings in the Cloudflare dashboard. Refer to your router's manufacturer documentation for detailed configuration steps to update the WAN interface. Typically, devices connected via Wi-Fi will use the router's IP address as their DNS server. The router forwards the DNS queries to Cloudflare on their behalf. As a result, DNS queries from the wireless devices will be sent Cloudflare and originate from the static IP address assigned to the router.</p>
<p>For enhanced security, prevent wireless guests from accessing other DNS services by creating a firewall rule on the router (if supported). This rule should allow access only to Cloudflare's DNS servers and block all other DNS destinations on UDP/TCP port 53. Additionally, some advanced wireless routers support content filtering. If available, enable options to block DNS over TLS (DoT) or DNS over HTTPS (DoH) to ensure endpoints cannot bypass your configured DNS security settings in Cloudflare.</p>
<p><img src="/assets/upstream/images/reference-architecture/securing-guest-wireless-networks/figure2.svg" alt="Figure 2: When DNS queries are forwarded to Cloudflare, policies can be implemented to prevent access to malicious and high risk destinations. Guest-Security-Block and Guest-Content-Block refer to the specific DNS policies applied to the wireless guest devices." title="Figure 2: When DNS queries are forwarded to Cloudflare, policies can be implemented to prevent access to malicious and high risk destinations.  `Guest-Security-Block` and `Guest-Content-Block` refer to the specific DNS policies applied to the wireless guest devices." /></p>
<h2 id="secure-guest-traffic-sourced-from-an-enterprise-network">Secure guest traffic sourced from an enterprise network</h2>
<p>Some companies go beyond using consumer or semi professional grade, all in one wireless routers and deploy guest Wi-Fi access on top of an existing enterprise networking solution. For example, the same Wi-Fi access point hardware might be broadcasting both the enterprise internal network as well as the guest network.</p>
<h3 id="segment-internal-and-guest-networks">Segment internal and guest networks</h3>
<p>A common approach to separating internal and guest networks involves the use of distinct SSIDs. The internal corporate SSID and the guest wireless SSID can be linked to separate VLANs (Virtual Local Area Networks) or <a href="https://en.wikipedia.org/wiki/IEEE_802.1Q">Dot1q tags</a>, providing virtual segmentation between the networks.</p>
<p>In this configuration:</p>
<ol>
<li>A subnet is assigned to the guest wireless VLAN.</li>
<li>The default gateway for that subnet is configured on an interface (or virtual interface) of an upstream network device such as a firewall or router.</li>
<li>The device segments guest network traffic from internal network traffic while also acting as a secure gateway to the public Internet.</li>
</ol>
<h3 id="configure-dns-for-the-guest-network">Configure DNS for the guest network</h3>
<p>Similar to simpler setups, DNS queries from guest wireless devices should be forwarded to Cloudflare's resolver IPs. You can achieve this by:</p>
<ul>
<li>Assigning Cloudflare DNS servers in the DHCP scope for guest devices.</li>
<li>Configuring the upstream network device to proxy DNS queries to Cloudflare.</li>
</ul>
<p>Note, you might also be providing guest devices access to some internal resources, and as such you might configure clients to use an internal DNS service. You can also set up this service to forward Internet bound DNS requests to Cloudflare.</p>
<p>To enhance security, configure outbound Internet firewall rules to allow DNS queries only to Cloudflare's enterprise resolver IPs on TCP/UDP port 53.</p>
<h3 id="assign-a-unique-public-ipv4-address-for-guest-traffic">Assign a unique Public IPv4 address for guest traffic</h3>
<p>To ensure guest traffic is sourced from a unique public IPv4 address:</p>
<ol>
<li>Create a Port Address Translation (PAT) policy on your firewall or edge device specifically for guest traffic.
<ul>
<li>PAT (or NAT overload) allows multiple devices on the local network to access the Internet using a single public IP address.</li>
</ul>
</li>
<li>Define the source address range as the guest subnet in the firewall settings.</li>
<li>Specify the translated source address—a public IPv4 address—to be used for all Internet-bound traffic originating from the guest network.</li>
</ol>
<p>Refer to your firewall manufacturer's documentation for detailed instructions on setting up a PAT or NAT overload rule.</p>
<h3 id="map-guest-traffic-in-cloudflare">Map guest traffic in Cloudflare</h3>
<p>Once guest network traffic is assigned a unique public IPv4 address, this address can be used as an attribute in the Cloudflare dashboard to map your DNS location effectively.</p>
<p><img src="/assets/upstream/images/reference-architecture/securing-guest-wireless-networks/figure3.svg" alt="Figure 3: This diagram shows how guest Wi-Fi traffic has different DNS filtering policies versus your use of our Gateway DNS service to secure corporate network traffic." title="Figure 3: This diagram shows how guest Wi-Fi traffic has different DNS filtering policies versus your use of our Gateway DNS service to secure corporate network traffic." /></p>
<h2 id="secure-guest-wireless-at-locations-with-a-dynamically-assigned-public-ipv4-or-ipv6-address">Secure guest wireless at locations with a dynamically assigned public IPv4 or IPv6 address</h2>
<h3 id="dedicated-dns-resolver-ipv4-and-ipv6-addresses">Dedicated DNS resolver IPv4 and IPv6 addresses</h3>
<p>If you are unable to use a static public IP address on your edge device, Cloudflare offers dedicated IPv4 and IPv6 resolver endpoint addresses that can be assigned specifically to your organization. In this scenario, the destination address to which DNS queries are sent can serve as a method to map your physical location to a Cloudflare DNS endpoint.</p>
<p>Cloudflare provides unique IPv6 resolver endpoint addresses at no cost through the Zero Trust dashboard. However, due to the limited availability of IPv4 addresses, dedicated IPv4 DNS endpoints are only available with Cloudflare Enterprise plans.</p>
<p>For example, if your guest wireless router is dynamically assigned an IPv6 address and an IPv6 DNS server by your ISP, you can modify the IPv6 DNS address to match the IPv6 DNS endpoint address configured in your Cloudflare DNS Location settings.</p>
<h3 id="add-dns-locations">Add DNS locations</h3>
<p>Now that we have covered various options for sending DNS queries to Cloudflare's DNS resolvers and identifying your organization's guest wireless network—either by its source IP address or a dedicated resolver address—you're ready to create new locations in Zero Trust.</p>
<p>To get started, navigate to <strong>DNS Locations</strong> in the Zero Trust dashboard. For detailed, step-by-step instructions, refer to the <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/"><strong>DNS Locations</strong></a> guide. When using IPv4 or IPv6 endpoint filtering and location matching, you can define a network and subnet mask in CIDR notation to represent your location's source IP addresses. For example:</p>
<ul>
<li>If all your wireless networks share a public IP address within the same subnet, you can apply a policy to all locations at once using a single DNS location object.</li>
<li>To assign unique policies to specific locations, use a host address ending in /32 to represent each location individually.</li>
</ul>
<h3 id="creating-dns-policies">Creating DNS policies</h3>
<p>To get started, navigate to firewall policies and select DNS in the Zero Trust dashboard. For detailed, step-by-step instructions, refer to the <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS Policies</a> guide.</p>
<p>To keep your policies organized, we recommend using meaningful names that clearly indicate their purpose. For instance, a policy named <strong>Guest-Security-Block</strong> conveys:</p>
<ul>
<li><strong>Guests</strong>: Who the policy applies to.</li>
<li><strong>Security</strong>: The type of content being evaluated.</li>
<li><strong>Block</strong>: The action being taken.</li>
</ul>
<p>Cloudflare provides a range of managed categories which you can use to filter a wide range of different types of threats. For example, adding into the DNS policy the <a href="/cloudflare-one/traffic-policies/domain-categories/#security-categories">security category</a> Malware will prevent a connected device from making a DNS request to any site that Cloudflare has tagged as being known as part of a malware campaign or might be hosting malware. As well as security categories, we also have <a href="/cloudflare-one/traffic-policies/domain-categories/#content-categories">content categories</a> which identify sites such as Cryptocurrency, P2P sharing sites or adult themed sites. Cloudflare also manages a list of <a href="/cloudflare-one/traffic-policies/application-app-types/">applications</a>, so you can filter access to public cloud storage or file sharing sites.</p>
<p>Cloudflare also allows <a href="/security-center/indicator-feeds/#publicly-available-feeds">custom feeds</a> where you can either subscribe to another vendor to provide a list of sites to filter, or you can use some of the built in government based threat feeds. This allows you to be very selective about what sites you wish to filter.</p>
<p>For devices making requests from known DNS locations, it's also possible to add these to the policy. So you can create different policies for different guest Wi-Fi locations. This can help with situations where local laws require you to prevent access to a specific type of Internet site.</p>
<p>Policies can be made up of multiple rules, so a single policy can prevent access to high risk websites as well as inappropriate content.</p>
<h3 id="recommended-policies">Recommended policies</h3>
<p>Cloudflare has several additional recommended DNS policies that can be found in the <a href="/learning-paths/secure-internet-traffic/build-dns-policies/recommended-dns-policies/">Secure your Internet traffic implementation guide</a>. These policies are designed to enhance your organization's overall security and should also be factored in when setting up policies for your internal production web traffic.</p>
<h3 id="visibility-into-guest-dns-internet-activity">Visibility into Guest DNS Internet Activity</h3>
<p>With DNS traffic now routed through Cloudflare and your wireless networks secured, you can gain detailed visibility into your guests' Internet activity using logs and advanced logging tools. Every DNS request is <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">logged</a> in Cloudflare and our dashboard provides a simple search interface. These logs help you understand how your policies are applied and detect trends or patterns in guest Internet usage, providing actionable insights to fine-tune your security configurations.</p>
<p>For advanced telemetry and seamless data management, consider enabling <strong>Logpush</strong> in your Cloudflare dashboard. Sending these logs to an external source, most commonly a SIEM platform, brings the following benefits:</p>
<ul>
<li><strong>Centralized Analysis</strong>: Consolidate logs from multiple Cloudflare services with other organizational data in your SIEM for comprehensive visibility.</li>
<li><strong>Enhanced Threat Detection</strong>: Correlate DNS activity with other security events to detect patterns of malicious behavior more effectively.</li>
<li><strong>Compliance and Audit Readiness</strong>: Store DNS logs for long-term retention to meet regulatory compliance requirements or support incident audits.</li>
<li><strong>Real-Time Alerts</strong>: Leverage SIEM integration to trigger automated alerts and responses based on suspicious DNS activity.</li>
<li><strong>Operational Insights</strong>: Gain a deeper understanding of guest browsing behavior to identify performance bottlenecks or optimize content filtering policies.</li>
</ul>
<p>By leveraging logs, Logpush, and SIEM integrations, you not only enhance visibility into guest Internet activity but also strengthen your organization's overall security posture.</p>
<h2 id="going-beyond-dns-filtering">Going beyond DNS filtering</h2>
<p>Up to this point all methods mentioned have revolved around DNS, mainly due to the fact most traffic over guest Wi-Fi networks will utilize DNS and these configurations do not require any agents or certificates installed on devices, for this reason DNS centric protections are always the recommended starting point when it comes to securing guest Wi-Fi networks. Unfortunately there are ways to bypass DNS based security enforcement like:</p>
<ul>
<li>Changing your dns resolver manually</li>
<li>Using IP address to reach sites (potentially saving IP to fully qualified domain name mappings via host file)</li>
<li>Using non sanctioned VPN clients</li>
</ul>
<p>For these reasons you should also consider applying security in layers and add network centric enforcement to complement the protections provided via DNS.</p>
<p><img src="/assets/upstream/images/reference-architecture/securing-guest-wireless-networks/figure4.svg" alt="Figure 4: This diagram shows how to connect guest networks to Cloudflare and the high level traffic flow to reach Internet resources." title="Figure 4: This diagram shows how to connect guest networks to Cloudflare and the high level traffic flow to reach Internet resources." /></p>
<p>To provide network level filtering, Cloudflare must be in the traffic path for more than just the DNS request. This is achieved by routing Internet-bound traffic over an <a href="https://www.cloudflare.com/learning/network-layer/what-is-ipsec/">IPsec</a> tunnel to Cloudflare. Cloudflare's <a href="/cloudflare-wan/">Cloudflare WAN</a> (formerly Magic WAN) service allows third-party devices to establish IPsec or GRE tunnels to the Cloudflare network. It is also possible to just deploy our <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a>, a pre-configured lightweight network appliance that automatically creates the tunnel back to Cloudflare and can be managed remotely. Once traffic reaches Cloudflare multiple security controls can be overlaid such as:</p>
<ul>
<li>Cloud based network firewall (<a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a>)</li>
<li>Secure web gateway (<a href="/cloudflare-one/traffic-policies/">Gateway</a>)</li>
</ul>
<p>Below is the high level traffic flow that correlates to the above diagram:</p>
<ol>
<li>Internet destined traffic will be routed to cloudflare from connected guest networks, this can be easily done with a policy based route. In most guest Wi-Fi setups devices will only be expected to generate internet bound traffic so in most cases a Policy based route referencing ANY as the destination will be sufficient. Ex Source 192.168.53.0/24 to Destination ANY next hop Cloudflare IPsec tunnel.</li>
<li>Once traffic reaches the cloudflare edge it will first be inspected by Cloudflare Network Firewall. Cloudflare Network Firewall can be used to create network and transport layer blocks which would allow admins to restrict access to certain destination IP's or ports, a common policy could be blocking all DNS traffic not directed towards cloudflare DNS resolvers. Custom lists can be used to import existing lists customers may already have. <a href="/cloudflare-network-firewall/about/ids/">IDS</a> can be enabled to monitor if any guest users are attempting to launch known exploits from your Guest network. Managed threat <a href="/waf/tools/lists/managed-lists/#managed-ip-lists">lists</a> allow you to use cloudflare's auto updated threat intel to block known threats like known malware repositories or botnets.</li>
<li>Traffic is then forwarded to Cloudflare gateway. At gateway network based policies can be created using the same Content categories and Security risks mentioned earlier within DNS based policies, the benefit is when these filters are applied at the network level, even if a user bypasses DNS these policies can still be applied providing multi tiered enforcement. It would be recommended to mirror DNS based rules in accordance with your organization's acceptable use policy. Cloudflare Gateway also acts as a secure outbound proxy and as such can SNAT private address to Internet routable public addresses, by default rfc 1918 addresses will automatically be SNAT to Shared Cloudflare egress ip's. This removes the need for managing PAT directly from your edge device and also provides a layer of privacy as traffic will source from Cloudflare owned ip's when browsing Internet sites. Dedicated Egress ip's unique to your account can also be provided and egress ip selection controlled via policy.</li>
<li>Traffic is now routed to the final Internet destination, return traffic will be routed back through Cloudflare edge and returned to the corresponding IPsec tunnel.</li>
</ol>
<h2 id="summary">Summary</h2>
<p>By following these strategies and leveraging Cloudflare Zero Trust, organizations can offer a secure, reliable, and policy-compliant wireless experience for their guests. These measures not only safeguard networks but also enhance visibility and enable proactive threat mitigation.</p>
<p>If you are interested in learning more about Gateway, or other aspects of the Cloudflare SASE platform, refer to our <a href="/reference-architecture/">Reference Architecture library</a> or our <a href="/">Developer docs</a> to get started.</p>
<h2 id="related-resources">Related Resources</h2>
<ul>
<li><a href="/reference-architecture/architectures/sase/">Evolving to a SASE architecture with Cloudflare</a></li>
<li><a href="/reference-architecture/diagrams/sase/cloudflare-one-appliance-deployment/">Cloudflare One Appliance deployment options · Cloudflare Reference Architecture docs</a></li>
<li><a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies - Cloudflare Zero Trust</a></li>
</ul>
