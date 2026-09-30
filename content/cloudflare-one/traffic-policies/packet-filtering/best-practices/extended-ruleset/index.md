<p>The extended ruleset builds on the <a href="/cloudflare-one/traffic-policies/packet-filtering/best-practices/minimal-ruleset/">Minimal ruleset</a> by creating targeted rules for different types of systems on your network. Before creating these rules, you must <a href="/waf/tools/lists/custom-lists/#ip-lists">create IP lists</a> for each category.</p>
<p>If you are unable to export your current perimeter firewall rules, consider identifying categories of systems or user groups that reside on your Magic Transit prefixes. For example:</p>
<ul>
<li><a href="#endpoints-user-devices">Endpoints (user devices)</a></li>
<li><a href="#internal-routerfirewall-ip-addresses">Internal routers</a></li>
<li><a href="#web-servers">Web servers</a></li>
<li><a href="#non-web-servers">Non-web servers</a></li>
</ul>
<p>For each item above, consider the requirements in terms of their permitted Internet access. For example, permit what is required for legitimate traffic and block the rest.</p>
<h2 id="create-lists-for-using-cloudflare-network-firewall-rules">Create lists for using Cloudflare Network Firewall rules</h2>
<p>For more information on lists, refer to <a href="/cloudflare-one/reusable-components/use-rules-list/">Use rule lists</a>.</p>
<p>You can also create a list from the dashboard from <strong>Configurations</strong> &gt; <strong>Lists</strong> on your <strong>Account Home</strong>.</p>
<h2 id="endpoints-user-devices">Endpoints (User devices)</h2>
<p>Endpoint devices do not operate as servers, which means:</p>
<ul>
<li>They receive traffic from standard common ports — for example <code>80</code> or <code>443</code> — towards their ephemeral ports (temporary ports assigned by the OS for outbound connections, typically above <code>32768</code> in modern operating systems).</li>
<li>Connections flow outwards, not inwards, and therefore do not receive unsolicited inbound TCP connections.</li>
<li>They typically only need client TCP and UDP, with no requirement for ingress ICMP.</li>
</ul>
<p>For example, you can create a list for the combination of generic client TCP and client UDP that allows external pings or traceroutes and a catchall rule for all other protocols and traffic.</p>
<p>Create a list named <strong>Endpoints</strong> and specify the list of endpoints or user IP addresses to reference within the rules.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6721.md")
</aside>
<h3 id="suggested-rules">Suggested rules</h3>
<p><strong>Rule ID</strong>: 1
<strong>Description</strong>: Allows return traffic (responses to outbound requests) to ephemeral ports while blocking unsolicited inbound connections. Blocks inbound SYN-only traffic (meaning SYN-ACKs are permitted).
<strong>Match</strong>: <code>ip.proto eq &quot;tcp&quot; and ip.dst in $endpoints and tcp.dstport in {32768..60999} and not (tcp.flags.syn and not tcp.flags.ack)</code>
<strong>Action</strong>: Allow</p>
<p><strong>Rule ID</strong>: 2
<strong>Description</strong>: Endpoints (clients) will receive traffic destined for ephemeral ports
<strong>Match</strong>: <code>ip.proto eq &quot;udp&quot; and ip.dst in $endpoints and udp.dstport in {32768..60999}</code>
<strong>Action</strong>: Allow</p>
<p><strong>Rule ID</strong>: 3
<strong>Description</strong>: Permits ICMP traffic to destination IP addresses in <code>$endpoints</code> list with ICMP Types:</p>
<ul>
<li>Type 0 = Echo Reply</li>
<li>Type 3 = Destination Unreachable</li>
<li>Type 11 = Time Exceeded</li>
</ul>
<p><strong>Match</strong>: <code>ip.proto eq &quot;icmp&quot; and ip.dst in $endpoints and (icmp.type eq 0 or icmp.type eq 3 or icmp.type eq 11)</code>
<strong>Action</strong>: Allow</p>
<p><strong>Rule ID</strong>: 10
<strong>Description</strong>: Otherwise deny all traffic to IP's in <code>$endpoints</code> list
<strong>Match</strong>: <code>ip.dst in $endpoints</code>
<strong>Action</strong>: Block</p>
<h2 id="internal-router-firewall-ip-addresses">Internal router/Firewall IP addresses</h2>
<p>Follow the best practices for internal routers or firewall interface IP addresses on your MT prefixes below.</p>
<ol>
<li>Create <a href="/waf/tools/lists/custom-lists/#ip-lists">an IP list</a>, <strong>Internal routers</strong> for example, with your IP addresses.</li>
<li>Block ICMP if it is not needed.</li>
<li>Permit GRE/ESP as needed if the devices have GRE/IPsec tunnels via the Internet.</li>
</ol>
<h3 id="suggested-rules-1">Suggested rules</h3>
<p><strong>Rule ID</strong>: 1
<strong>Description</strong>: Permit limited ICMP traffic inbound, including:</p>
<ul>
<li>Type 0 - Echo Reply</li>
<li>Type 3 - Destination Unreachable</li>
<li>Type 8 - Echo</li>
<li>Type 11 - Time Exceeded</li>
</ul>
<p><strong>Match</strong>: <code>ip.proto eq &quot;icmp&quot; and ip.dst in $internal_routers and ( (icmp.type eq 0 or icmp.type eq 3) or (icmp.type eq 11) or (icmp.type eq 8) )</code>
<strong>Action</strong>: Allow</p>
<p><strong>Rule ID</strong>: 2
<strong>Description</strong>: Block all other traffic destined to these IP addresses
<strong>Match</strong>: <code>ip.dst in $internal_routers</code>
<strong>Action</strong>: Block</p>
<h2 id="web-servers">Web Servers</h2>
<p>Web servers require careful consideration of necessary traffic flows. Traffic for the <strong>web server</strong> functionality is required in addition to traffic flows where the web server is acting as a client.</p>
<p>Where possible, permit the required destination IP addresses and ports for web servers and block everything else. Additional services, for example NTP/DNS, may be required along with the ports for the web traffic.</p>
<p>The following is an example of suggested rules, but you should only make changes based on your specific requirements. For example, if you are not proxied by Cloudflare Layer 7 protection and you expect traffic sourced from the web towards your web servers:</p>
<ol>
<li>Create <a href="/waf/tools/lists/custom-lists/#ip-lists">an IP list</a>, <strong>web servers</strong> for example, to list IP addresses for your web servers.</li>
<li>Permit traffic for the web server traffic inbound from the Internet.</li>
<li>Permit traffic for the infrastructure or client traffic flows from the Internet, for example DNS and NTP.</li>
<li>Block all other traffic destined for the web server IP addresses.</li>
</ol>
<h3 id="suggested-rules-2">Suggested rules</h3>
<p><strong>Rule ID</strong>: 1
<strong>Description</strong>: Allows inbound HTTP/S traffic from the Internet with SYN-only or ACK-only flag (not SYN/ACKs)
<strong>Match</strong>: <code>ip.proto eq &quot;tcp&quot; and tcp.srcport in {32768..60999} and ip.dst in $web_servers and tcp.dstport in {80 443} and not (tcp.flags.syn and tcp.flags.ack)</code>
<strong>Action</strong>: Allow</p>
<p><strong>Rule ID</strong>: 2
<strong>Description</strong>: Allows UDP replies for DNS and NTP to web servers
<strong>Match</strong>: <code>ip.dst in $web_servers and ip.proto eq &quot;udp&quot; and udp.srcport in {53 123} and udp.dstport in {1024..65535}</code>
<strong>Action</strong>: Allow if necessary but Disable if under attack</p>
<p><strong>Rule ID</strong>: 3
<strong>Description</strong>: Catch-all to block all other traffic destined for web server IP addresses
<strong>Match</strong>: <code>ip.dst in $web_servers</code>
<strong>Action</strong>: Block</p>
<p>Alternatively, if you have Cloudflare Layer 7 protection, the Cloudflare public IP addresses can be permitted as the source IP addresses to the destination IP addresses for the HTTP/HTTPS inbound traffic. This recommendation effectively replaces Rule 1 in the example above.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6720.md")
</aside>
<h3 id="suggested-rules-for-cloudflare-proxied-traffic">Suggested rules for Cloudflare proxied traffic</h3>
<p><strong>Description</strong>: Allow inbound HTTP/S traffic from Cloudflare with SYN or ACK
<strong>Match</strong>: <code>ip.proto eq &quot;tcp&quot; and ip.dst in $web_servers and tcp.dstport in {80 443} and not (tcp.flags.syn and tcp.flags.ack) and ip.src in {173.245.48.0/20 103.21.244.0/22 103.22.200.0/22 103.31.4.0/22 141.101.64.0/18 108.162.192.0/18 190.93.240.0/20 188.114.96.0/20 197.234.240.0/22 198.41.128.0/17 162.158.0.0/15 104.16.0.0/13 104.24.0.0/14 172.64.0.0/13 131.0.72.0/22}</code>
<strong>Action</strong>: Allow</p>
<h2 id="non-web-servers">Non-web servers</h2>
<p>Restrict the source based on whether the server is expecting traffic from the general Internet or from only specific users.</p>
<ol>
<li>Apply rules based on source IP or ports if possible.</li>
<li>Restrict permitted destination ports to only those that are required.</li>
<li>Block incoming SYN to the closed ports.</li>
</ol>
<h3 id="suggested-rules-3">Suggested rules</h3>
<ul>
<li><code>IP Destination Address { non-web server } and TCP dst port in \&lt;valid ports&gt; — Permit</code></li>
<li><code>IP Destination Address { non-web server } and UDP dst port in \&lt;valid ports&gt; — Permit</code></li>
<li><code>IP Destination Address { web server } — Block</code></li>
</ul>
