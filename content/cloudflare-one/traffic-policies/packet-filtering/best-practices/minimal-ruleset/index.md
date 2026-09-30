<p>The suggested minimal ruleset blocks some known common vectors for DDoS attacks and permits all other ESP (Encapsulating Security Payload, used in IPsec VPNs), TCP, UDP, GRE (Generic Routing Encapsulation, used for tunnels), and ICMP traffic.</p>
<p>This is a suggested list and not an exhaustive list. Check which ports and protocols your infrastructure uses (for example, VPN, NTP, or database services) and ensure they are not blocked by these rules.</p>
<h2 id="recommended-rules">Recommended rules</h2>
<p><strong>Rule ID</strong>: 1 <br/>
<strong>Description</strong>: Single rule that blocks all traffic with UDP source ports which are used in attacks or invalid in Magic Transit ingress. <br/>
<strong>Match</strong>: <code>(udp.srcport in {1900 11211 389 111 19 1194 3702 10001 20800 161 162 137 27005 520 0})</code> <br/>
<strong>Action</strong>: Block <br/></p>
<p><strong>Rule ID</strong>: 2 <br/>
<strong>Description</strong>: Blocks TCP traffic with source port <code>0</code> and common ports used in TCP SYN/ACK reflection attacks (attacks that exploit TCP handshake responses to flood a target). <br/>
<strong>Match</strong>: <code>(tcp.srcport in {21 0 3306})</code> <br/>
<strong>Action</strong>: Block <br/></p>
<p><strong>Rule ID</strong>: 3 <br/>
<strong>Description</strong>: Blocks HOPOPT (Hop-by-Hop Options, IP protocol 0), which has no legitimate use in most environments, and blocks any protocol that is not ESP, TCP, UDP, GRE, or ICMP. Permit the relevant protocols for your environment.<br/>
<strong>Match</strong>: <code>(ip.proto eq &quot;hopopt&quot;) or (not ip.proto in {&quot;esp&quot; &quot;tcp&quot; &quot;udp&quot; &quot;gre&quot; &quot;icmp&quot;})</code> <br/>
<strong>Action</strong>: Block <br/></p>
<p>These rules are also available as <a href="/cloudflare-one/traffic-policies/packet-filtering/enable-managed-rulesets/">managed rules</a> that you can enable without manual configuration. The rules above are provided for reference and customization.</p>
<h2 id="traffic-and-port-types">Traffic and port types</h2>
<p>The information below covers traffic type, how the port is used, and reasons for blocking the port.</p>
<table>
<thead>
<tr>
<th>Traffic</th>
<th>Port use</th>
<th>Reason to block</th>
</tr>
</thead>
<tbody>
<tr>
<td>UDP source port <code>0</code></td>
<td>Reserved port. Should not be used by applications.</td>
<td>Invalid as a legitimate traffic source port. Commonly used in DDoS attacks.</td>
</tr>
<tr>
<td>UDP source port <code>1900</code></td>
<td>Simple Service Discovery Protocol (SSDP). Allows universal plug and play devices to send and receive information.</td>
<td><a href="https://www.cloudflare.com/learning/ddos/ssdp-ddos-attack/">SSDP DDoS attacks</a> exploit Universal Plug and Play protocols.</td>
</tr>
<tr>
<td>UDP source port <code>11211</code></td>
<td>Memcached. A database caching system designed to speed up websites and networks.</td>
<td><a href="https://www.cloudflare.com/learning/ddos/memcached-ddos-attack/">Memcached DDoS Attacks</a>.</td>
</tr>
<tr>
<td>UDP source port <code>389</code></td>
<td>Connection-less Lightweight Directory Access Protocol (CLDAP).</td>
<td><a href="https://blog.cloudflare.com/reflections-on-reflections/">Used in reflection attacks</a>.</td>
</tr>
<tr>
<td>UDP source port <code>111</code></td>
<td>SunRPC</td>
<td>Common attack vector. <a href="https://blog.cloudflare.com/reflections-on-reflections/">Used in reflection attacks</a>.</td>
</tr>
<tr>
<td>UDP source port <code>19</code></td>
<td>CHARGEN</td>
<td><a href="https://blog.cloudflare.com/memcrashed-major-amplification-attacks-from-port-11211/">Amplification attack vector</a>.</td>
</tr>
<tr>
<td>UDP source port <code>1194</code></td>
<td>OpenVPN</td>
<td>Unless this is an authorized VPN in your environment, this common VPN should be blocked.</td>
</tr>
<tr>
<td>UDP source port <code>3702</code></td>
<td>Web Services Dynamic Discovery Multicast discovery protocol (WS-Discovery)</td>
<td>Vulnerable to exploiting for DDoS attacks.</td>
</tr>
<tr>
<td>UDP source port <code>10001</code></td>
<td>Ubiquiti UniFi discovery protocol</td>
<td>Ubiquiti devices were exploited and used to conduct DDoS attacks on this port.</td>
</tr>
<tr>
<td>UDP source port <code>20800</code></td>
<td>Call of Duty</td>
<td><a href="https://blog.cloudflare.com/reflections-on-reflections/">Commonly used in attacks</a>.</td>
</tr>
<tr>
<td>UDP source ports <code>161</code> and <code>162</code></td>
<td>SNMP</td>
<td>Vulnerable to exploiting for DDoS attacks.</td>
</tr>
<tr>
<td>UDP source port <code>137</code></td>
<td>NetBIOS</td>
<td>NetBIOS allows file sharing over networks. If configured improperly, can expose file systems.</td>
</tr>
<tr>
<td>UDP source port <code>27005</code></td>
<td>SRCDS</td>
<td>Used in <a href="https://blog.cloudflare.com/reflections-on-reflections/">amplication attacks</a>.</td>
</tr>
<tr>
<td>UDP source port <code>520</code></td>
<td>Routing Information Protocol (RIP)</td>
<td>Internal routing protocol. Not required on Internet WAN access.</td>
</tr>
<tr>
<td>TCP source port <code>0</code></td>
<td>Reserved port. Should not be used by applications.</td>
<td>Commonly used in DDoS attacks. Invalid as a legitimate traffic source port.</td>
</tr>
<tr>
<td>TCP source port <code>21</code></td>
<td>FTP</td>
<td>Commonly used for attacks.</td>
</tr>
<tr>
<td>TCP source port <code>3306</code></td>
<td>MYSQL open source database</td>
<td>Used as attack vector in DDoS attacks.</td>
</tr>
</tbody>
</table>
<h2 id="other-common-traffic-to-consider">Other common traffic to consider</h2>
<p>The list below is a common list of traffic types you should also consider blocking or restricting inbound.</p>
<ul>
<li>SFTP, TFTP</li>
<li>SSH, Telnet</li>
<li>RDP</li>
<li>RCP</li>
<li>SMCP</li>
<li>NTP
<ul>
<li>Common vector for reflection attacks. Consider using <a href="/cloudflare-one/traffic-policies/">Cloudflare One traffic policies</a>, <a href="/1.1.1.1/">1.1.1.1's DNS over HTTPS (DoH)</a>, or an internal DNS service if possible. Consider restricting your firewall rules to only allow the source and destination of DNS traffic.</li>
</ul>
</li>
<li>MS-SQL
<ul>
<li>Common vector and <a href="https://blog.cloudflare.com/ddos-attack-trends-for-2021-q4/">increasingly used as vector for DDoS attacks</a>. Block if unused or consider restricting only to the required source IP addresses.</li>
</ul>
</li>
<li>HTTP and HTTPS
<ul>
<li>If you only have servers on your Magic Transit prefixes, consider blocking ingress traffic on TCP source ports 80 and 443 from outside. If you have endpoints on your Magic Transit prefixes, you can allow traffic on the source ports but consider creating a disabled rule you can activate to respond to reflection attacks as needed.</li>
</ul>
</li>
</ul>
<p>If relevant to your environment, consider blocking based on geolocation data, which blocks traffic based on the country or user when an end user's IP address is registered in the geolocation database.</p>
<p>If you are interested in participating in the beta for <a href="https://blog.cloudflare.com/programmable-packet-filtering-with-magic-firewall/">Session Initiation Protocol (SIP) Validation</a>, contact your Implementation Manager.</p>
