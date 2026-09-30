<div class="nb-description">
@markup("md", "content/.markup/bodies/704.md")
</div>
<div class="nb-plan">
<p>Enterprise-only</p>
</div>
<p>Cloudflare Network Interconnect (CNI) allows you to connect your network infrastructure directly to Cloudflare — rather than using the public Internet — for a more performant and secure experience. With CNI, you can bring Cloudflare's full suite of network functions to your network edge.</p>
<h2 id="benefits">Benefits</h2>
<p>Enterprises use CNI to achieve:</p>
<ul>
<li><strong>Enhanced Performance</strong>: Gain lower latency and more consistent network throughput.</li>
<li><strong>Increased Security</strong>: Reduce your network's attack surface by connecting privately and avoiding the public Internet.</li>
</ul>
<h2 id="connection-types">Connection types</h2>
<p>Choose the connection type for your infrastructure and operational needs.</p>
<table>
<thead>
<tr>
<th></th>
<th>Direct Interconnect</th>
<th>Partner Interconnect</th>
<th>Cloud Interconnect</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Port type</strong></td>
<td>A dedicated physical fiber connection between your network equipment and Cloudflare's hardware in a shared data center.</td>
<td>A virtual connection to Cloudflare established through one of our global connectivity partners.</td>
<td>A private connection between a customer's cloud environments (for example, Amazon Web Services (AWS), Google Cloud) and Cloudflare.</td>
</tr>
<tr>
<td><strong>Operations</strong></td>
<td>You are responsible for procuring and managing the physical cross-connect to Cloudflare's equipment.</td>
<td>Your partner manages the connection logistics, often through a software-defined networking portal.</td>
<td>Cloudflare connects to cloud providers' dedicated services, and customers establish private virtual circuits from their virtual private clouds.</td>
</tr>
<tr>
<td><strong>Ideal use case</strong></td>
<td>For customers collocated with Cloudflare who require maximum control, performance, and reliability.</td>
<td>For customers who are not in the same data center as Cloudflare or prefer a managed connectivity solution.</td>
<td>For customers with workloads in public clouds who need secure, reliable connectivity to Cloudflare services.</td>
</tr>
</tbody>
</table>
<h2 id="dataplane">Dataplane</h2>
<p>Cloudflare's data centers may support one or more interconnect dataplanes. The dataplane is the type of equipment that terminates your direct connection:</p>
<ul>
<li><strong>Dataplane v1</strong>: A peering connection to a Cloudflare edge data center that supports Generic Routing Encapsulation (GRE) tunnels for connecting with the Cloudflare Virtual Network, with optional GRE-less delivery for Magic Transit Direct Server Return.</li>
<li><strong>Dataplane v2</strong>: Is based on the Customer Connectivity Router (CCR), which is specifically designed for customer connectivity. It provides simplified routing without GRE tunneling and supports a 1,500-byte Maximum Transmission Unit (MTU) bidirectionally.</li>
</ul>
<p>When you review the <a href="/network-interconnect/locations/">available locations</a>, you can see which dataplane version(s) are available.</p>
<h2 id="product-use-cases">Product use cases</h2>
<p>CNI provides a private point-to-point IP connection with Cloudflare. There are two Dataplanes that come with different technical specifications.</p>
<table>
<thead>
<tr>
<th></th>
<th>Dataplane v1</th>
<th>Dataplane v2</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Magic Transit Direct Server Return (DSR)</strong> <br /> Distributed Denial of Service (DDoS) protection for all ingress traffic from the Internet to your public network. Send egress traffic via your ISP.</td>
<td>Supported with or without a GRE tunnel established over the interconnect circuit.</td>
<td>Supported.</td>
</tr>
<tr>
<td><strong>Magic Transit with Egress</strong> <br /> DDoS protection for all ingress traffic from the Internet to your public network. Send egress traffic via Cloudflare.</td>
<td>Supported with a GRE tunnel established over the interconnect circuit.</td>
<td>Supported.</td>
</tr>
<tr>
<td><strong>Cloudflare WAN and Zero Trust</strong>  <br /> Build a secure, private network backbone connecting your Zero Trust users and applications with all your sites, data centers, and clouds.</td>
<td>Supported with a GRE tunnel established over the interconnect circuit.</td>
<td>Supported.</td>
</tr>
<tr>
<td><strong>Peering</strong> <br /> Exchange public routes with a single Cloudflare PoP (Point of Presence).</td>
<td>Supported. <br /><br /> All customers connecting with the edge data center will exchange public routes at that PoP with AS13335. Connectivity is established at each individual PoP. Routes for other edge locations in Cloudflare's network may not be available. Routes for customer-advertised prefixes will be available only in the connected PoP.</td>
<td>Not supported.</td>
</tr>
<tr>
<td><strong>Application Security and Performance</strong> <br /> Improve the performance and security of your web applications</td>
<td><strong>Supported via peering</strong>: Customers can use Argo Smart Routing to direct origin traffic via the edge peering connection when it is determined to be the lowest latency option. Customers must maintain a direct Internet connection which will always be used for a portion of traffic and during failure scenarios. <br /> <strong>Supported Via Magic Transit</strong>: Customers may configure any product with an origin server IP address that is protected by Magic Transit. Magic Transit will direct this traffic via the overlay and customer can control interconnect next-hops using the Magic Transit Virtual Network routing table.</td>
<td>When the origin IPs are behind Magic Transit over a CNI v2, all Cloudflare services that work with public origins (like Load Balancer, WAF, Cache) will run over the CNI.</td>
</tr>
</tbody>
</table>
<p>For more details refer to the <a href="/network-interconnect/get-started/#prerequisites">prerequisites section</a>.</p>
<h3 id="designing-for-high-availability">Designing for high availability</h3>
<p>To protect against a single point of failure, it is critical to design your CNI deployment for resilience. For business-critical applications, seek Cloudflare locations that support diversity on the device level. This ensures your connections terminate on physically separate hardware.</p>
<p>Refer to <a href="/network-interconnect/get-started/#service-expectations">Service Expectations</a> for more information.</p>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/705.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/706.md")
</div>
