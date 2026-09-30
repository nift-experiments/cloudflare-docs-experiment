<p>Because Cloudflare WAN wraps your traffic in additional headers (encapsulation), the effective space available for your original data in each packet is reduced. If you do not account for this overhead, packets may be too large for the network path and will be dropped or fragmented — leading to performance loss or failed connections. This page explains the two key values you need to configure: maximum transmission unit (MTU) and maximum segment size (MSS).</p>
<h2 id="mtu-and-mss">MTU and MSS</h2>
<p>The <a href="https://www.cloudflare.com/learning/network-layer/what-is-mtu/">maximum transmission unit (MTU)</a> is a measurement representing the largest data packet that a network-connected device will accept. The MTU almost always applies to Layer 3 of the Open Systems Interconnection (OSI) model in networking and includes the entire packet, including all headers (Transmission Control Protocol (TCP), Internet Protocol (IP), etc.) and the data (payload) itself. For example, packets must not exceed 1,500 bytes to route through the Internet.</p>
<p>The <a href="https://www.cloudflare.com/learning/network-layer/what-is-mss/">maximum segment size (MSS)</a> refers to the amount of data that you can send in a single TCP datagram packet. You determine this value by subtracting the size of the IP and TCP headers from the MTU, which instructs the router how large the payload can be. It applies to Layer 4 of the OSI model in networking.</p>
<p>One common misconception about MSS/MTU is that setting these values negatively impacts performance. While there is a slight performance penalty, it is worse not to configure these values to account for the specificities of your network.</p>
<h2 id="encapsulation">Encapsulation</h2>
<p>Since Cloudflare WAN uses encapsulation to deliver its services, it is also important to understand why MTU and MSS matter in this case.</p>
<p>Encapsulation adds bytes to the packet because Cloudflare adds a new IP header and (often) some sort of encapsulating header to every packet. For example, in the case of Generic Routing Encapsulation (GRE) for Internet Protocol version 4 (IPv4), encapsulation adds 24 bytes — 20 bytes for the IPv4 header and 4 bytes for the GRE tunnel header.</p>
<p>A network interface that performs GRE encapsulation needs to account for the added overhead by reducing its MTU. Since the MTU maximum size is 1,500 bytes, for IPv4 this means the MTU becomes 1,476 bytes (the original 1,500 bytes minus the 24 bytes from the GRE encapsulation). This reduced MTU defines the maximum size of the IP packet that GRE can encapsulate.</p>
<h2 id="fragmentation">Fragmentation</h2>
<p>If the data packet is larger than what the network interface can accept, the network must either drop or fragment it into smaller packets. When fragmentation occurs, Cloudflare only accepts data packets that it can completely reassemble. If some fragments are missing, Cloudflare discards all received fragments. Cloudflare does not forward incomplete packets to the customer.</p>
<p>Setting the do not fragment (DF) bit in the TCP header to <code>1</code> denotes that the network must drop the packet rather than fragment it if the packet is larger than the MTU that intermediary network devices can accept. Most TCP implementations set the DF bit to <code>1</code> to avoid the potential issues that fragmentation causes.</p>
<p>If you experience issues with fragmentation and cannot set an MSS clamp, Cloudflare can clear the DF bit for you. When you enable this option, Cloudflare fragments packets greater than 1,500 bytes, and your infrastructure reassembles the packets after decapsulation. Use this as a last resort option. Contact your account team for more information.</p>
<h3 id="fragmentation-in-cloudflare-wan">Fragmentation in Cloudflare WAN</h3>
<p>Consider a UDP datagram of size 3,000 bytes (8 bytes for the UDP header + 2,992 bytes for the UDP data). To fit within a standard 1,500-byte MTU, this UDP datagram would be fragmented across three IP packets as follows:</p>
<p><img src="/assets/upstream/images/magic-transit/mtu-mss/udp-datagram.png" alt="A diagram showing a UDP datagram and its various components." /></p>
<p>Suppose that the UDP datagram has source port <code>389</code> and is destined for a Cloudflare WAN customer IP address. Suppose also that the Cloudflare WAN customer has a firewall rule in place that drops UDP traffic with source port <code>389</code>, a common <a href="https://blog.cloudflare.com/reflections-on-reflections">Connectionless Lightweight Directory Access Protocol (CLDAP)</a> reflection attack vector.</p>
<p>The three preceding packet fragments will arrive at Cloudflare, but only the first fragment contains a UDP header with source port information. The second and third fragments contain UDP data but do not have UDP header information.</p>
<p>So the question is: which of these fragments does Cloudflare drop and which does it deliver to the customer? If Cloudflare only drops the first parts of fragmented packets, the remaining parts could still generate a large amount of traffic during a Denial of Service (DoS) attack.</p>
<h3 id="how-cloudflare-handles-fragments">How Cloudflare handles fragments</h3>
<p>The following diagram shows how the three UDP fragments in the preceding example flow through Cloudflare and Cloudflare WAN. The main takeaways are:</p>
<ul>
<li><strong>Cloudflare never sends incomplete packets to customers</strong>: If Cloudflare does not see all parts of a packet required to fully reassemble that packet, Cloudflare will not send the partial data fragments to the customer.</li>
<li><strong>Cloudflare Network Firewall operates on fully reassembled packets, not individual fragments</strong>: This means that filters that match on UDP/TCP header information, for example, apply to the fully reassembled packet, not just the initial fragment. Cloudflare will not leak non-initial fragments to customers.</li>
<li><strong>Customers can still see fragmented packets</strong>: By default (without <code>clear_dont_fragment_bit</code> set), Cloudflare fragments packets to fit within the configured MTU of the tunnel before sending the data to the customer. If a packet is larger than 1,476 bytes, Cloudflare will fragment it and send those fragments to the customer for reassembly.</li>
</ul>
<p>In all cases, Cloudflare sends all fragments to the customer.</p>
<p><img src="/assets/upstream/images/magic-transit/mtu-mss/fragmentation.png" alt="A diagram showing how Cloudflare handles fragmentation." /></p>
<h2 id="mss-clamping">MSS clamping</h2>
<p>Maximum segment size (MSS) is a TCP setting that limits the size of TCP segments. The SYN packets set this option during the three-way handshake.</p>
<p>By default, a TCP endpoint sets its MSS value based on its local network interface MTU. For example, for IPv4, if the MTU is 1,500 bytes then MSS becomes 1,460 bytes (1,500 bytes minus 20 bytes from the IPv4 header minus 20 bytes from the TCP header).</p>
<p>MSS is a tool that you can use to configure TCP packet size behavior. If a TCP endpoint sits behind a network with reduced MTU, changing the MSS value to match the actual path MTU value forces remote endpoints to send packets that fit within the specified MTU. So, if an IPv4 TCP endpoint sits behind a GRE tunnel with an MTU of 1,476 bytes, the MSS value in its TCP SYN packets should be 1,436 bytes - 1,476 bytes minus the 20 bytes from the IPv4 header, minus the 20 bytes from the TCP header.</p>
<p>One way to modify the MSS setting is by changing the MTU of the network interface in the router's WAN interface to match the path MTU. Another way to modify MSS is by applying an MSS clamp, where you configure an intermediary network device - such as a router - to modify the MSS TCP option on-the-fly when packets pass through it. Note that changing the MTU on the interface of an intermediary network device is not the same as applying an MSS clamp, and it does not change the TCP MSS value.</p>
<p>Refer to <a href="#mss-clamping-recommendations">MSS clamping recommendations</a> for information on what you should set your MSS clamping to, depending on the type of tunnel.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5555.md")
</aside>
<h2 id="mss-clamping-recommendations">MSS clamping recommendations</h2>
<h3 id="gre-tunnels-as-off-ramp">GRE tunnels as off-ramp</h3>
<p>The MSS value depends on how your network is set up.</p>
<ul>
<li><strong>On your edge router</strong>: Apply the clamp to the GRE tunnel internal interface (meaning where the egress traffic will traverse). Set the MSS clamp to 1,436 bytes. Your devices may do this automatically once the tunnel is configured, but it depends on your devices.</li>
</ul>
<h3 id="ipsec-tunnels">IPsec tunnels</h3>
<p>For IPsec tunnels, the value you need to specify depends on how your network is set up. The MSS clamping value is lower than for GRE tunnels because the physical interface sees IPsec-encrypted packets, not TCP packets, and MSS clamping does not apply to those.</p>
<ul>
<li><strong>On your edge router</strong>: Apply this on your IPsec tunnel internal interface (meaning where the egress traffic will traverse). Your devices may do this automatically once the tunnel is configured, but it depends on your devices. Set the TCP MSS clamp to 1,360 bytes maximum.</li>
</ul>
