<p>A key benefit of routing your network traffic through Cloudflare is that you can apply security policies without deploying additional hardware at each site. Once traffic reaches Cloudflare through WAN on-ramps (IPsec tunnels, GRE tunnels, CNI, or Appliance), multiple security services inspect it inline at the nearest Cloudflare data center. This page explains which services apply to WAN traffic, when to use each one, and how they work together.</p>
<h2 id="traffic-types">Traffic types</h2>
<p>Cloudflare WAN carries three types of traffic, and different security services apply to each:</p>
<ul>
<li><strong>Outbound (site-to-Internet)</strong>: Traffic from WAN-connected sites to the public Internet. For example, employees at a branch office browsing the web or accessing SaaS applications.</li>
<li><strong>East-west (site-to-site)</strong>: Traffic between WAN-connected locations routed through Cloudflare. For example, a branch office accessing an application hosted in a data center.</li>
<li><strong>Inbound (Internet-to-site)</strong>: Traffic from the Internet destined for customer networks. This typically applies to <a href="/magic-transit/">Magic Transit</a> scenarios where you advertise your own IP prefixes (BYOIP) through Cloudflare.</li>
</ul>
<h2 id="security-services">Security services</h2>
<h3 id="cloudflare-network-firewall">Cloudflare Network Firewall</h3>
<p><a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> provides packet-level filtering at layers 3 and 4. You define allow or block rules based on IP addresses, ports, and protocols.</p>
<ul>
<li><strong>Applies to</strong>: inbound, outbound, and east-west traffic</li>
<li><strong>Included with</strong>: Cloudflare WAN by default for <a href="/cloudflare-network-firewall/plans/">standard features</a></li>
</ul>
<p>Use Network Firewall when you need to control traffic at the packet level — for example, blocking specific IP ranges, restricting traffic to certain ports, or filtering protocols between sites.</p>
<h3 id="gateway-secure-web-gateway">Gateway (Secure Web Gateway)</h3>
<p><a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> inspects traffic at layers 4 through 7 and supports three policy types:</p>
<ul>
<li><strong>DNS policies</strong>: Filter and log DNS queries from your sites. You configure the DNS resolver for your WAN networks to point to Gateway's resolver IPs.</li>
<li><strong>Network policies</strong>: Filter TCP, UDP, and ICMP traffic based on IP, port, protocol, and identity attributes.</li>
<li><strong>HTTP policies</strong>: Inspect HTTP and HTTPS traffic for threats, content categories, and application-level controls.</li>
</ul>
<p>HTTP inspection requires TLS decryption and a Cloudflare root certificate installed on client devices. You must also enable the Gateway proxy for your WAN traffic.</p>
<ul>
<li><strong>Applies to</strong>: outbound and east-west traffic</li>
</ul>
<p>Gateway provides the deepest inspection for WAN traffic, covering DNS, network, and HTTP layers. For detailed setup instructions, refer to <a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Connect to Cloudflare Gateway with Cloudflare WAN</a>.</p>
<h3 id="browser-isolation">Browser Isolation</h3>
<p><a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> runs web content in a remote browser on Cloudflare's network and streams a visual representation to the user's device. No web code executes locally.</p>
<ul>
<li><strong>Applies to</strong>: outbound web traffic</li>
<li><strong>Triggered by</strong>: Gateway HTTP policies using the <strong>Isolate</strong> action</li>
</ul>
<p>Use Browser Isolation when users at branch offices need to access untrusted or uncategorized websites without exposing local devices to web-based threats.</p>
<h3 id="data-loss-prevention-dlp">Data Loss Prevention (DLP)</h3>
<p><a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention (DLP)</a> scans HTTP uploads and downloads for sensitive data patterns such as Social Security numbers, credit card numbers, and custom regular expressions.</p>
<ul>
<li><strong>Applies to</strong>: outbound HTTP traffic</li>
<li><strong>Requires</strong>: Gateway HTTP filtering with TLS decryption enabled</li>
</ul>
<p>You define DLP profiles with detection rules and reference those profiles in Gateway HTTP policies. When a policy matches, Gateway can block, log, or allow the transfer.</p>
<h3 id="cloud-access-security-broker-casb">Cloud Access Security Broker (CASB)</h3>
<p><a href="/cloudflare-one/cloud-and-saas-findings/">CASB</a> provides visibility and control over SaaS application usage through two modes:</p>
<ul>
<li><strong>Applies to</strong>: outbound traffic to SaaS applications</li>
<li><strong>API-based scanning</strong>: Connects to your SaaS applications (Google Workspace, Microsoft 365, and others) to detect misconfigurations and security posture issues.</li>
<li><strong>Inline remediation</strong>: Gateway HTTP policies can block unsanctioned SaaS application usage detected by CASB — for example, preventing file uploads to unapproved cloud storage services.</li>
</ul>
<h3 id="ai-visibility">AI visibility</h3>
<p>The <a href="/cloudflare-one/insights/analytics/ai-security/">AI Security Report</a> provides visibility into AI application usage across your organization. It shows which AI tools employees are using, how frequently, and what data is being shared.</p>
<p>AI visibility is not a separate inline security service. It is an analytics feature powered by Gateway — it requires Gateway to be inspecting outbound traffic from your sites.</p>
<h2 id="use-case-mapping">Use-case mapping</h2>
<table>
<thead>
<tr>
<th>Traffic scenario</th>
<th>Recommended services</th>
</tr>
</thead>
<tbody>
<tr>
<td>Block traffic between sites by IP, port, or protocol</td>
<td>Network Firewall</td>
</tr>
<tr>
<td>Filter DNS queries from branch offices</td>
<td>Gateway DNS policies</td>
</tr>
<tr>
<td>Block malware downloads from branch offices</td>
<td>Gateway HTTP policies</td>
</tr>
<tr>
<td>Prevent sensitive data uploads to the Internet</td>
<td>DLP (via Gateway HTTP policies)</td>
</tr>
<tr>
<td>Isolate risky web browsing from branch users</td>
<td>Browser Isolation (via Gateway HTTP policies)</td>
</tr>
<tr>
<td>Detect and block unsanctioned SaaS applications</td>
<td>CASB + Gateway HTTP policies</td>
</tr>
<tr>
<td>Monitor employee AI tool usage</td>
<td>AI Security Report (via Gateway)</td>
</tr>
<tr>
<td>Protect against DDoS on customer-owned IPs</td>
<td>Network Firewall (inbound) + <a href="/magic-transit/">Magic Transit</a></td>
</tr>
</tbody>
</table>
<h2 id="how-services-compose">How services compose</h2>
<p>Traffic on the Cloudflare network passes through a single-pass inspection pipeline. You do not need to backhaul traffic between services — all inspection happens at the nearest Cloudflare data center.</p>
<p>The evaluation order is:</p>
<ol>
<li><strong>Network Firewall (L3/L4)</strong>: Packet-level rules are evaluated first.</li>
<li><strong>Gateway (L4-L7 proxy)</strong>: If traffic passes the Network Firewall, Gateway inspects it. Within Gateway, policies are evaluated in order: DNS → Network → HTTP.</li>
<li><strong>DLP, Browser Isolation, and CASB</strong>: These services are triggered through Gateway HTTP policies. A single HTTP policy can reference a DLP profile, apply an Isolate action, or block a CASB-flagged application.</li>
</ol>
<p>This means you can layer multiple security services on the same traffic flow without adding network hops or latency.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Connect to Cloudflare Gateway with Cloudflare WAN</a>: Detailed setup guide for Gateway integration with WAN traffic.</li>
<li><a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a>: Configure packet-level filtering rules.</li>
<li><a href="/reference-architecture/architectures/sase/">SASE reference architecture</a>: Explore the full architecture of Cloudflare One as a SASE platform.</li>
<li><a href="/cloudflare-wan/wan-transformation/">WAN transformation</a>: Plan your migration from traditional WAN to Cloudflare.</li>
</ul>
