<p>IPv6 (beta) for Magic Transit allows customers with existing IPv4 tunnels to enable and test IPv6 functionality with minimal configuration changes. This beta provides an opportunity to evaluate IPv6 addressing, routing, and security within Magic Transit while maintaining the existing IPv4 setup.</p>
<p>As this is a beta release, we encourage customers to contact their account team to enable the feature and provide feedback to help refine the IPv6 functionality before general availability.</p>
<h2 id="cloudflare-support-for-ipv6-in-magic-transit">Cloudflare support for IPv6 in Magic Transit</h2>
<p>Cloudflare transports IPv6 traffic over an IPv6-over-IPv4 GRE tunnel. Here is how it works:</p>
<ol>
<li>The IPv6 packet is encapsulated into an IPv4 GRE packet, with the IP protocol field set to <code>47</code> (indicating it is a GRE packet) along with a GRE header.</li>
<li>The IPv4 packet header and GRE header are the additional headers (or encapsulation overhead) that ensure the correct routing of the IPv6 traffic.</li>
<li>On most routers that support this tunneling method, the tunnel mode is set to <code>gre</code>.</li>
</ol>
<p><img src="/assets/upstream/images/magic-transit/ipv6.png" alt="The IPv4 packet header and GRE header are the additional headers (or encapsulation overhead) that ensure the correct routing of the IPv6 traffic." /></p>
<h2 id="current-known-limitations">Current known limitations</h2>
<ul>
<li>The IPv6 beta is not available for accounts with CNI (Cloudflare Network Interconnect) links configured.</li>
<li>MTU (Maximum Transmission Unit) is 1,420 bytes for egress traffic (does not impact Direct Server Return).</li>
<li>Cloudflare Network Firewall supports two matching fields for IPv6 traffic: source IP address and destination IP address.</li>
<li>Cloudflare supports the advertisement of IPv6 prefixes ranging from <code>/48</code> to <code>/32</code>.</li>
<li>Limited to IPv4-based <a href="/magic-transit/reference/tunnel-health-checks/">tunnel health checks</a> only.</li>
<li>Supports only IPv4-based endpoint health checks.</li>
</ul>
<h2 id="how-to-configure-ipv6">How to configure IPv6</h2>
<p>Since IPv6 works over an existing IPv4 tunnel, you need to select either an existing IPv4 GRE tunnel or create a new one to test IPv6. All settings that apply to the IPv4 GRE tunnel apply to the IPv6 tunnel as well, except for any MSS clamping you might need to configure — refer to <a href="#mss-clamping-recommendations">MSS clamping recommendations</a> in the following section for more information.</p>
<p>To test and set up IPv6 in the Cloudflare dashboard, complete one new field when creating a new IPv4 GRE tunnel or editing an existing one: <strong>IPv6 Interface address</strong>. Enter the Cloudflare-assigned IPv6 address for the Cloudflare side of the tunnel. Each tunnel is assigned a <code>/127</code> subnet from your allocated <code>/96</code> range. You configure one address on the Cloudflare side and the other address on your router.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10655.md")
</aside>
<p>To configure IPv6:</p>
<ol>
<li>Follow the instructions on how to <a href="/magic-transit/how-to/configure-tunnel-endpoints/#add-tunnels">add a GRE tunnel</a>.</li>
<li>In <strong>IPv6 Interface address</strong>, enter the IPv6 address assigned to you for the Cloudflare side of the tunnel. This address is one of the two addresses in the <code>/127</code> subnet allocated from your <code>/96</code> allocation.</li>
<li>Configure your router with the paired IPv6 address from the same <code>/127</code> subnet.</li>
</ol>
<h3 id="example">Example</h3>
<p>Your account has been assigned the prefix <code>2001:db8:abcd:1234::/96</code>.</p>
<p>In this example, the first two addresses in the range (<code>::0</code> and <code>::1</code>) are reserved for Cloudflare. You can use any of the remaining addresses in the <code>/96</code> block to create <code>/127</code> subnets for your tunnels.</p>
<p>If you decide to use the first available <code>/127</code> after the reserved addresses (<code>2001:db8:abcd:1234::2/127</code>), your configuration would be:</p>
<ul>
<li><strong>Cloudflare IPv6 Interface address</strong>: <code>2001:db8:abcd:1234::2</code></li>
<li><strong>Router IPv6 address</strong>: <code>2001:db8:abcd:1234::3</code></li>
</ul>
<p>Continuing with the example, the next <code>/127</code> for the second tunnel would be <code>2001:db8:abcd:1234::4/127</code>. Thus, your configuration would be:</p>
<ul>
<li><strong>Cloudflare IPv6 Interface address</strong>: <code>2001:db8:abcd:1234::4</code></li>
<li><strong>Router IPv6 address</strong>: <code>2001:db8:abcd:1234::5</code></li>
</ul>
<p>After the first two reserved addresses, you can continue allocating <code>/127</code> subnets sequentially (or in any order you prefer) for as many tunnels as needed until you reach the end of your <code>/96</code> range. Each <code>/127</code> contains exactly two IPv6 addresses — one for Cloudflare, one for your router.</p>
<h3 id="mss-clamping-recommendations">MSS clamping recommendations</h3>
<p>If you use Magic Transit ingress-only traffic (DSR), apply a TCP MSS (Maximum Segment Size) clamp with a maximum of 1,416 bytes to your edge router's transit ports to account for the larger IPv6 header.</p>
